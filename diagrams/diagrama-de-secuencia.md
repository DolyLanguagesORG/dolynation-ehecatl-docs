@startuml
autonumber
skinparam shadowing false
skinparam sequenceMessageAlign center
skinparam boxPadding 10

actor "Estudiante" as Student
participant "Frontend\n(Next.js)" as FE
participant "Backend\n(NestJS)" as BE
database "Base de Datos\n(PostgreSQL)" as DB
actor "API de IA\n(MiniMax-M3)" as AI
actor "Servicio TTS" as TTS

' ==========================================
' FASE 1: GENERACIÓN DE LECTURA CON IA
' ==========================================
box "1. Módulo de Lecturas (RF-05, RF-06, RF-13)" #LightBlue
Student -> FE: Selecciona idioma, categoría, dificultad y longitud
FE -> BE: POST /api/v1/readings\n[Header: Bearer JWT | Body: language, category, difficulty, size]
BE -> BE: Validar JWT y DTO de entrada

alt Lectura en Caché (mismo usuario + prompt_hash)
    BE -> DB: Buscar lectura no borrada por (user_id, prompt_hash)
    DB --> BE: Retorna lectura almacenada previamente
    BE --> FE: HTTP 200 OK (Objeto Lectura cacheada)
else Lectura Nueva (Generación por IA)
    BE -> AI: Solicitar texto personalizado (prompt versionado por idioma)
    AI --> BE: Retorna lectura (título, descripción, contenido, metadatos)
    BE -> DB: Guardar lectura + language, length_type, category_id, prompt_hash
    DB --> BE: Confirmación (reading_id)
    BE --> FE: HTTP 201 Created (Objeto Lectura)
end

FE --> Student: Despliega texto en el Visor Inmersivo de Lectura
end box

' ==========================================
' FASE 2: DICCIONARIO Y AUDIO TTS
' ==========================================
box "2. Módulo de Vocabulario Contextual (RF-08)" #LightGreen
Student -> FE: Selecciona palabra o frase dentro del texto
FE -> BE: POST /api/v1/readings/{id}/explanations\n[Body: word, context]
BE -> AI: Solicitar significado, definición y ejemplo en contexto
AI --> BE: Retorna explicación estructurada
BE -> DB: Guardar en vocabulary_logs
BE --> FE: HTTP 200 OK (significado, definición, ejemplos, oración original)
FE --> Student: Muestra Pop-up / Modal de Diccionario Contextual

opt Reproducir Pronunciación de Audio
    Student -> FE: Clic en botón de Audio
    FE -> BE: GET /api/v1/readings/{id}/tts?text=frase_corta
    BE -> TTS: Solicitar síntesis de voz (texto corto)
    TTS --> BE: Retorna buffer de audio
    BE --> FE: Stream de Audio (MP3/WAV)
    FE --> Student: Reproduce audio de pronunciación
end
end box

' ==========================================
' FASE 3: EVALUACIÓN PNL Y RACHA DIARIA
' ==========================================
box "3. Evaluación PNL y Racha (RF-07, RF-09, RF-10)" #LightYellow
Student -> FE: Redacta resumen libre y clic en "Enviar Evaluación"
FE -> BE: POST /api/v1/readings/{id}/evaluate\n[Body: userResponse]
BE -> AI: Enviar texto original + resumen para análisis PNL/LLM
AI --> BE: Retorna cobertura, precisión, coherencia y feedback
BE -> DB: Guardar resultado en evaluations
BE -> DB: Actualizar lectura a status='completed'
BE -> BE: Calcular racha y puntos desde la evaluación
BE -> DB: Actualizar users.current_streak / last_streak_date
DB --> BE: Confirmación de actualización

BE --> FE: HTTP 200 OK (score, passed, feedback, racha actualizada)
FE --> Student: Muestra pantalla de resultados y animación de Racha Diaria
end box

@enduml
