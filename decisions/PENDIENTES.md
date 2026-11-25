# Decisiones pendientes

Decisiones que **necesitan al equipo** antes de poder seguir. Cada issue que
depende de una de ellas lleva la etiqueta `needs:decision` y apunta aquí.

La diferencia con los ADR ([`README.md`](./README.md)): un ADR registra una
decisión **tomada**; este archivo registra las que **están abiertas**.

| ID | Decisión | Issue | Estado | Quién decide |
| --- | --- | --- | --- | --- |
| PEND-001 | ¿Catálogo de categorías predefinido, o solo las dinámicas? | `infra#20` | **Resuelta** (25-nov-2026) | equipo |
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

- **Resolución (25-nov-2026):** Se mantiene el diseño de **categorías dinámicas
  sin tabla fija `categories`**, respaldado por la caché permanente en
  PostgreSQL (`moderated_categories`) que persiste los veredictos aprobados y
  rechazados de las capas de IA para evitar saturarlas. Con esto queda cerrada
  `infra#20` incorporando `readings.prompt_hash` e índice parcial en
  `database/postgres/01-init.sql`.

## PEND-002 — ¿Se autoriza el primer despliegue a producción?

- **Contexto:** el tren de release está montado (`develop` → `rc-*` →
  rehearsal → staging → `main`), el certificado wildcard `*.dolynation.app` de
  Cloudflare Origin CA ya quedó instalado en `vaneserver`, las rutas
  `dolynation.app` / `play.dolynation.app` ya están en Nginx y las credenciales
  de `prod` (Google OAuth, Microsoft Entra ID, Turnstile, Brevo SMTP y Stripe
  Test Mode) ya están cargadas en GitHub Environments. **Producción sigue sin
  desplegarse hasta completar QA.**

- **Qué se necesita:** cerrar la matriz de pruebas en `dev` y `staging`
  ([`plan/QA-PRUEBAS.md`](../plan/QA-PRUEBAS.md)) y dar autorización explícita
  para ejecutar el primer deploy a producción (`infra#15`). La activación de
  Stripe Live Mode puede quedar posterior al arranque inicial si se valida primero
  en Test Mode.

- **Nota:** mientras tanto, el `environment` `prod` conserva sus secretos y
  variables listos, sin ejecutarse hasta recibir aprobación.
