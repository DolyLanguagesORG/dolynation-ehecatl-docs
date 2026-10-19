# Diagramas

Diagramas del proyecto (UML y arquitectura). Los **fuentes** van aquí y se
versionan; las imágenes exportadas se pueden referenciar desde la documentación.

## Contenido

| Archivo | Tema |
| --- | --- |
| [diagrama-de-actores.md](./diagrama-de-actores.md) | Actores, casos de uso y servicios externos |
| [diagrama-de-ER(Entidad-Relacion).md](./diagrama-de-ER%28Entidad-Relacion%29.md) | Entidades, relaciones y columnas |
| [diagrama-de-secuencia.md](./diagrama-de-secuencia.md) | Generación, vocabulario/TTS y evaluación |
| [diagrama-de-secuencia-de-securidad.md](./diagrama-de-secuencia-de-securidad.md) | Login, JWT y refresh |
| [diccionario-de-datos.md](./diccionario-de-datos.md) | Tipos, restricciones y descripción de columnas |

## Convenciones

- Un archivo por diagrama, en `kebab-case`, con su formato de fuente.
- Prefiere **Mermaid** o PlantUML en texto: se renderiza en GitHub sin exportar
  binarios.
- Si exportas PNG/SVG, guárdalos junto al fuente con el mismo nombre.
- Referencia los diagramas desde el documento correspondiente con un enlace
  relativo.
- Mantén el ER y el diccionario alineados con
  [`../architecture/data-model.md`](../architecture/data-model.md) y con el
  schema de `dolynation-tlalli-infra`.
