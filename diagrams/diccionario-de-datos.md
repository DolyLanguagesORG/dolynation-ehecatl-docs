# Diccionario de datos

Modelo de la base PostgreSQL. La fuente de verdad del DDL es
`dolynation-tlalli-infra/database/postgres/01-init.sql`. Ver también
[`../architecture/data-model.md`](../architecture/data-model.md).

**Cómo leerlo:** cada tabla indica si **existe hoy** (`01-init.sql`) o si sigue
**planificada** o fue **sustituida**.

| Estado | Tablas |
| --- | --- |
| ✅ Existen (17) | `roles`, `users`, `user_oauth_accounts`, `user_settings`, `access_requests`, `auth_access_tokens`, `auth_email_tokens`, `readings`, `reading_explanations`, `prompt_logs`, `moderated_categories`, `category_daily_usage`, `audit_logs`, `error_logs`, `billing_subscriptions`, `billing_payments`, `billing_webhook_events` |
| 🕓 Planificada (1) | `evaluations` (`infra#21`) |
| 🔁 Sustituidas | `admins` (→ `roles` + `users.role_id`), `categories` (→ `moderated_categories`), `user_preferences` + `user_selected_categories` (→ `user_settings`), `vocabulary_logs` (→ `reading_explanations`) |

## 1. `roles` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador del rol (`1 = student`, `2 = admin`). |
| `name` | `VARCHAR(30)` | `NOT NULL, UNIQUE` | Nombre estable del rol (`student` \| `admin`). |
| `description` | `VARCHAR(255)` | `NULL` | Descripción del nivel de acceso. |
| `created_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Creación. |

## 2. `users` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador del usuario. |
| `full_name` | `VARCHAR(255)` | `NULL` | Nombre completo. |
| `email` | `VARCHAR(254)` | `NOT NULL, UNIQUE` | Correo de acceso (normalizado en minúsculas). |
| `password` | `VARCHAR(255)` | `NULL` | Hash Argon2id; `NULL` si se creó solo vía OAuth. |
| `role_id` | `INTEGER` | `NOT NULL, DEFAULT 1, FK roles.id` | Rol RBAC (`student` \| `admin`). |
| `subscription_tier` | `VARCHAR(30)` | `NULL` | Plan activo (`dolly` \| `dolly_plus` \| `dolly_pro`). |
| `stripe_customer_id` | `VARCHAR(64)` | `NULL, UNIQUE` parcial | Identificador del cliente en Stripe (`cus_...`). |
| `current_streak` | `INTEGER` | `NOT NULL, DEFAULT 0` | Días consecutivos de actividad. |
| `last_streak_date` | `DATE` | `NULL` | Última actividad registrada. |
| `email_verified_at` | `TIMESTAMP` | `NULL` | Marca de verificación de correo. |
| `locale` | `VARCHAR(10)` | `NOT NULL, DEFAULT 'es'` | Idioma de interfaz y correos transaccionales. |
| `created_at` | `TIMESTAMP` | `NOT NULL` | Fecha de creación. |
| `updated_at` | `TIMESTAMP` | `NULL` | Última modificación. |
| `deleted_at` | `TIMESTAMP` | `NULL` | Soft delete. |

## 3. `user_oauth_accounts` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador del vínculo OAuth. |
| `user_id` | `INTEGER` | `NOT NULL, FK users.id ON DELETE CASCADE` | Usuario propietario. |
| `provider` | `VARCHAR(30)` | `NOT NULL` | Proveedor OIDC (`google` \| `microsoft`). |
| `provider_user_id` | `VARCHAR(255)` | `NOT NULL` | Claim `sub` único del proveedor (`UNIQUE (provider, provider_user_id)`). |
| `provider_email` | `VARCHAR(254)` | `NULL` | Correo devuelto por el IdP al vincular. |
| `created_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Vinculación inicial. |
| `updated_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Última actualización. |

## 4. `user_settings` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `user_id` | `INTEGER` | `PK, FK users.id ON DELETE CASCADE` | Usuario dueño de las preferencias. |
| `preferred_language` | `VARCHAR(10)` | `NULL, DEFAULT 'en'` | Idioma principal de estudio. |
| `selected_languages` | `JSONB` | `NOT NULL, DEFAULT '[]'` | Lista ordenada por prioridad de idiomas de estudio. |
| `last_language_change_at` | `TIMESTAMP` | `NULL` | Último cambio anual consumido. |
| `language_change_credits` | `INTEGER` | `NOT NULL, DEFAULT 0` | Créditos pagados disponibles para cambiar idioma. |
| `preferred_categories` | `JSONB` | `NOT NULL, DEFAULT '[]'` | Categorías seleccionadas por el estudiante. |
| `saved_categories` | `JSONB` | `NOT NULL, DEFAULT '[]'` | Biblioteca personal de categorías guardadas. |
| `created_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Creación. |
| `updated_at` | `TIMESTAMP` | `NULL` | Última modificación. |

