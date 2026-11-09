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
├── 01-init.sql                         # estado final para instalaciones nuevas
└── updates/
    ├── README.md
    ├── 02-sprint2-study-config.sql
    ├── 03-sprint3-evaluations-vocabulary.sql
    └── 04-sprint4-admin-role.sql
```

El modelo de datos documentado está en
[`architecture/data-model.md`](../architecture/data-model.md).

## Regla de dos fases

### Antes del primer deploy real a producción

- `01-init.sql` es el **estado final deseado** y se usa para bases nuevas
  (dev, test y CI).
- Los scripts de `updates/` se mantienen **también** desde S2 para probar la
  ruta de migración y preparar producción.
- Cada cambio debe existir en **ambos**: el `CREATE TABLE`/columnas de
  `01-init.sql` y el script idempotente de `updates/`.
- Los scripts se prueban contra una base existente y contra una limpia.

### Después del primer deploy real a producción

- `01-init.sql` **se congela** en el estado del primer deploy.
- Todo cambio va **solo** en un nuevo script de `updates/`.
- Los scripts se aplican en orden numérico.

### Idempotencia obligatoria

Todos los statements deben poder ejecutarse más de una vez sin romper la BD:

```sql
CREATE TABLE IF NOT EXISTS categories (...);
CREATE INDEX IF NOT EXISTS idx_readings_prompt_hash ON readings(user_id, prompt_hash);
ALTER TABLE readings ADD COLUMN IF NOT EXISTS language VARCHAR(10) NOT NULL DEFAULT 'en';
ALTER TABLE readings ADD CONSTRAINT ... CHECK (...);
```

Evita `DROP COLUMN IF EXISTS` en PostgreSQL 15: no está soportado. Si hace
falta eliminar una columna, usa un script explícito y documenta que se aplica
una sola vez.

## Tablas

### Actuales

| Tabla | Propósito |
| --- | --- |
| `users` | Cuentas, hash Argon2id (`password`), racha y soft delete |
| `auth_access_tokens` | Refresh tokens persistidos con hash |
| `readings` | Lecturas generadas, estado y columnas legacy de evaluación |
| `prompt_logs` | Auditoría de prompts y errores del proveedor |
| `user_settings` | Preferencias por usuario: idioma de superficie y categorías elegidas |
| `admins` | Membresía de administrador (tabla aparte, no una columna en `users`) |

### Planificadas

| Tabla / cambio | Sprint | Issue |
| --- | --- | --- |
| `categories` (hoy el catálogo vive en el código) | S2 | `infra#20` |
| `readings.category_id`, `language`, `length_type`, `prompt_hash` | S2 | `infra#20` |
| `evaluations` | S3 | `infra#21` |
| `vocabulary_logs` | S3 | `infra#21` |
| `word_lookups` (lo necesita `/history`) | — | por crear |

> `user_preferences` y `user_selected_categories` se sustituyeron por una sola
> tabla, `user_settings`; y `users.role` por la tabla `admins`. El detalle
> esta en [`architecture/data-model.md`](../architecture/data-model.md).

> **Ojo con las bases que ya existen**: los scripts de
> `database/postgres/updates/` solo se aplican hoy a bases **nuevas** (el
> compose los monta en `/docker-entrypoint-initdb.d`). Para una base que ya
> existe hay que aplicarlos a mano con `psql`.

## Idea pendiente: que las migraciones se apliquen solas

**Hoy el paso 4 es manual**: si agregas una columna, el SQL llega a la
release (va en el PR de infra), pero aplicarlo a las bases que ya existen
(staging, producción, la de desarrollo) hay que hacerlo a mano con `psql`.

La idea es que el deploy lo haga solo:

1. `scripts/deploy-env.sh`, antes de levantar el stack, aplica los `.sql`
   pendientes **en orden numérico**.
2. Cada script aplicado se registra en una tabla `schema_migrations`
   (`version`, `applied_at`, `checksum`), para no reaplicar lo que ya está.
3. Si un script falla, el deploy **falla** (no se levanta el stack con el
   schema a medias).

Con eso, el flujo de un cambio de schema sería: **PR en infra → merge → el
siguiente deploy actualiza la base**. Sin.psql a mano.

Está trackeado en el issue de infra (`runner de migraciones`).

Detalle de columnas, tipos y relaciones en
[`architecture/data-model.md`](../architecture/data-model.md).

## Convenciones de nombres

| Capa | Convención | Ejemplo |
| --- | --- | --- |
| Tablas SQL | `snake_case` | `auth_access_tokens` |
| Columnas SQL | `snake_case` | `created_at` |
| Variables TS | `camelCase` | `createdAt` |
| Archivos TS | `kebab-case` | `auth-access-tokens.ts` |
| Updates SQL | `NN-<kebab>` | `02-sprint2-study-config.sql` |

## Workflow al cambiar el schema

1. Crear el script `NN-<nombre>.sql` en `database/postgres/updates/`.
2. Actualizar `01-init.sql` para que una base nueva tenga el mismo estado final.
3. Probar el script en una base existente y en una limpia; debe ser idempotente.
4. Commit de ambos archivos en el mismo PR de infra.
5. Los cambios de código backend que usan la nueva estructura van en su repo y
   en commits/PRs separados.
6. Si el cambio desbloquea un issue de backend, cierra el issue de migración
   con evidencia de la verificación.
