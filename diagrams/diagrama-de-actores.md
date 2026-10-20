@startuml
' Estado del modelo: los roles STUDENT/ADMIN y las categorias globales estan
' planificados (infra#22, back#17). El adaptador AIProvider ya existe
' (back#19) y el de TTS se implementa en el Sprint 2 (back#43).
left to right direction
skinparam packageStyle rectangle
skinparam shadowing false
skinparam actorStyle stickman

' --- COLUMNA IZQUIERDA: ACTORES HUMANOS ---
actor "Estudiante / Usuario\n(rol STUDENT)" as Student
actor "Administrador\n(rol ADMIN)" as Admin

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
  usecase "9. Supervisar Usuarios Registrados" as UC_Metrics
}

' --- COLUMNA DERECHA: SERVICIOS EXTERNOS ---
actor "Proveedor de IA\n(MiniMax-M3, via AIProvider)" as AI
actor "Proveedor de voz\n(MiniMax TTS, via TtsProvider)" as TTS

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