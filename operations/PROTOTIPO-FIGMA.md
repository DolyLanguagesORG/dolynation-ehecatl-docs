# Prototipo de Figma

Dónde está el prototipo de DolyNation, cómo se mantiene y qué hace falta para
que el profesor pueda verlo sin necesidad de una cuenta de Figma.

---

## 1. El prototipo

| Dato | Valor |
| --- | --- |
| Archivo de Figma | <https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation> |
| Enlace directo | <https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation?t=8gwQ2d6Pm2A7mIa-1> |
| Clave del archivo (`file_key`) | `NpeSJlQsZhpa0233xNcYkP` |
| Vista previa en la documentación | [`anteproyecto/assets/wireframes/`](../anteproyecto/assets/wireframes/) |

El archivo tiene **acceso público por link**: cualquiera que abra el enlace ve
el diseño, sin necesidad de cuenta de Figma. Eso se comprobó con la API
*oEmbed* de Figma, que responde `404` cuando el archivo **no** tiene ese
acceso.

## 2. La imagen versionada

![Vista previa del prototipo de DolyNation](../anteproyecto/assets/wireframes/dolynation-prototipo.webp)

La miniatura oficial que devuelve el oEmbed viene en una **URL firmada que
expira** (la actual, el 25 de diciembre de 2026). Por eso se **descarga y se
versiona en el repositorio**: así la entrega no depende de una fecha de
caducidad ni de que Figma siga sirviendo la imagen.

El procedimiento para re-exportarla está en
[`anteproyecto/assets/wireframes/README.md`](../anteproyecto/assets/wireframes/README.md).

## 2.1. Las pantallas del maquetado

Un **enlace al prototipo** es suficiente para que el profesor lo vea, y además
la vista previa general ya está versionada aquí. Pero el criterio de *maquetado*
pide que se vea el diseño completo, así que lo ideal es **exportar las 5-6
pantallas clave** (login, formulario de parámetros, visor, diccionario,
evaluación y dashboard) y subirlas al repo: son **10-15 minutos en Figma** y
convierten esa parte en un "Excelente".

El procedimiento paso a paso, con los nombres de archivo y los tamaños
recomendados, está en
[`anteproyecto/assets/wireframes/pantallas/README.md`](../anteproyecto/assets/wireframes/pantallas/README.md).

## 3. Dónde se ve

- En el **§17 Wireframes** del [anteproyecto](../anteproyecto/anteproyecto-dolynation.md),
  con la imagen embebida y el enlace a Figma.
- En la **portada de la organización** y en el README del repositorio de
  documentación, con el enlace al archivo.

## 4. Lo que NO se hace (y por qué)

- **No se embebe el prototipo en la aplicación.** Decidido el 19 de octubre:
  la ruta `/prototipo` con el *Embed Kit 2.0* no aporta a la entrega de la
  1 al 10 de diciembre y consume tiempo del sprint. El prototipo se abre desde
  el enlace de Figma.
  *Si algún día se quiere*, la vía es `https://embed.figma.com/design/<key>/<nombre>?embed-host=<host>`
  (el parámetro `embed-host` es obligatorio) dentro de un `iframe`, y hay que
  tratar el evento `LOGIN_SCREEN_SHOWN` para no dejar un espacio en blanco
  cuando el visitante no tiene sesión de Figma.
- **No se automatiza la extracción de tokens de diseño.** La *Variables API* de
  Figma es **solo para planes Enterprise** (devuelve 403 «Limited by Figma
  plan»). La extracción se hace a mano, como en el punto 5.

## 5. Tokens de diseño (opcional)

1. Exportar desde Figma en **Dev Mode** la paleta, la tipografía, los radios y
   los espaciados que usa el sistema.
2. Guardarlos como `design-tokens.json` en el repositorio del frontend.
3. Alimentar el `@theme` de Tailwind 4 con ese archivo.
4. Dejar anotado que **Figma es la fuente de verdad** y que cualquier cambio se
   re-exporta.

Con eso, el código y el diseño no se separan: el PR que cambia un token cambia
el JSON, el tema y (opcionalmente) la imagen de referencia.

## 6. App oficial «Figma for GitHub» (opcional)

Permite que **cada PR y cada issue muestren el diseño** y que se creen issues
desde un frame. Hoy la organización **no tiene ninguna app instalada**.

**Qué hace falta:** la **cuenta de Figma de quien creó el archivo** (o la de un
miembro del equipo con acceso de edición) y permisos de administrador en la
organización. **No se puede instalar por API**: el flujo de instalación de una
GitHub App necesita navegador.

### Pasos

1. Entrar en <https://github.com/apps/figma> y pulsar **Install** (o
   *Configure* si ya está instalada).
2. Seleccionar la organización `DolyLanguagesORG` y **dar acceso a los cuatro
   repositorios**: `dolynation-atl-back`, `dolynation-tonatiuh-front`,
   `dolynation-tlalli-infra` y `dolynation-ehecatl-docs`.
3. Comprobar en cada repositorio: **Settings → Apps → Figma → Installed**.
4. En Figma, abrir el archivo → *Share* y conectarlo con los repositorios.

**Riesgo:** la app pide acceso de lectura a los repositorios y a los archivos
de Figma de la organización. Que la instalen solo las personas con la cuenta
del equipo.

## 7. Comprobaciones

- [ ] La imagen del §17 se ve en GitHub (está versionada, no es una URL).
- [ ] Las pantallas exportadas del maquetado están en
      `anteproyecto/assets/wireframes/pantallas/` (o, si no se exportan, el
      enlace a Figma basta).
- [ ] El enlace de Figma abre el diseño sin necesidad de cuenta.
- [ ] `design-tokens.json` y el `@theme` de Tailwind coinciden con Figma.
- [ ] La app «Figma for GitHub» está instalada en los cuatro repositorios, o
      queda registrado por qué no.
