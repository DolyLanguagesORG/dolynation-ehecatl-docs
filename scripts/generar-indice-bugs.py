#!/usr/bin/env python3
"""Genera `plan/BUGS.md`: el indice de bugs conocidos de DolyNation.

El indice NO duplica las descripciones: dice que bugs conocemos y **donde**
esta la explicacion de cada uno (la issue, el PR, el commit). La descripcion
vive donde vive de verdad, asi que no se queda vieja ni hay que mantener dos
copias.

De donde sale cada seccion:

  - **Abiertos** y **Cerrados**: las issues con la etiqueta `bug` de los
    repos de la organizacion.
  - **Hallazgos de auditoria**: las issues con la etiqueta `type:gap` (lo
    que la auditoria encontro y no tenia issue propia).
  - **La auditoria del modulo de pagos**: la checklist de `back#150`, leida
    de la propia issue (con su estado `[x]` / `[ ]`).

Uso:
    GITHUB_TOKEN=... python3 scripts/generar-indice-bugs.py

Devuelve 0 y escribe el fichero solo si el contenido cambio; si no, no
toca nada (para que el workflow no abra PRs vacios).
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import sys
import urllib.request

ORG = "DolyLanguagesORG"
REPOS = [
    "dolynation-atl-back",
    "dolynation-tonatiuh-front",
    "dolynation-tetl-landing",
    "dolynation-tlalli-infra",
    "dolynation-ehecatl-docs",
]

# La auditoria del modulo de pagos: una sola issue con checklist, no una
# issue por hallazgo.
AUDITORIA = ("dolynation-atl-back", 150)

SALIDA = pathlib.Path(__file__).resolve().parent.parent / "plan" / "BUGS.md"

CABECERA = """# Bugs conocidos

> Este fichero es un **indice**, no un sitio donde se abren bugs. Dice que
> bugs conocemos y **donde esta la explicacion de cada uno**: la
> explicacion vive donde vive de verdad (la issue, el PR, el commit) y no se
> duplica ni se queda vieja.
>
> **Se regenera solo**: `.github/workflows/bugs-index.yml` lo reescribe cada
> lunes y abre un PR si algo cambio. Para reportar o corregir un bug, edita
> la issue: no esta tabla.

## Como se lee

| Columna | Que significa |
| --- | --- |
| `#` | El issue, con su repo: `back#45` es `dolynation-atl-back#45`. |
| Que es | El titulo del issue. |
| Donde esta la explicacion | El enlace al issue, que es donde esta el detalle. |
| Sprint | El milestone en el que vive (si tiene). |
| Desde | Cuando se abrio. |
"""

PIE = """
## Lo que todavia no tiene sitio

Los errores que pasan en runtime y nadie reporta: viven en `error_logs` y
`audit_logs` de la base de datos, y **no hay ningun sitio donde mirarlos**.
No es un bug conocido (nadie lo ha descrito), pero es un agujero: si un
error pasa en produccion, se descubre al mirarlo.

Cuando se defina, este apartado es el sitio: una entrada por cada error
recurrente, con su explicacion y el issue que lo corrige.

## El modulo de pagos

