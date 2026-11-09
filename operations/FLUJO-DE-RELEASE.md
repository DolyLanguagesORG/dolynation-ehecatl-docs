# El flujo de release, de punta a punta

Este documento explica **cómo viaja un cambio desde un PR hasta producción**,
qué se hace automático y qué requiere una persona, y por qué hay cuatro
ambientes.

Es el mapa de referencia del proyecto: cuando algo no esté claro, se empieza
por aquí.

Todo lo que está descrito aquí **se ha ejecutado de verdad** al menos una
vez. Donde algo es manual, está dicho como manual.

---

## 1. El mapa de un vistazo

```
   PR de feature  ──►  develop  ──►  PR "chore(release)"  ──►  tag vX.Y.Z
   (1 aprobación)      (CI verde)     (merge automático)       + manifiesto
                                                                   │
                                                                   v
                                    rc-<app_version> en los 4 repos
                                    (una sola a la vez: el guard)
                                                                   │
             ┌─────────────────────────────────────────────────────┤
             v                                                     v
   REHEARSAL (simulación)                                  STAGING (preproducción)
   se despliega solo                                        se despliega SOLO si el
   smoke test 8/8                                           smoke de rehearsal pasó
             │                                                     │
             └──────────────────────► smoke test 8/8 ◄────────────┘
                                           │
                                           v
                              PR rc -> main  (2 aprobaciones + code owner
                              + gate de staging en verde)
                                           │
                                           v
                              cascada: PRs rc -> main en back y front
                                           │
                                           v
                              PRODUCCIÓN: se dispara a mano y lo aprueban
                              2 revisores (sin self-review)
```

**Lo importante de este mapa:** nada llega a producción sin haber pasado por
rehearsal **y** por staging. El gate de `main` lo impone GitHub de forma
nativa: si no hay un deployment exitoso del environment `staging` para ese
commit, el PR a `main` no se puede mergear.

---

## 2. La máquina de versionado: qué es `chore(release): v0.3.2`

Es el PR que `release-please` abre (o actualiza) **solo**, en cada
repositorio, cuando algo entra a `develop`.

### De dónde sale el número

`release-please` lee los mensajes de commit (Conventional Commits) de todo
lo que se fusionó a `develop` desde la última release y decide el salto:

| Tipo de commit | Salto | Ejemplo |
| --- | --- | --- |
| `fix: ...` | patch (0.3.1 → 0.3.2) | corrige un error |
| `feat: ...` | minor (0.3.2 → 0.4.0) | agrega algo |
| `feat!: ...` | major (0.4.0 → 1.0.0) | rompe la API |
| `docs:`, `chore:`, `ci:`, `test:` | no cuentan | no cambian el número |

La decisión se puede forzar con un commit `Release-As: 1.0.0` en el PR de
release: el número que digas es el que sale.

### Qué lleva dentro

- `package.json` / `version.txt`: la versión de **ese** repositorio.
- `CHANGELOG.md`: el resumen de lo que trae la versión.
- `versions.yml`: la fila de ese repositorio en el manifiesto (versión, tag
  y commit exacto).

### Cada cuánto sale

**En cada merge a `develop`.** No hay que pedirlo ni escribir nada: si hubo
un `fix`, sale `v0.3.2`; si hubo un `feat`, sale `v0.4.0`.

### Qué pasa al mergearlo

1. Se publica el **tag** `v0.3.2` y la GitHub Release.
2. Se dispara `build-images` con ese tag: la imagen se construye **por
   architecturas** (`amd64` y `arm64`) y se publica en GHCR con dos
   etiquetas: el **SHA** del commit (inmutable, la que se despliega) y la
   **versión** (cómoda de leer).
3. Se dispara `sync-versions`: actualiza la fila de ese repositorio en
   `versions.yml` con versión, tag y commit, y abre un PR con ese cambio.

### El manifiesto `versions.yml`

Es el único punto donde se coordinan los repositorios. Cada repositorio
versiona por su cuenta, y el manifiesto dice **exactamente qué versión está
publicada en cada uno**:

