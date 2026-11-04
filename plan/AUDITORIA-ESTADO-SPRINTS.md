# Auditoría de estado de los sprints

> **Fecha:** 04-nov-2026 · **Alcance:** los 4 repositorios de la organización,
> sus 84 issues, 46 pull requests y el Project del plan.
>
> Este documento responde tres preguntas:
>
> 1. ¿Qué trabajo ya está hecho y mergeado en `develop`?
> 2. ¿Qué issues se pueden cerrar y cuáles siguen abiertos?
> 3. ¿Qué inconsistencias tiene el plan?
>
> La fuente de verdad de *qué* hay que hacer sigue siendo
> [`cronograma.md`](./cronograma.md). Este documento describe *dónde* está cada
> cosa, no redefine el alcance.

---

## 1. El origen del desalineamiento

El proyecto se separó del monorepo `doly-languages` (archivado) el **11-oct-2026**.
Ese trabajo entró por **push directo a `main`**, sin pull request y sin
`Closes #N`:

| Repo | Commit | Contenido | Volumen |
| --- | --- | --- | --- |
| `dolynation-atl-back` | `6792b63` | Backend completo: auth, lecturas, IA, health, Drizzle, tests | 116 archivos, 24 569 líneas |
| `dolynation-tonatiuh-front` | `67c2a70` | App Next.js 16 + Tailwind 4 (scaffold) | 27 archivos, 7 981 líneas |
| `dolynation-tlalli-infra` | `9e88059` | Compose (dev/test/prod), schema SQL, CI | 18 archivos, 1 153 líneas |
| `dolynation-ehecatl-docs` | `c1438df` | Documentación completa del monorepo | 32 archivos, 4 512 líneas |

> **Consecuencia:** el código que resuelve buena parte del Sprint 1 y del Sprint 2
> **ya está en `develop`**, pero los issues que lo pedían nunca se cerraron,
> porque el commit no llevaba `Closes #N` y nadie abrió el PR de trazabilidad.
> Por eso 32 de 33 entregables de producto siguen abiertos pese a que su código
> exista.

El plan ya preveía el remedio: el propio `back#2` decía *«Lo que falta: el PR de
trazabilidad que cierre esta issue»*. Ese PR nunca se abrió.

---

## 2. Estado por sprint

Conteo sobre las tablas por sprint de [`cronograma.md`](./cronograma.md), que
coinciden con los milestones de GitHub.

| Sprint | Periodo | Cerrados | Parciales | Sin avance | Sin PR asociado |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | 05–18 oct | 2/8 | 6/8 | 0/8 | 5/8 |
| 2 | 19 oct–01 nov | 1/17 | 7/17 | 9/17 | 7/17 |
| 3 | 02–15 nov | 0/10 | 2/10 | 8/10 | 3/10 |
| 4 | 16–29 nov | 0/17 | 5/17 | 12/17 | 4/17 |
| 5 | 30 nov–10 dic | 0/16 | 2/16 | 14/16 | 2/16 |

> **Ninguno de los 5 milestones está cerrado.** El Sprint 1 venció el 18-oct y el
> Sprint 2 el 01-nov; hoy es 04-nov, así que hay **dos sprints vencidos** y el
> Sprint 3 está a un día de terminarse.

---

## 3. Qué está hecho y qué falta, por issue

Cada issue abierto recibió un comentario con esta misma estructura: qué entregó
el trabajo ya mergeado, con rutas de archivo, y qué queda pendiente. Resumen:

### `dolynation-atl-back` (31 issues abiertos)

**Entregado y en `develop` (cierran o casi cierran):**

| Issue | Entrega | Pendiente |
| --- | --- | --- |
| `back#2` | `6792b63`: bootstrap NestJS, Drizzle, `users`, health, `CommonModule`, env con Zod | `/health/ready` real (`back#46`) y `verify` sin BD (`back#47`) |
| `back#3` | `6792b63`: Argon2id, JWT con `sub`/`email`/`type`, `JwtStrategy`, guard opt-in, TTL, errores `AUTH_*` | Spec unitario del hash (`back#6`) |
| `back#4` | `6792b63`: los 5 endpoints `/auth/*` y sus DTOs | El refresh no persiste ni rota en `auth_access_tokens`; `logout` es un no-op; **PR #33 está vacío** |
| `back#7` | `6792b63`: `AIProvider`, factory, MiniMax-M3, prompt-builder, `prompt_logs` | Prompts solo en inglés y sin versionar (`back#20`) |
| `back#10` | `6792b63`: `POST /api/v1/readings` con sus 3 parámetros y límite de pendientes | Sin `language`, sin caché ni `prompt_hash` |
| `back#11` | `6792b63`: `POST /api/v1/readings/{id}/explanations` | Faltan los 4 campos de RF-08, `vocabulary_logs` y TTS |
| `back#13` | `6792b63`: **`POST /api/v1/readings/{id}/evaluate` ya existe** (canónica) | No persiste en `evaluations`, no calcula cobertura, duplicado da 400 y pide 409 |
| `back#15` | `6792b63`: `computeStreak()` y `GET /api/v1/user/streak` | `activeStreakFor()` **inventa** la racha; sin puntos ni zona horaria |
| `back#19` | `6792b63`: interfaz `AIProvider`, factory, adaptador MiniMax | Sin segundo adaptador de ejemplo ni tests de contrato; `groq`allowed pero revienta en runtime |

