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
| `jxadevp` | admin | `10.92.0.2` | Jesus Alberto: administracion |
| `sebastian` | devs | `10.91.0.2` | Sebastian: PO |
| `azael` | devs | `10.91.0.3` | Azael: backend |
| `elias` | devs | `10.91.0.4` | Elias: backend |
| `y0adq1` | devs | `10.91.0.5` | Juan Antonio: frontend |

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
  administracion, tampoco por SSH.
- **servicios → admin**: un servicio comprometido no llega a la
  administracion.
- **servicios → devs**: los servicios solo responden; no inician.

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

## Verificar

```bash
sudo /etc/doly-vpn/vpn-test.sh
```

Comprueba el tunel, el mTLS (que responde con certificado y que rechaza
sin el) y el aislamiento entre familias.

## Documentos relacionados

- [`operations/VPN.md`](../operations/VPN.md) — runbook: dar de alta y
  revocar peers, rotar llaves, que hacer cuando algo falla.
- [`conventions/security.md`](./security.md) — reglas de seguridad del
  codigo.
