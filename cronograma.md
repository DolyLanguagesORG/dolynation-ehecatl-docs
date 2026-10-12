# Cronograma de DolyNation

Este documento es la fuente de verdad escrita del cronograma. La vista
interactiva (Kanban y Timeline) vive en el [Project de GitHub](
https://github.com/orgs/DolyLanguagesORG/projects/1), y el detalle de cada
tarea en los issues del repositorio.

> **Alcance:** este cronograma cubre el **producto completo**, de principio a
> fin. El tag `v1.0.0` del Sprint 5 es la primera versión estable de ese
> producto, no una entrega parcial.

| Dato | Valor |
| --- | --- |
| Inicio del proyecto | 05/Oct/2026 |
| Entrega final | 10/Dic/2026 |
| Límite diario por tarea | 23:59 CST |
| Sprints | 5 |
| Tareas | 33 |
| Release actual | `v0.1.0` |
| Release de cierre | `v1.0.0` |

## Dónde ver el avance

- **Kanban y Timeline**: [Project — DolyNation Plan de Desarrollo (2026)](https://github.com/orgs/DolyLanguagesORG/projects/1)
  - Vista *Tablero Kanban*: agrupada por `Status` (Todo / In Progress / In Review / Done)
  - Vista *Timeline del producto*: eje de tiempo con `Start Date` → `Target Date`
  - Vista *Todos los entregables*: tabla con las 33 tareas
- **Issues**: los 33 entregables, uno por tarea
- **Milestones**: un milestone por sprint, con su fecha de cierre
- **Standup diario**: [hilo de registro de avances](https://github.com/DolyLanguagesORG/doly-languages/discussions/39)

## Cómo leer los números

En este documento las tareas se numeran del **1 al 33**, como en el
cronograma original. En GitHub los issues van del **6 al 38**, porque los
cincos pull request de configuración de la infraestructura consumieron los
números 1 a 5 antes de que se creara el backlog.

La correspondencia es fija y lineal:

```
número de GitHub = número de cronograma + 5
```

Cada issue indica su número de cronograma en la primera línea del cuerpo,
y este documento indica el número de GitHub. La tabla de abajo es la
referencia para pasar de uno a otro.

---

## Sprint 1 — Infraestructura, Autenticación y Perfil

**Periodo:** 05/Oct – 18/Oct/2026  
**Objetivo:** Configuración inicial del repositorio con reglas CI/CD, modelo de base de datos y módulo funcional de autenticación y perfil.  
**Cierre (milestone):** [Sprint 1: Infraestructura, Autenticación y Perfil](https://github.com/DolyLanguagesORG/doly-languages/milestone/1)  
**Tareas:** 9

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 1 | [#6](https://github.com/DolyLanguagesORG/doly-languages/issues/6) | Configuración del repositorio: main/develop, branch protection, plantillas de PR/issue y GitHub Actions (CI) | Jesús (SM) | 05 Oct 2026 | 06 Oct 2026 |
| 2 | [#7](https://github.com/DolyLanguagesORG/doly-languages/issues/7) | Setup de arquitectura NestJS, conexión a base de datos (PostgreSQL/MongoDB) y entidad User | Azael | 05 Oct 2026 | 08 Oct 2026 |
| 3 | [#8](https://github.com/DolyLanguagesORG/doly-languages/issues/8) | Setup de proyecto Next.js con Tailwind CSS, layout base y temas de la interfaz | Juan | 05 Oct 2026 | 07 Oct 2026 |
| 4 | [#9](https://github.com/DolyLanguagesORG/doly-languages/issues/9) | Servicio de hash criptográfico (bcrypt/Argon2) y estrategia de autenticación JWT en NestJS | Azael | 09 Oct 2026 | 12 Oct 2026 |
| 5 | [#10](https://github.com/DolyLanguagesORG/doly-languages/issues/10) | DTOs de validación de registro/login y endpoints de autenticación (/auth/register, /auth/login) | Elías | 09 Oct 2026 | 12 Oct 2026 |
| 6 | [#11](https://github.com/DolyLanguagesORG/doly-languages/issues/11) | Maquetado e integración de vistas de login y registro en Next.js | Juan | 08 Oct 2026 | 12 Oct 2026 |
| 7 | [#12](https://github.com/DolyLanguagesORG/doly-languages/issues/12) | Endpoints para consultar y actualizar el perfil de usuario (/user/profile) | Elías | 13 Oct 2026 | 15 Oct 2026 |
| 8 | [#13](https://github.com/DolyLanguagesORG/doly-languages/issues/13) | Vista del perfil de usuario e integración con el estado de sesión en Next.js | Juan | 13 Oct 2026 | 16 Oct 2026 |
| 9 | [#14](https://github.com/DolyLanguagesORG/doly-languages/issues/14) | Pruebas de integración del Sprint 1, corrección de bugs y revisión de PRs hacia develop | Jesús (SM) | 16 Oct 2026 | 18 Oct 2026 |

---

## Sprint 2 — Configuración de Estudio y Lecturas con IA

**Periodo:** 19/Oct – 01/Nov/2026  
**Objetivo:** Conectar el backend con la API de IA (OpenAI/Gemini) para generar lecturas según la configuración del estudiante.  
**Cierre (milestone):** [Sprint 2: Configuración de Estudio y Lecturas con IA](https://github.com/DolyLanguagesORG/doly-languages/milestone/2)  
**Tareas:** 7

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 10 | [#15](https://github.com/DolyLanguagesORG/doly-languages/issues/15) | Módulo de servicios en NestJS para integración con la API de IA (OpenAI/Gemini) y arquitectura de prompts | Azael | 19 Oct 2026 | 23 Oct 2026 |
| 11 | [#16](https://github.com/DolyLanguagesORG/doly-languages/issues/16) | Endpoints para selección y guardado de categorías e idiomas (/settings/categories, /settings/languages) | Elías | 19 Oct 2026 | 22 Oct 2026 |
| 12 | [#17](https://github.com/DolyLanguagesORG/doly-languages/issues/17) | Formulario de selección de parámetros de estudio (idioma, categoría, dificultad, longitud) en Next.js | Juan | 19 Oct 2026 | 23 Oct 2026 |
| 13 | [#18](https://github.com/DolyLanguagesORG/doly-languages/issues/18) | Servicio de caché para respuestas de lectura con parámetros equivalentes (RNF-05) | Jesús (SM) | 22 Oct 2026 | 26 Oct 2026 |
| 14 | [#19](https://github.com/DolyLanguagesORG/doly-languages/issues/19) | Visor inmersivo de lectura (diseño enfocado en la legibilidad) en Next.js | Juan | 24 Oct 2026 | 28 Oct 2026 |
| 15 | [#20](https://github.com/DolyLanguagesORG/doly-languages/issues/20) | Endpoint de generación de lectura basada en los parámetros seleccionados (/content/generate) | Azael + Elías | 24 Oct 2026 | 28 Oct 2026 |
| 16 | [#21](https://github.com/DolyLanguagesORG/doly-languages/issues/21) | Conexión del flujo completo: formulario de parámetros → generación IA → visor | Jesús (SM) + Juan | 29 Oct 2026 | 01 Nov 2026 |

---

## Sprint 3 — Vocabulario Contextual y Evaluación por PNL

**Periodo:** 02/Nov – 15/Nov/2026  
**Objetivo:** Implementar la interacción flotante de diccionario por palabra/oración (con audio) y la calificación automática de resúmenes redactados.  
**Cierre (milestone):** [Sprint 3: Vocabulario Contextual y Evaluación por PNL](https://github.com/DolyLanguagesORG/doly-languages/milestone/3)  
**Tareas:** 7

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 17 | [#22](https://github.com/DolyLanguagesORG/doly-languages/issues/22) | Captura e interacción de selección de texto dentro del visor de lectura en Next.js | Juan | 02 Nov 2026 | 05 Nov 2026 |
| 18 | [#23](https://github.com/DolyLanguagesORG/doly-languages/issues/23) | Endpoint de consulta contextual de vocabulario a la IA (significado, definición, ejemplos, oración original) | Azael | 02 Nov 2026 | 06 Nov 2026 |
| 19 | [#24](https://github.com/DolyLanguagesORG/doly-languages/issues/24) | Componente emergente (pop-up) de diccionario contextual e integración de audio corto (TTS) | Juan | 06 Nov 2026 | 09 Nov 2026 |
| 20 | [#25](https://github.com/DolyLanguagesORG/doly-languages/issues/25) | Componente de área de redacción libre de resumen y envío de evaluación en Next.js | Juan + Elías | 07 Nov 2026 | 10 Nov 2026 |
| 21 | [#26](https://github.com/DolyLanguagesORG/doly-languages/issues/26) | Servicio de evaluación y calificación por PNL en NestJS (cobertura, precisión, coherencia) con feedback | Jesús (SM) + Azael | 06 Nov 2026 | 11 Nov 2026 |
| 22 | [#27](https://github.com/DolyLanguagesORG/doly-languages/issues/27) | Endpoint de procesamiento y almacenamiento del resultado de la evaluación (/evaluation/submit) | Elías | 10 Nov 2026 | 13 Nov 2026 |
| 23 | [#28](https://github.com/DolyLanguagesORG/doly-languages/issues/28) | Pruebas del módulo de vocabulario y evaluación de resúmenes por PNL | Jesús (SM) | 13 Nov 2026 | 15 Nov 2026 |

---

## Sprint 4 — Historial, Rachas y Panel Administrativo

**Periodo:** 16/Nov – 29/Nov/2026  
**Objetivo:** Desarrollar el módulo de trazabilidad (historial y progreso), contador de racha diaria y el panel básico de administración.  
**Cierre (milestone):** [Sprint 4: Historial, Rachas y Panel Administrativo](https://github.com/DolyLanguagesORG/doly-languages/milestone/4)  
**Tareas:** 6

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 24 | [#29](https://github.com/DolyLanguagesORG/doly-languages/issues/29) | Lógica de cálculo de racha diaria (días consecutivos de actividad) y asignación de puntos en NestJS | Azael | 16 Nov 2026 | 19 Nov 2026 |
| 25 | [#30](https://github.com/DolyLanguagesORG/doly-languages/issues/30) | Endpoints de consulta de historial de actividades (lecturas, palabras consultadas, calificaciones) | Elías | 16 Nov 2026 | 20 Nov 2026 |
| 26 | [#31](https://github.com/DolyLanguagesORG/doly-languages/issues/31) | Dashboard de usuario en Next.js (métricas, contador de racha, historial y gráfica de puntos) | Juan | 19 Nov 2026 | 24 Nov 2026 |
| 27 | [#32](https://github.com/DolyLanguagesORG/doly-languages/issues/32) | Endpoints para gestión administrativa de categorías globales y supervisión de usuarios (/admin/categories) | Elías | 21 Nov 2026 | 25 Nov 2026 |
| 28 | [#33](https://github.com/DolyLanguagesORG/doly-languages/issues/33) | Vista del panel administrativo básico en Next.js | Juan + Jesús (SM) | 24 Nov 2026 | 27 Nov 2026 |
| 29 | [#34](https://github.com/DolyLanguagesORG/doly-languages/issues/34) | Revisión general de código, limpieza de endpoints y merge a develop | Jesús (SM) | 27 Nov 2026 | 29 Nov 2026 |

---

## Sprint 5 — Pruebas, Tagging v1.0.0 y Cierre del proyecto

**Periodo:** 30/Nov – 10/Dic/2026  
**Objetivo:** Congelamiento de código, ejecución de pruebas E2E, tagging de versión estable v1.0.0 y entrega académica del anteproyecto.  
**Cierre (milestone):** [Sprint 5: Pruebas, Tagging v1.0.0 y Cierre del proyecto](https://github.com/DolyLanguagesORG/doly-languages/milestone/5)  
**Tareas:** 4

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 30 | [#35](https://github.com/DolyLanguagesORG/doly-languages/issues/35) | Pruebas de usabilidad y revisión de diseño responsivo (móvil/desktop) | Juan | 30 Nov 2026 | 03 Dic 2026 |
| 31 | [#36](https://github.com/DolyLanguagesORG/doly-languages/issues/36) | Pruebas de rendimiento, manejo de errores de la API de IA (modo degradado) y validación de seguridad | Azael + Elías | 30 Nov 2026 | 04 Dic 2026 |
| 32 | [#37](https://github.com/DolyLanguagesORG/doly-languages/issues/37) | Creación del pull request final de develop hacia main, tagging v1.0.0 y verificación de CI/CD | Jesús (SM) | 04 Dic 2026 | 06 Dic 2026 |
| 33 | [#38](https://github.com/DolyLanguagesORG/doly-languages/issues/38) | Preparación de la documentación final del repositorio, capturas del sistema y presentación del proyecto | Todo el equipo | 06 Dic 2026 | 10 Dic 2026 |

---

## Correspondencia completa

| Cronograma | GitHub | Tarea | Sprint |
| --: | :---: | --- | --: |
| 1 | [#6](https://github.com/DolyLanguagesORG/doly-languages/issues/6) | Configuración del repositorio: main/develop, branch protection, plantillas de PR/issue y GitHub Actions (CI) | 1 |
| 2 | [#7](https://github.com/DolyLanguagesORG/doly-languages/issues/7) | Setup de arquitectura NestJS, conexión a base de datos (PostgreSQL/MongoDB) y entidad User | 1 |
| 3 | [#8](https://github.com/DolyLanguagesORG/doly-languages/issues/8) | Setup de proyecto Next.js con Tailwind CSS, layout base y temas de la interfaz | 1 |
| 4 | [#9](https://github.com/DolyLanguagesORG/doly-languages/issues/9) | Servicio de hash criptográfico (bcrypt/Argon2) y estrategia de autenticación JWT en NestJS | 1 |
| 5 | [#10](https://github.com/DolyLanguagesORG/doly-languages/issues/10) | DTOs de validación de registro/login y endpoints de autenticación (/auth/register, /auth/login) | 1 |
| 6 | [#11](https://github.com/DolyLanguagesORG/doly-languages/issues/11) | Maquetado e integración de vistas de login y registro en Next.js | 1 |
| 7 | [#12](https://github.com/DolyLanguagesORG/doly-languages/issues/12) | Endpoints para consultar y actualizar el perfil de usuario (/user/profile) | 1 |
| 8 | [#13](https://github.com/DolyLanguagesORG/doly-languages/issues/13) | Vista del perfil de usuario e integración con el estado de sesión en Next.js | 1 |
| 9 | [#14](https://github.com/DolyLanguagesORG/doly-languages/issues/14) | Pruebas de integración del Sprint 1, corrección de bugs y revisión de PRs hacia develop | 1 |
| 10 | [#15](https://github.com/DolyLanguagesORG/doly-languages/issues/15) | Módulo de servicios en NestJS para integración con la API de IA (OpenAI/Gemini) y arquitectura de prompts | 2 |
| 11 | [#16](https://github.com/DolyLanguagesORG/doly-languages/issues/16) | Endpoints para selección y guardado de categorías e idiomas (/settings/categories, /settings/languages) | 2 |
| 12 | [#17](https://github.com/DolyLanguagesORG/doly-languages/issues/17) | Formulario de selección de parámetros de estudio (idioma, categoría, dificultad, longitud) en Next.js | 2 |
| 13 | [#18](https://github.com/DolyLanguagesORG/doly-languages/issues/18) | Servicio de caché para respuestas de lectura con parámetros equivalentes (RNF-05) | 2 |
| 14 | [#19](https://github.com/DolyLanguagesORG/doly-languages/issues/19) | Visor inmersivo de lectura (diseño enfocado en la legibilidad) en Next.js | 2 |
| 15 | [#20](https://github.com/DolyLanguagesORG/doly-languages/issues/20) | Endpoint de generación de lectura basada en los parámetros seleccionados (/content/generate) | 2 |
| 16 | [#21](https://github.com/DolyLanguagesORG/doly-languages/issues/21) | Conexión del flujo completo: formulario de parámetros → generación IA → visor | 2 |
| 17 | [#22](https://github.com/DolyLanguagesORG/doly-languages/issues/22) | Captura e interacción de selección de texto dentro del visor de lectura en Next.js | 3 |
| 18 | [#23](https://github.com/DolyLanguagesORG/doly-languages/issues/23) | Endpoint de consulta contextual de vocabulario a la IA (significado, definición, ejemplos, oración original) | 3 |
| 19 | [#24](https://github.com/DolyLanguagesORG/doly-languages/issues/24) | Componente emergente (pop-up) de diccionario contextual e integración de audio corto (TTS) | 3 |
| 20 | [#25](https://github.com/DolyLanguagesORG/doly-languages/issues/25) | Componente de área de redacción libre de resumen y envío de evaluación en Next.js | 3 |
| 21 | [#26](https://github.com/DolyLanguagesORG/doly-languages/issues/26) | Servicio de evaluación y calificación por PNL en NestJS (cobertura, precisión, coherencia) con feedback | 3 |
| 22 | [#27](https://github.com/DolyLanguagesORG/doly-languages/issues/27) | Endpoint de procesamiento y almacenamiento del resultado de la evaluación (/evaluation/submit) | 3 |
| 23 | [#28](https://github.com/DolyLanguagesORG/doly-languages/issues/28) | Pruebas del módulo de vocabulario y evaluación de resúmenes por PNL | 3 |
| 24 | [#29](https://github.com/DolyLanguagesORG/doly-languages/issues/29) | Lógica de cálculo de racha diaria (días consecutivos de actividad) y asignación de puntos en NestJS | 4 |
| 25 | [#30](https://github.com/DolyLanguagesORG/doly-languages/issues/30) | Endpoints de consulta de historial de actividades (lecturas, palabras consultadas, calificaciones) | 4 |
| 26 | [#31](https://github.com/DolyLanguagesORG/doly-languages/issues/31) | Dashboard de usuario en Next.js (métricas, contador de racha, historial y gráfica de puntos) | 4 |
| 27 | [#32](https://github.com/DolyLanguagesORG/doly-languages/issues/32) | Endpoints para gestión administrativa de categorías globales y supervisión de usuarios (/admin/categories) | 4 |
| 28 | [#33](https://github.com/DolyLanguagesORG/doly-languages/issues/33) | Vista del panel administrativo básico en Next.js | 4 |
| 29 | [#34](https://github.com/DolyLanguagesORG/doly-languages/issues/34) | Revisión general de código, limpieza de endpoints y merge a develop | 4 |
| 30 | [#35](https://github.com/DolyLanguagesORG/doly-languages/issues/35) | Pruebas de usabilidad y revisión de diseño responsivo (móvil/desktop) | 5 |
| 31 | [#36](https://github.com/DolyLanguagesORG/doly-languages/issues/36) | Pruebas de rendimiento, manejo de errores de la API de IA (modo degradado) y validación de seguridad | 5 |
| 32 | [#37](https://github.com/DolyLanguagesORG/doly-languages/issues/37) | Creación del pull request final de develop hacia main, tagging v1.0.0 y verificación de CI/CD | 5 |
| 33 | [#38](https://github.com/DolyLanguagesORG/doly-languages/issues/38) | Preparación de la documentación final del repositorio, capturas del sistema y presentación del proyecto | 5 |

## Reglas de trabajo

Cada tarea del cronograma se entrega con un pull request:

1. La rama sigue la convención `feat/issue-<n>-<kebab>`, donde `<n>` es el
   **número de GitHub** del issue (no el número de cronograma). También se
   acepta el formato `<n>-<kebab>` que genera el botón *Create a branch*.
2. El PR va hacia `develop`, salvo el PR de release, que va hacia `main`.
3. El título del PR es un Conventional Commit **en español**; el check
   `pr-title` lo valida.
4. Se requieren 7 checks en verde y una aprobación antes de fusionar.
5. Al fusionar a `main`, el workflow `release` crea el tag y la release
   automáticamente.

El detalle completo está en [git-workflow.md](./conventions/git-workflow.md)
y [versioning.md](./conventions/versioning.md).

## Reporte diario

Cada desarrollador publica su avance al cierre de su jornada en el
[hilo de standup](https://github.com/DolyLanguagesORG/doly-languages/discussions/39),
usando la plantilla del hilo. El límite es 23:59 CST.
