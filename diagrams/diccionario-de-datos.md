# Diccionario de datos

Modelo de la base PostgreSQL. La fuente de verdad del DDL es
`dolynation-tlalli-infra` (`01-init.sql` + `updates/`). Ver también
[`../architecture/data-model.md`](../architecture/data-model.md).

**Cómo leerlo:** cada tabla dice si **existe hoy** o si está **planificada**.

| Estado | Tablas |
| --- | --- |
| ✅ Existen | `users`, `auth_access_tokens`, `readings`, `prompt_logs`, `user_settings`, `admins` |
| 🕓 Planificadas | `categories`, `evaluations`, `vocabulary_logs` |

## 1. `users` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador del usuario. |
| `email` | `VARCHAR(254)` | `NOT NULL, UNIQUE` | Correo de acceso. |
| `password` | `VARCHAR(255)` | `NOT NULL` | Hash Argon2id; nunca texto plano. |
| `full_name` | `VARCHAR(255)` | `NULL` | Nombre completo. |
| `current_streak` | `INTEGER` | `NOT NULL, DEFAULT 0` | Días consecutivos de actividad. |
| `last_streak_date` | `DATE` | `NULL` | Última actividad registrada. |
| `created_at` | `TIMESTAMP` | `NOT NULL` | Fecha de creación. |
| `updated_at` | `TIMESTAMP` | `NULL` | Última modificación. |
| `deleted_at` | `TIMESTAMP` | `NULL` | Soft delete. |

## 2. `auth_access_tokens` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador del token. |
| `tokenable_id` | `INTEGER` | `NOT NULL, FK users.id` | Usuario propietario. |
| `type` | `VARCHAR(255)` | `NOT NULL` | `refresh`. |
| `name` | `VARCHAR(255)` | `NULL` | Etiqueta opcional. |
| `hash` | `VARCHAR(255)` | `NOT NULL` | Hash del refresh token. |
| `abilities` | `TEXT` | `NOT NULL` | Permisos serializados. |
| `created_at` | `TIMESTAMP` | `NULL` | Creación. |
| `updated_at` | `TIMESTAMP` | `NULL` | Modificación. |
| `last_used_at` | `TIMESTAMP` | `NULL` | Último uso. |
| `expires_at` | `TIMESTAMP` | `NULL` | Expiración. |
| `deleted_at` | `TIMESTAMP` | `NULL` | Revocación / soft delete. |

## 3. `user_settings` ✅ existe

Preferencias de estudio de cada usuario.

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `user_id` | `INTEGER` | PK, FK `users.id`, `ON DELETE CASCADE` | Usuario dueño de las preferencias. |
| `preferred_language` | `VARCHAR(10)` | `NOT NULL, DEFAULT 'en'` | Idioma de superficie. |
| `preferred_categories` | `JSONB` | `NOT NULL, DEFAULT '[]'` | Categorías elegidas (arreglo de slugs). |
| `created_at` | `TIMESTAMP` | `NOT NULL, DEFAULT CURRENT_TIMESTAMP` | Creación. |
| `updated_at` | `TIMESTAMP` | `NULL` | Última modificación. |

> Antes se planeaban dos tablas (`user_preferences` y
> `user_selected_categories`); se sustituyeron por esta.

## 4. `admins` ✅ existe

Membresía de administrador. Va **aparte** de `users` a propósito: los
SELECTs sobre `users` no cambian.

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `user_id` | `INTEGER` | PK, FK `users.id`, `ON DELETE CASCADE` | Usuario administrador. |
| `granted_at` | `TIMESTAMP` | `NOT NULL, DEFAULT NOW()` | Cuándo se le concedió. |

> El plan original era una columna `users.role` (`STUDENT`/`ADMIN`). Ese
> cambio de rol dentro de `users` sigue pendiente.

## 5. `categories` 🕓 planificada

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador. |
| `slug` | `VARCHAR(50)` | `NOT NULL, UNIQUE` | Clave estable para la API. |
| `name` | `VARCHAR(50)` | `NOT NULL` | Nombre visible. |
| `description` | `TEXT` | `NULL` | Descripción. |
| `is_global` | `BOOLEAN` | `NOT NULL, DEFAULT false` | `true` para categorías de sistema. |
| `created_by_user_id` | `INTEGER` | `NULL, FK users.id` | Dueño si es categoría propia. |
| `created_at` | `TIMESTAMP` | `NOT NULL` | Creación. |

