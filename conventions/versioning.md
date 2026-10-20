# Versionado

El proyecto usa [Semantic Versioning](https://semver.org/lang/es/) (`vX.Y.Z`) y
**versionado automático al llegar a `main`**: los Conventional Commits
determinan la próxima versión.

**La versión se declara en el repositorio, no solo en el tag.** En el backend y
el frontend vive en el campo `version` del `package.json`; en el repositorio de
documentación y en el de infraestructura, en la sección del `CHANGELOG.md`. El
tag se crea **solo si ese número coincide** con el que el workflow ha
calculado. Así el número que se ve en el código, en el changelog, en el tag y
en `/health` es siempre el mismo, y nadie tiene que confiar en la memoria.

## Cómo funciona

El versionado es **automático al llegar a `main`**: el workflow
[`.github/workflows/release.yml`](../.github/workflows/release.yml) se dispara
en cada `push` a `main` (y también a mano con `workflow_dispatch`) y hace lo
siguiente:

1. Calcula la versión siguiente a partir del **último tag `vX.Y.Z`** y de los
   commitsConventional Commits merges en `main` (`feat` y `fix` bumpean
   *minor* y *patch*; `BREAKING CHANGE` bumpea *major*). Se puede forzar el
   bump con la entrada `bump` del workflow.
2. **Verifica que la versión esté declarada en el repositorio**:
   - si hay `package.json`, su campo `version` debe ser exactamente la versión
     que se va a publicar;
   - si hay `CHANGELOG.md`, debe existir la sección `## [X.Y.Z]` de esa versión.
   Si algo no cuadra, el workflow **falla con un mensaje explícito** y no crea
   el tag. No hace falta que el workflow escriba en el repositorio (eso no
   puede hacerse sobre una rama protegida): la versión la sube una persona en
   el pull request de la release.
3. Crea un **tag anotado** `vX.Y.Z` y lo publica.
4. Publica la **GitHub Release** con las notas generadas entre el tag anterior
   y `HEAD`.

`main` solo recibe merges de `develop` (y `hotfix/*`), de modo que **cada run
del workflow corresponde a una release**. Durante el desarrollo normal **no hay
tags**: el tag nace al llegar a `main`. El detalle del pipeline está en
[CI-CD-Y-VERSIONADO.md](../operations/CI-CD-Y-VERSIONADO.md).

## Dónde vive cada versión

| Repositorio | Dónde se declara | Quién la sube |
| --- | --- | --- |
| `dolynation-atl-back` | `package.json` → `version` | El PR de la release |
| `dolynation-tonatiuh-front` | `package.json` → `version` | El PR de la release |
| `dolynation-tlalli-infra` | `CHANGELOG.md` → `## [X.Y.Z]` | El PR de la release |
| `dolynation-ehecatl-docs` | `CHANGELOG.md` → `## [X.Y.Z]` | El PR de la release |
| **Manifiesto del proyecto** | `dolynation-tlalli-infra/versions.yml` | El PR de la release |

`versions.yml` es el **manifiesto**: una tabla con la versión publicada de cada
repositorio y la fecha de la entrega. Sirve para saber de un vistazo si los
cuatro repos van juntos o si uno se quedó atrás.

## El pull request de la release

Antes de mergear `develop` → `main`, el pull request tiene que subir la versión
en los repositorios afectados:

1. `package.json` → `version` (backend y frontend) y el `package-lock.json`.
2. `CHANGELOG.md` → una sección `## [X.Y.Z]` con lo que trae la release.
3. `versions.yml` → la versión de cada repositorio.

Si el número no coincide con el que el workflow calcula, **la release no sale**
y el workflow dice exactamente qué corregir. Es un error que se ve en el merge, no
después del despliegue.

> **Pendiente (fuera de la entrega del 1-10 dic).** El versionado con
> *release-please* (PR de release acumulativo contra `develop`) está diseñado
> en `infra#7`, que quedó en el milestone «Fuera de alcance (post-entrega)».
> Hasta entonces, el mecanismo vigente es el script de `release.yml` descrito
> arriba.

## Reglas de bump

Como el merge es squash, el subject del commit resultante es el **título del
PR**. Ese título es el que decide el bump:

| Patrón en el título del PR                       | Bump   | Resultado             |
| ------------------------------------------------ | ------ | --------------------- |
| `fix(scope): ...`                                | patch  | `v0.1.0` → `v0.1.1`   |
| `refactor(scope): ...`, `chore(...)`, `docs(...)`| patch  | `v0.1.0` → `v0.1.1`   |
| `feat(scope): ...`                               | minor  | `v0.1.0` → `v0.2.0`   |
| `feat(scope)!: ...` (bang)                       | major  | `v0.1.0` → `v1.0.0`   |
| Cualquier tipo con `BREAKING CHANGE:` en el body | major | `v0.1.0` → `v1.0.0`   |

La lista de tipos es la misma de [commits.md](./commits.md). El título del PR
lo valida el check `pr-title` de CI **antes** de poder mergear, así que un
título inválido nunca llega a la release.

## Línea de tiempo del proyecto

| Versión  | Significado                                                        |
| -------- | ------------------------------------------------------------------ |
| `v0.1.0` | Primer release.                                                      |
| `v0.x.y` | Iteración durante el desarrollo. Cada merge a `main` bumpea.         |
| `v1.0.0` | Release final del entregable de diciembre.                          |

## Forzar un bump

Si el título no refleja el cambio real (por ejemplo, un `chore` que rompe la
API), dispara el workflow a mano y fuerza el bump:

```bash
gh workflow run release.yml -f bump=minor
```

## Ejemplo de flujo completo

```bash
# 1. Trabajo normal en una rama
git checkout -b feat/issue-8-settings
npm run verify    # en el repo correspondiente (atl-back / tonatiuh-front)
git commit -m "feat(users): persist study preferences in user_preferences"
git push -u origin feat/issue-8-settings

# 2. PR con título Conventional Commits hacia develop
gh pr create --base develop \
  --title "feat(users): persist study preferences in user_preferences" \
  --body "Closes #8"

# 3. PR de release: subir la versión en package.json / CHANGELOG.md
#    y en versions.yml (infra), y añadir la sección del changelog.
npm version 0.2.0 --no-git-tag-version   # backend y frontend
#    y en CHANGELOG.md:  ## [0.2.0] - 2026-12-10

# 4. Mergear develop -> main.
#    El workflow verifica la versión, crea el tag y publica la release.
```

Al llegar el merge a `main`, `release.yml` calcula la versión a partir de los
commits, **comprueba que el repositorio declare esa misma versión**, crea el
tag anotado y publica el GitHub Release con las notas. Si no coincide, la
release se detiene y avisa de qué archivo hay que corregir.

## Notas

- El primer release publica `v0.1.0` como base.
- Los tags son anotados (`git tag -a`), no lightweight, para que `git describe`
  y el historial conserven la fecha y el mensaje.
- Si un ciclo no tiene commits que bumpeen versión, el workflow aborta con un
  error explícito: no se crean tags vacíos ni duplicados.
- El backend expone la **versión y el commit** en `GET /api/v1/health/live` y
  `GET /api/v1/health/ready`, así que en el servidor se puede comprobar qué
  build está corriendo.
