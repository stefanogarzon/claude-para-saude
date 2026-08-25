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


def validar_json(caminho, sev, conf, catalogo=None):
    """Confere o achados.json de vocabulario fechado.

    Quase tudo e verificavel, ao contrario do formato anterior, em que 55 a 60%
    dos bytes eram prosa livre sem conferencia nenhuma. Aqui o modelo so escolhe
    dentro de conjuntos fechados, e escolha fora do conjunto e erro, nao estilo.

    A conferencia de severidade sumiu, e sumiu por construcao: a severidade nao
    e mais emitida pelo modelo — vem do catalogo pelo id do gatilho. Inflar
    severidade deixou de ser possivel.
    """
    import gatilhos as G
    from esquema_achados import (ORIGEM, SITUACAO, ALCANCE, MATERIAL, DADO,
                                 PAPEL, MODALIDADE, ESTAGIO, DESTINO, ARQUIVOS,
                                 RAIZ_OBRIGATORIA)
    problemas, avisos = [], []
    d = json.load(io.open(caminho, encoding="utf-8"))

    for c in RAIZ_OBRIGATORIA:
        if c not in d:
            problemas.append(f"raiz: falta `{c}`")
    if problemas:
        return d, problemas, avisos

    cat = G.carregar(catalogo or os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "corpus", "diretrizes", "07-gatilhos-de-auditoria.md"))
    idx = {g["id"]: g for g in cat}

    if d["alc"] not in ALCANCE:
        problemas.append(f"alcance fora do vocabulario: {d['alc']!r}")

    tri = d.get("tri") or {}
    for campo, mapa, nome in (("mat", MATERIAL, "material"), ("dado", DADO, "dado"),
                              ("papel", PAPEL, "papel"), ("mod", MODALIDADE, "modalidade"),
                              ("est", ESTAGIO, "estagio")):
        if campo not in tri:
            problemas.append(f"triagem: falta `{campo}`")
        elif tri[campo] not in mapa:
            problemas.append(f"triagem: {nome} fora do vocabulario: {tri[campo]!r} "
                             f"(vale {'/'.join(sorted(mapa))})")
    if "dec" in tri and not isinstance(tri["dec"], bool):
        problemas.append("triagem: `dec` tem de ser booleano")

    for x in (d.get("afast") or []):
        if x not in ARQUIVOS:
            problemas.append(f"afast: arquivo desconhecido {x!r}")

    vistos = collections.Counter()
    sevs = collections.Counter()
    perguntas = 0
    for i, t in enumerate(d["a"]):
        rot = f"achado[{i}]"
        if not isinstance(t, list) or not (3 <= len(t) <= 4):
            problemas.append(f"{rot}: tem de ser [gatilho, origem, situacao, evidencia]")
            continue
        gid, ori, sit = t[0], t[1], t[2]
        ev = t[3] if len(t) > 3 else None
        if gid not in idx:
            problemas.append(f"{rot}: gatilho inexistente no catalogo — {gid}")
        else:
            sevs[idx[gid]["severidade"].split()[0]] += 1
            for b in idx[gid]["base"]:
                if b not in sev:
                    problemas.append(f"{rot}: gatilho {gid} cita id inexistente "
                                     f"no corpus — {b} (erro do CORPUS)")
                elif conf.get(b) and conf[b] != "primária-conferida":
                    avisos.append(f"{rot}: {b} e {conf[b]}, exige ressalva")
        vistos[gid] += 1
        if ori not in ORIGEM:
            problemas.append(f"{rot}: origem fora do vocabulario: {ori!r}")
        if sit not in SITUACAO:
            problemas.append(f"{rot}: situacao fora do vocabulario: {sit!r}")
        if sit == "P":
            perguntas += 1
        # origem `ausente` nunca e constatacao — regra 3
        if ori == "A" and sit == "C":
            problemas.append(f"{rot}: origem `ausente` com situacao `confirmado` "
                             f"— e pergunta, nao constatacao")
        # evidencia so faz sentido no que foi observado, e e obrigatoria la
        if ori == "O" and not ev:
            problemas.append(f"{rot}: origem `observado` sem evidencia")
        if ori != "O" and ev:
            problemas.append(f"{rot}: evidencia com origem `{ori}` — so `O` tem "
                             f"arquivo e linha")

    for gid, n in vistos.items():
        if n > 1:
            problemas.append(f"gatilho {gid} repetido {n} vezes — um gatilho, um achado")

    for e in (d.get("esc") or []):
        if not isinstance(e, list) or len(e) != 2:
            problemas.append(f"escalar: {e!r} — tem de ser [item, destino]")
        elif e[1] not in DESTINO:
            problemas.append(f"escalar: destino fora do vocabulario: {e[1]!r}")

    if not d["a"]:
        problemas.append("nenhum achado no JSON")

    print(f"achados: {len(d['a'])} · severidades {dict(sevs)} · "
          f"perguntas {perguntas} · gatilhos distintos {len(vistos)}")
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
