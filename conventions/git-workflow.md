# Git workflow

Este documento define cómo se mueve el código entre ramas. Es la fuente de
verdad para PRs, merges y hotfixes.

## Diagrama de flujo

```
                     ┌──────────────────┐
                     │ feat/issue-12-*  │
                     │ fix/issue-45-*   │
                     │ docs/issue-20-*  │
                     │ chore/issue-6-*  │
                     └────────┬─────────┘
                              │  PR + checks en verde
                              ▼
                     ┌──────────────────┐
                     │     develop      │  ← integración diaria
                     └────────┬─────────┘
                              │  PR + 1 aprobación + checks
                              ▼
                     ┌──────────────────┐
                     │      main        │  ← producción / release
                     └──────────────────┘

                     ┌──────────────────┐
                     │   hotfix/*       │  ← sale de main, vuelve a develop
                     └──────────────────┘
```

## Convenciones de nombres

El prefijo de la rama coincide con el **tipo de commit** que llevará
(ver [commits.md](./commits.md)), para evitar confusiones alinear
`feat/issue-12-auth-login` con `feat(auth): ...`.

Formato: `tipo/issue-<n>-<módulo>-<detalle>`

- `feat/issue-<n>-...` — nuevas funcionalidades
- `fix/issue-<n>-...` — correcciones
- `refactor/issue-<n>-...` — reescritura sin cambiar comportamiento
- `docs/issue-<n>-...` — solo documentación
- `test/issue-<n>-...` — pruebas
- `chore/issue-<n>-...` — tooling, dependencias, limpieza
- `perf/`, `build/`, `ci/`, `style/` — con el mismo formato
- `hotfix/<detalle>` — corrección urgente sobre producción (sale de `main`)

`<n>` es el **número del issue en su repo** y es obligatorio: toda rama de
trabajo nace de una tarea con issue, para poder trazarla en el tablero de
Projects.

### También se acepta el formato de GitHub

El botón **Create a branch** de un issue crea la rama con el nombre `<n>-<detalle>`,
por ejemplo `12-auth-login`. Ese formato **también lo acepta el check
`pr-target`**, para que usar el botón no implique un CI en rojo.

| | Con prefijo (recomendado) | Formato de GitHub |
| --- | --- | --- |
| Ejemplo | `feat/issue-12-auth-login` | `12-auth-login` |
| Dice el tipo de cambio | Sí, de un vistazo | No |
| Enlaza con el tablero | Sí, por `issue-<n>` | Sí, por el número |
| Sale del botón *Create a branch* | No | Sí |
| Lo acepta `pr-target` | Sí | Sí |

**La forma con prefijo es la recomendada**, porque el prefijo te dice si es una
funcionalidad, un bug o documentación sin abrir la rama. El formato de GitHub es
el atajo para cuando prefieres el botón. No se mezclan en un mismo PR: usa una
o la otra.


Ejemplos:

- `feat/issue-12-auth-login-page`
- `fix/issue-45-header-overflow`
- `chore/issue-6-repo-config`
- `docs/issue-20-git-workflow`

Máximo 50 caracteres en total.

## Reglas por rama

### `develop` (integración diaria)

- Recibe PRs de `feat/issue-*`, `fix/issue-*`, `refactor/issue-*`, `docs/issue-*`,
  `test/issue-*`, `chore/issue-*`, `perf/issue-*`, `build/issue-*`, `ci/issue-*`,
  `style/issue-*` o del formato `<n>-<detalle>` del botón de GitHub.
