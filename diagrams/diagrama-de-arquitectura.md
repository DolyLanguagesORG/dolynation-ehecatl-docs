# Diagrama de arquitectura

Estructura del sistema: los cuatro repositorios, los módulos del backend, el
frontend y los servicios externos.

```mermaid
flowchart TB
    subgraph USUARIOS["Usuarios"]
        U["👤 Estudiante"]
    end

    subgraph FRONT["dolynation-tonatiuh-front · Next.js 16"]
        FE_ROUTES["App Router<br/>páginas y componentes"]
        FE_I18N["i18n en/fr/es/it"]
        FE_STATE["Estado de sesión<br/>tokens en memoria"]
        FE_API["Cliente HTTP<br/>src/lib/api.ts"]
    end

    subgraph BACK["dolynation-atl-back · NestJS 11"]
        subgraph MODULES["Módulos de negocio"]
            M_AUTH["auth<br/>register · login · refresh · logout · me"]
            M_USERS["users<br/>perfil · preferencias · racha"]
            M_READ["readings<br/>generar · evaluar · vocabulario"]
            M_IA["ia<br/>proveedor de IA · TTS"]
            M_HEALTH["health<br/>live · ready"]
        end
        subgraph COMMON["common"]
            C_ENV["Env (Zod)"]
            C_GUARD["JwtAuthGuard · AdminGuard"]
            C_ENVELOPE["Envelope apiOk/apiFail"]
            C_ERRORS["Catálogo ErrorCode"]
            C_VERSION["version.ts"]
        end
        DB_ACCESS["Drizzle ORM<br/>src/database/drizzle"]
    end

    subgraph INFRA["dolynation-tlalli-infra"]
        COMPOSE["Docker Compose<br/>dev · test · prod"]
        SCHEMA["Schema PostgreSQL 15<br/>01-init.sql + updates/"]
        CI["CI/CD<br/>Actions · rulesets · deploy"]
    end

    subgraph DOCS["dolynation-ehecatl-docs"]
        ANT["Anteproyecto (Unidad 1)"]
        U2["Unidad 2<br/>workflow · versionado · diagramas"]
    end

    subgraph EXT["Servicios externos"]
        LLM["MiniMax-M3<br/>generación y evaluación"]
        TTS["MiniMax TTS<br/>audio de palabra/frase"]
    end

    DB[("PostgreSQL 15<br/>users · readings · evaluations<br/>prompt_logs · categorías")]

    U --> FE_ROUTES
    FE_ROUTES --> FE_I18N
    FE_ROUTES --> FE_STATE
    FE_STATE --> FE_API
    FE_API -->|"REST /api/v1 + JWT"| M_AUTH
    FE_API --> M_USERS
    FE_API --> M_READ
    FE_API --> M_HEALTH
    C_GUARD -.->|"protege"| FE_API
    M_AUTH --> DB_ACCESS
    M_USERS --> DB_ACCESS
    M_READ --> DB_ACCESS
    M_HEALTH --> DB_ACCESS
    DB_ACCESS --> DB
    M_READ -->|"adaptador AIProvider"| LLM
    M_READ -->|"adaptador TtsProvider"| TTS
    COMPOSE -.->|"despliega"| BACK
    COMPOSE -.->|"define"| SCHEMA
    SCHEMA -.->|"fuente de verdad"| DB
    CI -.->|"valida y publica"| BACK
    CI -.->|"build y deploy"| FRONT
    DOCS -.->|"contrato y reglas"| BACK
    DOCS -.->|"contrato y reglas"| FRONT
    DOCS -.->|"entornos"| INFRA

    classDef front fill:#e8f2ff,stroke:#2864a5,color:#111111
    classDef back fill:#f3e8ff,stroke:#7b3fa0,color:#111111
    classDef infra fill:#fff4e0,stroke:#c77700,color:#111111
    classDef docs fill:#e8f5e9,stroke:#388e3c,color:#111111
    classDef ext fill:#fdecec,stroke:#c0392b,color:#111111
    classDef data fill:#f5f5f5,stroke:#555555,color:#111111

    class FE_ROUTES,FE_I18N,FE_STATE,FE_API front
    class M_AUTH,M_USERS,M_READ,M_IA,M_HEALTH,C_ENV,C_GUARD,C_ENVELOPE,C_ERRORS,C_VERSION,DB_ACCESS back
    class COMPOSE,SCHEMA,CI infra
    class ANT,U2 docs
    class LLM,TTS ext
    class DB data
```

**Estado:** el backend tiene implementados `auth`, `users`, `readings`, `ia` y
`health`; el frontend está en construcción (`front#2` en el Sprint 2) y la
infraestructura ya tiene los tres entornos definidos.

> **Nota.** El diagrama muestra la arquitectura **objetivo**. Lo que ya está
> construido y en qué sprint llega cada parte está en
> [`../plan/cronograma.md`](../plan/cronograma.md).
