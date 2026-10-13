# Commits y PRs

## Commits (Conventional Commits)

```
<type>(<scope>): <subject imperativo, español, ≤72 chars>

<body opcional, wrap a 72>

<footer opcional>
```

Tipos: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `build`, `ci`,
`perf`, `style`. Breaking change: `!` tras el tipo o `BREAKING CHANGE:` en el
body.

Scopes: `auth`, `readings`, `ia`, `users`, `errors`, `docs`, `deps`, `db`,
`prod`, `infra`, `cleanup`, `repo`, `ui`.

> La validación del mensaje es **local** (`commitlint` vía husky, por repo). El
> CI **no** revisa mensajes de commit: solo valida el **título del PR**
> (`pr-title`). El idioma del subject es **español** (el contrato de la API sí
> va en inglés).

Regla de oro: **commits pequeños**, un concern por commit.

## Pull requests

1. Rama desde `develop`.
2. `npm run verify` en back/front (en `infra`/`docs` no hay script; el CI de docs
   corre `link-check`).
3. Commit(s) conventional.
4. Push y PR hacia `develop` con la plantilla
   [`.github/PULL_REQUEST_TEMPLATE.md`](../../../../.github/PULL_REQUEST_TEMPLATE.md).
5. Título conventional (check `pr-title`), `Closes #N` en el cuerpo.
6. **Squash-merge** con 1 aprobación y los checks en verde.

## Checks de CI por repo

**Frontend** (`dolynation-tonatiuh-front`): `lint`, `typecheck`, `build`,
`pr-title`, `pr-target`.

**Backend** (`dolynation-atl-back`): `unit-and-static`, `e2e`, `build`,
`openapi-guard`, `pr-title`, `pr-target`.

**Infra** (`dolynation-tlalli-infra`): `compose-validate`, `pr-title`,
`pr-target`.

**Docs** (`dolynation-ehecatl-docs`): `link-check`, `pr-title`, `pr-target`.

`pr-title` y `pr-target` vienen de `pr-title.yml` (dos jobs) y están en los
cuatro repos. `pr-target` valida que el PR salga de una rama
`tipo/issue-<n>-...` (o del formato `<n>-<detalle>` del botón) y apunte a
`develop` (o `main` en releases/hotfixes).

Fuentes: [`conventions/commits.md`](../../../../conventions/commits.md),
[`COMO-HACER-UN-PR.md`](../../../../COMO-HACER-UN-PR.md).
