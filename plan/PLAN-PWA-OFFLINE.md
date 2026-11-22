# La PWA: la app sin conexión y la sincronización (v2)

> **Estado**: plan. La v1 no ha salido todavía; esto es la v2 del producto y
> se trabaja **en su propia rama**, sin tocar `develop`.
>
> **Issue con el detalle**: [`front#131`](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/131)
> **El carril**: `feat/issue-131-pwa` en `dolynation-tonatiuh-front`
> **Dependencia del backend**: [`back`](https://github.com/DolyLanguagesORG/dolynation-atl-back) (la idempotencia de `evaluate`)

---

## 1. Qué queremos (el propósito)

La app **genera historias**. El caso:

1. Generas una historia **con red**.
2. Te quedas **sin internet** (el túnel, el avión, el ascensor).
3. Entras en la app y **debes poder seguir con esa historia** como si nada:
   leerla, responderla, marcar el vocabulario.
4. Cuando vuelves a un lugar con red, **todo lo que hiciste se sube**.

Es el **modo offline de Duolingo**: no una PWA de adorno.

---

## 2. Qué es esto exactamente (dos cosas, no una)

| | Qué es | Qué aporta | Dificultad |
| --- | --- | --- | --- |
| **1. PWA** | Manifest + service worker | Poder **instalarla** (icono en la pantalla de inicio, sin barra de navegador) | 🟢 Baja |
| **2. Local-first / offline-first** | Los datos **en el dispositivo** + sincronización | **Funcionar sin red** y que lo que hiciste **se suba al volver** | 🔴 **Alta** |

> **Una PWA no implica offline.** Se puede tener una PWA que solo se instala y
> que sin red no hace nada (es lo más común). Lo que hacemos aquí es la parte
> difícil: **mover los datos al cliente**.

**Los nombres de las piezas** (por si hay que buscarlos):

| Pieza | Se llama | Qué es |
| --- | --- | --- |
| Los datos en el dispositivo | **local-first** | La fuente de verdad es el dispositivo, no el servidor |
| La cola de lo pendiente | **outbox pattern** | Se escribe local y se sube al volver |
| Cómo decide el service worker | **network-first / cache-first** | HTML: red primero; assets: caché primero |
| Subir sin la app abierta | **Background Sync API** | Opcional (para vaciar la outbox con la app cerrada) |
| Dos dispositivos editando lo mismo | **last-write-wins** | El servidor manda (es el que evalúa con la IA) |

**Referencias**: Ink & Switch (*local-first software*), PouchDB/CouchDB (el
offline-first de manual), PowerSync. Duolingo es un ejemplo de producto, no
de implementación.

---

## 3. La arquitectura

```
┌─ El dispositivo ────────────────────────────────────────────────┐
│  Service Worker                                                     │
│    ✅ cachea la SHELL (HTML, JS, CSS, iconos)                      │
│    ❌ NUNCA cachea /api/v1/** ni el HTML con datos de usuario       │
│                                                                       │
│  IndexedDB                                                           │
│    readings/{id} → el texto, el vocabulario, las traducciones        │
│    outbox       → lo que hiciste y aún no se ha subido              │
└───────────────────────────────────────────────────────────────────────┘
```

> **Lo que depende de quién eres no se "cachea": se guarda y se sincroniza.**
> El service worker no cachea datos del usuario: el **almacena localmente** y
> lo **sincroniza**.

| | Cachear (HTTP) | Guardar + sincronizar |
| --- | --- | --- |
| Qué guarda | La **respuesta del servidor** | **Tus datos**, en tu dispositivo |
| Dónde viven | La caché HTTP del navegador | **IndexedDB** |
| ¿Sirve offline? | Sí, pero es una **foto vieja** | **Sí, y es el que sigue vivo** |
| Riesgo | Que B vea los datos de A | **Ninguno**: cada uno tiene los suyos |
| Al volver la red | Se ignora | **Se sube lo que hiciste** |

### El ciclo

| Momento | Qué pasa |
| --- | --- |
| **Con red** | Generas la historia → la app **la guarda en IndexedDB** (texto + vocabulario). El SW guarda la shell. |
| **Sin red** | Entras a la app → el SW sirve la shell → el hook lee la historia **de IndexedDB** → **respondes igual, todo normal**. La respuesta y las acciones van a la **outbox**. |
| **Vuelve la red** | El sincronizador **vacía la outbox** contra la API, en orden. |

### Qué se puede hacer offline y qué no

| ✅ Offline (100% local) | 🔁 En cola (necesita red al final) |
| --- | --- |
| Leer la historia completa | **Enviar la respuesta** → la evalúa la IA en el servidor |
| Vocabulario, glosario, traducciones | Guardar una palabra en el glosario |
| Marcar, navegar, releer | La explicación profunda de una palabra (IA) |
| **Escribir** la respuesta | El "completado" de la lectura |

### La estrategia de caché, ruta por ruta

| Qué | Estrategia | Por qué |
| --- | --- | --- |
| HTML **autenticado** (`/history`, `/profile`, `/readings/*`, `/generate`) | **sin caché** (nunca, ni de respaldo) | Es el dato de otro |
| `/api/**` | **sin caché** | Datos del usuario |
| HTML **público** (`/`, `/login`, `/glossary`…) | **network-first**, con copia de respaldo | Contenido fresco; sin red, la copia |
| `_next/static/**`, iconos, fuentes | **cache-first** | Llevan hash: no cambian |
| Página **offline** | precacheada | Para abrir la app sin red |

> **El tercer bug clásico** (a evitar desde el principio): un SW que responde
> a *cualquier* navegación con el `index.html` cacheado → al abrir `/history`
> te pinta la portada. Con "network-first **por ruta**" no pasa.

---

## 4. Los 3 requisitos que no son opcionales

1. **El SW no cachea `/api/v1/**` ni el HTML autenticado.** La app de Next 16
   ya pone `no-store` en las páginas dinámicas: hoy el navegador **no** cachea
   ese HTML, y el estado de sesión va dentro. Cachearlo sería cachear datos
   de usuario.
2. **Al cerrar sesión se borra el IndexedDB.** Si no, en un dispositivo
   compartido el siguiente usuario encuentra las historias del anterior.
3. **La historia se descarga antes de perder la red.** Es el caso de este
   proyecto: "la generé con red y luego me quedé sin internet". → Botón
   **"Descargar para leer"** (o automático al abrirla).

---

## 5. El proceso de las ramas

```
                    ┌──────────────────── develop (la v1, intacta) ───────────────────┐
                    │                                                                   │
   otros trabajos ──┤                                                                   │
                    └──────────────┬────────────────────────────────────────────────────┘
                                   │  merge de develop → el carril (manual, para que el
                                   │  carril no se aleje de la v1)
                                   ▼
        ┌────────────────── feat/issue-131-pwa  (EL CARRIL, de larga vida) ───────────┐
        │                                                                                │
        │   PR 1a ← PR 1b ← PR 1c ← PR 1d ← PR 1e ← PR 1f ← PR 2 ← PR 3 ← PR 4        │
        │   (cada PR sale de una rama corta, vive en el carril y se mergea squash)      │
        │                                                                                │
        └────────────────────────────────────────────────────────────────────────────────┘
                                   │
                                   │  (al final, cuando esté lista: una decisión)
                                   ▼
                            PR  feat/issue-131-pwa → develop
```

| # | Regla | Por qué |
| --- | --- | --- |
| 1 | El carril sale de `develop` **ahora** y **no se borra** hasta que la PWA esté integrada | Es el "carril" de la v2 |
| 2 | **Cada cambio entra al carril por PR**, desde una rama corta (`feat/131-<que>`) | Nada se empuja directo al carril |
| 3 | Ruleset propia: push **bloqueado**, squash, **1 aprobación**, **7 checks** (`lint`, `typecheck`, **`unit`**, **`e2e`**, `build`, `pr-title`, `pr-target`) | El carril no se rompe nunca |
| 4 | **El CI corre en el carril** (si no, sus checks nunca reportan y cada PR queda bloqueado) | Sin CI, el carril es ciego |
| 5 | **`develop` se merges a mano** en el carril: `git merge develop` → PR al carril → merge | Es lo que se hace ahora; el workflow de sincronización, para después |
| 6 | **`develop` no se toca** hasta que la PWA esté lista | La v1 sigue su vida |
| 7 | El **PR del backend** (idempotencia) va a `develop` **normalmente** | Es una mejora del backend en sí misma |
| 8 | Al final: **PR `feat/issue-131-pwa` → `develop`** | Con la regla 5, el diff es **solo de la PWA** |

**Por qué merge y no rebase**: el rebase **reescribe** la historia de la rama
(cambian todos los SHA) y el diff final hacia `develop` sería ruidoso. Con
**merge**, `develop` queda dentro de la rama y la integración final es trivial.

**El bypass "Write"** de la ruleset del carril existe para que el bot de
sincronización (o un maintainer) pueda traer `develop` al carril sin
`--admin` en cada PR.

---

## 6. Las fases

| Fase | Qué | Repo | Rama | PR |
| --- | --- | --- | --- | --- |
| **0** | Issue + el carril + su ruleset + el CI en el carril + las reglas en `AGENTS.md` | front | `feat/131-carril` → carril | 1 |
| **1a** | **Idempotencia** en `POST /readings/:id/evaluate` y `/explanations` | **back** | `feat/131-idempotencia` → `develop` | 1 |
| **1b** | **IndexedDB**: `readings/{id}` + `outbox`; guardar la lectura; "Descargar para leer" | front | `feat/131-datos` → carril | 1 |
| **1c** | **El hook de lectura**: API → si falla, IndexedDB; el distintivo "sin conexión" | front | `feat/131-lectura-offline` → carril | 1 |
| **1d** | **El hook de evaluación**: si la API falla → outbox + "pendiente de enviar" | front | `feat/131-evaluacion-offline` → carril | 1 |
| **1e** | **El sincronizador**: al volver la red, vaciar la outbox (con la clave de idempotencia) | front | `feat/131-sync` → carril | 1 |
| **1f** | **La shell offline** + el modo offline de la app | front | `feat/131-shell-offline` → carril | 1 |
| **2** | **Installable**: `manifest.ts` (con i18n), iconos 192/512/maskable, `appleWebApp`, página offline | front | `feat/131-manifest` → carril | 1 |
| **3** | **Los tests**: unit + E2E | front | `feat/131-tests` → carril | 1 |
| **4** | **El CI de la PWA**: un job `pwa` → check requerido | front | `feat/131-ci-pwa` → carril | 1 |
| **5** | **La integración**: `feat/issue-131-pwa` → `develop` | front | — | 1 (futuro) |

**Orden**: la **1a** (backend) antes de la **1e** (sincronizador) — sin
idempotencia la outbox puede duplicar. La **2** es independiente y da
resultado visible rápido.

---

## 7. El punto delicado (y por qué la 1f va aparte)

> **Sin red, el servidor Next no existe.** La app se renderiza en el servidor;
> si no hay red, la navegación a `/readings/[id]` no llega a ningún sitio. Y el
> HTML de esa ruta **lleva el estado de sesión** y Next lo marca `no-store` a
> propósito.

La solución **no** es cachear ese HTML (sería cachear PII, y hoy Next lo
evita por diseño). Es: **una "shell offline" mínima** (un HTML estático con
el bundle) → la app arranca → detecta "sin red" → lee de IndexedDB → pinta la
lectura.

Por eso la 1f va en un PR aparte: es la parte que puede cambiar de
planteamiento, y no debe arrastrar a las demás.

---

## 8. Herramientas

| Opción | Estado | Veredicto |
| --- | --- | --- |
| `next-pwa` | v5.6.0, **parada desde 23-ago-2022** | ❌ abandonada |
| **`@serwist/next`** | v9.5.15, **modificada el 17-nov-2026**; pide `next >=14` (compatible con Next 16) | ✅ **la que se usa** |
| Workbox a mano (`public/sw.js`) | Workbox 7.4.1, vivo | ⚠️ reserva si `@serwist` no encaja |

La fase 2 va en un PR **aparte** de la fase 1 a propósito: si hay que cambiar
de librería, lo que ya está (manifest + iconos) se queda.

---

## 9. La dependencia del backend (y por qué no es opcional)

Para que la outbox pueda reenviar **sin duplicar**, la API tiene que ser
**idempotente**. Hoy:

| Endpoint | ¿Idempotente? |
| --- | --- |
| `POST /billing/...` | **Sí** — ya acepta la cabecera `idempotency-key` ✓ |
| **`POST /readings/:id/evaluate`** | **No** ← hay que añadirlo |
| `POST /readings/:id/explanations` (y `/deep`) | **No** ← hay que añadirlo |

Sin eso, un reintento de "evaluate" = la IA evalúa dos veces (cuesta dinero y
pisa el resultado).

La buena noticia: **el patrón ya existe en el billing** → es copiarlo
(cabecera + índice único + comprobación), no inventarlo.

---

## 10. Lo que NO se hace hasta que la PWA esté

- No se corta `site-rc-*` (la candidata del sitio).
- No se despliega a staging, rehearsal ni producción.
- No se mueve la app a `play.` (faltan los subdominios: `infra#259`).
- No se sube ninguna versión.
- **No se toca `develop`.**

---

## Referencias

| Qué | Dónde |
| --- | --- |
| La issue con el detalle | [`front#131`](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/131) |
| Los subdominios y `play.` | [`infra#259`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/259) |
| El apartado de lo pendiente | [`plan/PENDIENTES.md`](./PENDIENTES.md) |
| El flujo de release (el del sitio) | [`operations/FLUJO-DE-RELEASE.md`](../operations/FLUJO-DE-RELEASE.md) |
| El índice de bugs | [`plan/BUGS.md`](./BUGS.md) |
| Local-first (el artículo) | Ink & Switch — *Local-first software* |
| La librería del service worker | `@serwist/next` |
| El patrón de la cola | *outbox pattern* |
