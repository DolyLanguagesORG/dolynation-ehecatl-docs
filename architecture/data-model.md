# Modelo de datos

Fuente de verdad del schema: `dolynation-tlalli-infra`
(`database/postgres/01-init.sql`). El backend no ejecuta DDL; Drizzle solo
mapea las tablas para type-safety.

## Estado actual vs. planificado

Las **16 tablas** vigentes se definen en
`database/postgres/01-init.sql` (repositorio `dolynation-tlalli-infra`) y se
aplican en cada despliegue mediante `scripts/apply-schema.sh`. El backend usa
Drizzle ORM únicamente para type-safety; los cambios de DDL siempre nacen en
`dolynation-tlalli-infra`.

| Tabla / cambio | Estado | Dónde | Issue |
| --- | --- | --- | --- |
| `roles` | **Existe** (`student`, `admin`; reemplaza a la antigua tabla `admins`) | `01-init.sql` | — |
| `users` | **Existe** (incluye `role_id`, `subscription_tier`, `stripe_customer_id`, `email_verified_at`, `locale`) | `01-init.sql` | `infra#196` |
| `user_settings` | **Existe** (`preferred_language`, `selected_languages`, `last_language_change_at`, `language_change_credits`, `preferred_categories`, `saved_categories`) | `01-init.sql` | `infra#22` |
| `access_requests` | **Existe** (solicitudes manuales cuando `ACCESS_REQUESTS_ENABLED=true`) | `01-init.sql` | — |
| `auth_access_tokens` | **Existe** (refresh tokens opacos rotados en cookie `HttpOnly` desde el BFF de Next.js) | `01-init.sql` | — |
| `auth_email_tokens` | **Existe** (confirmación de cuenta y restablecimiento de contraseña) | `01-init.sql` | — |
| `readings` | **Existe** | `01-init.sql` | — |
| `reading_explanations` | **Existe** (explicaciones cacheadas y glosario personal) | `01-init.sql` | `back#11` |
| `prompt_logs` | **Existe** | `01-init.sql` | — |
| `moderated_categories` | **Existe** (caché de moderación y blueprint editorial compartido) | `01-init.sql` | — |
| `category_daily_usage` | **Existe** (cuota diaria anti-abuso por usuario) | `01-init.sql` | — |
| `audit_logs` | **Existe** (bitácora de auditoría por módulo/acción/estado) | `01-init.sql` | — |
| `error_logs` | **Existe** (registro estructurado de errores y fallos de proveedores) | `01-init.sql` | — |
| `billing_subscriptions` | **Existe** (estado local sincronizado de suscripción Stripe y resumen de tarjeta) | `01-init.sql` | `infra#196` |
| `billing_payments` | **Existe** (historial e idempotencia vía `fulfilled_at` y sesión/factura única) | `01-init.sql` | `infra#196` |
| `billing_webhook_events` | **Existe** (deduplicación atómica por `event_id` recibido desde Stripe) | `01-init.sql` | `infra#196` |
| `categories` (relacional) | Sustituida por `moderated_categories` + librería personal en `user_settings` | — | — |
| `evaluations` / `vocabulary_logs` | Planificado S3/S4 (`evaluations` pendiente; vocabulario cubierto por `reading_explanations`) | — | `infra#21` |

> **Notas de arquitectura vigentes respecto al diseño inicial:**
>
> - Los roles RBAC usan **`roles`** referenciada desde **`users.role_id`** (y no una tabla separada `admins`).
> - En web (`dolynation-tonatiuh-front`), los tokens opacos de refresco persistidos en **`auth_access_tokens`** viajan dentro de **cookies `HttpOnly`** gestionadas por el BFF de Next.js, manteniendo el `accessToken` JWT en memoria del cliente.
> - La propiedad **`users.stripe_customer_id`** enlaza al usuario con su cliente en Stripe Sandbox (índice único parcial `uq_users_stripe_customer_id`).

Los cambios de schema se hacen **en `dolynation-tlalli-infra`**, nunca en el backend.

## `users`

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `full_name` | `VARCHAR(255)` | Nullable |
| `email` | `VARCHAR(254)` | `NOT NULL`, `UNIQUE` |
| `password` | `VARCHAR(255)` | **Hash Argon2id**, nunca texto plano |
| `role_id` | `INTEGER` | FK `roles.id` (`student` \| `admin`) |
| `subscription_tier` | `VARCHAR(30)` | `dolly` \| `dolly_plus` \| `dolly_pro` (nullable en cuentas nuevas) |
| `stripe_customer_id` | `VARCHAR(64)` | Nullable; índice único parcial `uq_users_stripe_customer_id` |
| `email_verified_at` | `TIMESTAMP` | Nullable; confirmación de cuenta |
| `locale` | `VARCHAR(10)` | Idioma de interfaz/correos (`es` \| `en` \| ...) |
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

