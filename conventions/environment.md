# Environment variables

Política de configuración por variables de entorno. La fuente de verdad es
[`.env.example`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/.env.example).

## Tabla de variables

| Variable                | Requerida | Tipo   | Default               | Descripción                                       |
| ----------------------- | --------- | ------ | --------------------- | ------------------------------------------------- |
| `NODE_ENV`              | No        | enum   | `development`         | `development` \| `production` \| `test`           |
| `PORT`                  | No        | int    | `3333`                | Puerto del servidor HTTP                          |
| `HOST`                  | No        | string | `0.0.0.0`             | Interface de bind                                 |
| `API_PREFIX`            | No        | string | `api/v1`              | Prefijo global de rutas                           |
| `APP_NAME`              | No        | string | `dolynglish-backend`  | Nombre lógico para logs                           |
| `APP_VERSION`           | No        | string | -                     | Versión ÚNICA de la aplicación. La inyecta el build de la imagen; sin ella se usa la del repo |
| `COMPONENT`             | No        | string | `dolynation-atl-back` | Qué pieza de la aplicación es este proceso        |
| `BUILT_AT`              | No        | string | -                     | Momento de la construcción del artefacto. Lo inyecta el build |
| `GIT_COMMIT`            | No        | string | `unknown`             | Commit de build. Lo inyecta el Dockerfile (ARG -> ENV) |
| `DB_HOST`               | Sí        | string | -                     | Host de PostgreSQL                                |
| `DB_PORT`               | Sí        | int    | `5432`                | Puerto de PostgreSQL                              |
| `DB_USER`               | Sí        | string | -                     | Usuario de la BD                                  |
| `DB_PASSWORD`           | Sí        | string | -                     | Password de la BD                                 |
| `DB_DATABASE`           | Sí        | string | -                     | Nombre de la base                                 |
| `DB_LOGGING`            | No        | boolean| `false`               | Logging de queries de Drizzle                     |
| `JWT_SECRET`            | Sí        | string | -                     | Secreto para firmar JWT (≥48 chars random)        |
| `JWT_ACCESS_TTL`        | No        | string | `5m`                  | TTL del access token                              |
| `JWT_REFRESH_TTL`       | No        | string | `30d`                 | TTL del refresh token                             |
| `GOOGLE_OAUTH_CLIENT_ID` | No       | string | -                     | Client ID público de Google OAuth 2.0 / OIDC      |
| `GOOGLE_OAUTH_CLIENT_SECRET` | No   | string | -                     | Client Secret privado de Google OAuth 2.0         |
| `GOOGLE_OAUTH_REDIRECT_URI` | No    | url    | `${FRONTEND_BASE_URL}/api/auth/oauth/google/callback` | URI de callback autorizada (opcional si `FRONTEND_BASE_URL` coincide) |
| `AI_DEFAULT_PROVIDER`   | No        | enum   | `minimax`             | `minimax` \| `google` (los dos registrados en la factoría) |
| `MINIMAX_API_KEY`       | Cond.*    | string | -                     | API key de MiniMax (*si provider es minimax)        |
| `MINIMAX_MODEL`         | No        | string | `MiniMax-M2.7`        | Modelo principal (con fallback a `MiniMax-M3`)    |
| `MINIMAX_ENDPOINT`      | No        | string | `https://api.minimax.io/v1/chat/completions` | URL del API |
| `MINIMAX_MAX_TOKENS`    | No        | int    | `8192`                | Límite de tokens de salida                        |
| `MINIMAX_TEMPERATURE`   | No        | float  | `0.7`                 | Temperatura de sampling                           |
| `MINIMAX_TIMEOUT_MS`    | No        | int    | `90000`               | Timeout HTTP en ms                                |
| `MINIMAX_REASONING_EFFORT` | No     | enum   | `low`                 | `minimal` \| `low` \| `medium` \| `high`         |
| `GOOGLE_API_KEY`        | Cond.**   | string | -                     | API key de Google AI Studio (*si provider es `google`; también habilita `gemini-decision-1`) |
| `GOOGLE_MODEL`          | No        | string | `gemini-3.5-flash-lite` | Modelo de Gemini                              |
| `GOOGLE_ENDPOINT`       | No        | url    | `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` | Endpoint de Gemini (compatible con OpenAI) |
| `GOOGLE_TIMEOUT_MS`     | No        | int    | `90000`               | Timeout HTTP a Google en ms                    |
| `GOOGLE_MAX_TOKENS`     | No        | int    | `8192`                | Límite de tokens de salida (Gemini)           |
| `GOOGLE_TEMPERATURE`    | No        | float  | `0.7`                 | Temperatura de sampling (Gemini)               |
| `GOOGLE_DECISIONS_MODEL` | No       | string | `gemini-decision-1`  | Modelo de la API de Decisions (moderación por compuertas) |
| `GOOGLE_DECISIONS_ENDPOINT` | No    | url    | `https://generativelanguage.googleapis.com/v1beta/decisions` | Endpoint de Decisions |
| `GOOGLE_DECISIONS_TIMEOUT_MS` | No | int | `15000`             | Timeout de la API de Decisions en ms           |
| `CATEGORY_MODERATION_ENABLED` | No   | boolean| `true`                | Activa el filtro de moderación de categorías      |
| `CATEGORY_MODERATION_AI_ENABLED` | No | boolean| `true`             | Activa la capa de IA del filtro                   |
| `CATEGORY_MODERATION_AI_PROVIDER` | No | enum | `auto`               | `auto` \| `openai` \| `google-decisions` \| `minimax` \| `google` \| `none` |
| `CATEGORY_DAILY_LIMIT`  | No        | int    | `20`                  | Tope diario de categorías distintas por usuario    |
| `CATEGORY_MODERATION_SCORE_THRESHOLD` | No | float | `0.45`            | Umbral de las APIs gratuitas de moderación        |
| `CATEGORY_MODERATION_TIMEOUT_MS` | No | int   | `15000`               | Timeout por lote de moderación/blueprint en ms    |
| `CATEGORY_MODERATION_CACHE_TTL_MS` | No | int  | `86400000`            | TTL del caché de categorías moderadas             |
| `OPENAI_API_KEY`        | No        | string | -                     | API key de OpenAI (la moderación es **gratis**)    |
| `OPENAI_MODERATION_ENDPOINT` | No  | url    | `https://api.openai.com/v1/moderations` | Endpoint de moderación        |
| `OPENAI_MODERATION_MODEL` | No      | string | `omni-moderation-latest` | Modelo de moderación de OpenAI               |
| `GROQ_API_KEY`          | No        | string | -                     | *Legacy*: hoy ningún proveedor Groq está registrado|
| `GROQ_MODEL`            | No        | string | `qwen/qwen3-32b`      | Modelo legacy                                     |
| `LOG_LEVEL`             | No        | enum   | `info`                | `trace` \| `debug` \| `info` \| `warn` \| `error` |

