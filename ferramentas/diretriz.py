#!/usr/bin/env python3
"""Devolve UM bloco de diretriz por identificador, em vez do arquivo inteiro.

O analogo do citar.py, um nivel acima: la o dispositivo, aqui a diretriz que o
aplica. Existe por custo medido. A fase 2 da skill carregava o arquivo inteiro
de cada diretriz roteada — 1.428 a 5.115 tokens por arquivo, ~22.000 num caso
tipico, reenviados a cada turno de 14 a 28 turnos. Mas a varredura roda sobre o
catalogo de gatilhos, que ja traz `Gatilho | Severidade | Base | O que checar`
em forma de tabela. Do arquivo de diretriz so fazem falta, e so depois que um
gatilho dispara, o `Escalar se` e a `Leitura adotada`.

Identificador: `<arquivo-curto>:D<n>`, o mesmo que o checklist ja usa —
`uso-clinico:D3`, `seguranca:D7`.

Uso:
    python3 diretriz.py uso-clinico:D3
    python3 diretriz.py --campos escalar,leitura seguranca:D7 custodia:D13
    python3 diretriz.py --listar
    python3 diretriz.py --json uso-clinico:D3
"""

import argparse
import glob
import io
import json
import os
import re
import sys

# nome curto -> prefixo do arquivo. Os curtos sao os que o checklist ja usa.
CURTOS = {
    "uso-clinico": "01", "custodia": "02", "fornecedor": "03",
    "seguranca": "04", "responsabilidade": "05", "desenvolvimento": "06",
    "gatilhos": "07", "desidentificacao": "08",
}
CAMPOS = ["titulo", "enunciado", "base", "verificar", "escalar", "leitura"]

ROTULOS = {
    "Base": "base",
    "Verificar": "verificar",
    "Escalar se": "escalar",
    "Leitura adotada": "leitura",
}
RE_BLOCO = re.compile(r"^## (D\d+)\s*—\s*(.*)$", re.M)
RE_CAMPO = re.compile(r"^\*\*([^.*]+)\.\*\*[ \t]*(.*)$", re.M)


def carregar(dir_diretrizes):
    """{`curto:Dn`: {campo: valor}} de todos os arquivos."""
    out = {}
    inv = {v: k for k, v in CURTOS.items()}
    for caminho in sorted(glob.glob(os.path.join(dir_diretrizes, "*.md"))):
        base = os.path.basename(caminho)
        curto = inv.get(base[:2])
        if not curto:
            continue
        texto = io.open(caminho, encoding="utf-8").read()
        marcas = list(RE_BLOCO.finditer(texto))
        for i, m in enumerate(marcas):
            fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
            corpo = texto[m.start():fim]
            d = {"titulo": m.group(2).strip(), "arquivo": base,
                 "id": f"{curto}:{m.group(1)}"}
            # enunciado = prosa antes do primeiro campo em negrito
            campos = list(RE_CAMPO.finditer(corpo))
            corte = campos[0].start() if campos else len(corpo)
            d["enunciado"] = corpo[len(m.group(0)):corte].strip()
            for j, c in enumerate(campos):
                chave = ROTULOS.get(c.group(1).strip())
                if not chave:
                    continue
                f = campos[j + 1].start() if j + 1 < len(campos) else len(corpo)
                valor = (c.group(2) + "\n" + corpo[c.end():f]).strip()
                d[chave] = valor
            out[d["id"]] = d
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--diretrizes", default=os.environ.get(
        "CORPUS_DIRETRIZES", "corpus/diretrizes"))
    ap.add_argument("--campos", default="titulo,enunciado,base,verificar,escalar,leitura")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not os.path.isdir(a.diretrizes):
        sys.exit(f"ERRO: nao encontrei {a.diretrizes}")
    blocos = carregar(a.diretrizes)

    if a.listar:
        for k in sorted(blocos):
            print(f"{k}\t{blocos[k]['titulo']}")
        return 0
    if not a.ids:
        ap.error("informe ao menos um id, ou --listar")

    campos = [c.strip() for c in a.campos.split(",") if c.strip()]
    achados, faltando = [], []
    for i in a.ids:
        b = blocos.get(i)
        if not b:
            faltando.append(i)
            continue
        achados.append({**{"id": b["id"], "arquivo": b["arquivo"]},
                        **{c: b[c] for c in campos if c in b}})

    if a.json:
        print(json.dumps({"encontrados": achados, "nao_encontrados": faltando},
                         ensure_ascii=False, indent=2))
    else:
        for b in achados:
            print(f"## {b['id']} — {b.get('titulo','')}")
            print(f"_arquivo: {b['arquivo']}_\n")
            for c in campos:
                if c in b and c != "titulo" and b[c]:
                    print(f"**{c.capitalize()}.** {b[c]}\n")
            print("---\n")
        for i in faltando:
            print(f"## {i}\nNAO ENCONTRADO\n")
    return 1 if faltando else 0


if __name__ == "__main__":
    sys.exit(main())
