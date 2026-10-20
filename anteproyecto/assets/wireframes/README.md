# Wireframes y prototipo

Imágenes de referencia del prototipo de DolyNation, versionadas junto a la
documentación para que la entrega no dependa de un servicio externo.

## Contenido

| Archivo | Qué es | Origen |
| --- | --- | --- |
| `dolynation-prototipo.webp` | Vista previa del archivo de Figma (501 × 450) | Miniatura oficial del oEmbed de Figma |

## Procedencia

| Dato | Valor |
| --- | --- |
| Archivo de Figma | <https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation> |
| Clave del archivo (`file_key`) | `NpeSJlQsZhpa0233xNcYkP` |
| URL del prototipo | `https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation?t=8gwQ2d6Pm2A7mIa-1` |
| URL de embed (Embed Kit 2.0) | `https://embed.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation?embed-host=dolynation` |
| Miniatura (oEmbed) | `https://www.figma.com/api/oembed?url=<url del archivo codificada>` |

La miniatura se **descargó y versionó** a propósito: la URL que devuelve el
oEmbed de Figma viene firmada y **expira** (la actual caduca el 25 de
diciembre de 2026). Si se enlazara directamente, la imagen dejaría de verse a
partir de esa fecha.

## Cómo re-exportar la vista previa

1. Abrir el archivo de Figma y copiar la URL (*Share → Copy link*).
2. Pedir la miniatura:

   ```bash
   curl -s "https://www.figma.com/api/oembed?url=<URL codificada>" \
     | python3 -c "import sys,json;print(json.load(sys.stdin)['thumbnail_url'])"
   ```

3. Descargarla y reemplazar el archivo de esta carpeta:

   ```bash
   curl -sL "<thumbnail_url>" -o anteproyecto/assets/wireframes/dolynation-prototipo.webp
   ```

4. Subir el cambio en un PR (la imagen es binaria, pero GitHub muestra el diff
   de las imágenes) y actualizar la procedencia de esta tabla.

## Relación con el resto de la documentación

- La guía completa de la integración está en
  [`operations/PROTOTIPO-FIGMA.md`](../../../operations/PROTOTIPO-FIGMA.md).
- Los wireframes se muestran en el §17 del
  [anteproyyecto](../../anteproyecto-dolynation.md).
- La ruta `/prototipo` del frontend con el embed interactivo está en el issue
  `front#25` del repositorio del frontend.
