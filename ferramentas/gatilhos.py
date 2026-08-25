#!/usr/bin/env python3
"""Serve o catalogo de gatilhos por id ou por secao. Vocabulario fechado.

O catalogo e a taxonomia de risco do corpus: 77 padroes observaveis, cada um
com severidade, base normativa, pergunta de checagem e mitigacao canonica. A
skill nao descreve risco em prosa — ela CLASSIFICA dentro destas 77 categorias e
devolve o id. Tudo o mais o renderer busca aqui.

Isso existe por medicao. Com a skill escrevendo prosa, `checar`, `base` e
`severidade` sairam como copia literal deste arquivo em 100% dos achados dos
quatro casos de teste — o modelo pagava output para reemitir o que ja estava no
repositorio, e a redacao variava entre execucoes sem que o julgamento mudasse.

Servir por SECAO funciona; por elegibilidade da fase 2 nao. Os ids de `Base` sao
compartilhados entre arquivos de diretriz: filtrar por arquivo elegivel preserva
76 das 77 linhas. As 10 secoes, ao contrario, sao tematicas e disjuntas.

Uso:
    python3 gatilhos.py --listar
    python3 gatilhos.py G02 G31
    python3 gatilhos.py --secao "Segredos e credenciais" --json
    python3 gatilhos.py --json                 # tudo, compacto
"""

import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PADRAO = os.path.join(RAIZ, "corpus", "diretrizes", "07-gatilhos-de-auditoria.md")

COLUNAS = ["id", "gatilho", "severidade", "base", "checar", "mitigacao"]
RE_ID = re.compile(r"^G\d{2}$")


def carregar(caminho):
    """[{id, secao, gatilho, severidade, base[], checar, mitigacao, futuro}]."""
    if not os.path.isfile(caminho):
        sys.exit(f"ERRO: nao encontrei {caminho}")
    secao, out = None, []
    for linha in io.open(caminho, encoding="utf-8"):
        s = linha.rstrip()
        if s.startswith("## "):
            secao = s[3:].strip()
            continue
        if not (s.startswith("| ") and s.endswith(" |")):
            continue
        c = [x.strip() for x in s.strip("|").split("|")]
        if len(c) != 6 or not RE_ID.match(c[0]):
            continue
        gatilho = c[1]
        # `†` marca o que decorre da Res. CFM 2.454/2026, com vigencia propria.
        futuro = gatilho.startswith("†")
        out.append({
            "id": c[0], "secao": secao,
            "gatilho": gatilho.lstrip("† ").strip(),
            "severidade": c[2].strip("`"),
            "base": [b.strip() for b in c[3].split("·") if b.strip()],
            "checar": c[4], "mitigacao": c[5],
            "futuro": futuro,
        })
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="ex. G02 G31")
    ap.add_argument("--catalogo", default=os.environ.get("CORPUS_GATILHOS", PADRAO))
    ap.add_argument("--secao", nargs="+", default=None,
                    help="uma ou mais seções; casa por prefixo, sem acento-sensível")
    ap.add_argument("--listar", action="store_true", help="id, severidade e seção")
    ap.add_argument("--secoes", action="store_true", help="só os nomes de seção")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--tsv", action="store_true",
                    help="uma linha por gatilho, colunas separadas por TAB. "
                         "É o formato mais denso, e o que a skill consome: para "
                         "dado tabular o JSON perde, porque repete o nome de "
                         "cada chave em cada uma das 77 linhas.")
    a = ap.parse_args()

    todos = carregar(a.catalogo)

    if a.secoes:
        vistas = []
        for g in todos:
            if g["secao"] not in vistas:
                vistas.append(g["secao"])
        for s in vistas:
            print("%-40s %d" % (s, sum(1 for g in todos if g["secao"] == s)))
        return 0

    sel = todos
    if a.secao:
        alvo = [s.lower() for s in a.secao]
        sel = [g for g in sel
               if any(g["secao"].lower().startswith(x) for x in alvo)]
        if not sel:
            sys.exit("ERRO: nenhuma seção casou. Use --secoes para ver os nomes.")
    if a.ids:
        faltando = [i for i in a.ids if not any(g["id"] == i for g in todos)]
        if faltando:
            sys.exit("ERRO: id inexistente no catálogo: " + ", ".join(faltando))
        sel = [g for g in sel if g["id"] in a.ids]

    if a.listar:
        for g in sel:
            print("%s\t%-12s\t%s" % (g["id"], g["severidade"], g["gatilho"][:70]))
        return 0

    if a.tsv:
        print("id\tsev\tgatilho\tbase\tchecar\tmitigacao")
        for g in sel:
            print("\t".join([
                g["id"], g["severidade"][0].upper() + ("!" if g["futuro"] else ""),
                g["gatilho"], "·".join(g["base"]), g["checar"], g["mitigacao"]]))
        return 0

    if a.json:
        # compacto de proposito: isto entra no contexto da skill
        print(json.dumps(sel, ensure_ascii=False, separators=(",", ":")))
        return 0

    for g in sel:
        print("%s · %s · %s" % (g["id"], g["severidade"], g["secao"]))
        print("  gatilho:   %s" % g["gatilho"])
        print("  base:      %s" % " · ".join(g["base"]))
        print("  checar:    %s" % g["checar"])
        print("  mitigação: %s" % g["mitigacao"])
        if g["futuro"]:
            print("  † Res. CFM 2.454/2026 — vigência em 26/08/2026")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
