#!/usr/bin/env python3
"""Genera `plan/BUGS.md`: el indice de bugs conocidos de DolyNation.

El indice NO duplica las descripciones: dice que bugs conocemos, su ID
secuencial estable (`BUG-001`...) y **donde** esta la explicacion de cada uno
(la issue, el PR, el commit). La descripcion vive en GitHub, asi que no se
queda vieja ni hay que mantener dos copias.

De donde sale cada seccion:

  - **Abiertos** y **Cerrados**: las issues con la etiqueta `bug` de los
    repos de la organizacion, asignando un ID `BUG-NNN` estable por orden
    cronologico (o respetando `[BUG-NNN]` si aparece en el titulo).
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
> bugs conocemos, su identificador **`BUG-NNN`** y **donde esta la explicacion
> de cada uno**: la explicacion vive en la issue real de GitHub y no se
> duplica ni se queda vieja.
>
> **Se regenera solo**: `.github/workflows/bugs-index.yml` lo reescribe cada
> lunes (o bajo demanda con `workflow_dispatch`) y abre un PR si algo cambio.
> Para reportar un bug nuevo, abre la issue con la plantilla `bug.yml` en el
> repositorio correspondiente y referencia el caso de [`QA-PRUEBAS.md`](./QA-PRUEBAS.md).

## Como se lee

| Columna | Que significa |
| --- | --- |
| `ID` | Identificador unico y estable (`BUG-001`...) asignado por orden cronologico (o tomado de `[BUG-NNN]` en el titulo). |
| `Issue` | Enlace corto a la issue en su repo: [`back#134`](https://github.com/DolyLanguagesORG/dolynation-atl-back/issues/134). |
| `Severidad` | Impacto (`Crítica`, `Alta`, `Media`, `Baja`) leido del cuerpo de la plantilla. |
| `Entorno` | Ambiente reportado (`dev`, `staging`, `prod`, `local`). |
| `Que es` | Titulo de la issue. |
| `Sprint` | Milestone asignado (si tiene). |
| `Desde` | Fecha de apertura (`YYYY-MM-DD`). |
"""

PIE = """
## Observabilidad de errores en runtime

Los errores que ocurren en tiempo de ejecucion (HTTP 4xx/5xx y fallos de
proveedores de IA, SMTP o Stripe) se registran en las tablas `error_logs` y
`audit_logs` y pueden inspeccionarse desde el panel de administracion (`/admin`)
y los endpoints `/api/v1/admin/logs/errors`, `/api/v1/admin/logs/audit` y
`/api/v1/admin/logs/trace/:requestId`. Cuando uno revele un defecto
reproducible, abre su issue con la plantilla `bug.yml` para que reciba un
`BUG-NNN` en este indice.

## El modulo de pagos

La auditoria del modulo de pagos esta en **una sola issue con checklist**
(`back#150`), no en una issue por hallazgo: el tablero deja de servir si
cada matiz es una issue, y todos esos hallazgos viven en el mismo modulo y
se revisan con el mismo par de ojos.
"""

RE_BUG_TITULO = re.compile(r"\bBUG-(\d+)\b", re.IGNORECASE)


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


