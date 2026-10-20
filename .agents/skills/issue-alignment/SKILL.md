---
name: issue-alignment
description: Cómo auditar y alinear los issues de DolyNation con el anteproyecto, el cronograma y el Project de la organización. Cubre entregables, criterios de aceptación, dependencias blocked_by, sub-issues, milestones, compuerta de sprint y limpieza del Project. Úsala al revisar o crear tareas de cualquier repo.
---

# Alineación de issues — DolyNation

## Objetivo

Que cada issue diga **qué problema resuelve**, **qué entrega**, **cómo se
acepta** y **de qué depende**, y que el Project refleje el plan real.

## Fuentes

- [cronograma.md](../../../plan/cronograma.md) — 33 entregables + 5 de
  plataforma + 3 migraciones.
- [PLAN-Y-SEGUIMIENTO.md](../../../plan/PLAN-Y-SEGUIMIENTO.md) — ruta crítica y
  compuerta de sprint.
- [Anteproyecto](../../../anteproyecto/anteproyecto-dolynation.md) — RF/RNF.
- [decisions/](../../../decisions/README.md) — contratos, proveedor, roles,
  puntos y migraciones.
- [data-model.md](../../../architecture/data-model.md) — schema actual y
  planificado.

## Checklist por issue

Cada issue canónico debe tener:

- [ ] Metadata: `Cronograma: tarea X/33 · Sprint N · Issue repo#N`.
- [ ] Responsable, inicio y entrega.
- [ ] Área y RF/RNF.
- [ ] `## Problema / objetivo`.
- [ ] `## Alcance` y `## Fuera de alcance`.
- [ ] `## Entregables` concretos (endpoint, DTO, tabla, test, OpenAPI, docs).
- [ ] `## Criterios de aceptación` verificables (3-7).
- [ ] `## Dependencias` (`Bloqueada por` / `Bloquea`).
- [ ] Evidencia esperada.
- [ ] Definition of Done de proceso.
- [ ] Marcador `<!-- doly:... -->` si el issue lo tenía.

## Comandos de auditoría

```bash
# Listar issues con cuerpo y labels
gh issue list --repo DolyLanguagesORG/<repo> --state all --limit 100 \
  --json number,title,state,labels,milestone,assignees,body

# Revisar un issue
gh issue view <n> --repo DolyLanguagesORG/<repo> --json body

# Dependencias
gh api repos/DolyLanguagesORG/<repo>/issues/<n>/dependencies/blocked_by --jq '[.[].number]'

# Sub-issues (GraphQL)
gh api graphql -f query='query { repository(owner:"DolyLanguagesORG", name:"<repo>") { issue(number:<n>) { subIssues(first:20) { nodes { number } } parent { number } } } }'

# Project
gh project item-list 1 --owner DolyLanguagesORG --limit 100 --format json
```

## Reglas de alineación

1. **No duplicar tareas.** Los sub-issues no suman al conteo 33+5+3. Si un
   extra se solapa, se fusiona o se cierra como duplicado.
2. **Contratos canónicos.** `POST /readings`,
   `POST /readings/{id}/evaluate`, `POST /readings/{id}/explanations` y TTS bajo
   readings. No `/content`, `/evaluation` ni `/vocabulary` paralelos.
3. **Schema primero.** `back#8/#9/#10` dependen de `infra#20`;
   `back#11/#13/#16` de `infra#21`; `back#17` de `infra#22`.
4. **Compuerta de sprint.** Un issue no se mergea si su sprint no está activo o
   si tiene un `blocked_by` abierto. Los PRs futuros quedan en **Draft**.
5. **Fechas intactas.** No mover fechas de issues sin pedirlo; los milestones
   deben cerrar al final del sprint.
6. **Project manual.** Cerrar un issue no mueve la tarjeta; el `Status` se
   actualiza a mano.

## Plantilla de issue

```md
**Cronograma: tarea X/33 · Sprint N · Issue back#N** · Responsable: **...**

**Inicio:** YYYY-MM-DD · **Entrega:** YYYY-MM-DD 23:59 CST

**Área:** backend · **RFs:** RF-XX · **RNFs:** RNF-XX

## Problema / objetivo
...

## Alcance
- ...

## Fuera de alcance
- ...

## Entregables
- [ ] ...

## Criterios de aceptación
- [ ] ...

## Dependencias
- Bloqueada por: ...
- Bloquea: ...

## Evidencia esperada
...

## Definition of Done (proceso)
- [ ] Rama/PR/commits/checks/standup.

<!-- doly:start=... due=... sprint=... assignees=... area=... -->
```

## Errores comunes

- Copiar el mismo DoD genérico sin entregables propios.
- Referencias a números de tarea del cronograma que parecen números de issue.
- Enlaces al monorepo archivado `doly-languages`.
- No registrar `blocked_by` o registrar la dirección al revés.
- Dejar issues de sprints futuros con PRs listos para merge.
- Añadir tablas en Drizzle sin el update correspondiente en infra.

## Verificación final

- Todos los canónicos tienen problema, entregables, criterios y dependencias.
- No hay PRs abiertos de sprints futuros fuera de Draft.
- El Project no tiene PRs como si fueran tareas.
- Los enlaces y términos coinciden con
  [decisions/](../../../decisions/README.md) y
  [data-model.md](../../../architecture/data-model.md).
