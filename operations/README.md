# Operaciones

Cómo se trabaja y se despliega el proyecto.

- [FLUJO-DE-RELEASE.md](./FLUJO-DE-RELEASE.md) — el mapa del proyecto: cómo
  viaja un cambio desde un PR hasta producción, qué es automático, los cuatro
  ambientes, las ramas `rc-*` y los cinco puntos de freno.
- [FLUJO-DE-TRABAJO.md](./FLUJO-DE-TRABAJO.md) — panorama de ramas, tablero,
  CODEOWNERS, dependencias y releases.
- [COMO-HACER-UN-PR.md](./COMO-HACER-UN-PR.md) — paso a paso para abrir un PR,
  checks, `Closes #N` y troubleshooting.
- [CI-CD-Y-VERSIONADO.md](./CI-CD-Y-VERSIONADO.md) — entornos, `rc`, cascada de
  releases, versionado y deploy.
- [PLAN-DE-DESPLIEGUE.md](./PLAN-DE-DESPLIEGUE.md) — los ambientes (desarrollo,
  rehearsal, staging y producción) sobre servidor único, puertos, secretos y flujo de
  despliegue.
- [INTEGRACION-STRIPE-FRONTEND.md](./INTEGRACION-STRIPE-FRONTEND.md) — contrato completo
  de los 13 endpoints `/api/v1/billing/*`, flujos 3DS/OXXO/SPEI y configuración de Stripe
  Elements (`<PaymentElement>` + Appearance API) en blanco y negro para el frontend.
- [VPN.md](./VPN.md) — la VPN de desarrollo: WireGuard con mTLS, las tres familias
  de red, cómo dar de alta y revocar peers y qué hacer cuando algo falla.
- [PROTOTIPO-FIGMA.md](./PROTOTIPO-FIGMA.md) — el prototipo de Figma: dónde está,
  la imagen versionada, cómo se re-exporta, los tokens de diseño y la app
  «Figma for GitHub».
- [JUSTIFICACION-GITHUB.md](./JUSTIFICACION-GITHUB.md) — por qué GitHub es la
  plataforma principal de trabajo: criterios, alternativas descartadas y límites
  reales de la decisión.

La planeación y el backlog viven en [`../plan/`](../plan/README.md).
