# DolyNation — Documentación

DolyNation (Dolynglish) es una aplicación web de práctica de inglés que genera
ejercicios de lectura con IA y evalúa las respuestas del usuario. Este
repositorio centraliza la **documentación del proyecto**: convenciones,
arquitectura, onboarding, cronograma y el anteproyecto.

> El código vive en repos separados (ver abajo). Este repo no contiene el
> backend, el frontend ni la infraestructura.

## Repositorios de la organización

| Repo | Contenido |
| --- | --- |
| [`dolynation-tonatiuh-front`](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front) | Frontend web (Next.js 16) |
| [`dolynation-atl-back`](https://github.com/DolyLanguagesORG/dolynation-atl-back) | API REST (NestJS 11 + Drizzle + PostgreSQL) |
| [`dolynation-tlalli-infra`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra) | Docker Compose + schema SQL (dueño de la BD) |
| [`dolynation-ehecatl-docs`](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs) | Este repo: documentación |
| [`doly-languages`](https://github.com/DolyLanguagesORG/doly-languages) | Monorepo original (archivado, histórico) |

## Índice de la documentación

**Empieza por aquí:**

- **[Cómo hacer un Pull Request](./operations/COMO-HACER-UN-PR.md)** — flujo paso a paso:
  ramas, checks, `Closes #N`, troubleshooting. **Léelo si vas a abrir tu
  primer PR.**
- **[Flujo de trabajo](./operations/FLUJO-DE-TRABAJO.md)** — el panorama completo: ramas,
  tablero, CODEOWNERS, dependencias, releases, y qué reglas **sí** te bloquean
  y cuáles no.
- [Cronograma](./plan/cronograma.md) — plan de 5 sprints, 33 entregables y sus prerrequisitos, del
  05/Oct/2026 al 10/Dic/2026.
- [Plan y seguimiento](./plan/PLAN-Y-SEGUIMIENTO.md) — el orden de trabajo (qué
  depende de qué), cómo no perder fechas y cómo justificar atrasos.
- [Entrada rápida](./CONTRIBUTING.md) — clonar, instalar, contribuir.

**Detalle:**

- **Convenciones** (cómo escribir código, commits, PRs):
  [conventions/](./conventions/README.md)
- **Arquitectura**: [architecture/](./architecture/README.md)
- **Onboarding**: [onboarding/](./onboarding/README.md)
- **CI/CD y versionado**: [CI-CD-Y-VERSIONADO.md](./operations/CI-CD-Y-VERSIONADO.md)
- **Backlog** (mejoras sueltas): [backlog.md](./plan/backlog.md)
- **Diagramas** (UML): [diagrams/](./diagrams/README.md)
- **Decisiones**: [decisions/](./decisions/README.md)
- **Assets** (Word/PDF, capturas): [assets/](./assets/README.md)

## Documentación adicional

- [`dolynation-atl-back` README](https://github.com/DolyLanguagesORG/dolynation-atl-back) — quick start, scripts, arquitectura del backend.
- `TYPESCRIPT_STANDARDS.md` — reglas no negociables de TypeScript (en el repo del backend).
- [`dolynation-tlalli-infra` README](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra) — servicios dockerizados.

## Anteproyecto

[`anteproyecto-dolynation.md`](./anteproyecto/anteproyecto-dolynation.md) — documento
original con la planeación, roles y stack del proyecto.

## Estado del proyecto

- Backend: activo.
- Frontend web: en desarrollo.
- Mobile: pausado (fuera del alcance de `v1.0.0`).
- Release vigente: `v0.1.0`; la entrega de cierre está prevista para `v1.0.0`.
- La planificación vive en GitHub: [Project con Kanban y Timeline](https://github.com/orgs/DolyLanguagesORG/projects/1).

## Licencia

`UNLICENSED`. El repositorio es público, pero no se ha definido una licencia
abierta, así que todos los derechos quedan reservados.
