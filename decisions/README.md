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
| ADR-007 | PostgreSQL 15 con Drizzle ORM como capa de acceso a datos | Aceptada |
| ADR-008 | Argon2id + JWT HS256 con refresh token persistido y rotado | Aceptada |
| ADR-009 | GitHub como plataforma principal de trabajo | Aceptada |
| ADR-010 | `DolyNation` como nombre canónico del proyecto | Aceptada |

## ADR-001 — Proveedor de IA

- **Contexto:** el anteproyecto menciona OpenAI/Gemini; la implementación usa
  MiniMax-M3 y la arquitectura ya tiene una interfaz de proveedor.
- **Decisión:** MiniMax-M3 es el proveedor por defecto; la interfaz permite
  agregar OpenAI/Gemini sin cambiar los servicios de negocio.
- **Alternativas:** OpenAI o Gemini (más conocido por el equipo, pero con otro
  modelo de costos y de latencia); modelo local (fuera de alcance por
  hardware).
- **Consecuencia:** los issues `back#7` y `back#19` hablan de MiniMax-M3
  adaptable, no de una instalación obligatoria de OpenAI/Gemini.

## ADR-002 — Contratos canónicos

- **Contexto:** al separar el monorepo en cuatro repos, los PRs iniciales
  propusieron endpoints (`/content/generate`, `/evaluation/submit`) que
  duplicaban recursos y obligaban a documentar dos contratos para lo mismo.
- **Decisión:**
  - `POST /api/v1/readings` para generar una lectura.
  - `POST /api/v1/readings/{id}/evaluate` para evaluar un resumen.
  - `POST /api/v1/readings/{id}/explanations` para vocabulario contextual.
  - TTS bajo `readings` para palabras/frases cortas.
- **Alternativas:** módulos paralelos `/content`, `/evaluation` y `/vocabulary`
  (descartados: duplican el modelo de datos y la documentación).
- **Consecuencia:** no se crean módulos paralelos `/content`, `/evaluation` ni
  `/vocabulary`; los PRs que los proponían quedaron en Draft o se reworkearon.

## ADR-003 — Puntos

- **Contexto:** el cronograma y el dashboard piden puntos; el anteproyecto no
  define una tabla de puntos.
- **Decisión:** los puntos de una actividad son el `score` (0-100) de su
  evaluación; el total diario es la suma. No se crea tabla de puntos.
- **Alternativas:** tabla `user_points` con saldo acumulado (descartada:
  duplica un dato derivable y añade una fuente de verdad más).
- **Consecuencia:** `back#15` calcula racha y puntos desde `evaluations` y
  `users`; `front#15` grafica esos datos.

## ADR-004 — Roles

- **Contexto:** el módulo administrativo necesita distinguir al usuario
  administrador del estudiante.
- **Decisión:** la autorización usa `users.role` con `STUDENT`/`ADMIN`.
- **Alternativas:** tabla `admins` separada (descartada: un usuario con
  rol de administrador deja de ser un usuario); boolean `is_admin` (descartada:
  no escala a más roles).
- **Consecuencia:** no se usa una tabla `admins` aparte. `infra#22` agrega la
  columna y `back#17` implementa `AdminGuard` sobre ella.

## ADR-005 — Idiomas y TTS

- **Contexto:** el §8 del anteproyecto decía «cuatro opciones iniciales
  (inglés o español)», mientras que RF-02 define cuatro idiomas. El proveedor
  de voz nunca quedó decidido.
- **Decisión:** `v1.0.0` soporta `en`, `fr`, `es` e `it` y audio TTS para
  palabras/frases cortas, con **MiniMax** y la misma clave de API que el LLM.
- **Alternativas:** ElevenLabs o Cartesia para el TTS (descartadas por costo y
  por requerir una segunda clave); síntesis local (descartada por hardware).
- **Consecuencia:** `readings.language`, prompts por idioma, settings de idioma
  y el endpoint TTS forman parte de S2/S3.

## ADR-006 — Migraciones de schema

- **Contexto:** el schema cambió entre sprints y cada cambio necesita una
  versión reproducible.
- **Decisión:** los cambios de S2/S3/S4 se entregan con `01-init.sql`
  actualizado y un script idempotente en `database/postgres/updates/`.
- **Alternativas:** un único archivo de schema reescrito por sprint
  (descartada: se pierde el historial y no hay forma de reproducir un entorno
  anterior); herramientas de migración con su propio formato (descartada: el
  proyecto ya usa SQL plano y no quiere sumar dependencias).
- **Consecuencia:** se crean `02-sprint2-study-config.sql`,
  `03-sprint3-evaluations-vocabulary.sql` y `04-sprint4-admin-role.sql`. La
  convención de dos fases se mantiene para producción.

## ADR-007 — Base de datos y ORM

- **Contexto:** el proyecto importó su base del monorepo original, que usaba
  un ORM con abstracción de schema.
- **Decisión:** PostgreSQL 15 como base de datos y **Drizzle ORM** como capa de
  acceso a datos del backend; el SQL de referencia vive en
  `dolynation-tlalli-infra/database/postgres/` y es la fuente de verdad.
