---
tema: custódia, guarda e compartilhamento de dado de paciente
aplica-se-a: médico assistente, responsável técnico, desenvolvedor que projeta persistência
fichas: [02, 03, 04, 05, 07, 11]
verificado: 2026-08-11
---

# Custódia de dados de saúde

Regras de decisão sobre quem guarda o dado do paciente, por quanto tempo, em que sistema, e em que condições ele pode sair dali. Serve ao médico assistente, ao responsável técnico do serviço e a quem projeta o armazenamento. As três classes de retenção usadas pelo conjunto estão definidas em D13.

## D1 — Classifique como dado sensível todo dado de saúde vinculável a uma pessoa

Prontuário, evolução, anamnese, laudo, imagem, exame, prescrição, resultado genético e biometria são dado pessoal sensível. O regime não depende da presença do nome: basta que o titular seja identificável, direta ou indiretamente. Agendamento com especialidade, código de procedimento e nome de medicamento revelam condição de saúde e entram no mesmo regime.

**Base.** LGPD:art5.II · LGPD:art5.I · LGPD:art11§1-§3

**Verificar.**
- o inventário de dados marca como sensível a tabela de agendamento e a de faturamento
- campo de texto livre é tratado como sensível por padrão, sem depender de varredura
- metadado DICOM entra na classificação junto com o pixel

## D2 — Nomeie o responsável pela guarda de cada acervo

A guarda do prontuário é do médico ou da instituição que assiste o paciente. Em telemedicina, responde o médico do atendimento em consultório próprio, e o diretor ou responsável técnico havendo interveniência de empresa ou instituição. Fora da telemedicina, essa mesma repartição é boa prática, e não texto de norma. Cada base que contenha registro clínico tem um nome de pessoa associado, não apenas um time.

**Base.** CEM:art87 · CFM-2314-2022:art3

**Verificar.**
- existe documento que nomeia o responsável por cada base com dado clínico
- o responsável técnico do serviço consegue listar os sistemas onde há registro clínico
- bases criadas por integração ou por exportação também têm responsável nomeado

## D3 — Terceirize a execução da guarda por contrato, nunca a responsabilidade

Arquivamento e hospedagem podem ser contratados. A responsabilidade pela guarda continua com o médico ou com a instituição. O contrato vincula o operador às instruções do controlador e delimita finalidade, retenção e subprocessadores. Em telemedicina, a guarda é compartilhada com a contratada por cláusula expressa, e o contrato garante ao médico assistente acesso aos dados por todo o prazo de preservação, inclusive em plataforma institucional. Termos de serviço aceitos por clique não configuram repartição contratual de guarda.

**Base.** LGPD:art39 · CFM-2314-2022:art3 · CEM:art87

**Verificar.**
- há contrato assinado com cláusula de guarda de dados de paciente
- a cadeia de subprocessadores está listada no contrato
- o contrato prevê devolução integral do acervo no encerramento
- existe rotina de exportação do acervo que funciona sem depender do fornecedor

**Escalar se.** O fornecedor apenas processa e retém conteúdo, e discute-se se ele é serviço terceirizado de arquivamento.

## D4 — Exija NGS2 vigente do sistema que guarda ou transmite dado identificado

O uso de sistema informatizado para guardar prontuário, manuseá-lo e trocar informação identificada em saúde depende de atendimento integral ao NGS2. A assinatura digital é em ICP-Brasil, até a implantação do CRM Digital. Em telemedicina, a resolução própria admite também outro padrão legalmente aceito, e nesse caso o padrão invocado é identificado com sua base legal. Certificação em NGS1 não autoriza eliminar o papel. Peça o certificado com número, nível, versão da lista de requisitos e validade.

**Base.** CFM-1821-2007:art3 · CFM-1821-2007:art4 · CFM-1821-2007:art5 · CFM-2314-2022:art3

**Verificar.**
- o certificado apresentado indica o nível, e o nível é NGS2
- a versão da lista de requisitos está vigente
- fora da telemedicina, a assinatura usada é ICP-Brasil
- o escopo do certificado cobre o componente que processa o dado, e não só o sistema hospedeiro

