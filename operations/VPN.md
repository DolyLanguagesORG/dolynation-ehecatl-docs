# VPN de DolyNation — runbook

Como operar la VPN del servidor `vaneserver`. Las reglas (quefamilia
alcanza a que, como se autentica) estan en
[`conventions/vpn.md`](../conventions/vpn.md).

## Donde esta todo

| Que | Donde |
| --- | --- |
| Script de la VPN (CA, peers, certificados, paquetes) | `/usr/local/sbin/doly-vpn` |
| Envoltorio que pide la passphrase | `/usr/local/sbin/doly-vpn-run` |
| Descifrar un paquete | `/usr/local/sbin/doly-vpn-decrypt` |
| Levantar / bajar / estado | `/etc/doly-vpn/vpn-up.sh` |
| Firewall | `/etc/doly-vpn/vpn-firewall.sh` |
| Endurecimiento de SSH | `/etc/doly-vpn/vpn-sshd.sh` |
| Comprobaciones | `/etc/doly-vpn/vpn-test.sh` |
| Configuracion de MinIO | `/usr/local/sbin/doly-minio-setup` |
| Material sellado | `/etc/doly-vpn/{ca,peers,bundles}` |
| Config en claro del hub | `/etc/wireguard/wg0.conf` |
| Paquete de un developer | `/etc/doly-vpn/bundles/<peer>.tar.gz.sealed` |

## Estado

```bash
sudo /etc/doly-vpn/vpn-up.sh status
```

## Dar de alta a un developer

El developer genera su llave publica en su maquina y te la pasa:

```bash
wg genkey | tee privatekey | wg pubkey < privatekey
```

El `publickey` va en el `doly-vpn.py`, en la lista `PEERS`, con su
familia (`devs` o `admin`) y una IP libre de esa familia.

Luego, en el servidor:

```bash
sudo doly-vpn-run peers        # genera su llave, su PSK y su par
sudo doly-vpn-run render       # rehace el wg0.conf del hub
sudo doly-vpn-run certs        # le emite su certificado de cliente
sudo doly-vpn-run bundles      # le arma el paquete cifrado
sudo doly-vpn-run runtime      # regenera el material de los servicios
sudo /etc/doly-vpn/vpn-up.sh start
```

Entregarle el paquete:

```bash
scp vaneserver:/etc/doly-vpn/bundles/<peer>.tar.gz.sealed <peer>:
```

El developer lo abre con `doly-vpn-decrypt` (le pasas la passphrase de
la CA por un canal aparte).

## Revocar a un developer

1. Quitar su linea de `PEERS` en el `doly-vpn.py`.
2. Regenerar y reiniciar:

```bash
sudo doly-vpn-run peers
sudo doly-vpn-run render
sudo /etc/doly-vpn/vpn-up.sh start
```

3. Borrar su paquete:

```bash
sudo rm -f /etc/doly-vpn/bundles/<peer>.tar.gz.sealed
```

Su llave ya no esta en el hub: su paquete deja de servir.

## Rotar la llave de un peer

1. El peer genera una llave nueva y te pasa la publica.
2. En el `doly-vpn.py`, cambia la IP del peer a una libre (para forzar
   que se regenere la llave) o borra su directorio:

```bash
sudo rm -f /etc/doly-vpn/peers/<peer>/privatekey.sealed
sudo doly-vpn-run peers
sudo doly-vpn-run render
sudo /etc/doly-vpn/run start   # o vpn-up.sh start
```

3. Entregarle el paquete nuevo.

## Rotar la passphrase de la CA

Hay que volver a sellar todo el material con la nueva:

```bash
sudo sed -i "s/<passphrase actual>/<nueva>/" /etc/doly-vpn/ca/passphrase
# regenerar CA, peers, certificados y paquetes
sudo rm -rf /etc/doly-vpn/ca/certs
sudo doly-vpn-run ca
sudo doly-vpn-run peers
sudo doly-vpn-run render
sudo doly-vpn-run certs
sudo doly-vpn-run bundles
sudo doly-vpn-run runtime
```

