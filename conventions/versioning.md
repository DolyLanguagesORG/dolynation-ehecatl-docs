# Versionado

El proyecto usa [Semantic Versioning](https://semver.org/lang/es/) (`vX.Y.Z`) y
**versionado automático**: los Conventional Commits determinan la versión y
**nadie la escribe a mano**.

El mecanismo es [release-please](https://github.com/googleapis/release-please):
cada repositorio mantiene **un pull request de release acumulativo** contra
`develop`. Al mergear ese PR, la versión sube sola, el changelog se escribe
solo, y se crean el **tag anotado** y la **GitHub Release**.

## El ciclo, de punta a punta

```
PRs de trabajo  ->  develop
                       |
        release-please mantiene UN PR
        "chore(release): vX.Y.Z"
                       |  (merge)
                       v
   version + changelog + tag vX.Y.Z + GitHub Release
```

Mientras el PR de release está abierto, **acumula** todos los cambios que
entran a `develop`. Mergearlo es un acto deliberado: es el momento en que se
publica una versión.

## Reglas de bump

Como los merges son squash, el **título del PR** es el que decide el salto.
release-please mira los commits de todo el ciclo, no solo el último.

| Tipo del commit                                  | Bump   | Resultado             |
| ------------------------------------------------ | ------ | --------------------- |
| `feat(scope):`                                   | minor  | `v0.1.0` → `v0.2.0`   |
| `feat(scope)!:` o `BREAKING CHANGE:`             | major  | `v0.1.0` → `v1.0.0`   |
| `fix(scope):`                                    | patch  | `v0.1.0` → `v0.1.1`   |
| `refactor` `chore` `docs` `ci` `test` `perf` `style` | —    | **no genera versión** |

Los últimos seis tipos están **ocultos** en el changelog por defecto: si un
ciclo solo trae commits de esos tipos, **no se abre PR de release**. Es decir:
**el código genera versiones; la documentación, los refactors y los cambios de
CI no.**

> **El número no cuenta PRs.** Comunica riesgo de compatibilidad. Si entran 5
> PRs juntos, forman **una** release: `v0.2.0` no significa "dos features",
> significa "hay features nuevas y sigue siendo compatible con `0.1.x`". El
> detalle exacto de cada PR queda en el `CHANGELOG.md` de esa release y en el
> commit al que apunta el tag. **Nada se pierde.**

El título del PR lo valida el check `pr-title` de CI **antes** de poder
mergear, así que un título inválido nunca llega a la release.

## Dónde vive cada versión

| Repositorio | Dónde se declara | Quién la sube |
| --- | --- | --- |
| `dolynation-atl-back` | `package.json` → `version` | El PR de release (release-please) |
| `dolynation-tonatiuh-front` | `package.json` → `version` | El PR de release (release-please) |
| `dolynation-tlalli-infra` | `version.txt` | El PR de release (release-please) |
| `dolynation-ehecatl-docs` | `version.txt` | El PR de release (release-please) |
| **Manifiesto del proyecto** | `dolynation-tlalli-infra/versions.yml` | release-please (su propia fila) + el workflow `sync-versions` (las demás) |

El tag, el `CHANGELOG.md` y la versión del repositorio **siempre coinciden**:
los tres los escribe el mismo PR.

## El manifiesto del proyecto

`dolynation-tlalli-infra/versions.yml` es la fuente de verdad de **qué versión
de cada componente compone la aplicación publicada**.

```yaml
project: dolynation
app_version: 0.2.0        # la versión ÚNICA de la aplicación
updated: '2026-11-06'
repositories:
  dolynation-atl-back:
    version: 0.2.1
    tag: v0.2.1
    commit: a8525a278b81eb37b19f9f289e5b87128f9079fc
  dolynation-tonatiuh-front:
    version: 0.2.1
    tag: v0.2.1
    commit: 161a96847dce3352bcc9beb097de0c5d3d986722
  dolynation-tlalli-infra:
    version: 0.2.1
    tag: v0.2.1
    commit: aca29ce9f7bc8b080ca4aee834e0141cdeccc79b
  dolynation-ehecatl-docs:
    version: 0.1.2
    tag: v0.1.2
    commit: bc17498f97664bd50174ec6eb72c2df8320c4f37
release:
  target: 1.0.0
  deadline: '2026-12-10'
```

| Campo | Qué significa |
| --- | --- |
| `app_version` | La versión de la **aplicación** (el tren de release). Es la que ve el usuario final. |
| `repositories.<repo>.version` | La versión de **ese** repositorio. |
| `repositories.<repo>.tag` | El tag exacto que se publicó. |
| `repositories.<repo>.commit` | El commit exacto. Con esto se puede hacer rollback a un estado anterior. |

**Cómo se mantiene solo.** Cada repositorio, al publicar su tag, avisa a
`dolynation-tlalli-infra` con un `repository_dispatch`. El workflow
`sync-versions.yml` actualiza la fila correspondiente y **abre el PR** con el
cambio (nunca un push directo: `develop` está protegido).

> **Dos formatos, dos versiones.** La **aplicación** tiene una versión
> (`app_version`). Cada **componente** tiene la suya. La API expone las dos:
> `GET /api/v1/version` devuelve `appVersion` y `version` por separado.

## La `rc-<version>`: la candidata

La version que se publica es una cosa; la combinacion de versiones que se
**prueba** es otra. Para eso esta la `rc`.

```
develop  --(release-please)-->  tag vX.Y.Z + versions.yml actualizado
                                      |
                                      v
                        rc-<app_version> en los 4 repos
                                      |  (push)
                                      v
              rehearsal -> smoke -> staging -> smoke
                                      |
                                      v
                            PR rc -> main  (2 aprobaciones + code owner)
                                      |
                                      v
                        cascada: PR rc -> main en back, front y docs
                                      |
                                      v
                     deploy-prod  (A MANO, con 2 revisores)
```

Reglas:

| Regla | Por que |
| --- | --- |
| La `rc` se corta en los **cuatro** repos, en el commit de su tag | Todos despliegan la misma combinacion |
| Solo puede existir **una** `rc` a la vez | Si hubiera dos, dos combinaciones distintas podrian llegar a produccion sin que nadie lo notara (lo vigila `scripts/release-guard.sh`) |
| La `rc` **no es un ambiente**: es una rama efimera | Los ambientes son dev, rehearsal, staging y produccion |
| **Fusionar el PR a `main` no publica nada** | `deploy-prod` es manual y espera los 2 revisores del environment `prod`. `main` puede recibir varias promociones seguidas y la que se publica es la que se decide desplegar |
| Al abandonar una candidata: **cerrar el PR y borrar la rama** | Borrarla libera el slot del single-flight. Ojo: **borrar la rc no revierte staging** |

El ciclo completo, con comandos y criterios, esta en
[`operations/FLUJO-DE-RELEASE.md`](../operations/FLUJO-DE-RELEASE.md).

## Prerelease y release oficial

Con `"prerelease": true` en la configuración de release-please:

- Toda versión **0.x** se publica como **Pre-release** en GitHub.
- La **`v1.0.0`** se publica como **release oficial** (sin la marca).

Es el mecanismo de *beta/prerelease → release estable* sin ensuciar el número
con sufijos.

### Fijar una versión exacta

Cuando haya que publicar una versión concreta (por ejemplo, la promoción final),
se usa el trailer `RELEASE AS` en el commit:

```bash
git commit -m "feat(release): preparar la entrega final

RELEASE AS: 1.0.0"
```

release-please lo respeta de forma nativa y publica exactamente esa versión.

## Los tags

release-please crea el tag **lightweight** (apunta al commit, sin objeto de
tag). La convención del equipo es que sean **anotados**, para que `git describe`
y el historial conserven la fecha y el mensaje. El paso *"Convertir el tag en
anotado"* del workflow `release-please.yml` lo resuelve después de crearse,
sin cambiar a qué commit apunta.

## Qué NO se hace

- **No se sube la versión a mano.** Si alguien la edita, el tag y el
  `package.json` dejan de coincidir.
- **No se edita `versions.yml` a mano.** El workflow `sync-versions` lo hace.
- **No se crea el tag a mano.** Los tags salen del PR de release.
- **No se corta una `rc` a mano si ya hay otra.** El guard lo impide: primero
  se consolida la anterior.
- **No se borra una `rc` sin querer.** La rama esta protegida (regla
  `deletion` + bypass solo del scrum master).

## Forzar un bump

Si el título no refleja el cambio real (por ejemplo, un `chore` que rompe la
API), se fuerza con el trailer `RELEASE AS`:

```bash
git commit -m "fix(api): corregir el contrato

RELEASE AS: 0.3.0"
```

## Verificar que todo cuadra

```bash
# La versión del repositorio
cat version.txt            # en infra y docs
node -p "require('./package.json').version"   # en back y front

# El tag y a qué commit apunta
git show v0.2.1 --no-patch

# Lo que está corriendo en el servidor
curl -s https://devapi.yacaterkos.tech/api/v1/health/live
```

La respuesta del healthcheck trae la `version` y el `commit` del build en
ejecución: si coinciden con el tag, lo que corre en el servidor es
exactamente lo publicado.

## Un dry-run antes de tocar nada

release-please se puede ejecutar en local, **sin escribir nada en GitHub**:

```bash
git clone --branch develop https://github.com/DolyLanguagesORG/dolynation-atl-back.git /tmp/prueba
cd /tmp/prueba
export GH_TOKEN=$(gh auth token)
npx release-please@17 release-pr \
  --dry-run --local --local-path . \
  --repo-url DolyLanguagesORG/dolynation-atl-back \
  --target-branch develop \
  --config-file release-please-config.json \
  --manifest-file .release-please-manifest.json \
  --token "$GH_TOKEN"
```

Imprime el bump, el changelog completo y qué archivos cambiaría. Es la forma
rápida de comprobar una configuración antes de publicarla.

## Documentos relacionados

- [`operations/CI-CD-Y-VERSIONADO.md`](../operations/CI-CD-Y-VERSIONADO.md) — el
  pipeline completo y los tres ambientes.
- [`operations/FLUJO-DE-TRABAJO.md`](../operations/FLUJO-DE-TRABAJO.md) — ramas,
  PR y qué reglas bloquean de verdad.