**Escalar se.** O fornecedor invoca a certificação do sistema hospedeiro para cobrir um componente de IA fora do escopo certificado.

## D5 — Aplique guarda permanente ao prontuário arquivado eletronicamente

Prontuário arquivado em meio óptico, microfilmado ou digitalizado tem guarda permanente, sob controle do médico ou da instituição. A regra é da classe A. Política de ciclo de vida que apaga registro clínico por idade é incompatível com esse regime. Prazo de expiração definido por provedor externo não é política de retenção do serviço.

**Base.** CFM-1821-2007:art7 · CEM:art87

**Verificar.**
- não há regra de expiração automática sobre bucket, tabela ou índice com registro clínico
- o backup do registro clínico cobre o mesmo horizonte da guarda, com restauração testada
- migração de fornecedor preserva o acervo íntegro, com evidência de conferência

**Escalar se.** O serviço pretende eliminar prontuário digitalizado após vinte anos do último registro, com apoio em lei federal posterior à resolução.

## D6 — Preserve por vinte anos o papel que não foi arquivado eletronicamente

O prazo mínimo é de vinte anos contados do último registro, e não da abertura do prontuário. Ele vale para o suporte em papel da classe A que não foi arquivado em meio óptico, microfilmado ou digitalizado. Eliminação de acervo depende de parecer da comissão interna competente, e não de decisão operacional isolada.

**Base.** CFM-1821-2007:art8 · CFM-1821-2007:art6 · CFM-1821-2007:art9

**Verificar.**
- o cálculo de expiração parte da data do último registro
- a política de retenção distingue papel de eletrônico
- há registro do parecer da comissão antes de cada eliminação
- rotina automatizada de expurgo não executa sem aprovação registrada

## D7 — Libere cópia do prontuário apenas nas hipóteses fechadas

A liberação de cópia do prontuário sob guarda do médico é admitida em três hipóteses: ordem judicial, defesa própria do médico e autorização escrita do paciente. Some-se o dever de entregar cópia ao próprio paciente ou a seu representante legal quando solicitada, salvo quando a entrega puder gerar risco ao próprio paciente ou a terceiro, hipótese em que a recusa é fundamentada e registrada. Ao Conselho Regional de Medicina, entregue quando requisitada. Na defesa própria, peça a observância do sigilo.

**Base.** CEM:art89 · CEM:art88 · CEM:art90 · CFM-2314-2022:art3

**Verificar.**
- o sistema exporta o prontuário integral, em mídia digital ou impressa
- cada liberação registra a hipótese invocada, a data e o destinatário
- a autorização escrita do paciente é armazenada junto ao registro
- a exportação inclui o conteúdo de apoio à decisão que ficou em outro sistema

**Escalar se.** A aferição do risco ao paciente ou a terceiro, no caso concreto, não é evidente.

## D8 — Trate envio a terceiro como liberação de cópia

Enviar conteúdo de prontuário a serviço externo é liberação de cópia e, na leitura deste corpus, também revelação de fato conhecido em razão da profissão. Os dois regimes são cumulativos e as listas de exceção são distintas. Para a liberação de cópia, as hipóteses são fechadas: ordem judicial, defesa própria do médico e autorização escrita do paciente. Motivo justo e dever legal não bastam. Na prática, a única via disponível para uma integração de rotina é a autorização escrita e específica do paciente. Ganho de produtividade e melhoria do cuidado não são motivo justo nem para o sigilo. Antes de qualquer integração que faça o dado sair do domínio de guarda, registre por escrito a hipótese que a ampara.

**Leitura adotada.** Leitura nossa, conservadora: enviar a sistema de terceiro é revelação. O ponto não está pacificado. Para liberação de cópia de prontuário, o art. 89 sustenta a regra sem depender desta leitura.

**Base.** CEM:art89 · CEM:art73 · CFM-1821-2007:art3 · LGPD:art5.X

**Verificar.**
- existe inventário dos destinos externos de dado clínico
- cada destino tem hipótese declarada e documento que a sustenta
- há registro de consentimento escrito específico quando essa for a hipótese
- não há envio de dado de paciente a conta de consumidor ou a plano gratuito

