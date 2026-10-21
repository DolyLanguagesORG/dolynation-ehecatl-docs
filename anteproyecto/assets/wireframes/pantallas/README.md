# Pantallas del maquetado

Las nueve pantallas del prototipo de DolyNation, exportadas desde Figma y
**versionadas en este repositorio** para que el maquetado se pueda revisar sin
abrir Figma y sin depender de un enlace externo.

## Contenido

| Archivo | Pantalla | Tamaño | Cubre |
| --- | --- | --- | --- |
| `01-inicio.png` | Inicio | 1280 × 1703 | RF-12 |
| `02-iniciar-sesion.png` | Iniciar sesión | 1296 × 1107 | RF-01 |
| `03-registro-de-usuario.png` | Registro de usuario | 1296 × 1107 | RF-01 |
| `04-perfil-y-progreso.png` | Perfil y progreso | 1280 × 1360 | RF-03, RF-11 |
| `05-generacion-de-lectura.png` | Generación de lectura | 1280 × 800 | RF-02, RF-05 |
| `06-detalle-de-lectura.png` | Detalle de lectura | 1280 × 2313 | RF-06, RF-08 |
| `07-respuesta-de-comprension.png` | Respuesta de comprensión | 1280 × 1300 | RF-07 |
| `08-resultado-de-evaluacion.png` | Resultado de evaluación | 1280 × 2291 | RF-07 |
| `09-historial-de-lecturas.png` | Historial de lecturas | 1280 × 956 | RF-09, RF-10 |

El orden de los archivos es el del recorrido del usuario y coincide con el
§17 del [anteproyyecto](../../../anteproyecto-dolynation.md).

## Procedencia

| Dato | Valor |
| --- | --- |
| Archivo de Figma | <https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation> |
| Clave del archivo (`file_key`) | `NpeSJlQsZhpa0233xNcYkP` |
| Origen de las imágenes | Exportación de cada frame del archivo de Figma en PNG |
| Vista previa general | [`../dolynation-prototipo.webp`](../dolynation-prototipo.webp) |

## Cómo re-exportar una pantalla

1. Abrir el archivo de Figma y seleccionar el frame.
2. Clic derecho → **Copy as PNG** (o **Export** → PNG a **2×**).
3. Pegar el archivo en esta carpeta con el nombre de la tabla.
4. Sustituir la imagen y subir el cambio en un PR.

**Detalles que importan:** exporta a **2×** (a 1× el texto sale borroso en un
portátil) y **recorta** las pantallas muy altas: `06-detalle-de-lectura.png` y
`08-resultado-de-evaluacion.png` superan las 2 300 px de alto y en el documento
se ven mejor recortadas.
