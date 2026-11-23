# Bugs conocidos

> Este fichero es un **indice**, no un sitio donde se abren bugs. Dice que
> bugs conocemos, su identificador **`BUG-NNN`** y **donde esta la explicacion
> de cada uno**: la explicacion vive en la issue real de GitHub y no se
> duplica ni se queda vieja.
>
> **Se regenera solo**: `.github/workflows/bugs-index.yml` lo reescribe cada
> lunes (o bajo demanda con `workflow_dispatch`) y abre un PR si algo cambio.
> Para reportar un bug nuevo, abre la issue con la plantilla `bug.yml` en el
> repositorio correspondiente y referencia el caso de [`QA-PRUEBAS.md`](./QA-PRUEBAS.md).

## Como se lee

| Columna | Que significa |
| --- | --- |
| `ID` | Identificador unico y estable (`BUG-001`...) asignado por orden cronologico (o tomado de `[BUG-NNN]` en el titulo). |
| `Issue` | Enlace corto a la issue en su repo: [`back#134`](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/134). |
| `Severidad` | Impacto (`Crítica`, `Alta`, `Media`, `Baja`) leido del cuerpo de la plantilla. |
| `Entorno` | Ambiente reportado (`dev`, `staging`, `prod`, `local`). |
| `Que es` | Titulo de la issue. |
| `Sprint` | Milestone asignado (si tiene). |
| `Desde` | Fecha de apertura (`YYYY-MM-DD`). |

## Abiertos

| ID | Issue | Severidad | Entorno | Que es | Sprint | Desde |
| --- | --- | --- | --- | --- | --- | --- |
| `BUG-007` | [`front#172`](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/172) | Alta | dev local / staging | [bug] No se muestran los precios de los paquetes Dolly Plus y Dolly Pro en la selección de plan | — | 2026-11-23 |

## Cerrados

| ID | Issue | Severidad | Entorno | Que es | Sprint | Desde |
| --- | --- | --- | --- | --- | --- | --- |
| `BUG-001` | [`infra#166`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/166) | — | — | [bug] El schema nunca se aplicaba a los ambientes existentes: 500 en /auth/register y /auth/login | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `BUG-002` | [`infra#167`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/167) | — | — | [bug] Dos juegos de credenciales para la misma base: el backend no podia conectarse (503) | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `BUG-003` | [`infra#168`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/168) | — | — | [bug] El smoke test comprobaba un contrato viejo: el deploy podia salir verde con el contrato roto | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `BUG-004` | [`front#100`](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/100) | — | — | [bug] El build de imagenes se colgaba 3 horas y dejaba el repositorio sin imagen publicada | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `BUG-005` | [`back#134`](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/134) | — | — | [bug] El catalogo de categorias se servia vacio: el selector de la UI nunca tenia nada que ofrecer | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `BUG-006` | [`back#168`](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/168) | — | — | Login con Google permite tomar cuentas creadas por otro y los correos distinguen mayúsculas | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-11-22 |

## Hallazgos de auditoria sin issue propia

Los encontro la auditoria y no tenian issue: viven dentro del issue
de la auditoria que los detecto, con su checklist.

| # | Que es | Donde esta la explicacion | Sprint | Desde |
| --- | --- | --- | --- | --- |
| `infra#20` | Migración S2: preferencias, categorías, idioma y caché de lecturas | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-10-19 |
| `infra#21` | Migración S3: evaluaciones y vocabulario contextual | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |
| `back#44` | Endpoint de TTS: audio corto de palabra o frase seleccionada | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/44) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |
| `back#45` | Protección contra prompt injection en generación y evaluación | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/45) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |
| `infra#25` | Test de paridad entre el schema de Drizzle y el SQL de PostgreSQL | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/25) | Sprint 5: Calidad, integración y release v1.0.0 | 2026-10-19 |
| `infra#26` | Endurecer docker-compose.prod.yml: red interna, healthchecks, proxy TLS y límites | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/26) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |

## Observabilidad de errores en runtime

Los errores que ocurren en tiempo de ejecucion (HTTP 4xx/5xx y fallos de
proveedores de IA, SMTP o Stripe) se registran en las tablas `error_logs` y
`audit_logs` y pueden inspeccionarse desde el panel de administracion (`/admin`)
y los endpoints `/api/v1/admin/logs/errors`, `/api/v1/admin/logs/audit` y
`/api/v1/admin/logs/trace/:requestId`. Cuando uno revele un defecto
reproducible, abre su issue con la plantilla `bug.yml` para que reciba un
`BUG-NNN` en este indice.

