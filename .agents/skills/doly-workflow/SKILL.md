---
name: doly-workflow
description: Flujo de trabajo global de DolyNation (organización multirepo). Repos, ramas (develop/main/rc-*), Conventional Commits, PR y checks de CI, tablero Kanban y releases. Úsala cuando la pregunta sea sobre el proceso de la organización y no sobre un repositorio concreto.
---

# Flujo de trabajo — DolyNation

Cómo se trabaja en la organización. Todo lo global está aquí; lo específico de
cada repo vive en su propio repo (skills `nestjs-backend`, `nextjs-frontend`).

## Repositorios

| Repo | Contenido |
| --- | --- |
| `dolynation-atl-back` | API REST (NestJS 11 + Drizzle + PostgreSQL) |
| `dolynation-tonatiuh-front` | Frontend web (Next.js 16) |
| `dolynation-tlalli-infra` | Docker Compose + schema SQL (**dueño de la BD**) |
| `dolynation-ehecatl-docs` | Este repo: documentación |
| `doly-languages` | Monorepo original, **archivado / histórico** |

Detalle en `references/repos-and-branches.md`.

## Ramas

- `develop` es la rama **por defecto** y de integración diaria.
- `main` es producción / release; solo recibe merges desde `develop` (y hotfixes).
- `rc-*` son efímeras (release candidates); `staging` vive en `infra`.
- **Prohibido el push directo** a `develop`/`main`: siempre por PR.
- Solo **squash-merge**, para historia lineal.

## Commits

Conventional Commits, subject en **español**, ≤72 chars, un concern por commit.
Scopes habituales: `auth`, `readings`, `ia`, `users`, `errors`, `docs`, `deps`,
`db`, `prod`, `infra`, `cleanup`, `repo`, `ui`.

## Pull requests

- Título conventional (lo valida el check `pr-title`).
- Base `develop`; **squash**; 1 aprobación de cualquier persona con acceso.
- `Closes #N` en el cuerpo (en su propia línea) para cerrar el issue al mergear.
- Debe pasar **los checks del repo** (ver `references/commits-and-prs.md`).

## Tablero y releases

Kanban y Timeline viven en el
[Project de la organización](https://github.com/orgs/DolyLanguagesORG/projects/1).
Los releases usan SemVer automático con **release-please** (PR acumulativo en
`develop`; el tag nace al mergear el PR de release). Ver
`references/kanban-and-releases.md`.

## Documentos fuente

- [FLUJO-DE-TRABAJO.md](../../../operations/FLUJO-DE-TRABAJO.md)
- [COMO-HACER-UN-PR.md](../../../operations/COMO-HACER-UN-PR.md)
- [CI-CD-Y-VERSIONADO.md](../../../operations/CI-CD-Y-VERSIONADO.md)
- [conventions/](../../../conventions/)

## Referencias

- `references/repos-and-branches.md` — repos, ramas y reglas por rama.
- `references/commits-and-prs.md` — commits, PR y checks de CI por repo.
- `references/kanban-and-releases.md` — tablero, milestones y versionado.
