# Plan y seguimiento

Este documento responde tres preguntas prácticas del equipo:

1. **¿En qué orden se trabaja?** (qué depende de qué)
2. **¿Cómo no se me pasan las fechas?** (qué revisar cada día y cada sprint)
3. **¿Cómo se monitorea y cómo se justifica un atraso?** (para el SM y para la
   revisión académica)

El plan vive en [`cronograma.md`](./cronograma.md) y el detalle operativo en
[`FLUJO-DE-TRABAJO.md`](../operations/FLUJO-DE-TRABAJO.md). Este documento es el puente
entre los dos.

## 1. Orden de trabajo (ruta crítica)

**Regla de oro:** dentro de un sprint hay libertad para paralelizar, pero **el
backend va antes que el frontend que lo consume**. Nada de conectar una vista
contra un endpoint que todavía no existe (salvo datos mock, que es válido para
avanzar en el maquetado).

Las dependencias están registradas en GitHub con la relación *blocked by*, así
que aparecen en la sección **Relationships** de cada issue y el tablero lo
refleja:

| Tarea de frontend | Bloqueada por (backend) |
| --- | --- |
| [front#3](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/3) — Login/registro | [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) |
| [front#4](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/4) — Perfil | [back#5](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/5) |
| [front#5](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/5) — Form de parámetros | [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8) |
| [front#7](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/7) — Flujo completo | [back#10](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/10) |
| [front#9](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/9) — Popup diccionario | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11) |
| [front#10](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/10) — Redacción de resumen | [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) |
| [front#11](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/11) — Dashboard | [back#15](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/15), [back#16](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/16) |
| [front#12](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/12) — Panel admin | [back#17](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/17) |
| [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13) — Usabilidad/responsivo | [front#11](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/11), [front#12](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/12) |

Dependencias internas de backend y schema:

| Tarea | Bloqueada por |
| --- | --- |
| [back#3](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/3) — Hash/JWT | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2) |
| [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) — Endpoints auth | [back#3](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/3) |
| [back#5](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/5) — Perfil | [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) |
| [back#6](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/6) — Cierre S1 | `back#2` a `back#5` |
| [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7) — IA/prompts | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2) |
| [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8) — Settings | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2), [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) |
| [back#9](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9) — Caché | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7), [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) |
| [back#10](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/10) — Generar lectura | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7), [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8), [back#9](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9), [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) |
| [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11) — Vocabulario/TTS | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7), [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) |
| [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12) — Motor PNL | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7) |
| [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) — Guardar evaluación | [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12), [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) |
| [back#14](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/14) — Cierre S3 | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11), [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12), [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) |
| [back#15](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/15) — Racha/puntos | [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13), [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) |
| [back#16](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/16) — Historial | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11), [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13), [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) |
| [back#17](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/17) — Admin | [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8), [infra#22](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/22) |
| [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18) — Cierre S5 | `back#14` a `back#17`, [infra#22](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/22) |
| [infra#4](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/4) — PR final + tag `v1.0.0` | [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18), [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13), [infra#3](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/3), [infra#7](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/7) |
| [docs#3](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/3) — Documentación final | [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18), [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13), [infra#4](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/4) |

**Compuerta de sprint:** un issue no se mergea si su sprint no está activo o si
tiene un `blocked_by` abierto. Los PRs de sprints futuros se mantienen en
**Draft** hasta que toque su sprint.

### Qué puede empezar sin esperar al backend

Estas tareas de frontend son de **interfaz pura** y no dependen de un endpoint,
así que pueden arrancar en paralelo (con datos mock si hace falta):
[front#2](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/2)
(setup),
[front#6](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/6)
(visor de lectura) y
[front#8](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/8)
(selección de texto).

## 2. Plan de trabajo hasta la entrega

> Escrito por quien coordina el proyecto, tras la auditoría de trazabilidad del
> **04-nov-2026**. Es el orden en el que el equipo entra a codificar a partir de
> ahora.
>
> El **qué** y el **cuándo** de cada tarea están en
> [`cronograma.md`](./cronograma.md). La asignación por persona está en el
> [anteproyyecto](../anteproyecto/anteproyecto-dolynation.md#132-tabla-de-asignaci%C3%B3n-de-tareas-y-cronograma)
> y el inventario de lo ya entregado en
> [`AUDITORIA-ESTADO-SPRINTS.md`](./AUDITORIA-ESTADO-SPRINTS.md). Aquí está el
> **orden**.

### 2.1 El punto de partida

Lo primero que hice fue auditar qué estaba realmente hecho, porque el tablero
decía una cosa y el código otra. El resultado: **el Sprint 1 estaba casi
completo en código y sin cerrar en GitHub**, porque el split del monorepo entró
por push directo a `main` sin PR ni `Closes #N`.

Lo que hay que tener presente al empezar:

- **22 issues cerrados, 62 abiertos.** Cada issue abierto tiene un comentario
  con qué entregó el código ya mergeado y qué falta. No hace falta reconstruir
  el estado: está escrito.
- **El Sprint 1 se extiende al 08-nov y el Sprint 2 al 22-nov.** Los dos
  vencieron con trabajo pendiente; ampliarlos permite que quepa antes del
  10-dic. S3, S4 y S5 no se mueven.
- **Dos PRs esperan aprobación**: el #22 de docs (cierra `docs#11`, `docs#13` y
  `docs#14`) y el #31 del frontend (cierra `front#2`).

### 2.2 Tres frentes que pueden ir en paralelo

El error más caro que puede cometer el equipo ahora es esperar. Hay tres
frentes que **no se bloquean entre sí**:

| Frente | Qué incluye | Depende de |
| --- | --- | --- |
| **A — Schema** | `infra#20` (migración S2), `infra#24` (runner), `infra#21` y `infra#22` | Nada. Es el bloqueo raíz, pero es trabajo aislado |
| **B — Frontend** | `front#2` (PR #31, en revisión), `front#22` (los 4 idiomas), `front#24` (tokens) | Nada. Es la compuerta de 13 issues |
| **C — Backend** | `back#4` (refresh rotado), `back#5` (perfil), `back#6` (tests) | El frente A, para las partes de schema |

> El frente C arranca ya con lo que no depende del schema: `back#4` y `back#5`
> son endpoints que ya existen en `develop`, y `back#6` son pruebas de lo que ya
> está. El schema solo es necesario para `back#8`, `back#9` y `back#10`.

### 2.3 El orden del frente A (schema)

Es lo que desbloquea más, así que va primero:

| # | Tarea | Por qué es la primera |
| --- | --- | --- |
| 1 | **`infra#20`** — migración S2 | Sin `user_preferences`, `categories`, `subcategories` y `prompt_hash` no arrancan `back#8`, `back#9`, `back#10` ni `front#5` |
| 2 | **`infra#24`** — runner de migraciones | Hoy las migraciones **ni siquiera se aplican**: el `initdb.d` de la imagen ignora `updates/`. Escribir la migración sin el runner es escribirla dos veces |
| 3 | **`infra#21`** — migración S3 | Habilita `back#11`, `back#13`, `back#14`, `back#16` y `front#10` |
| 4 | **`infra#22`** — migración S4 | Habilita `back#17` y `front#12` |

Cada migración va en su PR, con su `update` en `database/postgres/updates/` y
el ajuste correspondiente en `src/database/drizzle/schema.ts` del backend, para
que no haya drift.

### 2.4 El orden del frente C (backend)

| # | Tarea | Qué hay que hacer | Nota |
| --- | --- | --- | --- |
| 1 | **`back#4`** | Rehacer el PR #33: persistir y rotar el refresh en `auth_access_tokens`, y hacer real el `logout` | El PR #33 está **vacío**. Los endpoints ya existen en `develop` |
| 2 | **`back#5`** | Completar el PR #34: `email` con validación de unicidad y 409, y el E2E | El PR #34 solo actualiza `fullName` |
| 3 | **`back#6`** | E2E de los cinco endpoints de auth y de `readings` / `evaluate` / `explanations`; cobertura ≥ 70 % | Depende de los dos anteriores |
| 4 | **`back#46`** | `/health/ready` consultando PostgreSQL de verdad | Hoy responde `db: up` sin preguntar a la base |
| 5 | **`back#47`** | Separar `test:unit` de `test:e2e` | Hoy `npm run verify` exige una base de datos local |
| 6 | **`back#19`**, **`back#7`** | Segundo adaptador de ejemplo, tests de contrato; prompts versionados por idioma | `back#20` es la parte grande |

### 2.5 El orden del frente B (frontend)

| # | Tarea | Qué hay que hacer | Nota |
| --- | --- | --- | --- |
| 1 | **`front#2`** | Aprobar el PR #31 | Cierra 13 issues de golpe |
| 2 | **`front#22`** | Completar `fr` e `it` | El PR #31 trae `es` y `en` |
| 3 | **`front#3`** | Login y registro | Depende de `back#4` |
| 4 | **`front#5`** | Formulario de parámetros | Depende de `back#8` y `back#10` |
| 5 | **`front#6`**, **`front#8`** | Visor de lectura y selección de texto | Interfaz pura: puede empezar ya, con datos mock |
| 6 | **`front#4`** | Vista de perfil | Depende de `back#5` |

### 2.6 Reglas del día a día

1. **Antes de escribir código**, leer el comentario de trazabilidad del issue:
   dice qué hay hecho y qué falta. Es más rápido que auditar el repo.
2. **Un PR por issue**, con `Closes #N` **solo si completa** el issue. Si
   aporta pero no completa, `Refs #N`.
3. **El schema va antes que el código que lo usa.** Si un endpoint necesita una
   tabla que no existe, primero la migración.
4. **Nada de `feat` en un PR de infraestructura.** El bump de versión lo
   decide el tipo del commit; un `feat` mal puesto infla la versión.
5. **Un PR no se mergea sin otra persona que lo apruebe.** Ni siquiera si
   quien lo abrió es code owner de la ruta.

### 2.7 Lo que hay que mirar cada semana

| Qué | Dónde | Qué mirar |
| --- | --- | --- |
| Qué está bloqueado | [Project](https://github.com/orgs/DolyLanguagesORG/projects/1) | Los items en «In Progress» sin movimiento en 3 días |
| Qué se cerró | Las discusiones de los 4 repos | El anuncio de cierre del Sprint |
| Qué se desbloqueó | `docs#15` y este documento | Las brechas que se cerraron |
| Qué se pospuso | Los issues con comentario | El motivo y la fecha |

### 2.8 Decisiones pendientes que no bloquean el código

Estas no bloquean a nadie, pero hay que cerrarlas antes del 10-dic:

- **Los 8 PRs de features** llevan `Closes #N` sin completar su issue. Hay que
  pasarlos a `Refs #N` para que un merge no cierre una tarea a medias. Está en
  [`PENDIENTES-AUDITORIA.md`](./PENDIENTES-AUDITORIA.md).
- **El milestone «Fuera de alcance (post-entrega)»** que menciona el
  cronograma no existe, y P3 y P4 ya están cerrados.
- **La numeración del versionado**: el cálculo del bump mira solo el último
  commit del ciclo, así que una funcionalidad puede publicarse como `patch`.
  El fix está en los PRs #59 (backend), #33 (frontend) y #32 (infra).

## 3. Cómo no perder las fechas

### Checklist diario (cada desarrollador)

- [ ] Mira el **Kanban** del [Project](https://github.com/orgs/DolyLanguagesORG/projects/1)
      y tus issues asignados.
- [ ] Si empiezas una tarea, muévela a **In Progress** y crea la rama
      `tipo/issue-<n>-<detalle>` desde `develop` (o usa el botón *Create a
      branch* del issue).
- [ ] Commits en **Conventional Commits** (husky los valida en local).
- [ ] Abre el PR hacia `develop` con título conventional y `Closes #N`.
- [ ] Publica tu avance en el **standup diario** antes de **23:59 CST**.

### Checklist de cierre de una tarea

- [ ] Los checks del repo están en verde (`pr-title`, `pr-target` y los del repo).
- [ ] El PR tiene **1 aprobación**.
- [ ] **Squash merge** hacia `develop`.
- [ ] El issue se cerró solo (por el `Closes #N`). **Si no**, ciérralo a mano
      (ver más abajo).
- [ ] Mueve la tarjeta a **Done** en el Project (esto **siempre** es manual).

> El `Status` del tablero y el estado *open/closed* del issue son cosas
> distintas: mergear cierra el issue, pero **no** mueve la tarjeta.

## 4. PRs que NO cierran un issue (el caso Flowbite)

**No todo PR cierra un issue, y está bien.** Ejemplo: alguien de frontend añade
**Flowbite** como dependencia y sube un PR. Ese PR:

- Es un `chore(deps): ...` (o `build(...)`).
- **No lleva `Closes #N`**, porque no completa el entregable de ninguna tarea.
- Se mergea igual, con sus checks y su aprobación.

Reglas para no confundir el tablero:

| Situación | Qué poner en el PR |
| --- | --- |
| El PR **completa** el issue (es su entregable) | `Closes #N` |
| El PR **aporta** a un issue pero no lo completa | `Refs #N` (no lo cierra) |
| El PR no pertenece a ninguna tarea (deps, config suelta) | Nada |

**Piénsalo así:** `Closes #N` es una promesa — al mergear, GitHub cierra el
issue. Si el trabajo de esa tarea no queda terminado, **no lo pongas**.

### Si el PR era de una tarea y se te olvidó el `Closes #N`

No pasa nada, se arregla a mano:

1. Abre el PR → panel derecho **Development** → engranaje → **Link an issue**,
   y elige el issue. (O edita el cuerpo del PR y añade `Closes #N` en su propia
   línea; GitHub lo reconoce aunque el PR ya esté abierto.)
2. Si ya se mergeó sin enlace: **cierra el issue manualmente** desde su página
   (botón **Close issue**).
3. Mueve la tarjeta a **Done** en el Project.

## 5. Monitoreo (para el SM)

Para saber **quién no ha avanzado**, sin adivinar:

- **Filtros de issues útiles:**
  - `milestone:"Sprint 1: Infraestructura, Autenticación y Perfil" is:open` → lo que falta del sprint.
  - `label:sprint-1 is:open` → lo mismo, por label.
  - `is:open no:assignee` → tareas sin dueño.
  - `assignee:@AzaelG26 is:open` → la carga de una persona.
- **Vistas del Project** (se crean a mano en la UI; la API no las crea):
  - agrupar por **Assignee** para ver carga por persona;
  - filtrar por **Milestone/Sprint** para el cierre de sprint.
- **Standup diario** ([hilo](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/discussions/1)):
  quien no reporta, probablemente no avanzó. Es la señal más temprana.
- **Relationships / blocked by**: si una tarea de frontend está bloqueada, no es
  atraso del responsable de front; es espera de backend. El tablero lo muestra.

## 6. Justificar un atraso (de cara a la revisión)

El profesor revisa fechas. Para que un atraso **no recaiga en el equipo sin
explicación**, déjalo documentado *en el propio issue*, no solo en el chat:

1. **Comenta en el issue** la causa (bloqueo externo, dependencia sin terminar,
   fallo de un servicio de IA, etc.) con fecha.
2. Si el bloqueo es otra tarea, registra la relación **blocked by** en GitHub
   (aparece en *Relationships*).
3. Menciona el bloqueo en el **standup** del día.
4. Cuando se destrabe, comenta que se retomó.

Así, cuando el SM tenga que explicar por qué algo no se entregó a tiempo, hay un
rastro verificable dentro de GitHub, con fechas, no una versión de memoria.

## Documentos relacionados

- [`cronograma.md`](./cronograma.md) — los 70 issues, sprints y fechas.
- [`FLUJO-DE-TRABAJO.md`](../operations/FLUJO-DE-TRABAJO.md) — ramas, tablero y releases.
- [`COMO-HACER-UN-PR.md`](../operations/COMO-HACER-UN-PR.md) — el paso a paso de un PR.
- [`conventions/git-workflow.md`](../conventions/git-workflow.md) — ramas y hotfixes.
