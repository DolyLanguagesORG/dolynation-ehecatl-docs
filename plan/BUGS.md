# Bugs conocidos

> Este fichero es un **indice**, no un sitio donde se abren bugs. Dice que
> bugs conocemos y **donde esta la explicacion de cada uno**: la
> explicacion vive donde vive de verdad (la issue, el PR, el commit) y no se
> duplica ni se queda vieja.
>
> **Se regenera solo**: `.github/workflows/bugs-index.yml` lo reescribe cada
> lunes y abre un PR si algo cambio. Para reportar o corregir un bug, edita
> la issue: no esta tabla.

## Como se lee

| Columna | Que significa |
| --- | --- |
| `#` | El issue, con su repo: `back#45` es `dolynation-atl-back#45`. |
| Que es | El titulo del issue. |
| Donde esta la explicacion | El enlace al issue, que es donde esta el detalle. |
| Sprint | El milestone en el que vive (si tiene). |
| Desde | Cuando se abrio. |

## Abiertos

| # | Que es | Donde esta la explicacion | Sprint | Desde |
| --- | --- | --- | --- | --- |
| `back#9` | Servicio de caché para respuestas de lectura con parámetros equivalentes (RNF-04) | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-09-28 |
| `infra#9` | Auditoría de seguridad: dependencias, secretos y protección de ramas | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/9) | Sprint 5: Calidad, integración y release v1.0.0 | 2026-10-12 |
| `back#21` | Manejo de errores, timeouts y modo degradado del proveedor IA (implementación) | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/21) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-12 |
| `back#45` | Protección contra prompt injection en generación y evaluación | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/45) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |
| `infra#25` | Test de paridad entre el schema de Drizzle y el SQL de PostgreSQL | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/25) | Sprint 5: Calidad, integración y release v1.0.0 | 2026-10-19 |
| `infra#26` | Endurecer docker-compose.prod.yml: red interna, healthchecks, proxy TLS y límites | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/26) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |

## Cerrados

| # | Que era | Donde esta la explicacion | Sprint | Desde |
| --- | --- | --- | --- | --- |
| `infra#166` | [bug] El schema nunca se aplicaba a los ambientes existentes: 500 en /auth/register y /auth/login | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/166) | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `infra#167` | [bug] Dos juegos de credenciales para la misma base: el backend no podia conectarse (503) | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/167) | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `infra#168` | [bug] El smoke test comprobaba un contrato viejo: el deploy podia salir verde con el contrato roto | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/168) | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `front#100` | [bug] El build de imagenes se colgaba 3 horas y dejaba el repositorio sin imagen publicada | [enlace](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/100) | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `back#134` | [bug] El catalogo de categorias se servia vacio: el selector de la UI nunca tenia nada que ofrecer | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/134) | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-11-16 |
| `back#168` | Login con Google permite tomar cuentas creadas por otro y los correos distinguen mayúsculas | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/168) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-11-22 |

## Hallazgos de auditoria sin issue propia

Los encontro la auditoria y no tenian issue: viven dentro del issue
de la auditoria que los detecto, con su checklist.

| # | Que es | Donde esta la explicacion | Sprint | Desde |
| --- | --- | --- | --- | --- |
| `back#45` | Protección contra prompt injection en generación y evaluación | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/45) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |
| `back#44` | Endpoint de TTS: audio corto de palabra o frase seleccionada | [enlace](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/44) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |
| `infra#26` | Endurecer docker-compose.prod.yml: red interna, healthchecks, proxy TLS y límites | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/26) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |
| `infra#25` | Test de paridad entre el schema de Drizzle y el SQL de PostgreSQL | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/25) | Sprint 5: Calidad, integración y release v1.0.0 | 2026-10-19 |
| `infra#21` | Migración S3: evaluaciones y vocabulario contextual | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) | Sprint 4: Vocabulario, TTS, evaluación y progreso | 2026-10-19 |
| `infra#20` | Migración S2: preferencias, categorías, idioma y caché de lecturas | [enlace](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) | Sprint 2: Fundamentos: autenticación, perfil y base del frontend | 2026-10-19 |

## Lo que todavia no tiene sitio

Los errores que pasan en runtime y nadie reporta: viven en `error_logs` y
`audit_logs` de la base de datos, y **no hay ningun sitio donde mirarlos**.
No es un bug conocido (nadie lo ha descrito), pero es un agujero: si un
error pasa en produccion, se descubre al mirarlo.

Cuando se defina, este apartado es el sitio: una entrada por cada error
recurrente, con su explicacion y el issue que lo corrige.

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
