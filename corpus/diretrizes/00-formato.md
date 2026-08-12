---
tipo: formato
versao: 1
atualizado: 2026-08-11
---

# Formato das diretrizes

As fichas do corpus servem para **citar**. As diretrizes servem para **decidir**. Uma skill carrega a diretriz primeiro; só busca a ficha quando precisa do texto literal da norma.

## Princípios

1. **Só entendimento consolidado.** O que está pacificado vira diretriz. O que é controverso vira uma linha em "Quando escalar", sem desenvolver as leituras concorrentes.
2. **Enunciado imperativo.** A diretriz diz o que fazer, não descreve a norma.
3. **Sem transcrição.** Nenhum bloco de citação. A base normativa entra como identificador de ficha, para a skill buscar se precisar citar.
4. **Verificação observável.** Cada diretriz traz como conferir se está sendo cumprida.
5. **Curto.** Um arquivo cabe no contexto de uma skill sem consumir o orçamento inteiro. Teto: 3.000 palavras, cerca de quatro mil tokens. Não há piso: arquivo focado pode ser curto.

## Estrutura do arquivo

```
---
tema: uso clínico de LLM
aplica-se-a: médico assistente, clínica, desenvolvedor
fichas: [01, 02, 05]
verificado: 2026-08-11
---

# Título

Uma frase dizendo do que trata e para quem.

## D1 — Enunciado curto e imperativo

O que fazer, em duas ou três frases.

**Base.** CFM-2454-2026:art4 · CEM:art87

**Verificar.** Como se confere na prática. Bullets curtos.

**Escalar se.** (opcional, uma linha) O caso em que a diretriz não resolve e a decisão sobe para o responsável técnico ou para o jurídico.
```

## Numeração

`D1`, `D2`, ... dentro de cada arquivo. O identificador completo é `arquivo:D3`, por exemplo `uso-clinico:D3`.

## O que não entra

- Transcrição de norma.
- Discussão de leituras concorrentes.
- Precedente judicial isolado.
- Recomendação sem base no corpus.
- Qualquer item apoiado apenas em entrada de confiança `secundária` ou `não-verificado`.

## Exemplo de diretriz bem escrita

> ## D4 — Registre o uso de IA no prontuário
>
> Todo uso de IA como apoio à decisão médica é registrado no prontuário do paciente. O registro traz ferramenta, versão, finalidade e confirmação de que houve revisão médica. Não depende de a IA ter sido determinante.
>
> **Base.** CFM-2454-2026:art4 · CEM:art87
>
> **Verificar.**
> - o sistema tem campo próprio para esse registro
> - a versão do modelo é persistida junto com a saída
> - existe etapa de revisão antes de o texto virar registro clínico
>
> **Escalar se.** O sistema não permite gravar a versão do modelo usada.

## Exemplo de diretriz mal escrita

> ## D4 — Sobre o art. 4º, V
>
> O art. 4º, V, da Res. CFM 2.454/2026 dispõe que é dever do médico "registrar no prontuário do paciente o uso de sistemas de IA como apoio à decisão médica". Há discussão sobre se isso alcança uso não relevante, dado que o art. 5º, §1º fala em "apoio relevante"...

Descreve a norma em vez de dizer o que fazer, transcreve, e desenvolve a controvérsia.
