# Changelog

Todas las novedades relevantes de este repositorio se registran aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el
versionado es [SemVer](https://semver.org/lang/es/).

La **versión se declara en `version.txt`**: el bot de release-please la sube
junto con la sección del changelog, y publica el tag al mergear su PR de
release.

## [0.1.3](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/compare/v0.1.2...v0.1.3) (2026-11-07)


### Bug Fixes

* **ci:** enviar el nombre del repositorio en el aviso al manifiesto ([#40](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/40)) ([aa5e759](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/commit/aa5e7598e5f825aeb81fdc2cd9c8a90444c6e64a))

## [0.1.2](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/compare/v0.1.1...v0.1.2) (2026-11-06)


### Bug Fixes

* **ci:** separar el checkout del paso que anota el tag ([#38](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/38)) ([071b25f](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/commit/071b25fbb4cf0ea543b227a837f27030d25e1a74))
* **docs:** corregir las reglas de proteccion declaradas en la documentacion ([#37](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/37)) ([7e040e8](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/commit/7e040e86f73880d344cbb72034387bb44102961a))

## [0.1.1](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/compare/v0.1.0...v0.1.1) (2026-11-06)


### Bug Fixes

* **ci:** eximir a Dependabot de la validacion de rama y titulo ([#26](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/26)) ([e66140b](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/commit/e66140ba9f8b2a37deb47d7bf2f1010fe36e05aa))
* **ci:** eximir el PR de release-please por nombre de rama ([9578935](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/commit/95789352e03efd00b3faf031d604c871c5cbf3fc)), closes [#4](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/4)
* **diagramas:** quitar el punto y coma que rompia el render de Mermaid en GitHub ([#20](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/20)) ([00d0f01](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/commit/00d0f01a5f78af1a1aa44b55c7f90d0415c73de2))
* **release:** activar el auto-merge aunque el PR de release ya exista ([24ce465](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/commit/24ce4652cc1a7636c3e2ab3fd89a12ae33e711e2)), closes [#4](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/4)
* **release:** localizar el PR de release por etiqueta para el auto-merge ([ba6ec82](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/commit/ba6ec823b78bb7cfabcc86f7e11ae4c69ea62eb0)), closes [#4](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/4)

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