- Requiere los **status checks de cada repositorio** en verde antes de mergear
  (ver [los checks de CI](#los-checks-de-ci-que-bloquean-el-merge)).
- Requiere **1 aprobación** de cualquier persona con acceso al repositorio.
  Los `CODEOWNERS` se solicitan automáticamente pero **no son obligatorios**
  (`require_code_owner_reviews: false`), ver
  [FLUJO-DE-TRABAJO.md](../operations/FLUJO-DE-TRABAJO.md#codeowners)).
- **Prohibido el push directo**: siempre por PR.
- Solo **squash-merge**, para mantener historia lineal.
- No se permiten force-pushes ni deleciones.
- Todas las conversaciones del PR deben estar resueltas.
- `develop` **no exige** estar al día con la rama base: se puede mergear con
  la rama de trabajo atrasada.

### `main` (producción / release)

- Recibe PRs **únicamente** desde `develop` (excepto hotfixes).
- Requiere los mismos checks del repositorio **más** 1 aprobación.
- **Prohibido el push directo**: siempre por PR.
- Solo **squash-merge**.
- No se permiten force-pushes ni deleciones.
- Al mergear el PR de release, `release-please` crea el tag y la GitHub
  Release (ver [versioning.md](./versioning.md)).

`main` permanece estable entre releases. Durante el desarrollo activo solo
recibe merge en los hitos acordados.

## Procedimiento de hotfix

Para un fix urgente en producción:

1. Crea rama desde `main`:
   ```bash
   git checkout main
   git checkout -b hotfix/<nombre-descriptivo>
   ```
2. Commitea el fix mínimo (ver [commits.md](./commits.md)).
3. Abre PR con título `fix(scope): <descripción>` directo contra `main`.
4. Después de mergearlo en `main`, **cherry-pick** el commit a `develop`:
   ```bash
   git checkout develop
   git cherry-pick <sha-del-hotfix>
   git push origin develop
   ```

## Cómo trabajar en el día a día

```bash
# 1. Traer lo último de develop
git checkout develop
git pull

# 2. Crear la rama de la tarea
git checkout -b feat/issue-12-login-page

# 3. Verificar antes de commitear (en back/front: npm run verify;
#    en infra/docs no hay script de verificación local)

# 4. Commitear (husky + commitlint validan el mensaje)
git add -A
git commit -m "feat(auth): endpoint de registro con hash argon2"

# 5. Publicar la rama y abrir el PR hacia develop
git push -u origin feat/issue-12-login-page
gh pr create --base develop --title "feat(auth): register endpoint" --body "Closes #12"
```

## Política de merges

- **Solo squash-merge**, en `develop` y en `main`, para mantener historia lineal.
- Commits locales en la rama de trabajo pueden ser múltiples; el squash
  los colapsa en uno al mergear.
- Títulos de PR siguen Conventional Commits y los valida el check
  `pr-title` de CI (ver [commits.md](./commits.md)).

## Versionado

El título del commit de squash determina el bump automático de versión
(ver [versioning.md](./versioning.md)):

| Prefijo del título del PR | Bump  | Ejemplo           |
| ------------------------- | ----- | ----------------- |
| `fix:` / `refactor:` / …  | patch | `v0.1.0` → `v0.1.1` |
| `feat:`                   | minor | `v0.1.0` → `v0.2.0` |
| `!` (breaking)            | major | `v0.1.0` → `v1.0.0` |

## Pull requests

Usa la plantilla en [`.github/PULL_REQUEST_TEMPLATE.md`](../.github/PULL_REQUEST_TEMPLATE.md)
y el paso a paso de [COMO-HACER-UN-PR.md](../operations/COMO-HACER-UN-PR.md). Cada PR
debe tener su checklist marcado antes de pedir review: `npm run verify` pasa,
tests añadidos, envelope respetado, etc.

Para enlazar el PR con su issue, escribe `Closes #<n>` en el **cuerpo del PR**.
`Refs #<n>` solo deja una mención y **no** cierra el issue al mergear.

## Los checks de CI que bloquean el merge

Cada repositorio corre sus propios checks. Si uno falla, GitHub no habilita el
botón de merge.

**Frontend** (`dolynation-tonatiuh-front`)

| Check | Qué valida |
| --- | --- |
| `lint` | ESLint + el test del regex de `pr-labels` |
| `typecheck` | `next typegen && tsc --noEmit` |
| `build` | que Next compile |
| `pr-title` | formato del título del PR |
| `pr-target` | rama base y rama origen |

**Backend** (`dolynation-atl-back`)

| Check | Qué valida |
| --- | --- |
| `unit-and-static` | tipos, lint, formato y tests unitarios |
| `e2e` | tests end-to-end (contra PostgreSQL) |
| `build` | que el backend compile |
| `openapi-guard` | que no se rompa el contrato de la API |
| `pr-title` | formato del título del PR |
| `pr-target` | rama base y rama origen |

**Infraestructura** (`dolynation-tlalli-infra`)

| Check | Qué valida |
| --- | --- |
| `compose-validate` | que los `docker-compose*.yml` sean válidos |
| `pr-title` | formato del título del PR |
| `pr-target` | rama base y rama origen |

**Documentación** (`dolynation-ehecatl-docs`)

| Check | Qué valida |
| --- | --- |
| `link-check` | que no haya links rotos en la documentación |
| `pr-title` | formato del título del PR |
| `pr-target` | rama base y rama origen |

`pr-title` y `pr-target` vienen del workflow `pr-title.yml` (dos jobs) y están
en los cuatro repos.