## 5. `access_requests` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador de solicitud manual. |
| `user_id` | `INTEGER` | `NOT NULL, FK users.id ON DELETE CASCADE` | Solicitante. |
| `request_type` | `VARCHAR(30)` | `NOT NULL` | Tipo (`plan_upgrade` \| `language_unlock`). |
| `requested_tier` | `VARCHAR(30)` | `NULL` | Plan solicitado cuando aplica. |
| `current_tier` | `VARCHAR(30)` | `NULL` | Plan al momento de la solicitud. |
| `user_message` | `TEXT` | `NULL` | Nota opcional del usuario. |
| `status` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'pending'` | `pending` \| `approved` \| `rejected`. |
| `rejection_reason` | `TEXT` | `NULL` | Motivo registrado por el admin. |
| `reviewed_by_user_id` | `INTEGER` | `NULL, FK users.id ON DELETE SET NULL` | Administrador revisor. |
| `reviewed_at` | `TIMESTAMP` | `NULL` | Fecha de resolución. |
| `created_at` / `updated_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Tiempos de auditoría. |

## 6. `auth_access_tokens` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador del token. |
| `tokenable_id` | `INTEGER` | `NOT NULL, FK users.id ON DELETE CASCADE` | Usuario propietario. |
| `type` | `VARCHAR(255)` | `NOT NULL` | `refresh`. |
| `name` | `VARCHAR(255)` | `NULL` | Etiqueta opcional. |
| `hash` | `VARCHAR(255)` | `NOT NULL` | Hash del refresh token. |
| `abilities` | `TEXT` | `NOT NULL` | Permisos serializados. |
| `created_at` / `updated_at` / `last_used_at` / `expires_at` / `deleted_at` | `TIMESTAMP` | `NULL` | Ciclo de vida y revocación. |

## 7. `auth_email_tokens` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador del token de correo. |
| `user_id` | `INTEGER` | `NOT NULL, FK users.id ON DELETE CASCADE` | Usuario asociado. |
| `type` | `VARCHAR(30)` | `NOT NULL` | Propósito (`verify_email` \| `reset_password`). |
| `token_hash` | `VARCHAR(64)` | `NOT NULL, UNIQUE` | Hash SHA-256 del token de un solo uso. |
| `expires_at` | `TIMESTAMP` | `NOT NULL` | Expiración. |
| `consumed_at` | `TIMESTAMP` | `NULL` | Marca cuando fue consumido. |
| `created_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Creación. |

## 8. `readings` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador de la lectura. |
| `user_id` | `INTEGER` | `NOT NULL, FK users.id ON DELETE CASCADE` | Usuario que la generó. |
| `title` | `VARCHAR(255)` | `NOT NULL` | Título. |
| `description` | `TEXT` | `NOT NULL` | Descripción corta. |
| `content` | `TEXT` | `NOT NULL` | Contenido completo. |
| `category` | `VARCHAR(50)` | `NOT NULL, DEFAULT 'technology'` | Categoría editorial. |
| `difficulty` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'medium'` | `easy` \| `medium` \| `hard`. |
| `language` | `VARCHAR(10)` | `NOT NULL, DEFAULT 'en'` | Idioma del texto. |
| `word_count` | `INTEGER` | `NOT NULL, DEFAULT 0` | Conteo de palabras. |
| `status` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'pending'` | `pending` \| `completed`. |
| `score` | `INTEGER` | `NULL` | Puntuación obtenida (`0`–`100`). |
| `passed` | `BOOLEAN` | `NULL` | Indicador de aprobación. |
| `user_response` | `TEXT` | `NULL` | Resumen del estudiante. |
| `feedback` | `TEXT` | `NULL` | Retroalimentación generada por IA. |
| `evaluation_operation_id` | `VARCHAR(100)` | `NULL, UNIQUE` parcial | Clave de idempotencia de evaluación. |
| `created_at` / `updated_at` / `deleted_at` | `TIMESTAMP` | `created_at NOT NULL` | Tiempos y soft delete. |

## 9. `reading_explanations` ✅ existe

Almacena explicaciones contextuales de palabras/frases seleccionadas dentro de una lectura y funciona como glosario personal (`is_saved`):

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador de la explicación. |
| `reading_id` | `INTEGER` | `NOT NULL, FK readings.id ON DELETE CASCADE` | Lectura de origen. |
| `user_id` | `INTEGER` | `NOT NULL, FK users.id ON DELETE CASCADE` | Estudiante propietario. |
| `word` / `normalized_word` | `TEXT` | `NOT NULL` | Término seleccionado y forma normalizada para caché. |
| `entry_type` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'word'` | `word` \| `phrase`. |
| `language` / `difficulty` | `VARCHAR` | `NOT NULL` | Idioma y nivel del contexto. |
| `context` / `literal_meaning` / `explanation` | `TEXT` | `explanation NOT NULL` | Oración original, sentido literal y explicación contextual. |
| `word_breakdown` / `other_ways_to_say` / `other_contexts` | `JSONB` | `NOT NULL, DEFAULT '[]'` | Desglose gramatical, sinónimos y otros usos. |
| `is_saved` / `saved_at` | `BOOLEAN` / `TIMESTAMP` | `is_saved NOT NULL DEFAULT FALSE` | Marca de guardado en el glosario personal. |
| `created_at` / `updated_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Auditoría temporal. |

## 10. `prompt_logs` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador. |
| `level` / `event` / `message` | `VARCHAR` / `TEXT` | `NOT NULL` | Nivel, tipo de evento IA y mensaje. |
| `seed` | `VARCHAR(255)` | `NULL` | Semilla o clave editorial. |
| `user_id` / `text_id` | `INTEGER` | `NULL, FK users/readings` | Usuario y lectura relacionados. |
| `request_id` / `ip_address` / `provider` / `model` | `VARCHAR` | `NULL` | Correlación HTTP, proveedor y modelo usado. |
| `params` | `JSONB` | `NULL` | Parámetros del prompt. |
| `system_prompt` / `user_prompt` | `TEXT` | `NULL` | Prompts enviados. |
| `error_message` / `error_stack` | `TEXT` | `NULL` | Detalle si la llamada falló. |
| `duration_ms` | `INTEGER` | `NULL` | Latencia en milisegundos. |
| `created_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Timestamp del evento. |