```yaml
project: dolynation
app_version: 0.3.1        # la versión de la app (backend y frontend)
repositories:
  dolynation-atl-back:
    version: 0.3.1
    tag: v0.3.1
    commit: 6733505cfcd31c385d46dd587e263080be6334bf
  dolynation-tonatiuh-front:
    version: 0.3.1
    tag: v0.3.1
    commit: ca2f039cd01bb511e149dfa55c6256c3682fcceb
  dolynation-tlalli-infra:
    version: 0.3.3
    tag: v0.3.3
    commit: a7b11f9be540c569008e49d77c4a5bfc010e048f
  dolynation-ehecatl-docs:
    version: 0.1.4
    tag: v0.1.4
    commit: a91262a8d7b973abc641bf86f5d1014c420e2c3d
```

`app_version` es **la versión de la aplicación** y sigue a la más alta entre
backend y frontend (los dos componentes que ve el usuario). Infra y docs
versionan su propio software, pero no mandan en la versión de la app.

---

## 3. Las cuatro ramas y los tres ambientes

### Ramas

| Rama | Qué es | Quién entra |
| --- | --- | --- |
| `develop` | donde se trabaja | cualquier PR de feature |
| `rc-<app_version>` | la combinación de versiones candidata | se corta al liberar |
| `main` | lo que está en producción | solo desde `develop` o una `rc` |
| `hotfix/*` | una urgencia en producción | directo a `main` |

### Ambientes

| Ambiente | Puertos | Se despliega | Para qué sirve |
| --- | --- | --- | --- |
| desarrollo | 57010-57012 | merge a `develop` | el día a día del equipo |
| **rehearsal** | 57040-57042 | al empujar una `rc` | simulación: el tren completo sin tocar staging ni producción |
| **staging** | 57020-57022 | al empujar una `rc`, **después** de que rehearsal pase su smoke test | preproducción con datos de prueba |
| producción | 57030-57032 | **a mano**, con 2 revisores | usuarios reales |

Rehearsal y staging comparten el mismo `docker-compose.env.yml`; se
distinguen por `COMPOSE_PROJECT_NAME` y por los puertos. El servidor nunca
compila: baja imágenes de GHCR.

---

## 4. La `rc`: una sola a la vez

La `rc-<app_version>` es la combinación de versiones que se va a promover.
Se corta en **los cuatro repositorios**, en el commit de la release
correspondiente (el del tag `vX.Y.Z`).

El **guard single-flight** (`release-guard`) revisa, en los cuatro repos,
que no exista otra `rc` con otro nombre. Si la hay, el workflow falla con un
mensaje claro y el despliegue no se dispara.

> Por qué importa: si hubiera dos rc a la vez, dos combinaciones distintas
> de versiones podrían llegar a producción sin que nadie lo notara.

El guard corre en el runner de GitHub (consulta las ramas públicas con
`git ls-remote`), sin SSH ni credenciales, y por eso funciona igual en los
cuatro repos, incluido el de documentación.

---

## 5. Qué pasa cuando se empuja la `rc`

Un solo push a `rc-0.3.1` dispara, en paralelo:

| Workflow | Qué hace |
| --- | --- |
| `release-guard` (en los 4 repos) | verifica que no haya otra rc |
| `build-images` (back y front) | construye la imagen (amd64 + arm64) y la publica en GHCR con el SHA y la versión |
| `deploy-rehearsal` (infra) | despliega el ambiente de simulación con las versiones del manifiesto |
| `promote-rc` (infra) | abre el PR `rc -> main` (no lo mergea) |
| `deploy-staging` (infra) | **espera** a que el smoke de rehearsal esté en verde y solo entonces despliega a staging |
| `smoke-test` (infra) | se dispara solo cuando un deploy terminó bien: 8 comprobaciones contra el ambiente |

El **smoke test** verifica, contra el ambiente recién desplegado:

1. que la versión desplegada sea la del manifiesto;
2. que la cabecera `X-App-Version` venga bien;
3. que el login devuelva un token;
4. que `GET /auth/me` responda con ese token;
5. que el frontend cargue;
6. que el proxy del frontend al backend funcione;
7. que el healthcheck de la base de datos responda;
8. que la versión declarada y la que reporta la app coincidan.

Si algo no cuadra, **el smoke falla** y el ambiente se queda con la versión
anterior: no se promueve nada.

---

## 6. Las cuatro formas de frenar una versión