## El modulo de pagos

La auditoria del modulo de pagos esta en **una sola issue con checklist**
(`back#150`), no en una issue por hallazgo: el tablero deja de servir si
cada matiz es una issue, y todos esos hallazgos viven en el mismo modulo y
se revisan con el mismo par de ojos.

### La checklist de la auditoria

Fuente: [back#150](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/150).

| # | Que es | Estado |
| --- | --- | --- |
| `A-1` | una suscripcion `incomplete`/`paused` concedia el plan pagado sin cobrar | corregido |
| `A-2` | los reembolsos (`charge.refunded` y `refund.created`) no revocaban nada | corregido |
| `A-3` | el pago asincrono (`checkout.session.async_payment_succeeded`) nunca se acreditaba | corregido |
| `A-4` | un webhook atascado en `processing` se perdia para siempre | corregido |
| `A-5` | doble cobro posible: la comprobacion era solo contra la base local. **Corregido en #148** (ahora se consulta a la pasarela) | corregido |
| `M-5` | la clave de idempotencia del checkout es **opcional**: si el cliente no la manda y el SDK reintenta tras un timeout ambiguo, se crean **dos sesiones de checkout**. Derivar una clave determinista en el servidor | pendiente |
| `M-6` | `updateSubscriptionPlan` manda `cancel_at_period_end: false`: cambiar de plan **deshace silenciosamente** una cancelacion programada. O se quita, o se documenta y se testea | pendiente |
| `M-4` | los bloqueos (`withUserLock`, `customerLocks`) son **en memoria de cada proceso**: con mas de una replica no serializan nada. Con una sola replica (la de ahora) no es un problema; si se escala, mover el cerrojo a la base (`pg_advisory_xact_lock`) o a Redis | pendiente |
| `M-9` | el webhook es publico y **sin limite de tamano de cuerpo ni de peticiones por IP**. La firma protege la autenticidad, no el volumen. Anadir `limit` al parser del cuerpo y un limite por IP | pendiente |
| `B-5` | el guard `check-no-real-keys.sh` solo escanea `src` y `test`: una `sk_live_` colada en `.github/workflows/` o en `.env.example` no se detecta. Anadir esos objetivos | pendiente |
| `B-8` | el `idempotencyKey` del cliente de Stripe es **fijo** (`doly-cust-<env>-<userId>`): si el usuario se borra y se recrea con el mismo id en 24 h, Stripe devuelve el cliente antiguo | pendiente |
| `B-6` | el registro de auditoria del credito de idioma se escribe **dentro de la transaccion** que puede revertirse: queda auditado un cambio que no ocurrio. Sacarlo fuera | pendiente |
| `B-3` | `GET /billing/invoices` usa `limit: 24` fijo, sin paginacion, y la documentacion no lo dice. Aceptar `limit`/`cursor` con tope, o documentar el tope | pendiente |
| `M-11 (a medias)` | `checkout.session.expired` ya no deja filas `pending`; faltan `invoice.payment_action_required` y `invoice.voided` | pendiente |
| `Firmas` | hay que cubrir firma valida sobre un cuerpo **distinto** al firmado, `timestamp` fuera de la tolerancia de 300 s, y `v1` con otro secreto (rotacion) | pendiente |
| `Eventos que nunca se probaron` | `invoice.payment_succeeded`, `invoice.payment_failed`, `customer.subscription.created` con `incomplete`, `charge.refunded` y `checkout.session.async_payment_succeeded` (los que se corrigieron ya tienen prueba) | pendiente |
| `Concurrencia real` | dos compras simultaneas contra Postgres de verdad (el e2e actual no abre conexiones en paralelo) | pendiente |
| `El e2e de billing es un solo `it()` gigante` | (~420 lineas): si falla una asercion a mitad, no se ejecutan las 200 siguientes y el diagnostico es pesoso. Partirlo en 8-12 `it()` independientes | pendiente |
| `Paridad del schema` | hay un issue abierto en infra (#25) para automatizar el test de paridad entre el schema de Drizzle y el SQL de PostgreSQL. Ese test habria atrapado el fallo de CI que hubo hoy. Refs #143 | pendiente |
