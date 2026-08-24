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
license: código MIT · corpus e skill CC BY-SA 4.0 — ver LICENSE do plugin
compatibility: >
  Requer Python 3 no PATH. As ferramentas fazem o lookup do corpus e renderizam
  o parecer; sem Python a skill não produz documento.
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

### 1. Severidade se copia, nunca se atribui

A severidade de um achado é **copiada literal** da coluna `Severidade` do gatilho
ou do campo `Severidade` da ficha, com o qualificador de escopo quando houver
(ex.: `bloqueante (inciso V)`). Nunca eleve, nunca infira, nunca arredonde para
cima porque "parece grave".

**A ordem de consulta é fixa, e é um passo, não um princípio.** Para cada achado:
procure primeiro a linha de gatilho que cobre o padrão observado e copie a
severidade dela. Só vá à ficha quando **nenhum** gatilho cobrir o padrão. Nunca
consulte os dois e escolha.

Quando as duas existirem e divergirem, vale a do gatilho. O gatilho é o
instrumento específico: ele grada o dispositivo para um padrão observável
concreto. A ficha é o **teto**, nunca o piso — a R6 já proíbe gatilho mais severo
que a entrada que o sustenta. Caso concreto: `CEM:art78` é `bloqueante` na ficha
e `risco` na linha de gatilho "ausência de evidência de orientação da equipe
quanto ao sigilo"; o achado sai `risco`.

O corpus passou por auditoria adversarial que rebaixou 21 severidades e eliminou
5 gatilhos por dispararem em arquitetura lícita (decisão R6). Reinflar severidade
desfaz esse trabalho e produz alarme falso em serviço conforme.

> Quando **nenhum gatilho e nenhuma ficha** sustentarem o item, ele fica **sem
> severidade**. Registre a lacuna, diga o que falta e não gradue. Atribuir
> severidade onde não há base é inferir — e inferir severidade é exatamente o
> que a R6 proíbe. Vale igualmente para `indeterminado`.

### 2. Você não escreve norma

Não há campo de texto de norma no `achados.json`. O literal, a URL e a data são
injetados por `render_parecer.py` a partir do id em `decide`. Não transcreva, não
parafraseie, não resuma dispositivo — nem no campo `texto`, que é a sua análise.

> **O campo `Base.` se copia, como o literal.** Reproduza os ids do campo `Base`
> do gatilho ou da diretriz que disparou o achado, e só eles. Não acrescente
> dispositivo que reforça o argumento, não junte bases de dois gatilhos num
> achado só, não complete a lista com o que "também se aplica".

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

Severidade e situação são eixos distintos. Severidade é o peso da norma e vem do
gatilho. Situação é se o padrão foi afirmado, e vem da origem:

| Origem | `situacao` |
|---|---|
| `observado`, ou `declarado` que afirma o padrão | `confirmado` |
| só `ausente` | `pergunta` |

Um dispositivo `bloqueante` continua `bloqueante` quando ninguém sabe se o
serviço o descumpre — muda que aquilo é **pergunta**, não constatação. Achado com
origem só `ausente` nunca é reportado como violação.

Pareamento unidirecional: todo achado `pergunta` tem linha `indeterminado` no
checklist. O inverso não é exigido.

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
| Onde gravar | proponha `saidas/<slug>/`, com `<slug>` derivado do projeto em kebab-case, e confirme o caminho com o usuário junto do resto da triagem |

Regras da triagem:

- Campo que não puder ser extraído do material: **pergunte**. Não presuma.
- O campo `Onde gravar` é **proposto pela skill e confirmado pelo usuário**, não
  adivinhado. O diretório de trabalho pode não ser o repositório do projeto, e
  frequentemente não é. Proponha o caminho, mostre-o por extenso e siga com o que
  o usuário confirmar. As fases 4 e 5 gravam nesse caminho, e em nenhum outro.
- Se o material é só prosa, registre-o: **todo achado terá origem `declarado`**,
  e o parecer diz isso na primeira linha.
- Se há repositório, os achados de código são `observado`; os demais continuam
  `declarado`. Um parecer pode misturar as duas origens — desde que cada achado
  diga qual é a sua.

Feche a fase com o quadro de triagem preenchido, confirmado pelo usuário.

---

## Fase 2 — roteamento

