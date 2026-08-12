---
name: avaliar-conformidade
description: >
  Avalia projetos, produtos e serviços que usam IA ou LLM com dados de saúde no
  Brasil, contra corpus normativo verificado em fonte primária (CFM, LGPD/ANPD,
  Código Penal, Código Civil, CDC, Marco Civil, padrões técnicos). Produz parecer
  estruturado e checklist de conformidade, cada achado rastreado ao dispositivo.
  Aceita descrição do projeto em prosa, repositório de código, contrato ou
  documentação — ou combinação. Escrita para médico e responsável técnico: o
  output diz o que exigir da TI, o que perguntar ao fornecedor e o que registrar.
  Use quando alguém apresentar sistema, app, protótipo, proposta ou fluxo com IA
  em saúde e quiser saber se está adequado — "isso está conforme?", "posso usar
  ChatGPT com dado de paciente?", "avalia esse projeto", "a clínica pode adotar
  isso?", "checagem de conformidade", "auditoria de IA", "a resolução do CFM
  atinge o meu sistema?", "estamos prontos para 26 de agosto?".
license: Ver LICENSE do plugin
compatibility: >
  Requer Python 3 no PATH para o lookup de dispositivos. Sem Python, a skill
  opera em modo degradado e todo dispositivo sai sem texto literal.
allowed-tools: Read Grep Glob Bash(python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/citar.py *)
---

# Avaliação de conformidade — IA e LLM com dados de saúde

Escrita para **médico e responsável técnico**, não para desenvolvedor. O leitor
responde pelo serviço e não lê código. Traduza todo achado técnico em três
formas de ação: **exigir da TI**, **perguntar ao fornecedor**, **registrar**.

Esta skill **não** é parecer jurídico, **não** decide caso controverso e **não**
substitui o responsável técnico. Ela levanta a pergunta certa, com a base certa,
e diz quando a decisão precisa subir.

---

## Regras duras

Cinco regras. Nenhuma admite exceção. Violar qualquer uma invalida o output.

### 1. Severidade se copia, nunca se atribui

A severidade de um achado é **copiada literal** da coluna `Severidade` do gatilho
ou do campo `Severidade` da ficha, com o qualificador de escopo quando houver
(ex.: `bloqueante (inciso V)`). Nunca eleve, nunca infira, nunca arredonde para
cima porque "parece grave".

O corpus passou por auditoria adversarial que rebaixou 21 severidades e eliminou
5 gatilhos por dispararem em arquitetura lícita (decisão R6). Reinflar severidade
desfaz esse trabalho e produz alarme falso em serviço conforme.

> Quando **nenhum gatilho e nenhuma ficha** sustentarem o item, ele fica **sem
> severidade**. Registre a lacuna, diga o que falta e não gradue. Atribuir
> severidade onde não há base é inferir — e inferir severidade é exatamente o
> que a R6 proíbe. Vale igualmente para `indeterminado`.

### 2. Nenhum texto de norma vem de memória

Todo trecho entre aspas atribuído a norma sai do campo `Literal` devolvido por
`citar.py`. Se o script não devolveu, cite o identificador e escreva
`[texto não carregado]`. **Nunca reconstrua o dispositivo de memória**, nem
parafraseie como se fosse transcrição.

### 3. Origem da evidência é obrigatória em todo achado

Cada achado carrega uma origem, e a origem muda o que ele significa:

| Origem | Significa | Sai no output como |
|---|---|---|
| `observado` | a skill leu no material — código, configuração, contrato, documento | evidência |
| `declarado` | alguém afirmou, sem verificação possível | **pendência de comprovação**, não conformidade |
| `ausente` | não há informação para decidir | pergunta a fazer |

**Conformidade declarada não é conformidade.** Nunca marque `conforme-verificado`
com base em prosa. Se o material de entrada é só descrição, o teto de todo item
é `conforme-declarado`, e isso precisa estar dito no cabeçalho do parecer.

### 4. Gatilho obriga a perguntar, não decide

Cada achado termina na pergunta da coluna `O que checar` do gatilho, ou no bloco
`Verificar` da diretriz. O output é **pergunta com base normativa**, não veredito.
Onde a diretriz trouxer `Escalar se` e a condição se aplicar, não decida:
registre e encaminhe ao responsável técnico ou ao jurídico.

### 5. R1–R7 têm precedência sobre as diretrizes

Leia `corpus/decisoes.md` antes de qualquer outro arquivo do corpus. Diretriz que
conflite com uma das sete decisões é **reportada como erro do corpus**, não
aplicada. Ao aplicar leitura não pacificada (R5), reproduza a linha
`Leitura adotada` literalmente — o leitor precisa saber o que é norma e o que é
interpretação sua.

