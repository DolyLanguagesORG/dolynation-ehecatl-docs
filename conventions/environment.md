# Environment variables

Política de configuración por variables de entorno. La fuente de verdad es
[`.env.example`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/.env.example).

## Tabla de variables

| Variable                | Requerida | Tipo   | Default               | Descripción                                       |
| ----------------------- | --------- | ------ | --------------------- | ------------------------------------------------- |
| `NODE_ENV`              | No        | enum   | `development`         | `development` \| `production` \| `test`           |
| `PORT`                  | No        | int    | `3333`                | Puerto del servidor HTTP                          |
| `HOST`                  | No        | string | `0.0.0.0`             | Interface de bind                                 |
| `API_PREFIX`            | No        | string | `api/v1`              | Prefijo global de rutas                           |
| `APP_NAME`              | No        | string | `dolynglish-backend`  | Nombre lógico para logs                           |
| `DB_HOST`               | Sí        | string | -                     | Host de PostgreSQL                                |
| `DB_PORT`               | Sí        | int    | `5432`                | Puerto de PostgreSQL                              |
| `DB_USER`               | Sí        | string | -                     | Usuario de la BD                                  |
| `DB_PASSWORD`           | Sí        | string | -                     | Password de la BD                                 |
| `DB_DATABASE`           | Sí        | string | -                     | Nombre de la base                                 |
| `DB_LOGGING`            | No        | boolean| `false`               | Logging de queries de Drizzle                     |
| `JWT_SECRET`            | Sí        | string | -                     | Secreto para firmar JWT (≥48 chars random)        |
| `JWT_ACCESS_TTL`        | No        | string | `15m`                 | TTL del access token                              |
| `JWT_REFRESH_TTL`       | No        | string | `30d`                 | TTL del refresh token                             |
| `AI_DEFAULT_PROVIDER`   | Sí        | enum   | `minimax`             | Solo `minimax` está registrado en la factoría     |
| `MINIMAX_API_KEY`       | Cond.*    | string | -                     | API key de MiniMax-M3 (*si provider es minimax)     |
| `MINIMAX_MODEL`         | No        | string | `MiniMax-M3`          | Modelo a usar                                     |
| `MINIMAX_ENDPOINT`      | No        | string | `https://api.minimax.io/v1/chat/completions` | URL del API |
| `MINIMAX_MAX_TOKENS`    | No        | int    | `4096`                | Límite de tokens de salida                        |
| `MINIMAX_TEMPERATURE`   | No        | float  | `0.6`                 | Temperatura de sampling                           |
| `MINIMAX_TIMEOUT_MS`    | No        | int    | `30000`               | Timeout HTTP en ms                                |
| `GROQ_API_KEY`          | No        | string | -                     | *Legacy*: hoy ningún proveedor Groq está registrado|
| `GROQ_MODEL`            | No        | string | `qwen/qwen3-32b`      | Modelo legacy                                     |
| `LOG_LEVEL`             | No        | enum   | `info`                | `trace` \| `debug` \| `info` \| `warn` \| `error` |

Las variables de TTS se definirán en `back#11`; no agregues nombres nuevos
hasta que el proveedor esté decidido.

## Política de secretos

1. **Nunca** commitear `.env` ni `.env.production`. El `.gitignore` raíz
   bloquea `*/.env` y `*/.env.production`.
2. **Generar** `JWT_SECRET` con: `openssl rand -base64 48`
3. **Rotar** secretos cada 90 días en producción (proceso manual).
4. **Diferenciar** dev / staging / prod con archivos separados:
   `.env.development`, `.env.production`, etc.

## Los mismos nombres en todos los ambientes

**El nombre de una variable es el mismo en todos los ambientes**; lo que
cambia es el **valor**.

| | local | desarrollo | rehearsal | staging | producción |
| --- | --- | --- | --- | --- | --- |
| `DB_PASSWORD` | la que sea | de prueba | de prueba | de prueba | **la real** |

Por qué:

- El código lee **un** nombre. Si el nombre cambiara por ambiente, el código
  necesitaría bifurcaciones ("si es staging lee X, si es prod lee Y"), que es
  justo donde aparecen los bugs.
- La seguridad no viene del nombre, viene de: **valores distintos** por
  ambiente, secrets **por environment** en GitHub, y `prod` con dos revisores
  y sin auto-aprobación.
- Regla de oro: **el `.env` de producción nunca se copia a staging**, ni al
  revés.

