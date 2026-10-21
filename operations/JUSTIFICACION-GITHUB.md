# Por qué GitHub es la plataforma principal de trabajo

Este documento justify la decisión de usar **GitHub** como plataforma única de
trabajo del proyecto DolyNation: repositorios, issues, revisiones, CI/CD,
entornos, configuración y documentación. No es una preferencia: es una decisión
tomada con criterios, que se puede revisar y revertir.

> **Alcance.** Cubre la plataforma de trabajo (dónde vive el código, cómo se
> coordina el trabajo y cómo se despliega). **No** es la justificación del
> stack de producto (NestJS, Next.js, PostgreSQL, Docker), que está en el
> §14 del anteproyecto.

---

## 1. Contexto y criterios de elección

El equipo son cinco personas (cuatro en desarrollo y una de producto) con un
presupuesto de tiempo limitado: el proyecto va del **5 de octubre al 10 de
diciembre de 2026** y la versión entregable es la `v1.0.0`.

La decisión se tomó con cinco criterios, en este orden de peso:

| # | Criterio | Qué significa en la práctica |
| --- | --- | --- |
| C1 | **Automatización** | Que el CI/CD, los checks y los releases no dependan de que alguien se acuerde de ejecutarlos. |
| C2 | **Trazabilidad** | Que cada cambio esté ligado a un entregable, con responsable, fecha y evidencia. |
| C3 | **Revisión de código** | Que nada llegue a `develop` sin que alguien del equipo lo mire. |
| C4 | **Configuración como código** | Que las reglas del proyecto vivan en el repositorio, no en la memoria de nadie. |
| C5 | **Coste yCurve de aprendizaje** | Que no haya que aprender y pagar dos plataformas ni dos herramientas de gestión. |

---

## 2. Lo que GitHub ya resuelve en este proyecto

No se eligió GitHub «a ciegas»: se eligió porque **todo lo que el proyecto
necesita ya está resuelto dentro de la misma plataforma**. Este es el
inventario real, verificado en los cuatro repositorios.

### 2.1 Automatización (C1)

| Elemento | Estado real | Para qué sirve |
| --- | --- | --- |
| **24 workflows** de GitHub Actions | 5 (docs) · 7 (back) · 6 (infra) · 6 (front) | CI de cada repo, validaciones de PR y despliegue a desarrollo |
| `ci-backend.yml` | 3 jobs: `unit-and-static`, `e2e`, `build` | Corre los tests contra PostgreSQL real en cada PR |
| `openapi-guard.yml` | 4 guardas de OpenAPI | Impide que el contrato de la API se rompa sin que se note |
| `schema-sql` (en `ci-infra.yml`) | Aplica `01-init.sql` y `updates/*.sql` sobre Postgres limpio | Un SQL roto falla en el PR, no en el servidor |
| `deploy-dev.yml` | Autodespliegue al mergear a `develop` | El entorno de desarrollo se actualiza solo |
| `release.yml` | Tag anotado + GitHub Release al llegar a `main` | La `v1.0.0` sale de un merge, no de un comando manual |
| `dependabot.yml` (4 repos) | Actualizaciones semanales de npm y de las actions | Las dependencias no se quedan rancias |
| Secret scanning + push protection (4 repos) | Activos | Ningún secreto llega a la historia del repositorio |

**El resultado:** la validación del código es una condición de entrada, no una
disciplina. Un PR que rompe los tests, el contrato de la API o el schema de la
base de datos **no se puede fusionar**.

### 2.2 Trazabilidad (C2)

- **68 issues abiertos** repartidos en 4 repositorios, con el mismo conjunto de
  **24 labels** en todos (por sprint y por área) y **5 milestones** con las
  mismas fechas.