def extraer_seccion_body(cuerpo: str, etiqueta: str) -> str:
    """Extrae el valor de una seccion `### Etiqueta` de Issue Forms."""
    if not cuerpo:
        return ""
    patron = re.compile(
        rf"^###\s*{re.escape(etiqueta)}\s*$\r?\n(.*?)(?=^###\s|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    m = patron.search(cuerpo)
    if not m:
        return ""
    lineas = [
        ln.strip()
        for ln in m.group(1).splitlines()
        if ln.strip() and ln.strip().lower() != "_no response_"
    ]
    return " ".join(lineas)


def normalizar_severidad(cuerpo: str) -> str:
    valor = extraer_seccion_body(cuerpo, "Severidad")
    if not valor:
        return "—"
    corto = re.split(r"\s*[—–-]\s*|\s+", valor, maxsplit=1)[0].strip()
    return (corto or "—").replace("|", "\\|")


def normalizar_entorno(cuerpo: str) -> str:
    valor = extraer_seccion_body(cuerpo, "Entorno")
    if not valor:
        return "—"
    limpio = re.sub(r"\s+", " ", valor).strip()
    return limpio.replace("|", "\\|")


def asignar_bug_ids(bugs: list[tuple[dict, str]]) -> list[tuple[int, str, dict, str]]:
    """Asigna IDs estables `BUG-001`..`BUG-NNN` a todos los issues `bug`."""
    usados: set[int] = set()
    explicitos: dict[tuple[str, int], int] = {}

    for issue, repo in bugs:
        clave = (repo, issue["number"])
        m = RE_BUG_TITULO.search(issue.get("title") or "")
        if m:
            num = int(m.group(1))
            if num > 0 and num not in usados:
                explicitos[clave] = num
                usados.add(num)

    # Orden determinista historico para que los IDs existentes nunca cambien
    # al abrir o cerrar bugs nuevos.
    ordenados = sorted(
        bugs,
        key=lambda par: (par[0]["created_at"], par[1], par[0]["number"]),
    )

    resultado: list[tuple[int, str, dict, str]] = []
    siguiente = 1
    for issue, repo in ordenados:
        clave = (repo, issue["number"])
        if clave in explicitos:
            num = explicitos[clave]
        else:
            while siguiente in usados:
                siguiente += 1
            num = siguiente
            usados.add(num)
        resultado.append((num, f"BUG-{num:03d}", issue, repo))

    resultado.sort(key=lambda item: item[0])
    return resultado


def fila_bug(bug_id: str, issue: dict, repo: str) -> str:
    numero = issue["number"]
    titulo = issue["title"].replace("|", "\\|")
    cuerpo = issue.get("body") or ""
    severidad = normalizar_severidad(cuerpo)
    entorno = normalizar_entorno(cuerpo)
    milestone = (issue.get("milestone") or {}).get("title") or "—"
    creado = issue["created_at"][:10]
    ref = f"[`{alias(repo)}#{numero}`]({enlace(repo, numero)})"
    return (
        f"| `{bug_id}` | {ref} | {severidad} | {entorno} | "
        f"{titulo} | {milestone} | {creado} |"
    )


def tabla_bugs(items: list[tuple[int, str, dict, str]]) -> str:
    if not items:
        return "_Ninguno._\n"
    lineas = [
        "| ID | Issue | Severidad | Entorno | Que es | Sprint | Desde |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    lineas += [fila_bug(bug_id, issue, repo) for _, bug_id, issue, repo in items]
    return "\n".join(lineas) + "\n"


def fila_gap(issue: dict, repo: str) -> str:
    numero = issue["number"]
    titulo = issue["title"].replace("|", "\\|")
    milestone = (issue.get("milestone") or {}).get("title") or "—"
    creado = issue["created_at"][:10]
    return (
        f"| `{alias(repo)}#{numero}` | {titulo} | "
        f"[enlace]({enlace(repo, numero)}) | {milestone} | {creado} |"
    )


def tabla_gaps(issues: list[tuple[dict, str]]) -> str:
    if not issues:
        return "_Ninguno._\n"
    lineas = [
        "| # | Que es | Donde esta la explicacion | Sprint | Desde |",
        "| --- | --- | --- | --- | --- |",
    ]
    lineas += [fila_gap(i, r) for i, r in issues]
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
        # El `**Corregido en #148.**` final se quita: el estado ya se dice
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

    bugs_asignados = asignar_bug_ids(bugs)
    abiertos = [item for item in bugs_asignados if item[2]["state"] == "open"]
    cerrados = [item for item in bugs_asignados if item[2]["state"] != "open"]
    huecos_abiertos = sorted(
        (par for par in huecos if par[0]["state"] == "open"),
        key=lambda par: (par[0]["created_at"], par[1], par[0]["number"]),
    )

    partes = [CABECERA]
    partes.append("\n## Abiertos\n\n")
    partes.append(tabla_bugs(abiertos))
    partes.append("\n## Cerrados\n\n")
    partes.append(tabla_bugs(cerrados))
    partes.append("\n## Hallazgos de auditoria sin issue propia\n\n")
    partes.append(
        "Los encontro la auditoria y no tenian issue: viven dentro del issue\n"
        "de la auditoria que los detecto, con su checklist.\n\n"
    )
    partes.append(tabla_gaps(huecos_abiertos))
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
