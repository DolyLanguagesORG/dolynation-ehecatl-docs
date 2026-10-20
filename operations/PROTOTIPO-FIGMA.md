# Prototipo de Figma

Cómo se integra el prototipo de DolyNation (Figma) en el proyecto, cómo se
mantiene y qué hace falta para que todo el equipo —y el profesor— lo puedan ver
sin depender de una cuenta de Figma.

---

## 1. Qué hay y dónde

| Pieza | Dónde | Qué es |
| --- | --- | --- |
| Archivo de diseño | <https://www.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation> | El diseño y el prototipo. `file_key`: `NpeSJlQsZhpa0233xNcYkP` |
| Vista previa (imagen) | [`anteproyecto/assets/wireframes/`](../anteproyecto/assets/wireframes/) | Miniatura oficial, **versionada en el repo** para que no expire |
| Mención en el anteproyecto | §17 *Wireframes* | La referencia al prototipo dentro del documento académico |
| Ruta interactiva en la app | `dolynation-tonatiuh-front` → `/prototipo` | El embed del **Embed Kit 2.0** (issue `front#25`) |

---

## 2. Lo que dice la documentación de Figma (y por qué importa)

| Regla de Figma | Consecuencia para el proyecto |
| --- | --- |
| El endpoint de embed es `https://embed.figma.com/...` (**Embed Kit 2.0**), no `www.figma.com/embed` | La URL que se usa es la de `embed.figma.com` |
| `embed-host` es **obligatorio** | Sin él el embed no carga. El valor identifica el sitio: `embed-host=dolynation` |
| `embed_origin` **no se usa** en v2 | El control del prototipo por `postMessage` exige una OAuth app de Figma (fuera de alcance de la entrega) |
| `node-id` fija el frame o página | Se puede abrir el prototipo en un punto concreto |
| `theme=light\|dark\|system` | El embed se adapta al tema del sistema |
| `allowfullscreen` | Da el botón de pantalla completa |
| Eventos: `INITIAL_LOAD`, `PRESENTED_NODE_CHANGED`, `NEW_STATE`, `MOUSE_PRESS_OR_RELEASE`, `REQUEST_CLOSE`, `LOGIN_SCREEN_SHOWN`, `PASSWORD_SCREEN_SHOWN` | `LOGIN_SCREEN_SHOWN` es el caso crítico: se dispara cuando el visitante ve la **pantalla de login de Figma** |
| El oEmbed devuelve `404` si el archivo **no tiene acceso público por link** | Nuestro archivo sí lo tiene (el oEmbed responde 200 con miniatura) |

---

## 3. En la documentación (este repo)

La imagen del prototipo está **versionada**, no enlazada a ciegas:

![Vista previa del prototipo de DolyNation](../anteproyecto/assets/wireframes/dolynation-prototipo.webp)

> La miniatura oficial de Figma se sirve desde una URL **firmada que expira**
> (la actual, el 25 de diciembre de 2026). Por eso se descarga y se versiona en
> el repo: así la entrega no depende de una fecha de caducidad ni de que
> Figma siga sirviendo la imagen.

El procedimiento para re-exportarla está en
[`anteproyecto/assets/wireframes/README.md`](../anteproyecto/assets/wireframes/README.md).

**GitHub no renderiza `iframe`**, así que el prototipo interactivo no puede
vivir en un `.md`. Lo que sí se puede —y es lo que hay— es la imagen
versionada y el enlace al original.

---

## 4. En la app (frontend)

Ruta **`/prototipo`** con el embed interactivo. El componente es pequeño y
va en `src/components/FigmaEmbed.tsx`:

```tsx
"use client";

import { useEffect, useRef, useState } from "react";

const FIGMA_ORIGIN = "https://www.figma.com";

export function FigmaEmbed({ className }: { className?: string }) {
  const iframe = useRef<HTMLIFrameElement>(null);
  const [needsFigmaLogin, setNeedsFigmaLogin] = useState(false);
  const url = process.env.NEXT_PUBLIC_FIGMA_PROTOTYPE_URL ?? "";

  useEffect(() => {
    const onMessage = (event: MessageEvent) => {
      if (event.origin !== FIGMA_ORIGIN) return;
      if (event.data?.type === "LOGIN_SCREEN_SHOWN") setNeedsFigmaLogin(true);
    };
    window.addEventListener("message", onMessage);
    return () => window.removeEventListener("message", onMessage);
  }, []);

  return (
    <section className={className}>
      {needsFigmaLogin ? (
        <p>
          El prototipo necesita una sesión de Figma.{" "}
          <a href={url} target="_blank" rel="noreferrer">
            Ábrelo en Figma
          </a>
          .
        </p>
      ) : (
        <iframe
          ref={iframe}
          title="Prototipo de DolyNation"
          src={url}
          className="h-[600px] w-full rounded-xl border"
          allowFullScreen
          loading="lazy"
          referrerPolicy="strict-origin-when-cross-origin"
        />
      )}
    </section>
  );
}
```

