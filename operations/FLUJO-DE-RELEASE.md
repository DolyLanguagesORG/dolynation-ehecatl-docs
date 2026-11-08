# El flujo de release, de punta a punta

Este documento explica **cómo viaja un cambio desde un PR hasta producción**,
qué se hace automático y qué requiere una persona, y por qué hay cuatro
ambientes.

Es el mapa de referencia del proyecto: cuando algo no esté claro, se empieza
por aquí.

---

## El recorrido completo

```
1. CREAR
   PR de feature en el repo que toque, con título Conventional Commits.
        |
        v
2. REVISAR
   CI en verde (unit, e2e, build, guards) + 1 aprobación + code owner.
        |
        v
3. MERGEAR A DEVELOP
   Merge squash a develop.
        |
        v
4. VERSIONAR  (automatico)
   release-please calcula el salto con TODOS los commits del ciclo y abre
   (o actualiza) el PR "chore(release): v0.3.0", que sube:
     - package.json / version.txt  (la versión del repo)
     - CHANGELOG.md               (lo que trae la versión)
     - versions.yml               (la fila de este repo en el manifiesto)
        |
        v
5. MERGEAR EL PR DE RELEASE  (1 aprobación)
   -> tag v0.3.0 + GitHub Release
   -> autodespliegue a DESARROLLO
        |
        v
6. DESARROLLAR A STAGING
   La rc-<version> dispara build-images -> GHCR -> deploy-staging.
        |
        v
7. VERIFICAR STAGING
   a) smoke test automatico (falla el deploy si algo no cuadra)
   b) checklist de salida, firmado por una persona
        |
        v
8. PROMOCIONAR
   PR rc -> main: 2 aprobaciones + code owner + el gate de staging en verde.
        |
        v
9. PRODUCCION
   La cascada abre los PRs develop -> main en back y front. Al mergearse,
   alguien dispara deploy-prod a mano y el environment "produccion" (2
   revisores, sin self-review) lo aprueba antes de tocar el servidor.
```

---

## Que es automatico y que no

| Paso | Automatico | Quien decide |
| --- | --- | --- |
| Calcular la version | si | el bot |
| Subir la version a los archivos | si | el bot (en su PR) |
| Publicar el tag y la Release | si | el bot, al mergear su PR |
| Desplegar a desarrollo | si | el bot |
| Construir la imagen y publicarla | si | el bot |
| Desplegar a staging | si | el bot |
| Verificar el contrato (smoke test) | si | el bot |
| **Promover a `main`** | **no** | **2 personas** |
| **Desplegar a produccion** | **no** | **2 personas mas** |

Es decir: **nada llega a producción sin que alguien lo decida dos veces.**

---

## Los cuatro ambientes

| Ambiente | Puertos | Sale a internet | Quien lo despliega | Para que sirve |
| --- | --- | --- | --- | --- |
| **Desarrollo** | 57010-57012 | si (`devweb`, `devapi`) | automatico en cada merge a `develop` | trabajar |
| **Rehearsal** | 57040-57042 | **no** | automatico | **probar el tren completo sin riesgo** |
| **Staging** | 57020-57022 | si (`stagingweb`) | automatico | probar lo que va a producción |
| **Produccion** | 57030-57032 | si (`yacaterkos.tech`, `www`) | manual + 2 revisores | producción |

### Por que rehearsal

Staging y producción se despliegan **por imagen**: el servidor nunca compila, y
la imagen es inmutable, así que se sabe exactamente qué corre y se puede
volver atrás. Un staging así es lo que hace que servir de algo: si staging
corriera por código y producción por imagen, el bug más común (la imagen no
trae un archivo, el schema está desfasado) solo aparecería en producción.

El problema es que **no se puede probar el mecanismo sin tocar producción**.
Rehearsal es un tercer ambiente **con el mismo camino de código** que staging
y producción — el mismo compose, el mismo script de despliegue, el mismo smoke
test — pero con otro directorio (`/srv/doly/rehearsal`), otros puertos
(5704x) y **sin salir a internet**.

Es donde se recorre el tren entero (`develop` → `rc` → despliegue → verificación)
antes de tocar nada real. Sin él, habría que descubrir los fallos del
mecanismo en staging, o peor, en producción.