> \* `MINIMAX_API_KEY` es obligatoria si `AI_DEFAULT_PROVIDER=minimax`: el provider
> la necesita para cada llamada.
> \** `GOOGLE_API_KEY` es **obligatoria** si `AI_DEFAULT_PROVIDER=google`: el schema
> Zod aborta el arranque sin ella (antes la app arrancaba y fallaba en cada
> generación de lectura).
>
> La API de **Google Perspective se eliminó**: Jigsaw la apaga el 31 de diciembre
> de 2026 y el cierre de keys nuevas fue en febrero de 2026. La moderación usa
> OpenAI Moderation, Google Decisions (`gemini-decision-1`) y la IA generativa.

Las variables de TTS se definirán en `back#11`; no agregues nombres nuevos
hasta que el proveedor esté decidido.

## Política de secretos

1. **Nunca** commitear `.env` ni `.env.production`. El `.gitignore` raíz
   bloquea `*/.env` y `*/.env.production`.
2. **Generar** `JWT_SECRET` con: `openssl rand -base64 48`
3. **Rotar** secretos cada 90 días en producción (proceso manual).
4. **Diferenciar** dev / staging / prod con archivos separados:
   `.env.development`, `.env.production`, etc.

## Los mismos nombres en todos los ambientes

**El nombre de una variable es el mismo en todos los ambientes**; lo que
cambia es el **valor**.