**Escalar se.** O destino é provedor sem sede no Brasil em fluxo de telemedicina, ou subprocessador estrangeiro por trás de plataforma inscrita no CRM.

## D9 — Contrate o fornecedor de tecnologia antes de enviar o primeiro dado

O contrato com o fornecedor limita o tratamento às instruções do controlador, veda uso do conteúdo para finalidade própria e desliga treinamento e melhoria de produto. A configuração da conta precisa refletir o contrato, com evidência documentada. Compartilhamento de dado de saúde entre controladores com objetivo de vantagem econômica tem vedação legal, com exceções estreitas.

**Base.** LGPD:art39 · LGPD:art11§4 · LGPD:art48 · CFM-2314-2022:art3§7 · CFM-2314-2022:art3

**Verificar.**
- o contrato tem cláusula de finalidade restrita às instruções do controlador
- há captura de tela ou documento do fornecedor comprovando o opt-out de treinamento
- a política de retenção do fornecedor está declarada, e a compatibilidade com o prazo de guarda é exigida da cópia sob controle da instituição, não da retenção no fornecedor
- existe cláusula de notificação de incidente ao controlador, com prazo

## D10 — Declare a base legal por finalidade, antes do tratamento

Cada finalidade de tratamento de dado de saúde tem uma hipótese declarada do rol de dado sensível, que é fechado. Legítimo interesse não ampara dado sensível. Consentimento, quando for a hipótese, é específico, destacado por finalidade e revogável. Uma finalidade nova exige nova análise, e não herda a base da anterior. Consentimento do CFM e base legal da LGPD são exigências distintas e cumulativas: a recusa do uso de IA pelo paciente, exigível a partir de 26/08/2026, desliga a ferramenta e não revoga a base legal do atendimento. A revogação do consentimento alcança apenas as finalidades que dependiam dele, e o pedido de eliminação pelo titular encontra o limite da guarda obrigatória do prontuário, com negativa fundamentada e registrada.

**Base.** LGPD:art11 · LGPD:art7 · LGPD:art11.II.f · LGPD:art8§5 · LGPD:art18 · CFM-2454-2026:art5 · CFM-1821-2007:art7

**Verificar.**
- existe registro que associa cada finalidade a uma hipótese
- o consentimento é coletado por finalidade, e não em bloco único
- a revogação do consentimento está implementada, produz efeito nos sistemas e não dispara exclusão em cascata sobre registro clínico
- pedido de eliminação do titular passa pela verificação da guarda obrigatória, com resposta registrada
- fluxo administrativo, comercial e de marketing tem base própria

## D11 — Restrinja a base de tutela da saúde ao ato assistencial

A tutela da saúde ampara o tratamento dentro do procedimento realizado por profissional de saúde, serviço de saúde ou autoridade sanitária. É defensável que ela cubra o uso da ferramenta pelo próprio médico assistente para conduzir o caso. Não cobre uso administrativo, comercial, de marketing nem de desenvolvimento de produto.

**Base.** LGPD:art11.II.f · LGPD:art7

**Verificar.**
- a finalidade declarada descreve um ato assistencial concreto
- o usuário do fluxo é profissional ou serviço de saúde
- não há invocação dessa base para faturamento, prospecção ou avaliação de produto

**Escalar se.** A base é invocada para amparar a remessa do dado a um fornecedor de tecnologia que não é profissional nem serviço de saúde.

## D12 — Desidentifique contra quase-identificadores e documente o teste

Remover nome e documento não produz dado anonimizado. O teste é a possibilidade de reassociação com esforços razoáveis, medida por custo, tempo e tecnologia disponível. A lista de quase-identificadores a varrer é a de `SEC:anonimizacao.quase-identificadores`, e este arquivo não mantém lista própria. Essa lista reproduz o Safe Harbor, que é regime dos Estados Unidos: use-a como piso operacional de varredura, não como salvo-conduto jurídico, porque cumpri-la não caracteriza anonimização no Brasil. Quem anonimiza carrega o ônus de demonstrar a irreversibilidade, com data e técnica registradas. Pseudonimização continua sob a lei.