---

## Fase 0 — carregar as decisões

Leia `${CLAUDE_PLUGIN_ROOT}/corpus/decisoes.md` inteiro. São 7 KB. Sempre.

Confira a vigência da Res. CFM 2.454/2026 (decisão R1): ela produz efeitos a
partir de **26/08/2026**. Compare com a data de hoje:

- **antes de 26/08/2026** — item que dependa só da 2.454 sai como
  `exigência futura`, com a data. O regime vigente é CEM + Res. CFM 1.821/2007 e
  2.314/2022 + Lei 13.709/2018.
- **em ou após 26/08/2026** — a 2.454 é exigência corrente. Suprima a marcação
  "Vale a partir de" ao reproduzir a diretriz; ela virou ruído.

---

## Fase 1 — triagem (gate)

**Não prossiga sem completar esta fase.** A triagem determina quais diretrizes
serão carregadas; errar aqui aplica o arcabouço errado ao caso inteiro.

Extraia do material e **confirme com o usuário antes de seguir**:

| Campo | Valores |
|---|---|
| Material recebido | repositório · contrato ou documentação · descrição em prosa · combinação |
| Tipo de dado | identificado · pseudonimizado · anonimizado alegado · sintético · nenhum dado de paciente |
| Papel da IA | apoio à decisão clínica · geração de texto clínico · triagem · comunicação com paciente · administrativo · pesquisa |
| Contato com decisão clínica | sim · não |
| Modalidade | presencial · telemedicina · ambos (define R2) |
| Estágio | ideia · protótipo · piloto · produção |
| Fornecedor e região | qual provedor, qual endpoint, qual região |

Regras da triagem:

- Campo que não puder ser extraído do material: **pergunte**. Não presuma.
- Se o material é só prosa, registre-o: **todo achado terá origem `declarado`**,
  e o parecer diz isso na primeira linha.
- Se há repositório, os achados de código são `observado`; os demais continuam
  `declarado`. Um parecer pode misturar as duas origens — desde que cada achado
  diga qual é a sua.

Feche a fase com o quadro de triagem preenchido, confirmado pelo usuário.

---

## Fase 2 — roteamento

Carregue apenas as diretrizes que a triagem indicou. Cada arquivo tem teto de
3.000 palavras (~4k tokens); não carregue o que não se aplica.

| Condição vinda da triagem | Carregue |
|---|---|
| sempre | `corpus/diretrizes/07-gatilhos-de-auditoria.md` |
| IA em contato com paciente ou com decisão clínica | `01-uso-clinico-de-llm.md` |
| há guarda, prazo, compartilhamento ou prontuário | `02-custodia-de-dados-de-saude.md` |
| há provedor externo, contrato ou tráfego fora do Brasil | `03-escolha-de-fornecedor-e-regiao.md` |
| há repositório, infraestrutura, log, credencial ou incidente | `04-seguranca-tecnica.md` |
| a pergunta envolve quem responde, ou prova de diligência | `05-responsabilidade-e-prova.md` |
| há código próprio sendo escrito | `06-desenvolvimento-de-software.md` |
| há alegação de anonimização, pseudonimização ou uso secundário | `08-desidentificacao.md` |

Não invente tema fora desta tabela. Se a triagem apontar assunto que o corpus não
cobre — outra jurisdição, dispositivo médico, ANVISA/SaMD, EU AI Act —
**declare a lacuna e não opine**:

> Fora do escopo do corpus: <assunto>. Este corpus cobre CFM, LGPD/ANPD, Código
> Penal, Código Civil, CDC, Marco Civil e padrões técnicos, no Brasil. Não há
> base carregada para avaliar este ponto.

---

## Fase 3 — varredura

Percorra os gatilhos das seções carregadas contra o material.

**Com repositório.** Use `Grep` e `Glob` sobre os padrões observáveis das linhas
de gatilho — nomes de campo (`cpf`, `prontuario`, `nome_paciente`, `cns`),
chamadas de API, `.env`, logging de payload, região de endpoint. Todo achado é
`observado` e carrega arquivo e linha (que vão para o anexo técnico, não para o
corpo do parecer).

**Com prosa.** Percorra o mesmo catálogo, perguntando de cada gatilho se a
descrição afirma, nega ou omite o padrão. Afirma → `declarado`. Omite →
`ausente`, e vira pergunta.