| | local | desarrollo | rehearsal | staging | producción |
| --- | --- | --- | --- | --- | --- |
| `DB_PASSWORD` | la que sea | de prueba | de prueba | de prueba | **la real** |

Por qué:

- El código lee **un** nombre. Si el nombre cambiara por ambiente, el código
  necesitaría bifurcaciones ("si es staging lee X, si es prod lee Y"), que es
  justo donde aparecen los bugs.
- La seguridad no viene del nombre, viene de: **valores distintos** por
  ambiente, secrets **por environment** en GitHub, y `prod` con dos revisores
  y sin auto-aprobación.
- Regla de oro: **el `.env` de producción nunca se copia a staging**, ni al
  revés.

## Agregar una variable nueva: los 5 lugares

Una variable no existe en la aplicación hasta que está en **todos** estos
lugares. Si se olvida uno, el error típico es "la variable no llega" (el
secret existe en GitHub, pero la aplicación no la ve):

| # | Dónde | Qué se hace |
| --- | --- | --- |
| 1 | `atl-back`: `src/config/env.validation.ts` | se declara en el schema Zod (si es requerida, la app **no arranca** sin ella) |
| 2 | `tlalli-infra`: `docker-compose.env.yml` | se pasa al contenedor que la use |
| 3 | `tlalli-infra`: los 3 workflows `deploy-*.yml` | **la lista de variables del `.env` está escrita a mano**: si no se agrega ahí, no llega al servidor |
| 4 | `atl-back`: `.env.example` | la forma para los que trabajan en local |
| 5 | GitHub **Environments** | un valor por ambiente (`desarrollo`, `rehearsal`, `staging`, `prod`), con valores distintos |

Y el sexto paso, que es de documentación: la tabla de variables de este
archivo (`conventions/environment.md`).

**Secret o variable de GitHub.** En el paso 5 no todo es un *secret*:

| Tipo | Qué es | Cómo se referencia en el workflow |
| --- | --- | --- |
| **Secret** | credencial: API keys, contraseñas, `JWT_SECRET` | `${{ secrets.NOMBRE }}` |
| **Variable** | parámetro de configuración: `CATEGORY_DAILY_LIMIT`, `EMAIL_VERIFICATION_REQUIRED`, `GOOGLE_MODEL` | `${{ vars.NOMBRE }}` |

Una variable de GitHub que no existe se resuelve a **cadena vacía**, no a error.
Por eso el `docker-compose.env.yml` le pone un default a cada una
(`${CATEGORY_DAILY_LIMIT:-20}`): el default del compose gana cuando la
variable no llegó, y el backend nunca se queda sin valor.

> **Las keys de IA no son las mismas en todos los ambientes.** Los ambientes
> no-productivos (`desarrollo`, `rehearsal`, `staging`) comparten un juego de
> credenciales y `prod` tiene el suyo, en otro proyecto del proveedor. La
> separación se puede hacer más fina después sin tocar código: solo cambian
> los valores de los secrets.

> Si la variable es **pública** (va al navegador), lleva el prefijo
> `NEXT_PUBLIC_` y se compila en el bundle. Si es de **servidor**, **no** lleva
> ese prefijo: así no se filtra al cliente (es el caso de
> `BACKEND_INTERNAL_URL` en el frontend).

## Variables del frontend

El frontend (`dolynation-tonatiuh-front`) tiene sus propias variables, todas de
**servidor** (el navegador nunca ve la dirección del backend).

| Variable | Repo | Ambiente | Qué es |
| --- | --- | --- | --- |
| `BACKEND_INTERNAL_URL` | tonatiuh-front | los 4 | URL **interna** del backend. En los 4 ambientes es `http://backend:3333/api/v1` (por la red de compose), **nunca** un dominio público |
| `NEXT_ALLOWED_DEV_ORIGINS` | tonatiuh-front | `desarrollo` | Hosts desde los que se permite el dev server de Next. Admite comodines: `**.yacaterkos.tech` matchea cualquier subdominio (no el apex) |

