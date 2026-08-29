#!/usr/bin/env python3
"""Serve o catalogo de gatilhos por id ou por secao. Vocabulario fechado.

O catalogo e a taxonomia de risco do corpus: 86 padroes observaveis, cada um com
severidade, base normativa, pergunta de checagem, mitigacao canonica e a
traducao do padrao para quem nao le codigo. A skill nao descreve risco em prosa —
ela CLASSIFICA dentro destas 86 categorias e devolve o id. Tudo o mais o renderer
busca aqui.

Isso existe por medicao. Com a skill escrevendo prosa, `checar`, `base` e
`severidade` sairam como copia literal deste arquivo em 100% dos achados dos
quatro casos de teste — o modelo pagava output para reemitir o que ja estava no
repositorio, e a redacao variava entre execucoes sem que o julgamento mudasse.

Servir por SECAO funciona; por elegibilidade da fase 2 nao. Os ids de `Base` sao
compartilhados entre arquivos de diretriz: filtrar por arquivo elegivel preserva
quase todas as linhas. As 10 secoes, ao contrario, sao tematicas e disjuntas.

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

VIGENCIA = {"CFM-2454-2026": "2026-08-26"}
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
        if len(c) != 8 or not RE_ID.match(c[0]):
            continue
        # A coluna `Norma` diz de que norma o gatilho decorre, quando isso muda o
        # regime. Era um `†` colado no texto do gatilho, ate a Res. CFM 2.454/2026
        # entrar em vigor em 26/08/2026: com a vigencia, a leitura obvia seria
        # apagar os simbolos — e isso destruiria o dado. Saber que um achado
        # decorre da 2.454 continua valendo depois da vigencia, porque e o que
        # permite dizer a quem foi avaliado antes o que mudou. Dado em coluna,
        # nao em enfeite de texto.
        norma = c[6] if c[6] and c[6] != "—" else None
        out.append({
            "id": c[0], "secao": secao,
            "gatilho": c[1],
            "severidade": c[2].strip("`"),
            "base": [b.strip() for b in c[3].split("·") if b.strip()],
            "checar": c[4], "mitigacao": c[5],
            "norma": norma,
            # `efeito`: o mesmo gatilho dito para quem responde pelo servico e
            # nao le codigo. A coluna `Gatilho` existe para casar com o Grep —
            # `logging.info(request.json)` e `AES.MODE_ECB` sao o padrao literal
            # que a varredura procura, e nao podem ser suavizados sem quebrar a
            # busca. Mas era esse texto que chegava ao medico no parecer. Dois
            # publicos, duas colunas, um arquivo. Quando nao ha traducao, o
            # renderer cai no proprio Gatilho: 59 das 86 linhas ja sao legiveis.
            "efeito": c[7] if c[7] and c[7] != "—" else c[1],
            # `so_norma`: o gatilho nao tem base alem da norma nova. Sao os que
            # mudam de natureza na vigencia — de advertencia preventiva a
            # infracao autonoma —, nao apenas de rotulo.
            "so_norma": bool(norma) and all(
                b.startswith(norma) for b in
                [x.strip() for x in c[3].split("·") if x.strip()]),
        })
    # Catalogo vazio e erro, nunca silencio. Um catalogo em formato antigo — seis
    # colunas em vez de sete — faz o `continue` acima descartar as 77 linhas, e o
    # renderer produzia um parecer SEM NENHUM ACHADO, exit 0, sem uma palavra. O
    # parser precisa gritar quando nao reconhece o que leu.
    if not out:
        sys.exit(f"ERRO: nenhum gatilho reconhecido em {caminho}. Esperado sete "
                 f"colunas: # | Gatilho | Severidade | Base | O que checar | "
                 f"Mitigação | Norma. Catálogo em formato antigo?")
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
        # `secao` e `efeito` entram aqui porque a fase 3 classifica contra ESTE
        # TSV, e as duas faltavam.
        #
        # `efeito` e a traducao do gatilho para quem nao le codigo. Ela existia
        # desde 0b73e52 e so chegava ao parecer — o classificador nunca a via. O
        # G01 mede o estrago: `payload serializado do registro, sem selecao de
        # campos` casa 11 de 11 vezes num caso com codigo e 2 de 14 num caso em
        # prosa, onde o material e um arquivo de audio que nao tem campo a
        # selecionar. O modelo estava sendo correto sobre o texto que recebeu.
        # Sai so quando difere do gatilho — 27 das 86 —, senao seriam 59 linhas
        # com a coluna duplicada, que treina a passar o olho.
        #
        # `secao` volta porque a SKILL manda rotear por tema e depois entregava
        # um bloco plano com o tema apagado.
        print("id\tsecao\tsev\tgatilho\tefeito\tbase\tchecar\tmitigacao\tnorma")
        for g in sel:
            print("\t".join([
                g["id"], g["secao"] or "", g["severidade"][0].upper(),
                g["gatilho"],
                "" if g["efeito"] == g["gatilho"] else g["efeito"],
                "·".join(g["base"]), g["checar"], g["mitigacao"],
                g["norma"] or ""]))
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
        if g["norma"]:
            v = VIGENCIA.get(g["norma"])
            print("  norma: %s%s%s" % (g["norma"],
                  " · em vigor desde %s" % v if v else "",
                  " · sem base autônoma fora dela" if g["so_norma"] else ""))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
