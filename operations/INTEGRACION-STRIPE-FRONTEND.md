# Integración de Stripe en el Frontend (UI DolyNation Blanco y Negro)

Guía de contrato e integración entre `dolynation-tonatiuh-front` (Next.js 16) y el módulo `billing` de `dolynation-atl-back` (`back#143`), diseñada para ofrecer checkout, gestión de suscripción, actualización de método de pago y consulta de facturas **100 % dentro de la interfaz editorial Blanco y Negro de DolyNation** sin redirigir visualmente al diseño genérico de Stripe.

> Toda respuesta HTTP sigue el envelope estándar definido en [`../conventions/api-contracts.md`](../conventions/api-contracts.md): `{ message, data, error? }`.

---

## 1. Descubrimiento de configuración y modo activo

Antes de renderizar precios o botones de checkout, el frontend consulta el endpoint público:

```http
GET /api/v1/billing/config
```

No requiere token de sesión. Devuelve `BillingConfigResponseDto`:

```json
{
  "message": "Billing configuration",
  "data": {
    "provider": "stripe",
    "publishableKey": "pk_test_...",
    "currency": "mxn",
    "uiMode": "custom",
    "plans": [
      {
        "tier": "dolly",
        "isFree": true,
        "checkoutRequired": false,
        "amountCents": 0,
        "currency": "mxn",
        "interval": null
      },
      {
        "tier": "dolly_plus",
        "isFree": false,
        "checkoutRequired": true,
        "amountCents": 14900,
        "currency": "mxn",
        "interval": "month"
      },
      {
        "tier": "dolly_pro",
        "isFree": false,
        "checkoutRequired": true,
        "amountCents": 24900,
        "currency": "mxn",
        "interval": "month"
      }
    ],
    "languageUnlock": {
      "checkoutRequired": true,
      "amountCents": 4900,
      "currency": "mxn"
    }
  }
}
```

### Comportamiento según `provider`

| Valor de `provider` | Planes de pago (`dolly_plus`, `dolly_pro`) y desbloqueo de idioma | Plan `dolly` ($0) |
| --- | --- | --- |
| `manual` | Conserva activación directa vía `POST /api/v1/user/subscription` y `POST /api/v1/settings/languages/unlock-change` (salvo si `ACCESS_REQUESTS_ENABLED=true`, en cuyo caso responde `402 ACCESS_REQUEST_REQUIRED`). | Activación directa vía `POST /api/v1/user/subscription`. |
| `stripe` | `POST /api/v1/user/subscription` (con tier de pago) y `POST /api/v1/settings/languages/unlock-change` devuelven **`402 BILLING_PAYMENT_REQUIRED`**. El frontend debe usar `/api/v1/billing/*`. | Sigue siendo gratuito (`$0`) y activable directo sin Stripe, **salvo** si el usuario ya tiene una suscripción Stripe activa (`409 BILLING_SUBSCRIPTION_CONFLICT`). |

---

## 2. Catálogo completo de endpoints (`/api/v1/billing/*`)

