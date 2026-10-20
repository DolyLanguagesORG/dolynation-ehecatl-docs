@startuml Flujo_Seguridad_Auth_DolyNation
' Estado del modelo: la persistencia, rotacion y revocacion del refresh token
' en auth_access_tokens todavia NO esta implementada (hoy el refresh es un JWT
' stateless y logout es un no-op). Corresponde a back#4. El hash de argon2 y el
' JWT con expiracion ya estan implementados (back#3).
autonumber
skinparam shadowing false
skinparam sequenceMessageAlign center

actor "👤 Usuario" as U
participant "📱 Next.js (Cliente)" as FE
participant "⚙️ NestJS (API)" as BE
database "🗄️ PostgreSQL" as DB

== FASE 1: INICIO DE SESIÓN ==
U -> FE: Ingresa Email y Contraseña
FE -> BE: POST /api/v1/auth/login\n[Body: email, password]
BE -> DB: Buscar usuario por email
DB --> BE: Retorna registro (incluye password)
BE -> BE: Comparar contraseña con argon2.verify()

alt Credenciales Válidas
    BE -> BE: Generar Access Token (JWT - 15 min)
    BE -> BE: Generar Refresh Token (30 días)
    BE -> DB: Guardar hash del Refresh Token en auth_access_tokens
    BE --> FE: HTTP 200 OK\n[Body: Access Token + Refresh Token + User Info]
    FE -> FE: Guardar access token en memoria/contexto\n(refresh en almacenamiento seguro; no localStorage)
    FE --> U: Redirige al Dashboard de Usuario
else Credenciales Inválidas
    BE --> FE: HTTP 401 Unauthorized (Mensaje genérico)
end

== FASE 2: PETICIÓN PROTEGIDA CON ACCESS TOKEN ==
U -> FE: Intenta generar una lectura
FE -> BE: POST /api/v1/readings\n[Header: Authorization: Bearer <JWT_Memoria>]
BE -> BE: JwtAuthGuard valida firma y expiración del JWT

alt Token Válido
    BE -> BE: Procesar petición y llamar a IA
    BE --> FE: HTTP 201 Created (Lectura generada)
else Token Expirado (401)
    BE --> FE: HTTP 401 Unauthorized (Token Expirado)

    == FASE 3: REFRESH TOKEN ROTATION (AUTOMÁTICO) ==
    FE -> BE: POST /api/v1/auth/refresh\n[Body: refreshToken]
    BE -> DB: Buscar y validar refresh token no revocado

    alt Refresh Token Válido
        BE -> BE: Revocar Refresh Token anterior (deleted_at)
        BE -> BE: Generar NUEVO Access Token + NUEVO Refresh Token
        BE -> DB: Guardar hash del nuevo Refresh Token
        BE --> FE: HTTP 200 OK [Nuevo Access Token + Nuevo Refresh Token]
        FE -> FE: Reintentar petición original con el nuevo token
    else Refresh Token Revocado / Inválido
        BE --> FE: HTTP 401 Unauthorized
        FE -> FE: Limpiar memoria y redirigir a Login
    end
end

@enduml
