# CI/CD y Versionado — DolyNation

Documentación del flujo integral de **Integración Continua**, **Entrega
Continua** y **versionado automático** para el ecosistema multirepositorio de
DolyNation: `dolynation-atl-back` (backend), `dolynation-tonatiuh-front`
(frontend), `dolynation-tlalli-infra` (infraestructura) y
`dolynation-ehecatl-docs` (docs).

> Para las reglas de ramas y commits del día a día, ver
> [conventions/git-workflow.md](../conventions/git-workflow.md),
> [conventions/commits.md](../conventions/commits.md) y
> [conventions/versioning.md](../conventions/versioning.md). Este documento
> describe el **pipeline completo** de extremo a extremo.

## Entornos (3)

DolyNation corre en **3 entornos de despliegue**:

| Entorno | Se despliega con | Trigger |
| --- | --- | --- |
| **Desarrollo** | merge a `develop` | automático |
| **Staging** | rama `rc-<version>` (con `versions.yml`) | automático |
| **Producción** | merge a `main` (desde la `rc` aceptada) | automático |

`rc-*` **no es un entorno**: es una rama/estado efímero y *single-flight* (solo
una a la vez). Mientras exista una `rc`, no se puede iniciar otra release; al
consolidarla en `main` se elimina la rama y se libera el ciclo.

---

## 0. Estado: hoy vs. objetivo

El pipeline por fases (abajo) es el **objetivo** acordado. Parte de él todavía
no está implementado:

| Componente | Hoy | Objetivo |
| --- | --- | --- |
| Checks de CI | Implementados en los 4 repos (`ci-*.yml`, `pr-title`, `pr-labels`) | Igual |
| Versionado | Script propio en `release.yml` que corre en `push` a `main` | **release-please** con PR acumulativo en `develop` (`infra#7`, fuera de la entrega) |
| Tag / Release | Se crea al llegar a `main` | Se crea al mergear el PR de release |
| Entornos (desarrollo, staging, producción) | Planificado; issues `infra#6`-`infra#9` | Deploy por SSH a 3 entornos; `rc-*` es rama efímera |
| Manifiesto `versions.yml` | Planificado (`infra#7`) | Fuente de verdad de versiones en `infra` |
| Cascada `infra → front/back` | Planificado (`infra#8`) | PRs automáticos vía PAT |

---

## 1. Arquitectura y principios de diseño

El flujo está diseñado bajo una filosofía **Zero Trust** y automatizada, para
eliminar los errores humanos, las discrepancias de versiones y los despliegues
manuales por SSH.

- **Estrategia multirepo:** los servicios evolucionan de forma independiente,
  pero se coordinan de forma centralizada mediante el repo de manifiesto
  (`dolynation-tlalli-infra`).
- **Versionado semántico (SemVer):** conducido automáticamente por
  *Conventional Commits*; nadie edita una versión a mano.
- **Fuente de la verdad:** `infra` centraliza en `versions.yml` los tags
  exactos de cada servicio, para que un despliegue mantenga compatibilidad
  estricta entre componentes.

---

## 2. Fase 1 — Desarrollo continuo y versionado (`develop`)

1. **Flujo de trabajo:** los desarrolladores crean ramas de características y
   abren Pull Requests hacia `develop` en los repos de código (*frontend* y
   *backend*).
2. **Versionado automático:** el mechanism vigente es el workflow `release.yml`,
   que se dispara al llegar a `main`: calcula la versión a partir del último
   tag y de los commits mergeados, crea el **tag anotado** y publica el GitHub
   Release con las notas. El variante con
   [release-please](https://github.com/googleapis/release-please) (un PR de
   release acumulativo contra `develop`) está diseñado en `infra#7` y quedó
   fuera de la entrega: ver la sección 8.
3. **Despliegues de desarrollo:** se compilan contenedores temporales para
   habilitar un entorno de desarrollo en la nube en tiempo real, sin saturar el
   registro con versiones estables prematuras.

Detalle de las reglas de bump en
[conventions/versioning.md](../conventions/versioning.md).

---

## 3. Fase 2 — Preparación de la Release Candidate (`rc-[version]`)

1. **Congelamiento de versión:** cuando `develop` alcanza un hito maduro para
   pruebas, se toma el número exacto de la versión (por ejemplo `v0.3.9`) para
   establecer la candidata.
2. **Registro en infraestructura:** se crea una rama de release en
   `dolynation-tlalli-infra`, actualizando `versions.yml` con los tags exactos
   de los servicios:

   ```yaml
   frontend: "v0.3.9"
   backend: "v0.2.9"
   ```

