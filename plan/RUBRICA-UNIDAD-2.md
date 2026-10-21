# Conformidad con la rúbrica de la Unidad 2

> **Actividad evaluada:** *Avences del proyecto* · **Unidad 2:** control de
> versiones, diagramas y diccionario de datos.
>
> Este documento es el índice de evidencias: para cada criterio de la rúbrica
> señala **dónde está el material que lo respalda**. Sirve para repasar la
> entrega en dos minutos y para que quien revise no tenga que buscarla.

| Asignatura | DESARROLLO WEB INTEGRAL |
| --- | --- |
| Programa | Ingeniería en Desarrollo y Gestión de Software |
| Grado y sección | 9 · A |
| Profesor | Jesús Del Toro Robledo |
| Entrega | `v1.0.0` el 10 de diciembre de 2026 |
| Repositorio principal | [`dolynation-ehecatl-docs`](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs) |

---

## Criterios específicos

### 1. Maquetado — ✅ Excelente

Maquetado completo, estructurado y fiel a los requerimientos: **las nueve
pantallas** del prototipo están versionadas en el repositorio, en el orden del
recorrido del usuario, y cada una mapeada a los requerimientos que cubre.

| Evidencia | Dónde |
| --- | --- |
| Las 9 pantallas | [`anteproyecto/assets/wireframes/pantallas/`](../anteproyecto/assets/wireframes/pantallas/README.md) |
| La galería con figuras y RF | [§17 Wireframes](../anteproyecto/anteproyecto-dolynation.md#17.-wireframes.) |
| Vista previa del archivo de Figma | [`anteproyecto/assets/wireframes/`](../anteproyecto/assets/wireframes/README.md) |
| Origen en Figma | <https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation> |
| Guía de mantenimiento | [`operations/PROTOTIPO-FIGMA.md`](../operations/PROTOTIPO-FIGMA.md) |

### 2. Prototipado — ✅ Excelente

Prototipo estructurado que define el flujo de navegación, la distribución de
pantallas y la experiencia: el recorrido completo está en las 9 pantallas, en el
diagrama de actores y casos de uso, y en los dos diagramas de secuencia
(flujo de aprendizaje y autenticación).

| Evidencia | Dónde |
| --- | --- |
| Flujo de pantallas | [§17 Wireframes](../anteproyecto/anteproyecto-dolynation.md#17.-wireframes.) |
| Casos de uso y actores | [`diagrams/diagrama-de-actores.md`](../diagrams/diagrama-de-actores.md) |
| Secuencia del flujo de aprendizaje | [`diagrams/diagrama-de-secuencia.md`](../diagrams/diagrama-de-secuencia.md) |
| Secuencia de autenticación | [`diagrams/diagrama-de-secuencia-de-securidad.md`](../diagrams/diagrama-de-secuencia-de-securidad.md) |

### 3. Documentación en el repositorio (README / Unidades 1 y 2) — ✅ Excelente

El documento de la **Unidad 1** (anteproyyecto) y la documentación de la
**Unidad 2** están integrados y estructurados en el **README** del repositorio
remoto, con tablas que apuntan a cada documento.

| Evidencia | Dónde |
| --- | --- |
| README con Unidad 1 y Unidad 2 | [`README.md`](../README.md) |
| Unidad 1: anteproyecto | [`anteproyecto/anteproyecto-dolynation.md`](../anteproyecto/anteproyecto-dolynation.md) |
| Unidad 2: flujo, versionado, justification, diagramas, diccionario | [`operations/`](../operations/README.md) · [`diagrams/`](../diagrams/README.md) |
| Índice completo | [`README.md`](../README.md) |

### 4. Justificación de la herramienta y la plataforma de versionamiento — ✅ Excelente

Justificación sólida y técnica de la elección de **Git** y **GitHub** a partir de
las necesidades del proyecto, con los criterios de evaluación, el inventario
real de lo que se usa, las alternativas descartadas con su motivo y los límites
reales de la decisión.

| Evidencia | Dónde |
| --- | --- |
| Justificación completa | [`operations/JUSTIFICACION-GITHUB.md`](../operations/JUSTIFICACION-GITHUB.md) |
| Decisión registrada (ADR-009) | [`decisions/README.md`](../decisions/README.md) |
| Referencia en el anteproyecto | [§11.1 Metodología](../anteproyecto/anteproyecto-dolynation.md#11.1.-metodología-de-trabajo) |

### 5. Definición y diseño del flujo de trabajo (workflow) — ✅ Excelente

Flujo de trabajo detallado con nomenclatura de ramas, políticas de combinación,
gestión de pull requests, reglas de protección, CODEOWNERS, dependencias entre
issues y releases.

| Evidencia | Dónde |
| --- | --- |
| Flujo completo | [`operations/FLUJO-DE-TRABAJO.md`](../operations/FLUJO-DE-TRABAJO.md) |
| Paso a paso de un PR | [`operations/COMO-HACER-UN-PR.md`](../operations/COMO-HACER-UN-PR.md) |
| Reglas de ramas y commits | [`conventions/git-workflow.md`](../conventions/git-workflow.md) · [`conventions/commits.md`](../conventions/commits.md) |
| Qué reglas bloquean de verdad | [FLUJO-DE-TRABAJO.md, §"Qué reglas te bloquean"](../operations/FLUJO-DE-TRABAJO.md#qué-reglas-te-bloquean-y-cuáles-no) |

### 6. Configuración y parámetros del entorno de versiones — ✅ Excelente

Configuración inicial, control de accesos, archivos de exclusión y credenciales
de seguridad, verificados en los cuatro repositorios.

| Evidencia | Dónde |
| --- | --- |
| Archivos de exclusión | `.gitignore` en los 4 repositorios |
| Control de accesos | 12 *rulesets* (3 por repositorio): `develop`, `main`, `rc-*` |
| Revisión obligatoria | `require_code_owner_reviews: true`, 1 aprobación en `develop` y 2 en `main`, **sin bypass** |
| Quién revisa cada ruta | `.github/CODEOWNERS` (mínimo 2 owners por ruta) |
| Credenciales y reporte | `SECURITY.md` en los 4 repositorios + secret scanning y push protection activos |
| Permisos mínimos | `permissions:` declarados en todos los workflows |
| Variables de entorno | [`conventions/environment.md`](../conventions/environment.md) · `.env.example` |
| Secretos de despliegue | GitHub Environments (`desarrollo`, `staging`, `produccion`) |

### 7. Repositorio en funcionamiento y evidencias — ✅ Excelente

Enlace funcional a repositorios remotos activos que muestran el flujo real,
commits estructurados y participación colaborativa del equipo.

| Evidencia | Dónde |
| --- | --- |
| Repositorios activos | [Los 4 repos de la organización](https://github.com/DolyLanguagesORG) |
| Releases publicadas | `v0.1.0` (docs, backend, infra) y `v0.1.1` (frontend) |
| Commits estructurados | [Conventional Commits](https://www.conventionalcommits.org/es/) en todos los repos |
| Colaboración del equipo | PRs de los 4 desarrolladores + `CODEOWNERS` con 2 owners por ruta |
| Planificación viva | [Project de la organización](https://github.com/orgs/DolyLanguagesORG/projects/1) con 66 issues |
| Continuidad del trabajo | [Cronograma de 5 sprints](../plan/cronograma.md) y [plan de seguimiento](../plan/PLAN-Y-SEGUIMIENTO.md) |

### 8. Diagramas del sistema (Arquitectura / Casos de uso / DER) — ✅ Excelente

Cinco diagramas claros, normalizados y alineados a los requerimientos, que
reflejan la estructura y el comportamiento del sistema. Están en **Mermaid**,
así que **se renderizan de forma nativa en GitHub**.

| Diagrama | Tipo | Qué representa |
| --- | --- | --- |
| [Arquitectura](../diagrams/diagrama-de-arquitectura.md) | `flowchart` | Los 4 repositorios, los módulos del backend, el frontend, la base de datos y los servicios externos |
| [Actores y casos de uso](../diagrams/diagrama-de-actores.md) | `flowchart` | Actores humanos, casos de uso del estudiante y servicios externos |
| [Entidad-relación](../diagrams/diagrama-de-ER%28Entidad-Relacion%29.md) | `erDiagram` | Las 9 tablas, sus claves y sus relaciones |
| [Secuencia: flujo principal](../diagrams/diagrama-de-secuencia.md) | `sequenceDiagram` | Generación, diccionario con TTS y evaluación PNL |
| [Secuencia: autenticación](../diagrams/diagrama-de-secuencia-de-securidad.md) | `sequenceDiagram` | Login, JWT y rotación del refresh token |

Los cinco están **validados con el motor de Mermaid** (10.9.8 y 11.17.2) leyendo
el bloque tal como GitHub lo recibe.

### 9. Diccionario de datos — ✅ Excelente

Estructura de datos documentada a detalle: nombre de tabla, campos, tipos,
restricciones, llaves primarias y foráneas y descripciones claras. Las nueve
tablas coinciden **campo por campo** con el diagrama entidad-relación.

| Evidencia | Dónde |
| --- | --- |
| Diccionario completo | [`diagrams/diccionario-de-datos.md`](../diagrams/diccionario-de-datos.md) |
| Modelo y estado real/planificado | [`architecture/data-model.md`](../architecture/data-model.md) |
| Fuente de verdad (SQL) | [`database/postgres/`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/tree/develop/database/postgres) |

---

## Criterios generales

| Criterio | Estado | Evidencia |
| --- | --- | --- |
| **Cumplimiento de la actividad** | ✅ | Los cuatro repositorios montados, documentados y con el flujo de trabajo funcionando |
| **Calidad del trabajo** | ✅ | Verificación automatizada: `link-check`, `openapi-guard`, `schema-sql`, CI por repo y diagramas validados |
| **Creatividad y originalidad** | ✅ | Caché por `prompt_hash`, evaluación por PNL con cobertura/precisión/coherencia, tokens de diseño, registro de ADR, `versions.yml` |
| **Presentación y orden** | ✅ | Documentación reorganizada en 8 carpetas con índice navegable y tablas por criterio |
| **Ortografía y redacción** | ✅ | Documentación en español, revisada y con índice y tablas regenerados |
| **Entrega y responsabilidad** | ✅ | `v1.0.0` el 10 de diciembre, con la versión verificada entre código, changelog, tag y `/health` |

---

## Lo que falta (del lado del equipo)

| Pendiente | Quién | Cómo |
| --- | --- | --- |
| Campo **«Nombre del estudiante»** de la rúbrica vacío | El equipo | Se llena en el Excel del profesor |
| Exportar las pantallas de Figma | El equipo | **Hecho**: las 9 pantallas ya están versionadas |
| Installar la app «Figma for GitHub» | Quien tenga la cuenta de Figma | [`operations/PROTOTIPO-FIGMA.md` §6](../operations/PROTOTIPO-FIGMA.md) |

## Dónde está el material, en un vistazo

| Necesito… | Voy a… |
| --- | --- |
| El anteproyecto (Unidad 1) | [`anteproyecto/anteproyecto-dolynation.md`](../anteproyecto/anteproyecto-dolynation.md) |
| El flujo de trabajo y el versionado | [`operations/FLUJO-DE-TRABAJO.md`](../operations/FLUJO-DE-TRABAJO.md) |
| Por qué GitHub | [`operations/JUSTIFICACION-GITHUB.md`](../operations/JUSTIFICACION-GITHUB.md) |
| Los diagramas | [`diagrams/`](../diagrams/README.md) |
| El modelo de datos | [`diagrams/diccionario-de-datos.md`](../diagrams/diccionario-de-datos.md) |
| El maquetado | [`anteproyecto/assets/wireframes/pantallas/`](../anteproyecto/assets/wireframes/pantallas/README.md) |
| El plan y el cronograma | [`plan/`](../plan/README.md) |
