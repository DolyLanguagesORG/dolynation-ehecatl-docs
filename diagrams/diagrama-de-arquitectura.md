# Diagrama de arquitectura

Estructura del sistema (`v0.15.0`): los cinco repositorios activos, los módulos
del backend, los BFF de Next.js, la landing estática y los servicios externos.

```mermaid
flowchart TB
    subgraph USUARIOS["Usuarios"]
        U["Estudiante"]
        ADM["Administrador"]
    end

    subgraph LANDING["dolynation-tetl-landing · Astro"]
        SITE["Landing pública estática (dev / staging / prod)"]
    end

    subgraph FRONT["dolynation-tonatiuh-front · Next.js 16"]
        FE_ROUTES["App Router e i18n (es, en, fr, it)"]
        FE_AUTH_BFF["BFF OAuth PKCE (/api/auth/oauth/*) y Refresh Cookie HttpOnly"]
        FE_PROXY["Proxy BFF (/api/v1/*) hacia BACKEND_INTERNAL_URL"]
        FE_STRIPE["UI Stripe Elements + Turnstile"]
    end

    subgraph BACK["dolynation-atl-back · NestJS 11"]
        subgraph MODULES["18 módulos de negocio e integración"]
            M_AUTH["auth + oauth (Google / Microsoft)"]
            M_STUDY["readings, evaluation, history, content, moderation"]
            M_PAY["billing, subscriptions, access-requests"]
            M_CORE["users, settings, ia, mail"]
            M_GOV["security (Turnstile / IP), admin, logs, health, version"]
        end
        subgraph COMMON["CommonModule y Drizzle"]
            C_GUARDS["JwtAuthGuard, SubscriptionGuard, IpRateLimitGuard, CaptchaGuard"]
            DB_ACCESS["Drizzle ORM (src/database/drizzle)"]
        end
    end

    subgraph INFRA["dolynation-tlalli-infra"]
        PROXY["Nginx + Cloudflare Full (strict) + WireGuard dev"]
        SCHEMA["Schema PostgreSQL 15 (01-init.sql, 17 tablas)"]
    end

    subgraph DOCS["dolynation-ehecatl-docs"]
        U2["Arquitectura, convenciones, QA y BUGS"]
    end

    subgraph EXT["Servicios externos"]
        AI["Google Gemini / MiniMax / OpenAI Moderation"]
        IDP["Google OAuth y Microsoft Entra ID v2.0"]
        CF["Cloudflare Turnstile"]
        STRIPE["Stripe (Checkout, Portal y Webhooks)"]
        BREVO["Brevo SMTP (no-reply@dolynation.app)"]
    end

    DB[("PostgreSQL 15 (17 tablas)")]

    U -->|"dev / dolynation.app"| PROXY
    ADM -->|"Panel /admin"| PROXY
    PROXY --> SITE
    PROXY --> FE_ROUTES
    PROXY -->|"location = /api/v1/billing/webhook"| M_PAY
    FE_ROUTES --> FE_STRIPE
    FE_ROUTES --> FE_AUTH_BFF
    FE_ROUTES --> FE_PROXY
    FE_AUTH_BFF --> M_AUTH
    FE_PROXY --> M_AUTH
    FE_PROXY --> M_STUDY
    FE_PROXY --> M_PAY
    FE_PROXY --> M_CORE
    FE_PROXY --> M_GOV
    C_GUARDS -.->|"protege"| M_STUDY
    C_GUARDS -.->|"protege"| M_PAY
    C_GUARDS -.->|"protege"| M_CORE
    M_AUTH --> DB_ACCESS
    M_STUDY --> DB_ACCESS
    M_PAY --> DB_ACCESS
    M_CORE --> DB_ACCESS
    M_GOV --> DB_ACCESS
    DB_ACCESS --> DB
    M_STUDY --> AI
    M_CORE --> AI
    M_AUTH --> IDP
    FE_AUTH_BFF -.->|"authorize redirect"| IDP
    M_GOV --> CF
    M_PAY --> STRIPE
    STRIPE -->|"POST /api/v1/billing/webhook"| PROXY
    M_CORE --> BREVO
    SCHEMA -.->|"fuente de verdad"| DB
    DOCS -.->|"contratos y QA"| BACK
    DOCS -.->|"contratos y QA"| FRONT
    DOCS -.->|"entornos"| INFRA

    classDef landing fill:#e0f7fa,stroke:#00838f,color:#111111
    classDef front fill:#e8f2ff,stroke:#2864a5,color:#111111
    classDef back fill:#f3e8ff,stroke:#7b3fa0,color:#111111
    classDef infra fill:#fff4e0,stroke:#c77700,color:#111111
    classDef docs fill:#e8f5e9,stroke:#388e3c,color:#111111
    classDef ext fill:#fdecec,stroke:#c0392b,color:#111111
    classDef data fill:#f5f5f5,stroke:#555555,color:#111111

    class SITE landing
    class FE_ROUTES,FE_AUTH_BFF,FE_PROXY,FE_STRIPE front
    class M_AUTH,M_STUDY,M_PAY,M_CORE,M_GOV,C_GUARDS,DB_ACCESS back
    class PROXY,SCHEMA infra
    class U2 docs
    class AI,IDP,CF,STRIPE,BREVO ext
    class DB data
```

**Estado (`v0.15.0`):** los módulos de autenticación (correo + Google +
Microsoft Entra ID), seguridad (Turnstile + rate limit + CORS), correo (Brevo),
lecturas, glosario, evaluación, pagos con Stripe, moderación, administración y
auditoría están implementados y en fase de pruebas ([`plan/QA-PRUEBAS.md`](../plan/QA-PRUEBAS.md)).
La landing estática (`dolynation-tetl-landing`) corre ya en `dev` (`dev.dolynation.app`)
con despliegue independiente a `staging` y `prod`.
