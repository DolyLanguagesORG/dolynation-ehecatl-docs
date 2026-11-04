# Pendientes de la auditoría — para retomar

> Lista de lo que quedó **pendiente de decisión o de ejecución** el
> **04-nov-2026**, después de la auditoría de trazabilidad y el anuncio de
> cierres.
>
> El usuario pidió explícitamente **aplazar estos tres puntos** hasta que
> Terminasen las revisiones de los PRs en curso. **No forgotten: siguen
> abiertos y hay que retomarlos.**

## 1. Pasar los `Closes #N` a `Refs #N` en los 8 PRs de features

**Estado:** pendiente · **Responsable:** coordinación · **Prioridad:** alta

Los ocho PRs del backend llevan `Closes #N` aunque **no completan** su issue.
Si se mergean tal cual, cierran tareas a medias.

| PR | Issue | Por qué no cumple |
| --- | --- | --- |
| #33 | `back#4` | **Diff vacío** (0 archivos) |
| #34 | `back#5` | Solo actualiza `fullName`; falta `email`, 409 y E2E |
| #35 | `back#8` | Usa `user_settings` (no canónico), 5 idiomas en vez de 4 |
| #36 | `back#10` | Agrega `/content/generate` en vez de `POST /readings` |
| #37 | `back#13` | Agrega `/evaluation/submit` duplicando la ruta canónica |
| #38 | `back#16` | Sin paginación; `wordsLookedUp` siempre 0 |
| #39 | `back#17` | Tabla `admins` en vez de `users.role`; solo GET |
| #40 | `back#18` | Solo retry + circuit breaker, sin integrar ni pruebas |

**Regla del repo** (`plan/PLAN-Y-SEGUIMIENTO.md`, sección 4): `Closes #N`
cuando el PR **completa** el issue; `Refs #N` cuando solo aporta.

**Acción:** editar el cuerpo de los 8 PRs y cambiar `Closes` por `Refs`, para
que un merge no cierre una tarea incompleta. Los que se reescriban (por
ejemplo #35, #36 y #37, que deben ir a las rutas canónicas) recuperan el
`Closes` cuando de verdad completen su issue.

## 2. Crear el milestone «Fuera de alcance (post-entrega)»

**Estado:** pendiente · **Responsable:** coordinación · **Prioridad:** media

El cronograma dice que P3 y P4 «siguen abiertos y visibles en el milestone
«Fuera de alcance (post-entrega)»», pero **ese milestone no existe** en
ninguno de los cuatro repos.

Además, la afirmación ya no es exacta: P3 y P4 son `infra#7` y `infra#8`, y
ambos están **cerrados**. El árbol `infra#10`–`#17` también se cerró como
duplicado.

**Acción:** decidir entre (a) crear el milestone en los cuatro repos para
alojar el trabajo que se pospone, o (b) corregir el cronograma para que
refleje que P3 y P4 ya se cerraron y no queda nada fuera de alcance. La opción
(b) es la más simple si no hay trabajo pendiente postergado.

## 3. Cerrar `docs#15` (saneamiento de la configuración de GitHub)

**Estado:** casi listo · **Responsable:** coordinación · **Prioridad:** media

Ya está hecho:

- Rulesets de `develop` con `require_code_owner_review: true` y
  `required_review_thread_resolution: true` en los cuatro repos.
- `CODEOWNERS` con tres owners por ruta.
- `LICENSE` (MIT), `SECURITY.md`, `CHANGELOG.md`, `dependabot.yml` e
  `ISSUE_TEMPLATE/config.yml` en los cuatro repos, más topics aplicados.
- `permissions:` declarado en todos los workflows.
- Milestones alineados con el cronograma (18-oct, 01-nov, 15-nov, 29-nov,
  10-dic) y **extendidos** a 08-nov y 22-nov para Sprint 1 y Sprint 2.
- Tablero: 65 items, todos con su milestone poblado, sin issues cerrados.

**Pendiente:** decidir el alcance final y cerrar el issue. El criterio de las
fechas ya se actualizó para que coincida con el cronograma.

## Decisiones ya tomadas en esta sesión

| Decisión | Resultado |
| --- | --- |
| Dónde anunciar los cierres | `dolynation-ehecatl-docs` es el **anuncio central**; cada repo mantiene sus discusiones para lo propio |
| Fechas de los milestones | Coinciden con el **cronograma**: 18-oct, 01-nov, 15-nov, 29-nov, 10-dic |
| Sprint 1 y 2 vencidos | **Extendidos** a 08-nov y 22-nov, sin mover S3–S5 |
| Tema del frontend | **Blanco y negro** (el de los wireframes); `front#24` actualizado para que no exija la paleta naranja |
| Aprobación de PRs | Cada PR lo aprueba **otro** miembro del equipo; quien lo sube no puede aprobarse a sí mismo |
| Revisión del PR #31 | Publicada como revisión con el detalle de lo que cumple y lo que queda |

## Estado de las revisiones

| PR | Estado | Nota |
| --- | --- | --- |
| `ehecatl-docs#22` | 4/4 checks en verde, `MERGEABLE` | Cierra la parte documental de `docs#11`, `docs#13` y `docs#14` |
| `tonatiuh-front#31` | 7/7 checks en verde, revisión publicada | Cierra `front#2` al mergear; `front#22` sigue abierta por `fr`/`it` |

## Documentos relacionados

- [`AUDITORIA-ESTADO-SPRINTS.md`](./AUDITORIA-ESTADO-SPRINTS.md) — inventario completo de lo entregado y de las inconsistencias.
- [`cronograma.md`](./cronograma.md) — sprints, entregables y fechas.
- [`PLAN-Y-SEGUIMIENTO.md`](./PLAN-Y-SEGUIMIENTO.md) — ruta crítica y compuerta de sprint.
