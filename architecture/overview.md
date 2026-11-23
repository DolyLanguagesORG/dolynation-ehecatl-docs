# Arquitectura — overview

Cómo está organizado el backend y cómo fluye un request desde que llega al
servidor hasta que vuelve la respuesta.

## Vista de módulos

```
                  ┌─────────────────────────────────────────┐
                  │           Bootstrap (main.ts)           │
                  │  helmet, CORS, rawBody, ValidationPipe  │
                  └────────────────────┬────────────────────┘
                                       │
                  ┌────────────────────▼────────────────────┐
                  │                AppModule                │
                  │  ConfigModule (Zod) · Schedule · Logger │
                  │  DatabaseModule · CommonModule (Global) │
                  └────────────────────┬────────────────────┘
                                       │
   ┌───────────────┬───────────┬───────┴───┬───────────────┬──────────────┐
   ▼               ▼           ▼           ▼               ▼              ▼
┌──────┐     ┌───────────┐ ┌────────┐ ┌─────────┐   ┌────────────┐  ┌──────────┐
│ auth │     │ readings  │ │billing │ │security │   │  settings  │  │  admin   │
│oauth │     │evaluation │ │subscr. │ │mail     │   │  history   │  │logs/audit│
└──┬───┘     └─────┬─────┘ └───┬────┘ └────┬────┘   └──────┬─────┘  └────┬─────┘
   │               │           │           │               │             │
   └───────────────┴───────────┴───────────┴───────────────┴─────────────┘
                                       │
                ┌──────────────────────▼──────────────────────┐
                │            PostgreSQL (Drizzle)             │
                │  Google/MiniMax IA · OAuth · Stripe · Brevo │
                └─────────────────────────────────────────────┘
```

`CommonModule` registra filtros, interceptores y cuatro guards globales en
[`src/common/common.module.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/common/common.module.ts):

- `APP_FILTER` → `AllExceptionsFilter` (envelope de errores + `error_logs`)
- `APP_INTERCEPTOR` → `LoggingInterceptor` (log HTTP estructurado)
- `APP_GUARD` → `JwtAuthGuard` (auth opt-out vía `@Public()`)
- `APP_GUARD` → `SubscriptionGuard` (requiere plan salvo `@Public()` o `@AllowWithoutSubscription()`)
- `APP_GUARD` → `IpRateLimitGuard` (rate limit vía `@RateLimitByIp(...)`)
- `APP_GUARD` → `CaptchaGuard` (Cloudflare Turnstile vía `@RequireCaptcha(...)`)

## Estructura de directorios del backend

```
src/
├── main.ts                          # Bootstrap (helmet, CORS, rawBody, Scalar)
├── app.module.ts                    # Composition root
├── config/                          # env.config.ts, env.validation.ts (Zod)
├── common/                          # Concerns transversales
│   ├── decorators/                  # @Public(), @AllowWithoutSubscription(), @CurrentUser(), @AdminOnly()
│   ├── errors/                      # AllExceptionsFilter, ErrorCode, AppHttpException
│   ├── guards/                      # JwtAuthGuard, SubscriptionGuard
│   ├── interceptors/                # LoggingInterceptor
│   └── types/                       # ApiResponse, ApiSuccessEnvelopeDto, envelope decorators
├── database/                        # @Global con Drizzle
│   └── drizzle/                     # schema.ts, relations.ts, types.ts
└── modules/                         # 18 módulos de negocio e integración
    ├── access-requests/             # Solicitudes manuales de plan o desbloqueo de idioma
    ├── admin/                       # Panel admin, usuarios, solicitudes y consultas de logs (+ AdminGuard)
    ├── auth/                        # register, login, refresh, logout, verify-email + oauth/ (Google y Microsoft)
    ├── billing/                     # Stripe Checkout/Portal, PaymentSheet, webhooks e historial
    ├── content/                     # Catálogos y recursos compartidos
    ├── evaluation/                  # Evaluación PNL de comprensión lectora
    ├── health/                      # /health/live, /health/ready (Terminus)
    ├── history/                     # Historial de lecturas y puntajes
    ├── ia/                          # Adaptadores Gemini / MiniMax y selección de proveedor
    ├── logs/                        # AuditLogService, ErrorLogService y RequestContextMiddleware
    ├── mail/                        # Brevo SMTP y plantillas multi-idioma
    ├── moderation/                  # Moderación multi-capa de categorías (regex + IA + caché)
    ├── readings/                    # Lecturas, explicaciones de vocabulario, glosario y prompt-logs
    ├── security/                    # CaptchaGuard (Turnstile) y IpRateLimitGuard
    ├── settings/                    # Idiomas, categorías y cambio anual / créditos
    ├── subscriptions/               # Reglas y cuotas por plan (Dolly, Dolly Plus, Dolly Pro)
    ├── users/                       # Perfil, racha diaria y preferencias de usuario
    └── version/                     # Metadatos de versión y build (`GET /api/v1/version`)
```

## Ciclo de vida de un request (happy path)

```
1. HTTP request llega a Express
2. helmet añade headers de seguridad
3. compression intenta comprimir la respuesta
4. JwtAuthGuard valida el token (si no es @Public()):
   - sin token → AUTH_UNAUTHORIZED (401)
   - token expirado → AUTH_TOKEN_EXPIRED (401)
   - token inválido → AUTH_TOKEN_INVALID (401)
5. ValidationPipe valida el body/query/params contra el DTO:
   - campos extra → VALIDATION_ERROR (400)
   - campos inválidos → VALIDATION_ERROR (400) con details.fields
6. Controller recibe los datos validados
7. Service ejecuta la lógica de negocio (consulta BD, llama al LLM, etc.)
8. Controller envuelve la respuesta con apiOk(message, data)
9. LoggingInterceptor loggea la respuesta exitosa
10. Express serializa el JSON y lo envía
```

## Ciclo de vida de un error

```
1. Cualquiera de los pasos anteriores lanza una excepción
2. NestJS enruta la excepción al AllExceptionsFilter
3. El filtro decide:
   - Es AppHttpException con ErrorCode? → usa el metadata del catálogo
   - Es HttpException de Nest (BadRequestException, etc.)? → mapea por status
   - Es un Error genérico? → loggea el stack completo, responde INTERNAL_ERROR
4. La respuesta se envuelve con apiFail(code, message, details?)
5. LoggingInterceptor loggea el fallo
6. Express envía el JSON
```

**Code path** del filtro:
[`src/common/errors/all-exceptions.filter.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/common/errors/all-exceptions.filter.ts).

