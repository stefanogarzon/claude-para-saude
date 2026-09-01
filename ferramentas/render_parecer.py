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
from validar_parecer import JARGAO
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


NOME_NORMA = {
    "CEM": "Código de Ética Médica", "CP": "Código Penal",
    "CC": "Código Civil", "CDC": "Código de Defesa do Consumidor",
    "MCI": "Marco Civil da Internet", "LGPD": "LGPD",
    "SEC": "padrão técnico", "PROV": "política do fornecedor",
    "STJ": "STJ",
}


def partes_base(bid, corpus):
    """`CEM:art87` vira ("Código de Ética Médica", "art. 87", "prontuário...").

    A ementa ja existia em toda ficha, e o renderer ja a carregava — mas so a
    imprimia no anexo. No parecer saia o id cru, que para um medico e nome de
    arquivo, nao referencia de norma. A convencao medico-juridica e "art. 87 do
    CEM"; `CEM:art87` e convencao de programador.
    """
    norma, _, disp = bid.partition(":")
    if norma.startswith("CFM-"):
        p = norma.split("-")
        rotulo_norma = "Res. CFM %s/%s" % (p[1][:1] + "." + p[1][1:], p[2]) \
            if len(p) == 3 else norma
    elif norma.startswith("ANPD-"):
        p = norma.split("-")
        rotulo_norma = "Res. ANPD %s/%s" % (p[1], p[2]) if len(p) == 3 else norma
    else:
        rotulo_norma = NOME_NORMA.get(norma, norma)
    disp = re.sub(r"^art(\d+)", lambda m: "art. %sº" % m.group(1)
                  if int(m.group(1)) <= 9 else "art. " + m.group(1), disp)
    disp = disp.replace("anexo", "anexo ").replace("§", ", §").strip()
    e = corpus.get(bid) or {}
    em = (e.get("ementa") or "").rstrip(".")
    # A ementa foi escrita para o corpus, nao para o parecer: sete delas trazem
    # `NGS2`, `S-RES`, `BAA`, `Zero Data Retention`. Reusa-la e bom negocio nas
    # outras 208, e nestas seria trocar um jargao (o id) por outro. Quando ela
    # traz termo da lista negra, o parecer fica so com a norma e o artigo — que
    # ja e legivel, e e o que a convencao medico-juridica usa.
    if em and any(x in em for x in JARGAO):
        em = ""
    return rotulo_norma, disp, (em[:1].lower() + em[1:] if em else "")


def coluna_base(ids, corpus, vistos):
    """Celula de base legal: a citacao, e o que o dispositivo exige.

    A linha do parecer e uma cadeia: o projeto faz X, isso contraria o inciso Y,
    que exige W, entao faca Z. Sem a ementa o terceiro elo some, e a linha passa
    a mandar o leitor deduzir de `LGPD, art. 11, §4` por que aquilo e problema.

    O custo da ementa e a repeticao, nao ela mesma: no caso 03 o art. 87 do CEM
    saia por extenso em cinco linhas do mesmo documento. Entao sai uma vez por
    documento, na primeira linha que cita o dispositivo; `vistos` carrega esse
    estado entre as linhas e entre os blocos.

    O nome da norma sai uma vez por celula. Quando nenhum dos dispositivos dela
    precisa de ementa, os artigos se juntam: `Res. CFM 1.821/2007, arts. 3º e 4º`.
    """
    por_norma = collections.OrderedDict()
    for b in ids:
        norma, disp, em = partes_base(b, corpus)
        if b in vistos:
            em = ""
        vistos.add(b)
        por_norma.setdefault(norma, []).append(
            ("%s — %s" % (disp, em)) if em else disp)

    def junta(ds):
        if len(ds) > 1 and all(x.startswith("art. ") and " — " not in x
                               for x in ds):
            return "arts. " + ", ".join(x[5:] for x in ds[:-1]) + " e " + ds[-1][5:]
        return "; ".join(ds)
    return " · ".join("%s, %s" % (n, junta(ds)) for n, ds in por_norma.items())


VAZIAS = {"o", "a", "os", "as", "de", "da", "do", "das", "dos", "e", "em", "no",
          "na", "nos", "nas", "que", "um", "uma", "por", "para", "com", "se",
          "ou", "ao", "aos", "à", "às", "qual", "quais", "onde", "como", "há",
          "sem", "cada", "seu", "sua"}


def conteudo(s):
    return {w for w in re.sub(r"[^\w áéíóúâêôãõç]", " ", s.lower()).split()
            if len(w) > 2 and w not in VAZIAS}


