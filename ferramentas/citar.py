#!/usr/bin/env python3
"""Devolve o texto literal de dispositivos do corpus, por identificador.

Lookup exato por id estavel. Nao ha busca semantica nem aproximacao: ou o id
existe, ou o script diz que nao existe. Stdlib pura, sem dependencia externa.

Uso:
    python3 citar.py CFM-2454-2026:art4
    python3 citar.py CFM-2454-2026:art4 LGPD:art11 CEM:art87
    python3 citar.py --fichas corpus/fichas CFM-2454-2026:art4
    python3 citar.py --campos literal,fonte CFM-2454-2026:art4
    python3 citar.py --listar                 # so os ids, um por linha
    python3 citar.py --json CFM-2454-2026:art4

Guardrails (espelham corpus/fichas/00-esquema.md):
  - id inexistente vira erro explicito, nunca silencio
  - entrada abaixo de `primaria-conferida` sai com aviso de ressalva obrigatoria
  - o campo Severidade sai inteiro, com o qualificador de escopo quando houver
    (decisao R6: o gatilho carrega o qualificador da ficha)

Saida: texto para o modelo ler. Nada de interpretacao, nada de resumo.
"""

import argparse
import glob
import json
import os
import re
import sys

# Campos do bloco, na ordem em que devem sair.
CAMPOS = ["ementa", "literal", "fonte", "confianca", "severidade",
          "aplicacao", "gatilhos", "incerteza", "relacionados",
          "tese", "verificacao"]

# Rotulo no markdown -> chave normalizada. Acento fora da chave, dentro do rotulo.
ROTULOS = {
    "Ementa": "ementa",
    "Literal": "literal",
    "Fonte": "fonte",
    "Confiança": "confianca",
    "Severidade": "severidade",
    "Aplicação": "aplicacao",
    "Gatilhos": "gatilhos",
    "Incerteza": "incerteza",
    "Relacionados": "relacionados",
    "Tese": "tese",
    "Verificação": "verificacao",
}

CONFIANCA_CITAVEL = "primária-conferida"

# Mesmo split do validar_fichas.py: cabecalho de nivel 2 que e so um id.
RE_BLOCO = re.compile(r"^## (?=[A-Za-z][\w\-\.§:]*$)", re.M)
RE_CAMPO = re.compile(r"^\*\*([^.*]+)\.\*\*[ \t]*(.*)$", re.M)
RE_ID = re.compile(r"^[A-Z][\w\-]*:[\w\-\.§]+$")


def carregar(dir_fichas):
    """Le todas as fichas e devolve {id: {campo: valor}}."""
    entradas = {}
    arquivos = sorted(f for f in glob.glob(os.path.join(dir_fichas, "*.md"))
                      if not os.path.basename(f).startswith("00-"))
    if not arquivos:
        erro(f"nenhuma ficha encontrada em {dir_fichas!r}")
    for caminho in arquivos:
        with open(caminho, encoding="utf-8") as fh:
            texto = fh.read()
        for parte in RE_BLOCO.split(texto)[1:]:
            linha0, _, corpo = parte.partition("\n")
            bid = linha0.strip()
            if ":" not in bid:
                continue
            if bid in entradas:
                erro(f"id duplicado no corpus: {bid} "
                     f"({entradas[bid]['_ficha']} e {os.path.basename(caminho)})")
            entradas[bid] = parse_bloco(corpo, os.path.basename(caminho))
    return entradas


def parse_bloco(corpo, ficha):
    """Extrai os campos **Rotulo.** de um bloco de dispositivo."""
    reg = {"_ficha": ficha}
    marcas = list(RE_CAMPO.finditer(corpo))
    for i, m in enumerate(marcas):
        chave = ROTULOS.get(m.group(1).strip())
        if not chave:
            continue
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(corpo)
        valor = (m.group(2) + "\n" + corpo[m.end():fim]).strip()
        # Corta a regua de separacao entre blocos.
        valor = re.sub(r"\n-{3,}\s*$", "", valor).strip()
        if chave in reg:
            continue  # primeira ocorrencia vence
        reg[chave] = valor
    return reg


def erro(msg, codigo=2):
    print(f"ERRO: {msg}", file=sys.stderr)
    sys.exit(codigo)


