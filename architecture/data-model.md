# Modelo de datos

Fuente de verdad del schema: `dolynation-tlalli-infra` (`database/postgres/01-init.sql`
y `database/postgres/updates/`). El backend no ejecuta DDL; Drizzle solo mapea
las tablas para type-safety.

## Estado actual vs. planificado

| Tabla / cambio | Estado | Issue |
| --- | --- | --- |
| `users` | Existe | — |
| `auth_access_tokens` | Existe (refresh tokens) | — |
| `readings` | Existe | — |
| `prompt_logs` | Existe | — |
| `categories` | Planificado S2 | `infra#20` |
| `user_preferences` | Planificado S2 | `infra#20` |
| `user_selected_categories` | Planificado S2 | `infra#20` |
| `readings.category_id`, `language`, `length_type`, `prompt_hash` | Planificado S2 | `infra#20` |
| `evaluations` | Planificado S3 | `infra#21` |
| `vocabulary_logs` | Planificado S3 | `infra#21` |
| `users.role` | Planificado S4 | `infra#22` |

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

## `prompt_logs`

Auditoría de generación: `level`, `event`, `message`, `seed`, `user_id`,
`text_id`, `params` (JSONB), `system_prompt`, `user_prompt`, `error_message`,
`error_stack`, `duration_ms`, `created_at`.

## Migraciones

| Archivo | Sprint | Contenido |
| --- | --- | --- |
| `updates/02-sprint2-study-config.sql` | S2 | preferencias, categorías, idioma, longitud y caché |
| `updates/03-sprint3-evaluations-vocabulary.sql` | S3 | evaluaciones y vocabulario |
| `updates/04-sprint4-admin-role.sql` | S4 | `users.role` |

Regla: cada cambio actualiza `01-init.sql` **y** agrega el script idempotente en
`updates/`. Ver [`../conventions/database.md`](../conventions/database.md).
