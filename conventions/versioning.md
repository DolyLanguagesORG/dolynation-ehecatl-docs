# Versionado

El proyecto usa [Semantic Versioning](https://semver.org/lang/es/) (`vX.Y.Z`) y
**versionado automático en `develop`**: los Conventional Commits determinan la
próxima versión.

**La versión se declara en el repositorio, no solo en el tag.** En el backend y
el frontend vive en el campo `version` del `package.json`; en el repositorio de
infraestructura y en el de documentación, en `version.txt`. El changelog lleva
la sección `## [X.Y.Z]` de cada versión. Así el número que se ve en el código,
en el changelog, en el tag y en `/health` es siempre el mismo, y nadie tiene
que confiar en la memoria.

## Cómo funciona

Cada repositorio corre
[release-please](https://github.com/googleapis/release-please) con el workflow
`.github/workflows/release-please.yml` de su repo, que se dispara en cada
`push` a `develop` (y también a mano con `workflow_dispatch`) y hace lo
siguiente:

1. Calcula la versión siguiente a partir del **último tag `vX.Y.Z`** y de
   **todos** los commits del ciclo, no solo del último (`feat` bumpea *minor*,
   `fix` bumpea *patch*; `BREAKING CHANGE` bumpea *major*).
2. Mantiene un **pull request de release** con la versión ya subida en los
   archivos del repositorio y la sección del changelog correspondiente.
3. Al mergear ese PR, crea un **tag anotado** `vX.Y.Z` y publica la **GitHub
   Release** con las notas generadas entre el tag anterior y `HEAD`.

El PR de release tiene **auto-merge activado**: se mergea solo cuando los
checks están en verde.

> **Nota:** el tag nace **en `develop`**, no en `main`. Así el número de versión
> se ve subir mientras se trabaja, en lugar de quedarse congelado hasta la
> entrega. `main` sigue siendo producción y recibe los merges de `develop`.

`main` solo recibe merges de `develop` (y `hotfix/*`). El detalle del pipeline
está en [CI-CD-Y-VERSIONADO.md](../operations/CI-CD-Y-VERSIONADO.md).

## Dónde vive cada versión

| Repositorio | Dónde se declara | Quién la sube |
| --- | --- | --- |
| `dolynation-atl-back` | `package.json` → `version` | El bot (release-please) |
| `dolynation-tonatiuh-front` | `package.json` → `version` | El bot (release-please) |
| `dolynation-tlalli-infra` | `version.txt` | El bot (release-please) |
| `dolynation-ehecatl-docs` | `version.txt` | El bot (release-please) |
| **Manifiesto del proyecto** | `dolynation-tlalli-infra/versions.yml` | El bot (release-please) |

`versions.yml` es el **manifiesto**: una tabla con la versión publicada de cada
repositorio y la fecha de la entrega. Sirve para saber de un vistazo si los
cuatro repos van juntos o si uno se quedó atrás.

> **El manifiesto lo actualiza el bot**, en su PR de release: el workflow
> `versions-manifest.yml` lo valida contra los tags reales y avisa si algún
> repositorio se quedó atrás.

## El pull request de la release

El versionado es **automático en `develop`**: cada repositorio corre
[release-please](https://github.com/googleapis/release-please), que mantiene un
**pull request de release acumulativo** contra `develop`.

```
PR de feature ──► develop ──► el bot actualiza el PR de release
                                  │
                                  └──► se mergea ──► tag vX.Y.Z + GitHub Release
```

El bot calcula el salto a partir de **todos** los commits del ciclo (no solo
del último), actualiza los archivos de versión y el changelog, y deja el PR
listo para mergearse. Al mergearlo se publica el tag y la Release.

Los archivos que toca, por repositorio:

| Repositorio | Archivos que actualiza el bot |
| --- | --- |
| `dolynation-atl-back` | `package.json`, `package-lock.json`, `CHANGELOG.md` |
| `dolynation-tonatiuh-front` | `package.json`, `package-lock.json`, `CHANGELOG.md` |
| `dolynation-tlalli-infra` | `version.txt`, `CHANGELOG.md`, `versions.yml` |
| `dolynation-ehecatl-docs` | `version.txt`, `CHANGELOG.md` |

El bot usa un **PAT** (`RELEASE_PLEASE_TOKEN`), no el `GITHUB_TOKEN` del
workflow: el `GITHUB_TOKEN` no dispara otros workflows, así que los checks
requeridos nunca correrían en el PR del bot y el merge se quedaría bloqueado.

> **Nota:** `develop` es la rama donde vive el trabajo y es la que se despliega
> al servidor. El tag nace **en `develop`**, no en `main`: así el número de
> versión se ve subir mientras se trabaja, en lugar de quedarse congelado
> durante semanas. `main` sigue siendo producción y recibe los merges de
> `develop`.

### Versiones independientes

Cada repositorio **escala por su cuenta**: `atl-back` puede estar en `0.3.0`
mientras `tlalli-infra` está en `0.2.0`, según lo que cambió en cada uno. Nadie
bloquea a nadie.

`versions.yml` (en `dolynation-tlalli-infra`) es el **manifiesto** que dice
dónde está cada repositorio, y lo mantiene actualizado el propio bot. El
workflow `versions-manifest.yml` lo valida contra los tags reales: si un
repositorio se queda atrás, avisa.

### Del `develop` a producción

`main` recibe los merges de `develop` y es la rama que se despliega a
producción. Cuando se acuerda una versión concreta para salir, se toman los
tags de `versions.yml` y se despliega la aplicación completa con esa
combinación de versiones.

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

> **El bump se calcula con TODOS los commits del ciclo, no solo con el último.**
> Como los merges son squash, el subject de cada commit es el título de su PR.
> Si un ciclo incluye un `feat` y el **último** PR fusionado fue un `chore`, una
> funcionalidad quedaría numerada como un ajuste menor. release-please recorre
> el ciclo completo, así que no ocurre.

## Línea de tiempo del proyecto

| Versión  | Significado                                                        |
| -------- | ------------------------------------------------------------------ |
| `v0.1.0` | Primer release.                                                      |
| `v0.x.y` | Iteración durante el desarrollo. Cada merge a `main` bumpea.         |
| `v1.0.0` | Release final del entregable de diciembre.                          |

## Publicar una versión exacta

A veces hace falta publicar una versión concreta y no la que saldría del
cálculo: el caso claro es la **entrega final**, donde los cuatro repositorios
tienen que pasar a `v1.0.0` el mismo día.

## Publicar una versión exacta

A veces hace falta publicar una versión concreta y no la que saldría del
cálculo: el caso claro es la **entrega final**, donde los cuatro repositorios
tienen que pasar a `v1.0.0` el mismo día.

Con release-please eso se hace con un commit `Release-As: X.Y.Z`, que fija la
próxima versión sin calcular el bump:

```bash
# En cada repositorio: un commit vacío con el mensaje "Release-As: 1.0.0"
git commit --allow-empty -m "Release-As: 1.0.0"
git push origin develop
```

El bot toma ese número tal cual, lo sube en los archivos de versión y deja el
PR de release listo para mergearse.

> **Los cuatro repositorios no se versionan a la vez.** Cada uno tiene su propio
> release-please y su propio tag. Para la entrega hay que hacer el commit
> `Release-As` en los cuatro y comprobar que `versions.yml` refleja los cuatro
> tags.

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

# 3. Merge a develop. El bot actualiza el PR de release con la nueva versión
#    (0.1.0 -> 0.2.0, porque el ciclo incluye un feat) y lo deja con
#    auto-merge: se mergea solo cuando los checks están en verde.

# 4. Al mergear el PR de release: tag v0.2.0 y GitHub Release.
```

Al llegar el merge a `develop`, el bot ya dejó la versión declarada en el
repositorio (package.json o version.txt), en el changelog y en el manifiesto.
Al mergearse su PR de release, publica el tag anotado y la GitHub Release con
las notas.

### La entrega final (`v1.0.0`)

La entrega es el caso en que la versión no sale del cálculo, sino que se
indica a mano. En los cuatro repositorios:

```bash
# 1. En cada repo, subir la versión y la sección del changelog
#    backend y frontend:  npm version 1.0.0 --no-git-tag-version
#    infra y docs:         añadir "## [1.0.0] - 2026-12-10" al CHANGELOG.md
#    infra:                versions.yml con los cuatro tags en 1.0.0

### La entrega final (`v1.0.0`)

La entrega es el caso en que la versión no sale del cálculo, sino que se
indica a mano. En los cuatro repositorios:

```bash
# 1. En cada repo, un commit que fija la versión exacta
git commit --allow-empty -m "Release-As: 1.0.0"
git push origin develop

# 2. Mergear el PR de release que el bot deja listo (un PR por repositorio)

# 3. Mergear develop -> main (un PR por repositorio)
```

El bot sube la versión en los archivos de cada repositorio y en el manifiesto
(`versions.yml` en infra), que es lo que dice qué versión va en cada uno.

> Los cuatro repositorios **no se versionan a la vez**: cada uno crea su tag
> en su propio run. Hay que comprobar los cuatro al terminar.

## Notas

- Los tags son anotados (`git tag -a`), no lightweight, para que `git describe`
  y el historial conserven la fecha y el mensaje.
- El bot solo crea un tag cuando hay cambios que lo ameritan: si un ciclo no
  tiene commits que bumpeen versión, no genera un PR de release vacío.
- El backend expone la **versión y el commit** en `GET /api/v1/health/live` y
  `GET /api/v1/health/ready`, así que en el servidor se puede comprobar qué
  build está corriendo. La raíz de la API y el documento OpenAPI reportan la
  misma versión.