| Método y ruta | Auth / Guard | Request DTO | Respuesta `data` | Uso principal en frontend |
| --- | --- | --- | --- | --- |
| `GET /api/v1/billing/config` | `@Public()` | — | `BillingConfigResponseDto` | Detectar `provider`, `publishableKey`, `uiMode` y precios en centavos (`amountCents`). |
| `POST /api/v1/billing/checkout/subscription` | Bearer + `@AllowWithoutSubscription()` | `{ tier: 'dolly_plus' \| 'dolly_pro', uiMode?: 'custom' \| 'hosted' }` | `CheckoutSessionResponseDto` | Iniciar checkout de suscripción pagada (devuelve `clientSecret` en modo `custom`). |
| `POST /api/v1/billing/checkout/language-unlock` | Bearer + suscripción activa | `{ uiMode?: 'custom' \| 'hosted' }` | `CheckoutSessionResponseDto` | Comprar `+1` crédito de cambio de idioma antes de cumplir 365 días. |
| `POST /api/v1/billing/checkout/:sessionId/sync` | Bearer + `@AllowWithoutSubscription()` | Param `:sessionId` | `BillingStatusResponseDto` | Reconciliar de forma síncrona e idempotente al volver del flujo 3DS/OXXO/SPEI o Checkout. |
| `GET /api/v1/billing/status` | Bearer + `@AllowWithoutSubscription()` | — | `BillingStatusResponseDto` | Consultar estado actual (`tier`, `subscription`, tarjeta predeterminada y últimos 10 pagos). |
| `POST /api/v1/billing/subscription/change-plan` | Bearer + suscripción activa | `{ tier: 'dolly_plus' \| 'dolly_pro' }` | `BillingStatusResponseDto` | Upgrade/downgrade in-app entre planes pagados con prorrateo en Stripe. |
| `POST /api/v1/billing/subscription/cancel` | Bearer + suscripción activa | — | `BillingStatusResponseDto` | Programar cancelación al final del ciclo (`cancelAtPeriodEnd = true`). |
| `POST /api/v1/billing/subscription/resume` | Bearer + suscripción activa | — | `BillingStatusResponseDto` | Revertir cancelación programada antes del cierre del periodo. |
| `POST /api/v1/billing/payment-method/setup-intent` | Bearer + suscripción activa | — | `SetupIntentResponseDto` | Obtener `clientSecret` para capturar/actualizar tarjeta in-app con `<PaymentElement>`. |
| `POST /api/v1/billing/payment-method/default` | Bearer + suscripción activa | `{ paymentMethodId: string }` | `BillingPaymentMethodSummaryDto` | Fijar la nueva tarjeta confirmada como método predeterminado para renovaciones. |
| `GET /api/v1/billing/invoices` | Bearer + suscripción activa | — | `BillingInvoiceDto[]` | Mostrar historial de facturas dentro del perfil con enlaces a `invoicePdfUrl`. |
| `POST /api/v1/billing/portal` | Bearer + suscripción activa | — | `{ url: string }` | Respaldo opcional para abrir Customer Portal alojado en Stripe. |
| `POST /api/v1/billing/webhook` | `@Public()` + header `stripe-signature` | Raw JSON body de Stripe | `{ received: boolean, ignored: boolean }` | Uso exclusivo servidor Stripe ↔ Backend (el frontend nunca lo invoca). |

### Protecciones de dinero, idempotencia y límites de tasa (`429`)

1. **Límites de tasa por usuario (`BILLING_RATE_LIMITED` 429):** los endpoints monetarios protegen contra doble clic, card-testing y abuso en ventana deslizante de **60 segundos** por usuario autenticado (complementando el futuro soporte de **reCAPTCHA** en frontend):
   - `checkout/subscription` y `checkout/language-unlock`: **5 peticiones / 60 s** (`checkout`)
   - `payment-method/setup-intent`: **5 peticiones / 60 s** (`setup_intent`)
   - `subscription/change-plan`, `subscription/cancel`, `subscription/resume`, `payment-method/default`, `portal`: **10 peticiones / 60 s** (`mutation`)
   - `checkout/:sessionId/sync`: **15 peticiones / 60 s** (`sync`)
   - `invoices`: **20 peticiones / 60 s** (`invoices`)
   - `GET /billing/config` usa caché de 5 min con coalescencia in-flight; `POST /billing/webhook` no se limita por usuario y se protege por firma HMAC `stripe-signature` + PK `billing_webhook_events`.
