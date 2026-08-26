#!/usr/bin/env python3
"""Renderiza o parecer a partir do achados.json e do catalogo.

O modelo devolve tuplas [gatilho, origem, situacao, evidencia]. Tudo o mais —
o que o padrao e, a severidade, a base normativa, a pergunta de checagem, a
mitigacao e o literal da norma — sai do corpus aqui. O modelo nao escreve texto
de norma nem de mitigacao, entao nao pode parafrasear nenhum dos dois.

O literal de cada dispositivo sai UMA vez, em anexo, e nao a cada achado que o
invoca: no formato anterior o mesmo artigo era transcrito em todos os achados
que o citavam.

Uso:
    python3 ferramentas/render_parecer.py achados.json --saida <dir> --hoje AAAA-MM-DD
"""

import argparse
import collections
import io
import json
import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import citar
import gatilhos
from esquema_achados import (ORIGEM, SITUACAO, ALCANCE, ARQUIVOS, TRIAGEM,
                             ROTULO_TRIAGEM, DESTINO)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDEM = {"bloqueante": 0, "risco": 1, "boa-prática": 2}
ABREV = {"bloqueante": "bloq.", "risco": "risco", "boa-prática": "b.prát."}

AVISO = ("> Orientação profissional, não parecer jurídico. As normas e as "
         "políticas de fornecedores citadas mudam. Confira a data de verificação "
         "antes de usar em decisão concreta.")


def versao(dir_corpus):
    p = os.path.join(dir_corpus, "VERSAO.md")
    if not os.path.isfile(p):
        return None, None
    t = io.open(p, encoding="utf-8").read()
    v = re.search(r"^corpus_verificado_em:\s*(\S+)", t, re.M)
    pv = re.search(r"^plugin_version:\s*(\S+)", t, re.M)
    return (v.group(1) if v else None), (pv.group(1) if pv else None)


def rotulo(mapa, chave):
    return mapa.get(chave, chave)