Y la URL va en la variable de entorno (nunca hardcodeada):

```bash
# .env.local del frontend
NEXT_PUBLIC_FIGMA_PROTOTYPE_URL=https://embed.figma.com/design/NpeSJlQsZhpa0233xNcYkP/DolyNation?embed-host=dolynation&theme=system
```

**Seguridad.** El frontend hoy no define CSP, así que el iframe funciona. Si se
añade una política de seguridad, tiene que permitir el origen:

```
Content-Security-Policy: frame-src 'self' https://embed.figma.com;
```

El backend no sirve el frontend y su CSP de *helmet* **no** necesita cambios.

---

## 5. La app oficial «Figma for GitHub»

Permite que **cada PR y cada issue muestren el diseño** y que se creen issues
desde un frame. Es el único punto que **no** se puede automatizar: la
instalación de una GitHub App requiere navegador y la cuenta de Figma.

### Qué hace falta

- La **cuenta de Figma de quien creó el archivo** (`NpeSJlQsZhpa0233xNcYkP`), o
  la de un miembro del equipo con acceso de edición al archivo.
- Acceso de administrador a la organización `DolyLanguagesORG`.

### Pasos

1. Entrar en <https://github.com/apps/figma> y pulsar **Install** (o
   *Configure* si ya está instalada).
2. Seleccionar la organización `DolyLanguagesORG` y **dar acceso a los cuatro
   repositorios**: `dolynation-atl-back`, `dolynation-tonatiuh-front`,
   `dolynation-tlalli-infra` y `dolynation-ehecatl-docs`.
3. Comprobar en cada repositorio: **Settings → Apps → Figma → Installed**.
4. En Figma, abrir el archivo → **Share → Publish / Connect** y conectarlo con los
   repositorios (o al revés, desde la app en GitHub: *Connect Figma design*).

### Qué se obtiene

- Los PRs muestran la miniatura del diseño afectado.
- Los issues pueden enlazarse a un frame concreto.
- Los cambios de diseño notifican a los PRs relacionados.

### Riesgo

La app pide acceso de lectura a los repositorios y a los archivos de Figma de
la organización. **Que la instalen solo las personas con la cuenta de Figma del
equipo** y que quede registrado en el issue de la organización.

---

## 6. Tokens de diseño

La **Variables API de Figma es solo para planes Enterprise** (devuelve 403
«Limited by Figma plan»), así que **no se puede automatizar** la extracción de
tokens en el plan de la escuela. La API de estilos y de contenido de archivo
sí funciona con un *token* personal, pero es frágil para un proyecto que
entrega en dos meses.

**Lo que sí funciona** (y es lo que hace el issue `front#24`):

1. Exportar desde Figma en **Dev Mode** los valores que usa el sistema
   (paleta, tipografía, radios, espaciados).
2. Guardarlos como `design-tokens.json` en el repositorio del frontend.
3. Alimentar el `@theme` de Tailwind 4 con ese archivo.
4. Dejar anotado en el propio archivo que **Figma es la fuente de verdad** y
   que cualquier cambio se re-exporta.

Con eso, el código y el diseño no se separan: el PR que cambia un token
cambia el JSON, el tema y (opcionalmente) la imagen de referencia.

---

## 7. Comprobaciones

Antes de dar por buena la entrega:

- [ ] La imagen del §17 se ve en GitHub (es un archivo versionado, no una URL).
- [ ] `/prototipo` carga el embed y se ve en un móvil.
- [ ] Si se abre sin sesión de Figma, sale el mensaje con el enlace, no un
      espacio en blanco.
- [ ] El enlace «abrir en Figma» funciona desde el móvil.
- [ ] `design-tokens.json` y el `@theme` de Tailwind tienen los mismos valores
      que el archivo de Figma.
- [ ] La app «Figma for GitHub» está instalada en los cuatro repositorios (o
      queda registrado por qué no).
