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
> describe el **pipeline completo** de extremo a extremo y **qué está
> implementado y qué falta**.

---

## 0. Estado real

| Componente | Estado | Dónde |
| --- | --- | --- |
| Versionado automático en `develop` | ✅ **Implementado** | `.github/workflows/release-please.yml` en los 4 repos |
| Tag anotado + GitHub Release (*Pre-release*) | ✅ **Implementado** | paso *"Convertir el tag en anotado"* del mismo workflow |
| Manifiesto multirepo (`versions.yml`) | ✅ **Implementado** | `dolynation-tlalli-infra/versions.yml` |
| Actualización automática del manifiesto | ✅ **Implementado** | `.github/workflows/sync-versions.yml` en infra |
| Autodespliegue a desarrollo con la versión inyectada | ✅ **Implementado** | `deploy-dev.yml` en back y front |
| Version visible en la API | 🔶 En curso | `atl-back#69` |
| Version visible en el frontend | 🔶 En curso | `tonatiuh-front#43` |
| Ambiente de staging | 🔶 Pendiente | `infra#43` |
| Deploy a staging desde `rc-<version>` | 🔶 Pendiente | `infra#14`, `infra#8` |
| Smoke test y checklist de salida de staging | 🔶 Pendiente | `infra#44` |
| Gate de producción (Environment con revisores) | 🔶 Pendiente | `infra#45` |
| Rulesets de `main` y `rc-*` | 🔶 Pendiente | `infra#46` |
| Cascada `infra → back/front` | 🔶 Pendiente | `infra#8` |
| Prueba de extremo a extremo del tren de release | 🔶 Pendiente | `infra#48` |

---

## 1. Arquitectura y principios de diseño

- **Estrategia multirepo:** los servicios evolucionan de forma independiente,
  pero se coordinan de forma centralizada mediante el repo de manifiesto
  (`dolynation-tlalli-infra`).
- **Versionado semántico (SemVer):** conducido automáticamente por
  *Conventional Commits*; nadie edita una versión a mano.
- **Fuente de la verdad:** `infra` centraliza en `versions.yml` el tag, la
  versión y el commit exacto de cada servicio, para que un despliegue maintain
  compatibilidad estricta entre componentes.
- **Zero Trust:** nada entra a `develop` o `main` sin pull request, sin checks
  en verde y sin aprobación.

---

## 2. Fase 1 — Desarrollo continuo y versionado (`develop`)

1. **Flujo de trabajo:** se crean ramas de características y se abren pull
   requests hacia `develop` en los repos de código.
2. **Versionado automático:** release-please mantiene **un PR de release
   acumulativo** contra `develop`. Ese PR:
   - sube la versión (`package.json` en back/front, `version.txt` en
     infra/docs),
   - escribe la sección `## [X.Y.Z]` del `CHANGELOG.md`,
   - actualiza el `.release-please-manifest.json`,
   - y en el caso de infra, su fila del `versions.yml`.
3. **Al mergear ese PR:** se crea el **tag anotado** `vX.Y.Z`, se publica la
   **GitHub Release** (marcada como *Pre-release* mientras la versión sea
   `0.x`) y se notifica al manifiesto del proyecto.
4. **Despliegues de desarrollo:** cada repo, en `push` a `develop`, despliega
   su servicio por SSH y verifica el healthcheck. El backend expone la
   `version` y el `commit` del build en ejecución.

Detalle de las reglas de bump en
[conventions/versioning.md](../conventions/versioning.md).

### Por qué el tag nace en `develop` y no en `main`

release-please acopla el PR de release con la creación del tag: la etiqueta
`autorelease: pending` solo se cambia cuando se crea el release. Si se le dice
"no publiques" (`skip-github-release`), el PR mergeado se queda con esa
etiqueta y en la siguiente corrida el bot detecta *"merged, untagged release
PRs outstanding"* y **aborta**: nunca vuelve a abrir un PR de release.

Además, sin tag no encuentra el punto de corte de los commits y el changelog
acumularía duplicados.

Por tanto: **el tag tiene que nacer donde nace la versión**. `main` es la
promoción, no el generador. La ventaja práctica es que en desarrollo el número
**se ve subir**: nunca está congelado, y `/health` dice siempre qué está
corriendo.

---

## 3. Fase 2 — Preparación de la Release Candidate (`rc-<version>`)

1. **Congelamiento de versión:** cuando `develop` alcanza un hito maduro para
   pruebas, se toma el número exacto de la versión de cada repositorio (ya está
   escrito en `develop`) para establecer la candidata.
2. **Registro en infraestructura:** se crea la rama `rc-<version>` en
   `dolynation-tlalli-infra` y se actualiza `versions.yml` con el tag y el
   commit exactos de cada servicio.

> La rama `rc` vive **solo en infra**: `versions.yml` ya lleva el pin exacto de
> los cuatro repos, así que una `rc` en cada repo sería una segunda fuente de
> verdad que habría que mantener sincronizada. Es además *single-flight*: sólo
> una `rc` a la vez.

---

## 4. Fase 3 — Validación y despliegue en QA / Staging

1. **PR único:** se abre un único PR en `infra` con el `versions.yml` al alza.
2. **Candado anti-degradación (Zero Trust):** las GitHub Actions de `infra`
   validan que cada tag y cada commit del manifiesto existen realmente. Si
   alguno no existe, el despliegue **no sale** y el error dice qué falta.
