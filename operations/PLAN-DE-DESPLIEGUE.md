# Plan de despliegue — DolyNation

Este documento describe **cómo se despliegan los 3 entornos** de DolyNation
(desarrollo, staging y producción) sobre un **servidor único** (self-host), con
los secretos gestionados en **GitHub Environments**. Es una **propuesta**: la
implementación todavía no está hecha.

> Para el pipeline completo de CI/CD y versionado, ver
> [CI-CD-Y-VERSIONADO.md](./CI-CD-Y-VERSIONADO.md). Para las reglas de ramas,
> commits y PR, ver [FLUJO-DE-TRABAJO.md](./FLUJO-DE-TRABAJO.md).

## Decisiones tomadas

| Tema | Decisión |
| --- | --- |
| Servidor | **Uno solo** aloja los 3 entornos (por directorio y puertos) |
| Puertos | **≥ 55000** y < 65535 |
| Secretos | **GitHub Environments** (`desarrollo`, `staging`, `produccion`); ningún valor sensible en el repo |
| Llave SSH | **Sin passphrase**; se restringe en el servidor (`authorized_keys` / usuario dedicado) |
| Merge | **Solo squash** (ya forzado por los rulesets) |
| `rc-<version>` | **No es un entorno**: rama/estado efímero y *single-flight* |

## Arquitectura

### Desarrollo — autodespliegue por repositorio

En desarrollo **no** se usan imágenes: cada repo despliega su propio servicio en
cada merge a `develop`.

- `tlalli-infra` provee **Postgres de desarrollo** y una **red Docker externa**
  (`dolynglish-dev`), más el directorio del servidor (`/srv/doly/dev`).
- `atl-back` tiene su `docker-compose.dev.yml` (servicio backend) conectado a la
  red externa.
- `tonatiuh-front` tiene su `docker-compose.dev.yml` (servicio frontend)
  conectado a la red externa.
- Cada repo, en `push` a `develop`: `ssh` al servidor → `git pull` → `docker
  compose up -d --build` de **su** servicio → healthcheck.
- El deploy de desarrollo es **automático**.

### Staging y producción — por imágenes

Para staging y producción se trabaja con **imágenes**, no con build en el server:

- `atl-back` y `tonatiuh-front` construyen y **publican su imagen**.
- `tlalli-infra` **jala la imagen** y despliega el stack.
- **Registry propuesto: GHCR** (`ghcr.io/dolylanguagesorg/...`), con la etiqueta
  ligada a la versión de la `rc-*` (staging) y de `main` (producción).

> Nota: el `docker-compose.prod.yml` actual de `infra` **no incluye el
> frontend** y usa `build:` (compila el backend). Para staging/producción habrá
> que añadir el servicio de frontend y pasar a `image:`.

## Entornos y puertos

| Entorno | Directorio (server) | DB | Back | Front |
| --- | --- | --: | --: | --: |
| Desarrollo | `/srv/doly/dev` | 57010 | 57011 | 57012 |
| Staging | `/srv/doly/staging` | 57020 | 57021 | 57022 |
| Producción | `/srv/doly/prod` | 57030 | 57031 | 57032 |

Los puertos actuales de producción en `docker-compose.prod.yml` (57000 y 57001)
se uniformarían a los de esta tabla.

## Secretos por Environment

Cada entorno define sus propios secretos (nada compartido en el repo):

| Grupo | Secretos |
| --- | --- |
| Conexión SSH | `SSH_HOST`, `SSH_USER`, `SSH_KEY` (privada ed25519), `SSH_PORT`, `DEPLOY_PATH` |
| Postgres | `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` |
| Backend DB | `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_DATABASE` |
| Auth | `JWT_SECRET` (mín. 32 chars), `JWT_ACCESS_TTL`, `JWT_REFRESH_TTL` |
| IA | `AI_DEFAULT_PROVIDER`, `MINIMAX_API_KEY`, `MINIMAX_MODEL` |
| App | `TZ`, `PORT`, `HOST`, `NODE_ENV`, `LOG_LEVEL`, `API_PREFIX` |

Los **Environments** se configuran en los repos que despliegan:

- `atl-back` → `desarrollo`
- `tonatiuh-front` → `desarrollo`
- `tlalli-infra` → `desarrollo`, `staging`, `produccion`

Sin *required reviewers* en `desarrollo` (automático). En `staging` y
`produccion` queda por definir si se exige aprobación.

## Healthcheck

El backend expone:

- `GET /api/v1/health/ready` — *readiness* (disponibilidad).
- `GET /api/v1/health/live` — *liveness* (proceso arriba).

El deploy debe terminar con un `curl -f` a `/api/v1/health/ready`.

## Ramas e issues propuestos

El despliegue de desarrollo vive en `back` y `front`; el aprovisionamiento del
servidor, en `infra`.

| Repo | Rama propuesta | Issue |
| --- | --- | --- |
| `tlalli-infra` | `ci/issue-12-stack-dev` | infra#12 — aprovisionar servidor + stack dev |
| `atl-back` | `ci/issue-<N>-deploy-dev` | por crear — autodespliegue a desarrollo (backend) |
| `tonatiuh-front` | `ci/issue-<M>-deploy-dev` | por crear — autodespliegue a desarrollo (frontend) |
| `tlalli-infra` | `ci/issue-14-deploy-staging` | infra#14 — deploy a staging |
| `tlalli-infra` | `ci/issue-15-deploy-prod` | infra#15 — deploy a producción |

## Pendientes (decisiones abiertas)

1. **Registry** definitivo (propuesta: GHCR).
2. **Modelo de desarrollo**: compose por-repo con red externa (propuesto) vs. un
   `docker-compose.dev.yml` central en `infra`.
3. **Renumerar** producción (57000/57001 → 57030/57031) para uniformar.
4. **Reencuadre de issues**: crear los issues de dev-deploy en `back`/`front` y
   ajustar `infra#12`.
5. **Aprobaciones** en `staging`/`produccion` (¿quiénes aprueban?).
6. Implementación de staging/producción con imágenes y `versions.yml`.