- **Sub-issues y dependencias nativas**: `back#19`–`#27` son sub-issues de
  `back#7`, `back#12` y `back#18`; `front#14`–`#16` son sub-issues de
  `front#11`. Las dependencias entre repos (`front#12` ← `back#17`,
  `docs#3` ← `infra#4`) se expresan con la API de dependencias, sin hojas de
  cálculo paralelas.
- **Un Project de organización** con 68 items y las vistas *Kanban*, *Timeline*
  y *Todos los entregables*: el tablero es la misma fuente de verdad que las
  issues, no una copia.
- **El issue es la unidad de trabajo**: cada uno tiene entregables, criterios
  de aceptación, evidencia esperada, responsable, sprint y fecha. Eso permite
  cerrar una tarea con una evidencia, no con una opinión.

### 2.3 Revisión de código (C3)

| Mecanismo | Qué aporta |
| --- | --- |
| **CODEOWNERS** en los 4 repos, con **≥2 owners por ruta** | GitHub pide la revisión de quien corresponde y avisa automáticamente |
| `require_code_owner_reviews: true` en los rulesets | **La revisión del owner es obligatoria**: sin ella, el merge se bloquea |
| `required_approving_review_count`: 1 en `develop`, 2 en `main` | Un par de ojos en el día a día, dos en el release |
| `required_review_thread_resolution` | No se fusiona con conversaciones sin resolver |
| `pr-title`, `pr-target`, `pr-labels` | Validan el título, la rama origen y las etiquetas **antes** de la revisión |
| Plantillas de PR y de issue (4 + 8) | El checklist y el formato son los mismos en todos los repos |
| `squash` + linear history + borrado de rama al fusionar | Historial legible y un commit por PR |

**No hay atajos:** los rulesets no declaran `bypass_actors`, así que nadie
—tampoco quien administra el repositorio— puede saltarse la revisión de un
code owner. El flujo es el mismo para el Product Owner, el Scrum Master y los
desarrolladores.

### 2.4 Despliegues y entornos (C1 + C4)

- **GitHub Environments** (`desarrollo`, `staging`, `produccion`) con los
  secretos por entorno: ninguna credencial vive en el repositorio.
- `deploy-dev.yml` + `scripts/deploy-dev-back.sh` / `-front.sh`: el despliegue
  es un script versionado, con healthcheck y salida distinta de cero si falla.
- **3 compose** (`dev`, `test`, `prod`) y el **schema en PostgreSQL 15** con
  migraciones idempotentes y un runner que registra la versión aplicada.
- El procedimiento completo está en
  [`PLAN-DE-DESPLIEGUE.md`](./PLAN-DE-DESPLIEGUE.md) y el pipeline en
  [`CI-CD-Y-VERSIONADO.md`](./CI-CD-Y-VERSIONADO.md).

### 2.5 Configuración como código (C4)

Las reglas del proyecto están **en el repositorio**, versionadas y con historia:

| Dónde | Qué se configura |
| --- | --- |
| `.github/CODEOWNERS` | Quién revisa cada ruta |
| `.github/workflows/` | CI, validaciones de PR y despliegue |
| `.github/ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE.md` | Formato de issues y PRs |
| `.github/dependabot.yml` | Actualizaciones de dependencias |
| `SECURITY.md`, `LICENSE`, `CHANGELOG.md` | Política de seguridad, licencia y cambios |
| **Rulesets** de la organización | Qué ramas existen, qué checks son obligatorios, cuántas aprobaciones hacen falta y si se puede hacer push directo |
| `conventions/` | Ramas, commits, contrato de la API, base de datos, seguridad, versionado y pruebas |

Cualquier cambio en estas reglas es **un PR más**, con su revisión y su
historia. Nadie necesita "¿recuerdas cómo se hacía esto?".

### 2.6 Adaptación al equipo (C5)

- **`AGENTS.md` + 8 skills** (`.agents/skills/`): cada repo explica cómo se
  trabaja en él (arquitectura, envelope, OpenAPI, Docker, migraciones,
  CI/CD, estilo de issues, documentación). Un contributor nuevo —o un agente
  automático— tiene las reglas del repo sin que nadie las escriba otra vez.