# Campos que NUNCA sao omitidos quando existem, qualquer que seja --campos.
# `incerteza` marca ponto nao pacificado ou regra de origem estrangeira. Omiti-lo
# entrega a regra crua sem a ressalva que a torna legivel — foi o que quase
# aconteceu com SEC:anonimizacao.quase-identificadores, cujo `literal` e a lista
# do Safe Harbor. Guardrail no codigo, nao no prompt: sobrevive a edicao da skill.
CAMPOS_FORCADOS = ["incerteza"]


def formatar(bid, reg, campos):
    campos = list(campos)
    for forcado in CAMPOS_FORCADOS:
        if reg.get(forcado) and forcado not in campos:
            campos.append(forcado)
    linhas = [f"## {bid}", f"_ficha: {reg['_ficha']}_", ""]
    conf = reg.get("confianca", "").strip()
    if conf and conf != CONFIANCA_CITAVEL:
        linhas += [
            f"> AVISO: confianca `{conf}`, abaixo de `{CONFIANCA_CITAVEL}`.",
            "> Nao pode ser citado como norma. Se usar, declare a ressalva no output.",
            "",
        ]
    for chave in campos:
        valor = reg.get(chave)
        if not valor:
            continue
        rotulo = next(k for k, v in ROTULOS.items() if v == chave)
        linhas.append(f"**{rotulo}.** {valor}" if "\n" not in valor
                      else f"**{rotulo}.**\n{valor}")
        linhas.append("")
    return "\n".join(linhas).rstrip()


def main():
    ap = argparse.ArgumentParser(add_help=True, description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="identificadores, ex. CFM-2454-2026:art4")
    ap.add_argument("--fichas", default=os.environ.get(
        "CORPUS_FICHAS", os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "corpus", "fichas")),
                    help="diretorio das fichas (padrao: corpus/fichas)")
    ap.add_argument("--campos", default=",".join(CAMPOS),
                    help="campos a devolver, separados por virgula")
    ap.add_argument("--listar", action="store_true",
                    help="lista todos os ids do corpus e sai")
    ap.add_argument("--json", action="store_true", help="saida em JSON")
    ap.add_argument("--permitir-nao-conferida", action="store_true",
                    help="devolve entrada abaixo de primaria-conferida (sai com aviso)")
    args = ap.parse_args()

    entradas = carregar(args.fichas)

    if args.listar:
        for bid in sorted(entradas):
            print(f"{bid}\t{entradas[bid]['_ficha']}")
        return 0

    if not args.ids:
        ap.error("informe ao menos um id, ou use --listar")

    campos = [c.strip() for c in args.campos.split(",") if c.strip()]
    desconhecidos = [c for c in campos if c not in CAMPOS]
    if desconhecidos:
        erro(f"campo invalido: {', '.join(desconhecidos)}. validos: {', '.join(CAMPOS)}")

    faltando, bloqueados, achados = [], [], []
    for bid in args.ids:
        if not RE_ID.match(bid):
            faltando.append((bid, "formato invalido, esperado NORMA:dispositivo"))
            continue
        reg = entradas.get(bid)
        if reg is None:
            faltando.append((bid, "nao existe no corpus"))
            continue
        conf = reg.get("confianca", "").strip()
        if conf and conf != CONFIANCA_CITAVEL and not args.permitir_nao_conferida:
            bloqueados.append((bid, conf))
            continue
        achados.append((bid, reg))

    if args.json:
        saida = {
            "encontrados": [
                dict({c: reg.get(c) for c in campos + CAMPOS_FORCADOS if reg.get(c)},
                     id=bid, ficha=reg["_ficha"])
                for bid, reg in achados
            ],
            "nao_encontrados": [{"id": b, "motivo": m} for b, m in faltando],
            "bloqueados_por_confianca": [{"id": b, "confianca": c} for b, c in bloqueados],
        }
        print(json.dumps(saida, ensure_ascii=False, indent=2))
    else:
        for bid, reg in achados:
            print(formatar(bid, reg, campos))
            print("\n---\n")
        for bid, conf in bloqueados:
            print(f"## {bid}\nBLOQUEADO: confianca `{conf}`, abaixo de "
                  f"`{CONFIANCA_CITAVEL}`. Nao cite como norma.\n\n---\n")
        for bid, motivo in faltando:
            print(f"## {bid}\nNAO ENCONTRADO: {motivo}. "
                  f"Nao reconstrua o texto de memoria.\n\n---\n", file=sys.stderr)

    return 1 if (faltando or bloqueados) else 0


if __name__ == "__main__":
    sys.exit(main())
