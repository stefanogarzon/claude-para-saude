#!/usr/bin/env python3
"""Valida o OUTPUT da skill de conformidade contra o corpus.

Analogo do validar_diretrizes.py, do outro lado do fluxo: la se confere que o
corpus e coerente; aqui se confere que o parecer nao extrapolou o corpus.

Confere:
  0. ha achado a validar — zero achado num parecer estruturado e FALHA, nao "ok"
  1. todo id citado existe no corpus
  2. nenhum id abaixo de `primaria-conferida` citado sem ressalva explicita
  3. severidade do achado nunca acima da maior severidade das suas bases
  4. todo achado tem Severidade, Origem, Base e Situacao
  5. achado com origem so `ausente` tem Situacao `pergunta`, nunca `confirmado`
  6. nenhuma linha `conforme-verificado` com origem `declarado` ou `ausente`
  7. toda citacao em bloco tem URL e data de verificacao
  8. as contagens declaradas no checklist batem com as linhas da tabela
  9. todo achado tem titulo numerado `N.N`
 10. `indeterminado` no checklist >= achados com Situacao `pergunta`
 11. o checklist declara a contagem das cinco situacoes, em tabela

A conferencia 0 existe porque a primeira versao exigia titulo `### N.N` enquanto
a SKILL.md especificava `### <titulo>` sem numero: um parecer escrito conforme a
spec produzia `achados: 0` e as conferencias 3, 4 e 5 rodavam sobre lista vazia,
em silencio. Validador que nao encontra nada tem de gritar, nao passar.

Uso:
    python3 validar_parecer.py <parecer.md> [checklist.md] [--fichas DIR]
"""

import argparse
import collections
import glob
import io
import json
import os
import re
import sys

ORDEM = {"boa-prática": 0, "risco": 1, "bloqueante": 2}

# O prefixo tem de ser MAIUSCULO. Os 20 prefixos do corpus sao todos assim —
# CEM, CP, CC, CDC, MCI, LGPD, PROV, SEC, STJ, CFM-####-####, ANPD-##-####.
# A versao anterior aceitava `[A-Z][\w\-]*`, que casa qualquer palavra
# capitalizada seguida de dois-pontos: um cabecalho de tabela `Arquivo:linha`
# no anexo tecnico virava "id inexistente no corpus". Exigir maiuscula em toda
# a extensao do prefixo mantem a deteccao de id errado dentro do namespace de
# ids, sem transformar prosa em falso positivo.
#
# O `(?<![\w.])` na frente fecha o resto do buraco, e ele custou dois runs do
# eval T6. `\b` sozinho casa depois de um ponto: o fixture do caso 04 chama-se
# `env.EXEMPLO` — maiusculo de proposito, para escapar do .gitignore do `.env` —
# e `env.EXEMPLO:5-8` no anexo virava o id `EXEMPLO:5-8`, inexistente no corpus.
# O validador reprovava a skill exatamente por fazer o que o criterio do caso 04
# exige: citar arquivo e linha no anexo. Extensao de arquivo nao e prefixo de id.
RE_ID = re.compile(r"(?<![\w.])([A-Z][A-Z0-9\-]*(?:-\d{4})?:[\w\-\.§]+)")
RE_SECAO = re.compile(r"^## (\d+)[\.\s]", re.M)
RE_SUB = re.compile(r"^### (.*)$", re.M)
RE_NUMERADO = re.compile(r"^(\d+\.\d+)\s+(.*)$")
RE_STATUS = re.compile(r"`(conforme-verificado|conforme-declarado|lacuna|"
                       r"nao-aplicavel|indeterminado)`")
STATUS = ["conforme-verificado", "conforme-declarado", "lacuna",
          "nao-aplicavel", "indeterminado"]


