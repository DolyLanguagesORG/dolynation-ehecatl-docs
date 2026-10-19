# AGENTS.md — `dolynation-ehecatl-docs`

Instrucciones para agentes de código (Claude Code, Codex, OpenCode, Cursor, etc.)
que trabajen en este repositorio.

## Qué es este repo

Centraliza la **documentación** de DolyNation: convenciones, arquitectura,
onboarding, cronograma, anteproyecto y el pipeline CI/CD. **No contiene código**
de backend, frontend ni infraestructura (viven en otros repos).

## Skills de este repo

Están en `.agents/skills/` y se cargan bajo demanda:

- **`doly-workflow`** — el flujo global de la organización: repos, ramas,
  commits, PR y checks, tablero Kanban y releases. Úsala cuando la pregunta sea
  del proceso y no de un repo concreto.
- **`anteproyecto`** — contexto y preguntas sobre el anteproyecto académico
  (problema, objetivos, requerimientos, metodología, roles, cronograma).
- **`docs-style`** — cómo escribir y mantener esta documentación (estructura,
  tono, links relativos, tablas).
- **`issue-alignment`** — cómo auditar issues, entregables, criterios,
  dependencias, sub-issues y Project; útil al crear o revisar tareas.

## Reglas rápidas

- Rama nueva desde `develop` (default). **Nunca** push directo a `develop`/`main`.
- El CI corre `link-check` (lychee, en modo offline) sobre los `.md`; antes de
  commitear, verifica a mano los enlaces relativos que hayas tocado.
- Commits en **Conventional Commits**, subject en **español**, un concern por commit.
- PR hacia `develop`, título conventional, **squash**, 1 aprobación.
- `Closes #N` en el cuerpo del PR (en su propia línea).
- Los enlaces internos son **relativos** y las anclas de sección se mantienen.

## Otros repos de la organización

- `dolynation-atl-back` — API (NestJS 11 + Drizzle + PostgreSQL)
- `dolynation-tonatiuh-front` — frontend (Next.js 16)
- `dolynation-tlalli-infra` — Docker Compose + schema SQL (dueño de la BD)
