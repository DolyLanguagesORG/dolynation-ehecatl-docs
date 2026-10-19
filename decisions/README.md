# Decisiones de implementación

Registro corto de las decisiones que afectan a varios repos. No sustituye al
anteproyecto; lo aclara cuando la implementación tomó una decisión concreta.

| ID | Decisión | Estado |
| --- | --- | --- |
| ADR-001 | MiniMax-M3 como proveedor de IA por defecto, con interfaz adaptable | Aceptada |
| ADR-002 | Contratos canónicos de lectura, evaluación y vocabulario | Aceptada |
| ADR-003 | Puntos calculados desde el score de las evaluaciones | Aceptada |
| ADR-004 | Roles en `users.role` (`STUDENT`/`ADMIN`) | Aceptada |
| ADR-005 | Cuatro idiomas y TTS en `v1.0.0` | Aceptada |
| ADR-006 | Migraciones de schema en dos fases para S2, S3 y S4 | Aceptada |

## ADR-001 — Proveedor de IA

- **Contexto:** el anteproyecto menciona OpenAI/Gemini; la implementación usa
  MiniMax-M3 y la arquitectura ya tiene una interfaz de proveedor.
- **Decisión:** MiniMax-M3 es el proveedor por defecto; la interfaz permite
  agregar OpenAI/Gemini sin cambiar los servicios de negocio.
- **Consecuencia:** los issues `back#7` y `back#19` hablan de MiniMax-M3
  adaptable, no de una instalación obligatoria de OpenAI/Gemini.

## ADR-002 — Contratos canónicos

- **Decisión:**
  - `POST /api/v1/readings` para generar una lectura.
  - `POST /api/v1/readings/{id}/evaluate` para evaluar un resumen.
  - `POST /api/v1/readings/{id}/explanations` para vocabulario contextual.
  - TTS bajo `readings` para palabras/frases cortas.
- **Consecuencia:** no se crean módulos paralelos `/content`, `/evaluation` ni
  `/vocabulary`; los PRs que los proponían quedaron en Draft o se reworkearon.

## ADR-003 — Puntos

- **Contexto:** el cronograma y el dashboard piden puntos; el anteproyecto no
  define una tabla de puntos.
- **Decisión:** los puntos de una actividad son el `score` (0-100) de su
  evaluación; el total diario es la suma. No se crea tabla de puntos.
- **Consecuencia:** `back#15` calcula streak y puntos desde `evaluations` y
  `users`; `front#15` grafica esos datos.

## ADR-004 — Roles

- **Decisión:** la autorización usa `users.role` con `STUDENT`/`ADMIN`.
- **Consecuencia:** no se usa la tabla `admins` del PR #39. `infra#22` agrega la
  columna y `back#17` implementa `AdminGuard` sobre ella.

## ADR-005 — Idiomas y TTS

- **Decisión:** `v1.0.0` soporta `en`, `fr`, `es` e `it` y audio TTS para
  palabras/frases cortas.
- **Consecuencia:** `readings.language`, prompts por idioma, settings de idioma
  y el endpoint TTS forman parte de S2/S3.

## ADR-006 — Migraciones de schema

- **Decisión:** los cambios de S2/S3/S4 se entregan con `01-init.sql`
  actualizado y un script idempotente en `database/postgres/updates/`.
- **Consecuencia:** se crean `02-sprint2-study-config.sql`,
  `03-sprint3-evaluations-vocabulary.sql` y `04-sprint4-admin-role.sql`. La
  convención de dos fases se mantiene para producción.
