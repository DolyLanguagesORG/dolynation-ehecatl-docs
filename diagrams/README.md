# Diagramas

Diagramas del proyecto (UML y arquitectura). Los **fuentes** van aquí y se
versionan; las imágenes exportadas se pueden referenciar desde la documentación.

## Convenciones

- Un archivo por diagrama, en `kebab-case`, con su formato de fuente:
  - `*.puml` (PlantUML), `*.drawio`, `*.mmd` (Mermaid) o `.md` con bloques
    Mermaid.
- Nombre descriptivo del tipo: `casos-de-uso-auth.puml`,
  `secuencia-login.mmd`, `despliegue-infra.drawio`.
- Si exportas PNG/SVG, guárdalos junto al fuente con el mismo nombre.
- Prefiere **Mermaid** cuando el diagrama sea simple: se renderiza directo en
  GitHub sin exportar binarios.
- Referencia los diagramas desde el documento correspondiente con un enlace
  relativo.

## Pendiente

Aún no hay diagramas versionados. Candidatos iniciales:

- Casos de uso (general).
- Secuencia de autenticación (registro, login, refresh).
- Secuencia de generación de lectura (formulario → IA → visor).
- Componentes del backend (ver [`architecture/overview.md`](../architecture/overview.md)).
- Despliegue (infra: Postgres + servicios).
