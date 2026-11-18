# Lo que falta: dentro de la entrega y fuera de la entrega

Este documento es el **apartado de lo pendiente**: qué queda por hacer, en
qué sprint entra y qué se decidió dejar fuera.

La diferencia entre las dos mitades es importante:

| | Qué es | Dónde se anota |
| --- | --- | --- |
| **Dentro de la entrega** | Trabajo del MVP que está **calendarizado** para el 10-dic | Son issues con `sprint-2`…`sprint-5` y milestone de sprint |
| **Fuera de la entrega** | Ideas que **no están** en el MVP y no entran en el 10-dic | Son issues con `scope:deferred` y milestone «Fuera de alcance (post-entrega)» |

Las dos mitades son issues, no notas: lo que está fuera también se
**mantiene visible y abierta**, para que la decisión de cuándo entre sea
explícita y no se pierda.

---

## 1. Dentro de la entrega

El detalle por sprint está en el [`cronograma.md`](./cronograma.md) (la tabla
de tareas) y en los **milestones** de GitHub (una vista por sprint). El
estado real de cada issue está en GitHub, no aquí: una tabla escrita a mano
se queda vieja; el milestone, no.

### Sprint 2 — cierra el 22 de noviembre

| Issue | Repo | Qué falta |
| --- | --- | --- |
| `back#19` | backend | Adaptador MiniMax como segundo proveedor (la interfaz ya la usan Google y Gemini) |
| `back#20` | backend | Prompts versionados por idioma, categoría, dificultad y longitud |
| `back#6` | backend | Pruebas de integración del Sprint 1 y corrección de bugs (issue paraguas) |
| `infra#20` | infra | **Reducida**: ya no son "3 migraciones de schema", solo falta `readings.prompt_hash` (el schema vive completo en `01-init.sql`) |

### Sprint 3 — cerrado (7/10 entregadas)

Las 3 que no se completaron (`back#9` caché, `back#21` modo degradado,
`back#45` prompt injection) se trasladaron al Sprint 4.

### Sprint 4 — cierra el 29 de noviembre

| Issue | Repo | Qué falta |
| --- | --- | --- |
| `back#11` | backend | Vocabulario contextual (4 campos de RF-08) + TTS |
| `back#12` | backend | Servicio de evaluación PNL por cobertura, precisión y coherencia |
| `back#22` | backend | Motor de puntuación por cobertura y precisión semántica |
| `back#23` | backend | Cálculo de coherencia y construcción del feedback |
| `back#15` | backend | Racha diaria y **asignación de puntos** (la racha ya es real; los puntos no) |
| `back#44` | backend | Endpoint de TTS (audio corto de palabra o frase) |
| `back#9` | backend | Caché de respuestas por `prompt_hash` (traído del S3) |
| `back#21` | backend | Errores, timeouts y modo degradado del proveedor (traído del S3) |
| `back#45` | backend | Protección contra prompt injection (traído del S3) |
| `front#12` | frontend | Vista del panel administrativo |
| `front#9` | frontend | Pop-up de diccionario contextual + audio corto (traído del S3) |
| `infra#21` | infra | Tablas `evaluations` y `vocabulary_logs` (bloquean `back#11`, `#22`, `#23`) |
| `infra#26` | infra | Endurecer `docker-compose.prod.yml` (**crítico**: hoy Postgres queda publicado en `0.0.0.0` sin TLS) |

### Sprint 5 — cierra el 10 de diciembre (entrega)

| Issue | Repo | Qué falta |
| --- | --- | --- |
| `back#14` | backend | Pruebas del módulo de vocabulario y evaluación PNL |
| `back#24` | backend | Pruebas unitarias del motor de evaluación PNL |
| `back#25` | backend | Pruebas de carga y latencia |
| `back#26` | backend | E2E del modo degradado ante fallos de la IA |
| `back#71` | backend | Suite E2E de los endpoints críticos contra staging |
| `front#11` | frontend | Dashboard de usuario (métricas, racha, historial, gráfica) |
| `front#13` | frontend | Pruebas de usabilidad y diseño responsivo |
| `front#15` | frontend | Gráfica de puntos por día |
| `infra#3` | infra | Revisión general de código, limpieza de endpoints y merge a `develop` |
| `infra#9` | infra | Auditoría de seguridad: dependencias, secretos y protección de ramas |
| `infra#25` | infra | Test de paridad entre el schema de Drizzle y el SQL de PostgreSQL |
| `docs#3` | docs | Documentación final, capturas y presentación |

### El grafo que decide el orden real

Dos issues bloquean a casi todo lo demás:

