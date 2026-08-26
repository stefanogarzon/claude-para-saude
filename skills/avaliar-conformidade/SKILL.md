---
name: avaliar-conformidade
description: >
  Avalia projetos, produtos e serviços que usam IA ou LLM com dados de saúde no
  Brasil, contra corpus normativo verificado em fonte primária (CFM, LGPD/ANPD,
  Código Penal, Código Civil, CDC, Marco Civil, padrões técnicos). Produz um
  parecer em tabela — o que o projeto faz, o risco, a legislação, a mitigação —
  com cada achado rastreado ao dispositivo, mais o anexo com o texto das normas
  citadas. Aceita descrição do projeto em prosa, repositório de código, contrato
  ou documentação — ou combinação. Escrita para médico e responsável técnico.
  Use quando alguém apresentar sistema, app, protótipo, proposta ou fluxo com IA
  em saúde e quiser saber se está adequado — "isso está conforme?", "posso usar
  ChatGPT com dado de paciente?", "avalia esse projeto", "a clínica pode adotar
  isso?", "checagem de conformidade", "auditoria de IA", "a resolução do CFM
  atinge o meu sistema?", "estou em dia com a 2.454?".
license: código MIT · corpus e skill CC BY-SA 4.0 — ver LICENSE do plugin
compatibility: >
  Requer Python 3 no PATH. O catálogo, a validação e a renderização passam pelas
  ferramentas; sem Python a skill não produz documento.
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*)
# `Bash(python3:*)` e nao o caminho completo do script: o matcher de
# permissao NAO expande ${CLAUDE_PLUGIN_ROOT}. Com a variavel no padrao,
# toda chamada fica aguardando aprovacao e, em modo nao interativo, nunca
# roda — o modelo entao le as fichas inteiras com Read, que e o oposto do
# que as ferramentas existem para fazer. Testado: `Bash(python3 ${...}/x.py *)`
# trava; `Bash(python3:*)` passa.
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

### 1. Você classifica, não descreve

O catálogo de gatilhos é o vocabulário. Cada achado é **um id do catálogo**, não
uma frase sua. Severidade, base normativa, pergunta de checagem e mitigação vêm
de lá — você não as escreve, não as parafraseia e não as completa.

Se o material mostra um padrão que o catálogo não cobre, ele **não vira achado**.
Registre em `esc` se merecer decisão humana, ou em `fora` se for outra jurisdição.
Inventar categoria é o mesmo que inventar norma.

### 2. Você não escreve norma nem mitigação

Não há campo para nenhuma das duas. O renderer as busca no corpus pelo id. Não
transcreva dispositivo, não resuma artigo, não sugira correção fora da coluna
`Mitigação` do catálogo.

### 3. Origem e situação são eixos distintos

| Origem | Significa |
|---|---|
| `O` observado | você leu no material — código, configuração, contrato |
| `D` declarado | alguém afirmou, sem verificação possível |
| `A` ausente | não há informação para decidir |

| Origem | `situação` |
|---|---|
| `O`, ou `D` que afirma o padrão | `C` confirmado |
| só `A` | `P` pergunta |

Um gatilho `bloqueante` continua `bloqueante` quando ninguém sabe se o serviço o
descumpre — muda que aquilo é **pergunta**, não constatação. Achado com origem
`A` nunca é reportado como violação.

**Conformidade declarada não é conformidade.** Material só em prosa: `alc` é
`D`, e nenhum item pode sair como verificado.

Evidência (`arquivo:linha`) é obrigatória quando a origem é `O`, e proibida nas
outras — o que não foi observado não tem onde.

### 4. Gatilho obriga a perguntar, não decide

Onde a diretriz trouxer `Escalar se` e a condição se aplicar, não decida:
registre em `esc` com o destinatário.

### 5. R1–R7 têm precedência sobre as diretrizes

Leia `corpus/decisoes.md` antes de qualquer outro arquivo. Diretriz que conflite
com uma das sete decisões é **reportada como erro do corpus**, não aplicada.

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

Apresente ao usuário por extenso; grave no JSON pelo código.

