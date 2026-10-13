# Tablero y releases

## Tablero (Kanban / Timeline)

La planificación vive en el
[Project de la organización](https://github.com/orgs/DolyLanguagesORG/projects/1):
33 tareas, 5 sprints, del 05/Oct/2026 al 10/Dic/2026.

- **Issues**: un issue por entregable, repartido entre los cuatro repos (se
  referencian como `back#2`, `front#2`, `infra#2`, `docs#3`, etc.).
- **Milestones**: uno por sprint, replicado en cada repo.
- **Standup diario**: cada dev publica su avance al cierre de jornada
  (límite 23:59 CST).
- **Dependencias**: se registran con *blocked by* (p. ej. `infra#4` bloqueado por
  `back#18`).

Cronograma completo en [`cronograma.md`](../../../../cronograma.md).

## Versionado (release-please)

SemVer (`vX.Y.Z`) automático a partir de los Conventional Commits:

- `release-please` mantiene **un PR de release acumulativo** contra `develop`
  (`chore(release): release vX.Y.Z`).
- Al mergear ese PR → actualiza versión, crea el **tag anotado** y publica la
  GitHub Release; luego reabre un PR limpio.
- Nadie edita versiones a mano.

| Título del PR | Bump |
| --- | --- |
| `fix(...)`, `refactor(...)`, `chore(...)`, `docs(...)` | patch |
| `feat(...)` | minor |
| `feat(...)!` o `BREAKING CHANGE:` | major |

> El pipeline completo (fases, `rc-*`, staging, `versions.yml` en `infra`,
> cascada con PAT) está en
> [`CI-CD-Y-VERSIONADO.md`](../../../../CI-CD-Y-VERSIONADO.md). Parte todavía es
> **objetivo pendiente**, no implementado.

Fuentes: [`conventions/versioning.md`](../../../../conventions/versioning.md),
[`FLUJO-DE-TRABAJO.md`](../../../../FLUJO-DE-TRABAJO.md).