def render(d, cat, corpus, verif, pver, hoje, vigente):
    idx = {g["id"]: g for g in cat}
    achados = []
    for i, t in enumerate(d["a"]):
        gid, ori, sit = t[0], t[1], t[2]
        ev = t[3] if len(t) > 3 else None
        g = idx.get(gid)
        if not g:
            continue
        achados.append({"g": g, "ori": ori, "sit": sit, "ev": ev})
    achados.sort(key=lambda x: (ORDEM.get(x["g"]["severidade"].split()[0], 9),
                                x["g"]["id"]))
    # Numeracao `B1`/`R1`, nao `2.1`/`3.1`. A anterior punha achados `risco` em
    # `3.x` enquanto todos vivem sob `## 2. Achados` e `## 3.` e outra secao — um
    # medico que pedisse ao responsavel tecnico "veja o 3.5" mandava a pessoa
    # para "Escalar". Documento que se pretende citavel nao pode ter duas coisas
    # com o mesmo numero.
    cont = collections.Counter()
    for a in achados:
        pre = "B" if a["g"]["severidade"].startswith("bloqueante") else "R"
        cont[pre] += 1
        a["num"] = "%s%d" % (pre, cont[pre])

    L = ["# Parecer de conformidade — %s\n" % d["p"]]
    L.append("corpus conferido em **%s** · distribuível v%s · alcance `%s` · %s"
             % (verif or "?", pver or "?", rotulo(ALCANCE, d["alc"]), hoje))
    # O split de confianca sai do proprio corpus. Afirmar "verificado em fonte
    # primaria" sem ressalva era falso para 20 dos 215 dispositivos — os que
    # foram conferidos contra informativo, e nao contra inteiro teor.
    n_conf = sum(1 for e in corpus.values()
                 if e.get("confianca") == "primária-conferida")
    if corpus:
        L.append("\n%d dos %d dispositivos do corpus foram conferidos em fonte "
                 "primária; %d o foram parcialmente, e cada ficha registra qual "
                 "é o caso." % (n_conf, len(corpus), len(corpus) - n_conf))
    if d["alc"] == "D":
        L.append("\nMaterial só declarado: o teto de todo item é "
                 "`conforme-declarado`. Conformidade declarada não é conformidade.")
    L.append("\n" + AVISO + "\n")

    L.append("## 1. O que o projeto é\n")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    for k, mapa in TRIAGEM:
        if d["tri"].get(k):
            L.append("| %s | %s |" % (ROTULO_TRIAGEM[k], rotulo(mapa, d["tri"][k])))
    L.append("| %s | %s |" % (ROTULO_TRIAGEM["dec"],
                              "sim" if d["tri"].get("dec") else "não"))
    if d["tri"].get("forn"):
        L.append("| %s | %s |" % (ROTULO_TRIAGEM["forn"], d["tri"]["forn"]))
    L.append("")
    afast = d.get("afast") or []
    if afast:
        # Sem afirmar o que os gatilhos fizeram: a frase anterior dizia "os
        # gatilhos desses arquivos nao dispararam" e a tabela abaixo trazia dois
        # achados de desidentificacao num caso que declarava desidentificacao
        # afastada. Arquivo de diretriz e secao de catalogo sao eixos diferentes,
        # e os ids de `Base` sao compartilhados entre eles — distincao interna
        # que o leitor nao tem por que conhecer, e que fazia o documento se
        # desmentir. E o nome do tema no lugar do numero do arquivo, que e
        # referencia que o usuario nao possui.
        L.append("A triagem afastou estes temas, por não se aplicarem ao caso: "
                 "%s.\n" % ", ".join(ARQUIVOS.get(a, a) for a in afast))

    L.append("## 2. Achados\n")
    n_b = sum(1 for a in achados if a["g"]["severidade"].startswith("bloqueante"))
    L.append("%d achado(s): %d bloqueante(s), %d de risco. "
             "`confirmado` é constatação; `pergunta` é o que a resposta errada "
             "poria em desconformidade.\n"
             % (len(achados), n_b, len(achados) - n_b))
    L.append("| # | O que faz | Risco | Base | Mitigação |")
    L.append("|---|---|---|---|---|")
    for a in achados:
        g = a["g"]
        sev = ABREV.get(g["severidade"].split()[0], g["severidade"])
        marca = " †" if g["norma"] and not vigente else ""
        onde = " · `%s`" % a["ev"] if a["ev"] else ""
        L.append("| %s | %s%s | `%s` · %s%s | %s | %s |"
                 % (a["num"], g["gatilho"], onde, sev,
                    rotulo(SITUACAO, a["sit"]), marca,
                    " · ".join("`%s`" % b for b in g["base"]), g["mitigacao"]))
    L.append("")

    # A virada de vigencia nao pode ser entregue como AUSENCIA. Ate aqui, o unico
    # efeito de a norma passar a valer era o simbolo † sumir da tabela — e simbolo
    # que desaparece se le como "resolvido", nao como "a norma entrou em vigor".
    # Quem leu o parecer na vespera precisa entender o que mudou.
    da_norma = [a for a in achados if a["g"]["norma"]]
    if da_norma and not vigente:
        L.append("† decorre da Res. CFM 2.454/2026, com efeitos a partir de "
                 "26/08/2026 — até lá é exigência futura.\n")
    elif da_norma:
        so = [a for a in da_norma if a["g"]["so_norma"]]
        L.append("**A Res. CFM 2.454/2026 está em vigor desde 26/08/2026.** %d "
                 "dos achados acima decorrem dela e são exigência corrente, sem "
                 "período de adaptação." % len(da_norma))
        if so:
            L.append("")
            L.append("Destes, %s %s de base fora da 2.454: até 25/08/2026 eram "
                     "advertência preventiva; hoje são exigência autônoma. São os "
                     "que mais mudaram de natureza nesta data."
                     % (", ".join("**%s**" % a["num"] for a in so),
                        "não dispõe" if len(so) == 1 else "não dispõem"))
        L.append("")

    L.append("#### O que checar, por achado\n")
    for a in achados:
        L.append("- **%s** — %s" % (a["num"], a["g"]["checar"]))
    L.append("")

    esc = d.get("esc") or []
    L.append("## 3. Escalar\n")
    L += ["- %s → **%s**" % (e[0], rotulo(DESTINO, e[1])) for e in esc] or \
         ["Nada a escalar."]
    L.append("")

    fora = d.get("fora") or []
    L.append("## 4. Fora do escopo\n")
    if fora:
        L.append("Este corpus cobre CFM, LGPD/ANPD, Código Penal, Código Civil, "
                 "CDC, Marco Civil e padrões técnicos, no Brasil. Não há base "
                 "carregada para: **%s**. O parecer não opina sobre eles.\n"
                 % ", ".join(fora))
    else:
        L.append("Nada fora do escopo.\n")

    # Cobertura: derivada, nao escrita pelo modelo — e AGORA honesta sobre o que
    # nao foi visto. A versao anterior dizia "os N restantes foram percorridos e
    # nao dispararam", contando sobre o catalogo INTEIRO. Mas a fase 2 carrega so
    # as secoes que a triagem indicou: num caso que afastou seis dos sete
    # arquivos, o parecer atestava 75 gatilhos percorridos. Era a unica frase do
    # documento que convertia varredura parcial em atestado de cobertura, e saia
    # em todo parecer, por codigo.
    #
    # Nao da para saber daqui QUAIS secoes a skill carregou — o achados.json nao
    # registra isso. Entao o parecer para de afirmar o que nao sabe: diz quantos
    # gatilhos dispararam, e que os demais ou nao se aplicam ou nao foram
    # avaliados, sem escolher por conta propria qual dos dois.
    disparou = {a["g"]["id"] for a in achados}
    perg = sum(1 for a in achados if a["sit"] == "P")
    secoes_com = {g["secao"] for g in cat if g["id"] in disparou}
    L.append("## 5. Cobertura\n")
    L.append("O catálogo tem %d gatilhos, em %d seções temáticas. **%d** "
             "dispararam neste caso, %d deles como pergunta, e vieram de %d "
             "seções."
             % (len(cat), len({g["secao"] for g in cat}), len(disparou), perg,
                len(secoes_com)))
    L.append("")
    L.append("Os demais gatilhos não constam deste parecer por uma de duas "
             "razões: a triagem afastou a seção a que pertencem, ou o padrão não "
             "foi encontrado no material. **Este documento não afirma que o "
             "catálogo inteiro foi percorrido.**\n")

    # anexo: literal de cada dispositivo, uma vez
    ids = []
    for a in achados:
        for b in a["g"]["base"]:
            if b not in ids:
                ids.append(b)
    L.append("O texto integral de cada dispositivo citado está em "
             "`anexo-normativo.md`, com URL e data de verificação.\n")

    obs = [a for a in achados if a["ev"]]
    L.append("## Anexo — evidência técnica\n")
    if obs:
        L.append("| Achado | Onde |")
        L.append("|---|---|")
        L += ["| %s | `%s` |" % (a["num"], a["ev"]) for a in obs]
    else:
        L.append("Não há. Nenhum achado tem origem `observado`.")
    L.append("")

    # Anexo em arquivo proprio. No mesmo documento ele era 82% dos bytes — 50 KB
    # de literal contra 11 KB de parecer — e nao e o que o medico le para decidir.
    A = ["# Anexo normativo — %s\n" % d["p"]]
    A.append("Transcrição dos **%d dispositivos citados neste parecer**. Não é o "
             "texto integral das normas, nem compilação de legislação: são apenas "
             "os dispositivos que sustentam os achados acima. Corpus conferido em "
             "%s.\n" % (len(ids), verif or "?"))
    # O aviso vive aqui tambem. Este arquivo e o que se encaminha isolado ao
    # juridico ou a diretoria clinica, e sem ressalva parece compendio normativo
    # autoritativo — 60 KB de texto de lei sem uma linha dizendo o que nao e.
    A.append(AVISO + "\n")
    faltando = []
    for i in ids:
        e = corpus.get(i)
        A.append("## `%s`\n" % i)
        if e and e.get("ementa"):
            A.append("%s\n" % e["ementa"])
        if e and e.get("literal"):
            A.append(e["literal"].rstrip())
            A.append("> — %s\n" % e.get("fonte", ""))
        else:
            faltando.append(i)
            A.append("[texto não carregado]\n")
    return "\n".join(L), "\n".join(A), faltando


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("achados")
    ap.add_argument("--saida", required=True)
    # `--hoje` decide se a Res. CFM 2.454/2026 sai como exigencia corrente ou
    # futura — a afirmacao factual mais consequente do documento. Era comparacao
    # de string sem parsing: `--hoje ontem` dava `'o' > '2'` e virava vigente por
    # acidente; `--hoje 2025-12-31` fazia o parecer negar uma norma em vigor.
    # Agora o default e a data do sistema, e formato invalido e erro duro.
    ap.add_argument("--hoje", type=date.fromisoformat, default=date.today(),
                    help="AAAA-MM-DD; omita para usar a data de hoje")
    ap.add_argument("--fichas", default=os.environ.get(
        "CORPUS_FICHAS", os.path.join(RAIZ, "corpus", "fichas")))
    ap.add_argument("--corpus", default=os.environ.get(
        "CORPUS_DIR", os.path.join(RAIZ, "corpus")))
    ap.add_argument("--catalogo", default=None)
    a = ap.parse_args()

    d = json.load(io.open(a.achados, encoding="utf-8"))
    cat = gatilhos.carregar(a.catalogo or os.path.join(
        a.corpus, "diretrizes", "07-gatilhos-de-auditoria.md"))
    corpus = citar.carregar(a.fichas)
    verif, pver = versao(a.corpus)
    vigente = a.hoje >= date(2026, 8, 26)

    texto, anexo, faltando = render(d, cat, corpus, verif, pver,
                                    a.hoje.isoformat(), vigente)
    os.makedirs(a.saida, exist_ok=True)
    io.open(os.path.join(a.saida, "parecer-conformidade.md"), "w",
            encoding="utf-8").write(texto + "\n")
    io.open(os.path.join(a.saida, "anexo-normativo.md"), "w",
            encoding="utf-8").write(anexo + "\n")

    if faltando:
        print("AVISO: sem literal no corpus: " + ", ".join(faltando), file=sys.stderr)
    print("parecer %d B · anexo %d B · %d achados · %s"
          % (len(texto.encode()), len(anexo.encode()), len(d["a"]), a.saida))
    return 0


if __name__ == "__main__":
    sys.exit(main())
