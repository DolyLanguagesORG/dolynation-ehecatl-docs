# Flujo de trabajo del repositorio

Este documento es el mapa completo de cómo se trabaja en
`DolyLanguagesORG/doly-languages`: qué ramas existen, cómo viaja una tarea
desde el cronograma hasta producción, dónde se registra el trabajo y qué
reglas te bloquean.

Para el paso a paso de abrir un PR, ve a
[COMO-HACER-UN-PR.md](./COMO-HACER-UN-PR.md).

## El panorama en una imagen

```
   CRONOGRAMA                 PLANIFICACIÓN (GitHub)
   docs/cronograma.md    ──►  issues  +  milestones  +  Project
   33 tareas, 5 sprints         │        │              │
   quién / cuándo                │        │              │
                                 │        │              │
                          ┌──────┴────────┴──────────────┴──────┐
                          │  Asignar → In Progress             │
                          │  Tarjeta en el Kanban              │
                          └──────┬─────────────────────────────┘
                                 │
                          ┌──────▼──────────┐
                          │  Rama de trabajo │  feat/ fix/ chore/ docs/
                          │  + commits      │  validados por husky local
                          └──────┬──────────┘
                                 │
                          ┌──────▼──────────┐
                          │  PULL REQUEST    │  ← aquí va Closes #N
                          │  7 checks CI     │
                          │  1 aprobación    │
                          └──────┬──────────┘
                                 │  squash
                          ┌──────▼──────────┐
                          │    develop      │  integración diaria
                          └──────┬──────────┘
                                 │  PR + checks + 1 aprobación
                          ┌──────▼──────────┐
                          │     main        │  producción
                          └──────┬──────────┘
                                 │  se dispara
                          ┌──────▼──────────┐
                          │  release.yml    │  tag + GitHub Release
                          │  v0.x.y         │
                          └─────────────────┘
```

## Las tres ramas

| Rama | Qué es | Recibe PR de | Qué pasa al mergear |
| --- | --- | --- | --- |
| `develop` | **Integración diaria.** Aquí vive el trabajo del día. | `feat/*` `fix/*` `chore/*` `docs/*` | Nada. Se acumula. |
| `main` | **Producción.** Estable entre releases. | Solo `develop` o `hotfix/*` | **Dispara `release.yml`**: tag y GitHub Release |
| `hotfix/*` | Corrección urgente sobre producción. | — | Sale de `main`, luego se lleva a `develop` |

`main` es la única que genera releases. Ese es el motivo de que esté tan
protegida: tocarla es un acto, no un merge rutinario.

`develop` recibe todo el trabajo y por eso es la que se abre y se cierra
constantemente. Nunca debe estar en un estado que no se pueda construir.

### Por qué `develop` es la rama por defecto

`develop` es la rama por defecto del repositorio, y `main` no lo es. Esto no es
un detalle menor: de la rama por defecto dependen cosas que **no funcionan si no
coincide con la rama de trabajo**.

| Depende de la default | Consecuencia |
| --- | --- |
| **Palabras clave de cierre** (`Closes`, `Fixes`, `Resolves`) | GitHub solo las interpreta si el PR apunta a la default. Con `main` como default, ningún PR a `develop` cerraba su issue. |
| **Enlaces issue ↔ PR** (sección *Development*, campo *Linked pull requests* del Project) | Con `main` como default no se creaban, y el campo quedaba siempre vacío. |
| **Workflows con `schedule` o `workflow_dispatch`** | Solo se activan si el archivo del workflow existe en la default. |

Por eso se invirtió. `develop` es el tronco real del proyecto: es donde se
integra el trabajo y donde siempre se puede construir. `main` es un artefacto
de release, y para eso ya tiene su propio disparador (`release.yml`), que no
depende de la default.

**El único costo:** el PR de release `develop` → `main` apunta a una rama que
ya no es la default, así que ahí la palabra clave se ignora. Ese PR debe usar
`Refs #N`, nunca `Closes #N`. Y el release sigue disparándose igual, porque
`release.yml` filtra por `push` a `main` de forma explícita.