Los certificados emitidos con la CA vieja dejan de valer: hay que
reemitirlos y redistribuir los paquetes.

## Migrar el bot de GitHub Actions al puerto 50022

1. Abrir el `tcp/50022` en la **Security List de OCI** (solo ese puerto;
   el `22` se puede cerrar despues).
2. Cambiar el secret `DEPLOY_PORT` de los environments
   (`desarrollo`, `rehearsal`, `staging`, `prod`) de `tlalli-infra` a
   `50022`. **Ningun workflow cambia.**
3. Lanzar un deploy de prueba y confirmar que sale bien.
4. Cuando el bot entre por el 50022, cerrar el 22:

```bash
sudo /etc/doly-vpn/vpn-firewall.sh cerrar-22
```

El `22` sigue escuchando en sshd hasta que se quite de
`/etc/ssh/sshd_config.d/60-doly-vpn.conf`.

## Cambiar el firewall

```bash
sudo /etc/doly-vpn/vpn-firewall.sh apply    # reaplica (idempotente)
sudo /etc/doly-vpn/vpn-firewall.sh verify   # comprueba
sudo /etc/doly-vpn/vpn-firewall.sh backup   # copia de seguridad
```

Los rangos de GitHub Actions y de Cloudflare se actualizan solos cada 6
horas (`doly-vpn-refresh.timer`). Para forzar la actualizacion:

```bash
sudo systemctl start doly-vpn-refresh.service
```

Si la actualizacion falla, se conserva la lista anterior: el bot nunca
se queda sin desplegar por un fallo de red.

## MinIO

```bash
sudo /usr/local/sbin/doly-minio-setup apply
```

Crea el bucket `doly-nation` (con versionado) y deja las credenciales
de la aplicacion en `/etc/doly-vpn/state/minio-app.env` (600, root).

> Este MinIO corre en **un solo nodo**, y en ese modo la API de
> administracion no esta disponible: no se puede crear un usuario con
> permisos acotados, asi que la aplicacion usa las credenciales root.
> Cuando llegue el MinIO externo (que si soporta esa API), se sustituyen
> por un usuario de servicio con politica de solo ese bucket.

El contenedor corre como root dentro de su namespace (MinIO lo pide
asi en el modo single). El que importa es que el puerto 9000 **no** se
publica: la unica entrada es la interfaz de tunel, con nginx y mTLS
por delante.

## Cuando algo falla

| Sintoma | Causa probable | Que hacer |
| --- | --- | --- |
| El handshake no ocurre | El `udp/50443` no esta abierto en la Security List de OCI | Abrirlo en la consola de OCI |
| El handshake ocurre pero no hay datos | PSK distinto, o la regla del firewall | `sudo wg show` y `vpn-firewall.sh verify` |
| `400 The SSL certificate error` | El navegador no tiene el certificado de cliente, o no confia en la CA | Importar el `.p12` e instalar `ca.crt` |
| `404` en vez de la aplicacion | El peer no tiene su interfaz de tunel arriba | `docker logs doly-vpn-<peer>` |
| El bot no puede desplegar | Los rangos de Actions quedaron viejos | `sudo systemctl start doly-vpn-refresh.service` |
| `SSH` al 50022 da timeout | El puerto no esta abierto en OCI | Abrir el `tcp/50022` |
| Un developer no entra a un servicio | Su `AllowedIPs` no incluye la IP del peer | `sudo doly-vpn list` y regenerar su paquete |

## Comprobaciones

```bash
sudo /etc/doly-vpn/vpn-test.sh
```

- el tunel esta arriba y los 8 peers estan,
- `devapi` y `devweb` responden **con** certificado de cliente y
  **rechazan** sin el,
- las reglas de familia estan puestas.

## Cosas que NO se tocan

- Los repos y los workflows: la migracion del bot es un cambio de
  secret, no de codigo.
- `staging` y `prod`: siguen publicos. Que el admin entre a ellos por
  la VPN es una fase posterior.
- La OCI Security List: se cambia a mano desde la consola de OCI.
