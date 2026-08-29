# Mudanças

Versões publicadas em `github.com/stefanogarzon/claude-para-saude`. O corpus tem
data de verificação própria, registrada em `corpus/VERSAO.md` no campo
`corpus_verificado_em` — ela não muda a cada versão do plugin, e é ela que conta
para decidir se a norma citada ainda vale.

## v0.1.31 — 2026-08-29

O parecer encolheu de 11% a 26%, e de 15% a 17% por achado nos três casos com
mais de vinte. Cada linha da tabela passa a ser uma cadeia fechada: o que o
projeto faz, o dispositivo que isso contraria, o que o dispositivo exige, e o que
fazer a respeito.

- **A lista "O que checar, por achado" saiu.** Eram até 31 marcadores ao fim da
  seção, repetindo os identificadores da tabela para o leitor cruzar os dois.
  Ocupavam 11% dos bytes do documento. A pergunta de checagem passou para a
  linha do achado a que pertence.
- **A ementa da norma sai uma vez por documento**, na primeira linha que cita o
  dispositivo. O art. 87 do Código de Ética Médica saía por extenso em cinco
  linhas do mesmo parecer. O nome da norma sai uma vez por célula:
  `Res. CFM 1.821/2007, arts. 3º e 4º`.
- **Em 26 dos 86 gatilhos, a checagem e a mitigação diziam a mesma coisa** em
  vozes diferentes. "Quais campos a tarefa exige" e "enviar só os campos que a
  tarefa exige" ocupavam duas orações para uma informação. Onde a sobreposição
  passa de 60%, sai só a mitigação.
- **Tetos de tamanho nos campos de prosa**, conferidos pelo validador: veredito
  40 palavras, ação de hoje 30, histórico 30, cada encaminhamento 25. Ponto e
  vírgula e travessão são recusados nesses campos. O veredito de um caso saiu com
  86 palavras numa oração só.
- **Títulos descritivos**: `Objeto avaliado`, `Achados e ações`, `Ações do
  próprio serviço`, `Exigências ao fornecedor`, `Instrumentos contratuais`,
  `Encaminhamentos`, `Cobertura do catálogo`, `Método`.
- A regra de vocabulário passou a valer nos campos livres da triagem. O parecer
  reprovava por `endpoint` no campo de fornecedor, e nada dizia ao modelo que
  aquele campo sai no corpo do documento.

As v0.1.29 e v0.1.30 são etapas desta mudança.

## v0.1.28 — 2026-08-28

O parecer passa a responder a pergunta que o leitor fez. Na v0.1.24, quem
perguntasse "gravo a consulta e mando pro ChatGPT na minha conta pessoal, isso é
permitido?" recebia 29 achados de peso igual, e nenhuma frase dizendo se pode ou
não. A palavra "Vedada" saía no anexo, na linha 21, numa célula de quadro
comparativo de fornecedores.

- **A resposta abre o documento**: veredito, o que fazer hoje, e o que fazer com
  o que já rodou — este último quando o material declara uso com paciente real.
  Os metadados de método desceram para o pé do parecer; ocupavam as quatro
  primeiras linhas.
- **Os achados agrupam por quem executa**, em quatro blocos: o que você resolve
  sozinho, o que exigir do fornecedor, o que precisa de contrato ou de advogado,
  e o que um serviço desse porte não resolve. Antes conviviam na mesma coluna
  "desligar o treino na configuração", de dois minutos, e "estender a
  certificação do prontuário ao componente", que depende do fornecedor.
- **A coluna da base legal diz do que trata o artigo.** `CEM:art87` passou a sair
  como "Código de Ética Médica, art. 87 — prontuário legível, autoria e guarda".
  Onde a ementa da ficha traz sigla não expandida, a base sai com norma e artigo
  apenas.
- **Jargão fora do texto.** O catálogo de 86 gatilhos ganhou uma coluna `Efeito`,
  com 27 traduções para os que saíam em dialeto de código; nove mitigações e três
  perguntas de checagem foram reescritas. Um critério de validação novo reprova o
  parecer que traga qualquer termo de uma lista de 34 entradas. Rodado contra o
  parecer da versão anterior, o critério pega 11.

A causa da regressão fica registrada. A v0.1.14 removeu os campos de ação junto
com a mudança para tabela, e os quatro critérios de aprovação continuaram verdes,
porque nenhum deles olhava para o leitor.

As v0.1.25 e v0.1.26 são etapas desta mudança e do backup do repositório
editorial, publicadas sem anúncio.

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
