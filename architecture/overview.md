# Arquitectura — overview

Cómo está organizado el backend y cómo fluye un request desde que llega al
servidor hasta que vuelve la respuesta.

## Vista de módulos

```
                  ┌──────────────────────────────────┐
                  │          Bootstrap (main.ts)      │
                  │  helmet, ValidationPipe, Scalar  │
                  └─────────────────┬────────────────┘
                                    │
                  ┌─────────────────▼────────────────┐
                  │           AppModule              │
                  │  ConfigModule + LoggerModule     │
                  │  + DatabaseModule (Global)       │
                  │  + CommonModule (Global)         │
                  └─────────────────┬────────────────┘
                                    │
        ┌───────────┬───────────┬───┴────────┬────────────┬───────────┐
        ▼           ▼           ▼            ▼            ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
   │  auth   │ │  users  │ │readings │ │   ia    │ │ health  │ │settings │
   │ module  │ │ module  │ │ module  │ │ module  │ │ module  │ │history  │
   │         │ │         │ │         │ │         │ │         │ │admin    │
   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └─────────┘
        │           │           │           │           │
        └───────────┴───────────┴─────┬─────┴───────────┘
                                     │
                       ┌─────────────▼──────────────┐
                       │  Drizzle ORM (PostgreSQL)  │
                       │  + AI providers            │
                       │  (MiniMax-M3, groq)         │
                       └────────────────────────────┘
```

`CommonModule` registra tres providers globales (en
[`src/common/common.module.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/common/common.module.ts)):

- `APP_FILTER` → `AllExceptionsFilter` (envelope de errores)
- `APP_INTERCEPTOR` → `LoggingInterceptor` (log de cada request exitoso)
- `APP_GUARD` → `JwtAuthGuard` (auth opt-in vía `@Public()`)

## Estructura de directorios del backend

```
src/
├── main.ts                          # Bootstrap (helmet, pipes, Scalar)
├── app.module.ts                    # Composition root
├── config/                          # env.config.ts, env.validation.ts (Zod)
├── common/                          # Concerns transversales
│   ├── decorators/                  # @Public(), @CurrentUser()
│   ├── errors/                      # AllExceptionsFilter, ErrorCode, AppHttpException
│   ├── guards/                      # JwtAuthGuard
│   ├── interceptors/                # LoggingInterceptor
│   └── types/                       # ApiResponse, ApiSuccessEnvelopeDto, envelope decorators
├── database/                        # @Global con Drizzle
│   └── drizzle/                     # schema.ts, relations.ts, types.ts
└── modules/
    ├── auth/                        # register, login, refresh, /me, logout
    ├── users/                       # /users/streak, /users/points
    ├── readings/                    # /readings (generar, evaluar, explicar, TTS)
    │   ├── prompt-generation/       # Subdomain: catalog, prompt-builder
    │   ├── prompt-logs/             # Subdomain: audit de prompts
    │   └── (planificado) cache/     # S2: caché por prompt_hash
    ├── settings/                    # (S2) /settings/language, /settings/categories
    ├── history/                     # (S4) /history, /history/scores
    ├── admin/                       # (S4) /admin/categories, /admin/users
    ├── ia/                          # /ia/chat (passthrough al provider activo)
    │   └── providers/               # MiniMax-M3.provider, ai-provider.factory, interfaces
    └── health/                      # /health/live, /health/ready (Terminus)
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

## Módulos actuales y planificados

| Módulo | Estado | Issue |
| --- | --- | --- |
| `auth`, `users`, `readings`, `ia`, `health` | Implementado | — |
| `settings` (preferencias e idioma) | Planificado S2 | `back#8` |
| caché de lecturas | Planificado S2 | `back#9` |
| evaluación de resumen y vocabulario/TTS | Planificado S3 (dentro de `readings`) | `back#11`, `back#13` |
| `history` | Planificado S4 | `back#16` |
| `admin` | Planificado S4 | `back#17` |

## Próximos pasos arquitecturales (ideas)

- Extraer `ia/` en un módulo de infraestructura para que
  `readings/` no importe providers directamente.
- Mover la lógica de auth a un módulo compartido si se añade un segundo
  servicio que necesite JWT.
- Introducir un `cache.module.ts` cuando el catálogo de prompts esté
  lo suficientemente estable como para cachear.