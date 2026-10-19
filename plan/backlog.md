# Backlog

Mejoras y pendientes sueltos que no forman parte del cronograma de 5 sprints.
Recoge las notas de generación del proyecto (antes en `notas.txt`). No hay
issues para todo esto todavía; cuando una tarea pase a trabajarse, se crea su
issue.

## IA / generación de texto

- Para dificultad alta, **buscar** artículos o textos reales en lugar de
  generarlos con la IA, y mostrarlos tal cual.

## API (backend)

- Guardar la **respuesta del usuario** de cada texto generado.
- Guardar también la **retroalimentación** generada por la IA.
- Verificar que la **racha** funcione bien y añadir un cron diario (12:00) que
  verifique el estado de las rachas.
- Añadir el **tono** del texto a las opciones de generación (divertido, serio,
  formal).
- Revisar la **seguridad**: permisos y “poderes” por usuario.
- Arreglar el bug de **generación de niveles de dificultad** en los textos.

## Mobile (fuera del alcance de `v1.0.0`)

- Arreglar el bug del botón al responder/fallar: no debería permitir reabrir una
  lectura ya contestada; quitar el botón de “regresar a la lectura”.
- Validar que solo se pueda cargar la página de respuesta para textos
  **no respondidos**.
- **Notificaciones** tipo Duolingo.
- En el perfil, una card extra que, además de las lecturas completadas, muestre
  cuántas se aprobaron y cuántas se reprobaron.
- Poder releer respuestas y volver a ver la retroalimentación de la IA
  (depende de la actualización del backend).
- Consultar la **definición** de palabras y guardar un **glosario** de
  palabras con su definición; extenderlo a **oraciones** completas.
- Sección de **glosario** con apartados de palabras y de oraciones (las
  explicaciones son explicaciones extendidas/contexto, no traducciones).
- Arreglar el bug de **categorías** (algunas no muestran el género y aparecen
  como “tecnología”).
- Arreglar bugs visuales de la lectura (en algunos dispositivos el botón de
  responder se sobrepone a la historia).
- Mejorar el bug visual del botón de generar historia: que se **deshabilite**
  (no que desaparezca) al haber 3 historias.
- Mover el botón de generar historias **arriba** de la sección de lecturas.
