# claude-para-saude

Plugin do Claude Code que avalia se um projeto de IA ou LLM com dado de saúde
está adequado às normas brasileiras. Escrito para **médico e responsável
técnico**, não para desenvolvedor: o parecer diz o que exigir da TI, o que
perguntar ao fornecedor e o que registrar.

> Orientação profissional, **não parecer jurídico**. Ver `LICENSE`.

## O que ele faz

Você descreve o projeto — em prosa, ou apontando um repositório, contrato ou
documentação — e a skill devolve dois arquivos:

- `parecer-conformidade.md`, com os achados separados por severidade e cada um
  rastreado ao dispositivo que o sustenta;
- `checklist-conformidade.md`, uma linha por diretriz aplicável.

Cada trecho de norma entre aspas sai da transcrição literal guardada no corpus,
com URL e data de verificação. A skill não escreve norma de memória.

## Instalação

```
/plugin marketplace add stefanogarzon/claude-para-saude
/plugin install claude-para-saude
```

Requer **Python 3 no PATH** — é o que faz o lookup dos dispositivos. Sem Python a
skill opera em modo degradado e todo dispositivo sai sem texto literal, o que
esvazia o principal: a citação verificável.

## Uso

```
/claude-para-saude:avaliar-conformidade
```

e descreva o projeto. A skill abre com uma **triagem** — tipo de dado, papel da
IA, contato com decisão clínica, modalidade, fornecedor — e **confirma com você
antes de julgar qualquer coisa**. Errar a triagem aplica o arcabouço errado ao
caso inteiro, por isso ela é um portão, não uma formalidade.

## O que esperar, em números

Modelo Opus, caso de porte médio (descrição em prosa de um fluxo em produção):

| | |
|---|---|
| tempo por avaliação | 6 a 13 minutos |
| custo em API | US$ 2,30 a 4,70 |

Não é uma resposta de trinta segundos. É a leitura de um corpus de 202
dispositivos contra o seu caso, com cada dispositivo citado carregado da fonte.

Casos menores saem mais baratos: um projeto sem dado de paciente fica em US$ 2,30
e 6 minutos, porque a triagem afasta a maior parte do catálogo.

## Cobertura, e os limites dela

Cobre **Brasil**: CFM (Res. 2.454/2026, CEM, Res. 1.821/2007 e 2.314/2022),
LGPD e resoluções da ANPD, Código Penal, Código Civil, CDC, Marco Civil e padrões
técnicos de segurança.

**Não cobre** — e a skill declara a lacuna em vez de opinar: FDA, HIPAA, EU AI
Act, MDR, regulação de dispositivo médico e ANVISA/SaMD.

## Data da norma

O corpus foi conferido em fonte primária numa data específica, registrada em
`corpus/VERSAO.md` no campo `corpus_verificado_em` e reproduzida no cabeçalho de
todo parecer. **Não confunda com `construido:`**, que é a data em que o pacote foi
montado e nada diz sobre a idade da norma.

Confira a data antes de decidir. A ficha de provedores de LLM envelhece mais
depressa que o resto — política de retenção e de treino muda sem aviso.

## Como ler o parecer

Três coisas mudam o peso de um achado, e vale entender antes de ler:

- **Severidade** é o peso da norma — `bloqueante`, `risco`, `boa-prática` — e é
  copiada do corpus, nunca atribuída pela skill.
- **Origem** é de onde veio a evidência: `observado` (a skill leu no material),
  `declarado` (alguém afirmou) ou `ausente` (não há informação). **Conformidade
  declarada não é conformidade**: se você só descreveu o projeto, o teto de todo
  item é `conforme-declarado`.
- **Situação** diz se é constatação (`confirmado`) ou pergunta (`pergunta`). Um
  achado `bloqueante` com situação `pergunta` **não** afirma que você está em
  desconformidade — diz que a resposta errada o poria lá.
