---
tema: escolha e contratação de fornecedor de IA para uso com dado de paciente
aplica-se-a: médico que contrata, responsável técnico, desenvolvedor que escolhe a integração
fichas: [01, 04, 05, 06, 07, 12]
verificado: 2026-08-11
---

# Escolha de fornecedor e região de processamento

Como escolher, qualificar e contratar um fornecedor de IA que vai tratar dado de paciente, e como fixar a região de processamento. As diretrizes valem por critério. Nome de produto e política de fornecedor mudam; o critério permanece.

> Parte destas diretrizes decorre da Res. CFM 2.454/2026, **em vigor desde 26/08/2026**. Elas são exigência corrente. Cada diretriz traz a resolução no campo `Base`, ao lado das demais normas que a sustentam.

## D1 — Trate envio a fornecedor fora do Brasil como transferência internacional

Todo envio de dado de paciente a fornecedor cujo processamento ocorre fora do Brasil é transferência internacional. Disponibilizar acesso já basta: credencial de leitura, bucket, índice vetorial, backup replicado ou suporte remoto em região externa entram na definição, mesmo sem cópia de arquivo. A lei brasileira se aplica qualquer que seja a sede do fornecedor ou o local do armazenamento.

**Base.** ANPD-19-2024:art3.III · ANPD-19-2024:art7 · ANPD-19-2024:art4

**Verificar.**
- existe inventário de fornecedores com a região de processamento de cada fluxo
- backups, índices vetoriais e logs estão mapeados junto com o endpoint principal

## D2 — Exija hipótese legal e mecanismo de transferência antes do primeiro envio

Os dois requisitos são cumulativos. Para dado de saúde, a hipótese legal vem do rol do art. 11 da LGPD. O mecanismo de transferência vem do art. 33. Faltando qualquer um dos dois, o fluxo não é liberado.

**Base.** ANPD-19-2024:art9 · LGPD:art33 · LGPD:art11 · LGPD:art11.II.f

**Verificar.**
- a hipótese do art. 11 está nomeada por escrito, por fluxo
- o mecanismo do art. 33 está identificado e o instrumento está assinado
- a data de assinatura é anterior ao primeiro envio de dado real

**Escalar se.** O único mecanismo disponível for o consentimento específico do art. 33, VIII. Escalar também quando a hipótese for a tutela da saúde e o destinatário for fornecedor de tecnologia que não é profissional nem serviço de saúde (`custodia:D11`).

## D3 — Envie o mínimo necessário

A minimização é exigível na própria transferência. O payload leva os campos pertinentes à tarefa, não o registro inteiro. Histórico de conversa acumulado a cada requisição amplia a transferência sem finalidade.

**Base.** ANPD-19-2024:art9 · CFM-2454-2026:art6

**Verificar.**
- há filtro de campos antes da chamada externa
- o tamanho do payload corresponde à tarefa declarada
- existe etapa de desidentificação antes da chamada

## D4 — Prefira destino com decisão de adequação

Em 11/08/2026 existe uma decisão de adequação da ANPD: União Europeia e Espaço Econômico Europeu. Não há decisão de adequação para os Estados Unidos. Com processamento na UE ou no EEE, o mecanismo do art. 33, I fica disponível. Para qualquer outro destino, o caminho de uso corrente é a cláusula-padrão contratual do Anexo II da Res. 19/2024.

**Base.** ANPD-32-2026:art1 · LGPD:art33 · ANPD-19-2024:art9

**Verificar.**
- a região contratada está na UE, no EEE ou no Brasil, ou existe instrumento com as cláusulas-padrão
- a lista de decisões de adequação foi consultada na data da decisão de arquitetura
- a hipótese do art. 11 permanece documentada, mesmo com destino adequado

**Escalar se.** O fornecedor não oferecer residência de dados na UE, no EEE ou no Brasil e o fluxo for assistencial.

## D5 — Não declare adequação por conta própria

A avaliação do nível de proteção de país de destino é competência da ANPD. Decisão de adequação emitida por autoridade estrangeira não aproveita ao exportador brasileiro.

**Base.** LGPD:art34 · ANPD-32-2026:art1

**Verificar.**
- nenhum documento interno afirma adequação de país sem decisão da ANPD
- nenhuma decisão de arquitetura invoca acordo entre outras jurisdições como mecanismo

## D6 — Fixe a região de processamento por configuração explícita