### Por qué cuatro y no dos

| Si solo existieran... | El fallo aparecería en... |
| --- | --- |
| desarrollo y producción | producción, con usuarios viendo el fallo |
| desarrollo, staging y producción | staging: se pierde el tiempo del equipo probando en un ambiente que no se parece a producción |
| los cuatro | nada: rehearsal lo encuentra antes |

---

## Las ramas `rc-<version>`

Una `rc` es **la combinación de versiones que se va a promover**. Por ejemplo
`rc-1.0.0` significa: el backend en `0.4.0`, el frontend en `0.3.1`, la
infraestructura en `0.2.0` y la documentación en `0.2.1`.

**No es un entorno**: es una etiqueta de estado, como una `rc` de una
distribución Linux.

Por qué hace falta:

- Los repos escalan **por su cuenta**. El backend puede estar en `0.4.0`
  mientras la documentación va en `0.2.1`. No tiene sentido forzar que
  coincidan.
- Pero **producir** sí necesita una combinación concreta. La rc la fija.
- Solo puede haber **una** a la vez: si hubiera dos, dos combinaciones
  distintas podrían llegar a producción sin que nadie lo notara. De eso se
  encarga el **guard single-flight**, que falla con un mensaje claro.

La `rc` se crea en los cuatro repos con el **mismo número** (no la misma
versión: cada repo va en la suya, la que dice `versions.yml`).

---

## Los cinco frenos

Un cambio puede detenerse en cinco sitios, y cada uno tiene su mecanismo:

### 1. En el PR de release

El bot abre el PR `chore(release): v0.3.0` en `develop`.

- **Pedir cambios**: se puede. El PR no se mergea y el bot lo vuelve a
  actualizar en el siguiente push.
- **Rechazar la versión entera**: cerrar el PR. El bot lo **vuelve a abrir**
  con el mismo contenido. Para detenerlo de verdad: un commit
  `Release-As: <otra-version>`.

### 2. En el despliegue a staging

Si falla el **healthcheck**, el deploy falla y el stack no se queda a medias.
Si falla el **smoke test**, ese job falla.

En los dos casos **staging se queda con la versión anterior**, y nadie promovió
la nueva: la promoción es manual.

### 3. En el checklist de salida

Una persona recorre la aplicación en staging y **lo firma**. Cubre lo que la
máquina no puede juzgar: que el texto de la IA se lea bien, que el feedback
sea útil, que el diseño se vea bien.

Es la capa que el smoke test no puede sustituir.

### 4. En el PR hacia `main`

- **2 aprobaciones** obligatorias.
- **Code owner review**: quien toca el archivo tiene que aprobar.
- **Gate de ambiente**: GitHub no deja mergear hasta que el environment
  `staging` tenga un deployment exitoso.

### 5. En el despliegue a producción

El environment `produccion` tiene **2 required reviewers** y **sin
self-review**: GitHub **pausa el workflow** antes de tocar el servidor.

---

## Los numeros de version

| Version | Cuando | Gate |
| --- | --- | --- |
| `0.x.y` | cada merge a `develop` | automatico (CI en verde) |
| `v1.0.0` | cuando el sistema sea un **MVP que funcione sin errores** | checklist de staging firmado + 2 aprobaciones en `main` |

Las `0.x.y` **no representan un entregable**: suben con cada merge mientras se
trabaja. La `v1.0.0` es la del entregable de diciembre, y sale cuando el
checklist de salida se firma por primera vez con todo funcionando.

Se fija con un commit:

```bash
git commit --allow-empty -m "Release-As: 1.0.0"
```

---

## Referencias

| Documento | Qué contiene |
| --- | --- |
| [`conventions/versioning.md`](../conventions/versioning.md) | el versionado automático y las reglas de bump |
| [`operations/CI-CD-Y-VERSIONADO.md`](./CI-CD-Y-VERSIONADO.md) | el pipeline completo, fase por fase |
| [`operations/PLAN-DE-DESPLIEGUE.md`](./PLAN-DE-DESPLIEGUE.md) | los ambientes, los puertos, los secrets y los gates |
| `operations/CHECKLIST-SALIDA-STAGING.md` (en `tlalli-infra`) | lo que una persona revisa y firma antes de promover |