**Con PR abierto que aún no cumple (8):**

| PR | Issue | Por qué no cierra |
| --- | --- | --- |
| #33 | `back#4` | **Diff vacío**: 0 archivos |
| #34 | `back#5` | Solo actualiza `fullName`; falta `email`, 409 y E2E |
| #35 | `back#8` | Usa `user_settings` (no canónico), 5 idiomas en vez de 4, sin `POST` de categoría propia |
| #36 | `back#10` | Agrega `/content/generate`, **fuera del contrato canónico** |
| #37 | `back#13` | Agrega `/evaluation/submit`, duplica la ruta que ya existe |
| #38 | `back#16` | Sin paginación; `wordsLookedUp` siempre 0 |
| #39 | `back#17` | Tabla `admins` en vez de `users.role`; solo GET |
| #40 | `back#18` | Solo retry + circuit breaker, sin integrar ni pruebas |

### `dolynation-tonatiuh-front` (18 issues abiertos)

`67c2a70` entregó el **scaffold** de Next.js 16 con Tailwind 4, `layout.tsx`,
`globals.css` y el CI de `lint`/`typecheck`/`build`. Eso cubre la parte
infraestructural de `front#2`; **ninguna otra tarea de frontend tiene código**.

- `front#2` parcial: falta layout con header/nav/footer, tokens de marca,
  componentes base, cliente HTTP y `.env.example` (además `.gitignore` ignora
  `.env*`, así que hoy no puede existir).
- `front#3` a `front#16`, `front#22`, `front#23`, `front#24`: **sin avance**.

> El frontend es el cuello de botella del proyecto: 13 issues de Sprint 2–5
> dependen de una base que todavía no existe.

### `dolynation-tlalli-infra` (11 issues abiertos)

- `9e88059` + PR #19 entregaron los 3 compose, `.env.dev.example`,
  `deploy-dev.yml` y los scripts de deploy con `set -euo pipefail` y healthcheck.
  Eso cubre la parte mayor de `infra#6`.
- **Las 3 migraciones de schema no existen.** `database/postgres/updates/` solo
  tiene `.gitkeep` y `README.md`: faltan `02-sprint2-study-config.sql`,
  `03-sprint3-evaluations-vocabulary.sql` y `04-sprint4-admin-role.sql`.
  Sin ellas, `back#8`, `#9`, `#10`, `#11`, `#13`, `#16` y `#17` no pueden
  completarse.
- `infra#24` (runner de migraciones) sin implementar: el `initdb.d` de la
  imagen **ignora el subdirectorio `updates/`**, así que hoy las migraciones
  ni siquiera se aplican.
- `infra#26` y `infra#27` sin implementar: Postgres publicado en
  `0.0.0.0:57000` sin TLS, sin healthcheck, sin proxy inverso y sin pipeline de
  despliegue por SHA con rollback.

### `dolynation-ehecatl-docs` (5 issues abiertos)