**A porta é uma só e fecha aqui.** Um arquivo entra quando cumpre as **duas**
colunas: a condição da triagem *e* a premissa de escopo. Falhar qualquer uma o
deixa de fora, e ficar de fora significa **não existir para o resto da
execução** — sem gatilho, sem achado, sem linha de checklist. Aparece uma vez, em
`premissas_afastadas`.

| Arquivo | Condição da triagem | **E** premissa de escopo |
|---|---|---|
| `07-gatilhos-de-auditoria.md` | sempre | — |
| `01-uso-clinico-de-llm` | contato com paciente ou decisão clínica | idem |
| `02-custodia-de-dados-de-saude` | guarda, prazo, compartilhamento, prontuário | há dado de paciente sob guarda |
| `03-escolha-de-fornecedor-e-regiao` | provedor externo, contrato, tráfego fora do Brasil | há dado de paciente indo ao fornecedor |
| `04-seguranca-tecnica` | repositório, infra, log, credencial, incidente | há dado de saúde no sistema |
| `05-responsabilidade-e-prova` | quem responde, prova de diligência | há dado de paciente, ou ato médico apoiado por IA |
| `06-desenvolvimento-de-software` | código próprio | código tratando dado de paciente **ou chamando LLM** |
| `08-desidentificacao` | alegação de anonimização, pseudonimização, uso secundário | idem |

**Carregue apenas `07-gatilhos-de-auditoria.md`.** Os demais arquivos não são
lidos inteiros: a coluna decide quais ficam *elegíveis*, e os blocos deles são
buscados um a um na fase 3, depois que um gatilho dispara.

Silêncio do material não supre premissa ausente. Se a triagem confirmou "nenhum
dado de paciente", `04-seguranca-tecnica` fica de fora e o gatilho de `.env`
versionado **não dispara** só porque ninguém falou do `.env`. Fazê-lo é disparar
em arquitetura lícita, que a R6 proíbe.

No `06` a premissa é alternativa: software que **integra LLM** entra sem dado de
paciente. É por essa porta que os gatilhos de OWASP valem num projeto sem
paciente nenhum.

Assunto que o corpus não cobre — outra jurisdição, dispositivo médico,
ANVISA/SaMD, EU AI Act — entra em `fora_do_escopo`. **Não opine.** No campo
`porque`, escreva só o que é específico daquele assunto: a frase sobre o que o
corpus cobre é do renderer, e repeti-la duplica o texto no parecer.

---

## Fase 3 — varredura

### Passo 1 — percorrer os gatilhos

Percorra as linhas de `07-gatilhos-de-auditoria.md` cujo `Base` pertença a
arquivo elegível pela fase 2. A tabela já traz `Gatilho`, `Severidade`, `Base` e
`O que checar` — é ela que decide o achado.

**Com repositório.** `Grep` e `Glob` sobre os padrões observáveis: nomes de campo
(`cpf`, `prontuario`, `nome_paciente`, `cns`), chamadas de API, `.env`, logging
de payload, região de endpoint. Achado é `observado`, com arquivo e linha.

**Com prosa.** De cada gatilho, pergunte se a descrição afirma, nega ou omite o
padrão. Afirma → `declarado`. Nega → sem achado. Omite → `ausente`, vira pergunta.

### Passo 2 — carregar o que os gatilhos pediram

Dois lookups, em lote, só sobre o que disparou.

Dispositivos, para severidade e ementa:

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/citar.py --campos ementa,severidade <ID>...
```

Blocos de diretriz, para `Escalar se` e `Leitura adotada`:

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/diretriz.py --campos escalar,leitura uso-clinico:D3 seguranca:D7
```

`--listar` mostra os 94 blocos com título. Peça vários ids numa chamada só.
Acrescente `verificar` **apenas** quando o `O que checar` do gatilho não bastar.

**Não peça `literal`.** O texto da norma não entra no seu output — quem o injeta
é o renderer, pelo id de `decide`. Pedir literal gasta contexto sem destino.

Sem `python3`, opere em modo degradado: registre os ids, não invente severidade,
e diga no campo `alcance` que o corpus não foi carregado.

---

## Fase 4 — emitir `achados.json`

Grave **um arquivo**, `achados.json`, no caminho confirmado na triagem. Não
escreva markdown: `render_parecer.py` produz o parecer e o checklist a partir
deste JSON.