def carregar_corpus(dir_fichas):
    sev, conf = {}, {}
    arquivos = [f for f in glob.glob(os.path.join(dir_fichas, "*.md"))
                if not os.path.basename(f).startswith("00-")]
    if not arquivos:
        sys.exit(f"ERRO: nenhuma ficha em {dir_fichas!r}")
    for caminho in arquivos:
        texto = open(caminho, encoding="utf-8").read()
        for bloco in re.split(r"^## (?=[A-Za-z][\w\-\.§:]*$)", texto, flags=re.M)[1:]:
            bid = bloco.split("\n", 1)[0].strip()
            if ":" not in bid:
                continue
            m = re.search(r"\*\*Severidade\.\*\*\s*`?([\w\-á]+)`?", bloco)
            sev[bid] = m.group(1) if m else None
            c = re.search(r"\*\*Confiança\.\*\*\s*`?([\w\-áí]+)`?", bloco)
            conf[bid] = c.group(1) if c else None
    return sev, conf


def blocos_de_achado(texto):
    """Achado = subsecao `###` dentro das secoes 2 (bloqueante) e 3 (risco).

    Reconhece o bloco mesmo sem numero, mas devolve `num=None` nesse caso para
    que o chamador reclame. A versao anterior exigia `### N.N` e devolvia lista
    vazia num parecer escrito conforme a spec — as conferencias de severidade e
    de campos obrigatorios rodavam sobre nada, em silencio. A versao seguinte
    aceitava titulo sem numero e batizava de `2.?`, tambem em silencio: as
    referencias cruzadas das secoes 4 a 8 ("ver 2.5") nao resolvem sem numero.

    `####` nao casa aqui, de proposito: e o nivel dos divisores 2a/2b/3a/3b e de
    toda subdivisao das demais secoes.

    Devolve (num|None, secao, titulo, bloco).
    """
    secoes = list(RE_SECAO.finditer(texto))
    for i, s in enumerate(secoes):
        if int(s.group(1)) not in (2, 3):
            continue
        fim = secoes[i + 1].start() if i + 1 < len(secoes) else len(texto)
        corpo = texto[s.start():fim]
        marcas = list(RE_SUB.finditer(corpo))
        for j, m in enumerate(marcas):
            f = marcas[j + 1].start() if j + 1 < len(marcas) else len(corpo)
            titulo = m.group(1).strip()
            num = RE_NUMERADO.match(titulo)
            yield (num.group(1) if num else None), s.group(1), \
                  (num.group(2) if num else titulo), corpo[m.start():f]


