# VPN

La red privada por la que el equipo llega a los ambientes de desarrollo.
La API, la web y el almacenamiento de objetos **solo** se alcanzan desde
dentro de la VPN.

## Como esta montada

El hub es el servidor `vaneserver` (`141.148.148.45`). Cada peer tiene
**su propia llave** y **su propio PSK** (llave precompartida): el hub no
comparte material con nadie, y revocar un peer no toca a los demas.

| Peer | Familia | IP de tunel | Que es |
| --- | --- | --- | --- |
| `devapi` | servicios | `10.90.0.2` | API del ambiente de desarrollo |
| `devweb` | servicios | `10.90.0.3` | Web del ambiente de desarrollo |
| `minios` | servicios | `10.90.0.4` | Almacenamiento de objetos (S3) |
| `jxadevp-dev` | devs | `10.91.0.6` | Jesus Alberto: desarrollo |
| `jxadevp-admin` | admin | `10.92.0.2` | Jesus Alberto: administracion |
| `sebastian-dev` | devs | `10.91.0.2` | Sebastian: desarrollo |
| `sebastian-admin` | admin | `10.92.0.3` | Sebastian: administracion |
| `azael` | devs | `10.91.0.3` | Azael: backend |
| `elias` | devs | `10.91.0.4` | Elias: backend |
| `y0adq1` | devs | `10.91.0.5` | Juan Antonio: frontend |

### Las personas con dos identidades

Jesus Alberto y Sebastian desarrollan **y** administran. Cada uno tiene por
eso **dos peers distintos**, con su propia llave y su propio PSK:

| Identidad | Familia | Alcanza a |
| --- | --- | --- |
| `jxadevp-dev` / `sebastian-dev` | devs | servicios y los demas developers |
| `jxadevp-admin` / `sebastian-admin` | admin | todo |

Son **identidades separadas a proposito**: la de desarrollo no puede tocar
el plano de administracion, aunque la persona sea la misma. Asi una laptop
que se filtra no arrastra a la identidad de administracion.

Cada identidad tiene su certificado de cliente, con su CN: el registro del
servidor dice **que identidad** se uso en cada conexion.

- **Protocolo**: WireGuard, sobre `udp/50443`.
- **TLS**: CA interna de DolyNation (raiz + intermedia). Los servicios
  exigen **mTLS**: sin un certificado de cliente firmado por la CA, la
  peticion se rechaza con `400`.
- **Puerto del cliente**: `50022` (el `22` queda como respaldo mientras
  la migracion del bot no este hecha).

## Las familias

Cada familia es un dominio de confianza. Dentro de una familia sus
miembros se hablan; entre familias, solo por una regla explicita del
firewall.

| Familia | Subred | Alcanza a |
| --- | --- | --- |
| `servicios` | `10.90.0.0/24` | servicios, devs, admin |
| `devs` | `10.91.0.0/24` | servicios, devs |
| `admin` | `10.92.0.0/24` | todo |

Lo que **no** pasa:

- **devs → admin**: un developer no entra en la familia de
  administracion, tampoco por SSH. Esto vale tambien para la identidad de
  desarrollo de quien ademas administra: su peer de desarrollo no llega a
  la familia admin.
- **servicios → admin**: un servicio comprometido no llega a la
  administracion.
- **servicios → devs**: los servicios solo responden; no inician.

El corte se hace en dos sitios, a proposito:

1. **En el `AllowedIPs` del peer**: la identidad de desarrollo no tiene
   ruta hacia la familia admin, asi que ni siquiera puede dirigir el
   paquete.
2. **En el firewall** (cadena `DOLY-FWD`): la regla
   `-s 10.91.0.0/24 -d 10.92.0.0/24 -j DROP` corta lo que se cuele por
   el camino del reenvio.

Que el firewall vea ese trafico es lo que hace posible la segunda capa: en
OpenVPN el demonio reenruta entre clientes en *userspace* y el firewall del
host no lo ve (medido: los contadores de `INPUT` y `FORWARD` se quedan en
cero y una regla `DROP` no corta nada).

Que el admin sea una familia aparte y no "el primero de los devs" es
deliberado: revocar el acceso de un developer no toca el del admin, y
un developer comprometido no gana el de nadie mas.

## Entrar

Cada developer recibe un paquete cifrado con su configuracion de
WireGuard, su certificado de cliente y las CAs. El procedimiento
completo (instalar WireGuard, instalar la CA, importar el `.p12`) esta
en el README de la VPN del servidor: `operations/VPN.md`.

Direcciones dentro de la VPN:

| Servicio | Direccion |
| --- | --- |
| API | `https://devapi.yacaterkos.tech` |
| Web | `https://devweb.yacaterkos.tech` |
| Objetos (S3) | `https://minios.doly.internal:50090` |

### El DNS va dentro del tunel

El config de WireGuard del cliente lleva `DNS = 10.90.0.1`: el hub de la
VPN, donde corre un `dnsmasq` que responde con la **IP de tunel** de cada
servicio:

| Nombre | Resuelve a (dentro de la VPN) |
| --- | --- |
| `devapi.yacaterkos.tech` | `10.90.0.2` |
| `devweb.yacaterkos.tech` | `10.90.0.3` |
| `minios.doly.internal` | `10.90.0.4` |