```json
{
  "projeto": "<nome curto>",
  "alcance": "observado | declarado | misto",
  "triagem": {"material":"", "dado":"", "papel":"", "decisao_clinica":"",
              "modalidade":"", "estagio":"", "fornecedor":"", "regiao":""},
  "premissas_afastadas": [{"arquivo":"08-desidentificacao", "porque":""}],
  "achados": [
    {"id":"2.1", "titulo":"<linguagem de conformidade, não de código>",
     "severidade":"bloqueante", "origem":"observado|declarado|ausente",
     "situacao":"confirmado|pergunta",
     "base":["CEM:art73","CP:art154"], "decide":"CEM:art73",
     "texto":"duas ou três frases, sem jargão de código",
     "leitura_adotada": null,
     "checar":"<pergunta do gatilho>",
     "acao":{"ti":"", "fornecedor":"", "registrar":""},
     "evidencia":{"arquivo":"app.py","linha":"57-61"}}
  ],
  "checklist": [
    {"diretriz":"uso-clinico:D3", "exigencia":"", "status":"lacuna",
     "origem":"observado", "base":["CFM-2454-2026:art4"], "proximo":""}
  ],
  "fornecedor": ["<pergunta direta e respondível>"],
  "ti": ["<requisito verificável>"],
  "registrar": ["<classe A/B/C da R4>"],
  "fora_do_escopo": [{"assunto":"FDA", "porque":"o corpus cobre Brasil"}],
  "escalar": [{"item":"", "para":"jurídico|responsável técnico", "porque":""}]
}
```

Regras do formato, todas verificadas por `validar_parecer.py`:

- `id` é `N.N`. `N` é **2** para `bloqueante` e **3** para `risco`. A sequência é
  contínua dentro da seção, atravessando confirmados e perguntas.
- `decide` é o dispositivo que **decide** o ponto, e tem de estar em `base`. É
  dele que o renderer tira o literal, a URL e a data.
- `evidencia` só quando `origem` é `observado`. Vai para o anexo, não para o
  corpo.
- `situacao` sai da tabela da regra 3: `observado` ou `declarado` que afirma o
  padrão → `confirmado`; só `ausente` → `pergunta`.
- `checklist` traz uma linha por diretriz dos arquivos elegíveis na fase 2 — não
  dos oito. Diretriz cumprida também entra. `nao-aplicavel` é para diretriz de
  arquivo **elegível** cujo gatilho não disparou, e a linha traz a justificativa
  em `proximo`.
- `alcance` `declarado` proíbe qualquer `conforme-verificado`.
- Todo achado com `situacao` `pergunta` tem linha `indeterminado` no checklist. O
  inverso não é exigido.

Você **não** escreve texto de norma. Não há campo para isso, e é proposital: o
literal vem do corpus pelo id, não da sua memória.

---

## Fase 5 — renderizar

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/render_parecer.py <saida>/achados.json \
  --saida <saida> --hoje <AAAA-MM-DD>
```

Produz `parecer-conformidade.md` e `checklist-conformidade.md`. Data, versão do
corpus e literais saem do `VERSAO.md` e das fichas. Se o comando avisar que falta
literal para algum id, o `decide` está errado — corrija o JSON e rode de novo.

---

## Antes de entregar

`validar_parecer.py` confere sozinho: campos obrigatórios, vocabulário, ids
existentes, severidade acima da base, `decide` dentro de `base`, numeração `N.N`
por seção, `ausente` que virou `confirmado`, `conforme-verificado` com origem
declarada, teto do `alcance` e pareamento com o checklist. Não gaste turno
reconferindo isso.

Rode e corrija até sair 0:

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/validar_parecer.py <saida>/achados.json
```

Confira à mão só o que script nenhum alcança:

1. Cada severidade foi **copiada** do gatilho, não atribuída por parecer grave?
2. Onde gatilho e ficha divergiram, prevaleceu a do gatilho?
3. Item sem gatilho e sem ficha ficou **sem severidade**?
4. `base` reproduz o campo `Base` do gatilho que disparou, sem id acrescentado
   para reforçar o argumento?
5. A vigência da 2.454 foi aplicada conforme R1?
6. Assunto fora do corpus foi para `fora_do_escopo`, sem opinião?
7. Todo `Escalar se` acionado está em `escalar`, sem decisão tomada?
8. O `checklist` só tem linhas de arquivo elegível na fase 2?
