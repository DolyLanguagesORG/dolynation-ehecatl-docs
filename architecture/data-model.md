# Modelo de datos

Fuente de verdad del schema: `dolynation-tlalli-infra`
(`database/postgres/01-init.sql`). El backend no ejecuta DDL; Drizzle solo
mapea las tablas para type-safety.

## Estado actual vs. planificado

| Tabla / cambio | Estado | Dónde | Issue |
| --- | --- | --- | --- |
| `users` | **Existe** | `01-init.sql` | — |
| `auth_access_tokens` | **Existe** (refresh tokens) | `01-init.sql` | — |
| `readings` | **Existe** | `01-init.sql` | — |
| `prompt_logs` | **Existe** | `01-init.sql` | — |
| `user_settings` | **Existe** (idioma de superficie + categorías elegidas) | `01-init.sql` | `infra#22` |
| `admins` | **Existe** (membresía de administrador) | `01-init.sql` | `infra#22` |
| `categories` | Planificado S2 (hoy el catálogo vive **en el código**: `catalog.constants.ts`) | — | `infra#20` |
| `readings.category_id`, `language`, `length_type`, `prompt_hash` | Planificado S2 | — | `infra#20` |
| `evaluations` | Planificado S3 | — | `infra#21` |
| `vocabulary_logs` | Planificado S3 | — | `infra#21` |
| `word_lookups` | Planificado (lo necesita `/history`: hoy `wordsLookedUp` devuelve 0) | — | por crear |

> **Dos disenos cambian respecto al plan original:**
>
> - `user_preferences` + `user_selected_categories` se sustituyeron por **una**
>   tabla, `user_settings`, con `preferred_language` y `preferred_categories`
>   (jsonb). Es lo que implementa el backend.
> - `users.role` (`STUDENT`/`ADMIN`) se sustituyó por la tabla aparte
>   `admins`: los SELECTs sobre `users` no cambian y el guardia de admin
>   consulta `admins`. El cambio de rol dentro de `users` sigue pendiente.

Las diez tablas que existen hoy se crean **todas** con `01-init.sql`: el schema
vive en un solo archivo y `scripts/apply-schema.sh` (en el repo de infra) lo
aplica en cada deploy. Los cambios de schema se hacen **en
`dolynation-tlalli-infra`**, nunca en el backend.

## `users`

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `full_name` | `VARCHAR(255)` | Nullable |
| `email` | `VARCHAR(254)` | `NOT NULL`, `UNIQUE` |
| `password` | `VARCHAR(255)` | **Hash Argon2id**, nunca texto plano |
| `role` | `VARCHAR(20)` | S4: `STUDENT` \| `ADMIN`, default `STUDENT` |
| `current_streak` | `INTEGER` | Default 0 |
| `last_streak_date` | `DATE` | Última actividad |
| `created_at` | `TIMESTAMP` | `NOT NULL` |
| `updated_at` | `TIMESTAMP` | Nullable |
| `deleted_at` | `TIMESTAMP` | Soft delete |

## `auth_access_tokens`

Tokens de refresco persistidos. Se usa esta tabla existente en lugar de crear
`auth_refresh_tokens`.

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `tokenable_id` | `INTEGER` | FK `users.id`, `ON DELETE CASCADE` |
| `type` | `VARCHAR(255)` | `refresh` |
| `name` | `VARCHAR(255)` | Nullable |
| `hash` | `VARCHAR(255)` | Hash del token |
| `abilities` | `TEXT` | Permisos serializados |
| `created_at` | `TIMESTAMP` | — |
| `updated_at` | `TIMESTAMP` | — |
| `last_used_at` | `TIMESTAMP` | — |
| `expires_at` | `TIMESTAMP` | Expiración |
| `deleted_at` | `TIMESTAMP` | Revocación / soft delete |

## `readings`

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `user_id` | `INTEGER` | FK `users.id` |
| `category` | `VARCHAR(50)` | **Deprecada**; se mantiene durante la transición |
| `category_id` | `INTEGER` | S2: FK `categories.id` |
| `language` | `VARCHAR(10)` | S2: `en` \| `fr` \| `es` \| `it`, default `en` |
| `length_type` | `VARCHAR(20)` | S2: `short` \| `medium` \| `long` |
| `prompt_hash` | `VARCHAR(64)` | S2: hash para caché por parámetros |
| `title` | `VARCHAR(255)` | `NOT NULL` |
| `description` | `TEXT` | `NOT NULL` |
| `content` | `TEXT` | `NOT NULL` |
| `difficulty` | `VARCHAR(20)` | `easy` \| `medium` \| `hard` |
| `word_count` | `INTEGER` | Default 0 |
| `status` | `VARCHAR(20)` | `pending` \| `completed` |
| `score` | `INTEGER` | Legacy; la fuente nueva es `evaluations` |
| `passed` | `BOOLEAN` | Legacy |
| `user_response` | `TEXT` | Legacy |
| `feedback` | `TEXT` | Legacy |
| `created_at` | `TIMESTAMP` | `NOT NULL` |
| `updated_at` | `TIMESTAMP` | Nullable |
| `deleted_at` | `TIMESTAMP` | Soft delete |

