# Diagramas

Diagramas del proyecto (UML y arquitectura). Están escritos en **Mermaid**, que
GitHub **renderiza de forma nativa**: se ven en el propio archivo, sin plugins,
sin exportar imágenes y sin que se rompan al cambiar el diagrama.

## Contenido

| Archivo | Tema |
| --- | --- |
| [diagrama-de-actores.md](./diagrama-de-actores.md) | Actores, casos de uso y servicios externos |
| [diagrama-de-ER(Entidad-Relacion).md](./diagrama-de-ER%28Entidad-Relacion%29.md) | Entidades, relaciones y columnas |
| [diagrama-de-secuencia.md](./diagrama-de-secuencia.md) | Generación, vocabulario/TTS y evaluación |
| [diagrama-de-secuencia-de-securidad.md](./diagrama-de-secuencia-de-securidad.md) | Login, JWT y refresh |
| [diccionario-de-datos.md](./diccionario-de-datos.md) | Tipos, restricciones y descripción de columnas |

## Convenciones

- Un archivo por diagrama, en `kebab-case`, con el diagrama dentro de una valla
  ` ```mermaid `.
- Todo diagrama se escribe en **Mermaid** para que se renderice solo en GitHub.
  Si necesitas el mismo diagrama fuera de GitHub, se exporta a PNG/SVG y se
  guarda junto al `.md` con el mismo nombre.
- Cada diagrama lleva arriba su título, una frase de qué muestra y una nota de
  **estado** (qué está implementado y qué es el flujo objetivo pendiente), para
  que no se lea como si todo existiera ya.
- El bloque `---` de configuración de Mermaid (por ejemplo `layout: fixed`) va
  al principio del diagrama, dentro de la valla.
- Referencia los diagramas desde el documento correspondiente con un enlace
  relativo.
- Mantén el ER y el diccionario alineados con
  [`../architecture/data-model.md`](../architecture/data-model.md) y con el
  schema de `dolynation-tlalli-infra`.
