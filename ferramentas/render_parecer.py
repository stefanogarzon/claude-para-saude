#!/usr/bin/env python3
"""Renderiza parecer e checklist a partir do achados.json emitido pela skill.

O modelo emite dados; este script escreve o documento. O literal de cada norma
NAO vem do modelo: vem do corpus, pelo id em `decide`, via citar.py. Assim o
texto de lei no parecer e sempre o do corpus, e parafrasear deixa de ser
possivel — que era o buraco que o validar_parecer.py nao cobria.

A data do cabecalho sai do `corpus_verificado_em` do VERSAO.md, nunca de
`construido:` e nunca da memoria do modelo.

Uso:
    python3 ferramentas/render_parecer.py achados.json --saida <dir>
"""

import argparse
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import citar
from esquema_achados import STATUS, TRIAGEM

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AVISO = ("> Orientação profissional, não parecer jurídico. As normas e as "
         "políticas de\n> fornecedores citadas mudam. Confira a data de "
         "verificação antes de usar em\n> decisão concreta.")

ROTULO_TRIAGEM = {
    "material": "Material recebido", "dado": "Tipo de dado",
    "papel": "Papel da IA", "decisao_clinica": "Contato com decisão clínica",
    "modalidade": "Modalidade", "estagio": "Estágio",
    "fornecedor": "Fornecedor e região", "regiao": "Região de processamento",
}


def versao(dir_corpus):
    """(corpus_verificado_em, plugin_version) do VERSAO.md do distribuivel."""
    p = os.path.join(dir_corpus, "VERSAO.md")
    if not os.path.isfile(p):
        return None, None
    t = io.open(p, encoding="utf-8").read()
    v = re.search(r"^corpus_verificado_em:\s*(\S+)", t, re.M)
    pv = re.search(r"^plugin_version:\s*(\S+)", t, re.M)
    return (v.group(1) if v else None), (pv.group(1) if pv else None)


def literais(ids, dir_fichas):
    """{id: {literal, fonte}} do corpus. Fonte unica do texto de norma."""
    corpus = citar.carregar(dir_fichas)
    out = {}
    for i in ids:
        e = corpus.get(i)
        if not e:
            continue
        out[i] = {"literal": e.get("literal", ""), "fonte": e.get("fonte", "")}
    return out


def bloco_achado(a, lits):
    L = ["### %s %s\n" % (a["id"], a["titulo"])]
    L.append("**Severidade.** `%s`" % a["severidade"])
    ori = a["origem"]
    if a.get("evidencia"):
        ev = a["evidencia"]
        ori += " — `%s:%s`" % (ev.get("arquivo", "?"), ev.get("linha", "?"))
    L.append("**Origem.** `%s`" % ori)
    L.append("**Situação.** `%s`" % a["situacao"])
    L.append("**Base.** " + " · ".join("`%s`" % b for b in a["base"]))
    if a.get("leitura_adotada"):
        L.append("**Leitura adotada.** %s" % a["leitura_adotada"])
    L.append("")
    L.append(a["texto"])
    L.append("")

    # O literal vem do corpus, nao do modelo.
    d = a.get("decide")
    lit = lits.get(d)
    if lit and lit["literal"]:
        L.append(lit["literal"].rstrip())
        L.append("> — %s" % lit["fonte"])
    else:
        L.append("> `%s` — [texto não carregado]" % (d or "sem id"))
    L.append("")
    if a.get("checar"):
        L.append("**O que checar.** %s" % a["checar"])
    ac = a.get("acao") or {}
    if ac:
        partes = [("exigir da TI: " + ac["ti"]) if ac.get("ti") else None,
                  ("perguntar ao fornecedor: " + ac["fornecedor"]) if ac.get("fornecedor") else None,
                  ("registrar: " + ac["registrar"]) if ac.get("registrar") else None]
        L.append("**Ação.** " + " · ".join(p for p in partes if p))
    L.append("")
    return "\n".join(L)


def secao_severidade(d, num, titulo, sev, lits):
    achados = [a for a in d["achados"] if a["severidade"].split()[0] == sev]
    conf = [a for a in achados if a["situacao"] == "confirmado"]
    perg = [a for a in achados if a["situacao"] == "pergunta"]
    L = ["## %d. %s\n" % (num, titulo)]
    L.append("#### %da. Violações e pontos confirmados\n" % num)
    L.append("%d achado(s).\n" % len(conf))
    L += [bloco_achado(a, lits) for a in conf]
    rot = ("Perguntas bloqueantes — resposta errada põe o serviço em desconformidade"
           if sev == "bloqueante" else
           "Perguntas de risco — resposta errada expõe o serviço")
    L.append("#### %db. %s\n" % (num, rot))
    L.append("%d achado(s).\n" % len(perg))
    L += [bloco_achado(a, lits) for a in perg]
    return "\n".join(L)


def lista(titulo, itens, num):
    L = ["## %d. %s\n" % (num, titulo)]
    L += ["- %s" % i for i in (itens or [])] or ["Nada a registrar."]
    L.append("")
    return "\n".join(L)


