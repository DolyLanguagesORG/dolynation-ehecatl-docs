# Security

Reglas de seguridad del backend. Toda decisión de seguridad vive en el
código y se valida con tests automatizados.

## Authentication

### Hashing de passwords

**Argon2id** vía la librería `argon2` (^0.41). Configuración por defecto
de la librería es suficiente para nuestro nivel de tráfico.

**No** usar bcrypt, scrypt ni SHA-256 nativo.

### JWT (JSON Web Tokens)

- **Algoritmo**: HS256 con `JWT_SECRET` (≥48 caracteres random).
- **Access token TTL**: `15m` (default, configurable vía `JWT_ACCESS_TTL`).
- **Refresh token TTL**: `30d` (configurable vía `JWT_REFRESH_TTL`).
- **Storage en cliente**: access token en memoria/contexto; refresh en almacenamiento seguro del cliente. No usar `localStorage` para tokens.
- **Refresh tokens persistidos** en `auth_access_tokens` con hash SHA-256, **nunca en claro**, rotados en cookie `HttpOnly` desde el BFF de Next.js.
- **OAuth 2.0 / OIDC (Google y Microsoft Entra ID):** flujo PKCE `S256` manejado en las rutas BFF del frontend (`/api/auth/oauth/[provider]`) y verificación JWKS en el backend. Las cuentas con rol `admin` tienen bloqueado el acceso y la auto-vinculación vía OAuth (`AUTH_OAUTH_ADMIN_FORBIDDEN`) y se autentican únicamente con correo y contraseña.

### Decoradores

- `@Public()` — marca una ruta como pública, saltando el `JwtAuthGuard`.
  En [`src/common/decorators/public.decorator.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/common/decorators/public.decorator.ts).
- `@AllowWithoutSubscription()` — permite acceso autenticado aunque la cuenta aún no elija plan (onboarding, perfil y facturación).
- `@CurrentUser()` — inyecta el `User` autenticado en el controller. En
  [`src/common/decorators/current-user.decorator.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/common/decorators/current-user.decorator.ts).
- `@RequireCaptcha()` y `@RateLimitByIp()` — aplican verificación Cloudflare Turnstile y límite por IP en rutas públicas sensibles.

### Guards

`CommonModule` registra cuatro guards globales en orden estricto (`JwtAuthGuard` → `SubscriptionGuard` → `IpRateLimitGuard` → `CaptchaGuard`), complementados por `AdminGuard` en rutas `/admin/*`.

## Protección anti-bot y límite por IP

- **Cloudflare Turnstile** (`CaptchaGuard` en `src/modules/security/`): se ejecuta después de `JwtAuthGuard` para evitar quemar tokens ante respuestas `401`. Valida `CAPTCHA_ALLOWED_HOSTNAMES` (en producción/staging/dev) y exige token cuando `CAPTCHA_PROVIDER=turnstile`.
- **Rate limiting por IP** (`IpRateLimitGuard`): limita ráfagas por IP real en endpoints sensibles (`login`, `register`, `forgot-password`, `access_request`), configurable con `IP_RATE_LIMIT_ENABLED`.

## Validación de input

`ValidationPipe` global en
[`src/main.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/main.ts) con:

- `whitelist: true` — strip propiedades no declaradas en DTOs.
- `forbidNonWhitelisted: true` — rechaza requests con props extra.
- `transform: true` — convierte tipos (query params a números, etc.).
- `transformOptions: { enableImplicitConversion: true }`.

Cada DTO usa `class-validator` (`@IsString()`, `@IsEmail()`, etc.).

## Headers y CORS

### Helmet

Configurado en [`src/main.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/main.ts) con
Content Security Policy estricto. **Excepción importante**: `script-src`
permite `https://cdn.jsdelivr.net` porque Scalar API Reference carga su
JS bundle desde ahí.

Si añades una nueva dependencia externa que requiere ser permitida en
CSP, justifícalo en el PR.

### CORS

`CORS_ALLOWED_ORIGINS` (lista separada por comas) restringe los orígenes
permitidos en `desarrollo`, `staging` y `prod` con `credentials: true`. Si la
variable queda vacía en desarrollo local, hace fallback a `origin: true`.

## Logging y observabilidad

- `nestjs-pino` para logs estructurados JSON (en dev con `pino-pretty`) y
  `LoggingInterceptor` en `src/common/interceptors/logging.interceptor.ts`.
- **Bitácoras persistidas en PostgreSQL:** `audit_logs` y `error_logs`,
  consultables desde el panel `/admin` (`/api/v1/admin/logs/audit`,
  `/api/v1/admin/logs/errors` y `/api/v1/admin/logs/trace/:requestId`).

**No loggear** passwords, tokens, secretos ni datos personales (PII) en claro.

## Manejo de errores

El [`AllExceptionsFilter`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/common/errors/all-exceptions.filter.ts)
garantiza:

1. `INTERNAL_ERROR` (500) **nunca** expone el mensaje original al cliente.
2. Validación de DTOs se mapea a `VALIDATION_ERROR` con
   `details.fields: [{ field, message }]`.
3. `HttpException` conocidas (`NotFoundException`, `ConflictException`,
   etc.) se mapean a códigos estables del catálogo.
4. Errores de Drizzle/pg se loggean con stack completo y se responden
   como `INTERNAL_ERROR` sin leak de queries.

Ver [api-contracts.md](./api-contracts.md) para el detalle.

## Brechas conocidas

| Brecha | Estado | Referencia |
| --- | --- | --- |
| Límite de tamaño de cuerpo y de peticiones por IP en `POST /api/v1/billing/webhook` | Pendiente | [`back#150` (`M-9`)](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/150) |
| Escaneo de `check-no-real-keys.sh` ampliado a `.github/workflows/` y `.env.example` | Pendiente | [`back#150` (`B-5`)](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/150) |
| Bloqueos en memoria (`withUserLock`) si algún día se escala a >1 réplica | Pendiente (1 réplica hoy) | [`back#150` (`M-4`)](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/150) |
| Migración de Stripe Test Mode a Stripe Live antes de abrir cobros reales | Pendiente de salida a vivo | [`decisions/PENDIENTES.md`](../decisions/PENDIENTES.md#pend-002--se-autoriza-el-primer-despliegue-a-producción) |