| Campo | Valores | código |
|---|---|---|
| Material recebido | repositório · contrato/documentação · prosa · combinação | `mat` `R`/`C`/`P`/`X` |
| Tipo de dado | identificado · pseudonimizado · anonimizado alegado · sintético · nenhum | `dado` `ID`/`PS`/`AN`/`SI`/`NA` |
| Papel da IA | apoio à decisão clínica · geração de texto clínico · triagem · comunicação com paciente · administrativo · pesquisa | `papel` `ADC`/`GTC`/`TRI`/`COM`/`ADM`/`PES` |
| Contato com decisão clínica | sim · não | `dec` booleano |
| Modalidade | presencial · telemedicina · ambos (define R2) | `mod` `PRES`/`TELE`/`AMBOS` |
| Estágio | ideia · protótipo · piloto · produção | `est` `IDEIA`/`PROTO`/`PILOTO`/`PROD` |
| Fornecedor e região | qual provedor, qual endpoint, qual região | `forn`, texto livre |
| Onde gravar | proponha `saidas/<slug>/`, em kebab-case, e confirme junto do resto | — |

Regras da triagem:

- Campo que não puder ser extraído do material: **pergunte**. Não presuma.
- O campo `Onde gravar` é **proposto pela skill e confirmado pelo usuário**, não
  adivinhado. O diretório de trabalho pode não ser o repositório do projeto, e
  frequentemente não é. Proponha o caminho, mostre-o por extenso e siga com o que
  o usuário confirmar. As fases 4 e 5 gravam nesse caminho, e em nenhum outro.
- Só prosa: `alc` é `D`, e todo achado sai `D` ou `A`.
- Com repositório: `alc` é `M`, achados de código são `O` com `arquivo:linha`, os
  demais seguem `D` ou `A`.

Feche a fase com o quadro de triagem preenchido, confirmado pelo usuário.

---

## Fase 2 — roteamento

**A porta é uma só e fecha aqui.** Um arquivo entra quando cumpre as **duas**
colunas: a condição da triagem *e* a premissa de escopo. Ficar de fora significa
não existir para o resto da execução. Liste os afastados em `afast`.

| Arquivo | Condição da triagem | **E** premissa de escopo |
|---|---|---|
| `01` uso clínico | contato com paciente ou decisão clínica | idem |
| `02` custódia | guarda, prazo, compartilhamento, prontuário | há dado de paciente sob guarda |
| `03` fornecedor | provedor externo, contrato, tráfego fora do Brasil | há dado de paciente indo ao fornecedor |
| `04` segurança | repositório, infra, log, credencial, incidente | há dado de saúde no sistema |
| `05` responsabilidade | quem responde, prova de diligência | há dado de paciente, ou ato médico apoiado por IA |
| `06` desenvolvimento | código próprio | código tratando dado de paciente **ou chamando LLM** |
| `08` desidentificação | alegação de anonimização ou pseudonimização | idem |

Silêncio do material não supre premissa ausente. Se a triagem confirmou "nenhum
dado de paciente", o gatilho de `.env` versionado **não dispara** só porque
ninguém falou do `.env`. Fazê-lo é disparar em arquitetura lícita, que a R6 proíbe.

No `06` a premissa é alternativa: software que **integra LLM** entra sem dado de
paciente. É por essa porta que os gatilhos de OWASP valem num projeto sem
paciente nenhum.

