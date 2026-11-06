# Changelog

Todas las novedades relevantes de este repositorio se registran aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el
versionado es [SemVer](https://semver.org/lang/es/).

La **versión se declara en `version.txt`**: el bot de release-please la sube
junto con la sección del changelog, y publica el tag al mergear su PR de
release.

## [No publicado]

### Añadido
- Versionado **automático en `develop`**: cada repositorio corre release-please
  con un PR de release acumulativo que sube la versión y el changelog, y al
  mergearse publica el tag y la GitHub Release. El PR lleva auto-merge.
- `version.txt`: archivo de versión de los repositorios sin `package.json`
  (infra y documentación).
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
- El versionado se calcula con **todos** los commits del ciclo, no solo con el
  último: una funcionalidad ya no puede publicarse como `patch` porque el
  último PR fusionado fuera un `chore`.
- La versión se declara en `version.txt` (en vez de la sección del `CHANGELOG.md`)
  en los repositorios sin `package.json`.
- Los milestones de los cuatro repos quedan alineados con el cierre de cada
  sprint del cronograma: 18-oct, 01-nov, 15-nov, 29-nov y 10-dic.

## [0.1.0] - 2026-10-12

### Añadido
- Extracción del repositorio de documentación del monorepo original.

[No publicado]: https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/releases/tag/v0.1.0