## Por qué este diseño

- **CommonModule global** evita repetir `useGlobalFilters`, `useGlobalGuards`,
  etc. en cada módulo.
- **Subdominios en `readings/`** (`prompt-generation`, `prompt-logs`) — el
  módulo principal solo orquesta; cada subdominio tiene su propio service
  y tests.
- **DTOs separados de entities** — el contrato HTTP no expone la forma
  interna de la BD.
- **Envelopes via decorador** (`ApiOkResponseOf`) — un solo lugar para
  cambiar la forma de todas las respuestas en Scalar.

## Estado por módulos (`v0.15.0`)

| Grupo de módulos | Estado | Alcance |
| --- | --- | --- |
| `auth` (incluye `oauth/`), `users`, `settings`, `security`, `mail` | Implementado | Registro, verificación SMTP, JWT + refresh BFF, Google y Microsoft Entra ID OAuth, Turnstile y rate limit |
| `readings`, `evaluation`, `history`, `moderation`, `ia`, `content` | Implementado | Generación y evaluación con Gemini/MiniMax, moderación por capas, glosario (`reading_explanations`), historial y racha |
| `billing`, `subscriptions`, `access-requests` | Implementado | Planes `dolly`/`dolly_plus`/`dolly_pro`, Stripe Checkout/Portal + webhooks e idempotencia, modo manual |
| `admin`, `logs`, `health`, `version` | Implementado | Panel administrativo, `audit_logs`, `error_logs`, traza por `requestId` y sondas Terminus |
| TTS de palabra/frase y caché por `prompt_hash` | Pendiente | [`back#44`](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/44), [`back#9`](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9) |

## Próximos pasos arquitecturales (ideas)

- Extraer puertos de dominio entre `readings/` e `ia/` si aumenta el número de proveedores externos.
- Evaluar un `cache.module.ts` compartido para `prompt_hash` (`back#9`) y locks distribuidos (`back#150` `M-4`) si el backend escala a múltiples réplicas.