# Versionado

El proyecto usa [Semantic Versioning](https://semver.org/lang/es/) (`vX.Y.Z`)
y **versionado automático con
[release-please](https://github.com/googleapis/release-please)**: los
Conventional Commits determinan la próxima versión y nadie edita un número a
mano.

## Cómo funciona

`release-please`
([`.github/workflows/release.yml`](../.github/workflows/release.yml)) mantiene
**un PR de release acumulativo** contra `develop`:

1. Cada PR mergeado a `develop` (squash) es un Conventional Commit y se suma
   al PR de release abierto.
2. El PR de release se titula `chore(release): release vX.Y.Z` y va subiendo
   la versión propuesta según los commits acumulados.
3. Al mergear **ese** PR, `release-please` actualiza la versión, crea el
   **tag anotado** y publica el GitHub Release con las notas.
4. `release-please` abre de nuevo un PR de release limpio para el ciclo
   siguiente.

Durante el desarrollo normal **no hay tags**: el tag nace al mergear el PR de
release. El promote a `main` (producción) es un PR aparte; el detalle del
pipeline está en [CI-CD-Y-VERSIONADO.md](../operations/CI-CD-Y-VERSIONADO.md).

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
| `v0.1.0` | Primer release. Se crea al mergear el primer PR de release.         |
| `v0.x.y` | Iteración durante el desarrollo. Cada PR de release mergeado bumpea.|
| `v1.0.0` | Release final del entregable de diciembre.                         |

## Forzar un bump

Si el título no refleja el cambio real (por ejemplo, un `chore` que rompe la
API), añade un footer al commit (o al body del PR de release):

```
Release-As: 1.0.0
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

# 3. Cuando toca release: mergear el PR de release-please.
#    Ese PR acumula los commits y propone vX.Y.Z.
```

Al mergear el PR de release, `release-please` regenera la versión, crea el tag
y publica el GitHub Release con las notas de los commits incluidos.

## Notas

- El primer release publica `v0.1.0` como base.
- Los tags son anotados (`git tag -a`), no lightweight, para que `git describe`
  y el historial conserven la fecha y el mensaje.
- Si un ciclo no tiene commits que bumpeen versión, `release-please` no abre
  PR de release: no se crean tags vacíos.