## 11. `moderated_categories` y 12. `category_daily_usage` ✅ existen

- `moderated_categories` (`canonical_key` PK): cachea veredictos de moderación (`allowed`, `layer`, `reason`, `provider`) y `prompt_profile` (`JSONB`) reutilizable para categorías dinámicas aprobadas.
- `category_daily_usage` (`id` PK, único `(user_id, usage_date, canonical_key)`): controla la cuota diaria anti-abuso de categorías distintas por usuario.

## 13. `audit_logs` y 14. `error_logs` ✅ existen

- `audit_logs` (`id` PK): trazabilidad de acciones por `request_id`, `actor_user_id`, `target_user_id`, `module`, `action`, `event`, `before_state`/`after_state` (`JSONB`), `changed_fields` (`JSONB`) y `duration_ms`.
- `error_logs` (`id` PK): registro centralizado de fallos (`severity`, `source`, `module`, `error_code`, `http_status`, `error_stack`, `request_body`, `details`) consultable desde `/admin`.

## 15. `billing_subscriptions`, 16. `billing_payments` y 17. `billing_webhook_events` ✅ existen

Espejo local de suscripciones Stripe (`billing_subscriptions`), historial e idempotencia de pagos por `fulfilled_at` y sesión/factura única (`billing_payments`) y deduplicación atómica de eventos Stripe por `event_id` (`billing_webhook_events`). Ver columnas completas en [`../architecture/data-model.md`](../architecture/data-model.md).

## 18. `evaluations` 🕓 planificada (`infra#21`)

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador. |
| `reading_id` | `INTEGER` | `NOT NULL, UNIQUE, FK readings.id` | Lectura evaluada. |
| `user_id` | `INTEGER` | `NOT NULL, FK users.id` | Estudiante. |
| `user_summary` | `TEXT` | `NOT NULL` | Resumen redactado. |
| `score` | `INTEGER` | `NOT NULL, CHECK 0-100` | Calificación. |
| `passed` | `BOOLEAN` | `NOT NULL` | Aprobación (`score >= 80`). |
| `feedback` | `TEXT` | `NOT NULL` | Retroalimentación. |
| `main_ideas_coverage` | `TEXT` | `NULL` | Cobertura de ideas. |
| `created_at` | `TIMESTAMP` | `NOT NULL` | Fecha de evaluación. |