def celula_acao(g, situacao):
    """Uma instrucao por linha, e a pergunta de checagem so quando ela acrescenta.

    Em achado `pergunta` falta informacao, e a checagem e o primeiro passo. Mas
    em 26 dos 86 gatilhos a checagem e a mitigacao dizem a mesma coisa em vozes
    diferentes — `quais campos a tarefa exige` e `enviar so os campos que a
    tarefa exige`. Imprimir as duas enche a celula sem dizer nada a mais.

    O corte e por sobreposicao de palavras de conteudo: da checagem para a
    mitigacao, 60% ou mais, sai so a mitigacao.
    """
    m = g["mitigacao"]
    c = g.get("checar") or ""
    if situacao != "P" or not c:
        return m
    pc = conteudo(c)
    if pc and len(pc & conteudo(m)) / len(pc) >= 0.6:
        return m
    return "Checar: %s. Depois: %s" % (c, m)


def render(d, cat, corpus, verif, pver, hoje, vigente):
    idx = {g["id"]: g for g in cat}
    achados = []
    for i, t in enumerate(d["a"]):
        gid, ori, sit = t[0], t[1], t[2]
        ev = t[3] if len(t) > 3 else None
        acao = t[4] if len(t) > 4 else "voce"
        g = idx.get(gid)
        if not g:
            continue
        achados.append({"g": g, "ori": ori, "sit": sit, "ev": ev, "acao": acao})
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

    # A RESPOSTA vem antes de tudo. Ate aqui as quatro primeiras linhas eram
    # metadado de metodo — versao do distribuivel, split de confianca do corpus,
    # teto de alcance — e o aviso legal vinha antes de qualquer palavra sobre o
    # caso. Quem perguntou "posso fazer isso?" precisava atravessar nove linhas
    # sobre o proprio documento, e depois decodificar `bloq.` numa celula de
    # tabela, para descobrir que a resposta era nao. O metodo desceu para o pe do
    # documento; a resposta subiu.
    firmes = [a for a in achados
              if a["g"]["severidade"].startswith("bloqueante") and a["sit"] == "C"]
    perg_b = [a for a in achados
              if a["g"]["severidade"].startswith("bloqueante") and a["sit"] == "P"]
    if d.get("veredito"):
        L.append("**%s**\n" % d["veredito"])
    elif firmes:
        L.append("**Não, do jeito que está hoje.** %d ponto(s) do que foi descrito "
                 "contraria norma em vigor.\n" % len(firmes))
    elif perg_b:
        L.append("**Depende de %d resposta(s) que só você tem.** Nada do que foi "
                 "descrito contraria norma de forma clara, mas há pontos em que a "
                 "resposta errada põe o serviço em desconformidade.\n" % len(perg_b))
    else:
        L.append("**Nada do que foi descrito contraria norma em vigor.**\n")

    if d.get("agora"):
        L.append("**Hoje:** %s\n" % d["agora"])
    if d.get("passado"):
        L.append("**Sobre o que já rodou:** %s\n" % d["passado"])

    L.append(AVISO + "\n")

    L.append("## 1. Objeto avaliado\n")
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

    # Achados agrupados por QUEM EXECUTA, nao por severidade.
    #
    # Vinte e nove linhas de peso visual identico nao dizem por onde comecar. Na
    # mesma coluna conviviam "desligar o treino na configuracao do provedor" —
    # dois minutos, o proprio medico faz — e "estender a certificacao ao
    # componente", que depende do fornecedor do prontuario e talvez nao exista.
    # Sem separar as duas, o documento parece exigir vinte e nove coisas
    # igualmente urgentes, e a pessoa nao faz nenhuma.
    #
    # O agrupamento sai do campo `acao` de cada achado, que o modelo preenche
    # dizendo a quem cabe. Era isso que a SKILL sempre pediu — "traduza todo
    # achado tecnico em tres formas de acao: exigir da TI, perguntar ao
    # fornecedor, registrar" — e que a refatoracao de vocabulario fechado
    # removeu do esquema sem que nenhum criterio de aprovacao notasse.
    # Titulo nominal, e o destinatario dentro dele. A linha de ajuda sob cada
    # bloco saiu: dizia o que o titulo ja diz.
    BLOCOS = [
        ("voce", "Ações do próprio serviço"),
        ("fornecedor", "Exigências ao fornecedor"),
        ("contrato", "Instrumentos contratuais"),
        ("fora", "Pontos fora do alcance do serviço"),
    ]
    ORDEM_ACAO = {k: i for i, (k, _) in enumerate(BLOCOS)}

    def dono(a):
        return (a.get("acao") or "voce") if isinstance(a.get("acao"), str) else "voce"

    L.append("## 2. Achados e ações\n")
    n_b = sum(1 for a in achados if a["g"]["severidade"].startswith("bloqueante"))
    n_p = sum(1 for a in achados if a["sit"] == "P")
    # A divisao primaria e confirmado contra depende-de-informacao, e nao o peso.
    # Com a fase 3 enxergando o que lhe escapava, um caso com repositorio passou
    # de 29 para 36 achados — e 22 deles sao pergunta. Aberto pelo peso, o leitor
    # le 36 exigencias; aberto pela situacao, le 14 e uma lista do que falta
    # informar.
    n_c = len(achados) - n_p
    L.append("%d pontos a tratar: **%d confirmados** pelo material e **%d que "
             "dependem de informação** que ninguém deu ainda. Por peso: %d "
             "impeditivos, %d de risco.\n"
             % (len(achados), n_c, n_p, n_b, len(achados) - n_b))

    # `vistos` atravessa os quatro blocos: a ementa de um dispositivo sai na
    # primeira linha que o cita, e nas seguintes sai so a citacao.
    vistos = set()
    for chave, titulo in BLOCOS:
        do_bloco = [a for a in achados if dono(a) == chave]
        if not do_bloco:
            continue
        L.append("### %s\n" % titulo)
        L.append("| # | Achado | Peso | Base legal | Ação |")
        L.append("|---|---|---|---|---|")
        for a in do_bloco:
            g = a["g"]
            sev = ("impeditivo" if g["severidade"].startswith("bloqueante")
                   else g["severidade"].split()[0])
            marca = " †" if g["norma"] and not vigente else ""
            onde = " (visto em `%s`)" % a["ev"] if a["ev"] else ""
            base = coluna_base(g["base"], corpus, vistos)
            # A pergunta de checagem entra na linha do achado a que pertence.
            # Ela saia numa lista propria ao fim da secao, repetindo os 31 ids
            # para que o leitor cruzasse os dois.
            L.append("| %s | %s%s | %s · %s%s | %s | %s |"
                     % (a["num"], g["efeito"], onde, sev,
                        rotulo(SITUACAO, a["sit"]), marca, base,
                        celula_acao(g, a["sit"])))
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
        L.append("**Res. CFM 2.454/2026, em vigor desde 26/08/2026:** %d achados "
                 "acima decorrem dela, como exigência corrente." % len(da_norma))
        if so:
            L.append("Sem base fora dela: %s."
                     % ", ".join("**%s**" % a["num"] for a in so))
        L.append("")

    esc = d.get("esc") or []
    L.append("## 3. Encaminhamentos\n")
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
    L.append("## 5. Cobertura do catálogo\n")
    L.append("Catálogo: %d gatilhos em %d seções. Dispararam %d, de %d seções, "
             "%d como pergunta. Os demais ou tiveram a seção afastada na triagem, "
             "ou não foram encontrados no material. A varredura cobriu as seções "
             "carregadas, não o catálogo inteiro.\n"
             % (len(cat), len({g["secao"] for g in cat}), len(disparou),
                len(secoes_com), perg))

    # anexo: literal de cada dispositivo, uma vez
    ids = []
    for a in achados:
        for b in a["g"]["base"]:
            if b not in ids:
                ids.append(b)
    L.append("Texto integral dos dispositivos citados: `anexo-normativo.md`, "
             "com URL e data de verificação.\n")

    # Metodo no pe, nao no topo. Continua no documento, e continua verificavel —
    # so deixou de ser a primeira coisa que o medico le.
    # Metodo no pe, em linhas de dado. Eram tres paragrafos de prosa.
    n_conf = sum(1 for e in corpus.values()
                 if e.get("confianca") == "primária-conferida")
    L.append("## Método\n")
    L.append("- Corpus conferido em fonte primária em **%s**: %d dispositivos "
             "palavra por palavra, %d em parte."
             % (verif or "?", n_conf, len(corpus) - n_conf))
    L.append("- Distribuível v%s. Avaliação de %s." % (pver or "?", hoje))
    if d["alc"] == "D":
        L.append("- Base da avaliação: apenas o material escrito. Nada foi "
                 "verificado no sistema, no contrato ou na configuração. Item "
                 "afirmado aqui é item a comprovar.")
    L.append("")

    obs = [a for a in achados if a["ev"]]
    L.append("## Evidência técnica\n")
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