2. **Cabecera opcional `Idempotency-Key`:** los `POST` `checkout/subscription`, `checkout/language-unlock`, `subscription/change-plan` y `payment-method/setup-intent` aceptan `Idempotency-Key` (`1–128` caracteres `[A-Za-z0-9._:-]`), aislada automáticamente por ambiente y usuario antes de enviarse a Stripe.
3. **Prorrateo seguro y webhooks tardíos:** `change-plan` envía `payment_behavior: 'pending_if_incomplete'` y bloquea cambios si la suscripción está en `past_due` (`402 BILLING_PAYMENT_REQUIRED`); además, `syncSubscriptionState` ignora webhooks `canceled`/`unpaid` tardíos de suscripciones antiguas si existe otra suscripción activa vigente.

### Estructuras DTO clave

- **`CheckoutSessionResponseDto`**:
  `{ sessionId, clientSecret, url, publishableKey, uiMode, tier }`
- **`SetupIntentResponseDto`**:
  `{ setupIntentId, clientSecret, publishableKey }`
- **`BillingStatusResponseDto`**:
  `{ provider, tier, subscription, recentPayments }`, donde `subscription` incluye `{ status, tier, currentPeriodStart, currentPeriodEnd, cancelAtPeriodEnd, canceledAt, paymentMethod: { brand, last4, expMonth, expYear } | null }`.
- **`BillingInvoiceDto`**:
  `{ id, number, status, amountPaidCents, amountDueCents, currency, createdAt, invoicePdfUrl, hostedInvoiceUrl }`.

---

## 3. UI 100 % DolyNation B&W con `<PaymentElement>` y Appearance API

Para cumplir con **PCI-DSS SAQ A**, los datos crudos de tarjeta (PAN, CVC, fecha de vencimiento) **nunca** pasan por inputs HTML propios ni por el servidor de Next.js/NestJS. Todo campo sensible vive dentro del iframe seguro de Stripe Elements, pero estilizado al 100 % con la paleta monocromática editorial definida en el prototipo de Figma ([`./PROTOTIPO-FIGMA.md`](./PROTOTIPO-FIGMA.md)):

### Dependencias recomendadas en `dolynation-tonatiuh-front`

```bash
npm install @stripe/stripe-js @stripe/react-stripe-js
```

### Mapa de tokens DolyNation → Stripe `Appearance`

| Token en `globals.css` | Valor | Propiedad Stripe `appearance` |
| --- | --- | --- |
| `--background` | `#fafafa` | `variables.colorBackground` / superficies secundarias |
| `--surface` | `#ffffff` | Fondo de inputs (`.Input`) |
| `--foreground` | `#0a0a0a` | `variables.colorText` |
| `--ink` | `#000000` | `variables.colorPrimary` y borde activo en foco |
| `--subtle` | `#737373` | `variables.colorTextPlaceholder` |
| `--border` / `--border-strong` | `#e5e5e5` / `#d4d4d4` | Bordes `1px solid` en inputs y pestañas |
| `--status-error` | `#b91c1c` | `variables.colorDanger` |
| `--radius` / `--radius-xs` | `4px` / `2px` | `variables.borderRadius` (geometría editorial recta) |
| `--font-geist-sans` | `Geist, sans-serif` | `variables.fontFamily` |

```ts
import type { Appearance } from '@stripe/stripe-js';

export const dolyStripeAppearance: Appearance = {
  theme: 'flat',
  variables: {
    colorPrimary: '#000000',
    colorBackground: '#ffffff',
    colorText: '#0a0a0a',
    colorTextSecondary: '#525252',
    colorTextPlaceholder: '#737373',
    colorDanger: '#b91c1c',
    fontFamily: 'var(--font-geist-sans), system-ui, sans-serif',
    borderRadius: '2px',
    spacingUnit: '4px',
  },
  rules: {
    '.Input': {
      border: '1px solid #d4d4d4',
      boxShadow: 'none',
      backgroundColor: '#ffffff',
      color: '#0a0a0a',
    },
    '.Input:focus': {
      border: '1px solid #000000',
      boxShadow: '0 0 0 1px #000000',
    },
    '.Label': {
      color: '#0a0a0a',
      fontWeight: '600',
      fontSize: '13px',
    },
    '.Tab': {
      border: '1px solid #e5e5e5',
      backgroundColor: '#fafafa',
    },
    '.Tab--selected': {
      border: '1px solid #000000',
      backgroundColor: '#ffffff',
      color: '#000000',
    },
  },
};
```