O parâmetro de região é declarado na chamada e na infraestrutura, com valor fixo. Valor padrão do fornecedor, ausência de parâmetro e roteamento automático entre regiões descaracterizam o controle.

**Base.** ANPD-32-2026:art1 · ANPD-19-2024:art3.III · LGPD:art36

**Verificar.**
- a região aparece explícita no código, na variável de ambiente e no console do fornecedor
- buckets, filas, índices e backups do fluxo estão na mesma região
- mudança de região gera registro datado e, quando altera a garantia apresentada na transferência, comunicação à ANPD

**Escalar se.** O produto rotear entre regiões sem possibilidade de fixação.

## D7 — O contrato de tratamento de dados do fornecedor não substitui as cláusulas-padrão brasileiras

O contrato de tratamento de dados do fornecedor (DPA) cumpre outra função. A validade do mecanismo de cláusulas-padrão depende da adoção integral e sem alteração do texto do Anexo II, em instrumento firmado entre exportador e importador. Texto adaptado, resumido, traduzido ou parcial invalida o mecanismo. O prazo de incorporação esgotou-se em 23/08/2025: contrato anterior e nunca aditado está em descumprimento.

**Base.** ANPD-19-2024:art16 · ANPD-19-2024:art2 · LGPD:art35

**Verificar.**
- o anexo contratual reproduz o texto do Anexo II sem edição
- o instrumento está assinado pelas duas partes, com data
- contratos anteriores a 23/08/2025 têm aditivo

**Escalar se.** O fornecedor recusar firmar o Anexo II integral ou propuser redação própria.

## D8 — Defina o papel do importador no contrato e mantenha coerência com os termos do produto

O Anexo II exige marcar o papel do importador como controlador ou operador. A marcação precisa corresponder ao que os termos do produto autorizam. Marcar o fornecedor como operador e conviver com termos que reservam uso do conteúdo para finalidade própria do fornecedor é contradição documental.

**Base.** ANPD-19-2024:anexoII

**Verificar.**
- o quadro do importador está preenchido
- os termos do produto em vigor foram lidos contra a marcação escolhida
- a cadeia de subprocessadores está descrita no contrato

## D9 — Escreva as medidas de segurança dentro do instrumento

Transferência com dado sensível exige salvaguardas adicionais descritas na seção própria do Anexo II. Criptografia, controle de acesso e segregação precisam estar escritos no contrato, além de implementados. As garantias do mecanismo são avaliadas pelas medidas técnicas efetivas do operador.

**Base.** ANPD-19-2024:anexoII · LGPD:art35 · CFM-2454-2026:art17

**Verificar.**
- a seção de medidas de segurança está preenchida e menciona dado sensível
- as medidas descritas correspondem à arquitetura em produção
- existe data de avaliação das medidas, com referência técnica declarada

## D10 — Vede conta pessoal, gratuita ou de consumidor com dado de paciente

Conta pessoal, plano gratuito e plano de consumidor não oferecem os padrões mínimos de segurança exigidos para dado sensível. Pagar por plano pessoal não contrata DPA, nem retenção diferenciada, nem cobertura contratual.

**Base.** CFM-2454-2026:art6 · PROV:comparativo · LGPD:art46

**Verificar.**
- nenhuma chave de tier gratuito aparece em código que processa dado de paciente
- as contas em uso pertencem à organização, com administração e trilha de acesso
- ambientes de teste e homologação não recebem dado real de paciente

## D11 — Exija configuração padrão que não use os dados para treinamento

A configuração de fábrica precisa garantir o nível mais alto de privacidade, sem exigir ação do usuário. Produto cujo padrão usa os inputs para treinamento é desconforme, ainda que exista opção de desligar. Em telemedicina, treinamento, avaliação de qualidade e melhoria de serviço do fornecedor ficam fora da finalidade primária do dado.

**Base.** CFM-2454-2026:anexoI.XV-XVI · CFM-2454-2026:art6 · CFM-2314-2022:art3§7 · PROV:comparativo

**Verificar.**
- a política vigente do produto declara não usar dado comercial para treino por padrão, com data de consulta registrada
- mecanismos de avaliação e de feedback do usuário estão desligados na interface clínica
- o estado da configuração foi capturado em evidência documental, com data

## D12 — Pergunte, verifique e delimite a retenção

