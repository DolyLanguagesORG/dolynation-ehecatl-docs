# Pantallas del prototipo

Aquí van las **capturas de las pantallas del prototipo** exportadas desde Figma.
El objetivo es que el maquetado se pueda ver **sin abrir Figma** y sin que la
entrega dependa de un enlace externo.

## Qué exportar

| Archivo | Pantalla | Por qué |
| --- | --- | --- |
| `01-login.png` | Inicio de sesión y registro | Cubre RF-01 |
| `02-parametros.png` | Formulario de selección de parámetros | Cubre RF-02 y RF-05 |
| `03-visor.png` | Visor de lectura | Cubre RF-06 |
| `04-diccionario.png` | Pop-up de diccionario contextual | Cubre RF-08 |
| `05-evaluacion.png` | Envío del resumen y resultados | Cubre RF-07 |
| `06-dashboard.png` | Dashboard de usuario | Cubre RF-09 y RF-11 |

Con 4 o 5 pantallas ya se cubre lo esencial; el orden de los archivos es el que
usa el §17 del anteproyecto.

## Cómo exportarlas desde Figma (10-15 minutos)

1. Abre el archivo: <https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation>
2. En el panel de la izquierda, selecciona el **frame** de la pantalla.
3. Con el frame seleccionado:
   - **Opción rápida**: clic derecho sobre el frame → **Copy as PNG** (2×) →
     pega el archivo en esta carpeta y renómbralo según la tabla.
   - **Opción con control**: clic derecho → **Export** → elige **PNG**, escala
     **2×** → *Export frame*.
4. Repite para cada pantalla.
5. Sube el cambio en un PR (GitHub muestra el diff de las imágenes) y añade las
   capturas al §17 del anteproyecto.

**Detalles que hacen que se vean bien:**

- Exporta a **2×** (o 3× si la pantalla tiene texto pequeño): a 1× el texto se
  ve borroso en un portátil.
- Usa **PNG** para las capturas con texto; **SVG** solo si la pantalla es
  vectorial y quieres que escala sin pixelarse.
- Si la pantalla es muy alta, recórtala a la parte que explica el flujo: una
  captura de 3000 px de alto no aporta.

## Referencia

- La **vista previa general** del archivo está un nivel arriba:
  [`dolynation-prototipo.webp`](../dolynation-prototipo.webp).
- La guía completa está en
  [`operations/PROTOTIPO-FIGMA.md`](../../../../operations/PROTOTIPO-FIGMA.md).
