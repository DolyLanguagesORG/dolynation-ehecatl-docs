# Database

El backend usa **PostgreSQL 15** vía **Drizzle ORM** sobre el driver `pg`.

## Stack

- **PostgreSQL 15** (dev, test y prod vía Docker).
- **node-postgres** (`pg` ^8.13) como driver.
- **Drizzle ORM** (`drizzle-orm` ^0.36) como query builder y type-safety.
- **Sin migraciones desde el backend**: el schema vive como SQL escrito a mano
  en `dolynation-tlalli-infra`.

Drizzle se usa **solo** para tipos TypeScript y para construir queries. No
genera SQL ni corre migraciones. El SQL es la fuente de verdad.

## Fuente de verdad

El schema pertenece a [`dolynation-tlalli-infra`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra):

```
database/postgres/
└── 01-init.sql                         # El schema COMPLETO, en un solo archivo
```

El modelo de datos documentado está en
[`architecture/data-model.md`](../architecture/data-model.md).

## Fase 1 (la actual): el schema en un solo archivo

**El schema se cambia en un solo lugar**: `database/postgres/01-init.sql`.
**No hay carpeta `updates/`** mientras producción no tenga datos.

### Por qué no basta con editar el archivo

`01-init.sql` se monta en `/docker-entrypoint-initdb.d`, pero PostgreSQL
**solo ejecuta esos scripts cuando el volumen de datos está vacío** (la
primera vez que se crea la base). En un ambiente que ya existe, editar el
archivo **no cambia la base**: la base se queda con el schema viejo y el
backend nuevo falla con `columna o tabla inexistente` → **HTTP 500** en
endpoints que antes funcionaban.

Eso es exactamente lo que pasó en desarrollo: el backend se actualizó, la
base no, y `/auth/register` y `/auth/login` empezaron a devolver 500.

### Qué lo resuelve

`scripts/apply-schema.sh` (en el repo de infra) compara el hash de
`01-init.sql` con el hash guardado **dentro de la base** (tabla
`schema_metadata`) y decide:

| Situación | Qué hace |
| --- | --- |
| El schema no cambió | No toca nada (el caso normal de cada deploy) |
| El schema cambió y la base **no** tiene datos | **Recrea** la base: Postgres aplica el schema solo |
| El schema cambió y la base **sí** tiene datos | **No borra nada** y el deploy **se detiene**: hay que migrar a mano |

El runner lo ejecutan **todos** los deploys:

| Deploy | Quién lo llama |
| --- | --- |
| Desarrollo (infra) | `.github/workflows/deploy-dev.yml` (con `FORCE=1`: los datos de desarrollo son desechables) |
| Desarrollo (backend) | `scripts/deploy-dev-back.sh`, antes de reiniciar el backend |
| Staging / producción / rehearsal | `scripts/deploy-env.sh`, **antes** de levantar el stack |

> El orden importa: el schema se aplica **antes** de que arranque el backend
> de la versión nueva. Al revés, la app arranca contra el schema viejo y
> falla en cuanto toca una tabla o columna nueva.

**Consecuencia práctica: un cambio de schema y un deploy son la misma
operación.** No hay que acordarse de aplicar nada a mano con `psql`.

### Idempotencia obligatoria

Aunque hoy no haya scripts incrementales, el SQL debe poder ejecutarse más de
una vez sin romper la base (es lo que hace seguro al runner):

```sql
CREATE TABLE IF NOT EXISTS categories (...);
CREATE INDEX IF NOT EXISTS idx_readings_prompt_hash ON readings(user_id, prompt_hash);
ALTER TABLE readings ADD COLUMN IF NOT EXISTS language VARCHAR(10) NOT NULL DEFAULT 'en';
```

Evita `DROP COLUMN IF EXISTS` en PostgreSQL 15: no está soportado. Si hace
falta eliminar una columna, usa un script explícito y documenta que se aplica
una sola vez.

## Fase 2: cuando producción tenga datos

En cuanto producción tenga datos reales, recrear la base deja de ser una
opción. Ahi se activa la ruta de migraciones incrementales:

- `01-init.sql` **se congela**: ya no se edita.
- Los cambios van en `database/postgres/updates/NN-<nombre>.sql`, en orden
  numérico, **idempotentes** (`IF NOT EXISTS`, `ON CONFLICT`, backfills con
  `WHERE ... IS NULL`).
- `scripts/apply-schema.sh` deja de recrear y pasa a **aplicar los updates**
  sobre la base existente, registrando los ya aplicados.

El cambio de fase se hace **a mano y con un PR propio**: no se mezcla con un
cambio de schema normal.

## Tablas

Las **17 tablas** del schema vigente en `01-init.sql`:

| Tabla | Propósito |
| --- | --- |
| `roles` | Catálogo de roles RBAC (`student`, `admin`); reemplaza a la antigua tabla `admins` |
| `users` | Cuentas, hash Argon2id (`password`, nullable en OAuth), `role_id`, `subscription_tier`, `stripe_customer_id`, `email_verified_at`, `locale`, racha y soft delete |
| `user_oauth_accounts` | Identidades externas OAuth/OIDC vinculadas (Google y Microsoft Entra ID) |
| `user_settings` | Preferencias por usuario: idiomas prioritarios, créditos de cambio anual y categorías elegidas/guardadas |
| `access_requests` | Solicitudes manuales de plan o desbloqueo de idioma cuando `ACCESS_REQUESTS_ENABLED=true` |
| `auth_access_tokens` | Refresh tokens persistidos con hash y expiración |
| `auth_email_tokens` | Tokens de un solo uso para confirmación de cuenta y restablecimiento de contraseña |
| `readings` | Lecturas generadas, dificultad, idioma, idempotencia offline (`evaluation_operation_id`) y estado |
| `reading_explanations` | Explicaciones contextuales de palabras/frases y glosario guardado por usuario |
| `prompt_logs` | Auditoría de prompts, proveedores IA y duración |
| `moderated_categories` | Caché global de moderación de categorías y blueprint editorial compartido |
| `category_daily_usage` | Cuota diaria por usuario de categorías distintas evaluadas |
| `audit_logs` | Bitácora estructurada de auditoría (`before_state`, `after_state`, `request_id`) |
| `error_logs` | Registro centralizado de fallos HTTP 4xx/5xx y proveedores externos |
| `billing_subscriptions` | Espejo local de suscripciones recurrentes en Stripe y resumen no sensible de tarjeta |
| `billing_payments` | Historial e idempotencia (`fulfilled_at`) de suscripciones, facturas y `language_unlock` |
| `billing_webhook_events` | Deduplicación atómica de webhooks Stripe por `event_id` |

La CI de infra (`schema-sql`) comprueba que el schema aplique limpio y el job
`schema-runner` prueba el runner de punta a punta (aplicar, reaplicar y negarse
a borrar una base con datos).

> `user_preferences` y `user_selected_categories` se sustituyeron por `user_settings`,
> `categories` relacional por `moderated_categories`, y la antigua tabla `admins`
> por `roles` referenciada desde `users.role_id`. El detalle campo por campo vive
> en [`architecture/data-model.md`](../architecture/data-model.md).
> esta en [`architecture/data-model.md`](../architecture/data-model.md).

Detalle de columnas, tipos y relaciones en
[`architecture/data-model.md`](../architecture/data-model.md).