Índices: `idx_readings_user_id`, `idx_readings_status`,
`idx_readings_user_status` (parcial), `idx_readings_category_id` y
`(user_id, prompt_hash)` (S2).

## `categories` (S2)

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `slug` | `VARCHAR(50)` | `UNIQUE`, clave estable para API |
| `name` | `VARCHAR(50)` | Nombre visible |
| `description` | `TEXT` | Nullable |
| `is_global` | `BOOLEAN` | `true` para categorías de sistema |
| `created_by_user_id` | `INTEGER` | FK `users.id`; nulo si es global |
| `created_at` | `TIMESTAMP` | `NOT NULL` |

Seed inicial: `technology`, `history`, `education`, `programming`, `culture`,
`pop_culture`.

## `user_preferences` (S2)

| Columna | Tipo | Notas |
| --- | --- | --- |
| `user_id` | `INTEGER` | PK, FK `users.id` |
| `target_language` | `VARCHAR(10)` | Default `en` |
| `default_difficulty` | `VARCHAR(20)` | Default `medium` |
| `default_length` | `VARCHAR(20)` | Default `medium` |
| `updated_at` | `TIMESTAMP` | `NOT NULL` |

## `user_selected_categories` (S2)

| Columna | Tipo | Notas |
| --- | --- | --- |
| `user_id` | `INTEGER` | PK compuesta, FK `users.id` |
| `category_id` | `INTEGER` | PK compuesta, FK `categories.id` |

## `evaluations` (S3)

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `reading_id` | `INTEGER` | FK `readings.id`, `UNIQUE` |
| `user_id` | `INTEGER` | FK `users.id` |
| `user_summary` | `TEXT` | Resumen del estudiante |
| `score` | `INTEGER` | 0-100 |
| `passed` | `BOOLEAN` | `score >= 80` |
| `feedback` | `TEXT` | Feedback por criterio |
| `main_ideas_coverage` | `TEXT` | Cobertura de ideas |
| `created_at` | `TIMESTAMP` | `NOT NULL` |

## `vocabulary_logs` (S3)

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `user_id` | `INTEGER` | FK `users.id` |
| `reading_id` | `INTEGER` | FK `readings.id`, nullable |
| `selected_text` | `VARCHAR(255)` | Palabra o frase |
| `original_sentence` | `TEXT` | Contexto |
| `definition` | `TEXT` | Explicación |
| `contextual_example` | `TEXT` | Ejemplo |
| `created_at` | `TIMESTAMP` | `NOT NULL` |

## `reading_explanations` (glosario y ayuda contextual)

Almacena explicaciones estructuradas de palabras y oraciones seleccionadas dentro de una lectura (`01-init.sql`): `word` (`TEXT`), `normalized_word`, `entry_type` (`word` | `phrase`), `language`, `difficulty`, `context`, `literal_meaning`, `explanation`, `word_breakdown` (`JSONB`), `other_ways_to_say` (`JSONB`), `other_contexts` (`JSONB`), `is_saved`, `saved_at`, `created_at` y `updated_at`. También alimenta la cuota diaria por suscripción, la caché por `(user_id, reading_id, normalized_word)` y el contador `wordsLookedUp` en `/history`.

## `moderated_categories`

Caché global persistente de moderación y biblioteca compartida de prompts por categoría (`01-init.sql`):

| Columna | Tipo | Notas |
| --- | --- | --- |
| `canonical_key` | `VARCHAR(120)` | PK normalizada (minúsculas, sin acentos) |
| `sample_category` | `VARCHAR(100)` | Nombre original de muestra |
| `allowed` | `BOOLEAN` | Veredicto de moderación reutilizado globalmente |
| `layer` | `VARCHAR(30)` | Capa que decidió el bloqueo (nullable) |
| `reason` | `VARCHAR(120)` | Motivo normalizado |
| `provider` | `VARCHAR(30)` | Proveedor que evaluó la categoría (`minimax`, `openai`, etc.) |
| `prompt_profile` | `JSONB` | Blueprint editorial reutilizable (`displayName`, `editorialGuidance`, `subtopics`, `uniqueFocusAngles`, `coreConcepts`) |
| `profile_model` | `VARCHAR(60)` | Modelo de IA que generó el blueprint (nullable) |
| `created_at` / `updated_at` | `TIMESTAMP` | Control temporal |

## `prompt_logs`

Auditoría de generación: `level`, `event`, `message`, `seed`, `user_id`,
`text_id`, `params` (JSONB), `system_prompt`, `user_prompt`, `error_message`,
`error_stack`, `duration_ms`, `created_at`.

## Cambios de schema

El schema vive en **un solo archivo**, `database/postgres/01-init.sql`, y lo
aplica `scripts/apply-schema.sh` (en el repo de infra) en cada deploy. **No
hay carpeta `updates/`** mientras producción no tenga datos.

Cuando producción tenga datos reales, `01-init.sql` se congela y los cambios
pasan a scripts incrementales idempotentes en
`database/postgres/updates/NN-<nombre>.sql` (en orden numérico). Ese cambio de
fase se hace a mano y con un PR propio.

Ver [`../conventions/database.md`](../conventions/database.md).