### Carregue o catálogo pelas seções que a triagem indicou

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/gatilhos.py --tsv --secao <seção>...
```

`--secoes` lista as dez com a contagem. Escolha por tema, não por arquivo de
diretriz: os ids de `Base` são compartilhados, então filtrar por arquivo elegível
não filtra nada.

A coluna `norma` do TSV diz de que norma o gatilho decorre quando isso muda o
regime. A Res. CFM 2.454/2026 está em vigor desde 26/08/2026 — é exigência
corrente, não futura. Não acrescente ressalva de vigência aos achados; o parecer
já traz o aviso, e o renderer o escreve sozinho.

| Seção | Deixe de fora quando |
|---|---|
| Envio de dado a LLM | — sempre entra |
| Identificadores e desidentificação | não há dado de paciente |
| Segredos e credenciais | não há repositório nem infraestrutura |
| Logs e telemetria | não há repositório nem infraestrutura |
| Criptografia e transporte | não há repositório nem infraestrutura |
| Retenção e descarte | não há dado sob guarda |
| Supervisão humana e registro clínico | não há contato com paciente nem decisão clínica |
| Consentimento e recusa | não há dado de paciente |
| Ambiente de teste | não há repositório |
| Governança e classificação de risco | — sempre entra |

Assunto que o corpus não cobre — outra jurisdição, dispositivo médico,
ANVISA/SaMD, EU AI Act — entra em `fora`, com o nome do assunto e nada mais.
**Não opine.**

---

## Fase 3 — classificar

Percorra as linhas do TSV contra o material. Cada linha é uma pergunta fechada:
**este padrão está presente?**

**Com repositório.** `Grep` e `Glob` sobre os padrões observáveis da coluna
`gatilho` — nomes de campo, chamadas de API, `.env`, logging de payload, região
de endpoint. Achado é `O`, com `arquivo:linha`.

**Com prosa.** De cada linha, a descrição afirma, nega ou omite o padrão?
Afirma → `D`. Nega → sem achado. Omite → `A`, e vira pergunta.

Um gatilho dispara **no máximo uma vez**. Se o padrão aparece em três lugares do
código, é um achado com a evidência mais forte, não três.

Só quando a diretriz precisar decidir escalonamento:

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/diretriz.py --campos escalar,leitura uso-clinico:D3
```

**Não chame `citar.py`.** O literal da norma não entra no seu output — o renderer
o busca pelo id. Carregá-lo gasta contexto sem destino.

---

## Fase 4 — emitir `achados.json`

Grave **um arquivo**, no caminho confirmado na triagem. Só variáveis:

```json
{"p":"escriba de consulta em cardiologia",
 "alc":"D",
 "tri":{"mat":"P","dado":"ID","papel":"GTC","dec":false,"mod":"PRES","est":"PROD",
        "forn":"OpenAI ChatGPT, plano pessoal; região não declarada"},
 "afast":["06","08"],
 "a":[["G02","D","C",null],
      ["G31","O","C","app.py:57-61"],
      ["G68","A","P",null]],
 "esc":[["escriba de consulta, não classificado em nível de risco","JUR"]],
 "fora":["FDA","EU AI Act"]}
```

Vocabulário, e nada fora dele:

| campo | valores |
|---|---|
| `alc` | `O` observado · `D` declarado · `M` misto |
| `mat` | `R` repositório · `C` contrato/documentação · `P` prosa · `X` combinação |
| `dado` | `ID` identificado · `PS` pseudonimizado · `AN` anonimizado alegado · `SI` sintético · `NA` nenhum |
| `papel` | `ADC` apoio à decisão · `GTC` geração de texto clínico · `TRI` triagem · `COM` comunicação · `ADM` administrativo · `PES` pesquisa |
| `mod` | `PRES` · `TELE` · `AMBOS` |
| `est` | `IDEIA` · `PROTO` · `PILOTO` · `PROD` |
| `afast` | `01` `02` `03` `04` `05` `06` `08` |
| destino em `esc` | `RT` responsável técnico · `JUR` jurídico |

`a` é uma lista de tuplas `[gatilho, origem, situação, evidência]`. Evidência é
`arquivo:linha` quando a origem é `O`, e `null` nas outras.

Escreva compacto, sem indentação. Não há campo de texto livre além de `p`,
`forn`, o item de `esc` e o assunto em `fora`.

---

## Fase 5 — renderizar e conferir

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/validar_parecer.py <saida>/achados.json
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/render_parecer.py <saida>/achados.json \
  --saida <saida> --hoje <AAAA-MM-DD>
```

O validador confere vocabulário, existência dos gatilhos, o par origem/situação,
evidência e repetição. Corrija até sair 0, depois renderize.

O renderer grava **dois** arquivos: `parecer-conformidade.md`, com a tabela de
achados, e `anexo-normativo.md`, com o texto integral dos dispositivos citados.
Diga ao usuário que são dois.

---

## Antes de entregar

O validador cobre quase tudo. Confira à mão só o que script nenhum alcança:

1. Cada gatilho que você marcou está mesmo presente no material, e não foi
   marcado por parecer provável?
2. Padrão que o catálogo não cobre ficou fora dos achados?
3. A vigência da 2.454 foi aplicada conforme R1?
4. Assunto fora do corpus foi para `fora`, sem opinião?
5. Todo `Escalar se` acionado está em `esc`, sem decisão tomada?