La auditoria del modulo de pagos esta en **una sola issue con checklist**
(`back#150`), no en una issue por hallazgo: el tablero deja de servir si
cada matiz es una issue, y todos esos hallazgos viven en el mismo modulo y
se revisan con el mismo par de ojos.
"""


def api(ruta: str, token: str) -> object:
    peticion = urllib.request.Request(
        f"https://api.github.com{ruta}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(peticion, timeout=30) as respuesta:
        return json.loads(respuesta.read().decode())


def issues_con_label(repo: str, etiqueta: str, token: str) -> list[dict]:
    datos = api(
        f"/repos/{ORG}/{repo}/issues?labels={etiqueta}&state=all&per_page=100",
        token,
    )
    # La API devuelve tambien los pull requests: no son bugs.
    return [i for i in datos if "pull_request" not in i]


def enlace(repo: str, numero: int) -> str:
    return f"https://github.com/{ORG}/{repo}/issues/{numero}"


def alias(repo: str) -> str:
    return {
        "dolynation-atl-back": "back",
        "dolynation-tonatiuh-front": "front",
        "dolynation-tetl-landing": "landing",
        "dolynation-tlalli-infra": "infra",
        "dolynation-ehecatl-docs": "docs",
    }[repo]


def fila(issue: dict, repo: str) -> str:
    numero = issue["number"]
    titulo = issue["title"].replace("|", "\\|")
    milestone = (issue.get("milestone") or {}).get("title") or "—"
    creado = issue["created_at"][:10]
    return (
        f"| `{alias(repo)}#{numero}` | {titulo} | "
        f"[enlace]({enlace(repo, numero)}) | {milestone} | {creado} |"
    )


def tabla(issues: list[tuple[dict, str]]) -> str:
    if not issues:
        return "_Ninguno._\n"
    lineas = [
        "| # | Que es | Donde esta la explicacion | Sprint | Desde |",
        "| --- | --- | --- | --- | --- |",
    ]
    lineas += [fila(i, r) for i, r in issues]
    return "\n".join(lineas) + "\n"


def checklist_auditoria(token: str) -> str:
    repo, numero = AUDITORIA
    issue = api(f"/repos/{ORG}/{repo}/issues/{numero}", token)
    cuerpo = issue.get("body") or ""

    # Cada punto de la checklist empieza con `- [x]` o `- [ ]` y su texto
    # puede ocupar varias lineas (las de continuacion vienen indentadas).
    # Se juntan para que la tabla no quede partida a mitad de frase.
    patron_inicio = re.compile(r"^-\s*\[([ xX])\]\s*\*\*([^*]+)\*\*\s*(.*)$")
    bloques: list[tuple[str, str, list[str]]] = []
    for linea in cuerpo.splitlines():
        m = patron_inicio.match(linea.strip())
        if m:
            marcado, clave, resto = m.groups()
            bloques.append((marcado, clave.strip(), [resto.strip()]))
        elif bloques and linea.strip() and not linea.strip().startswith("#"):
            bloques[-1][2].append(linea.strip())

    filas = []
    for marcado, clave, trozos in bloques:
        texto = " ".join(t for t in trozos if t).strip()
        # El `**Corregido en #148.**` final se quitan: el estado ya se dice
        # en su propia columna.
        texto = re.sub(r"\*\*Corregido en #[0-9]+\.\*\*", "", texto).strip()
        texto = texto.lstrip(": ").strip()
        texto = texto.rstrip(".").replace("|", "\\|")
        # Los `**` de dentro se dejan: el markdown los usa para el enfasis.
        estado = "corregido" if marcado.lower() == "x" else "pendiente"
        filas.append(f"| `{clave}` | {texto} | {estado} |")

    if not filas:
        return "_No se pudo leer la checklist de la auditoria._\n"
    lineas = [
        "| # | Que es | Estado |",
        "| --- | --- | --- |",
        *filas,
    ]
    return "\n".join(lineas) + "\n"


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        print("Falta GITHUB_TOKEN", file=sys.stderr)
        return 1

    bugs: list[tuple[dict, str]] = []
    huecos: list[tuple[dict, str]] = []
    for repo in REPOS:
        for issue in issues_con_label(repo, "bug", token):
            bugs.append((issue, repo))
        for issue in issues_con_label(repo, "type:gap", token):
            huecos.append((issue, repo))

    bugs.sort(key=lambda par: (par[0]["state"] != "open", par[0]["created_at"]))
    abiertos = [par for par in bugs if par[0]["state"] == "open"]
    cerrados = [par for par in bugs if par[0]["state"] != "open"]
    huecos_abiertos = [par for par in huecos if par[0]["state"] == "open"]

    partes = [CABECERA]
    partes.append("\n## Abiertos\n\n")
    partes.append(tabla(abiertos))
    partes.append("\n## Cerrados\n\n")
    partes.append("| # | Que era | Donde esta la explicacion | Sprint | Desde |\n")
    partes.append("| --- | --- | --- | --- | --- |\n")
    if cerrados:
        partes.append("\n".join(fila(i, r) for i, r in cerrados) + "\n")
    else:
        partes.append("_Ninguno._\n")
    partes.append("\n## Hallazgos de auditoria sin issue propia\n\n")
    partes.append(
        "Los encontro la auditoria y no tenian issue: viven dentro del issue\n"
        "de la auditoria que los detecto, con su checklist.\n\n"
    )
    partes.append(tabla(huecos_abiertos))
    partes.append(PIE)
    partes.append("\n### La checklist de la auditoria\n\n")
    partes.append(
        f"Fuente: [{alias(AUDITORIA[0])}#{AUDITORIA[1]}]"
        f"({enlace(*AUDITORIA)}).\n\n"
    )
    partes.append(checklist_auditoria(token))

    texto = "".join(partes)
    if not texto.endswith("\n"):
        texto += "\n"

    anterior = SALIDA.read_text() if SALIDA.exists() else ""
    if anterior == texto:
        print("El indice ya estaba al dia.")
        return 0

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(texto)
    print(f"Indice regenerado: {len(abiertos)} abiertos, {len(cerrados)} cerrados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
