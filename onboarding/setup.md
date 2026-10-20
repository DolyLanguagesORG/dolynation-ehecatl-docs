# Onboarding — setup local

Cómo levantar el backend de Dolynglish desde cero en tu máquina.

## Requisitos

- **Node.js ≥ 22.0.0** (recomendado: usar [nvm](https://github.com/nvm-sh/nvm))
- **npm ≥ 11.0.0**
- **Docker + Docker Compose** (para PostgreSQL)
- **Git** con SSH configurado para GitHub

Verifica tu entorno:

```bash
node --version    # v22.x.x
npm --version     # 11.x.x
docker --version
```

## Alternativa: Codespaces (sin instalar nada)

Si no quieres instalar Node, npm ni Docker en tu máquina, puedes trabajar en
un **Codespace** (una máquina virtual de GitHub en el navegador). Los cuatro
repos ya traen su `.devcontainer/devcontainer.json`, así que el entorno llega
preconfigurado: Node 22, Docker, `gh` y las extensiones del repo.

**Antes de la primera vez**, hay que habilitar Codespaces en cada repositorio
(lo hace un administrador):

> `Settings` → `Codespaces` → **Enable Codespaces**

Después, en cualquier repo:

```bash
gh codespace create --repo DolyLanguagesORG/dolynation-atl-back
```

O desde el navegador: `Code` → `Codespaces` → `Create codespace on main`.

Qué trae cada uno:

| Repo | Imagen | Servicios y puertos | Al crear |
| --- | --- | --- | --- |
| `dolynation-atl-back` | `typescript-node:22` | API en 3333, Postgres en 5432 | `npm ci` + `.env` desde la plantilla |
| `dolynation-tonatiuh-front` | `typescript-node:22` | Next.js en 3000 | `npm ci` |
| `dolynation-tlalli-infra` | `universal:2` | Postgres 57010, API 57011, front 57012 | valida `docker-compose.test.yml` |
| `dolynation-ehecatl-docs` | `typescript-node:22` | — | ejecuta el test del regex de `pr-labels` |

**Tips**

- Los Codespaces consumen minutos de cómputo: ciérralos cuando no los uses
  (`gh codespace stop`) y bórralos si ya no los necesitas (`gh codespace delete`).
- El Codespace es **personal**: nadie más ve tus cambios hasta que abras un PR.
- Para el trabajo normal del equipo, el clone local sigue siendo la vía
  principal; el Codespace es la alternativa cuando hay que levantar el entorno
  en otro equipo o en otra máquina.

## Clonar el repo

Este setup levanta el **backend**. Clona su repo (más abajo clonarás el de
infraestructura):

```bash
git clone git@github.com:DolyLanguagesORG/dolynation-atl-back.git
cd dolynation-atl-back
```

## Instalar dependencias del backend

```bash
# dentro de dolynation-atl-back
npm ci
```

`npm ci` es estricto con el lockfile. Si necesitas actualizar
dependencias, usa `npm install <pkg>` y commitea el `package-lock.json`
resultante.

## Configurar variables de entorno

```bash
cp .env.example .env
```

Edita `.env` y rellena **al menos**:

- `JWT_SECRET` — genera con `openssl rand -base64 48`
- `DB_PASSWORD` — la que pusiste en el compose de Postgres
- `MINIMAX_API_KEY` — obtén del panel de MiniMax-M3
- `AI_DEFAULT_PROVIDER` — `minimax` o `groq`

El resto tiene defaults razonables.

## Levantar PostgreSQL en local

El repo de infraestructura incluye un compose de Postgres standalone:

```bash
git clone https://github.com/DolyLanguagesORG/dolynation-tlalli-infra.git
cd dolynation-tlalli-infra
docker compose -f docker-compose.test.yml up -d
```

Verifica:

```bash
docker ps             # el contenedor 'dolynglish_postgres' debe estar 'healthy'
docker logs dolynglish_postgres   # debe mostrar 'database system is ready'
```

El schema (`01-init.sql`) se aplica **automáticamente** al primer arranque.

## Levantar el backend en modo desarrollo

```bash
# En el repo del backend (dolynation-atl-back):
npm run start:dev
```

Deberías ver en logs:

```
Application listening on http://0.0.0.0:3333
API documentation: http://0.0.0.0:3333/docs
```

## Verificar que todo funciona

En otra terminal:

```bash
# Health check
curl http://localhost:3333/api/v1/health/live

# Scalar docs en el navegador
open http://localhost:3333/docs

# OpenAPI JSON
curl http://localhost:3333/api/v1/openapi.json | head -50
```

## Correr los tests

```bash
# dentro de dolynation-atl-back
npm run verify    # typecheck + lint + format + test (todo en uno)
```

O paso a paso:

```bash
npm run typecheck     # tsc --noEmit
npm run lint:check    # ESLint
npm run format:check  # Prettier
npm run test          # Jest (unit + e2e)
```

## Solución de problemas

### `EADDRINUSE: address already in use :::3333`

Otro proceso está usando el puerto. Encuentra y mata:

```bash
lsof -ti:3333 | xargs kill -9
```

### `ECONNREFUSED 127.0.0.1:5432` (o el puerto que uses)

Postgres no está corriendo. Levanta el contenedor:

```bash
cd dolynation-tlalli-infra && docker compose -f docker-compose.test.yml up -d
```

### Los tests fallan con errores de Drizzle

Verifica que `01-init.sql` se aplicó:

```bash
docker exec -it dolynglish_postgres psql -U postgres -d dolynglish -c "\dt"
```

Deberías ver las 4 tablas base: `users`, `auth_access_tokens`, `readings` y `prompt_logs`. Al aplicar las migraciones `02`, `03` y `04` se agregan `categories`, `user_preferences`, `user_selected_categories`, `evaluations`, `vocabulary_logs` y `users.role`.

Si faltan, recrea el contenedor:

```bash
docker compose -f docker-compose.test.yml down -v
docker compose -f docker-compose.test.yml up -d
```

### Hooks de git no se ejecutan

Si tienes los hooks configurados pero no corren:

```bash
# dentro de dolynation-atl-back
npx husky
```

## Próximos pasos

- Lee [conventions/code-style.md](../conventions/code-style.md)
- Lee [conventions/api-contracts.md](../conventions/api-contracts.md)
- Lee [conventions/git-workflow.md](../conventions/git-workflow.md)
- Sigue [adding-endpoint.md](./adding-endpoint.md) para tu primer endpoint