### Por qué `NEXT_ALLOWED_DEV_ORIGINS` existe

Next.js 16 bloquea los recursos cross-site del dev server (`/_next/*`) cuando el
`Origin` de la petición no está en `allowedDevOrigins`, y **el websocket de HMR**
(`/_next/hmr`) entra en esa regla.

El rechazo de Next **no es una respuesta HTTP válida**: escribe `"Unauthorized"`
crudo en el socket, sin línea de estado ni cabeceras. El proxy de Cloudflare lo
interpreta como una respuesta inválida y devuelve **520**, que el navegador
reporta como:

```
WebSocket connection to 'wss://devweb.yacaterkos.tech/_next/hmr' failed
```

Sin esta variable, **el HMR no funciona** en desarrollo (el sitio carga, pero
hay que recargar a mano para ver los cambios).

> Solo aplica al **dev server**. En `rehearsal`, `staging` y `prod` la app corre
> compilada (`output: 'standalone'` → `node server.js`): sin HMR, sin websocket.

## Cambiar el dominio público

El **frontend nunca conoce el dominio público**: su `BACKEND_INTERNAL_URL` es
interno en los 4 ambientes. El dominio aparece en **3 lugares**, y solo 2 son
código:

| # | Dónde | Qué cambia | ¿Requiere código? |
| --- | --- | --- | --- |
| 1 | `tlalli-infra/nginx/dolynation.conf` → `server_name` | el ruteo de `devweb` / `devapi` / `stagingweb` | **Sí** |
| 2 | `NEXT_ALLOWED_DEV_ORIGINS` (variable del front, env `desarrollo`) | el HMR de desarrollo | **No** |
| 3 | `FRONTEND_BASE_URL` (variable del backend, por ambiente) | los enlaces de los correos transaccionales | **No** |

Procedimiento completo:

1. **DNS / Cloudflare** → apuntar el host nuevo al servidor (y emitir el
   certificado de origen si hace falta).
2. **`tlalli-infra`**: `nginx/dolynation.conf` → `server_name` del host nuevo
   (y `upstream` si cambian los puertos). Un PR a `develop` y el deploy.
3. **`NEXT_ALLOWED_DEV_ORIGINS`** del environment `desarrollo` del front →
   el patrón del dominio nuevo. Sin código: redeploy del front.
4. **`FRONTEND_BASE_URL`** del environment correspondiente del backend → la URL
   pública nueva. Sin código: redeploy del backend.

### `rehearsal` no tiene dominio

`rehearsal` **no sale a internet**: no tiene `server_name` en el nginx y se
accede por puerto (`5704x`) desde el propio servidor. Por eso su
`FRONTEND_BASE_URL` **replica el de producción**: rehearsal existe para probar
el tren de release completo, así que debe ensayar la configuración de
producción.

## Variables de correo (SMTP)
Para enviar correo, el backend necesita estas variables (todas **de
servidor**: nunca al frontend):

| Variable | Requerida | Descripción |
| --- | --- | --- |
| `SMTP_HOST` | No | Host del servidor SMTP |
| `SMTP_PORT` | No | Puerto (587 con STARTTLS, 465 con TLS implícito) |
| `SMTP_USER` | No | Usuario de la cuenta |
| `SMTP_PASSWORD` | No | Clave SMTP de la cuenta |
| `SMTP_FROM` | No | Remitente (`Nombre <correo@dominio>`) |
| `SMTP_FROM_NAME` | No | Nombre del remitente, si se quiere separado |
| `SMTP_SECURE` | No | `true` solo si el cifrado es implícito (465) |
| `FRONTEND_BASE_URL` | No | URL pública del frontend para construir los enlaces de los correos (default `http://localhost:3000`) |
| `EMAIL_VERIFICATION_REQUIRED` | No | `true` para exigir correo confirmado al registrarse / iniciar sesión (default `false`) |