- `docs#12` y `docs#6`: **cerrados** (PRs #20 y #7).
- `docs#11`, `docs#13`, `docs#14`: el PR #10 aplicó casi todo lo pedido, pero
  quedan huecos concretos:
  - `docs#11`: el índice **no es navegable**: usa `{#ancla}`, sintaxis que
    GitHub no interpreta (12 de 28 entradas rotas) y dos enlaces muestran `##`
    como texto.
  - `docs#13`: la sección de decisiones pendientes tiene **9 decisiones**, no
    las 10 que fija el entregable; además «Consecuencias» se escribe en
    singular.
  - `docs#14`: tres filas del contrato quedaron desactualizadas respecto al
    código (`/evaluate` y `/explanations` figuran como «Planificado S3» pero
    **ya están implementados**).
- `docs#15`: las reglas de rama, los `CODEOWNERS`, los archivos de higiene y los
  `permissions:` están hechos; falta la fecha de los milestones y el estado
  real del Project.
- `docs#3`: parcial; falta la documentación final de la entrega.

---

## 4. Inconsistencias del plan

### 4.1 Corregidas en esta auditoría

| # | Inconsistencia | Alcance | Corrección |
| --- | --- | --- | --- |
| 1 | La etiqueta `sprint-N` no coincide con el milestone | 39 issues | Etiqueta alineada al milestone |
| 2 | El marcador `<!-- doly:... -->` traía `sprint=`, `start=` y `due=` obsoletos | 46 issues | Marcador reescrito con los valores del encabezado |
| 3 | El Project mantenía issues cerrados (`docs#12`, `docs#15`) | 2 items | Items eliminados del tablero |
| 4 | Tarjetas con estado que no reflejan el código | 16 items | Estado recalculado |
| 5 | El `CHANGELOG.md` y el criterio de `docs#15` prometían fechas de milestone que nunca se aplicaron | 2 fuentes | Alineados con el cronograma |
| 6 | Sprint 1 y Sprint 2 vencidos con trabajo pendiente | 2 sprints | **Extendidos** al 08-nov y 22-nov, sin mover S3–S5 |
| 7 | `FLUJO-DE-TRABAJO.md` decía `require_code_owner_reviews: true` y `git-workflow.md` decía `false` | 2 documentos | Ambos reflejan la configuración real |
| 8 | `front#24` pedía la paleta naranja, que los wireframes no usan | 1 issue | Actualizado al tema **blanco y negro** |

### 4.2 Pendientes de decisión del equipo

| # | Inconsistencia | Detalle |
| --- | --- | --- |
| 5 | ~~Dos calendars distintos para los milestones~~ **Resuelto** | Los milestones están en 18-oct, 01-nov, 15-nov, 29-nov y 10-dic, que coinciden con el cronograma. Se corrigieron el `CHANGELOG.md` y el criterio de `docs#15`, que prometían otras fechas. |
| 6 | **La tabla «Correspondencia completa» contradice las tablas por sprint** | 21 de 33 filas asignan un sprint distinto al del milestone y al del encabezado del issue. Ejemplo: `front#2` aparece como Sprint 1 en la correspondencia y como Sprint 2 en la tabla por sprint (y su milestone es Sprint 2). |
| 7 | **El conteo de issues no cuadra** | El cronograma dice «68 abiertas», el anteproyecto dice «70» y la realidad son **65 abiertas** (84 en total, 19 cerradas). |
| 8 | **Faltan 3 entregables de la tabla de correspondencia** | `infra#20`, `#21` y `#22` (migraciones) están en la sección de prerrequisitos pero no en la numeración 1–33 de entregables. |
| 9 | **El milestone «Fuera de alcance (post-entrega)» no existe** | El cronograma dice que P3 y P4 «siguen abiertos y visibles» en ese milestone, pero no hay ningún milestone con ese nombre en los 4 repos, y P3 y P4 son en realidad `infra#7` y `infra#8`, **ya cerrados**. *Queda pendiente de decisión.* |
| 10 | **La tabla de distribución del anteproyecto no cuadra** | Suma 27 + 20 + 19 + 18 = 84 asignaciones sobre 70 issues declaradas. |
| 11 | **El endpoint `/api/v1/user/points` está en el contrato pero `back#15` no lo entrega** | `back#15` solo contempla el cálculo y la asignación de puntos, no un endpoint `/user/points`; el contrato lo lista como «Planificado S4». |
| 12 | **Los 8 PRs de features usan `Closes #N` sin cumplir el issue** | Si se mergean tal cual, cierran issues incompletos. La regla de `PLAN-Y-SEGUIMIENTO.md` dice `Refs #N` cuando el PR aporta pero no completa. *Queda pendiente por decisión del equipo; está en [`PENDIENTES-AUDITORIA.md`](./PENDIENTES-AUDITORIA.md).* |

### 4.3 Sobre qué fuente manda

El plan tiene **cuatro fuentes de sprint** en conflicto:

| Fuente | Ejemplo (`back#4`) | Coincide con el milestone |
| --- | --- | --- |
| Etiqueta `sprint-N` | `sprint-1` | 26/65 |
| Marcador `<!-- doly:sprint= -->` | `sprint=1` | 19/65 |
| Encabezado del issue | «Sprint 2'» | **65/65** |
| Milestone de GitHub | Sprint 2 | **65/65** |

> El encabezado del issue y el milestone coinciden en **65 de 65** issues abiertos.
> Son la fuente fiable; las etiquetas y los marcadores eran ruido. Tras la
> corrección de esta auditoría, **las cuatro coinciden en 65/65**.

Además, las fechas del cronograma y las del encabezado del issue coinciden en
**65/65**, y las del Project también. El calendario de trabajo está sólido; lo
que estaba roto era la **etiqueta de sprint** y la **tabla de correspondencia**.

---

## 5. Qué hacer para cerrar cada sprint

### Cierres inmediatos (el código ya está, solo falta el PR)

| Issue | Acción |
| --- | --- |
| `back#2`, `back#3` | **Cerrados.** El trabajo llegó en `6792b63`; las brechas que quedan ya son issues propias (`back#46`, `back#47`, `back#6`, `back#27`). |
| `docs#11`, `docs#13`, `docs#14` | Abrir un PR de cierre que corrija el índice, la 10.ª decisión pendiente y las 3 filas del contrato. |
| `docs#15` | Actualizar fechas de milestones, limpiar el Project y cerrar. |

### Sprint 2 — lo que bloquea el resto

1. **`infra#20`** (migración S2): desbloquea `back#8`, `#9`, `#10` y `front#5`.
2. **`infra#24`** (runner de migraciones): sin él, las migraciones escritas no se
   aplican.
3. **`back#4`**: rehacer el PR #33 con persistencia y rotación del refresh.
4. **`front#2`**: la base del frontend. Sin ella, 13 issues no pueden empezar.

### Correcciones de contrato en los PRs abiertos

Reescribir `#36` a `POST /api/v1/readings` y `#37` a
`POST /api/v1/readings/{id}/evaluate`, o cerrarlos: las dos rutas canónicas ya
existen en `develop`, así que de lo contrario se duplicarían.

---

## 5. Decisiones tomadas y estado final

| Decisión | Resultado |
| --- | --- |
| Dónde anunciar los cierres | `dolynation-ehecatl-docs` es el **anuncio central**; cada repo mantiene las suyas para lo propio (código de ese repo) |
| Fechas de los milestones | Coinciden con el **cronograma**: 18-oct, 01-nov, 15-nov, 29-nov y 10-dic |
| Sprint 1 y 2 vencidos | **Extendidos** a **08-nov** y **22-nov**, sin mover S3, S4 ni S5. El Project se recalculó conservando la duración de cada tarea |
| Tema del frontend | **Blanco y negro**, el de los wireframes. `front#24` se actualizó para que no exija la paleta naranja |
| Aprobación de PRs | Cada PR lo aprueba **otro** miembro del equipo: quien lo sube no puede aprobarse a sí mismo |

**Anuncios publicados** (4-nov-2026):

| Repo | Discusión |
| --- | --- |
| `dolynation-ehecatl-docs` | [#23 — Central: qué se entregó, qué se cerró y qué sigue](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/discussions/23) |
| `dolynation-atl-back` | [#58 — Cierre de Sprint 1 y Sprint 2](https://github.com/DolyLanguagesORG/dolynation-atl-back/discussions/58) |
| `dolynation-tonatiuh-front` | [#32 — El frontend entra en marcha](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/discussions/32) |
| `dolynation-tlalli-infra` | [#31 — El schema es el bloqueo raíz](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/discussions/31) |

**PRs en revisión:**

| PR | Estado | Cierra |
| --- | --- | --- |
| `ehecatl-docs#22` | 4/4 checks en verde, `MERGEABLE` | `docs#11`, `docs#13`, `docs#14` |
| `tonatiuh-front#31` | 7/7 checks en verde, revisión publicada | `front#2` |

Lo que quedó en suspense está en
[`PENDIENTES-AUDITORIA.md`](./PENDIENTES-AUDITORIA.md).

## Documentos relacionados

- [`cronograma.md`](./cronograma.md) — sprints, entregables y fechas.
- [`PLAN-Y-SEGUIMIENTO.md`](./PLAN-Y-SEGUIMIENTO.md) — ruta crítica y compuerta de sprint.
- [`../operations/FLUJO-DE-TRABAJO.md`](../operations/FLUJO-DE-TRABAJO.md) — ramas, tablero y releases.
- [`../decisions/README.md`](../decisions/README.md) — decisiones tomadas y pendientes.