> **Limitación técnica de Stripe:** los logotipos mínimos de redes de tarjeta/OXXO o el badge obligatorio en métodos redirect los renderiza Stripe dentro del iframe por requisitos normativos; todo el contenedor, resumen del pedido, botones de acción (`#000000` con texto `#ffffff`), alertas y pantallas de éxito pertenecen al 100 % a los componentes de DolyNation.

---

## 4. Flujos recomendados en el frontend

### 4.1. Nueva suscripción pagada o desbloqueo de idioma (Checkout `custom`)

1. Consultar `GET /api/v1/billing/config` al montar la vista de precios o modal de desbloqueo.
2. Si el usuario elige **`dolly`** ($0), llamar directamente a `POST /api/v1/user/subscription` con `{ tier: 'dolly' }` y continuar al onboarding/perfil sin tocar Stripe.
3. Si elige **`dolly_plus`**, **`dolly_pro`** o **`language_unlock`**:
   - Invocar `POST /api/v1/billing/checkout/subscription` (o `/checkout/language-unlock`).
   - Con `publishableKey`, `clientSecret` (`uiMode === 'custom'`) y `dolyStripeAppearance`, inicializar el Checkout custom de Stripe Elements dentro de un diálogo o página `/checkout` de DolyNation con `<PaymentElement />`.
   - Si el backend responde `uiMode === 'hosted'` y `url !== null` (fallback operativo por env), redirigir a `url`.
4. Al completar la confirmación o volver desde 3DS/OXXO/SPEI a `/billing/return?session_id={CHECKOUT_SESSION_ID}`:
   - Invocar inmediatamente `POST /api/v1/billing/checkout/:sessionId/sync`.
   - Aunque el webhook llegue milisegundos antes o después, el backend reclama la operación transaccionalmente (`billing_webhook_events` + `billing_payments.fulfilled_at`), evitando doble crédito o estados desfasados.
   - Si `:sessionId/sync` devuelve **`402 BILLING_PAYMENT_REQUIRED`** (por ejemplo en voucher OXXO pendiente de pago en tienda), mostrar estado «Pago pendiente de confirmación» y consultar periódicamente `GET /api/v1/billing/status` o `GET /api/v1/settings/languages`.

### 4.2. Gestión de suscripción y tarjeta dentro del perfil (`/profile#subscription`)

- **Mostrar estado:** `GET /api/v1/billing/status` entrega plan vigente, fecha de corte (`currentPeriodEnd`), bandera `cancelAtPeriodEnd` y últimos 4 dígitos (`paymentMethod`).
- **Cambiar entre `dolly_plus` y `dolly_pro`:** `POST /api/v1/billing/subscription/change-plan` sin abandonar la app (aplica prorrateo automático en Stripe).
- **Cancelar / Reanudar:** `POST /api/v1/billing/subscription/cancel` marca cancelación al cierre del ciclo (`cancelAtPeriodEnd = true`); mientras no venza el periodo el usuario conserva sus beneficios y puede revertirlo con `POST /api/v1/billing/subscription/resume`.
- **Degradación automática al vencer:** cuando Stripe emite `customer.subscription.deleted`, el backend baja al usuario automáticamente al plan gratuito **`dolly`**, **conservando intacto el orden prioritario de `user_settings.selected_languages`** (solo limita `active` a 1 idioma y respeta el candado anual de 365 días).
- **Cambiar tarjeta sin salir de DolyNation:**
  1. `POST /api/v1/billing/payment-method/setup-intent` → obtiene `clientSecret`.
  2. Montar `<Elements stripe={stripePromise} options={{ clientSecret, appearance: dolyStripeAppearance }}>` con `<PaymentElement />` y ejecutar `stripe.confirmSetup({ elements, redirect: 'if_required' })`.
  3. Enviar `setupIntent.payment_method` a `POST /api/v1/billing/payment-method/default`.