- **4 devcontainers** (`.devcontainer/`): el entorno de trabajo completo se
  crea solo, en local o en **Codespaces**, sin instalar Node, Docker ni
  PostgreSQL a mano.
- **Documentación en el mismo sitio** que el código: el anteproyecto, el
  cronograma, las convenciones y el plan de despliegue viven en
  `dolynation-ehecatl-docs` y se versionan igual que el código.

---

## 3. Alternativas evaluadas y por qué no

| Alternativa | Por qué no |
| --- | --- |
| **GitLab** (self-hosted) | Requiere mantener la instancia, el runner y las actualizaciones. El proyecto no tiene operador de infraestructura; el plan gratuito de GitHub cubre lo necesario. |
| **Bitbucket** | La integración con CI/CD, reglas de rama y Project es más débil; obligaría a sumar herramientas de terceros. |
| **CircleCI / Jenkins** | Un motor de CI **además** de la plataforma: dos configuraciones, dos credenciales, dos lugares donde falla algo. Con Actions, el CI vive junto al código. |
| **Jira + Trello/Notion** | El tablero sería una copia del estado real, con riesgo de divergir. En GitHub, la issue **es** la tarea y el Project **es** la vista; no hay sincronización que mantener. |
| **Google Docs / Notion para el plan** | El plan dejaría de estar versionado con el código y de revisarse en el mismo PR que la cambia. |
| **Repositorio único (monorepo)** | Se evaluó y se descartó: cuatro repos con CODEOWNERS por área permiten que backend y frontend avancen en paralelo sin bloquearse mutuamente. El monorepo original (`doly-languages`) queda archivado como histórico. |

---

## 4. Límites reales de la decisión

Conviene ser honestos sobre lo que GitHub **no** da:

| Límite | Consecuencia | Cómo lo mitigamos |
| --- | --- | --- |
| **Plan gratuito**: no hay *organization rulesets* | Las reglas se configuran por repositorio (3 rulesets × 4 repos = 12) | Se mantiene el mismo patrón en los 4, y `operations/FLUJO-DE-TRABAJO.md` lo documenta |
| **Minutos de Actions** | Un uso intensivo puede agotarlos | El CI solo corre en PRs y en `develop`; las matrices están acotadas |
| **Codespaces** consume cómputo | Costo si se dejan abiertos | Se documenta en el onboarding cómo pararlos y borrarlos |
| **Los *bypass actors* se quitaron** | Nadie puede fusionar sin revisión del code owner | Cada ruta tiene ≥2 owners, así que siempre hay alguien del equipo que pueda aprobar |
| **Dependencias entre repos** | Se expresan con la API de dependencias, no con un tablero nativo | Se validan con un grafo (0 ciclos) y se revisan en la planeación |

---

## 5. Conclusión

GitHub cubre los cinco criterios con la configuración que el proyecto ya tiene:
**automatización** (24 workflows, checks obligatorios, despliegue y release),
**trazabilidad** (68 issues con labels, milestones, sub-issues, dependencias y
Project), **revisión** (CODEOWNERS + rulesets obligatorios, sin excepciones),
**configuración como código** (todo en el repositorio) y **coste cero** (plan
gratuito) con una sola plataforma que aprender.

El coste de esta decisión es que **el proyecto depende de GitHub**: si mañana
se quisiera migrar, habría que reconstruir el tablero, los checks y las reglas.
Es un coste aceptable porque la alternativa (varias herramientas) costaría más
en tiempo de equipo, que es el recurso escaso de este proyecto.

Las decisiones concretas que se derivan de aquí están en
[`../decisions/README.md`](../decisions/README.md) (ADR-009) y el detalle
operativo en [`FLUJO-DE-TRABAJO.md`](./FLUJO-DE-TRABAJO.md).