A pergunta ao fornecedor é por recurso, não por empresa: prazo de retenção de cada endpoint e de cada funcionalidade, local de armazenamento, quem acessa e em que hipótese. A verificação é feita antes do primeiro envio e repetida a cada mudança de arquitetura. O arranjo de retenção zero (ZDR) costuma ser concedido por organização, por endpoint ou por recurso, e não cobre tudo. Costumam ficar de fora: classificadores de segurança, conteúdo sinalizado, retenção sob ordem judicial, consoles e ferramentas de teste, recursos com estado (arquivos, lote, execução de código, agentes persistentes), logs de métricas e de conformidade, integrações de terceiros e busca ou ancoragem externa.

**Base.** PROV:comparativo · PROV:erros-comuns · PROV:anthropic · PROV:openai · PROV:google

**Verificar.**
- existe evidência datada do arranjo no artefato que o fornecedor oferece: estado no console, aprovação contratual registrada ou parâmetro explícito declarado na chamada
- o arranjo depende de aprovação prévia do fornecedor, e essa aprovação está documentada
- o modelo escolhido não está em regime que torne a retenção zero inalcançável
- cada endpoint e cada recurso usados no fluxo constam da lista de elegíveis do arranjo
- recursos não elegíveis estão bloqueados no código, e não apenas desaconselhados

**Escalar se.** Um recurso necessário ao produto ficar fora do arranjo de retenção zero e não houver alternativa.

## D13 — Trate política de retenção como compromisso contratual, não como controle técnico

Prazo declarado de deleção é promessa revogável. Entre abril e setembro de 2025, ordem judicial em jurisdição estrangeira suspendeu a deleção de conteúdo de um fornecedor de grande porte, e as únicas configurações imunes foram a de retenção zero e os planos Enterprise e Edu. O plano de equipe corporativo foi alcançado. Ser plano pago de empresa não é o critério; o critério é a configuração de retenção contratada. Verificado em 11/08/2026; reverificar antes de citar. A mitigação estrutural é não deixar o dado retido: retenção zero contratada, desidentificação antes da chamada e bloqueio de recursos que persistem.

**Base.** PROV:openai · PROV:erros-comuns · LGPD:art46

**Verificar.**
- o desenho do fluxo suporta a hipótese de o dado permanecer armazenado no fornecedor
- o dossiê registra a configuração de retenção contratada, e não apenas o nome do plano
- existe desidentificação antes da chamada externa
- nenhum documento interno apresenta o prazo de deleção como controle técnico

## D14 — Em telemedicina, exija sede no Brasil, inscrição no CRM e responsável técnico

Pessoa jurídica que presta serviço de telemedicina, plataforma de comunicação e arquivamento de dados precisa de sede em território brasileiro, inscrição no CRM do Estado da sede e responsável técnico médico inscrito no mesmo Conselho. Os três requisitos são cumulativos.

**Base.** CFM-2314-2022:art17

**Verificar.**
- a plataforma contratada apresenta CNPJ com sede no Brasil e número de inscrição no CRM
- existe médico nomeado como responsável técnico, com inscrição no CRM daquele Estado
- serviços com pacientes em vários estados têm o mapeamento de jurisdição de CRM

**Escalar se.** O enquadramento do fornecedor estrangeiro contratado por trás da plataforma inscrita estiver em disputa.

## D15 — Em telemedicina, reparta a guarda no contrato e garanta acesso do médico

Em telemedicina, a terceirização de arquivamento exige repartição contratual expressa da guarda dos dados do paciente e do atendimento. Termos de serviço aceitos por clique não configuram guarda compartilhada. O contrato assegura ao médico assistente acesso aos dados durante todo o prazo legal de preservação, inclusive depois do encerramento da relação com a plataforma. Fora da telemedicina, a repartição da guarda segue `custodia:D3`.

**Base.** CFM-2314-2022:art3

**Verificar.**
- o contrato tem cláusula de guarda com repartição de responsabilidade
- há previsão de exportação dos dados em formato utilizável no encerramento
- o SRES atende integralmente ao NGS2, requisito incondicionado
- o padrão de assinatura invocado é ICP-Brasil ou outro padrão com base legal de aceitação identificada
- a certificação invocada pelo fornecedor nomeia o escopo certificado, e o componente de IA está dentro dele
- existe rotina de entrega de cópia do registro ao paciente

**Escalar se.** O enquadramento do fornecedor que retém prompt e saída como serviço terceirizado de arquivamento estiver em disputa.