> ¿Por qué la convención de GitHub es que la default sea `main`? Porque su
> modelo de trabajo ([GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow))
> tiene **una sola rama**, que es a la vez la de trabajo y la de release. Ahí no
> hay conflicto. Este repositorio tiene dos ramas vivas, y la default tiene que
> ser la del trabajo.


## El viaje de una tarea

### 1. Sale del cronograma

El plan vive en [`docs/cronograma.md`](./cronograma.md). 33 tareas, 5 sprints,
del 5 de octubre al 10 de diciembre de 2026. Cada fila tiene: número, issue
asociado, descripción, responsable, fecha de inicio y fecha de entrega.

**El "Responsable" del cronograma es texto, no una asignación.** Es
documentación. Para que GitHub notifique a alguien, filter por persona o lo
muestre en el tablero, necesitas el campo **Assignee** del issue.

### 2. Se registra en GitHub

Cada tarea del cronograma tiene un issue. Los tres registros de planificación
se complementan, no se sustituyen:

| Dónde | Pregunta que responde | Ejemplo |
| --- | --- | --- |
| **Issue** | ¿Qué hay que hacer? | `#12` Ver detalle, comments,PRs |
| **Milestone** | ¿En qué sprint cae? | `Sprint 1: Infraestructura, Autenticación y Perfil` |
| **Project** | ¿Dónde va en el tiempo y en el flujo? | Kanban con Status y fechas |

Y dentro del issue, tres campos de clasificación:

| Campo | Qué es | Cuántos | Ejemplo |
| --- | --- | --- | --- |
| **Type** | Qué clase de cosa es. Lo define la organización, es cerrado. | exactamente 1 | `Task` · `Feature` |
| **Labels** | Etiquetas libres para filtrar. Dos ejes: cuándo y qué parte. | varias | `sprint-1`, `area:backend` |
| **Assignee** | Quién lo hace. Cuenta real de GitHub. | varias | `@XxjesusalbertoxX` |

**Type vs Labels.** El Type es uno solo y no lo inventas: en esta organización
hay `Task`, `Bug` y `Feature`. Las labels son muchas y las define el equipo.
La regla que se aplicó para los 33 issues:

- **`Feature`** → entrega una capacidad que el usuario puede ejercer
  (endpoints de negocio, vistas, componentes, servicios de dominio).
- **`Task`** → setup, infraestructura interna, pruebas, revisión,
  documentación y release.

**Labels.** Dos familias, dos ejes distintos:

| Familia | Eje | Valores |
| --- | --- | --- |
| `sprint-1` … `sprint-5` | **cuándo** | una por sprint |
| `area:*` | **qué parte del producto** | `backend` `frontend` `fullstack` `qa` `infra` `docs` |

Las labels sobreviven al cierre, así que sirven para buscar histórico:
`label:area:backend is:closed`.

### 3. Entra al tablero

