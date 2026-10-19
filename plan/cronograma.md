# Cronograma de DolyNation

Este documento es la fuente de verdad escrita del cronograma. La vista
interactiva (Kanban y Timeline) vive en el [Project de GitHub](
https://github.com/orgs/DolyLanguagesORG/projects/1), y el detalle de cada
tarea en los issues del repositorio.

> **Alcance:** este cronograma cubre el **producto completo**, de principio a
> fin. El tag `v1.0.0` del Sprint 5 es la primera versión estable de ese
> producto, no una entrega parcial.

> **Repositorios:** el proyecto vive hoy en cuatro repos separados
> (`dolynation-atl-back`, `dolynation-tonatiuh-front`, `dolynation-tlalli-infra`
> y `dolynation-ehecatl-docs`). Cada tarea es un issue en el repo que le
> corresponde (el monorepo original `doly-languages` quedó archivado como
> histórico); el seguimiento actual está en el Project de la organización.

| Dato | Valor |
| --- | --- |
| Inicio del proyecto | 05/Oct/2026 |
| Entrega final | 10/Dic/2026 |
| Límite diario por tarea | 23:59 CST |
| Sprints | 5 |
| Tareas | 33 (+5 de plataforma + 3 migraciones de schema) |
| Release actual | `v0.1.0` |
| Release de cierre | `v1.0.0` |

## Dónde ver el avance

- **Kanban y Timeline**: [Project — DolyNation Plan de Desarrollo (2026)](https://github.com/orgs/DolyLanguagesORG/projects/1)
  - Vista *Tablero Kanban*: agrupada por `Status` (Todo / In Progress / In Review / Done)
  - Vista *Timeline del producto*: eje de tiempo con `Start Date` → `Target Date`
  - Vista *Todos los entregables*: tabla con todas las tareas
- **Issues**: 33 entregables (uno por tarea) repartidos entre los cuatro repos;
  en la tabla enlazada cada uno se marca con su repo, p. ej. `back#2`
- **Milestones**: un milestone por sprint, replicado en cada repo (misma fecha
  de cierre en los cuatro)
- **Standup diario**: [hilo de registro de avances](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/discussions/1)

## Cómo leer los números

En este documento las tareas se numeran del **1 al 33**, como en el
cronograma original. Al repartir el monorepo en cuatro repos, cada issue
recibió además el número que le tocó en su repo destino; por eso en las tablas
cada issue se identifica con su repo y su número, por ejemplo `back#2`
(`dolynation-atl-back`, issue #2).

Referencias de repo: `back` = `dolynation-atl-back`, `front` =
`dolynation-tonatiuh-front`, `infra` = `dolynation-tlalli-infra`, `docs` =
`dolynation-ehecatl-docs`.

---

## Sprint 1 — Infraestructura, Autenticación y Perfil

**Periodo:** 05/Oct – 18/Oct/2026  
**Objetivo:** Configuración inicial del repositorio con reglas CI/CD, modelo de base de datos y módulo funcional de autenticación y perfil.  
**Cierre (milestone):** Sprint 1: Infraestructura, Autenticación y Perfil — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/1) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/1) · [infra](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/milestone/1)  
**Tareas:** 9

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 1 | [infra#2](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/2) | Configuración del repositorio: main/develop, branch protection, plantillas de PR/issue y GitHub Actions (CI) | Jesús (SM) | 05 Oct 2026 | 06 Oct 2026 |
| 2 | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2) | Setup de arquitectura NestJS, conexión a PostgreSQL (Drizzle ORM) y entidad User | Azael | 05 Oct 2026 | 08 Oct 2026 |
| 3 | [front#2](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/2) | Setup de proyecto Next.js con Tailwind CSS, layout base y temas de la interfaz | Juan | 05 Oct 2026 | 07 Oct 2026 |
| 4 | [back#3](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/3) | Servicio de hash criptográfico (Argon2id) y estrategia de autenticación JWT en NestJS | Azael | 09 Oct 2026 | 12 Oct 2026 |
| 5 | [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) | DTOs y endpoints de autenticación (/auth/register, /login, /refresh, /logout, /me) | Elías | 09 Oct 2026 | 12 Oct 2026 |
| 6 | [front#3](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/3) | Maquetado e integración de vistas de login y registro en Next.js | Juan | 08 Oct 2026 | 12 Oct 2026 |
| 7 | [back#5](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/5) | Endpoints para consultar y actualizar el perfil de usuario (/user/profile) | Elías | 13 Oct 2026 | 15 Oct 2026 |
| 8 | [front#4](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/4) | Vista del perfil de usuario e integración con el estado de sesión en Next.js | Juan | 13 Oct 2026 | 16 Oct 2026 |
| 9 | [back#6](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/6) | Pruebas de integración del Sprint 1, corrección de bugs y revisión de PRs hacia develop | Jesús (SM) | 16 Oct 2026 | 18 Oct 2026 |

---

## Sprint 2 — Configuración de Estudio y Lecturas con IA

**Periodo:** 19/Oct – 01/Nov/2026  
**Objetivo:** Conectar el backend con la API de IA (MiniMax-M3 adaptable) para generar lecturas según la configuración del estudiante.  
**Cierre (milestone):** Sprint 2: Configuración de Estudio y Lecturas con IA — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/2) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/2)  
**Tareas:** 7

**Prerrequisito de schema:** [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) — preferencias, categorías, idioma y `prompt_hash`.

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 10 | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7) | Módulo de servicios en NestJS para integración con MiniMax-M3 (adaptable) y arquitectura de prompts | Azael | 19 Oct 2026 | 23 Oct 2026 |
| 11 | [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8) | Endpoints para selección y guardado de categorías e idiomas (/settings/categories, /settings/languages) | Elías | 19 Oct 2026 | 22 Oct 2026 |
| 12 | [front#5](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/5) | Formulario de selección de parámetros de estudio (idioma, categoría, dificultad, longitud) en Next.js | Juan | 19 Oct 2026 | 23 Oct 2026 |
| 13 | [back#9](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9) | Servicio de caché para respuestas de lectura con parámetros equivalentes (RNF-04) | Jesús (SM) | 22 Oct 2026 | 26 Oct 2026 |
| 14 | [front#6](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/6) | Visor inmersivo de lectura (diseño enfocado en la legibilidad) en Next.js | Juan | 24 Oct 2026 | 28 Oct 2026 |
| 15 | [back#10](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/10) | Endpoint de generación de lectura (POST /readings) basado en parámetros | Azael + Elías | 24 Oct 2026 | 28 Oct 2026 |
| 16 | [front#7](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/7) | Conexión del flujo completo: formulario de parámetros → generación IA → visor | Jesús (SM) + Juan | 29 Oct 2026 | 01 Nov 2026 |

---

## Sprint 3 — Vocabulario Contextual y Evaluación por PNL

**Periodo:** 02/Nov – 15/Nov/2026  
**Objetivo:** Implementar la interacción flotante de diccionario por palabra/oración (con audio) y la calificación automática de resúmenes redactados.  
**Cierre (milestone):** Sprint 3: Vocabulario Contextual y Evaluación por PNL — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/3) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/3)  
**Tareas:** 7

**Prerrequisito de schema:** [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) — `evaluations` y `vocabulary_logs`.

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 17 | [front#8](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/8) | Captura e interacción de selección de texto dentro del visor de lectura en Next.js | Juan | 02 Nov 2026 | 05 Nov 2026 |
| 18 | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11) | Endpoint de vocabulario contextual (significado, definición, ejemplos, oración original) y TTS | Azael | 02 Nov 2026 | 06 Nov 2026 |
| 19 | [front#9](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/9) | Componente emergente (pop-up) de diccionario contextual e integración de audio corto (TTS) | Juan | 06 Nov 2026 | 09 Nov 2026 |
| 20 | [front#10](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/10) | Componente de área de redacción libre de resumen y envío de evaluación en Next.js | Juan + Elías | 07 Nov 2026 | 10 Nov 2026 |
| 21 | [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12) | Servicio de evaluación y calificación por PNL en NestJS (cobertura, precisión, coherencia) con feedback | Jesús (SM) + Azael | 06 Nov 2026 | 11 Nov 2026 |
| 22 | [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) | Endpoint de evaluación de resumen (POST /readings/{id}/evaluate) | Elías | 10 Nov 2026 | 13 Nov 2026 |
| 23 | [back#14](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/14) | Pruebas del módulo de vocabulario y evaluación de resúmenes por PNL | Jesús (SM) | 13 Nov 2026 | 15 Nov 2026 |

---

## Sprint 4 — Historial, Rachas y Panel Administrativo

**Periodo:** 16/Nov – 29/Nov/2026  
**Objetivo:** Desarrollar el módulo de trazabilidad (historial y progreso), contador de racha diaria y el panel básico de administración.  
**Cierre (milestone):** Sprint 4: Historial, Rachas y Panel Administrativo — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/4) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/4)  
**Tareas:** 6

**Prerrequisito de schema:** [infra#22](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/22) — rol `STUDENT`/`ADMIN` en `users`.

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 24 | [back#15](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/15) | Lógica de cálculo de racha diaria (días consecutivos de actividad) y asignación de puntos en NestJS | Azael | 16 Nov 2026 | 19 Nov 2026 |
| 25 | [back#16](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/16) | Endpoints de consulta de historial de actividades (lecturas, palabras consultadas, calificaciones) | Elías | 16 Nov 2026 | 20 Nov 2026 |
| 26 | [front#11](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/11) | Dashboard de usuario en Next.js (métricas, contador de racha, historial y gráfica de puntos) | Juan | 19 Nov 2026 | 24 Nov 2026 |
| 27 | [back#17](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/17) | Endpoints admin de categorías globales y usuarios (/admin/categories, /admin/users) | Elías | 21 Nov 2026 | 25 Nov 2026 |
| 28 | [front#12](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/12) | Vista del panel administrativo básico en Next.js | Juan + Jesús (SM) | 24 Nov 2026 | 27 Nov 2026 |
| 29 | [infra#3](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/3) | Revisión general de código, limpieza de endpoints y merge a develop | Jesús (SM) | 27 Nov 2026 | 29 Nov 2026 |

---

## Sprint 5 — Pruebas, Tagging v1.0.0 y Cierre del proyecto

**Periodo:** 30/Nov – 10/Dic/2026  
**Objetivo:** Congelamiento de código, ejecución de pruebas E2E, tagging de versión estable v1.0.0 y entrega académica del anteproyecto.  
**Cierre (milestone):** Sprint 5: Pruebas, Tagging v1.0.0 y Cierre del proyecto — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/5) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/5) · [infra](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/milestone/5) · [docs](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/milestone/5)  
**Tareas:** 4

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | --- | :---: | :---: |
| 30 | [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13) | Pruebas de usabilidad y revisión de diseño responsivo (móvil/desktop) | Juan | 30 Nov 2026 | 03 Dic 2026 |
| 31 | [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18) | Pruebas de rendimiento, manejo de errores de la API de IA (modo degradado) y validación de seguridad | Azael + Elías | 30 Nov 2026 | 04 Dic 2026 |
| 32 | [infra#4](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/4) | Creación del pull request final de develop hacia main, tagging v1.0.0 y verificación de CI/CD | Jesús (SM) | 04 Dic 2026 | 06 Dic 2026 |
| 33 | [docs#3](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/3) | Preparación de la documentación final del repositorio, capturas del sistema y presentación del proyecto | Todo el equipo | 06 Dic 2026 | 10 Dic 2026 |

---

## Correspondencia completa

| Cronograma | GitHub | Tarea | Sprint |
| --: | :---: | --- | --: |
| 1 | [infra#2](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/2) | Configuración del repositorio: main/develop, branch protection, plantillas de PR/issue y GitHub Actions (CI) | 1 |
| 2 | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2) | Setup de arquitectura NestJS, conexión a PostgreSQL (Drizzle ORM) y entidad User | 1 |
| 3 | [front#2](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/2) | Setup de proyecto Next.js con Tailwind CSS, layout base y temas de la interfaz | 1 |
| 4 | [back#3](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/3) | Servicio de hash criptográfico (Argon2id) y estrategia de autenticación JWT en NestJS | 1 |
| 5 | [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) | DTOs y endpoints de autenticación (/auth/register, /login, /refresh, /logout, /me) | 1 |
| 6 | [front#3](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/3) | Maquetado e integración de vistas de login y registro en Next.js | 1 |
| 7 | [back#5](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/5) | Endpoints para consultar y actualizar el perfil de usuario (/user/profile) | 1 |
| 8 | [front#4](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/4) | Vista del perfil de usuario e integración con el estado de sesión en Next.js | 1 |
| 9 | [back#6](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/6) | Pruebas de integración del Sprint 1, corrección de bugs y revisión de PRs hacia develop | 1 |
| 10 | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7) | Módulo de servicios en NestJS para integración con MiniMax-M3 (adaptable) y arquitectura de prompts | 2 |
| 11 | [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8) | Endpoints para selección y guardado de categorías e idiomas (/settings/categories, /settings/languages) | 2 |
| 12 | [front#5](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/5) | Formulario de selección de parámetros de estudio (idioma, categoría, dificultad, longitud) en Next.js | 2 |
| 13 | [back#9](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9) | Servicio de caché para respuestas de lectura con parámetros equivalentes (RNF-04) | 2 |
| 14 | [front#6](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/6) | Visor inmersivo de lectura (diseño enfocado en la legibilidad) en Next.js | 2 |
| 15 | [back#10](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/10) | Endpoint de generación de lectura (POST /readings) basado en parámetros | 2 |
| 16 | [front#7](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/7) | Conexión del flujo completo: formulario de parámetros → generación IA → visor | 2 |
| 17 | [front#8](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/8) | Captura e interacción de selección de texto dentro del visor de lectura en Next.js | 3 |
| 18 | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11) | Endpoint de vocabulario contextual (significado, definición, ejemplos, oración original) y TTS | 3 |
| 19 | [front#9](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/9) | Componente emergente (pop-up) de diccionario contextual e integración de audio corto (TTS) | 3 |
| 20 | [front#10](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/10) | Componente de área de redacción libre de resumen y envío de evaluación en Next.js | 3 |
| 21 | [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12) | Servicio de evaluación y calificación por PNL en NestJS (cobertura, precisión, coherencia) con feedback | 3 |
| 22 | [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) | Endpoint de evaluación de resumen (POST /readings/{id}/evaluate) | 3 |
| 23 | [back#14](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/14) | Pruebas del módulo de vocabulario y evaluación de resúmenes por PNL | 3 |
| 24 | [back#15](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/15) | Lógica de cálculo de racha diaria (días consecutivos de actividad) y asignación de puntos en NestJS | 4 |
| 25 | [back#16](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/16) | Endpoints de consulta de historial de actividades (lecturas, palabras consultadas, calificaciones) | 4 |
| 26 | [front#11](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/11) | Dashboard de usuario en Next.js (métricas, contador de racha, historial y gráfica de puntos) | 4 |
| 27 | [back#17](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/17) | Endpoints admin de categorías globales y usuarios (/admin/categories, /admin/users) | 4 |
| 28 | [front#12](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/12) | Vista del panel administrativo básico en Next.js | 4 |
| 29 | [infra#3](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/3) | Revisión general de código, limpieza de endpoints y merge a develop | 4 |
| 30 | [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13) | Pruebas de usabilidad y revisión de diseño responsivo (móvil/desktop) | 5 |
| 31 | [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18) | Pruebas de rendimiento, manejo de errores de la API de IA (modo degradado) y validación de seguridad | 5 |
| 32 | [infra#4](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/4) | Creación del pull request final de develop hacia main, tagging v1.0.0 y verificación de CI/CD | 5 |
| 33 | [docs#3](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/3) | Preparación de la documentación final del repositorio, capturas del sistema y presentación del proyecto | 5 |

## Tareas adicionales de plataforma

Además de las 33 tareas del producto, el equipo de infraestructura mantiene
cinco tareas de habilitación (todas en `dolynation-tlalli-infra`, con label
`area:infra`) que cierran el pipeline descrito en
[CI-CD-Y-VERSIONADO.md](../operations/CI-CD-Y-VERSIONADO.md)

| # | Issue | Tarea | Sprint |
| --: | :---: | --- | --: |
| P1 | [infra#5](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/5) | Repositorio `.github` de la organización (plantillas y workflows reutilizables) | 1 |
| P2 | [infra#6](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/6) | Entornos (dev/staging/prod), secretos y acceso SSH | 1 |
| P3 | [infra#7](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/7) | Versionado con release-please, `versions.yml` y guard single-flight de `rc` | 5 |
| P4 | [infra#8](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/8) | Cascada de releases y deploy a staging desde `rc` con PAT | 5 |
| P5 | [infra#9](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/9) | Auditoría de seguridad: dependencias, secretos y protección de ramas | 5 |

El árbol `infra#10-#17` se fusionó en P2-P5 e `infra#4`; los issues quedaron cerrados como duplicados.

## Prerrequisitos de schema

Estas tareas no suman a las 33 del producto, pero bloquean backend y se rastrean en el mismo Project:

| Issue | Qué habilita | Bloquea |
| :---: | --- | --- |
| [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) | `user_preferences`, `user_selected_categories`, `categories`, `readings.language`, `length_type` y `prompt_hash` | `back#8`, `back#9`, `back#10` |
| [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) | `evaluations` y `vocabulary_logs` | `back#11`, `back#13`, `back#16` |
| [infra#22](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/22) | `users.role` (`STUDENT`/`ADMIN`) | `back#17` |

Cada migración sigue la regla de dos fases: actualizar `01-init.sql` y agregar un script en `database/postgres/updates/`.

## Reglas de trabajo

Cada tarea del cronograma se entrega con un pull request:

1. La rama sigue la convención `tipo/issue-<n>-<módulo>-<detalle>`, donde
   `<n>` es el **número del issue en su repo** (no el número de cronograma).
   Ejemplo: `feat/issue-12-auth-login-page`. También se acepta el formato
   `<n>-<detalle>` que genera el botón *Create a branch* del issue.
2. El PR va hacia `develop`. El PR de release de `release-please` también
   apunta a `develop`; el promote a `main` (producción) es un PR aparte.
3. El título del PR es un Conventional Commit **en español**; el check
   `pr-title` lo valida.
4. Se requieren los checks del repo en verde (ver
   [FLUJO-DE-TRABAJO.md](../operations/FLUJO-DE-TRABAJO.md)) y una aprobación antes de
   fusionar.
5. Al mergear el PR de release, `release-please` crea el tag y la release
   automáticamente.

El detalle completo está en [git-workflow.md](../conventions/git-workflow.md)
y [versioning.md](../conventions/versioning.md).

## Reporte diario

Cada desarrollador publica su avance al cierre de su jornada en el
[hilo de standup](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/discussions/1),
usando la plantilla del hilo. El límite es 23:59 CST.

El **orden de trabajo** (qué tarea depende de cuál), los **checklists para no
perder fechas** y el **monitoreo del SM** están en
[PLAN-Y-SEGUIMIENTO.md](./PLAN-Y-SEGUIMIENTO.md).
