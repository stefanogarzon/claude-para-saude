#!/usr/bin/env python3
"""Esquema do achados.json — contrato entre a skill e o renderer.

O modelo emite DADOS. O renderer produz o documento. A divisao existe por dois
motivos, um de custo e um de correcao:

  custo    — 20,3% do parecer era literal de norma que o citar.py acabou de
             devolver, reemitido como saida a $25/1M. Mais 73,8% de prosa, boa
             parte dela boilerplate deterministico. O modelo passa a emitir so
             o que so ele sabe: qual gatilho disparou, com que evidencia.

  correcao — o validar_parecer.py tem onze conferencias e nenhuma compara o
             texto citado com o corpus. Parecer que parafraseasse a norma de
             memoria, com id e URL certos, passava. Com o literal injetado pelo
             renderer a partir do id, parafrasear deixa de ser possivel.

Campos obrigatorios e vocabulario fechado ficam aqui, num lugar so, lidos pelo
renderer e pelo validador.
"""

SEVERIDADES = ["bloqueante", "risco", "boa-prática"]
ORIGENS = ["observado", "declarado", "ausente"]
SITUACOES = ["confirmado", "pergunta"]
STATUS = ["conforme-verificado", "conforme-declarado", "lacuna",
          "nao-aplicavel", "indeterminado"]

# Campos da triagem, na ordem em que saem na secao 1.
TRIAGEM = ["material", "dado", "papel", "decisao_clinica", "modalidade",
           "estagio", "fornecedor", "regiao"]

RAIZ_OBRIGATORIA = ["projeto", "alcance", "triagem", "achados", "checklist"]
ACHADO_OBRIGATORIO = ["id", "titulo", "severidade", "origem", "situacao",
                      "base", "decide", "texto"]
LINHA_OBRIGATORIA = ["diretriz", "exigencia", "status"]

# `alcance` governa o teto do checklist: material so declarado nao produz
# conforme-verificado. Regra 3 da skill.
ALCANCES = ["observado", "declarado", "misto"]

EXEMPLO = {
    "projeto": "escriba de consulta em consultorio de cardiologia",
    "alcance": "declarado",
    "triagem": {
        "material": "descrição em prosa",
        "dado": "identificado (nome, data de nascimento, conteúdo clínico)",
        "papel": "geração de texto clínico — transcrição e escriba",
        "decisao_clinica": "não decide conduta; produz o registro que o médico assina",
        "modalidade": "presencial (define a aplicação da R2)",
        "estagio": "produção, há cerca de dois meses",
        "fornecedor": "OpenAI, ChatGPT, plano pessoal de consumidor",
        "regiao": "não declarada",
    },
    "premissas_afastadas": [
        {"arquivo": "08-desidentificacao",
         "porque": "não há alegação de anonimização nem de pseudonimização"}
    ],
    "achados": [
        {
            "id": "2.1",
            "titulo": "Conta pessoal de consumidor recebendo dado identificável de paciente",
            "severidade": "bloqueante",
            "origem": "declarado",
            "situacao": "confirmado",
            "base": ["CEM:art73", "PROV:comparativo"],
            "decide": "CEM:art73",
            "texto": "O áudio da consulta, com nome e data de nascimento, é enviado a "
                     "produto de consumidor cujo contrato não é o do CNPJ.",
            "leitura_adotada": None,
            "checar": "qual contrato ampara o tratamento, e em nome de quem",
            "acao": {
                "ti": "cortar o caminho até a conta pessoal",
                "fornecedor": "exigir contrato corporativo com cláusula de não treino",
                "registrar": "a base legal por finalidade, com data",
            },
            "evidencia": None,
        }
    ],
    "checklist": [
        {"diretriz": "uso-clinico:D3",
         "exigencia": "registro do uso de IA no prontuário",
         "status": "lacuna", "origem": "observado",
         "base": ["CFM-2454-2026:art4"],
         "proximo": "exigir campo próprio e versionamento do modelo"}
    ],
    "fornecedor": ["A empresa treina modelo com o conteúdo enviado?"],
    "ti": ["Cortar qualquer caminho do consultório à conta pessoal."],
    "registrar": ["Consentimento específico para o uso de IA — classe A da R4."],
    "fora_do_escopo": [
        {"assunto": "FDA", "porque": "o corpus cobre Brasil"}
    ],
    "escalar": [
        {"item": "enquadramento como agente de pequeno porte",
         "para": "jurídico", "porque": "leitura não pacificada"}
    ],
}
