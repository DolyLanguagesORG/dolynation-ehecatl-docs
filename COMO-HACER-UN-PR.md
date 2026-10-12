# Cómo hacer un Pull Request

Guía práctica del repositorio. Si solo te lees una sección, léete
[El flujo completo de una tarea](#el-flujo-completo-de-una-tarea).

## Las 6 órdenes, y ya

```bash
git switch develop && git pull
git switch -c docs/issue-6-guia-pr
cd backend && npm run verify && cd ..
git add -A
git commit -m "docs(repo): agrega la guia de pull requests"
git push -u origin docs/issue-6-guia-pr
gh pr create --base develop \
  --title "docs(repo): agrega la guia de pull requests" \
  --body "## Resumen
- Documenta el flujo de PR paso a paso
Closes #6"
```

Eso es un PR completo. El resto de este documento explica **por qué**
funciona y qué pasa si te saltas un paso.

## Requisitos (una sola vez)

```bash
git clone git@github.com:DolyLanguagesORG/doly-languages.git
cd doly-languages
cd backend && npm ci && cd ..
```

`npm ci` es lo que instala **husky**, los hooks que validan tus commits
([abajo](#qué-se-valida-en-tu-máquina-y-qué-no)). Si te lo saltas, commitear
no te va a avisar de nada.

## El flujo completo de una tarea

### 1. Sincroniza `develop`

```bash
git switch develop
git pull
```

Nunca construyas sobre un `develop` viejo. Si alguien mergeó mientras
trabajabas, esto lo trae.

### 2. Crea la rama

```bash
git switch -c feat/issue-12-login-page
```

**Prefijos permitidos** (el check `pr-target` acepta estos, y también el
formato de GitHub que se explica abajo):

| Prefijo | Para qué |
| --- | --- |
| `feat/` | funcionalidad nueva |
| `fix/` | corrección de bug |
| `chore/` | mantenimiento, refactors, tooling |
| `docs/` | solo documentación |
| `hotfix/` | corrección urgente **desde `main`** |

**Reglas de nombre:**

- En `feat/` y `fix/` el **número de issue es obligatorio**: `feat/issue-12-login-page`.
  Sin él nadie puede trazar tu PR en el tablero.
- En `chore/` y `docs/` es opcional.
- Máximo 50 caracteres *(convención del equipo; el CI no lo mide)*.
- El prefijo debe coincidir con el tipo de commit que va a llevar. Si la rama
  es `feat/`, el commit es `feat(...)` y el título del PR es `feat(...)`.
- Todo en kebab-case, sin espacios ni acentos: `docs/actualiza-readme`.

#### ¿Prefijo o el botón *Create a branch*?

Las dos formas valen. El botón **Create a branch** del issue crea la rama como
`<n>-<kebab>` (`12-login-page`), y `pr-target` también la acepta, para que usar
el botón no te deje el CI en rojo.

| | Con prefijo | Formato de GitHub |
| --- | --- | --- |
| Ejemplo | `feat/issue-12-login-page` | `12-login-page` |
| Dice el tipo de cambio | Sí, de un vistazo | No |
| La acepta `pr-target` | Sí | Sí |
| Sale del botón *Create a branch* | No | Sí |

**La forma con prefijo es la recomendada.** No las mezcles en el mismo PR.

> ⚠️ **El botón no hace todo.** Crea la rama y ya. No te asigna el PR, no
> mueve la tarjeta a *In Progress*, no escribe el `Closes #<n>` y no sube
> código. Eso lo haces tú, paso a paso.


### 3. Verifica en local antes de commitear

```bash
cd backend
npm run verify     # typecheck + lint:check + format:check + test
cd ..
```

Este comando es tu red de seguridad. Lo que falla aquí, falla igual en CI pero
tú lo descubres en 20 segundos en vez de esperar 4 minutos. Si tienes que
corregir algo automáticamente:

```bash
npm run verify:fix
```

**Si `verify` falla, casi siempre es una de estas dos cosas** (ninguna es tu
código):

| Síntoma | Causa | Solución |
| --- | --- | --- |
| `'ESLINT_USE_FLAT_CONFIG' is not recognized` | El prefijo de variable de entorno es sintaxis Unix y no funciona en Windows | Ver [Windows](#si-estás-en-windows) abajo |
| `connect ECONNREFUSED 127.0.0.1:5432` en 5 suites | `npm test` incluye los tests e2e, que necesitan Postgres | Levanta Docker ([onboarding/setup.md](./onboarding/setup.md)) o ejecuta solo los unitarios: `npx jest --testPathIgnorePatterns 'e2e-spec'` |

#### Si estás en Windows

Los scripts de `backend/package.json` usan el prefijo
`ESLINT_USE_FLAT_CONFIG=false`, que es sintaxis de shell Unix. En Windows
`npm` lo ejecuta con `cmd` y se rompe. Corre los pasos por separado:

```bash
cd backend
npx tsc --noEmit
ESLINT_USE_FLAT_CONFIG=false npx eslint "{src,test}/**/*.ts"   # en Git Bash
npx prettier --check "{src,test}/**/*.ts"
npx jest --testPathIgnorePatterns 'e2e-spec'
```

Sin Postgres levantado, los 9 suites unitarios (71 tests) deben pasar. Los
e2e son los que necesitan la base de datos.

### 4. Commitea

```bash
git add -A
git status                 # lee qué vas a commitear, siempre
git diff --cached          # lee el diff, siempre
git commit -m "feat(auth): agrega registro de usuarios"
```

**Formato obligatorio** (lo valida el hook local `commit-msg`):

```
<tipo>(<scope>): <descripción>

<cuerpo opcional>

<footer opcional>
```

Tipos permitidos: `feat` `fix` `refactor` `docs` `test` `chore` `build` `ci`
`perf` `style`. Para un cambio que rompe algo: `feat(api)!: ...`

**Commits pequeños.** Un concern por commit. Tres commits enfocados se revisan
más rápido que uno de 80 archivos, y si algo falla sabes exactamente cuál
revertir.

### 5. Sube la rama

```bash
git push -u origin feat/issue-12-login-page
```

### 6. Abre el PR

```bash
gh pr create --base develop \
  --title "feat(auth): agrega registro de usuarios" \
  --body "$(cat <<'EOF'
## Resumen

- Endpoint de registro con hash argon2
- DTO de validación

Closes #12
EOF
)"
```

O en la web: <https://github.com/DolyLanguagesORG/doly-languages/compare/develop...tu-rama>

**Reglas que el CI impone al PR:**

| Regla | Detalle |
| --- | --- |
| **Rama base** | `develop` para trabajo diario. `main` solo para release o hotfix |
| **Rama origen** | `feat/`, `fix/`, `chore/`, `docs/` **o** el formato `<n>-<kebab>` de GitHub |
| **Título** | debe ser Conventional Commits: `tipo(scope): descripción` |
| **Merges** | solo **squash**. No hay merge commit ni rebase merge |

**Las etiquetas se copian solas.** El workflow `pr-labels` lee el `Closes #N`
del cuerpo, busca ese issue y le pone al PR sus etiquetas `sprint-*` y `area:*`.
No tienes que copiarlas a mano, pero **sí tienes que haber escrito el `Closes`**:
si el PR no cierra ningún issue, el workflow no sabe de dónde sacar las
etiquetas y no hace nada.

> **Pon el `Closes` en su propia línea, al principio.** El workflow exige lo
> mismo que GitHub: la palabra tiene que **empezar la línea**, no aparecer
> mencionada en medio de una frase. Si escribes *"el PR anterior llevaba
> `Closes #6`"*, GitHub no cierra el #6… y el workflow tampoco lo toma, así que
> tampoco te pone sus etiquetas. Sirve `- Closes #6`, `> Closes #6` o
> `**Closes #6**`.
>
> `Refs #6` **no** propaga etiquetas: no es una palabra de cierre.
>
> El workflow también se re-dispara cuando **editas** el cuerpo del PR, así que
> no pasa nada si abres el PR y luego añades el `Closes`.
>
> Para cambiar el comportamiento de esa detección hay un test que lee el regex
> del propio workflow, para que no puedan desincronizarse:
>
> ```bash
> node .github/workflows/pr-labels.regex.test.cjs
> ```

### 7. Enlaza el issue: `Closes`, no `Refs`

**Esta es la parte que más confunde, y es la más importante.**

El enlace entre un PR y un issue se escribe **dentro del cuerpo del PR nuevo**,
con una palabra clave. GitHub la lee y llena sola la sección *Development* del
issue.

| Escribes | Qué pasa |
| --- | --- |
| `Closes #6` | El issue se enlaza **y se cierra solo** al mergear el PR ✅ |
| `Fixes #6` / `Resolves #6` | Igual que `Closes` ✅ |
| `Refs #6` | Solo deja una **mención**. El issue **no** se enlaza ni se cierra ❌ |

> ⚠️ **Esto solo funciona si el PR apunta a `develop`, que es la rama por
> defecto del repositorio.** GitHub lee las palabras clave de cierre
> **únicamente** cuando el PR tiene como base la rama por defecto. Si el PR
> apunta a `main`, la palabra se **ignora por completo**: no se crea ningún
> enlace y el issue no se cierra ni aunque merges. Es el caso del PR de
> release `develop` → `main`, así que **ese PR usa `Refs`, nunca `Closes`**.
> Explicación completa en
> [FLUJO-DE-TRABAJO.md](./FLUJO-DE-TRABAJO.md#por-que-develop-es-la-rama-por-defecto).

Tres cosas que no funcionan y la gente intenta:

- **Poner `Closes #6` en el issue.** No. Va en el PR.
- **Enlazar un PR viejo ya mergeado.** No se puede. Solo cuenta el PR que
  creas ahora, mientras está abierto.
- **Pegar un PR a otro PR.** Los PRs no se enlazan entre sí. Un PR se enlaza
  a un issue, y punto.
- **Escribir `Closes` en un PR hacia `main`.** La palabra se ignora. Va en el
  cuerpo, pero apuntando a `develop`.

Si tu PR resuelve varias cosas, repite la palabra clave:

```
Closes #6
Closes #14
Refs #35
```

> **Verifica que el enlace se creó.** Después de abrir el PR, entra al issue y
> comprueba que el PR aparece en la sección **Development**. Si no aparece,
> el enlace no se registró. Comprueba primero que el PR apunta a `develop`:
> si apunta a `main`, no se va a registrar nunca, por muy bien escrita que esté
> la palabra clave.
>
> Si el PR sí apunta a `develop` y el enlace sigue sin aparecer, deja la
> palabra clave igual (es la sintaxis correcta) y enlázalo a mano desde el
> issue, en **Development → Link a pull request**. Aun así el cierre al
> mergear depende de que el PR llegue a la rama por defecto.

#### Si tienes que verificarlo por API, mira el campo correcto

Los dos campos de la API **no coinciden**, y el que se consulta primero miente:

| Campo | Dónde | Qué dice |
| --- | --- | --- |
| `closingIssuesReferences` | En el **PR** | Frecuentemente `[]` aunque el enlace **sí** exista. **No confíes en él.** |
| `closedByPullRequestsReferences` | En el **issue** | Dice la verdad: lista los PRs que cerrarán ese issue. |

Y el evento `cross-referenced` en el timeline aparece siempre, incluso sin
enlace real. **La ausencia de un evento `connected` no prueba que falte el
enlace**: en este repo el enlace se registró sin que apareciera ese evento.

Para comprobarlo de verdad:

```bash
# correcto: pregunta al issue
gh issue view 6 --json closedByPullRequestsReferences \
  --jq '.closedByPullRequestsReferences[].number'

# NO sirve: devuelve [] aunque el enlace exista
gh pr view 45 --json closingIssuesReferences \
  --jq '.closingIssuesReferences[].number'
```



### 8. Espera los 7 checks

Cuando abras el PR arranca el CI. Son **7 checks repartidos en 5 archivos**:

| Check | Qué valida |
| --- | --- |
| `unit-and-static` | tipos, lint, formato y tests unitarios |
| `e2e` | tests end-to-end |
| `build` | que el backend compile |
| `link-check` | que no haya links rotos en la documentación |
| `openapi-guard` | que no se rompa el contrato de la API |
| `pr-title` | el formato del **título del PR** |
| `pr-target` | la **rama base** y la **rama origen** |

Mientras un check esté en rojo o en cola, **GitHub no habilita el botón de
merge**. No es un aviso: es un bloqueo.

### 9. Pide revisión

Las reglas de protección de `develop` y `main`:

| Regla | Qué implica |
| --- | --- |
| 1 aprobación | Alguien con acceso al repo debe aprobar |
| Ramas protegidas | No se pueden borrar ni hacer force-push |
| Conversaciones resueltas | Hay que responder o resolver cada comentario |
| Historial lineal | Prohibidos los merge commits |

**No puedes aprobar tu propio PR.** GitHub lo bloquea siempre, aunque seas el
único miembro del equipo, para que nadie se auto-apruebe. Necesitas a otra
persona.

Si alguien aprueba y tú subes más commits después, **la aprobación se cae**
(así está configurado el repositorio) y hay que pedirla otra vez.

> Los `CODEOWNERS` casi no aplican aquí: el repositorio está configurado con
> `require_code_owner_reviews: false`, así que **no hace falta que revise
> ningún owner en concreto**, basta con una aprobación de cualquiera con
> acceso. Explicación completa en
> [FLUJO-DE-TRABAJO.md](./FLUJO-DE-TRABAJO.md#codeowners).

### 10. Mergea

Botón **Squash and merge**. Al hacerlo:

1. GitHub colapsa tu rama en **un solo commit** en `develop`.
2. El título del PR se convierte en el mensaje de ese commit.
3. **Tu issue se cierra solo** si usaste `Closes #N` y el PR apuntaba a
   `develop`. Si apunta a `main`, ciérralo tú.
4. La rama se borra automáticamente.
5. **No** se dispara ningún release: eso solo pasa al mergear en `main`.
6. La tarjeta del tablero **no** se mueve sola: ponla en `Done` tú.

## El estado del tablero: cuándo va *In Review*

**Nada de esto es automático, y ahí está el error más común.** El tablero no
sabe que hubo revisión. Si tú no mueves la tarjeta, se queda en *In Progress*
para siempre aunque el PR ya esté approved.

| Cuándo | Estado de la tarjeta | Quién lo mueve |
| --- | --- | --- |
| Entras a la tarea | `Todo` → `In Progress` | tú, a mano |
| Abres el PR | `In Progress` → `In Review` | tú, a mano |
| Alguien aprueba y el CI está verde | sigue en `In Review` | nadie |
| Mergeas el PR | `In Review` → `Done` | tú, a mano |

**Regla mental:** el PR pone los checks en verde y se aprueba solo. La tarjeta
del tablero **solo la mueves tú**. Ni el merge ni la aprobación tocan el status.

Y ojo con esto: **cerrar el PR no es lo mismo que cerrar la tarea.** Son dos
cosas distintas que la gente confunde todo el tiempo.

- El **PR** pasa a `MERGED` cuando lo mergeas. Eso GitHub lo hace solo.
- El **issue** pasa a `CLOSED` si usaste `Closes #N`. También solo.
- La **tarjeta** del tablero queda en `In Review` hasta que tú la muevas a
  `Done`. Nada la mueve por ti.

Por eso una tarea puede estar mergeada y seguir apareciendo como *In Review* en
el kanban. Si te pasa, no es un bug: falta mover la tarjeta.

## Los campos del issue y del tablero

Son **dos sistemas distintos** y se confunden mucho:

| | Issue Fields de la organización | Fields del Project |
| --- | --- | --- |
| Dónde se ven | En la barra lateral **del issue** | En el tablero (Kanban, Timeline, tabla) |
| Configurados | `Priority`, `Effort` | `Status`, `Start Date`, `Target Date`, `Assignees`, `Labels`, `Milestone` |
| Quién los pone | tú, en el issue | tú, en el tablero |

**Las fechas viven en dos sitios, a propósito:** en el cuerpo del issue
(`**Inicio:**` y `**Entrega:**`) y en el Project (`Start Date` / `Target Date`).
Se mantienen iguales a mano, así que si mueves una, mueve la otra.

El `Status` del Project es el único campo con valores de flujo:
`Todo` → `In Progress` → `In Review` → `Done`. Ese es el que se mueve solo
cuando te acuerdas.

## Qué se valida en tu máquina, y qué no

Esta tabla es la que hay que entender para no confiar de más en el CI:

| Regla | ¿Quién la valida? | ¿Y si no la cumples? |
| --- | --- | --- |
| Título del PR | **CI** (`pr-title`) | PR bloqueado, en rojo |
| Rama base y origen | **CI** (`pr-target`) | PR bloqueado, en rojo |
| Tests, lint, formato, build | **CI** | PR bloqueado, en rojo |
| Links de la documentación | **CI** (`link-check`) | PR bloqueado, en rojo |
| **Mensaje de commit** | **solo tu máquina** (hook) | **Pasa.** Nadie lo revisa después ⚠️ |
| **Scope del commit** | **solo tu máquina** | **Pasa.** Puedes escribir `feat(cualquiercosa):` ⚠️ |
| **Idioma del mensaje** | **nadie** | **Pasa.** El CI no lo comprueba ⚠️ |

Los hooks viven en `.husky/`:

- `pre-commit` → ejecuta `lint-staged` sobre lo que stageaste
- `commit-msg` → ejecuta `commitlint` sobre el mensaje

Se pueden saltar con `git commit --no-verify`. **No lo hagas** salvo que sepas
exactamente qué te estás saltando.

> Detalle: el hook `commit-msg` hace `cd backend` antes de correr, así que solo
> funciona si commiteas **desde la raíz del repositorio**. Si entras a
> `backend/` y commiteas desde ahí, el hook no se ejecuta.

## Problemas frecuentes

| Síntoma | Causa | Solución |
| --- | --- | --- |
| `pr-target` en rojo | La rama no empieza por `feat/ fix/ chore/ docs/` | Renombra la rama y haz `git push -u origin <nueva>` |
| `pr-title` en rojo | El título no es Conventional Commits | Edita el título en el PR, no hace falta push |
| Botón de merge gris | Falta un check, o falta aprobación | Revisa la sección *Checks* del PR |
| `link-check` en rojo | Un link roto en un `.md` | Corrige el link; en docs, rutas relativas |
| `openapi-guard` en rojo | Cambiaste un DTO sin actualizar el contrato | Lee el error: te dice qué campo se movió |
| El issue no se cerró al mergear | El enlace no se registró, o usaste `Refs` en vez de `Closes` | Ciérralo a mano. Comprueba antes la sección *Development* del issue |
| `e2e` falla en verde local | Falta un servicio en tu entorno | Levanta Docker: ver [onboarding/setup.md](./onboarding/setup.md) |
| Commits en rojo en `develop` | Falta actualizar la rama | `git switch develop && git pull`, luego `git rebase origin/develop` |

## Resumen en una tarjeta

```
ANTES
  git switch develop && git pull
  git switch -c <tipo>/issue-<n>-<kebab>      # tipo: feat fix chore docs

ANTES DE COMMITEAR
  cd backend && npm run verify && cd ..

COMMIT
  git add -A && git status && git diff --cached
  git commit -m "<tipo>(<scope>): <descripción>"

PR
  git push -u origin <rama>
  gh pr create --base develop \
    --title "<tipo>(<scope>): <descripción>" \
    --body "... Closes #<n>"

ANTES DE MERGEAR
  [ ] base = develop
  [ ] rama origen con prefijo permitido
  [ ] título conventional
  [ ] 7 checks verdes
  [ ] 1 aprobación de otra persona
  [ ] conversaciones resueltas
  [ ] Squash and merge

DESPUÉS
  [ ] issue cerrado automático (por Closes)
  [ ] rama borrada
  [ ] tarjeta del Project → Done
```

## Documentos relacionados

- [FLUJO-DE-TRABAJO.md](./FLUJO-DE-TRABAJO.md) — el panorama completo del repo
- [conventions/git-workflow.md](./conventions/git-workflow.md) — reglas de ramas
- [conventions/commits.md](./conventions/commits.md) — mensajes de commit
- [conventions/versioning.md](./conventions/versioning.md) — cómo se decide la versión
- [CONTRIBUTING.md](./CONTRIBUTING.md) — entrada rápida