El Project de la organización es
[DolyNation — Plan de Desarrollo](https://github.com/orgs/DolyLanguagesORG/projects/1).
Tiene tres vistas y un campo `Status` de cuatro valores:

```
Todo  ──►  In Progress  ──►  In Review  ──►  Done
```

El ciclo de una tarea, con lo que hay que hacer en cada paso:

| Estado | Qué está pasando | Qué haces |
| --- | --- | --- |
| `Todo` | Planificada, sin empezar | — |
| `In Progress` | Alguien ya está trabajando | Asignar, crear la rama |
| `In Review` | El PR está abierto | Esperar checks y aprobación |
| `Done` | Mergeada | El issue ya se cerró solo |

**El Status del Project y el estado open/closed del issue son cosas
distintas.** Puedes tener un issue cerrado con la tarjeta en `In Progress`
(tecnicamente posible, significa "hay que sincronizar el tablero"), o al
revés. Cuando merges el PR, el issue se cierra; **mover la tarjeta a `Done`
es manual**.

### 4. Se desarrolla

Rama nueva desde `develop`, commits, y el PR. Todo eso está detallado en
[COMO-HACER-UN-PR.md](./COMO-HACER-UN-PR.md).

    Lo que conecta el PR con la planificación es la palabra `Closes #N` en el
    cuerpo del PR. Al mergear en `develop`, el issue se cierra solo. Ese PR
    apunta a la rama por defecto, que es lo que hace que la palabra funcione.

### 5. Se revisa a fin de sprint

Cada sprint cierra con una tarea de integración (issues **#14**, **#28**,
**#34**): pruebas, corrección de bugs y merge a `develop`. Ahí es donde se
detecta lo que se rompió antes de llegar a `main`.

### 6. Se libera

`v1.0.0` es la entrega de cierre (issue **#37**). Consiste en un PR de
`develop` a `main`, que dispara `release.yml`.

## CODEOWNERS

**Qué es.** Un archivo (`.github/CODEOWNERS`) que dice qué persona debe
revisar qué archivos. Cuando abres un PR que toca esos archivos, GitHub pide
su revisión automáticamente, sin que nadie lo solicite a mano.

**Qué hay hoy.**

| Ruta | Owner | Por qué |
| --- | --- | --- |
| `*` (todo) | `@SebastianRdzC04` `@XxjesusalbertoxX` | Default del repo |
| `/backend/src/common/`, `/auth/`, `/readings/`, `/ia/`, `/users/`, `main.ts`, `app.module.ts`, `/database/`, `/config/` | `@SebastianRdzC04` | Código compartido y sensible |
| `/docs/`, `/.github/`, `/infrastructure/` | `@SebastianRdzC04` | Documentación, CI e infraestructura |

**Lo importante: aquí CODEOWNERS es una recomendación, no una obligación.**

El repositorio está configurado con `require_code_owner_reviews: false`. Eso
significa que GitHub **pide** la revisión del owner pero **no bloquea** el merge
si no llegó. Lo único que bloquea es **1 aprobación de cualquier persona con
acceso al repo**.

En otras palabras:

| Pregunta | Respuesta |
| --- | --- |
| ¿GitHub pide revisión al owner? | Sí, automáticamente |
| ¿El merge se bloquea si el owner no aprueba? | **No** |
| ¿Quién sí bloquea? | Cualquiera con acceso, y hace falta al menos 1 |
| ¿Y a quién puede aprobar? | A cualquiera con acceso, no tiene que ser owner |

**Cómo está configurado a propósito.** La protección exige 1 aprobación y el
repositorio es de `@SebastianRdzC04`, mientras que el owner real del
cronograma de trabajo es el Scrum Master. Con
`require_code_owner_reviews: true`, el PR quedaría atascado esperando a una
persona que no participa en el desarrollo del sprint. Con `false`, el
responsable del día aprueba sin fricción.

**Si algún día quieres que sí sea obligatorio**, hay que poner
`require_code_owner_reviews: true` y tener al menos a un owner del equipo en
la lista. Hoy no lo es.

**Placeholders pendientes.** El archivo tiene tres marcadores sin resolver
(`@PLACEHOLDER-1`, `@PLACEHOLDER-2`, `@PLACEHOLDER-3`) para Azael, Juan y
Elías. Hasta que se completen, esas personas no tienen revisión automática ni
aparecen como owners.

## Dependencias entre issues

A veces dos tareas tienen un orden obligatorio. El caso real del proyecto:
**#37** (PR final a `main` y tag `v1.0.0`) está **bloqueado por #36** (pruebas
de rendimiento y seguridad). No se puede cerrar la entrega sin las pruebas.

Eso se registra con la relación *blocked by* y aparece en la sección
*Relationships* de ambos issues. GitHub también ofrece *relates to* para
tareas que se tocan sin depender.

**Dependencia no es lo mismo que subtarea:**

| | Subtarea (*sub-issue*) | Dependencia (*blocked by*) |
| --- | --- | --- |
| Relación | Contiene. Jerárquica. | Orden. Horizontal. |
| Pregunta | "¿De qué partes se compone?" | "¿Qué tiene que pasar antes?" |
| Uso | Dividir una tarea grande | Bloquear el avance |
| Ejemplo | `#12 Panel admin` → `#A CRUD usuarios`, `#B CRUD reportes` | `#37` espera a `#36` |

## Releases y versionado

`release.yml` corre cuando algo llega a `main`. El **título del PR** decide el
salto de versión (ver [conventions/versioning.md](./conventions/versioning.md)):

| Título del PR | Salto | Ejemplo |
| --- | --- | --- |
| `fix:` `refactor:` `chore:` `docs:` `ci:` `test:` `perf:` | patch | `v0.1.0` → `v0.1.1` |
| `feat:` | minor | `v0.1.0` → `v0.2.0` |
| `!` (breaking change) | major | `v0.1.0` → `v1.0.0` |

Esto significa que **el título del PR no es solo cosmético**: decide el número
de versión que se publica. `v1.0.0` requiere un `!` o un `feat` en el PR de
release.

## Hotfixes

Corrección urgente sobre producción:

```bash
git switch main
git switch -c hotfix/logo-roto
# ... commitea el fix mínimo ...
    gh pr create --base main --title "fix(ui): corrige el logo" --body "Refs #52"
```

Después de mergearlo en `main`, hay que devolverlo a `develop`, o el fix
desaparece en el siguiente merge:

```bash
git switch develop
git cherry-pick <sha-del-hotfix>
git push origin develop
```

## Qué reglas te bloquean, y cuáles no

Esto es lo que tienes que saber para no confiar de más en las herramientas.

**Bloquean de verdad** (configuración de GitHub, no se pueden saltar salvo
que seas admin):

- 7 checks de CI en verde
- 1 aprobación de otra persona
- Toda conversación del PR resuelta
- Nada de force-push, nada de borrar ramas, nada de merge commits
- Solo squash-merge

**No bloquean** (dependen de que tú seas disciplinado):

| Regla | Por qué no se aplica |
| --- | --- |
| **Mensajes de commit** | Solo los valida el hook local de husky. **CI no los revisa.** Si commiteas con `--no-verify` o sin `npm ci`, entra basura. |
| **Scopes de commit** | El regex del CI no los valida contra la lista de `commits.md`. |
| **Idioma de los mensajes** | Nadie lo comprueba. La documentación dice inglés; el historial reciente está en español. **Pendiente de decidir.** |
| **CODEOWNERS** | Se piden, pero no son obligatorios (`require_code_owner_reviews: false`). |
| **Que la rama esté al día** | `develop` no exige estar al día con la base. Puedes mergear con la rama atrasada. |
| **El checklist de la plantilla** | Es un recordatorio, no un gate. |

**Y una advertencia concreta**: `enforce_admins` está en `false`. Eso significa
que los administradores del repo **pueden saltarse todas las protecciones**
haciendo push directo a `develop` o `main`. Existe porque, en un equipo de una
persona, un bloqueo de auto-aprobación dejaría el repo trabado. No es una
práctica recomendada para el día a día; cuando haga falta, es preferible bajar
temporalmente el requisito de aprobaciones y restaurarlo después.

## Dónde vive cada cosa

| Necesitas... | Ve a |
| --- | --- |
| Saber qué hacer hoy | [Project](https://github.com/orgs/DolyLanguagesORG/projects/1) → vista Kanban |
| Ver fechas y qué se solapa | Project → vista Timeline |
| Leer el detalle de una tarea | El issue |
| Ver el avance del día | [Discussion #39](https://github.com/DolyLanguagesORG/doly-languages/discussions/39) (standup) |
| Ver el plan completo | [`docs/cronograma.md`](./cronograma.md) |
| Saber cómo abrir un PR | [COMO-HACER-UN-PR.md](./COMO-HACER-UN-PR.md) |
| Reglas de ramas | [conventions/git-workflow.md](./conventions/git-workflow.md) |
| Reglas de commits | [conventions/commits.md](./conventions/commits.md) |
| Reglas de versionado | [conventions/versioning.md](./conventions/versioning.md) |
| Montar el entorno | [onboarding/setup.md](./onboarding/setup.md) |

## Documentos relacionados

- [COMO-HACER-UN-PR.md](./COMO-HACER-UN-PR.md) — el paso a paso
- [CONTRIBUTING.md](./CONTRIBUTING.md) — entrada rápida
- [cronograma.md](./cronograma.md) — las 33 tareas
- [conventions/](./conventions/README.md) — todas las convenciones
