# Matriz de pruebas QA (`v0.15.0`)

Bitácora de verificación funcional para la fase de pruebas en **`dev` (VPN)**
(`https://dev.dolynation.app` / `https://devplay.dolynation.app`) y
**`staging`** (`https://staging.dolynation.app` /
`https://stagingplay.dolynation.app`).

> **Cómo trabajar los hallazgos durante QA**
>
> 1. Si un caso falla, abre un issue usando la plantilla `bug.yml` **en el repo
>    donde vive la corrección** (`back`, `front`, `landing`, `infra` o `docs`).
> 2. Cita el identificador del caso (`TC-NNN`) en la descripción e indica la
>    **Severidad** y el **Entorno** (`dev (VPN)` o `staging`).
> 3. El índice [`BUGS.md`](./BUGS.md) asigna un ID estable **`BUG-NNN`** (el
>    próximo libre tras los cerrados históricos) y se actualiza cada lunes o bajo
>    demanda ejecutando `gh workflow run bugs-index.yml -R DolyLanguagesORG/dolynation-ehecatl-docs`.

## Leyenda de estado

- `Pendiente`: pendiente de validar en el ambiente indicado.
- `OK`: flujo probado extremo a extremo sin errores.
- `Parcial / Bug`: bloqueado o con defecto enlazado en [`BUGS.md`](./BUGS.md).
- `N/A`: no aplica por diseño de red o ambiente.

## Matriz de casos de prueba (`TC-001`–`TC-020`)

| ID | Flujo / Módulo | Qué probar | Dev (VPN) | Staging | Bugs |
| --- | --- | --- | --- | --- | --- |
| `TC-001` | Landing → App | Cargar portada (`dev` / `staging`), navegar a login/registro y verificar salto hacia `devplay` / `stagingplay`. | Pendiente | Pendiente | — |
| `TC-002` | Páginas legales y soporte | Abrir `/terms`, `/privacy` y `/support` en español/inglés y validar enlaces desde registro/login y pie de página. | Pendiente | Pendiente | — |
| `TC-003` | Salud y versión | Comprobar `GET /api/v1/version` (vía proxy BFF), `/version` y `GET /api/v1/health/ready` con TLS válido. | Pendiente | Pendiente | — |
| `TC-004` | Cloudflare Turnstile | Validar carga invisible (`interaction-only`) en `/login`, `/register` y `/forgot-password` y rechazo sin token válido. | Pendiente | Pendiente | — |
| `TC-005` | Rate limit por IP | Probar repetidos intentos inválidos en `/login` o `/forgot-password` y verificar bloqueo `429` controlado. | Pendiente | Pendiente | — |
| `TC-006` | Registro + Brevo SMTP | Crear cuenta con correo y contraseña y validar llegada del correo de confirmación desde `no-reply@dolynation.app` con link al dominio correcto. | Pendiente | Pendiente | — |
| `TC-007` | Login, refresh y logout | Iniciar sesión con contraseña, recargar la app (rotación silenciosa vía cookie `HttpOnly` en BFF) y cerrar sesión. | Pendiente | Pendiente | — |
| `TC-008` | Recuperar contraseña | Solicitar restablecimiento en `/forgot-password`, abrir enlace de Brevo en `/reset-password` e iniciar sesión con la nueva clave. | Pendiente | Pendiente | — |
| `TC-009` | Google OAuth | Iniciar sesión y registrarse con Google; validar redirección al callback `/api/auth/oauth/google/callback` y alta de sesión. | Pendiente | Pendiente | — |
| `TC-010` | Microsoft Entra ID OAuth | Iniciar sesión con cuenta Microsoft personal y escolar/laboral (`tenant=common`), callback `/api/auth/oauth/microsoft/callback` y alta de sesión. | Pendiente | Pendiente | — |
| `TC-011` | Bloqueo OAuth para `admin` | Intentar acceder con Google o Microsoft usando una cuenta con rol `admin` y verificar rechazo `AUTH_OAUTH_ADMIN_FORBIDDEN`. | Pendiente | Pendiente | — |
| `TC-012` | Onboarding y selección de plan | Elegir plan en `/register` (Paso `03/04`) o `/select-plan`; revisar visualización de tarjetas (`Dolly`, `Dolly Plus`, `Dolly Pro`). | Pendiente | Pendiente | [`BUG-007`](./BUGS.md#abiertos) (`front#172`) |
| `TC-013` | Preferencias e idiomas | Configurar idioma objetivo, idiomas múltiples y categorías (incluyendo categorías nuevas moderadas por IA). | Pendiente | Pendiente | — |
| `TC-014` | Generación de lectura IA | Generar lectura según idioma, nivel, longitud y categoría; comprobar guardado e historial inmediato. | Pendiente | Pendiente | — |
| `TC-015` | Diccionario contextual y glosario | Seleccionar palabra/frase dentro de una lectura, consultar explicación contextual y guardar/consultar en `/glossary`. | Pendiente | Pendiente | — |
| `TC-016` | Evaluación, racha e historial | Enviar resumen en `/readings/[id]/evaluate`, revisar resultado y comprobar actualización de racha y `/history`. | Pendiente | Pendiente | — |
| `TC-017` | Stripe Checkout (planes pagos) | Comprar `Dolly Plus` o `Dolly Pro` en `staging` con tarjeta de prueba `4242...` (`mxn`), retorno `/billing/return` y activación de suscripción. | N/A (`manual` tras VPN) | Pendiente | — |
| `TC-018` | Stripe desbloqueo de idioma | Pagar crédito único de cambio de idioma en `/profile` o `/setup-preferences` y verificar incremento de `language_change_credits`. | N/A (`manual` tras VPN) | Pendiente | — |
| `TC-019` | Portal de facturación y webhooks | Cambiar plan / cancelar / actualizar tarjeta y confirmar sincronización vía `POST /api/v1/billing/webhook` en `billing_webhook_events`. | N/A (`manual` tras VPN) | Pendiente | — |
| `TC-020` | Panel administrativo (`/admin`) | Acceder con usuario `admin`, listar usuarios, revisar solicitudes manuales, `error_logs`, `audit_logs` y trazabilidad por `requestId`. | Pendiente | Pendiente | — |

> **Nota sobre pagos en `dev`:** por diseño de red (`dev` aislado detrás de
> WireGuard + mTLS), Stripe no puede entregar webhooks entrantes a `devapi`.
> Por ello `dev` corre con `BILLING_PROVIDER=manual` y la pasarela completa de
> Stripe se prueba en `staging` (o en local con `stripe listen`). Ver
> [`../conventions/environment.md`](../conventions/environment.md#estrategia-por-ambiente-y-red-vpn--sandbox).
