# Diagrama entidad-relación

Modelo de datos de PostgreSQL: diez tablas, sus claves y sus relaciones.

```mermaid
erDiagram
    users {
        SERIAL id PK
        VARCHAR email UK
        VARCHAR password
        VARCHAR full_name
        VARCHAR role
        INTEGER current_streak
        DATE last_streak_date
        TIMESTAMP created_at
        TIMESTAMP updated_at
        TIMESTAMP deleted_at
    }

    auth_access_tokens {
        SERIAL id PK
        INTEGER tokenable_id FK
        VARCHAR type
        VARCHAR name
        VARCHAR hash
        TEXT abilities
        TIMESTAMP created_at
        TIMESTAMP updated_at
        TIMESTAMP last_used_at
        TIMESTAMP expires_at
        TIMESTAMP deleted_at
    }

    categories {
        SERIAL id PK
        VARCHAR slug UK
        VARCHAR name
        TEXT description
        BOOLEAN is_global
        INTEGER created_by_user_id FK
        TIMESTAMP created_at
    }

    user_preferences {
        INTEGER user_id PK, FK
        VARCHAR target_language
        VARCHAR default_difficulty
        VARCHAR default_length
        TIMESTAMP updated_at
    }

    user_selected_categories {
        INTEGER user_id PK, FK
        INTEGER category_id PK, FK
    }

    readings {
        SERIAL id PK
        INTEGER user_id FK
        VARCHAR category
        INTEGER category_id FK
        VARCHAR language
        VARCHAR length_type
        VARCHAR prompt_hash
        VARCHAR title
        TEXT description
        TEXT content
        VARCHAR difficulty
        INTEGER word_count
        VARCHAR status
        INTEGER score
        BOOLEAN passed
        TEXT user_response
        TEXT feedback
        TIMESTAMP created_at
        TIMESTAMP updated_at
        TIMESTAMP deleted_at
    }

    evaluations {
        SERIAL id PK
        INTEGER reading_id FK, UK
        INTEGER user_id FK
        TEXT user_summary
        INTEGER score
        BOOLEAN passed
        TEXT feedback
        TEXT main_ideas_coverage
        TIMESTAMP created_at
    }

    vocabulary_logs {
        SERIAL id PK
        INTEGER user_id FK
        INTEGER reading_id FK
        VARCHAR selected_text
        TEXT original_sentence
        TEXT definition
        TEXT contextual_example
        TIMESTAMP created_at
    }

    prompt_logs {
        SERIAL id PK
        VARCHAR level
        VARCHAR event
        TEXT message
        VARCHAR seed
        INTEGER user_id FK
        INTEGER text_id FK
        JSONB params
        TEXT system_prompt
        TEXT user_prompt
        TEXT error_message
        TEXT error_stack
        INTEGER duration_ms
        TIMESTAMP created_at
    }

    users ||--o| user_preferences : "tiene preferencias"
    users ||--o{ auth_access_tokens : "posee tokens"
    users ||--o{ user_selected_categories : "selecciona"
    categories ||--o{ user_selected_categories : "es seleccionada"
    users ||--o{ readings : "genera"
    categories ||--o{ readings : "clasifica"
    readings ||--o| evaluations : "tiene evaluacion"
    users ||--o{ evaluations : "realiza"
    users ||--o{ vocabulary_logs : "consulta vocabulario"
    readings o|--o{ vocabulary_logs : "contextualiza"
    users o|--o{ prompt_logs : "genera registros"
    readings o|--o{ prompt_logs : "se registra en"
    users o|--o{ categories : "crea categorias"
```


**Estado:** el diagrama muestra el modelo **objetivo**. Hoy existen `users`, `auth_access_tokens`, `readings` y `prompt_logs` (`01-init.sql`); las demás tablas llegan con las migraciones `02`, `03` y `04` (`infra#20`, `infra#21`, `infra#22`). El detalle campo por campo está en [`diccionario-de-datos.md`](./diccionario-de-datos.md).