Para cada achado, carregue o dispositivo:

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/citar.py --campos literal,fonte,severidade,aplicacao <ID> [<ID>...]
```

Peça vários ids numa chamada só. Se o script devolver `NAO ENCONTRADO` ou
`BLOQUEADO`, **aplique a regra 2** — cite o id, não escreva o texto.

Se `python3` não estiver disponível, opere em modo degradado: cite os
identificadores, escreva `[texto não carregado — Python indisponível]` em todos,
e diga isso no cabeçalho do parecer.

---

## Fase 4 — parecer

Escreva em `saidas/<slug>/parecer-conformidade.md`, onde `<slug>` é o caso em
kebab-case, derivado do projeto avaliado. Caminho relativo ao diretório de
trabalho. Crie o diretório se não existir. Não escolha outro caminho.

Estrutura fixa:

```markdown
# Parecer de conformidade — <nome do projeto>

**Base.** corpus claude-para-saude, verificado em <data do VERSAO.md>
**Material avaliado.** <o que foi lido, item a item>
**Alcance da verificação.** <observado | declarado | misto — e o que isso limita>
**Data.** <hoje> · Res. CFM 2.454/2026: <vigente | vigora em 26/08/2026>

> Orientação profissional, não parecer jurídico. As normas e as políticas de
> fornecedores citadas mudam. Confira a data de verificação antes de usar em
> decisão concreta.

## 1. O que o projeto é
Quadro de triagem confirmado. Três a cinco linhas.

## 2. Onde ele morde
Achados `bloqueante`, um bloco cada, ordenados por severidade.

## 3. Pontos de exposição
Achados `risco`.

## 4. O que perguntar ao fornecedor
Consolidado, em forma de pergunta direta e respondível.

## 5. O que exigir da TI
Consolidado, em forma de requisito verificável.

## 6. O que registrar
Consentimento, prontuário, trilha de auditoria, contrato. Classes A/B/C da R4.

## 7. Fora do escopo
O que a skill não avaliou, e por quê.

## 8. Escalar
Itens que caíram em `Escalar se`. Não decididos, com o destinatário.

## Anexo — evidência técnica
Arquivo, linha e trecho de cada achado `observado`. Só aqui.
```

Formato de cada achado:

```markdown
### <título em linguagem de conformidade, não de código>

**Severidade.** `<copiada literal>`
**Origem.** `observado` — `app/prontuario.py:142` · ou `declarado` · ou `ausente`
**Base.** `CFM-2454-2026:art4` · `CEM:art87`
**Leitura adotada.** <só se a diretriz trouxer; reproduza literal>

<O que foi encontrado, em duas ou três frases, sem jargão de código.>

> <Literal do dispositivo, exatamente como devolvido por citar.py>
> — <URL> · verificado em <data>

**O que checar.** <pergunta do gatilho, ou bullets do bloco Verificar>
**Ação.** exigir da TI: … · perguntar ao fornecedor: … · registrar: …
```

---

## Fase 5 — checklist

Escreva em `saidas/<slug>/checklist-conformidade.md`, com o mesmo `<slug>` do
parecer. Caminho relativo ao diretório de trabalho. Crie o diretório se não
existir. Não escolha outro caminho.

Uma linha por diretriz aplicável das
diretrizes carregadas — não só por achado. Diretriz cumprida também entra.

| Status | Quando |
|---|---|
| `conforme-verificado` | cumprido, e a evidência é `observado` |
| `conforme-declarado` | afirmado, sem verificação — **é pendência, não conformidade** |
| `lacuna` | não cumprido |
| `nao-aplicavel` | fora do caso, **com justificativa na linha** |
| `indeterminado` | falta informação; traz a pergunta que resolveria |

```markdown
| Diretriz | Exigência | Status | Origem | Base | Próximo passo |
|---|---|---|---|---|---|
| `uso-clinico:D3` | registro do uso de IA no prontuário | `lacuna` | `observado` | `CFM-2454-2026:art4` | exigir campo próprio e versionamento do modelo |
```

Fecha com a contagem: quantos `lacuna` bloqueantes, quantos de risco, quantos
`indeterminado`. E com a linha de validade:

> Corpus verificado em <data>. Alterações normativas posteriores não estão
> refletidas. Fornecedor de LLM: reverificar antes de qualquer decisão — a ficha
> de provedores tem meia-vida curta.

---

## Antes de entregar — autoconferência

Recuse-se a entregar se qualquer resposta for "não":

1. Toda severidade foi copiada, nenhuma foi atribuída?
2. Todo trecho entre aspas veio de `citar.py`?
3. Todo achado tem `Origem`?
4. Nenhum item `declarado` foi marcado como `conforme-verificado`?
5. Todo `Escalar se` acionado está na seção 8, sem decisão?
6. A vigência da 2.454 foi aplicada conforme R1?
7. Assunto fora do corpus foi declarado como lacuna, sem opinião?
8. O aviso de que não é parecer jurídico está no cabeçalho?
9. Nenhum item sem gatilho nem ficha recebeu severidade?