**Son opcionales a propósito**: si fueran obligatorias, un ambiente sin
SMTP no arrancaría. El servicio de correo falla con un mensaje claro
("falta SMTP_HOST/SMTP_USER") cuando se usa sin configurar.

### El servidor de correo que hay hoy

| | Valor |
| --- | --- |
| Host | `smtp-relay.brevo.com` |
| Puerto | `587` (STARTTLS) |
| Usuario | la cuenta del ambiente |
| Clave | **una distinta por ambiente**, en los GitHub Environments |

Los valores de cada ambiente los pone el scrum master como secrets del
Environment correspondiente: el deploy escribe el `.env` del servidor con
ellos, así que **nadie tiene que saber el servidor de correo de ningún
ambiente para trabajar en su código**. En local, cada quien usa los suyos o
un catcher local (Mailpit/MailHog).

Detalle en la issue del backend (SMTP) y en
[`operations/FLUJO-DE-RELEASE.md`](../operations/FLUJO-DE-RELEASE.md).

En local no hace falta una clave real: se puede levantar un *catch-all*
(Mailpit/MailHog) y ver el correo en el navegador.

## Validación

Las variables se validan al arrancar con un schema Zod en
[`src/config/env.validation.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/config/env.validation.ts).
Si falta una variable requerida o tiene un valor inválido, la app **no
arranca** y muestra el error exacto.

## Pagos y facturación (Stripe Sandbox / manual)

| Variable | Default | Cuándo es obligatoria / propósito |
| --- | --- | --- |
| `BILLING_PROVIDER` | `manual` | `manual` mantiene el flujo local/CI sin pasarela externa; `stripe` activa checkout, sincronización y webhooks. |
| `BILLING_ENV_TAG` | `local` | Aísla eventos (`local`, `dev`, `rehearsal`, `staging`, `prod`) cuando varios ambientes no productivos comparten una misma clave Stripe Sandbox (`metadata.env`). |
| `STRIPE_SECRET_KEY` | — | Obligatoria si `BILLING_PROVIDER=stripe` (`sk_test_...` en Sandbox). Nunca en el frontend. |
| `STRIPE_PUBLISHABLE_KEY` | — | Obligatoria si `BILLING_PROVIDER=stripe` (`pk_test_...`). Expuesta en `GET /api/v1/billing/config`. |
| `STRIPE_WEBHOOK_SECRET` | — | Obligatoria si `BILLING_PROVIDER=stripe` (`whsec_...`). Firma HMAC para `POST /api/v1/billing/webhook`. |
| `STRIPE_CURRENCY` | `mxn` | Código ISO 4217 normalizado a minúsculas. |
| `STRIPE_CHECKOUT_UI_MODE` | `custom` | `custom` usa Stripe `<PaymentElement>` + Appearance API dentro de la UI B&W de DolyNation; `hosted` funciona como respaldo hacia Stripe Checkout alojado. |
| `STRIPE_PRICE_DOLLY` | — | Opcional. Dejar vacía mientras `dolly` permanezca gratuito (`$0`). |
| `STRIPE_PRICE_DOLLY_PLUS` | — | Obligatoria si `BILLING_PROVIDER=stripe` (`price_...` recurrente mensual en MXN). |
| `STRIPE_PRICE_DOLLY_PRO` | — | Obligatoria si `BILLING_PROVIDER=stripe` (`price_...` recurrente mensual en MXN). |
| `STRIPE_PRICE_LANGUAGE_UNLOCK` | — | Obligatoria si `BILLING_PROVIDER=stripe` (`price_...` pago único `+1` crédito de cambio de idioma). |

### Estrategia por ambiente y red (VPN + Sandbox)

- **Sandbox global por ahora:** todos los entornos (incluido `prod` mientras opere en beta) usan Test Mode / Sandbox de Stripe; pasar a Live Mode solo requiere sustituir secretos y Price IDs en el Environment de GitHub correspondiente.
- **`dev` tras VPN WireGuard + mTLS:** el tráfico saliente (`dev → api.stripe.com`, IA, SMTP) funciona normalmente, pero **los webhooks entrantes de Stripe (`POST /api/v1/billing/webhook`) no pueden alcanzar un `dev` privado tras VPN**. Por ello `BILLING_PROVIDER=manual` es el valor por defecto en CI, `rehearsal` y `dev`.
- **Pruebas locales con webhooks reales:** usar `stripe listen --forward-to http://localhost:3333/api/v1/billing/webhook` (sin abrir puertos ni exponer DNS público).
- **`staging`:** Nginx enruta `location = /api/v1/billing/webhook` directo al backend (sin pasar por el BFF de Next.js), validando la firma criptográfica `stripe-signature` con `rawBody: true` en lugar de depender de listas de IPs detrás de Cloudflare.

## Autenticación externa OAuth 2.0 / OIDC (Google)

| Variable | Tipo en GitHub | Default | Propósito |
| --- | --- | --- | --- |
| `GOOGLE_OAUTH_CLIENT_ID` | `vars` | — | Client ID de Google OAuth 2.0 (Web Application). Si falta junto con el secret, Google Sign-In permanece oculto y deshabilitado. |
| `GOOGLE_OAUTH_CLIENT_SECRET` | `secrets` | — | Client Secret de Google OAuth 2.0 (solo vive en el backend). |
| `GOOGLE_OAUTH_REDIRECT_URI` | `vars` | `${FRONTEND_BASE_URL}/api/auth/oauth/google/callback` | URI exacta registrada en Google Cloud Console. Si se omite, el backend la deriva automáticamente de `FRONTEND_BASE_URL`. |

### Estrategia por ambiente, VPN y seguridad

- **Dos juegos de credenciales en Google Cloud (presupuesto $0):**
  - **No-productivo (`local`, `desarrollo`, `staging`):** comparten un OAuth Client en modo *Testing* con múltiples *Authorized redirect URIs* (`http://localhost:3000/api/auth/oauth/google/callback`, `https://devweb.yacaterkos.tech/api/auth/oauth/google/callback`, `https://stagingweb.yacaterkos.tech/api/auth/oauth/google/callback`).
  - **Producción (`prod`):** usa un OAuth Client independiente para `https://yacaterkos.tech/api/auth/oauth/google/callback`. `rehearsal` deja las variables vacías para no depender de dominio público en sus smoke tests.
- **Compatibilidad con `desarrollo` tras VPN WireGuard + mTLS:** a diferencia de los webhooks entrantes de Stripe, Google OAuth funciona en `desarrollo` porque la redirección de callback pasa por el navegador del usuario (conectado por VPN) y el intercambio `code → token` + JWKS es tráfico saliente desde el backend.
- **Imagen inmutable del frontend:** el frontend (`tonatiuh-front`) nunca compila el Client ID en `NEXT_PUBLIC_*`; consulta en runtime `GET /api/v1/auth/oauth/providers` y ejecuta el flujo PKCE a través de sus Route Handlers BFF (`/api/auth/oauth/[provider]` y `/callback`).
- **Bloqueo de cuentas `admin`:** el acceso y la auto-vinculación vía OAuth están bloqueados para cuentas con rol `admin` (`AUTH_OAUTH_ADMIN_FORBIDDEN`); los administradores siguen autenticándose exclusivamente con correo y contraseña.
- **Extensible a Microsoft Entra ID:** la tabla `user_oauth_accounts` y los adaptadores del backend permiten incorporar otros proveedores OIDC sin cambios de esquema.

## Cómo arrancar en local

```bash
# En el repo del backend (dolynation-atl-back):
cp .env.example .env
# Editar .env y rellenar DB_PASSWORD, JWT_SECRET, MINIMAX_API_KEY, etc.
```

Para la BD de desarrollo, se usa el
[`docker-compose.test.yml`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/blob/develop/docker-compose.test.yml)
del repo de infraestructura:

```bash
git clone https://github.com/DolyLanguagesORG/dolynation-tlalli-infra.git
cd dolynation-tlalli-infra
docker compose -f docker-compose.test.yml up -d
```

El schema se aplica automáticamente al primer arranque del contenedor.