```
infra#21 (evaluations + vocabulary_logs) ─┬─► back#11  (vocabulario + TTS)
                                            └─► back#22, #23 (motor de evaluación)
infra#20 (solo prompt_hash) ────────────────► back#9   (caché)
back#9, #11, #12, #15, #22, #23 ───────────► front#9, #11, #12, #13, #15
```

**Si hubiera que elegir por dónde empezar**: `infra#21` (desbloquea el motor de
evaluación completo) y `back#19` (desbloquea `back#20`).

---

## 2. Fuera de la entrega (pero visibles)

Estas ideas **no están en el anteproyecto** ni en los 5 sprints. No es un
olvido: son decisiones de producto que no se han tomado. Se mantienen
abiertas, con la etiqueta `scope:deferred` y en el milestone «Fuera de
alcance (post-entrega)» (cierre el 30-ene-2027).

| Issue | Repo | Qué es | Lo que hay que decidir |
| --- | --- | --- | --- |
| `back#143` | backend | **Módulo de pagos con Stripe** | Proveedor y países, si el estado se sincroniza por webhook, y qué pasa si el cobro llega pero el webhook no |
| `back#144` | backend | **reCAPTCHA** (o equivalente) anti-bot en el registro | Proveedor, si la clave va en el frontend y cómo la valida el backend, y si aplica también a los endpoints de coste |
| `front#114` | frontend | **Tutorial y ayudas dentro de la app** | Dónde vive, si son textos estáticos (4 idiomas) o dinámicos según el estado del usuario, y si se mide |
| `front#115` | frontend | **Módulo de amistades** | Si es un módulo completo (contactos, invitaciones, feed) o solo "compartir una lectura con un enlace"; modelo de privacidad y si hace falta moderación |

> `back#144` (el captcha) tiene un motivo extra para entrar pronto: el tier
> gratis de Google da **20 lecturas al día**. Un bot que se registre y
> genere lecturas se come la cuota del proyecto entero, y el síntoma (un 503
> raro) no dice por qué.

### Y lo que ya estaba en el backlog

El [`backlog.md`](./backlog.md) recoge ideas sueltas que tampoco forman parte
de los sprints (notificaciones tipo Duolingo, guardarte el glosario de
palabras, el tono de los textos, la app de Figma para GitHub, la sección de
glosario con oraciones, varios bugs visuales de la lectura, **móvil**...). No
tienen issue propia todavía: cuando una pase a trabajarse, se le crea.

---

## 3. Dónde vive cada cosa (para no buscarla en el sitio equivocado)

| Qué | Dónde | Con qué se filtra |
| --- | --- | --- |
| **Bugs** | **Issues** con la etiqueta `bug` y su severidad | Plantilla `bug.yml` (descripción, pasos, esperado, actual, logs, severidad, entorno) |
| **Trabajo por hacer** | **Issues** con `sprint-N` y `area:*`, en su milestone | El Project (Kanban) y los milestones |
| **Decisiones que faltan** | **Issues** con `needs:decision` | [`decisions/PENDIENTES.md`](../decisions/PENDIENTES.md) los explica |
| **Decisiones ya tomadas** | [`decisions/README.md`](../decisions/README.md) (ADR) | — |
| **Anuncios y contexto** | **Discussions** | Por repo; en el de docs está el historial del equipo (versionado, tren de release, ambientes) |
| **Huecos del plan** | **Issues** con `type:gap` | — |
| **Estado del proyecto** | `scripts/status-summary.sh` (en infra) | Genera una foto para pegar en una discussion |

> **Los bugs NO van en las discusiones.** Una discusión es un anuncio o una
> decisión; un bug es trabajo que hay que hacer, con dueño, severidad y un PR
> que lo cierra. Lo que sí va en la discusión es **el resumen**: "esta semana
> se han encontrado estos bugs y estos son los que quedan".
>
> La plantilla `bug.yml` y la etiqueta `bug` existen desde el principio del
> proyecto, pero **nunca se habían usado** (0 issues). A partir de ahora, cada
> error encontrado se reporta así: queda registro auditable de que el fallo
> existió, con su severidad y el PR que lo cierra.

---

## 4. Cómo se actualiza esto

- **El estado real está en GitHub** (issues y milestones). Este documento
  explica el criterio y da el punto de entrada; las cifras concretas se
  regeneran con `scripts/status-summary.sh` (en infra).
- **Al abrir un issue**: assignee + `area:*` + `sprint-*`. La regla está en
  [`conventions/versioning.md`](../conventions/versioning.md) y en la skill
  `doly-workflow`.
- **Al cerrar un sprint**: se mueve lo pendiente al sprint siguiente (como
  se hizo con las 3 tareas del S3) y se actualiza la tabla de arriba.