1. **En el PR de release**: "Request changes" o cerrarlo. El bot lo vuelve
   a abrir en el siguiente push a `develop`; para detenerlo de verdad, un
   commit `Release-As: <otra-version>`.
2. **En el deploy**: si falla el healthcheck o el smoke, el ambiente se
   queda con la versión anterior y no se promueve.
3. **En el checklist de salida** (`operations/CHECKLIST-SALIDA-STAGING.md`):
   una persona lo recorre y lo firma. Si algo no está bien, no se firma y no
   se abre el PR a `main`.
4. **En el PR a `main`**: 2 aprobaciones + code owner + el gate de staging.

Y el último freno, en producción: el environment `prod` tiene **2 revisores
y no permite auto-aprobación**. GitHub pausa el workflow antes de tocar el
servidor.

---

## 7. Quién puede hacer qué (las reglas del repo)

| Regla | Alcance |
| --- | --- |
| 1 aprobación + CI en verde | `develop` |
| Bypass del scrum master | **solo `develop`** (`can_bypass: always`) |
| 2 aprobaciones + code owner | `main` |
| Gate de staging en `main` | `main` (required deployment del environment `staging`) |
| Sin bypass | `main` (`can_bypass: never`) |
| 2 revisores, sin self-review | environment `prod` |

El bypass de `develop` existe porque el scrum master es quien aprueba y
mergea; el de `main` **no** existe: los releases a producción se miran entre
dos.

---

## 8. Rollback

El backend se despliega por **SHA**, que es inmutable. Para volver atrás:

```bash
# en el servidor, con ORG_DIR del ambiente
IMAGE_TAG=<sha-anterior> COMPOSE_PROJECT_NAME=doly-staging \
  DB_HOST_PORT=57020 BACKEND_HOST_PORT=57021 FRONTEND_HOST_PORT=57022 \
  bash /srv/doly/staging/dolynation-tlalli-infra/scripts/deploy-env.sh
```

El `deploy-env.sh` lee el manifiesto, baja esa imagen exacta y levanta el
stack. Como la imagen es inmutable, el rollback es exacto: no depende de que
"la versión 0.3.1" siga siendo la misma.

---

## 9. Lo que se hace automático y lo que no

| Paso | Automático | Quién decide |
| --- | --- | --- |
| Número de versión | sí | release-please, según los commits |
| PR de release | sí | release-please |
| Tag y GitHub Release | sí | release-please, al mergear el PR |
| Imagen en GHCR | sí | `build-images` (push a develop, rc o tag) |
| Manifiesto `versions.yml` | sí | `sync-versions` |
| Despliegue a rehearsal | sí | al empujar la `rc` |
| Smoke test | sí | `workflow_run` tras cada deploy |
| Despliegue a staging | sí | al empujar la `rc`, si rehearsal pasó |
| PR `rc -> main` | sí (se abre) | **una persona lo mergea** |
| Aprobaciones de `main` | no | 2 revisores + code owner |
| Despliegue a producción | **no** | alguien lo dispara y lo aprueban 2 revisores |

---

## 10. Si algo falla, dónde mirar

| Síntoma | Dónde |
| --- | --- |
| El PR de release no se mergea solo | el ruleset de `develop` pide 1 aprobación y el PR lo abre la misma cuenta: hay que aprobarlo con otra cuenta o usar el bypass del scrum master |
| "Permission denied (publickey)" en un deploy | el secret `DEPLOY_SSH_KEY` del environment no corresponde a la llave del servidor |
| "not found" al bajar una imagen | la imagen no se construyó: el `build-images` del commit del manifiesto no corrió o no se publicó |
| "exec format error" al arrancar | la imagen no es de la arquitectura del servidor (arm64): el build tiene que ser multi-arquitectura |
| El smoke test falla con URLs vacías | se disparó sin deploy: el smoke solo corre cuando el deploy terminó bien |
| El PR a `main` no se puede mergear | falta el deployment de staging de ese commit (gate nativo de GitHub) |

---

Ver también: `CI-CD-Y-VERSIONADO.md` (por qué así), `PLAN-DE-DESPLIEGUE.md`
(detalle de los ambientes) y `CHECKLIST-SALIDA-STAGING.md` (la lista que
decide si el MVP está listo).