def validar_json(caminho, sev, conf):
    """Confere o achados.json — o formato que a skill emite desde a v0.2.

    Mais estrito que a versao markdown, e por dois motivos. Primeiro, nao ha
    parser: campo ausente e campo ausente, nao "a regex nao casou". Segundo, o
    modelo nao emite mais o literal da norma — quem o injeta e o
    render_parecer.py, lendo o corpus pelo id em `decide` —, entao a conferencia
    de fidelidade do texto deixa de ser necessaria: ela virou impossivel de
    falhar por construcao. Era o unico buraco que as onze conferencias do
    markdown nao cobriam.
    """
    from esquema_achados import (SEVERIDADES, ORIGENS, SITUACOES, STATUS,
                                 ALCANCES, RAIZ_OBRIGATORIA,
                                 ACHADO_OBRIGATORIO, LINHA_OBRIGATORIA)
    problemas, avisos = [], []
    d = json.load(io.open(caminho, encoding="utf-8"))

    for c in RAIZ_OBRIGATORIA:
        if c not in d:
            problemas.append(f"raiz: falta `{c}`")
    if problemas:
        return d, problemas, avisos

    if d["alcance"] not in ALCANCES:
        problemas.append(f"alcance invalido: {d['alcance']}")

    contagem_sev = collections.Counter()
    contagem_sit = collections.Counter()
    perguntas = 0

    for a in d["achados"]:
        rot = a.get("id", "?")
        for c in ACHADO_OBRIGATORIO:
            if not a.get(c):
                problemas.append(f"achado {rot}: falta `{c}`")
        s = (a.get("severidade") or "").split()[0] if a.get("severidade") else ""
        if s and s not in SEVERIDADES:
            problemas.append(f"achado {rot}: severidade invalida {s!r}")
        contagem_sev[s] += 1
        if a.get("origem") not in ORIGENS:
            problemas.append(f"achado {rot}: origem invalida {a.get('origem')!r}")
        if a.get("situacao") not in SITUACOES:
            problemas.append(f"achado {rot}: situacao invalida {a.get('situacao')!r}")
        contagem_sit[a.get("situacao")] += 1
        if a.get("situacao") == "pergunta":
            perguntas += 1
        # 5 — origem `ausente` nunca vira constatacao
        if a.get("origem") == "ausente" and a.get("situacao") == "confirmado":
            problemas.append(f"achado {rot}: origem `ausente` com situacao "
                             f"`confirmado` — e pergunta, nao constatacao")
        # 9 — numeracao N.N, e a secao bate com a severidade
        if not re.match(r"^\d+\.\d+$", str(rot)):
            problemas.append(f"achado {rot}: id fora do formato N.N")
        else:
            secao = rot.split(".")[0]
            esperada = {"bloqueante": "2", "risco": "3"}.get(s)
            if esperada and secao != esperada:
                problemas.append(f"achado {rot}: severidade {s} pede secao "
                                 f"{esperada}, nao {secao}")
        # 1, 2, 3 — ids existem, sao citaveis, e a severidade nao passa da base
        bases = a.get("base") or []
        for b in bases:
            if b not in sev:
                problemas.append(f"achado {rot}: id inexistente no corpus — {b}")
            elif conf.get(b) and conf[b] != "primária-conferida":
                avisos.append(f"achado {rot}: {b} e {conf[b]}, exige ressalva")
        conhecidas = [sev[b] for b in bases if b in sev and sev[b] in ORDEM]
        if s in ORDEM and conhecidas:
            teto = max(ORDEM[x] for x in conhecidas)
            if ORDEM[s] > teto:
                problemas.append(f"achado {rot}: severidade {s} acima da maior "
                                 f"das bases")
        # 10 — `decide` tem de estar entre as bases: e dele que sai o literal
        if a.get("decide") and a["decide"] not in bases:
            problemas.append(f"achado {rot}: `decide` {a['decide']} nao esta em "
                             f"`base` — o renderer citaria norma que o achado "
                             f"nao invoca")

    linhas = d["checklist"]
    cont_status = collections.Counter()
    for l in linhas:
        rot = l.get("diretriz", "?")
        for c in LINHA_OBRIGATORIA:
            if not l.get(c):
                problemas.append(f"checklist {rot}: falta `{c}`")
        st = l.get("status")
        if st not in STATUS:
            problemas.append(f"checklist {rot}: status invalido {st!r}")
        cont_status[st] += 1
        # 6 — conformidade declarada nao e conformidade
        if st == "conforme-verificado" and l.get("origem") in ("declarado", "ausente"):
            problemas.append(f"checklist {rot}: `conforme-verificado` com origem "
                             f"`{l.get('origem')}`")
        for b in (l.get("base") or []):
            if b not in sev:
                problemas.append(f"checklist {rot}: id inexistente — {b}")

    # 7 — material so declarado tem teto `conforme-declarado`
    if d["alcance"] == "declarado" and cont_status.get("conforme-verificado"):
        problemas.append(f"alcance `declarado` com "
                         f"{cont_status['conforme-verificado']} linha(s) "
                         f"`conforme-verificado` — o teto e `conforme-declarado`")

    # 11 — pareamento unidirecional da regra 3
    indet = cont_status.get("indeterminado", 0)
    if indet < perguntas:
        problemas.append(f"pareamento: {perguntas} achado(s) com situacao "
                         f"`pergunta` para {indet} linha(s) `indeterminado`")

    # 0 — validador que nao encontra nada tem de gritar
    if not d["achados"]:
        problemas.append("nenhum achado no JSON")

    print(f"achados: {len(d['achados'])} · severidades {dict(contagem_sev)} · "
          f"situacao {dict(contagem_sit)}")
    print(f"checklist: {len(linhas)} linhas · {dict(cont_status)}")
    return d, problemas, avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("parecer")
    ap.add_argument("checklist", nargs="?")
    ap.add_argument("--fichas", default="corpus/fichas")
    args = ap.parse_args()

    sev, conf = carregar_corpus(args.fichas)
    print(f"corpus: {len(sev)} entradas")
    problemas, avisos = [], []

    # `.json` e o formato corrente; `.md` fica para os pareceres ja gravados.
    if args.parecer.endswith(".json"):
        _, problemas, avisos = validar_json(args.parecer, sev, conf)
        for p in problemas:
            print(f"  - {p}")
        if avisos:
            print(f"avisos: {len(avisos)}")
            for a in avisos:
                print(f"  ~ {a}")
        print(f"problemas: {len(problemas)}")
        return 1 if problemas else 0

    parecer = open(args.parecer, encoding="utf-8").read()
    achados = list(blocos_de_achado(parecer))
    contagem_sev = collections.Counter()
    contagem_sit = collections.Counter()

    # 0 — o validador precisa falhar alto quando nao tem o que validar.
    # Zero achado num parecer que tem secao 2 ou 3 nao e "tudo certo": e
    # conferencia que nao rodou.
    if not achados:
        if RE_SECAO.search(parecer):
            problemas.append(
                "NENHUM achado reconhecido, mas o parecer tem secoes numeradas. "
                "As conferencias de severidade e de campos obrigatorios NAO rodaram.")
        else:
            problemas.append("NENHUM achado reconhecido — estrutura do parecer "
                             "nao bate com a esperada (## 2. / ## 3. com ### por achado)")

    # 4 — campos obrigatorios; 3 — severidade nao inflada; 9 — titulo numerado
    for num, secao, titulo, bloco in achados:
        if num is None:
            problemas.append(
                f"achado em `## {secao}.` sem numero `N.N`: {titulo[:60]} — "
                f"as referencias cruzadas das secoes 4 a 8 nao resolvem sem ele")
            num = f"{secao}.?"
        for campo in ("**Severidade.**", "**Origem.**", "**Base.**", "**Situação.**"):
            if campo not in bloco:
                problemas.append(f"achado {num} — falta {campo}")
        m = re.search(r"\*\*Severidade\.\*\*\s*`?([\w\-á]+)`?", bloco)
        if not m:
            continue
        s = m.group(1)
        contagem_sev[s] += 1
        if s not in ORDEM:
            problemas.append(f"achado {num} — severidade invalida: {s}")
            continue
        linha_base = re.search(r"\*\*Base\.\*\*(.*)", bloco)
        bases = RE_ID.findall(linha_base.group(1)) if linha_base else []
        if not bases:
            problemas.append(f"achado {num} — sem base")
            continue
        teto = max((ORDEM.get(sev.get(b) or "", -1) for b in bases), default=-1)
        if teto >= 0 and ORDEM[s] > teto:
            inv = {v: k for k, v in ORDEM.items()}
            problemas.append(
                f"achado {num} — severidade `{s}` ACIMA da base `{inv[teto]}`: {titulo[:50]}")

        # Situacao x Origem: `ausente` nunca e violacao confirmada, e uma pergunta
        # cuja resposta errada seria violacao. Confundir os dois transforma
        # parecer sobre prosa em catastrofe aparente.
        msit = re.search(r"\*\*Situação\.\*\*\s*`?(confirmado|pergunta)`?", bloco)
        morig = re.search(r"\*\*Origem\.\*\*(.*)", bloco)
        if msit:
            contagem_sit[msit.group(1)] += 1
            origem = morig.group(1) if morig else ""
            so_ausente = "ausente" in origem and not re.search(
                r"observado|declarado", origem)
            if so_ausente and msit.group(1) != "pergunta":
                problemas.append(
                    f"achado {num} — origem so `ausente` mas Situação `{msit.group(1)}`; "
                    f"deveria ser `pergunta`")
            if not so_ausente and msit.group(1) == "pergunta" and "ausente" not in origem:
                avisos.append(f"achado {num} — Situação `pergunta` com origem afirmativa")

    # 1 e 2 — ids citados
    textos = {"parecer": parecer}
    if args.checklist:
        textos["checklist"] = open(args.checklist, encoding="utf-8").read()
    citados = set()
    for nome, texto in textos.items():
        for cid in sorted(set(RE_ID.findall(texto))):
            citados.add(cid)
            if cid not in sev:
                problemas.append(f"{nome}: id inexistente no corpus — {cid}")
            elif conf.get(cid) not in ("primária-conferida", None):
                # aceita se houver ressalva explicita perto da mencao
                if not re.search(rf"{re.escape(cid)}.{{0,400}}?"
                                 rf"(ressalva|primária-parcial|não conferid)",
                                 texto, re.S | re.I):
                    problemas.append(
                        f"{nome}: cita `{cid}` ({conf[cid]}) sem ressalva explicita")

    # 6 — citacoes em bloco com fonte
    citacoes = re.findall(r"(?:^>.*\n)+", parecer, re.M)
    sem_fonte = [c for c in citacoes
                 if "verificado em" not in c and "http" not in c]
    if sem_fonte:
        avisos.append(f"{len(sem_fonte)} bloco(s) de citacao sem URL/data "
                      f"(pode ser citacao interna, conferir a mao)")

    # 5 e 7 — checklist
    if args.checklist:
        chk = textos["checklist"]
        linhas = [l for l in chk.splitlines()
                  if l.startswith("|") and l.count("|") >= 6
                  and RE_STATUS.search(l)]
        real = collections.Counter()
        for l in linhas:
            col = [c.strip() for c in l.strip("|").split("|")]
            m = RE_STATUS.search(col[2]) if len(col) > 2 else None
            if not m:
                continue
            st = m.group(1)
            real[st] += 1
            origem = col[3] if len(col) > 3 else ""
            if st == "conforme-verificado" and ("declarado" in origem or "ausente" in origem):
                problemas.append(
                    f"checklist: `conforme-verificado` com origem {origem} — {col[0][:40]}")
        print(f"checklist: {sum(real.values())} linhas")
        for st in STATUS:
            # 11 — contagem ausente e problema, nao traco. Sem a linha declarada
            # a conferencia 8 nao roda, e passava em silencio quando o checklist
            # fechava com lista de marcadores em vez da tabela da fase 5.
            m = re.search(rf"\|\s*`{re.escape(st)}`\s*\|\s*\**(\d+)", chk)
            declarado = int(m.group(1)) if m else None
            marca = "" if declarado is None or declarado == real[st] else "  <-- NAO BATE"
            if declarado is None:
                problemas.append(
                    f"checklist: contagem de `{st}` nao declarada — a tabela de "
                    f"contagem da fase 5 e obrigatoria, e lista nao e lida")
            elif declarado != real[st]:
                problemas.append(
                    f"checklist: contagem de `{st}` declarada {declarado}, real {real[st]}")
            print(f"  {st:22} real={real[st]:>3}  declarado="
                  f"{declarado if declarado is not None else '—':>3}{marca}")

        # 10 — pareamento unidirecional: todo achado `pergunta` tem de ter uma
        # linha `indeterminado`. O inverso nao se exige, entao a conferencia e
        # por piso, nao por igualdade: um checklist pode registrar falta de
        # informacao que nao virou bloco no parecer.
        perguntas = contagem_sit["pergunta"]
        if real["indeterminado"] < perguntas:
            problemas.append(
                f"pareamento: {perguntas} achado(s) com Situação `pergunta` mas "
                f"so {real['indeterminado']} linha(s) `indeterminado` no checklist")

    print(f"achados: {len(achados)} blocos · severidades {dict(contagem_sev)}"
          f" · situacao {dict(contagem_sit)}")
    print(f"ids citados: {len(citados)}")
    print(f"problemas: {len(problemas)}")
    for p in problemas:
        print("  -", p)
    if avisos:
        print(f"avisos: {len(avisos)}")
        for a in avisos:
            print("  ~", a)
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