## `billing_subscriptions` (`infra#196`)

Estado sincronizado de la suscripción recurrente pagada en Stripe (un registro por usuario):

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `user_id` | `INTEGER` | `NOT NULL`, `UNIQUE`, FK `users.id` (`ON DELETE CASCADE`) |
| `provider` | `VARCHAR(20)` | `NOT NULL`, default `'stripe'` |
| `stripe_customer_id` | `VARCHAR(64)` | `NOT NULL`, índice `idx_billing_subscriptions_customer` |
| `stripe_subscription_id` | `VARCHAR(64)` | `NOT NULL`, `UNIQUE` |
| `stripe_price_id` | `VARCHAR(64)` | `NOT NULL` |
| `tier` | `VARCHAR(30)` | `NOT NULL` (`dolly_plus` \| `dolly_pro` \| `dolly`) |
| `status` | `VARCHAR(30)` | `NOT NULL`, índice `idx_billing_subscriptions_status` (`active`, `trialing`, `past_due`, `canceled`, etc.) |
| `current_period_start` / `current_period_end` | `TIMESTAMP` | Nullable; límites del ciclo actual |
| `cancel_at_period_end` | `BOOLEAN` | `NOT NULL`, default `false` |
| `canceled_at` | `TIMESTAMP` | Nullable |
| `payment_method_brand` / `payment_method_last4` / `payment_method_exp_month` / `payment_method_exp_year` | `VARCHAR` / `INTEGER` | Resumen no sensible de la tarjeta predeterminada (sin PAN ni CVC) |
| `created_at` / `updated_at` | `TIMESTAMP` | `NOT NULL`, default `NOW()` |

## `billing_payments` (`infra#196`)

Historial e idempotencia transaccional de checkout único (`language_unlock`), checkout inicial de suscripción y facturas (`subscription_invoice`):

| Columna | Tipo | Notas |
| --- | --- | --- |
| `id` | `SERIAL` | PK |
| `user_id` | `INTEGER` | `NOT NULL`, FK `users.id` (`ON DELETE CASCADE`) |
| `provider` | `VARCHAR(20)` | `NOT NULL`, default `'stripe'` |
| `kind` | `VARCHAR(40)` | `NOT NULL` (`subscription` \| `subscription_invoice` \| `language_unlock`) |
| `tier` | `VARCHAR(30)` | Nullable |
| `stripe_checkout_session_id` | `VARCHAR(128)` | `UNIQUE` (idempotencia por sesión) |
| `stripe_payment_intent_id` | `VARCHAR(128)` | Nullable |
| `stripe_invoice_id` | `VARCHAR(128)` | `UNIQUE` (idempotencia por factura) |
| `amount_cents` | `INTEGER` | `NOT NULL`, default `0` |
| `currency` | `VARCHAR(10)` | `NOT NULL`, default `'mxn'` |
| `status` | `VARCHAR(30)` | `NOT NULL`, default `'pending'` (`pending` \| `paid` \| `failed`) |
| `fulfilled_at` | `TIMESTAMP` | Marca atómica (`IS NULL`) para evitar acreditar dos veces en carrera webhook ↔ `/sync` |
| `metadata` | `JSONB` | `NOT NULL`, default `{}` |
| `created_at` / `updated_at` | `TIMESTAMP` | `NOT NULL`, default `NOW()` |

## `billing_webhook_events` (`infra#196`)

Tabla de deduplicación por identificador de evento de Stripe (`event_id`):

| Columna | Tipo | Notas |
| --- | --- | --- |
| `event_id` | `VARCHAR(120)` | PK (`evt_...`) |
| `provider` | `VARCHAR(20)` | `NOT NULL`, default `'stripe'` |
| `event_type` | `VARCHAR(100)` | `NOT NULL` (ej. `checkout.session.completed`, `customer.subscription.deleted`) |
| `status` | `VARCHAR(20)` | `NOT NULL`, default `'processing'` (`processing` \| `processed` \| `failed`) |
| `error_message` | `TEXT` | Nullable; error en caso de fallo recuperable |
| `processed_at` / `created_at` | `TIMESTAMP` | `processed_at` nullable; `created_at` `NOT NULL` |

## Cambios de schema

El schema vive en **un solo archivo**, `database/postgres/01-init.sql`, y lo
aplica `scripts/apply-schema.sh` (en el repo de infra) en cada deploy. **No
hay carpeta `updates/`** mientras producción no tenga datos.

Cuando producción tenga datos reales, `01-init.sql` se congela y los cambios
pasan a scripts incrementales idempotentes en
`database/postgres/updates/NN-<nombre>.sql` (en orden numérico). Ese cambio de
fase se hace a mano y con un PR propio.

Ver [`../conventions/database.md`](../conventions/database.md).