---

## 4. Fase 3 — Validación y despliegue en QA / Staging

1. **PR único:** se abre un único PR en `infra` apuntando hacia la rama de
   staging.
2. **Candado anti-degradación (Zero Trust):** las GitHub Actions de `infra`
   validan `versions.yml`. Si detectan una versión **igual o menor** a la que ya
   opera en producción, el PR se **bloquea y rechaza automáticamente**,
   previniendo cualquier degradación.
3. **Autodespliegue:** al autorizar el merge en `infra`, el servidor
   autohospedado descarga los contenedores definidos en el manifiesto y
   actualiza de forma autónoma el entorno de staging para las pruebas.

---

## 5. Fase 4 — Salida a producción (versión Beta / pre-release)

1. **Paso a `main`:** una vez superado QA, se autoriza el PR hacia `main` en
   `infra`.
2. **Efecto dominó automatizado:** mediante un token de acceso seguro (**PAT**)
   y acciones automatizadas, el merge en `infra` dispara en cascada la apertura
   de los PRs hacia `main` en los repos de *frontend* y *backend* (ver
   [§7](#7-disparadores-y-cascada)).
3. **Despliegue y beta:** se actualiza la infraestructura productiva y se genera
   automáticamente una **GitHub Release marcada como Beta / pre-release**,
   limpiando de inmediato las ramas temporales.

---

## 6. Fase 5 — Consolidación estable (release oficial)

1. **Período de observación:** el sistema opera en producción bajo la etiqueta
   Beta, validando la estabilidad de todos los módulos en uso real.
2. **Bandera a estable:** tras verificar la integridad de extremo a extremo, se
   marca la versión como **Release oficial / estable**, cerrando el ciclo.

---

## 7. Disparadores y cascada

El versionado y la promoción se apoyan en **events de PR** para respetar Zero
Trust (nadie hace push directo a las ramas protegidas):

- El disparador canónico es `on: pull_request: types: [closed]` con la guarda
  `if: github.event.pull_request.merged == true` y un filtro por
  `github.base_ref` (`develop`, `main` o `rc-*`). Así, **solo un merge real**
  dispara el pipeline; cerrar un PR sin mergear no hace nada.
- **`GITHUB_TOKEN` no dispara workflows.** Los eventos generados con el token
  por defecto no inician workflows nuevos, por eso la cascada
  `infra → front/back` necesita un **PAT** (secret repartido por la org).
- Los jobs usan `concurrency` con `cancel-in-progress: false` para **serializar**
  runs y evitar carreras entre versiones.

---

## 8. Versionado automático

- La fuente es **Conventional Commits**; con squash, **un PR = un bump**.
- Hoy el bump lo calcula el script de `release.yml` al llegar a `main`; el
  variante con *release-please* (PR de release acumulativo) está en `infra#7`,
  fuera de la entrega, y la tabla de bumps de abajo aplica a ambos.
- El crecimiento de la versión no es un problema (`v0.43.253` es válido); el
  minor resetea el patch.

| Patrón en el título del PR | Bump | Resultado |
| --- | --- | --- |
| `fix(scope): ...` | patch | `v0.1.0` → `v0.1.1` |
| `refactor(...)`, `chore(...)`, `docs(...)` | patch | `v0.1.0` → `v0.1.1` |
| `feat(scope): ...` | minor | `v0.1.0` → `v0.2.0` |
| `feat(scope)!: ...` o `BREAKING CHANGE:` | major | `v0.1.0` → `v1.0.0` |

La tabla completa y las reglas están en
[conventions/versioning.md](../conventions/versioning.md).

---

## 9. Notas y decisiones abiertas

- **Mensajes en español:** los Conventional Commits del equipo son en español;
  el check `pr-title` valida el formato, no el idioma.
- **Relación `develop` ↔ `main`:** definir cómo se refleja un release de
  `develop` en `main` sin duplicar el tag.
- **`rc-*`:** son ramas efímeras y *single-flight*: solo una a la vez. Mientras
  exista una `rc`, no se puede iniciar otra release; se elimina al consolidar la
  release en `main` para liberar el ciclo.
- **Implementación de los entornos:** servidor, puertos, secretos y ramas de
  despliegue se detallan en [PLAN-DE-DESPLIEGUE.md](./PLAN-DE-DESPLIEGUE.md)
  (propuesta, aún no implementada).
