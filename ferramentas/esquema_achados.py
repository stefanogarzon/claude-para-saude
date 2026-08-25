#!/usr/bin/env python3
"""Esquema do achados.json — vocabulario fechado.

O modelo le o projeto, CLASSIFICA dentro do catalogo e devolve so as variaveis.
Nao escreve prosa: nem titulo, nem analise, nem mitigacao. Tudo isso vem do
catalogo pelo id do gatilho.

Por que fechado. Medicao sobre os quatro casos, no formato anterior:

  - `checar`, `base` e `severidade` eram copia LITERAL do catalogo em 100% dos
    achados (4/4, 27/27, 41/41, 28/28)
  - `checklist.exigencia` tinha similaridade 0,96 com o titulo da diretriz
  - `decide` estava sempre dentro de `base[]`, sem uma excecao
  - 56 a 89% das linhas de checklist eram `nao-aplicavel` ou `indeterminado`,
    cada uma com ~100 caracteres de justificativa em prosa
  - 55 a 60% dos bytes nao passavam por conferencia nenhuma

O achado e uma TUPLA POSICIONAL de quatro: [gatilho, origem, situacao, evidencia].
Objeto com nome de campo custaria ~4x mais em 77 linhas, e nao ha campo opcional
que justifique.

Efeito colateral maior que o de custo: o texto do parecer passa a ser
deterministico. O T6 mediu Jaccard de 0,75 a 0,85 entre execucoes; a partir daqui
o que varia e apenas QUAIS gatilhos dispararam, que e o julgamento, e e o que
deve variar.
"""

# --- vocabulario fechado -----------------------------------------------------

ORIGEM = {"O": "observado", "D": "declarado", "A": "ausente"}
SITUACAO = {"C": "confirmado", "P": "pergunta"}
ALCANCE = {"O": "observado", "D": "declarado", "M": "misto"}

# Triagem. Cada campo e enum; `forn` e livre porque nome de produto nao se cataloga.
MATERIAL = {"R": "repositório", "C": "contrato ou documentação",
            "P": "descrição em prosa", "X": "combinação"}
DADO = {"ID": "identificado", "PS": "pseudonimizado", "AN": "anonimizado alegado",
        "SI": "sintético", "NA": "nenhum dado de paciente"}
PAPEL = {"ADC": "apoio à decisão clínica", "GTC": "geração de texto clínico",
         "TRI": "triagem", "COM": "comunicação com paciente",
         "ADM": "administrativo", "PES": "pesquisa"}
MODALIDADE = {"PRES": "presencial", "TELE": "telemedicina", "AMBOS": "ambos"}
ESTAGIO = {"IDEIA": "ideia", "PROTO": "protótipo", "PILOTO": "piloto",
           "PROD": "produção"}
DESTINO = {"RT": "responsável técnico", "JUR": "jurídico"}

TRIAGEM = [("mat", MATERIAL), ("dado", DADO), ("papel", PAPEL),
           ("mod", MODALIDADE), ("est", ESTAGIO)]

ROTULO_TRIAGEM = {
    "mat": "Material recebido", "dado": "Tipo de dado", "papel": "Papel da IA",
    "dec": "Contato com decisão clínica", "mod": "Modalidade",
    "est": "Estágio", "forn": "Fornecedor e região",
}

# Arquivos de diretriz, pelo numero. `afast` lista os que a triagem afastou.
ARQUIVOS = {
    "01": "uso clínico de LLM", "02": "custódia de dados de saúde",
    "03": "escolha de fornecedor e região", "04": "segurança técnica",
    "05": "responsabilidade e prova", "06": "desenvolvimento de software",
    "08": "desidentificação",
}

RAIZ_OBRIGATORIA = ["p", "alc", "tri", "a"]

# --- exemplo -----------------------------------------------------------------

EXEMPLO = {
    "p": "escriba de consulta em consultório de cardiologia",
    "alc": "D",
    "tri": {"mat": "P", "dado": "ID", "papel": "GTC", "dec": False,
            "mod": "PRES", "est": "PROD",
            "forn": "OpenAI ChatGPT, plano pessoal de consumidor; região não declarada"},
    "afast": ["06", "08"],
    "a": [["G02", "D", "C", None],
          ["G18", "D", "C", None],
          ["G51", "A", "P", None],
          ["G68", "A", "P", None]],
    "esc": [["escriba e transcrição de consulta, não classificados em nível de risco", "JUR"]],
    "fora": ["FDA", "EU AI Act"],
}