## 6. `user_preferences` 🕓 no se creó

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `user_id` | `INTEGER` | PK, FK users.id | Usuario. |
| `target_language` | `VARCHAR(10)` | `NOT NULL, DEFAULT 'en'` | `en`, `fr`, `es` o `it`. |
| `default_difficulty` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'medium'` | `easy`, `medium` o `hard`. |
| `default_length` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'medium'` | `short`, `medium` o `long`. |
| `updated_at` | `TIMESTAMP` | `NOT NULL` | Última modificación. |

## 7. `user_selected_categories` 🕓 no se creó

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `user_id` | `INTEGER` | PK, FK users.id | Usuario. |
| `category_id` | `INTEGER` | PK, FK categories.id | Categoría seleccionada. |

## 8. `readings` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador de la lectura. |
| `user_id` | `INTEGER` | `NOT NULL, FK users.id` | Usuario que la generó. |
| `category` | `VARCHAR(50)` | `NOT NULL, DEFAULT 'technology'` | **Deprecada**; usar `category_id`. |
| `category_id` | `INTEGER` | `NULL, FK categories.id` | 🕓 Categoría normalizada (aún no existe). |
| `language` | `VARCHAR(10)` | `NOT NULL, DEFAULT 'en'` | 🕓 Idioma del texto (aún no existe). |
| `length_type` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'medium'` | 🕓 Longitud configurada (aún no existe). |
| `prompt_hash` | `VARCHAR(64)` | `NULL` | 🕓 Hash para caché (aún no existe). |
| `title` | `VARCHAR(255)` | `NOT NULL` | Título. |
| `description` | `TEXT` | `NOT NULL` | Descripción corta. |
| `content` | `TEXT` | `NOT NULL` | Contenido completo. |
| `difficulty` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'medium'` | `easy`, `medium` o `hard`. |
| `word_count` | `INTEGER` | `NOT NULL, DEFAULT 0` | Conteo de palabras. |
| `status` | `VARCHAR(20)` | `NOT NULL, DEFAULT 'pending'` | `pending` o `completed`. |
| `score` | `INTEGER` | `NULL` | Legacy; usar `evaluations`. |
| `passed` | `BOOLEAN` | `NULL` | Legacy. |
| `user_response` | `TEXT` | `NULL` | Legacy. |
| `feedback` | `TEXT` | `NULL` | Legacy. |
| `created_at` | `TIMESTAMP` | `NOT NULL` | Creación. |
| `updated_at` | `TIMESTAMP` | `NULL` | Modificación. |
| `deleted_at` | `TIMESTAMP` | `NULL` | Soft delete. |

## 9. `evaluations` 🕓 planificada

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

## 10. `vocabulary_logs` 🕓 planificada

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador. |
| `user_id` | `INTEGER` | `NOT NULL, FK users.id` | Usuario. |
| `reading_id` | `INTEGER` | `NULL, FK readings.id` | Lectura asociada. |
| `selected_text` | `VARCHAR(255)` | `NOT NULL` | Palabra o frase. |
| `original_sentence` | `TEXT` | `NULL` | Oración original. |
| `definition` | `TEXT` | `NULL` | Definición. |
| `contextual_example` | `TEXT` | `NULL` | Ejemplo contextual. |
| `created_at` | `TIMESTAMP` | `NOT NULL` | Fecha de consulta. |

## 11. `prompt_logs` ✅ existe

| Campo | Tipo | Restricciones | Descripción |
| --- | --- | --- | --- |
| `id` | `SERIAL` | PK | Identificador. |
| `level` | `VARCHAR(20)` | `NOT NULL` | `INFO`, `WARN` o `ERROR`. |
| `event` | `VARCHAR(100)` | `NOT NULL` | Evento (`text_generated`, etc.). |
| `message` | `TEXT` | `NOT NULL` | Mensaje. |
| `seed` | `VARCHAR(255)` | `NULL` | Seed del prompt. |
| `user_id` | `INTEGER` | `NULL, FK users.id` | Usuario. |
| `text_id` | `INTEGER` | `NULL, FK readings.id` | Lectura. |
| `params` | `JSONB` | `NULL` | Parámetros. |
| `system_prompt` | `TEXT` | `NULL` | Prompt de sistema. |
| `user_prompt` | `TEXT` | `NULL` | Prompt de usuario. |
| `error_message` | `TEXT` | `NULL` | Error. |
| `error_stack` | `TEXT` | `NULL` | Stack trace. |
| `duration_ms` | `INTEGER` | `NULL` | Duración de la llamada. |
| `created_at` | `TIMESTAMP` | `NOT NULL` | Fecha del evento. |