**Base.** LGPD:art12 · LGPD:art5.XI · LGPD:art5.III · CEM:art75 · SEC:anonimizacao.quase-identificadores · SEC:anonimizacao.evidencia

**Verificar.**
- há teste de reidentificação documentado, com data e método
- existe regra declarada de generalização para data e para localidade, com o critério registrado
- a tabela de correspondência fica separada da base desidentificada
- caso clínico usado em exemplo, demonstração ou material de treinamento não é reconhecível

**Escalar se.** O serviço quer tratar prompt com texto clínico desidentificado como dado fora da lei, sem teste documentado.

## D13 — Separe as três classes de retenção e persista no prontuário o que virou registro

São três classes, com regimes distintos. Classe A, registro clínico: conteúdo gerado com apoio de IA que influenciou a decisão, mais a gravação e a transcrição que originaram a nota clínica. Ele é exportado para o sistema de registro e persistido lá, com autor, CRM, data e hora, e segue a guarda do prontuário. Classe B, trilha de auditoria: prompt, resposta, versão do modelo, quem revisou, data e hora. Fica em repositório próprio sob controle do serviço, cifrado e com controle de acesso, com prazo declarado, e não vive no provedor. Classe C, log de aplicação e telemetria: nunca recebe conteúdo de paciente nem corpo de requisição, e tem retenção curta definida por necessidade operacional. Rotina de expurgo alcança as classes B e C, e não alcança a A.

**Base.** CEM:art87 · CEM:art88 · CEM:art6 · CFM-1821-2007:art7 · LGPD:art37 · SEC:segredos.logs

**Verificar.**
- há rotina de exportação do conteúdo gerado para o sistema de registro
- a versão do modelo é persistida junto com a saída
- a exportação do prontuário a pedido do paciente inclui esse conteúdo
- o log de aplicação não tem campo de prompt, de resposta nem de payload
- existe cópia sob controle da instituição, e não apenas no provedor

## D14 — Mantenha o sigilo depois da morte do paciente

A obrigação de sigilo sobrevive ao óbito e à publicidade do fato. Registro, prompt e áudio de paciente falecido continuam protegidos, e sua retenção em provedor externo não deixa de ser um problema com a morte. A informação prestada a seguradora sobre circunstâncias da morte limita-se ao conteúdo da declaração de óbito, salvo consentimento expresso do representante legal.

**Base.** CEM:art73 · CEM:art77

**Verificar.**
- o controle de acesso não libera registro por marcação de óbito
- resposta a seguradora tem campo de saída restrito, sem sumarização do prontuário
- a rotina de exclusão a pedido de familiar passa pela análise do prazo de guarda

## D15 — Não reaproveite base assistencial para finalidade diversa da assistência

O dado coletado no atendimento segue a finalidade específica para a qual foi coletado, que é a assistência. Treinamento de modelo, avaliação de produto, benchmark, demonstração e melhoria de serviço são finalidades diversas e exigem base própria. Alcançada a finalidade, a conservação depende de uma das hipóteses legais e o inciso invocado é declarado. Em telemedicina, a resolução própria vincula o dado à finalidade primária de forma expressa. Pesquisa com dispensa de consentimento pressupõe órgão de pesquisa na definição legal, que exclui clínica, consultório e empresa com fins lucrativos. Base de estudo em saúde pública é tratada dentro do órgão, em ambiente controlado.

**Base.** LGPD:art15 · LGPD:art16 · LGPD:art13 · LGPD:art5.XVIII · LGPD:art11 · CFM-2314-2022:art3§7

**Verificar.**
- não há exportação de base assistencial para conjunto de teste, avaliação ou demonstração
- ambiente de desenvolvimento não recebe cópia de base de produção
- projeto rotulado como pesquisa interna tem base declarada e finalidade registrada
- a rotina de treinamento não lê de tabela com dado de paciente

**Escalar se.** Um órgão de pesquisa pretende usar serviço externo de processamento sobre base de estudo em saúde pública.
