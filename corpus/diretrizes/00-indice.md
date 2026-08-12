---
tipo: índice
atualizado: 2026-08-11
---

# Diretrizes

Camada de decisão do corpus. As fichas em `corpus/fichas/` servem para citar o texto da norma; estas diretrizes servem para decidir. Uma skill carrega a diretriz do tema; só busca a ficha quando precisa citar.

**94 diretrizes e 77 gatilhos**, em 8 arquivos. Todo identificador citado aponta para uma das 202 entradas do corpus, todas `primária-conferida`.

Antes de qualquer arquivo, leia `00-decisoes.md`. São sete decisões de projeto com precedência sobre as diretrizes.

| Arquivo | Tema | Público | Conteúdo |
|---|---|---|---|
| [`00-decisoes.md`](00-decisoes.md) | decisões de projeto R1 a R7 | todos | 7 decisões |
| [`01-uso-clinico-de-llm.md`](01-uso-clinico-de-llm.md) | o que o médico pode e não pode fazer com IA | médico, responsável técnico | 13 |
| [`02-custodia-de-dados-de-saude.md`](02-custodia-de-dados-de-saude.md) | guarda, prazos e compartilhamento | médico, responsável técnico, desenvolvedor | 15 |
| [`03-escolha-de-fornecedor-e-regiao.md`](03-escolha-de-fornecedor-e-regiao.md) | transferência internacional e qualificação do fornecedor | quem contrata, quem integra | 19 |
| [`04-seguranca-tecnica.md`](04-seguranca-tecnica.md) | criptografia, segredos, logs, incidente | desenvolvedor, responsável técnico | 18 |
| [`05-responsabilidade-e-prova.md`](05-responsabilidade-e-prova.md) | quem responde e como se prova diligência | médico, responsável técnico, jurídico | 14 |
| [`06-desenvolvimento-de-software.md`](06-desenvolvimento-de-software.md) | o que observar ao escrever código clínico | desenvolvedor | 11 |
| [`07-gatilhos-de-auditoria.md`](07-gatilhos-de-auditoria.md) | catálogo de padrões que acionam revisão | skill de auditoria | 77 gatilhos |
| [`08-desidentificacao.md`](08-desidentificacao.md) | reduzir identificabilidade e medir o risco residual | desenvolvedor, pesquisador | 4 |

## As sete decisões

| | Decisão |
|---|---|
| R1 | a Res. CFM 2.454/2026 vale a partir de 26/08/2026; diretriz dependente traz marcação |
| R2 | o que a Res. 2.314/2022 impõe à telemedicina não é regra geral |
| R3 | parâmetro do Safe Harbor americano não é exigência brasileira; lista canônica de quase-identificadores no arquivo 08 |
| R4 | três classes de retenção: A registro clínico, B trilha de auditoria, C log de aplicação |
| R5 | três controvérsias resolvidas pela leitura conservadora, e declaradas como leitura nossa |
| R6 | gatilho nunca é mais severo que a entrada que o sustenta, nem dispara em arquitetura lícita |
| R7 | recusa da IA não revoga base legal da LGPD nem interrompe a guarda do prontuário |

## Como a skill usa

1. Lê `00-decisoes.md`.
2. Carrega a diretriz do tema.
3. Aplica o enunciado e o bloco `Verificar`.
4. Para citar a norma, busca o identificador de `Base` na ficha e usa o campo `Literal`.
5. Caso caia em `Escalar se`, não decide. Registra e encaminha.

## Gatilhos

77 gatilhos: 35 `bloqueante`, 42 `risco`. A auditoria de 11/08/2026 rebaixou 21 severidades e eliminou 5 gatilhos que disparavam em arquitetura lícita. Cada linha traz o padrão observável, a severidade, os identificadores de ficha e a pergunta de checagem.

## Verificação

`ferramentas/validar_diretrizes.py` confere que todo identificador existe, que nenhuma diretriz se apoia em entrada abaixo de `primária-conferida`, que nenhum gatilho excede a severidade da base, e o tamanho dos arquivos. Roda limpo.

Auditoria adversarial em 11/08/2026, em seis frentes, registrada em `auditoria/D*.md`: cerca de 150 achados, todos aplicados ou justificados.

## Manutenção

Reverificar quando houver alteração normativa, e a cada seis meses. O arquivo 03 depende de política de fornecedor, que muda com frequência: reverificar antes de cada distribuição.
