# Tablero y releases

## Tablero (Kanban / Timeline)

La planificación vive en el
[Project de la organización](https://github.com/orgs/DolyLanguagesORG/projects/1):
33 tareas, 5 sprints, del 05/Oct/2026 al 10/Dic/2026.

- **Issues:** un issue por entregable, repartido entre los cuatro repos (se
  referencian como `back#2`, `front#2`, `infra#2`, `docs#3`, etc.).
- **Milestones:** uno por sprint, replicado en cada repo.
- **Standup diario:** cada dev publica su avance al cierre de jornada
  (límite 23:59 CST).
- **Dependencias:** se registran como *blocked by* (p. ej. `infra#4` bloqueado
  por `back#18`).

Cronograma completo en [`cronograma.md`](../../../../plan/cronograma.md).

## Versionado (release-please)

SemVer (`vX.Y.Z`) automático a partir de los Conventional Commits.

- `release-please` mantiene **un PR de release acumulativo** contra `develop`
  (`chore(release): vX.Y.Z`).
- Ese PR sube la versión, escribe el `CHANGELOG.md` y actualiza el manifiesto.
- Al mergearlo → **tag anotado** + **GitHub Release** (marcada *Pre-release*
  mientras la versión sea `0.x`); luego se abre un PR limpio.

**El tag nace en `develop`, no en `main`.** release-please acopla el PR de
release con el tag: sin release, el PR queda con la etiqueta
`autorelease: pending` y el bot aborta en el siguiente ciclo. `main` es la
**promoción**, no el generador.

| Título del PR | Bump |
| --- | --- |
| `feat(...)` | minor |
| `feat(...)!` o `BREAKING CHANGE:` | major |
| `fix(...)` | patch |
| `refactor` `chore` `docs` `ci` `test` `perf` `style` | **no genera versión** |

El **número no cuenta PRs**: comunica riesgo de compatibilidad. El detalle de
cada PR queda en el changelog y en el commit al que apunta el tag.

### El manifiesto del proyecto

`dolynation-tlalli-infra/versions.yml` dice, por repositorio, la versión, el
tag y el commit exacto, más la `app_version` de la aplicación. Se mantiene
solo: cada repo avisa a infra al publicar su tag y el workflow `sync-versions`
abre el PR que actualiza su fila.

### Promoción

```
develop ──► rc-<version> (en infra) ──► main
   |              |                        |
 tag+release    staging                 PRODUCCIÓN
 Pre-release                              (Environment: requiere aprobación)
```

> El pipeline completo (fases, `rc-*`, staging, `versions.yml`, cascada con
> PAT) está en
> [`CI-CD-Y-VERSIONADO.md`](../../../../operations/CI-CD-Y-VERSIONADO.md). Parte
> todavía es **objetivo pendiente**, no implementado.

Fuentes: [`conventions/versioning.md`](../../../../conventions/versioning.md),
[`FLUJO-DE-TRABAJO.md`](../../../../operations/FLUJO-DE-TRABAJO.md).
