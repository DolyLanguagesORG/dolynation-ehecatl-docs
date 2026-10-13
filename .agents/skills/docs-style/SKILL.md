---
name: docs-style
description: Cómo escribir y mantener la documentación de DolyNation (repo dolynation-ehecatl-docs). Estructura de archivos, tono, enlaces relativos, tablas y diagramas ASCII. Úsala al crear o editar cualquier archivo .md de la documentación.
---

# Estilo de la documentación

Reglas para escribir y mantener `dolynation-ehecatl-docs`.

## Principios

1. **La doc explica y enlaza; no duplica el código.** Referencia el archivo
   real del repo correspondiente cuando haga falta.
2. **Un tema por archivo.** Si crece, divide y enlaza desde el índice.
3. **Fuente de verdad única.** Ramas/commits → `conventions/`; el pipeline →
   `CI-CD-Y-VERSIONADO.md`; el plan → `cronograma.md`. No repitas reglas: enlaza.
4. **Español.** Títulos, prosa y ejemplos en español. Los términos técnicos se
   mantienen (envelope, squash, commit).

## Estructura

- `README.md` — índice raíz; apunta a todo lo demás.
- `conventions/` — reglas no negociables (una página por área) + `README.md` índice.
- `architecture/` — cómo está organizado el backend.
- `onboarding/` — setup y guías paso a paso.
- `COMO-HACER-UN-PR.md`, `FLUJO-DE-TRABAJO.md`, `CI-CD-Y-VERSIONADO.md` — guías largas.
- `cronograma.md`, `Anteproyecto - DolyNation.md` — plan y planteamiento.
- `backlog.md` — mejoras/pendientes sueltos.
- `diagrams/`, `assets/` — UML y binarios (Word/PDF), ver sus `README.md`.

## Convenciones de formato

- **Enlaces internos relativos**: `[texto](./archivo.md)` o
  `[texto](./carpeta/archivo.md#ancla)`. Nunca absolutos a tu propia máquina.
- **Anclas** en minúsculas y con guiones; van al ser una cabecera.
- **Tablas** para comparar opciones, versiones o checks.
- **Diagramas ASCII** en bloques de código cuando ayuden (evita imágenes si un
  diagrama de texto basta).
- **Callouts** con `> **Nota:** ...` para advertencias.
- Línea larga envuelta a ~80 caracteres.
- El check `link-check` del CI falla si dejas un enlace roto: verifica antes.

## Antes de commitear

No hay `npm run verify` en este repo (los `.md` no tienen dependencias Node). El
CI corre `link-check` (lychee, offline) sobre todos los `.md`, así que **revisa a
mano los enlaces relativos** que toques para no romperlo.

Rama desde `develop`, commit `docs(scope): ...` en español, PR hacia `develop`.