def render_parecer(d, lits, verif, pver, hoje):
    L = ["# Parecer de conformidade — %s\n" % d["projeto"]]
    L.append("**Base.** corpus claude-para-saude, norma conferida em fonte "
             "primária em %s · distribuível v%s" % (verif or "?", pver or "?"))
    L.append("**Material avaliado.** %s" % d["triagem"].get("material", "—"))
    teto = {"declarado": "o teto de todo item é `conforme-declarado`",
            "observado": "há evidência observada",
            "misto": "cada achado declara a sua origem"}
    L.append("**Alcance da verificação.** `%s` — %s"
             % (d["alcance"], teto.get(d["alcance"], "")))
    L.append("**Data.** %s\n" % hoje)
    L.append(AVISO + "\n")
    L.append("---\n")

    L.append("## 1. O que o projeto é\n")
    L.append("| Campo | Valor confirmado |")
    L.append("|---|---|")
    for k in TRIAGEM:
        v = d["triagem"].get(k)
        if v:
            L.append("| %s | %s |" % (ROTULO_TRIAGEM.get(k, k), v))
    L.append("")
    afast = d.get("premissas_afastadas") or []
    if afast:
        L.append("**Premissas que a triagem afastou.** " + " ".join(
            "`%s` — %s." % (a["arquivo"], a["porque"]) for a in afast) + "\n")

    L.append(secao_severidade(d, 2, "Onde ele morde", "bloqueante", lits))
    L.append(secao_severidade(d, 3, "Pontos de exposição", "risco", lits))
    L.append(lista("O que perguntar ao fornecedor", d.get("fornecedor"), 4))
    L.append(lista("O que exigir da TI", d.get("ti"), 5))
    L.append(lista("O que registrar", d.get("registrar"), 6))

    L.append("## 7. Fora do escopo\n")
    fe = d.get("fora_do_escopo") or []
    if fe:
        L.append("Este corpus cobre CFM, LGPD/ANPD, Código Penal, Código Civil, "
                 "CDC, Marco Civil e padrões técnicos, no Brasil. Não há base "
                 "carregada para avaliar os pontos abaixo, e o parecer não opina "
                 "sobre eles.\n")
        for f in fe:
            L.append("- **%s** — %s" % (f["assunto"], f["porque"].rstrip(".") + "."))
    else:
        L.append("Nada fora do escopo.")
    L.append("")

    L.append("## 8. Escalar\n")
    esc = d.get("escalar") or []
    L += ["- **%s** → %s. %s" % (e["item"], e["para"], e.get("porque", ""))
          for e in esc] or ["Nada a escalar."]
    L.append("")

    L.append("## Anexo — evidência técnica\n")
    obs = [a for a in d["achados"] if a.get("evidencia")]
    if obs:
        L.append("| Achado | Arquivo | Linha |")
        L.append("|---|---|---|")
        for a in obs:
            e = a["evidencia"]
            L.append("| %s | `%s` | %s |" % (a["id"], e.get("arquivo", "?"),
                                             e.get("linha", "?")))
    else:
        L.append("Não há. Nenhum achado tem origem `observado`.")
    L.append("")
    return "\n".join(L)


def render_checklist(d, verif):
    L = ["# Checklist de conformidade — %s\n" % d["projeto"]]
    L.append("| Diretriz | Exigência | Status | Origem | Base | Próximo passo |")
    L.append("|---|---|---|---|---|---|")
    cont = {s: 0 for s in STATUS}
    for l in d["checklist"]:
        cont[l["status"]] = cont.get(l["status"], 0) + 1
        L.append("| `%s` | %s | `%s` | `%s` | %s | %s |"
                 % (l["diretriz"], l["exigencia"], l["status"],
                    l.get("origem", "ausente"),
                    " · ".join("`%s`" % b for b in l.get("base", [])) or "—",
                    l.get("proximo", "—")))
    L.append("")
    L.append("| Status | Contagem |")
    L.append("|---|---|")
    for s in STATUS:
        L.append("| `%s` | %d |" % (s, cont[s]))
    L.append("")
    lac = [l for l in d["checklist"] if l["status"] == "lacuna"]
    sev = {}
    for a in d["achados"]:
        sev[a["severidade"].split()[0]] = sev.get(a["severidade"].split()[0], 0) + 1
    L.append("Dos %d `lacuna`, %d correspondem a achado bloqueante e %d a achado "
             "de risco.\n" % (len(lac), sev.get("bloqueante", 0), sev.get("risco", 0)))
    L.append("> Corpus verificado em %s. Alterações normativas posteriores não "
             "estão refletidas. Fornecedor de LLM: reverificar antes de qualquer "
             "decisão — a ficha de provedores tem meia-vida curta." % (verif or "?"))
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("achados")
    ap.add_argument("--saida", required=True)
    ap.add_argument("--fichas", default=os.environ.get(
        "CORPUS_FICHAS", os.path.join(RAIZ, "corpus", "fichas")))
    ap.add_argument("--corpus", default=os.environ.get(
        "CORPUS_DIR", os.path.join(RAIZ, "corpus")))
    ap.add_argument("--hoje", required=True, help="data do parecer, AAAA-MM-DD")
    a = ap.parse_args()

    d = json.load(io.open(a.achados, encoding="utf-8"))
    ids = {x.get("decide") for x in d["achados"] if x.get("decide")}
    lits = literais(ids, a.fichas)
    verif, pver = versao(a.corpus)

    os.makedirs(a.saida, exist_ok=True)
    io.open(os.path.join(a.saida, "parecer-conformidade.md"), "w",
            encoding="utf-8").write(render_parecer(d, lits, verif, pver, a.hoje) + "\n")
    io.open(os.path.join(a.saida, "checklist-conformidade.md"), "w",
            encoding="utf-8").write(render_checklist(d, verif) + "\n")

    faltando = sorted(i for i in ids if i not in lits)
    if faltando:
        print("AVISO: sem literal no corpus: " + ", ".join(faltando), file=sys.stderr)
    print("parecer e checklist em %s · %d achados · %d linhas de checklist"
          % (a.saida, len(d["achados"]), len(d["checklist"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
