@startuml
left to right direction
skinparam packageStyle rectangle
skinparam shadowing false
skinparam actorStyle stickman

' --- COLUMNA IZQUIERDA: ACTORES HUMANOS ---
actor "Estudiante / Usuario\n(ROLE_STUDENT)" as Student
actor "Administrador\n(ROLE_ADMIN)" as Admin

' Forzar apilamiento en la columna izquierda
Student -[hidden]down-> Admin

' --- COLUMNA CENTRAL: SISTEMA Y CASOS DE USO (CUBRE RF-01 A RF-13) ---
rectangle "Sistema de Lectura e Inteligencia (DolyNation)" {
  
  ' Casos de Uso Estudiante
  usecase "1. Autenticación y Perfil\n(RF-01, RF-02, RF-03, RF-04, RF-11)" as UC_Auth
  usecase "2. Consultar Racha e Historial\n(RF-09, RF-10)" as UC_Hist
  usecase "3. Generar Lecturas\n(RF-05, RF-06, RF-13)" as UC_Gen
  usecase "4. Consultar Diccionario Contextual\n(RF-08)" as UC_Dict
  usecase "5. Reproducir Audio (TTS)\n(RF-08)" as UC_Audio
  usecase "6. Enviar Resumen (Evaluación PNL)\n(RF-07)" as UC_Eval

  ' Casos de Uso Admin
  usecase "7. Acceso a Panel Administrativo" as UC_Admin
  usecase "8. Gestionar Categorías Globales" as UC_Cat
  usecase "9. Supervisar Métricas del Sistema" as UC_Metrics
}

' --- COLUMNA DERECHA: SERVICIOS EXTERNOS ---
actor "Proveedor de IA\n(SYSTEM_AI_PROVIDER)" as AI
actor "Servicio TTS\n(SYSTEM_TTS_PROVIDER)" as TTS

' Forzar apilamiento en la columna derecha
AI -[hidden]down-> TTS

' --- RELACIONES: ESTUDIANTE -> CASOS DE USO ---
Student --> UC_Auth
Student --> UC_Hist
Student --> UC_Gen
Student --> UC_Dict
Student --> UC_Audio
Student --> UC_Eval

' --- RELACIONES: ADMINISTRADOR -> CASOS DE USO ---
Admin --> UC_Admin
Admin --> UC_Cat
Admin --> UC_Metrics

' --- RELACIONES: CASOS DE USO -> SERVICIOS EXTERNOS ---
UC_Gen --> AI
UC_Dict --> AI
UC_Eval --> AI
UC_Audio --> TTS

@enduml