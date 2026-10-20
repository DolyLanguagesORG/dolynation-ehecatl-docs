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
| Issues | 68 abiertas (33 entregables + 12 sub-issues + 3 de plataforma + 3 migraciones + 17 de saneamiento) |
| Release actual | `v0.1.0` |
| Release de cierre | `v1.0.0` |

## Dónde ver el avance

- **Kanban y Timeline**: [Project — DolyNation Plan de Desarrollo (2026)](https://github.com/orgs/DolyLanguagesORG/projects/1)
  - Vista *Tablero Kanban*: agrupada por `Status` (Todo / In Progress / In Review / Done)
  - Vista *Timeline del producto*: eje de tiempo con `Start Date` → `Target Date`
  - Vista *Todos los entregables*: tabla con todas las tareas
- **Issues**: 68 issues repartidos entre los cuatro repos; en la tabla
  enlazada cada uno se marca con su repo, p. ej. `back#2`
- **Milestones**: un milestone por sprint, replicado en cada repo (misma fecha
  de cierre en los cuatro)
- **Standup diario**: [hilo de registro de avances](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/discussions/1)

## Cómo leer los números

En este documento las tareas se numeran del **1 al 68**, en el orden en que
se entregan. Al repartir el monorepo en cuatro repos, cada issue recibió
además el número que le tocó en su repo destino; por eso en las tablas cada
issue se identifica con su repo y su número, por ejemplo `back#2`
(`dolynation-atl-back`, issue #2).

Referencias de repo: `back` = `dolynation-atl-back`, `front` =
`dolynation-tonatiuh-front`, `infra` = `dolynation-tlalli-infra`, `docs` =
`dolynation-ehecatl-docs`.

---

## Sprint 1 — Configuración del repositorio y cimientos

**Periodo:** 05 al 18 de octubre de 2026  
**Objetivo:** Dejar el proyecto listo para desarrollar: cuatro repositorios separados, reglas de protección, CI/CD, plantillas, skills, documentación saneada y el contrato de la API alineado al código. **Sprint cerrado con retraso: el trabajo se completó el 19 de octubre de 2026.**  
**Cierre (milestone):** Sprint 1: Infraestructura, Autenticación y Perfil — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/1) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/1) · [infra](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/milestone/1)  
**Tareas:** 8

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | :---: | :---: | :---: |
| 1 | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2) | Setup de arquitectura NestJS, conexión a PostgreSQL (Drizzle ORM) y entidad User | Azael | 5 Oct 2026 2026 | 8 Oct 2026 2026 |
| 2 | [back#3](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/3) | Servicio de hash criptográfico (Argon2id) y estrategia de autenticación JWT en NestJS | Azael | 9 Oct 2026 2026 | 12 Oct 2026 2026 |
| 3 | [docs#6](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/6) | docs(repo): onboarding de Elías, CODEOWNERS y reglas de revisión | Sebastián | 12 Oct 2026 2026 | 15 Oct 2026 2026 |
| 4 | [docs#11](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/11) | Sanear el anteproyecto: corregir contradicciones con el código y desajustes de formato | Jesús | 19 Oct 2026 2026 | 19 Oct 2026 2026 |
| 5 | [docs#12](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/12) | Revisar los diagramas y corregir los que contradicen el código | Jesús | 19 Oct 2026 2026 | 20 Oct 2026 2026 |
| 6 | [docs#13](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/13) | Completar el registro de decisiones (ADR) y documentar las decisiones pendientes | Jesús | 20 Oct 2026 2026 | 20 Oct 2026 2026 |
| 7 | [docs#14](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/14) | Unificar el contrato API y alinear las convenciones al código real | Jesús | 20 Oct 2026 2026 | 20 Oct 2026 2026 |
| 8 | [docs#15](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/15) | Saneamiento de la configuración de GitHub: milestones, tablero, rulesets e higiene de los repos | Jesús | 20 Oct 2026 2026 | 20 Oct 2026 2026 |

---

## Sprint 2 — Fundamentos: autenticación, perfil y base del frontend

**Periodo:** 19 de octubre al 01 de noviembre de 2026  
**Objetivo:** Cimientos del producto: autenticación completa con refresh rotado, perfil de usuario, base del frontend (layout, tokens, i18n, sistema de diseño y base de pruebas) y base de infraestructura (entornos, secretos y runner de migraciones).  
**Cierre (milestone):** Sprint 2: Configuración de Estudio y Lecturas con IA — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/2) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/2)  
**Tareas:** 17

**Prerrequisito de schema:** [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) — preferencias, categorías, idioma y `prompt_hash`.

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | :---: | :---: | :---: |
| 1 | [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) | DTOs de validación y endpoints de autenticación (/auth/register, /auth/login, /auth/refresh, /auth/logout, /auth/me) | Azael | 19 Oct 2026 2026 | 21 Oct 2026 2026 |
| 2 | [front#2](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/2) | Setup de proyecto Next.js con Tailwind CSS, layout base y temas de la interfaz | Juan | 19 Oct 2026 2026 | 24 Oct 2026 2026 |
| 3 | [infra#24](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/24) | Runner de migraciones con tabla schema_migrations | Jesús | 19 Oct 2026 2026 | 21 Oct 2026 2026 |
| 4 | [back#19](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/19) | Cliente IA: adaptador MiniMax-M3 configurable (interfaz para otros proveedores) | Elías | 21 Oct 2026 2026 | 22 Oct 2026 2026 |
| 5 | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7) | Módulo de servicios en NestJS para integración con la API de IA (MiniMax-M3) y arquitectura de prompts | Azael | 22 Oct 2026 2026 | 24 Oct 2026 2026 |
| 6 | [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) | Migración S2: preferencias, categorías, idioma y caché de lecturas | Jesús | 22 Oct 2026 2026 | 24 Oct 2026 2026 |
| 7 | [back#5](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/5) | Endpoints para consultar y actualizar el perfil de usuario (/user/profile) | Elías | 23 Oct 2026 2026 | 25 Oct 2026 2026 |
| 8 | [back#20](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/20) | Arquitectura de prompts versionados por idioma, categoría, dificultad y longitud | Azael | 25 Oct 2026 2026 | 27 Oct 2026 2026 |
| 9 | [front#22](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/22) | Base de i18n con next-intl y diccionarios en inglés, francés, español e italiano | Juan | 25 Oct 2026 2026 | 26 Oct 2026 2026 |
| 10 | [infra#6](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/6) | Definir entornos (dev/staging/prod), secretos y acceso SSH | Jesús | 25 Oct 2026 2026 | 26 Oct 2026 2026 |
| 11 | [back#6](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/6) | Pruebas de integración del Sprint 1, corrección de bugs y revisión de PRs hacia develop | Elías + Sebastián | 26 Oct 2026 2026 | 28 Oct 2026 2026 |
| 12 | [front#24](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/24) | Sistema de diseño: tokens de marca, componentes base y Flowbite | Juan | 27 Oct 2026 2026 | 29 Oct 2026 2026 |
| 13 | [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8) | Endpoints para selección y guardado de categorías e idiomas (/settings/categories, /settings/languages) | Azael | 28 Oct 2026 2026 | 30 Oct 2026 2026 |
| 14 | [back#46](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/46) | /health/ready debe validar la conexión real con PostgreSQL | Elías | 29 Oct 2026 2026 | 29 Oct 2026 2026 |
| 15 | [back#47](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/47) | Separar test:unit de test:e2e para que npm run verify no exija base de datos | Elías | 30 Oct 2026 2026 | 30 Oct 2026 2026 |
| 16 | [front#3](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/3) | Maquetado e integración de vistas de login y registro en Next.js | Juan | 30 Oct 2026 2026 | 1 Nov 2026 2026 |
| 17 | [back#41](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/41) | Verificar y completar la documentación OpenAPI/Scalar del Sprint 1 | Azael | 31 Oct 2026 2026 | 31 Oct 2026 2026 |

---

## Sprint 3 — Lecturas con IA

**Periodo:** 02 al 15 de noviembre de 2026  
**Objetivo:** Generación de lecturas con IA: caché por `prompt_hash`, prompts versionados por idioma, categorías e idiomas, visor de lectura y flujo completo formulario → IA → visor. Incluye el adaptador de TTS con MiniMax y la protección contra prompt injection.  
**Cierre (milestone):** Sprint 3: Vocabulario Contextual y Evaluación por PNL — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/3) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/3)  
**Tareas:** 10

**Prerrequisito de schema:** [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) — `evaluations` y `vocabulary_logs`.

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | :---: | :---: | :---: |
| 1 | [back#9](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9) | Servicio de caché para respuestas de lectura con parámetros equivalentes (RNF-04) | Elías | 2 Nov 2026 2026 | 4 Nov 2026 2026 |
| 2 | [front#4](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/4) | Vista del perfil de usuario e integración con el estado de sesión en Next.js | Juan | 2 Nov 2026 2026 | 3 Nov 2026 2026 |
| 3 | [front#5](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/5) | Formulario de selección de parámetros de estudio (idioma, categoría, dificultad, longitud) en Next.js | Juan | 4 Nov 2026 2026 | 6 Nov 2026 2026 |
| 4 | [back#21](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/21) | Manejo de errores, timeouts y modo degradado del proveedor IA (implementación) | Azael | 5 Nov 2026 2026 | 6 Nov 2026 2026 |
| 5 | [back#43](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/43) | Adaptador de TTS con MiniMax y sus variables de entorno | Azael | 7 Nov 2026 2026 | 8 Nov 2026 2026 |
| 6 | [front#6](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/6) | Visor inmersivo de lectura (diseño enfocado en la legibilidad) en Next.js | Juan | 7 Nov 2026 2026 | 10 Nov 2026 2026 |
| 7 | [back#10](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/10) | Endpoint de generación de lectura (POST /readings) basado en parámetros | Elías + Azael | 9 Nov 2026 2026 | 11 Nov 2026 2026 |
| 8 | [back#45](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/45) | Protección contra prompt injection en generación y evaluación | Azael | 12 Nov 2026 2026 | 13 Nov 2026 2026 |
| 9 | [front#7](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/7) | Conexión del flujo completo: formulario de parámetros → generación IA → visor | Elías + Sebastián + Juan | 12 Nov 2026 2026 | 14 Nov 2026 2026 |
| 10 | [front#23](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/23) | Base de pruebas del frontend: Vitest, Playwright y jobs de CI | Juan | 15 Nov 2026 2026 | 15 Nov 2026 2026 |

---

## Sprint 4 — Vocabulario, TTS, evaluación y progreso

**Periodo:** 16 al 29 de noviembre de 2026  
**Objetivo:** Vocabulario contextual con audio, motor de evaluación por PNL (cobertura, precisión, coherencia y feedback), racha, puntos, historial y dashboard. Cierra con el endurecimiento de producción y el pipeline de despliegue.  
**Cierre (milestone):** Sprint 4: Historial, Rachas y Panel Administrativo — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/4) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/4)  
**Tareas:** 17

**Prerrequisito de schema:** [infra#22](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/22) — rol `STUDENT`/`ADMIN` en `users`.

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | :---: | :---: | :---: |
| 1 | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11) | Endpoint de vocabulario contextual (significado, definición, ejemplos, oración original) y TTS | Azael | 16 Nov 2026 2026 | 17 Nov 2026 2026 |
| 2 | [front#8](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/8) | Captura e interacción de selección de texto dentro del visor de lectura en Next.js | Juan | 16 Nov 2026 2026 | 18 Nov 2026 2026 |
| 3 | [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) | Migración S3: evaluaciones y vocabulario contextual | Jesús | 16 Nov 2026 2026 | 18 Nov 2026 2026 |
| 4 | [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12) | Servicio de evaluación y calificación por PNL en NestJS (cobertura, precisión, coherencia) con feedback | Azael | 18 Nov 2026 2026 | 20 Nov 2026 2026 |
| 5 | [infra#22](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/22) | Migración S4: rol de administrador en users | Jesús | 19 Nov 2026 2026 | 20 Nov 2026 2026 |
| 6 | [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) | Endpoint de evaluación de resumen (POST /readings/{id}/evaluate) | Azael | 21 Nov 2026 2026 | 22 Nov 2026 2026 |
| 7 | [infra#26](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/26) | Endurecer docker-compose.prod.yml: red interna, healthchecks, proxy TLS y límites | Jesús | 21 Nov 2026 2026 | 23 Nov 2026 2026 |
| 8 | [back#17](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/17) | Endpoints administrativos de categorías globales y supervisión de usuarios (/admin/categories, /admin/users) | Elías | 23 Nov 2026 2026 | 24 Nov 2026 2026 |
| 9 | [back#22](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/22) | Motor de puntuación por cobertura y precisión semántica | Azael | 23 Nov 2026 2026 | 24 Nov 2026 2026 |
| 10 | [front#10](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/10) | Componente de área de redacción libre de resumen y envío de evaluación en Next.js | Elías + Sebastián + Juan | 23 Nov 2026 2026 | 25 Nov 2026 2026 |
| 11 | [infra#27](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/27) | Pipeline de build de imágenes y despliegue por SHA con rollback | Jesús | 24 Nov 2026 2026 | 26 Nov 2026 2026 |
| 12 | [back#15](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/15) | Lógica de cálculo de racha diaria (días consecutivos de actividad) y asignación de puntos en NestJS | Elías | 25 Nov 2026 2026 | 26 Nov 2026 2026 |
| 13 | [back#23](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/23) | Cálculo de coherencia y construcción del feedback | Elías | 25 Nov 2026 2026 | 25 Nov 2026 2026 |
| 14 | [back#44](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/44) | Endpoint de TTS: audio corto de palabra o frase seleccionada | Azael | 26 Nov 2026 2026 | 27 Nov 2026 2026 |
| 15 | [front#12](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/12) | Vista del panel administrativo básico en Next.js | Elías + Sebastián + Juan | 26 Nov 2026 2026 | 27 Nov 2026 2026 |
| 16 | [back#16](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/16) | Endpoints de consulta de historial de actividades (lecturas, palabras consultadas, calificaciones) | Elías | 27 Nov 2026 2026 | 28 Nov 2026 2026 |
| 17 | [front#9](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/9) | Componente emergente (pop-up) de diccionario contextual e integración de audio corto (TTS) | Juan | 28 Nov 2026 2026 | 29 Nov 2026 2026 |

---

## Sprint 5 — Calidad, integración y release v1.0.0

**Periodo:** 30 de noviembre al 06 de diciembre de 2026 (desarrollo) y del 07 al 10 de diciembre (entrega)  
**Objetivo:** Calidad e integración: panel administrativo, auditoría de seguridad, pruebas de carga y modo degradado, revisión general, **release v1.0.0 (07-dic), documentación final y presentación (08-10 dic)**.  
**Cierre (milestone):** Sprint 5: Pruebas, Tagging v1.0.0 y Cierre del proyecto — [back](https://github.com/DolyLanguagesORG/dolynation-atl-back/milestone/5) · [front](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/milestone/5) · [infra](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/milestone/5) · [docs](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/milestone/5)  
**Tareas:** 16

| # | Issue | Tarea | Responsable | Inicio | Entrega |
| --: | :---: | --- | :---: | :---: | :---: |
| 1 | [back#14](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/14) | Pruebas del módulo de vocabulario y evaluación de resúmenes por PNL | Elías + Sebastián | 30 Nov 2026 2026 | 1 Dic 2026 2026 |
| 2 | [infra#9](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/9) | Auditoría de seguridad: dependencias, secretos y protección de ramas | Sebastián + Jesús | 30 Nov 2026 2026 | 1 Dic 2026 2026 |
| 3 | [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18) | Pruebas de rendimiento, manejo de errores de la API de IA (modo degradado) y validación de seguridad | Elías + Sebastián | 2 Dic 2026 2026 | 3 Dic 2026 2026 |
| 4 | [back#24](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/24) | Pruebas unitarias del motor de evaluación PNL | Elías + Sebastián | 2 Dic 2026 2026 | 2 Dic 2026 2026 |
| 5 | [front#11](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/11) | Dashboard de usuario en Next.js (métricas, contador de racha, historial y gráfica de puntos) | Juan | 2 Dic 2026 2026 | 3 Dic 2026 2026 |
| 6 | [infra#25](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/25) | Test de paridad entre el schema de Drizzle y el SQL de PostgreSQL | Jesús | 2 Dic 2026 2026 | 2 Dic 2026 2026 |
| 7 | [back#27](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/27) | Validación de seguridad (auth, validación de entrada, rate limiting) | Elías + Sebastián | 4 Dic 2026 2026 | 5 Dic 2026 2026 |
| 8 | [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13) | Pruebas de usabilidad y revisión de diseño responsivo (móvil/desktop) | Sebastián + Juan | 4 Dic 2026 2026 | 4 Dic 2026 2026 |
| 9 | [front#14](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/14) | Tarjetas de métricas y contador de racha en el dashboard | Juan | 4 Dic 2026 2026 | 4 Dic 2026 2026 |
| 10 | [infra#3](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/3) | Revisión general de código, limpieza de endpoints y merge a develop | Sebastián + Jesús | 4 Dic 2026 2026 | 5 Dic 2026 2026 |
| 11 | [front#15](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/15) | Gráfica de puntos por día | Juan | 5 Dic 2026 2026 | 5 Dic 2026 2026 |
| 12 | [back#25](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/25) | Pruebas de carga y latencia de endpoints críticos | Elías + Jesús | 6 Dic 2026 2026 | 6 Dic 2026 2026 |
| 13 | [back#26](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/26) | Verificación E2E del modo degradado ante fallos de la API de IA | Elías + Azael | 6 Dic 2026 2026 | 6 Dic 2026 2026 |
| 14 | [front#16](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/16) | Tabla de historial de actividad con paginación | Juan | 6 Dic 2026 2026 | 6 Dic 2026 2026 |
| 15 | [infra#4](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/4) | Creación del pull request final de develop hacia main, tagging v1.0.0 y verificación de CI/CD | Sebastián + Jesús | 7 Dic 2026 2026 | 7 Dic 2026 2026 |
| 16 | [docs#3](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/3) | Preparación de la documentación final del repositorio, capturas del sistema y presentación del proyecto | Sebastián | 8 Dic 2026 2026 | 10 Dic 2026 2026 |

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

Además de los 33 entregables del producto, el equipo de infraestructura
mantiene cinco tareas de habilitación (todas en `dolynation-tlalli-infra`, con
label `area:infra`) que cierran el pipeline descrito en
[CI-CD-Y-VERSIONADO.md](../operations/CI-CD-Y-VERSIONADO.md)

| # | Issue | Tarea | Sprint |
| --: | :---: | --- | --: |
| P1 | [infra#5](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/5) | Repositorio `.github` de la organización (plantillas y workflows reutilizables) | 1 |
| P2 | [infra#6](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/6) | Entornos (dev/staging/prod), secretos y acceso SSH | 1 |
| P5 | [infra#9](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/9) | Auditoría de seguridad: dependencias, secretos y protección de ramas | 5 |

El árbol `infra#10-#17` se fusionó en P2-P5 e `infra#4`; los issues quedaron cerrados como duplicados.

**P3 y P4 quedan fuera de la entrega** (1-10 dic 2026): el cierre usa el tag
manual `v1.0.0` de `release.yml` y el despliegue por SHA con rollback
(`infra#27`). Ambos issues siguen abiertos y visibles en el milestone
«Fuera de alcance (post-entrega)».

## Prerrequisitos de schema

Estas tareas no suman a los entregables del producto, pero bloquean backend y
se rastrean en el mismo Project:

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
2. El PR va hacia `develop`; el promote a `main` (producción) es un PR aparte.
   Al llegar a `main`, el workflow `release.yml` crea el tag y la release.
3. El título del PR es un Conventional Commit **en español**; el check
   `pr-title` lo valida.
4. Se requieren los checks del repo en verde (ver
   [FLUJO-DE-TRABAJO.md](../operations/FLUJO-DE-TRABAJO.md)) y una aprobación antes de
   fusionar.
5. Al mergear a `main`, `release.yml` calcula la versión, crea el tag anotado
   y publica la GitHub Release automáticamente.

El detalle completo está en [git-workflow.md](../conventions/git-workflow.md)
y [versioning.md](../conventions/versioning.md).

## Reporte diario

Cada desarrollador publica su avance al cierre de su jornada en el
[hilo de standup](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/discussions/1),
usando la plantilla del hilo. El límite es 23:59 CST.

El **orden de trabajo** (qué tarea depende de cuál), los **checklists para no
perder fechas** y el **monitoreo del SM** están en
[PLAN-Y-SEGUIMIENTO.md](./PLAN-Y-SEGUIMIENTO.md).
