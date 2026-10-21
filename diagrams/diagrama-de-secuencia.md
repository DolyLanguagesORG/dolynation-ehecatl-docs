# Diagrama de secuencia — flujo principal

Las tres fases del flujo de aprendizaje: generación de la lectura con IA, diccionario contextual con audio TTS y evaluación PNL con racha diaria.

```mermaid
sequenceDiagram
    autonumber

    actor Student as Estudiante
    participant FE as Frontend (Next.js)
    participant BE as Backend (NestJS)
    participant DB as Base de Datos (PostgreSQL)
    participant AI as API de IA (MiniMax-M3)
    participant TTS as Servicio TTS

    Note over Student,DB: FASE 1: Generación de Lectura con IA (RF-05, RF-06, RF-13)

    Student->>FE: Selecciona idioma, categoría, dificultad y longitud
    FE->>BE: POST /api/v1/readings<br/>Header: Bearer JWT<br/>Body: language, category, difficulty, size
    BE->>BE: Validar JWT y DTO de entrada

    alt Lectura en caché (mismo usuario + prompt_hash)
        BE->>DB: Buscar lectura no borrada por user_id y prompt_hash
        DB-->>BE: Retorna lectura almacenada previamente
        BE-->>FE: HTTP 200 OK (Objeto Lectura cacheada)
    else Lectura nueva (Generación por IA)
        BE->>AI: Solicitar texto personalizado (prompt versionado por idioma)
        AI-->>BE: Retorna título, descripción, contenido y metadatos
        BE->>DB: Guardar lectura, language, length_type, category_id y prompt_hash
        DB-->>BE: Confirmación (reading_id)
        BE-->>FE: HTTP 201 Created (Objeto Lectura)
    end

    FE-->>Student: Despliega texto en el Visor Inmersivo de Lectura

    Note over Student,TTS: FASE 2: Diccionario y Audio TTS (RF-08)

    Student->>FE: Selecciona palabra o frase dentro del texto
    FE->>BE: POST /api/v1/readings/{id}/explanations<br/>Body: word, context
    BE->>AI: Solicitar significado, definición y ejemplo en contexto
    AI-->>BE: Retorna explicación estructurada
    BE->>DB: Guardar en vocabulary_logs
    DB-->>BE: Confirmación de guardado
    BE-->>FE: HTTP 200 OK (significado, definición, ejemplos y oración original)
    FE-->>Student: Muestra Pop-up / Modal de Diccionario Contextual

    opt Reproducir pronunciación de audio
        Student->>FE: Clic en botón de Audio
        FE->>BE: GET /api/v1/readings/{id}/tts?text=frase_corta
        BE->>TTS: Solicitar síntesis de voz (texto corto)
        TTS-->>BE: Retorna buffer de audio
        BE-->>FE: Stream de Audio (MP3/WAV)
        FE-->>Student: Reproduce audio de pronunciación
    end

    Note over Student,DB: FASE 3: Evaluación PNL y Racha Diaria (RF-07, RF-09, RF-10)

    Student->>FE: Redacta resumen libre y clic en Enviar Evaluación
    FE->>BE: POST /api/v1/readings/{id}/evaluate<br/>Body: userResponse
    BE->>AI: Enviar texto original y resumen para análisis PNL/LLM
    AI-->>BE: Retorna cobertura, precisión, coherencia y feedback
    BE->>DB: Guardar resultado en evaluations
    BE->>DB: Actualizar lectura a status=completed
    BE->>BE: Calcular racha y puntos desde la evaluación
    BE->>DB: Actualizar users.current_streak y last_streak_date
    DB-->>BE: Confirmación de actualización

    BE-->>FE: HTTP 200 OK (score, passed, feedback y racha actualizada)
    FE-->>Student: Muestra resultados y animación de Racha Diaria
```


**Estado:** describe el comportamiento **objetivo**. La caché por `prompt_hash` (`back#9`), el endpoint de TTS (`back#44`) y el motor de evaluación (`back#12`) se entregan en los sprints 2 y 3.