## Agregar una variable nueva: los 5 lugares

Una variable no existe en la aplicación hasta que está en **todos** estos
lugares. Si se olvida uno, el error típico es "la variable no llega" (el
secret existe en GitHub, pero la aplicación no la ve):

| # | Dónde | Qué se hace |
| --- | --- | --- |
| 1 | `atl-back`: `src/config/env.validation.ts` | se declara en el schema Zod (si es requerida, la app **no arranca** sin ella) |
| 2 | `tlalli-infra`: `docker-compose.env.yml` | se pasa al contenedor que la use |
| 3 | `tlalli-infra`: los 3 workflows `deploy-*.yml` | **la lista de variables del `.env` está escrita a mano**: si no se agrega ahí, no llega al servidor |
| 4 | `atl-back`: `.env.example` | la forma para los que trabajan en local |
| 5 | GitHub **Environments** | un secret por ambiente (`desarrollo`, `rehearsal`, `staging`, `prod`), con valores distintos |

Y el sexto paso, que es de documentación: la tabla de variables de este
archivo (`conventions/environment.md`).

> Si la variable es **pública** (va al navegador), lleva el prefijo
> `NEXT_PUBLIC_` y se compila en el bundle. Si es de **servidor**, **no** lleva
> ese prefijo: así no se filtra al cliente (es el caso de
> `BACKEND_INTERNAL_URL` en el frontend).

## Variables de correo (SMTP)

Para enviar correo, el backend necesita estas variables (todas **de
servidor**: nunca al frontend):

| Variable | Requerida | Descripción |
| --- | --- | --- |
| `SMTP_HOST` | No | Host del servidor SMTP |
| `SMTP_PORT` | No | Puerto (587 con STARTTLS, 465 con TLS implícito) |
| `SMTP_USER` | No | Usuario de la cuenta |
| `SMTP_PASSWORD` | No | Clave SMTP de la cuenta |
| `SMTP_FROM` | No | Remitente (`Nombre <correo@dominio>`) |
| `SMTP_FROM_NAME` | No | Nombre del remitente, si se quiere separado |
| `SMTP_SECURE` | No | `true` solo si el cifrado es implícito (465) |

**Son opcionales a propósito**: si fueran obligatorias, un ambiente sin
SMTP no arrancaría. El servicio de correo falla con un mensaje claro
("falta SMTP_HOST/SMTP_USER") cuando se usa sin configurar.

### El servidor de correo que hay hoy

| | Valor |
| --- | --- |
| Host | `smtp-relay.brevo.com` |
| Puerto | `587` (STARTTLS) |
| Usuario | la cuenta del ambiente |
| Clave | **una distinta por ambiente**, en los GitHub Environments |

Los valores de cada ambiente los pone el scrum master como secrets del
Environment correspondiente: el deploy escribe el `.env` del servidor con
ellos, así que **nadie tiene que saber el servidor de correo de ningún
ambiente para trabajar en su código**. En local, cada quien usa los suyos o
un catcher local (Mailpit/MailHog).

Detalle en la issue del backend (SMTP) y en
[`operations/FLUJO-DE-RELEASE.md`](../operations/FLUJO-DE-RELEASE.md).

En local no hace falta una clave real: se puede levantar un *catch-all*
(Mailpit/MailHog) y ver el correo en el navegador.

## Validación

Las variables se validan al arrancar con un schema Zod en
[`src/config/env.validation.ts`](https://github.com/DolyLanguagesORG/dolynation-atl-back/blob/develop/src/config/env.validation.ts).
Si falta una variable requerida o tiene un valor inválido, la app **no
arranca** y muestra el error exacto.

## Cómo arrancar en local

```bash
# En el repo del backend (dolynation-atl-back):
cp .env.example .env
# Editar .env y rellenar DB_PASSWORD, JWT_SECRET, MINIMAX_API_KEY, etc.
```

Para la BD de desarrollo, se usa el
[`docker-compose.test.yml`](https://github.com/DolyLanguagesORG/dolynation-tlalli-infra/blob/develop/docker-compose.test.yml)
del repo de infraestructura:

```bash
git clone https://github.com/DolyLanguagesORG/dolynation-tlalli-infra.git
cd dolynation-tlalli-infra
docker compose -f docker-compose.test.yml up -d
```

El schema se aplica automáticamente al primer arranque del contenedor.