## D16 — Acordo de conformidade com lei estrangeira de saúde não é conformidade brasileira

Um acordo desse tipo (BAA) significa que o fornecedor aceita cobrir contratualmente uma lista fechada de serviços, em configurações determinadas, sob regime jurídico de outro país. Não significa base legal do art. 11 da LGPD, nem mecanismo de transferência do art. 33, nem contrato de operador, nem dispensa do registro no prontuário. Entra na qualificação como indicador do que o fornecedor aceita assumir.

**Base.** PROV:comparativo · LGPD:art33 · CFM-2454-2026:art6 · CFM-2454-2026:art4

**Verificar.**
- o produto, o plano e o endpoint em uso constam da lista de serviços cobertos
- a lista de serviços cobertos tem data de leitura
- os documentos de conformidade brasileira existem de forma independente do acordo estrangeiro

## D17 — Aplique uma lista fixa de perguntas de qualificação e trate resposta ausente como reprovação

As perguntas são feitas por escrito, antes da contratação, e as respostas ficam anexadas ao dossiê do fornecedor. Resposta verbal, apresentação comercial e página de marketing não contam. Resposta ausente, evasiva ou sem data reprova o fornecedor para o fluxo com dado de paciente. A última pergunta apura preferência, não requisito: sozinha, não reprova.

**Base.** ANPD-19-2024:art4 · ANPD-19-2024:art16 · ANPD-19-2024:anexoII · CFM-2454-2026:art3 · CFM-2454-2026:anexoIII.V

**Verificar.** Perguntas obrigatórias, com resposta escrita e datada:
- em que regiões o dado é processado, armazenado e replicado, e como a região é fixada
- quais são os prazos de retenção por endpoint e por recurso, e o que não é alcançado por arranjo de retenção zero
- os inputs são usados para treinamento, avaliação ou melhoria do serviço em alguma configuração
- a empresa firma as cláusulas-padrão contratuais brasileiras, integrais e sem alteração
- qual é a lista de subprocessadores e como são comunicadas as mudanças
- quais medidas de segurança se aplicam a dado sensível, em trânsito e em repouso
- qual o procedimento e o prazo de comunicação de incidente
- como o cliente obtém exportação e eliminação dos dados no encerramento
- qual é o processo em caso de ordem de acesso por autoridade estrangeira
- quais limitações, riscos conhecidos e evidência de desempenho o fornecedor documenta
- o produto oferece acesso a parametrizações e interfaces auditáveis, ou é sistema fechado

**Escalar se.** O fornecedor recusar responder por escrito a qualquer item da lista.

## D18 — Registre a decisão por fluxo, com data

O controlador é o médico ou a clínica que contrata. A verificação da transferência é dever dele, com registro. O dossiê traz, por fluxo: produto, plano, endpoint, região, prazo de retenção, hipótese legal, mecanismo de transferência, versão dos termos aceitos e data de cada verificação.

**Base.** ANPD-19-2024:art4 · ANPD-19-2024:art17

**Verificar.**
- existe inventário de destinos externos de dados clínicos
- o contrato e o anexo de cláusulas estão acessíveis ao encarregado
- existe fluxo de atendimento a pedido do titular pelo texto das cláusulas

## D19 — Reverifique em prazo fixo e a cada mudança

Defina prazo de reverificação, com responsável nomeado, e reabra as páginas oficiais de retenção, treinamento, regiões e serviços cobertos. Mudança de fornecedor, de região ou dos termos altera a garantia apresentada e exige registro, reavaliação e comunicação à ANPD. Arquitetura apoiada em decisão de adequação depende de reverificação: a decisão vigente será reavaliada em quatro anos contados de 27/01/2026.

**Base.** LGPD:art36 · ANPD-32-2026:art2-art6 · PROV:erros-comuns

**Verificar.**
- existe rotina de reverificação com periodicidade definida e responsável
- alteração da garantia apresentada — mecanismo, instrumento de cláusulas, região de processamento — foi comunicada à ANPD, com data e protocolo
- cada afirmação sobre política de fornecedor no dossiê tem URL e data
- alterações unilaterais dos termos geram nova avaliação registrada
- a data da última reverificação é posterior à última mudança conhecida do produto

**Escalar se.** O fornecedor alterar de forma unilateral os termos, a região ou a lista de serviços cobertos.
