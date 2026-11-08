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
| Llave SSH | **Con passphrase**, cargada en un **agente SSH** durante el job (el runner no es interactivo) |
| Usuario de despliegue | **`ddeploy`**, sin sudo ni shell interactivo; su `authorized_keys` usa `restrict` (sin forwarding, sin PTY) |
| Publicación | **nginx** delante, con **Origin Certificate** de Cloudflare. Los contenedores escuchan **solo en `127.0.0.1`** |
| Merge | **Solo squash** (ya forzado por los rulesets) |
| `rc-<version>` | **No es un entorno**: rama/estado efímero y *single-flight* |

### El servidor de desarrollo

| Dato | Valor |
| --- | --- |
| IP | `141.148.148.45` |
| Sistema | Ubuntu 24.04.5, Docker 29.9.1, Compose v5.6.0, nginx 1.24.0 |
| Raíz de los repos | `/srv/doly/dev` (los tres repos, hermanos) |
| Red de Docker | `doly-dev-net` (definida en `docker-compose.dev.yml`) |
| Puertos | `57010` (DB), `57011` (backend), `57012` (frontend), **solo en `127.0.0.1`** |
| Proxy | nginx en `80` (redirige) y `443` (Cloudflare) |
| DNS | `devweb.yacaterkos.tech` → frontend, `devapi.yacaterkos.tech` → API |

> El `compose` de desarrollo vive **solo** en `dolynation-tlalli-infra` y
> levanta los tres contenedores a la vez. No hay un compose por repositorio:
> el `PLAN-DE-DESPLIEGUE.md` anterior lo contemplaba, pero el modelo real es
> un compose central en infra que monta `../dolynation-atl-back` y
> `../dolynation-tonatiuh-front`.

### TLS

Cloudflare gestiona el TLS con el navegador. El tramo Cloudflare → origen va
cifrado con un **Origin Certificate**, que solo es válido entre Cloudflare y
el servidor: el navegador nunca negocia TLS contra el origen y el certificado
no sale del servidor. El CSR se genera en el servidor y se emite en el panel
de Cloudflare.

Detalle operativo en
[`nginx/README.md`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/blob/develop/nginx/README.md).

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

- `atl-back` y `tonatiuh-front` construyen y **publican su imagen** en GHCR
  (`ghcr.io/dolylanguagesorg/...`), con dos etiquetas: el **SHA** del commit
  y la **versión**.
- `tlalli-infra` **jala la imagen** y despliega el stack con
  `scripts/deploy-env.sh`, que lee `versions.yml` y despliega exactamente las
  versiones declaradas.

> **El servidor nunca compila.** Si dos máquinas compilaran el mismo commit,
> no serían el mismo binario. Una imagen es inmutable: se sabe exactamente qué
> corre y se puede volver atrás.

**El backend se despliega por SHA** (inmutable: es lo que corre y lo que
permite el rollback) y **el frontend por versión**.

### El ambiente de simulación

`rehearsal` es un tercer ambiente, en el mismo servidor y con el mismo camino
de código que staging y producción, pero en otro directorio (`/srv/doly/rehearsal`)
y otros puertos (`5704x`). No sale a internet.

Existe para **probar el tren completo sin tocar staging ni producción**:
`develop` → `rc-<version>` → despliegue → healthcheck → smoke test. Es el
mismo `docker-compose.env.yml` con otros puertos, así que lo que se prueba
allí es exactamente lo que irá a producción.

| Ambiente | Directorio | Puertos | Sale a internet |
| --- | --- | --- | --- |
| Desarrollo | `/srv/doly/dev` | 57010-57012 | sí (`devweb`, `devapi`) |
| Rehearsal | `/srv/doly/rehearsal` | 57040-57042 | no |
| Staging | `/srv/doly/staging` | 57020-57022 | sí (`stagingweb`) |
| Producción | `/srv/doly/prod` | 57030-57032 | sí (`yacaterkos.tech`, `www`) |

### Verificación del despliegue

`scripts/smoke-test.sh` comprueba que el ambiente cumple el contrato (la API
responde, la versión es la del manifiesto, el login funciona, el frontend
sirve y su proxy llega al backend) y **falla** si algo no cuadra. Un smoke
test que no puede fallar no sirve de nada.

Lo que no se puede automatizar (que la lectura generada tenga sentido, que el
diseño se vea bien) lo verifica una persona con el checklist de salida.

## Entornos y puertos

| Entorno | Directorio (server) | DB | Back | Front |
| --- | --- | --: | --: | --: |
| Desarrollo | `/srv/doly/dev` | 57010 | 57011 | 57012 |
| Rehearsal | `/srv/doly/rehearsal` | 57040 | 57041 | 57042 |
| Staging | `/srv/doly/staging` | 57020 | 57021 | 57022 |
| Producción | `/srv/doly/prod` | 57030 | 57031 | 57032 |

Staging, producción y rehearsal comparten el mismo
`docker-compose.env.yml` de `infra`; lo que cambia son los puertos y el
nombre del proyecto. Todos escuchan **solo en `127.0.0.1`**: el único que
llega a los contenedores es el proxy (nginx) de este servidor.

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

- `atl-back` → `desarrollo`, `staging`, `produccion`, `rehearsal`
- `tonatiuh-front` → `desarrollo`, `staging`, `produccion`, `rehearsal`
- `tlalli-infra` → `desarrollo`, `staging`, `produccion`, `rehearsal`

| Environment | Required reviewers | Self-review | Uso |
| --- | --- | --- | --- |
| `desarrollo` | ninguno | — | autodespliegue en cada merge a `develop` |
| `rehearsal` | ninguno | — | la simulación: el tren completo, sin salir a internet |
| `staging` | ninguno | — | despliegue de la `rc-<version>`, automático |
| `produccion` | **2** (Azael y Elías) | **bloqueado** | promoción a producción |

> **Un Environment con required reviewers no es lo mismo que "2 aprobaciones
> en el PR".** El PR con 2 aprobaciones dice "el código está bien revisado".
> El Environment dice "**alguien decide que esto sale a producción ahora**".
> Para producción se quiere las dos cosas.

`POSTGRES_PASSWORD`, `DB_PASSWORD` y `JWT_SECRET` son **propios de cada
ambiente**: un token de staging no tiene que valer en producción. La llave
SSH sí es la misma (`ddeploy` sirve para los tres).

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

1. **Rollback de un comando**: falta registrar automáticamente el SHA
   desplegado anterior y un job que lo restaure. Hoy el rollback es cambiar
   `IMAGE_TAG` y volver a desplegar (`infra#27`).
2. **Los registros DNS** de `stagingweb` (los crea el SM).
3. **El primer despliegue real** a staging y a producción, cuando se autorice.
4. **Publicar las imágenes en GHCR** de verdad: las de prueba se construyeron
   en local, no se publicaron.

## Decisiones ya tomadas

| Decisión | Valor |
| --- | --- |
| Registry | **GHCR** (`ghcr.io/dolylanguagesorg/...`) |
| Modelo de desarrollo | un `docker-compose.dev.yml` central en `infra` que monta los otros dos repos |
| Puertos | 5701x dev, 5702x staging, 5703x producción, 5704x rehearsal |
| Aprobaciones | `produccion` con 2 required reviewers y sin self-review; los demás, automáticos |
| Etiqueta de imagen | **SHA** para el backend (inmutable, la del rollback) y **versión** para el frontend |
