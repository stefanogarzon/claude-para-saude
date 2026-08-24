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

> Medido: o mesmo conjunto de bases saiu `bloqueante` num run e `risco` noutro,
> porque um consultou a ficha tendo gatilho disponível. Gatilho primeiro, sempre.

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

> Quando o achado tiver mais de uma base, cite o **literal do dispositivo que
> decide** o ponto. Os demais entram como identificador em `Base.`, sem
> transcrição. Nunca transcreva de memória o que não foi carregado.

> **O campo `Base.` se copia, como o literal.** Reproduza os ids do campo `Base`
> do gatilho ou da diretriz que disparou o achado, e só eles. Não acrescente
> dispositivo que reforça o argumento, não junte bases de dois gatilhos num
> achado só, não complete a lista com o que "também se aplica".
>
> Medido: o mesmo achado substantivo saiu com `art12, anexoII` num run e com
> `art12, art13, anexoII` noutro. `Base.` é o que o parecer aponta como
> autoridade — base montada a cada execução é autoridade que muda de tamanho.

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

> Origem e situação são eixos distintos. A **severidade** é o peso da norma e
> vem do gatilho. A **situação** é se o padrão foi afirmado, e vem da origem:
>
> | Origem do achado | `Situação` |
> |---|---|
> | `observado`, ou `declarado` que afirma o padrão | `confirmado` |
> | só `ausente` | `pergunta` |
>
> Um dispositivo `bloqueante` continua `bloqueante` mesmo quando ninguém sabe se
> o serviço o descumpre — o que muda é que aquilo é **pergunta**, não
> constatação. Achado com origem só `ausente` **nunca** é reportado como
> violação.
>
> O pareamento com o checklist é **unidirecional**: todo achado com `Situação`
> `pergunta` **tem de** aparecer como `indeterminado`. O inverso não é exigido —
> o checklist **pode** trazer `indeterminado` sem achado correspondente, quando
> registra falta de informação que não merece bloco próprio no parecer. O que
> nunca se admite é o mesmo item sair `indeterminado` no checklist e como
> violação no parecer.

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

Carregue apenas as diretrizes que a triagem indicou. Cada arquivo tem teto de
3.000 palavras (~4k tokens); não carregue o que não se aplica.

**A porta é uma só, e fecha aqui.** Um arquivo entra quando cumpre as **duas**
colunas da tabela abaixo: a condição da triagem *e* a premissa de escopo. Falhar
qualquer uma o deixa de fora, e ficar de fora significa **não existir para o
resto da execução** — não gera gatilho, não gera achado e **não gera nenhuma
linha de checklist**. Ele aparece uma vez só, na frase de premissas afastadas da
seção 1 do parecer.

> Medido: a versão anterior filtrava duas vezes, aqui por condição e de novo no
> passo 0 da fase 3 por premissa de escopo, sem dizer qual das duas mandava. No
> caso sem dado de paciente, execuções diferentes da mesma entrada produziram
> checklists de 19 e de 69 linhas — a de 69 enumerou como `nao-aplicavel` cada
> diretriz dos arquivos afastados, e os dois achados reais ficaram no meio de 60
> linhas de ruído. Achado nenhum apareceu nas três execuções.

| Carregue | Condição vinda da triagem | **E** a premissa de escopo do arquivo |
|---|---|---|
| `07-gatilhos-de-auditoria.md` | sempre | — |
| `01-uso-clinico-de-llm.md` | IA em contato com paciente ou com decisão clínica | contato com paciente ou com decisão clínica |
| `02-custodia-de-dados-de-saude.md` | há guarda, prazo, compartilhamento ou prontuário | há dado de paciente sob guarda |
| `03-escolha-de-fornecedor-e-regiao.md` | há provedor externo, contrato ou tráfego fora do Brasil | há dado de paciente indo ao fornecedor |
| `04-seguranca-tecnica.md` | há repositório, infraestrutura, log, credencial ou incidente | há dado de saúde no sistema |
| `05-responsabilidade-e-prova.md` | a pergunta envolve quem responde, ou prova de diligência | há dado de paciente, ou ato médico apoiado por IA |
| `06-desenvolvimento-de-software.md` | há código próprio sendo escrito | há código próprio tratando dado de paciente **ou chamando LLM** |
| `08-desidentificacao.md` | há alegação de anonimização, pseudonimização ou uso secundário | há alegação de anonimização ou pseudonimização |

A premissa de escopo é o campo `tema:` do cabeçalho de cada arquivo, transcrito.
Silêncio do material não supre premissa ausente: se a triagem confirmou "nenhum
dado de paciente", `04-seguranca-tecnica` fica de fora, e o gatilho de `.env`
versionado **não vira pergunta bloqueante** só porque ninguém falou do `.env`.
Fazê-lo é disparar em arquitetura lícita, que é o que a R6 proíbe.

Repare no `06`: a premissa é alternativa. Software que **integra LLM** entra
mesmo sem dado de paciente — é por essa porta que os gatilhos de OWASP e de
comportamento do modelo continuam valendo num projeto sem paciente nenhum.

