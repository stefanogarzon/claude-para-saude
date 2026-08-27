# Mudanças

Versões publicadas em `github.com/stefanogarzon/claude-para-saude`. O corpus tem
data de verificação própria, registrada em `corpus/VERSAO.md` no campo
`corpus_verificado_em` — ela não muda a cada versão do plugin, e é ela que conta
para decidir se a norma citada ainda vale.

## v0.1.24 — 2026-08-27

- A skill passa a ser encontrada por quem escreve em português natural. O disparo
  foi medido em 30 frases: **80% nas que devem disparar, 0% nas que não devem**.
  Antes de qualquer ajuste eram 35%.
- A `description` deixou de exigir que a pergunta mencione IA. "Meu consultório
  está adequado à LGPD e ao CFM?" tem saúde e norma, e não disparava.
- Pergunta de conformidade cujo domínio não está dito passa a entrar: a triagem
  confirma o escopo antes de julgar. Fica de fora o que se declara fora da saúde,
  a regulação estrangeira isolada e o registro na ANVISA.

## v0.1.19 — 2026-08-26

Correções no que o parecer **afirmava e não era verdade**. Todas saíam por
código, em todos os pareceres.

- O parecer atestava "os N restantes foram percorridos e não dispararam" contando
  sobre o catálogo inteiro, quando a triagem carrega só parte dele. Num caso que
  afastou seis dos sete arquivos, isso declarava 75 gatilhos percorridos. Agora o
  documento diz de quantas seções vieram os achados, e afirma explicitamente que
  não percorreu o catálogo inteiro.
- Dizia "premissas afastadas: desidentificação" e listava achados de
  desidentificação na mesma página.
- Achados de risco eram numerados `3.1`, `3.2` — e `## 3.` é a seção "Escalar".
  Pedir "veja o 3.5" mandava ao lugar errado. Agora é `B1`/`R1`.
- "Corpus verificado em fonte primária" saía sem ressalva, com 20 dos 215
  dispositivos em verificação parcial. O cabeçalho passa a trazer o split.
- O anexo normativo — até 60 KB de texto de lei, que se encaminha isolado ao
  jurídico — saía sem aviso nenhum. Agora traz o mesmo aviso do parecer e diz que
  são apenas os dispositivos citados, não o texto integral das normas.
- A data que decide a vigência da Res. 2.454 era comparada como string: `ontem`
  virava "em vigor" por acidente.

## v0.1.17 — 2026-08-26

- Corpus de 202 para **215 dispositivos**, e catálogo de 77 para **86 gatilhos**.
- Fichados os deveres que a vigência da Res. CFM 2.454/2026 tornou exigíveis e o
  corpus não cobria: art. 10 (direitos do paciente, incluindo segunda opinião),
  art. 20 (projetos-piloto), as oito medidas de governança do Anexo III — entre
  elas a atribuição de fiscalização ao Diretor Técnico e o acesso de órgãos de
  controle — e cinco definições do Anexo I.
- Nove gatilhos novos para alcançá-los. Ficha sem gatilho é norma que a skill não
  encontra.

## v0.1.15 — 2026-08-26

- **A Res. CFM 2.454/2026 entrou em vigor.** O parecer passa a avisar quando um
  achado decorre dela, e a nomear os que não têm base fora dela — até 25/08 eram
  advertência preventiva, hoje são exigência autônoma.
- Duas ferramentas abortavam fora do diretório do plugin, o que quebrava a fase
  de validação na máquina de quem instala.

## v0.1.14 — 2026-08-25

- O parecer virou **tabela**: o que o projeto faz, o risco, a legislação, a
  mitigação. Antes eram oito seções em prosa, e até 104 KB.
- O texto normativo deixou de passar pelo modelo — sai do corpus pelo
  identificador do dispositivo. Parafrasear norma tornou-se impossível.
- O anexo com o texto das leis virou arquivo próprio.
- Custo por avaliação caiu de US$ 3,82 para US$ 1,51 em média.

## Antes da v0.1.14

Versões de desenvolvimento, publicadas mas não anunciadas. O histórico está em
`git log`.
