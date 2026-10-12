# Cómo contribuir

Gracias por sumarte al equipo de Dolynglish. Esta guía resume el flujo de
trabajo en cinco líneas. Para el detalle, sigue los enlaces.

1. **Clona** el repo: `git clone git@github.com:DolyLanguagesORG/doly-languages.git`
2. **Instala** dependencias: `cd backend && npm ci` (esto instala también los
   hooks de husky que validan tus commits)
3. **Levanta** el entorno local ([onboarding/setup.md](./onboarding/setup.md))
4. **Crea una rama** desde `develop`: `git switch -c docs/<nombre-kebab>`
5. **Abre un PR** contra `develop` siguiendo la
   [guía de pull requests](./COMO-HACER-UN-PR.md)

Para el panorama completo de ramas, planificación y releases, ve a
[FLUJO-DE-TRABAJO.md](./FLUJO-DE-TRABAJO.md).

## Convenciones obligatorias

- [Cómo hacer un PR](./COMO-HACER-UN-PR.md) — flujo paso a paso, checks, `Closes`.
- [Flujo de trabajo del repo](./FLUJO-DE-TRABAJO.md) — ramas, tablero, releases.
- [Git workflow](./conventions/git-workflow.md) — flujo de ramas, hotfixes.
- [Conventional Commits](./conventions/commits.md) — formato de mensajes.
- [API contracts](./conventions/api-contracts.md) — envelope `{ message, data, error? }`.
- [Code style](./conventions/code-style.md) — TypeScript estricto, ESLint, Prettier.
- [Testing](./conventions/testing.md) — qué testear y cómo.

Antes de commitear:

```bash
cd backend
npm run verify    # typecheck + lint:check + format:check + test
```

El comando `verify` es la red mínima local; el CI en GitHub Actions añade la
suite e2e, el guard de OpenAPI y el build de producción.

Dos salvedades conocidas sobre `verify`:

- **En Windows** los scripts usan un prefijo de variable de entorno que `cmd`
  no entiende, así que `verify` se rompe. Corre los pasos por separado
  (ver [COMO-HACER-UN-PR.md](./COMO-HACER-UN-PR.md#si-estás-en-windows)).
- **Sin Postgres local** los 5 suites e2e fallan con `ECONNREFUSED :5432`,
  porque `npm test` los incluye. Levanta Docker o usa
  `npx jest --testPathIgnorePatterns 'e2e-spec'` para correr solo los unitarios.

## Reportar bugs o pedir features

Usa las plantillas en `.github/ISSUE_TEMPLATE/`. Para bugs, incluye pasos
para reproducir y comportamiento esperado vs. observado.