Registre no parecer, em uma frase, quais premissas a triagem afastou e o que isso
desligou. A ausência de achado bloqueante é resultado, e resultado se explica.

Não invente tema fora desta tabela. Se a triagem apontar assunto que o corpus não
cobre — outra jurisdição, dispositivo médico, ANVISA/SaMD, EU AI Act —
**declare a lacuna e não opine**:

> Fora do escopo do corpus: <assunto>. Este corpus cobre CFM, LGPD/ANPD, Código
> Penal, Código Civil, CDC, Marco Civil e padrões técnicos, no Brasil. Não há
> base carregada para avaliar este ponto.

---

## Fase 3 — varredura

### Passo 0 — a porta já fechou

A porta de aplicabilidade é da **fase 2**, e é única. Aqui não se reabre arquivo
afastado nem se reavalia premissa: percorra os gatilhos dos arquivos carregados e
mais nada.

O requisito de arquivo afastado que continue fazendo sentido como higiene técnica
não desaparece — entra nas seções 5 e 6 do parecer **sem severidade**, pela regra
1. Mas não vira achado, não vira gatilho e não vira linha de checklist.

### Passo 1 — percorrer os gatilhos

Percorra os gatilhos das seções carregadas contra o material.

**Com repositório.** Use `Grep` e `Glob` sobre os padrões observáveis das linhas
de gatilho — nomes de campo (`cpf`, `prontuario`, `nome_paciente`, `cns`),
chamadas de API, `.env`, logging de payload, região de endpoint. Todo achado é
`observado` e carrega arquivo e linha (que vão para o anexo técnico, não para o
corpo do parecer).

**Com prosa.** Percorra o mesmo catálogo, perguntando de cada gatilho **dos
arquivos carregados** se a descrição afirma, nega ou omite o padrão. Afirma →
`declarado`. Nega → não há achado. Omite → `ausente`, e vira pergunta.

Carregue os dispositivos em **duas etapas**. Pedir tudo de uma vez estoura o
limite de saída de ferramenta: `aplicacao` é a maior parte do volume e é
redundante com a diretriz na maioria dos casos.

**Etapa 1 — triagem ampla.** Sobre todos os candidatos, para decidir o que entra
no parecer e com que peso:

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/citar.py --campos ementa,severidade <ID> [<ID>...]
```

**Etapa 2 — literal.** Só para os que forem de fato citados, que são muito menos:

```
python3 ${CLAUDE_PLUGIN_ROOT}/ferramentas/citar.py --campos literal,fonte <ID> [<ID>...]
```

Peça vários ids numa chamada só, em cada etapa. Some `aplicacao` **apenas** quando
a diretriz não resolver o ponto — não por padrão. Se o script devolver
`NAO ENCONTRADO` ou `BLOQUEADO`, **aplique a regra 2** — cite o id, não escreva o
texto.

Se `python3` não estiver disponível, opere em modo degradado: cite os
identificadores, escreva `[texto não carregado — Python indisponível]` em todos,
e diga isso no cabeçalho do parecer.

---

## Fase 4 — parecer

Escreva o parecer em `parecer-conformidade.md`, **dentro do caminho confirmado no
campo `Onde gravar` da triagem**. Crie o diretório se não existir. Não escolha
outro caminho, e não invente um se o usuário não confirmou — volte e confirme.

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
Achados `bloqueante`, um bloco cada. Separados em dois, cada um com contagem própria:

#### 2a. Violações e pontos confirmados
Achados com `Situação` `confirmado`. Contagem própria na abertura do bloco.

#### 2b. Perguntas bloqueantes — resposta errada põe o serviço em desconformidade
Achados com `Situação` `pergunta`. Contagem própria na abertura do bloco.

## 3. Pontos de exposição
Achados `risco`, na mesma separação:

#### 3a. Violações e pontos confirmados
#### 3b. Perguntas de risco — resposta errada expõe o serviço

## 4. O que perguntar ao fornecedor
Consolidado, em forma de pergunta direta e respondível.

## 5. O que exigir da TI
Consolidado, em forma de requisito verificável.

## 6. O que registrar
Consentimento, prontuário, trilha de auditoria, contrato. Classes A/B/C da R4.
Subdivisão, se houver, em `####` — nunca `###`.

## 7. Fora do escopo
O que a skill não avaliou, e por quê.

## 8. Escalar
Itens que caíram em `Escalar se`. Não decididos, com o destinatário.
Subdivisão, se houver, em `####` — nunca `###`.

## Anexo — evidência técnica
Arquivo, linha e trecho de cada achado `observado`. Só aqui.
```

**Regra de níveis de título, e ela é verificável por script.** Dentro das seções
2 e 3, `###` é **exclusivamente** título de achado, sempre numerado `N.N`. Tudo o
mais que precise de subtítulo — os divisores `2a`/`2b`/`3a`/`3b`, e qualquer
subdivisão dentro das seções 1 e 4 a 8 — é `####`. Um `### 6.1` ou `### 8.1`
quebra a contagem automática tanto quanto um divisor promovido a `###`.

