# Changelog

Todas las novedades relevantes de este repositorio se registran aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el
versionado es [SemVer](https://semver.org/lang/es/).

La **versión se declara en el `CHANGELOG.md`**: el workflow `release.yml` exige
que exista la sección de la versión que se va a publicar antes de crear el tag.

## [No publicado]

### Añadido
- Reorganización de la documentación en `anteproyecto/`, `plan/`, `operations/`,
  `architecture/`, `conventions/`, `onboarding/` y `decisions/`.
- Diagramas migrados a **Mermaid**, que GitHub renderiza de forma nativa.
- `operations/JUSTIFICACION-GITHUB.md`: por qué GitHub es la plataforma principal
  de trabajo, con los criterios, las alternativas descartadas y sus límites.
- `operations/PROTOTIPO-FIGMA.md`: guía de integración del prototipo de Figma
  (imagen versionada, embed en la app, tokens de diseño y app para GitHub).
- `operations/PLAN-DE-DESPLIEGUE.md`: los 3 entornos, puertos, secretos y flujo
  de despliegue.
- Registro de decisiones (ADR) con contexto, alternativas y consecuencias, más
  la lista de decisiones pendientes de toma.
- Anteproyecto saneado: Argon2id, Drizzle, los 4 idiomas, la tabla de riesgos
  corregida, el índice navegable y el cronograma 19-oct → 10-dic.

### Cambiado
- Los milestones pasan a las fechas reales de entrega (31-oct, 14-nov, 28-nov,
  5-dic y 10-dic).

## [0.1.0] - 2026-10-12

### Añadido
- Extracción del repositorio de documentación del monorepo original.

[No publicado]: https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/releases/tag/v0.1.0