3. **Autodespliegue:** al autorizar el merge, el servidor autohospedado
   descarga las imágenes de los tags exactos del manifiesto y actualiza el
   ambiente de staging.
4. **Smoke test + checklist:** un workflow verifica que la API, el frontend y
   la base de datos responden, y una persona recorre el checklist de salida.

---

## 5. Fase 4 — Salida a producción

1. **Paso a `main`:** una vez superado el staging, se autoriza el PR hacia
   `main` en `infra`.
2. **Efecto dominó automatizado:** mediante un **PAT**, el merge en `infra`
   dispara en cascada la apertura de los PRs hacia `main` en `atl-back` y
   `tonatiuh-front` (ver [§7](#7-disparadores-y-cascada)).
3. **Gate de producción:** el despliegue a producción usa el GitHub Environment
   `produccion` con *required reviewers*: **el workflow se pausa y espera a que
   alguien autorice la salida**. Ninguna promoción es automática.
4. **Despliegue y release oficial:** se actualiza la infraestructura productiva
   y la GitHub Release deja de ser *Pre-release*.

---

## 6. Fase 5 — Consolidación estable

1. **Período de observación:** el sistema opera en producción bajo la etiqueta
   Beta, validando la estabilidad de todos los módulos en uso real.
2. **Bandera a estable:** tras verificar la integridad de extremo a extremo, se
   marca la versión como **Release oficial / estable**, cerrando el ciclo.
3. **Limpieza:** se borra la rama `rc-<version>`, que libera el ciclo y
   permite abrir la siguiente candidata.

---

## 7. Disparadores y cascada

- El disparador canónico del versionado es `push` a `develop`, que dispara
  `release-please.yml`.
- La promoción entre ramas usa eventos de PR con la guarda
  `github.event.pull_request.merged == true` y un filtro por
  `github.base_ref` (`develop`, `main` o `rc-*`). Así, **sólo un merge real**
  dispara el pipeline; cerrar un PR sin mergear no hace nada.
- **`GITHUB_TOKEN` no dispara workflows.** Los eventos generados con el token
  por defecto no inician workflows nuevos, por eso la cascada
  `infra → back/front` necesita un **PAT**.
- Los jobs usan `concurrency` con `cancel-in-progress: false` para
  **serializar** runs y evitar carreras entre versiones.

### 7.1. La cascada en detalle

La cascada **abre** los PRs; **no los mergea**. `main` exige aprobación, y que
un bot la esquivara vaciaría esa garantía.

| Quién | Qué hace |
| --- | --- |
| `atl-back`, `tonatiuh-front` | Al publicar su tag, envían un `repository_dispatch` a infra con su repositorio, versión y commit. |
| `tlalli-infra` (`sync-versions.yml`) | Actualiza la fila del repositorio en `versions.yml` y abre el PR con el cambio. |
| `tlalli-infra` (cascada) | Al promover a `main`, abre los PRs `develop → main` en back y front con un PAT. |

---

## 8. Versionado automático

- La fuente es **Conventional Commits**; con squash, **un PR = un bump**.
- El bump lo calcula release-please sobre **todos** los commits del ciclo.
- El crecimiento de la versión no es un problema (`v0.43.253` es válido); el
  minor resetea el patch.

| Patrón en el título del PR | Bump | Resultado |
| --- | --- | --- |
| `feat(scope): ...` | minor | `v0.1.0` → `v0.2.0` |
| `feat(scope)!: ...` o `BREAKING CHANGE:` | major | `v0.1.0` → `v1.0.0` |
| `fix(scope): ...` | patch | `v0.1.0` → `v0.1.1` |
| `refactor` `chore` `docs` `ci` `test` `perf` `style` | — | **no genera versión** |

La tabla completa y las reglas están en
[conventions/versioning.md](../conventions/versioning.md).

### 8.1. La versión que se ve en la aplicación

Hay **dos** versiones, y conviene no confundirlas:

| Versión | Dónde vive | Quién la ve |
| --- | --- | --- |
| **De la aplicación** (`app_version`) | `versions.yml` | El usuario final y la auditoría |
| **Del componente** | `package.json` / `version.txt` | Quien despliega ese repositorio |
| **El commit** | `GIT_COMMIT` inyectado en el build | Quien audita el build exacto |

La API expone las dos en `GET /api/v1/version`, y el frontend en
`/version.json`. Ver `atl-back#69` y `tonatiuh-front#43`.

---

## 9. Notas y decisiones

- **Mensajes en español:** los Conventional Commits del equipo son en español;
  el check `pr-title` valida el formato, no el idioma.
- **`main` es la promoción, no el generador.** El tag nace en `develop`; ver
  [§2](#2-fase-1--desarrollo-continuo-y-versionado-develop).
- **`rc-*`:** son ramas efímeras y *single-flight*: sólo una a la vez, en
  `tlalli-infra`. Mientras exista una `rc`, no se puede iniciar otra release;
  al consolidarla en `main` se elimina la rama y se libera el ciclo.
- **Bypass actor:** los rulesets de `develop` declaran a `@XxjesusalbertoxX`
  con `bypass_mode: always`. Es lo que permite al bot de versionado mergear sus
  propios PR de release, que de otro modo quedarían bloqueados esperando una
  aprobación. El resto del equipo no tiene atajos.