Formato de cada achado:

```markdown
### <N.N> <título em linguagem de conformidade, não de código>

**Severidade.** `<copiada literal>`
**Origem.** `observado` — `app/prontuario.py:142` · ou `declarado` · ou `ausente`
**Situação.** `confirmado` · ou `pergunta` — pela tabela da regra 3
**Base.** `CFM-2454-2026:art4` · `CEM:art87`
**Leitura adotada.** <só se a diretriz trouxer; reproduza literal>

<O que foi encontrado, em duas ou três frases, sem jargão de código.>

> <Literal do dispositivo, exatamente como devolvido por citar.py>
> — <URL> · verificado em <data>

**O que checar.** <pergunta do gatilho, ou bullets do bloco Verificar>
**Ação.** exigir da TI: … · perguntar ao fornecedor: … · registrar: …
```

O título é **numerado**, `N.N`, com `N` igual ao número da seção e a sequência
contínua dentro dela, atravessando os divisores `a` e `b`. A numeração é
funcional: as seções 4 a 8 fazem referência cruzada a achado ("ver 2.5"), e sem
número a referência não resolve.

---

## Fase 5 — checklist

Escreva o checklist em `checklist-conformidade.md`, **no mesmo caminho confirmado
do parecer**. Crie o diretório se não existir. Não escolha outro caminho.

Uma linha por diretriz **dos arquivos que a fase 2 carregou** — não só por
achado, e não dos oito. Diretriz cumprida também entra.

O tamanho do checklist é derivável antes de escrevê-lo: some as diretrizes dos
arquivos carregados. Se a fase 2 carregou dois dos oito, o checklist tem as
diretrizes desses dois. Arquivo afastado **não contribui com nenhuma linha** —
nem como `nao-aplicavel`. `nao-aplicavel` é para diretriz de arquivo **carregado**
cujo gatilho não disparou no caso, e a linha traz a justificativa.

| Status | Quando |
|---|---|
| `conforme-verificado` | cumprido, e a evidência é `observado` |
| `conforme-declarado` | afirmado, sem verificação — **é pendência, não conformidade** |
| `lacuna` | não cumprido |
| `nao-aplicavel` | fora do caso, **com justificativa na linha** |
| `indeterminado` | falta informação; traz a pergunta que resolveria |

O pareamento com o parecer é **unidirecional** (regra 3). Todo achado com
`Situação` `pergunta` tem de aparecer aqui como `indeterminado`. O contrário não
é exigido: uma linha `indeterminado` sem achado correspondente é legítima quando
falta informação que não merece bloco próprio no parecer — traga nela a pergunta
que a resolveria. O que nunca se admite é o mesmo item sair `indeterminado` aqui
e como violação no parecer.

```markdown
| Diretriz | Exigência | Status | Origem | Base | Próximo passo |
|---|---|---|---|---|---|
| `uso-clinico:D3` | registro do uso de IA no prontuário | `lacuna` | `observado` | `CFM-2454-2026:art4` | exigir campo próprio e versionamento do modelo |
```

Fecha com a contagem, **em tabela e neste formato exato** — é o que o
`validar_parecer.py` lê para conferir contra as linhas reais da tabela acima.
Lista com marcadores não é lida, e a conferência passa em silêncio:

```markdown
| Status | Contagem |
|---|---|
| `conforme-verificado` | 0 |
| `conforme-declarado` | 3 |
| `lacuna` | 0 |
| `nao-aplicavel` | 57 |
| `indeterminado` | 3 |
```

Abaixo da tabela, em prosa: quantos dos `lacuna` são bloqueantes e quantos de
risco. E a linha de validade:

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
10. Todo achado tem `Situação`, e nenhum com origem só `ausente` está como
    `confirmado`?
11. Onde gatilho e ficha divergiram na severidade, prevaleceu a do gatilho?
12. Todo gatilho que disparou veio de arquivo que a fase 2 carregou, e o parecer
    diz quais premissas a triagem afastou?
13. Dentro das seções 2 e 3, todo `###` é achado numerado `N.N` — e nada mais
    usa `###` no documento inteiro?
14. A contagem do checklist está em tabela, no formato da fase 5, e bate com as
    linhas reais?
15. **Conte, não estime.** Achados com `Situação` `pergunta`: N. Linhas
    `indeterminado` no checklist: M. Escreva os dois números. Se M < N, o
    pareamento da regra 3 está quebrado — corrija antes de entregar, não depois.
16. **Conte também o checklist.** Diretrizes dos arquivos que a fase 2 carregou:
    D. Linhas de dado no checklist: L. Se L > D, entrou linha de arquivo afastado
    — tire. Nenhuma linha de checklist vem de arquivo que a fase 2 não carregou.
17. Todo `Base.` foi copiado do gatilho ou da diretriz que disparou o achado, sem
    id acrescentado para reforçar o argumento?