El resto de nombres se resuelven como siempre (el hub los reenvia).

**Por que es obligatorio**: sin esa linea, el nombre resuelve por la DNS
publica a la IP de Cloudflare, y la peticion sale por la conexion normal
de internet **sin pasar por el tunel**. La VPN seguiria levantada y el
servicio responderia igual: el filtro no existiria. El resolutor escucha
solo en la direccion del tunel y el firewall deja el 53 unicamente desde
las tres familias.

Para comprobarlo, desde un equipo con la VPN levantada:

```bash
dig +short devapi.yacaterkos.tech
# debe devolver 10.90.0.2, nunca una IP de Cloudflare
```

## Servicios de terceros y la VPN

La VPN cierra el ambiente de desarrollo al exterior. Pero hay entradas que
**no son de la VPN**: un proveedor de pagos (Stripe) entrega eventos a una
URL publica. La regla es separar *"el servicio tiene que ser publico"* de
*"el servicio esta publico"*.

| Ambiente | Como entra el webhook | Superficie publica |
| --- | --- | --- |
| `desarrollo` | `stripe listen` (CLI) reenvia a `localhost` | **cero** |
| `rehearsal` / `staging` | una sola ruta en el proxy | 1 ruta |
| `produccion` | una sola ruta en el proxy | 1 ruta |

Las reglas:

- **En desarrollo no se expone nada.** El cliente de Stripe (`stripe listen
  --forward-to localhost:3333`) recibe los eventos y los reenvia a la
  maquina. La firma se verifica igual que en produccion. Cero puertos
  nuevos, cero entradas al servidor.
- **En staging y produccion se expone una ruta, no un servicio.** El proxy
  enruta solo `/api/v1/billing/webhook`; el resto del vhost responde
  `deny`. La regla de firewall que deja entrar el trafico viene del
  conjunto de rangos de IP del proveedor, no de `0.0.0.0/0`.
- **La firma se verifica en el backend.** Que un atacante alcance el
  puerto no sirve de nada: sin una firma valida del proveedor, la
  peticion se rechaza y no cambia nada.
- **El webhook no pasa por la VPN.** Es una entrada de internet por
  definicion. Lo que es privado es todo lo demas: la API, la base de
  datos, el panel de administracion y el almacenamiento de objetos.

Esto vive en el issue `atl-back#143` (modulo de pagos). Cuando ese modulo
entre, el camino publico es **una ruta**, no un ambiente entero.

## El bot de GitHub Actions

El bot **no entra en la VPN**: sus runners son efemeros y tienen IP
dinamica, y darle acceso a la VPN significaria que cualquiera que
lograra ejecutar un workflow tendria acceso a la red interna.

Su canal es propio: SSH por el `50022`, con el firewall aceptando solo
los rangos oficiales de IP de GitHub Actions. Esos rangos cambian, asi
que un timer los actualiza cada 6 horas. El puerto se cambia en el
secret `DEPLOY_PORT` de los environments: **ningun workflow cambia**.

## Reglas

- **Ningun material secreto va en un repositorio.** Los repos son
  publicos. Las llaves privadas, los PSKs y la passphrase de la CA
  viven solo en el servidor, cifrados (AES-256-GCM con clave derivada
  por scrypt).
- **Cada peer tiene su propia llave y su propio PSK.** No se comparte
  material entre peers.
- **Cada servicio es un peer con su propia identidad**, no un puerto
  del host: `devapi` y `devweb` se pueden revocar por separado.
- **El material sellado se sella con AES-256-GCM**, no con AES-CBC: el
  GCM autentica, asi que un fichero alterado no se abre.
- **El `22` se cierra** cuando la migracion del bot al `50022` este
  hecha y verificada.
- **La CA raiz solo firma la intermedia.** Ningun certificado de
  servicio o de developer se emite directamente con la raiz.
- **El origen solo lo alcanza Cloudflare.** El 80/443 se acepta
  unicamente desde los rangos publicados de Cloudflare (el set
  `cf_ranges`, que se refresca cada 6 h). Sin esto, la IP del origen es
  publica y cualquiera se salta el proxy. El firewall es *fail-safe*: si
  la lista de Cloudflare se queda vacia, **no** corta el 80/443 y avisa,
  porque cortar ahi tumbaria el sitio.
- **Una lista de IPs vacia no vacia el conjunto**: se conserva la
  anterior. La lista de Cloudflare cambio de URL (`/ips-v4.txt` devolvio
  404 y dejo la proteccion desactivada sin que nadie se enterara).

## Verificar

```bash
sudo /etc/doly-vpn/vpn-test.sh
```

Comprueba el tunel, el mTLS (que responde con certificado y que rechaza
sin el), el aislamiento entre familias, las identidades duales y que el
DNS de la VPN resuelve los servicios a sus IPs de tunel.

Y, desde un equipo con la VPN levantada, que el nombre **no** resuelve a
la IP publica:

```bash
dig +short devapi.yacaterkos.tech   # 10.90.0.2
```

## Documentos relacionados

- [`operations/VPN.md`](../operations/VPN.md) — runbook: dar de alta y
  revocar peers, rotar llaves, que hacer cuando algo falla.
- [`conventions/security.md`](./security.md) — reglas de seguridad del
  codigo.
