# Diagrama de actores y casos de uso

Actores humanos, casos de uso del estudiante y servicios externos del sistema de lectura e inteligencia de DolyNation.

```mermaid
---
config:
  layout: fixed
---
flowchart LR
 subgraph HUMANOS["Actores humanos"]
    direction LR
        Student["👤 Estudiante / Usuario<br>(rol STUDENT)"]
  end
 subgraph STUDENT_UC["Casos de uso del estudiante"]
    direction LR
        UC_Auth(["1. Autenticación y Perfil<br>(RF-01, RF-02, RF-03, RF-04, RF-11)"])
        UC_Hist(["2. Consultar Racha e Historial<br>(RF-09, RF-10)"])
        UC_Gen(["3. Generar Lecturas<br>(RF-05, RF-06, RF-13)"])
        UC_Dict(["4. Consultar Diccionario Contextual<br>(RF-08)"])
        UC_Audio(["5. Reproducir Audio (TTS)<br>(RF-08)"])
        UC_Eval(["6. Enviar Resumen (Evaluación PNL)<br>(RF-07)"])
  end
 subgraph SYSTEM["Sistema de Lectura e Inteligencia (DolyNation)"]
    direction LR
        UC_Auth
        UC_Hist
        UC_Gen
        UC_Dict
        UC_Audio
        UC_Eval
  end
 subgraph EXTERNAL["Servicios externos"]
    direction LR
        AI["Proveedor de IA<br>MiniMax-M3<br>(AIProvider)"]
        TTS["Proveedor de voz<br>MiniMax TTS<br>(TtsProvider)"]
  end
    UC_Auth ~~~ UC_Hist
    UC_Hist ~~~ UC_Gen
    UC_Gen ~~~ UC_Dict
    UC_Dict ~~~ UC_Audio
    UC_Audio ~~~ UC_Eval
    AI ~~~ TTS
    Student --> UC_Auth & UC_Hist & UC_Gen & UC_Dict & UC_Audio & UC_Eval
    UC_Gen --> AI
    UC_Dict --> AI
    UC_Eval --> AI
    UC_Audio --> TTS

     Student:::actor
     UC_Auth:::usecase
     UC_Hist:::usecase
     UC_Gen:::usecase
     UC_Dict:::usecase
     UC_Audio:::usecase
     UC_Eval:::usecase
     AI:::external
     TTS:::external
    classDef actor fill:#ffffff,stroke:#333333,color:#111111
    classDef usecase fill:#e8f2ff,stroke:#2864a5,color:#111111
    classDef external fill:#e8f5e9,stroke:#388e3c,color:#111111
```


**Estado:** el diagrama describe el modelo de casos de uso del MVP. Los casos de uso administrativos (`back#17`, `front#12`) se entregan en el Sprint 4.

