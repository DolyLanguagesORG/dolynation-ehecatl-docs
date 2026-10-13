# Repos y ramas

## Repositorios de la organización

| Repo | Contenido | Rama por defecto |
| --- | --- | --- |
| `dolynation-atl-back` | API (NestJS 11 + Drizzle + PostgreSQL) | `develop` |
| `dolynation-tonatiuh-front` | Frontend (Next.js 16) | `develop` |
| `dolynation-tlalli-infra` | Docker Compose + schema SQL (dueño de la BD) | `develop` |
| `dolynation-ehecatl-docs` | Documentación | `develop` |
| `doly-languages` | Monorepo original, archivado | — |

El monorepo `doly-languages` **no se usa**: quedó archivado como histórico. Todo
el trabajo nuevo ocurre en los cuatro repos de arriba.

## Ramas

| Rama | Rol |
| --- | --- |
| `tipo/issue-<n>-<módulo>-<detalle>` | Trabajo de una tarea (`feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `build`, `ci`, `style`) |
| `develop` | Integración diaria (default) |
| `rc-*` | Release candidate (efímera) |
| `main` | Producción / release |
| `hotfix/*` | Fix urgente desde `main`, vuelve a `develop` por cherry-pick |

El `<n>` es el número del issue en su repo y es obligatorio. También se acepta
el formato del botón *Create a branch* de GitHub (`<n>-<detalle>`). La forma con
prefijo es la recomendada. Máx. 50 caracteres.

## Reglas por rama

**`develop`**

- Recibe PRs de `tipo/issue-*` o del formato `<n>-<detalle>` del botón de GitHub.
- Requiere los checks del repo en verde y 1 aprobación.
- Prohibido el push directo; solo squash-merge.
- No exige estar al día con la base.

**`main`**

- Recibe PRs **únicamente** desde `develop` (excepto hotfixes).
- Mismos checks + 1 aprobación; solo squash-merge.
- Permanece estable entre releases.

## Hotfix

1. Rama desde `main`: `git checkout -b hotfix/<nombre>`.
2. Fix mínimo + PR `fix(scope): ...` contra `main`.
3. Tras mergear, cherry-pick a `develop`.

Fuente: [`conventions/git-workflow.md`](../../../../conventions/git-workflow.md).