- **Historial de facturas:** `GET /api/v1/billing/invoices` para listar recibos y botón de descarga PDF (`invoicePdfUrl`).

---

## 5. Manejo de errores en UI (`ErrorCode`)

| Código (`error.code`) | HTTP | Cuándo ocurre y qué debe hacer el frontend |
| --- | --- | --- |
| `BILLING_PAYMENT_REQUIRED` | 402 | Se intentó activar `dolly_plus`/`dolly_pro`, cambiar de plan sin suscripción activa o desbloquear idioma directo cuando `provider === 'stripe'`, o el pago sigue pendiente en `/sync`. Abrir flujo `/billing/checkout/*` o mostrar aviso de pago pendiente. |
| `BILLING_CHECKOUT_INVALID` | 400 | `sessionId` vacío o perteneciente a otro `BILLING_ENV_TAG`. Mostrar mensaje genérico editorial y reiniciar checkout. |
| `BILLING_SUBSCRIPTION_CONFLICT` | 409 | Ya existe una suscripción Stripe activa y el usuario intentó crear un checkout duplicado o bajar directo a `dolly` vía `/user/subscription`. Redirigir a `change-plan` o `cancel`. |
| `BILLING_PROVIDER_ERROR` | 502 | Falla temporal comunicándose con `api.stripe.com`. Permitir reintento manual sin duplicar cargos. |
| `BILLING_NOT_CONFIGURED` | 503 | Ambiente configurado con `BILLING_PROVIDER=manual` o sin credenciales/Price IDs completos. Ocultar formularios Stripe o usar flujo manual. |
| `BILLING_RATE_LIMITED` | 429 | Límite de peticiones en ventana de 60 s superado (`details.retryAfterSeconds`). Deshabilitar botón temporalmente y respetar espera antes de reintentar. |
| `SUBSCRIPTION_INVALID_TIER` | 400 | Se envió `dolly` a `/checkout/subscription` o un identificador desconocido. |
| `LANGUAGE_CHANGE_LOCKED` | 403 | El usuario intentó cambiar idiomas antes de cumplir 365 días y sin créditos (`languageChangeCredits === 0`). Ofrecer botón que invoca `POST /api/v1/billing/checkout/language-unlock`. |

## 6. Notas operativas de Sandbox y entorno local

- **No mezclar claves API y Price IDs entre cuentas/sandboxes de Stripe:** los prefijos/sufijos de `STRIPE_PUBLISHABLE_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_PRICE_*` y `stripe listen` deben pertenecer exactamente a la misma cuenta o Sandbox (`livemode: false`), o Stripe responderá `No such price` (`400 BILLING_CHECKOUT_INVALID`).
- **Stripe CLI `1.55+`:** `stripe listen` requiere indicar eventos explícitos (`--events checkout.session.completed,customer.subscription.created,customer.subscription.updated,customer.subscription.deleted,invoice.payment_succeeded,invoice.payment_failed` o `--all-snapshot`).
- **Suites E2E con `.env` local en modo `stripe`:** las suites heredadas manuales (`subscription-language-flows` y `access-requests`) fijan explícitamente `BILLING_PROVIDER=manual` en `beforeAll` para no fallar cuando el desarrollador tiene `BILLING_PROVIDER=stripe` en su `.env` local.

Referencias relacionadas: [`../conventions/environment.md`](../conventions/environment.md), [`../conventions/api-contracts.md`](../conventions/api-contracts.md), [`../architecture/data-model.md`](../architecture/data-model.md) y [`./PLAN-DE-DESPLIEGUE.md`](./PLAN-DE-DESPLIEGUE.md).