- **Alternativas:** Prisma (descartada: el schema vive en el repo de
  infraestructura y no en el backend, y Prisma Oculta el SQL); SQL manual con
  `pg` (descartada: se pierde el tipado de las consultas).
- **Consecuencia:** no hay un generador de migraciones en el backend: el SQL
  se escribe en infra y Drizzle lo replica. `infra#25` añade un test de
  paridad entre ambos para que la duplicación no se desincronice en silencio.

## ADR-008 — Autenticación

- **Contexto:** el código importado ya usaba Argon2id y JWT, pero el refresh
  token era stateless (nunca se persistía) y `logout` no revocaba nada.
- **Decisión:** Argon2id para el hash de contraseñas, JWT HS256 con expiración
  y refresh token **persistido con hash, rotado y revocable** en
  `auth_access_tokens`.
- **Alternativas:** sesiones en base de datos (descartada: el proyecto ya
  migrate a JWT); refresh token stateless (descartada: no permite revocar ni
  detectar robo de token).
- **Consecuencia:** `back#4` cierra el hueco de persistencia y rotación;
  `back#27` endurece el arranque (secreto sin valor por defecto), CORS y rate
  limiting.

## ADR-009 — GitHub como plataforma principal de trabajo

- **Contexto:** el equipo de cinco personas tiene que coordinar código, tareas,
  revisiones, CI/CD, entornos y documentación entre el 5 de octubre y el 10 de
  diciembre de 2026, sin operador de infraestructura.
- **Decisión:** GitHub es la plataforma única: repositorios, issues, sub-issues
  y dependencias, Project, rulesets, CODEOWNERS, GitHub Actions, Environments,
  Releases y secret scanning. No se usa una segunda herramienta de gestión ni
  un motor de CI aparte.
- **Alternativas:** GitLab self-hosted (hay que mantener la instancia),
  Bitbucket (integración más débil con CI/CD y rulesets), CircleCI o Jenkins
  (un motor de CI adicional que duplica la configuración), y Jira/Trello/Notion
  (un tablero que se desincroniza de las issues).
- **Consecuencia:** el proyecto depende de GitHub y una migración exigiría
  reconstruir tablero, checks y reglas; es un coste aceptado porque la
  alternativa costaría más tiempo de equipo, que es el recurso escaso.
  Los rulesets **no** declaran `bypass_actors`: la revisión del code owner es
  obligatoria para todos, sin excepciones. El detalle está en
  [`operations/JUSTIFICACION-GITHUB.md`](../operations/JUSTIFICACION-GITHUB.md).

## ADR-010 — Nombre canónico del proyecto

- **Contexto:** el proyecto nació como «Dolynglish» y en algunos archivos
  antiguos todavía aparece ese nombre.
- **Decisión:** el nombre canónico es **DolyNation**. «Dolynglish» queda como
  alias histórico y solo se usa para identificar el monorepo original archivado.
- **Alternativas:** mantener «Dolynglish» (descartado: no coincide con el
  nombre de los repositorios, el `package.json` ni el título del anteproyecto) o
  usar los dos indistintamente (descartado: genera ambigüedad en la entrega).
- **Consecuencia:** el `package.json`, la API, la documentación, la portada de
  la organización y el material de la entrega usan **DolyNation**.

## Decisiones pendientes de toma

Estas decisiones **no están tomadas**: se listan con sus opciones y con el
criterio para cerrarlas, para que el equipo no las tome de forma implícita. Las
que bloquean a una issue concreta llevan esa issue en la última columna.

| # | Decisión pendiente | Opciones | Criterio para decidir | Issue que la espera |
| --- | --- | --- | --- | --- |
| 1 | Umbral de `passed` | `score ≥ 70` / `score ≥ 80` | Qué proporción de resúmenes «razonables» debe pasar la evaluación | `back#22` |
| 2 | Métrica de cobertura de ideas principales | Rúbrica con LLM / keywords de referencia por lectura | Reproducibilidad y costo por evaluación | `back#22` |
| 3 | Umbral y forma del feedback | Texto libre / bullets por criterio | Que el usuario sepa qué cambiar | `back#23` |
| 4 | Tipo de columna del rol | `ENUM` de PostgreSQL / `VARCHAR` con `CHECK` | Compatibilidad con el runner de migraciones | `infra#22` |
| 5 | Formato y límite del audio TTS | `audio/mpeg` con tope de tamaño | Compatibilidad del navegador y costo del proveedor | `back#44` |
| 6 | Reintentos y backoff del proveedor IA | 2 reintentos exponenciales / sin reintento | Costo por llamada y latencia percibida | `back#21` |
| 7 | Caché y rate limit en memoria o Redis | En memoria (1 instancia) / Redis | Nº de instancias del despliegue | `back#9`, `back#27` |
| 8 | Política de contraseñas | `MinLength(8)` actual / 12 con mayúscula y número | Usabilidad contra el RNF-05 | `back#27` |
| 9 | Modelo de despliegue | 1 servidor self-host / varias instancias | Volumen esperado de usuarios | `infra#26` |
