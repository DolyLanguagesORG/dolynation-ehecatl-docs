# Plan y seguimiento

Este documento responde tres preguntas prácticas del equipo:

1. **¿En qué orden se trabaja?** (qué depende de qué)
2. **¿Cómo no se me pasan las fechas?** (qué revisar cada día y cada sprint)
3. **¿Cómo se monitorea y cómo se justifica un atraso?** (para el SM y para la
   revisión académica)

El plan vive en [`cronograma.md`](./cronograma.md) y el detalle operativo en
[`FLUJO-DE-TRABAJO.md`](../operations/FLUJO-DE-TRABAJO.md). Este documento es el puente
entre los dos.

## 1. Orden de trabajo (ruta crítica)

**Regla de oro:** dentro de un sprint hay libertad para paralelizar, pero **el
backend va antes que el frontend que lo consume**. Nada de conectar una vista
contra un endpoint que todavía no existe (salvo datos mock, que es válido para
avanzar en el maquetado).

Las dependencias están registradas en GitHub con la relación *blocked by*, así
que aparecen en la sección **Relationships** de cada issue y el tablero lo
refleja:

| Tarea de frontend | Bloqueada por (backend) |
| --- | --- |
| [front#3](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/3) — Login/registro | [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) |
| [front#4](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/4) — Perfil | [back#5](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/5) |
| [front#5](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/5) — Form de parámetros | [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8) |
| [front#7](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/7) — Flujo completo | [back#10](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/10) |
| [front#9](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/9) — Popup diccionario | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11) |
| [front#10](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/10) — Redacción de resumen | [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) |
| [front#11](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/11) — Dashboard | [back#15](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/15), [back#16](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/16) |
| [front#12](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/12) — Panel admin | [back#17](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/17) |
| [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13) — Usabilidad/responsivo | [front#11](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/11), [front#12](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/12) |

Dependencias internas de backend y schema:

| Tarea | Bloqueada por |
| --- | --- |
| [back#3](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/3) — Hash/JWT | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2) |
| [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) — Endpoints auth | [back#3](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/3) |
| [back#5](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/5) — Perfil | [back#4](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/4) |
| [back#6](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/6) — Cierre S1 | `back#2` a `back#5` |
| [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7) — IA/prompts | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2) |
| [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8) — Settings | [back#2](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/2), [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) |
| [back#9](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9) — Caché | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7), [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) |
| [back#10](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/10) — Generar lectura | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7), [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8), [back#9](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/9), [infra#20](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/20) |
| [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11) — Vocabulario/TTS | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7), [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) |
| [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12) — Motor PNL | [back#7](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/7) |
| [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) — Guardar evaluación | [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12), [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) |
| [back#14](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/14) — Cierre S3 | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11), [back#12](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/12), [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13) |
| [back#15](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/15) — Racha/puntos | [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13), [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) |
| [back#16](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/16) — Historial | [back#11](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/11), [back#13](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/13), [infra#21](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/21) |
| [back#17](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/17) — Admin | [back#8](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/8), [infra#22](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/22) |
| [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18) — Cierre S5 | `back#14` a `back#17`, [infra#22](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/22) |
| [infra#4](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/4) — PR final + tag `v1.0.0` | [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18), [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13), [infra#3](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/3), [infra#7](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/7) |
| [docs#3](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/issues/3) — Documentación final | [back#18](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/18), [front#13](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/13), [infra#4](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/issues/4) |

**Compuerta de sprint:** un issue no se mergea si su sprint no está activo o si
tiene un `blocked_by` abierto. Los PRs de sprints futuros se mantienen en
**Draft** hasta que toque su sprint.

### Qué puede empezar sin esperar al backend

Estas tareas de frontend son de **interfaz pura** y no dependen de un endpoint,
así que pueden arrancar en paralelo (con datos mock si hace falta):
[front#2](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/2)
(setup),
[front#6](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/6)
(visor de lectura) y
[front#8](https://github.com/DolyLanguagesORG/dolynation-tonatiuh-front/issues/8)
(selección de texto).

## 2. Cómo no perder las fechas

### Checklist diario (cada desarrollador)

- [ ] Mira el **Kanban** del [Project](https://github.com/orgs/DolyLanguagesORG/projects/1)
      y tus issues asignados.
- [ ] Si empiezas una tarea, muévela a **In Progress** y crea la rama
      `tipo/issue-<n>-<detalle>` desde `develop` (o usa el botón *Create a
      branch* del issue).
- [ ] Commits en **Conventional Commits** (husky los valida en local).
- [ ] Abre el PR hacia `develop` con título conventional y `Closes #N`.
- [ ] Publica tu avance en el **standup diario** antes de **23:59 CST**.

### Checklist de cierre de una tarea

- [ ] Los checks del repo están en verde (`pr-title`, `pr-target` y los del repo).
- [ ] El PR tiene **1 aprobación**.
- [ ] **Squash merge** hacia `develop`.
- [ ] El issue se cerró solo (por el `Closes #N`). **Si no**, ciérralo a mano
      (ver más abajo).
- [ ] Mueve la tarjeta a **Done** en el Project (esto **siempre** es manual).

> El `Status` del tablero y el estado *open/closed* del issue son cosas
> distintas: mergear cierra el issue, pero **no** mueve la tarjeta.

## 3. PRs que NO cierran un issue (el caso Flowbite)

**No todo PR cierra un issue, y está bien.** Ejemplo: alguien de frontend añade
**Flowbite** como dependencia y sube un PR. Ese PR:

- Es un `chore(deps): ...` (o `build(...)`).
- **No lleva `Closes #N`**, porque no completa el entregable de ninguna tarea.
- Se mergea igual, con sus checks y su aprobación.

Reglas para no confundir el tablero:

| Situación | Qué poner en el PR |
| --- | --- |
| El PR **completa** el issue (es su entregable) | `Closes #N` |
| El PR **aporta** a un issue pero no lo completa | `Refs #N` (no lo cierra) |
| El PR no pertenece a ninguna tarea (deps, config suelta) | Nada |

**Piénsalo así:** `Closes #N` es una promesa — al mergear, GitHub cierra el
issue. Si el trabajo de esa tarea no queda terminado, **no lo pongas**.

### Si el PR era de una tarea y se te olvidó el `Closes #N`

No pasa nada, se arregla a mano:

1. Abre el PR → panel derecho **Development** → engranaje → **Link an issue**,
   y elige el issue. (O edita el cuerpo del PR y añade `Closes #N` en su propia
   línea; GitHub lo reconoce aunque el PR ya esté abierto.)
2. Si ya se mergeó sin enlace: **cierra el issue manualmente** desde su página
   (botón **Close issue**).
3. Mueve la tarjeta a **Done** en el Project.

## 4. Monitoreo (para el SM)

Para saber **quién no ha avanzado**, sin adivinar:

- **Filtros de issues útiles:**
  - `milestone:"Sprint 1: Infraestructura, Autenticación y Perfil" is:open` → lo que falta del sprint.
  - `label:sprint-1 is:open` → lo mismo, por label.
  - `is:open no:assignee` → tareas sin dueño.
  - `assignee:@AzaelG26 is:open` → la carga de una persona.
- **Vistas del Project** (se crean a mano en la UI; la API no las crea):
  - agrupar por **Assignee** para ver carga por persona;
  - filtrar por **Milestone/Sprint** para el cierre de sprint.
- **Standup diario** ([hilo](https://github.com/DolyLanguagesORG/dolynation-ehecatl-docs/discussions/1)):
  quien no reporta, probablemente no avanzó. Es la señal más temprana.
- **Relationships / blocked by**: si una tarea de frontend está bloqueada, no es
  atraso del responsable de front; es espera de backend. El tablero lo muestra.

## 5. Justificar un atraso (de cara a la revisión)

El profesor revisa fechas. Para que un atraso **no recaiga en el equipo sin
explicación**, déjalo documentado *en el propio issue*, no solo en el chat:

1. **Comenta en el issue** la causa (bloqueo externo, dependencia sin terminar,
   fallo de un servicio de IA, etc.) con fecha.
2. Si el bloqueo es otra tarea, registra la relación **blocked by** en GitHub
   (aparece en *Relationships*).
3. Menciona el bloqueo en el **standup** del día.
4. Cuando se destrabe, comenta que se retomó.

Así, cuando el SM tenga que explicar por qué algo no se entregó a tiempo, hay un
rastro verificable dentro de GitHub, con fechas, no una versión de memoria.

## Documentos relacionados

- [`cronograma.md`](./cronograma.md) — los 33 entregables, sprints y fechas.
- [`FLUJO-DE-TRABAJO.md`](../operations/FLUJO-DE-TRABAJO.md) — ramas, tablero y releases.
- [`COMO-HACER-UN-PR.md`](../operations/COMO-HACER-UN-PR.md) — el paso a paso de un PR.
- [`conventions/git-workflow.md`](../conventions/git-workflow.md) — ramas y hotfixes.
