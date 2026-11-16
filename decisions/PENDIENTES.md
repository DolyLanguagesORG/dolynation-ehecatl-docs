# Decisiones pendientes

Decisiones que **necesitan al equipo** antes de poder seguir. Cada issue que
depende de una de ellas lleva la etiqueta `needs:decision` y apunta aquí.

La diferencia con los ADR ([`README.md`](./README.md)): un ADR registra una
decisión **tomada**; este archivo registra las que **están abiertas**.

| ID | Decisión | Issue | Estado | Quién decide |
| --- | --- | --- | --- | --- |
| PEND-001 | ¿Catálogo de categorías predefinido, o solo las dinámicas? | `infra#20` | **Abierta** (16-nov-2026) | equipo |
| PEND-002 | ¿Se autoriza el primer despliegue a producción? | `infra#15` | **Abierta** (16-nov-2026) | scrum master |

---

## PEND-001 — ¿Catálogo de categorías predefinido o solo dinámicas?

- **Contexto:** el frontend tiene un selector de categorías que las saca de
  `GET /settings/categories`. Ese endpoint devolvía `catalog: []`
  hardcodeado, y ya lo sirve desde `moderated_categories` (PR #129): las
  categorías que alguien escribió y pasaron la moderación. Es decir: **las
  categorías dinámicas funcionan y el catálogo no está vacío**.

  Lo que **no** existe es un catálogo **predefinido**: una lista curada de
  categorías de partida ("Historia", "Ciencia", "Tecnología"…) que el equipo
  mantiene a mano. Se eliminó a propósito cuando las categorías pasaron a ser
  dinámicas (el catálogo fijo era el que obligaba a escribir la tabla
  `categories` y su CRUD de admin).

- **Opciones:**
  1. **Solo dinámicas** (lo que hay hoy). El catálogo se llena con el uso.
     Cero trabajo extra, pero una cuenta nueva ve el catálogo vacío hasta que
     alguien más haya escrito categorías.
  2. **Catálogo predefinido en el frontend**: una constante curada
     (`catalog.constants.ts`) que se ofrece como sugerencia, sin tocar el
     backend. Es el minimo trabajo y resuelve la cuenta nueva.
  3. **Catálogo predefinido en el backend**: tabla `categories` + CRUD en
     `/admin/categories` + `GET /settings/categories` sirviéndola. Es lo que
     dice `infra#20` y `back#17` a medias. Es trabajo de S2, no un parche.

- **Qué se necesita:** elegir una. La opción 1 ya está; la 2 son un archivo
  y un merge en el front; la 3 es un issue de schema + uno de backend.

- **Recomendación del equipo técnico:** la **2**. Da la experiencia de
  "categorías de partida" sin el coste de una tabla y su CRUD, y deja la
  puerta abierta a la 3.

## PEND-002 — ¿Se autoriza el primer despliegue a producción?

- **Contexto:** el tren de release está montado y probado de punta a punta
  (`develop` → `rc-*` → rehearsal → staging → `main`), con smoke test en
  verde en los tres ambientes. **Producción no se ha desplegado nunca.**

  Antes de hacerlo faltan dos cosas:
  - el `server_name` de `yacaterkos.tech` en `nginx/dolynation.conf` (el
    dominio está reservado pero el nginx no lo sirve);
  - y la decisión de si se despliega con ese dominio o con otro.

- **Qué se necesita:** autorización y el `server_name` definitivo.

- **Nota:** hasta entonces, el `environment` `prod` tiene sus secretos y
  variables, pero no se ejecuta. El primer deploy real es el paso que falta
  para cerrar la entrega del 10-dic.
