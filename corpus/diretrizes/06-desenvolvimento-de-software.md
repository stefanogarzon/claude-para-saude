---
tema: desenvolvimento de software que trata dado de paciente ou integra LLM
aplica-se-a: desenvolvedor, arquiteto de software, revisor de código
fichas: [01, 02, 03, 04, 05, 06, 07, 11, 12]
verificado: 2026-08-11
---

# Desenvolvimento de software com dado de paciente e LLM

O que observar ao escrever ou revisar código que trata dado de paciente ou integra um modelo de linguagem. Dirigido a quem escreve o código e a quem revisa o pull request.

> Parte destas diretrizes decorre da Res. CFM 2.454/2026, **em vigor desde 26/08/2026**. Elas são exigência corrente. Cada diretriz traz a resolução no campo `Base`, ao lado das demais normas que a sustentam.

## D1 — Desidentifique antes da chamada, ou documente a base do envio identificado

Desidentifique antes de chamar o provedor, salvo quando houver base documentada para o envio identificado. Não existe caminho ao provedor sem uma das duas coisas. A desidentificação é etapa do código, não instrução ao usuário. O payload leva os campos que a tarefa exige e nada além.

**Base.** CFM-2454-2026:art6 · CEM:art73 · CEM:art89 · ANPD-19-2024:art9 · SEC:llm.vetores-clinicos

**Verificar.**
- existe um único ponto de saída para o provedor, e ele chama a rotina de desidentificação
- o payload é montado por seleção explícita de campos, não por serialização do registro
- o envio identificado, onde ocorre, tem base registrada por finalidade, com data e responsável
- há teste que falha quando um campo novo do registro alcança o payload
- o histórico reenviado a cada requisição é recortado, não acumulado
- a rotina trata texto livre, e não apenas colunas estruturadas

**Escalar se.** A base legal do fluxo depende de tratar o prompt desidentificado como dado anonimizado.

## D2 — Envie identificador direto só por necessidade demonstrada

Nome, CPF, número de prontuário, CNS e data de nascimento entram na chamada quando a tarefa exige, e a exigência fica escrita. Receita, atestado e sumário de alta endereçados ao paciente são casos legítimos. Fora deles, use pseudônimo gerado com sal secreto e guarde a tabela de correspondência fora do alcance de quem acessa o dataset. A lista de quase-identificadores é a de `SEC:anonimizacao.quase-identificadores`; este arquivo não mantém lista própria.

**Base.** CEM:art73 · CEM:art89 · LGPD:art11 · LGPD:art12 · SEC:anonimizacao.quase-identificadores

**Verificar.**
- cada identificador direto no payload tem justificativa de tarefa registrada no código ou no desenho do fluxo
- arquivo DICOM passa por remoção de `PatientName`, `PatientBirthDate`, `PatientID`, `AccessionNumber`
- anexo em PDF e imagem recebem tratamento próprio, e não seguem em claro
- o pseudônimo não é hash simples de CPF ou de prontuário
- a tabela de correspondência está em banco, bucket e credencial distintos do dataset
- data completa, CEP e identificador de unidade recebem generalização antes de sair

**Escalar se.** O fluxo exige identificador direto e não há base declarada que o ampare.

## D3 — Registre a chamada no repositório clínico, não no log

Toda chamada persiste modelo, versão, provedor, região, data e hora, e a referência do usuário que a originou. Prompt e resposta ficam no repositório clínico da instituição, cifrado e com controle de acesso. O log de aplicação e a telemetria nunca recebem esse conteúdo. São classes distintas, na decisão R4: registro clínico, trilha de auditoria e log de aplicação.

**Base.** CFM-2454-2026:art3 · LGPD:art37 · LGPD:art42 · ANPD-15-2024:art6 · SEC:llm.nist · SEC:segredos.logs

**Verificar.**
- a versão do modelo é gravada junto com a saída, e não inferida depois
- existe cópia da trilha sob controle da instituição, exportável sem depender do fornecedor
- a trilha registra a categoria de dado que saiu e a referência do registro clínico correspondente
- a retenção da trilha acompanha o prazo do registro clínico correspondente
- a trilha permite contar quantos titulares foram afetados em um recorte de tempo
- troca de modelo ou de versão gera registro de reavaliação

## D4 — Exija etapa humana antes de gravar saída em registro clínico

Nenhuma saída de modelo entra em prontuário, laudo, receita ou mensagem ao paciente sem confirmação de um médico identificado. A etapa é do fluxo, não da interface: um endpoint que grava direto descumpre a regra mesmo que a tela peça confirmação. O médico precisa poder editar e rejeitar a sugestão.

> Leitura nossa, extensiva: a vedação alcança sistemas. O ponto não está pacificado. A partir de 26/08/2026 o art. 15, parágrafo único, e o art. 18, §2º da Res. 2.454/2026 sustentam a regra sem depender desta leitura.

**Base.** CFM-2454-2026:art15 · CFM-2454-2026:art18 · CEM:art2 · CEM:art87 · LGPD:art20

**Verificar.**
- a gravação em registro clínico exige um identificador de revisor, com CRM, data e hora
- não há job agendado, webhook ou rota que persista saída de modelo sem revisão
- o campo gerado é editável, e existe caminho para rejeitar a sugestão
- o registro distingue texto gerado de texto revisado
- assinatura digital é aplicada depois da revisão, nunca antes
- triagem, priorização de fila e negativa geradas por modelo têm canal de revisão humana declarado

**Escalar se.** A revisão humana existe no fluxo, mas ocorre em lote e sem leitura efetiva do conteúdo.

## D5 — Permita desligar a IA por paciente

A recusa do paciente precisa de efeito técnico. O sistema guarda a preferência por paciente e o fluxo alternativo funciona sem a ferramenta. Recusa de IA e base legal são exigências distintas e cumulativas: a recusa desliga a ferramenta, não revoga a base legal do atendimento e não autoriza eliminar o prontuário. A base legal se declara por finalidade, em campo próprio.

**Base.** CFM-2454-2026:art5 · CFM-2454-2026:art11 · LGPD:art11 · LGPD:art8§5

**Verificar.**
- existe campo de recusa do uso de IA no cadastro, com data, hora e versão do texto
- a preferência é consultada antes de montar o payload, não depois
- a base legal por finalidade é registrada em campo próprio, separada da recusa
- o consentimento de uso de IA é separado do consentimento de telemedicina
- a revogação do consentimento interrompe as finalidades que dependiam dele e preserva as demais
- o registro da preferência fica no registro clínico, não em sistema de agendamento ou de marketing
- existe rota ou flag que permite atender com a preferência ignorada em emergência, com registro de quem a acionou

## D6 — Mantenha segredo fora do código e do repositório

Chave de API, credencial de banco e certificado ficam em cofre, com escopo por serviço e rotação prevista. Nada disso entra em arquivo versionado, em notebook, em imagem de container ou em captura de tela. Vazamento se resolve por revogação, não por reescrita de histórico.

**Base.** LGPD:art46 · SEC:segredos.armazenamento · SEC:segredos.deteccao · SEC:segredos.privilegio

**Verificar.**
- `.gitignore` cobre `.env*`, e nenhum `.env` com segredo real está versionado
- o repositório tem detecção de segredo no pre-commit e varredura do histórico
- chaves de desenvolvimento, homologação e produção são distintas
- a credencial da aplicação não tem DDL, `GRANT ALL`, `DROP`, `TRUNCATE` nem superusuário (`postgres`, `root`)
- a credencial da aplicação mantém `DELETE`, que é o que executa a eliminação exigida em D9
- a chave do provedor de LLM tem projeto ou workspace próprio por serviço
- credencial de acesso a prontuário não é compartilhada entre pessoas nem embutida em automação
- system prompt não contém segredo nem regra confidencial

## D7 — Escreva log que não serializa payload

Log de aplicação registra evento, identificador de correlação e resultado. É a classe C da decisão R4: nunca contém conteúdo de paciente nem corpo de requisição. Não registra prompt, completion nem header de autorização. Rastreador de erro externo só entra com scrubbing configurado.

**Base.** LGPD:art49 · SEC:segredos.logs · CEM:art6

**Verificar.**
- nenhuma rota com dado de paciente chama `logging.info(request.json)`, `console.log(req.body)` ou equivalente
- o logger não serializa o objeto de resposta do provedor
- `messages`, `prompt`, `completion`, `Authorization` e `api_key` não são campos de log
- Sentry, Rollbar ou equivalente tem `before_send` com scrubbing ativo
- log de query com parâmetros está desligado em produção
- existe log de acesso a dado sensível, com prazo de retenção definido
- log local é cifrado e entra na política de backup e de expurgo

## D8 — Implemente a fixação de região no código e na provisão

A região é parâmetro obrigatório na chamada e na provisão de banco, bucket e índice vetorial. Não use o padrão do fornecedor. Mudança de região é mudança de configuração registrada, com o instrumento de transferência conferido antes. O critério de escolha da região está em `fornecedor:D6`; esta diretriz trata da implementação.

**Base.** LGPD:art33 · ANPD-19-2024:art3.III · ANPD-19-2024:art16 · ANPD-19-2024:anexoII · CFM-2314-2022:art17

**Verificar.**
- a variável de região existe, tem valor definido e é lida em tempo de execução
- não há roteamento automático entre regiões
- backup e réplica de leitura ficam na mesma região do dado primário
- o inventário registra, por fluxo, provedor, produto, endpoint e região
- existe instrumento de cláusulas-padrão assinado entre exportador e importador quando a região está fora do Brasil, da União Europeia e do EEE
- em telemedicina, a plataforma tem sede no Brasil, inscrição no CRM do Estado e responsável técnico médico inscrito no mesmo Conselho
- a cadeia de subprocessadores do fornecedor está documentada

**Escalar se.** Em telemedicina, o provedor de modelo ou de infraestrutura atua por trás da plataforma e não tem sede nem inscrição no Brasil.

## D9 — Defina retenção e descarte por classe de dado

Cada base, log, backup e histórico de conversa tem termo de tratamento declarado e rotina de expurgo que executa. O prazo do registro clínico é o do prontuário e não depende de política do fornecedor. A eliminação a pedido do titular é rotina do sistema e para no que está sob guarda obrigatória: log, histórico, backup e cópia derivada são eliminados; o prontuário não.

**Base.** LGPD:art15 · LGPD:art16 · LGPD:art18 · LGPD:art47 · CFM-1821-2007:art7 · CFM-1821-2007:art8

**Verificar.**
- existe tabela de retenção por classe de dado, com termo declarado, prazo e responsável
- a rotina de expurgo roda e deixa registro de execução
- backup, réplica e histórico de conversa entram na rotina
- existe rotina que atende o pedido de eliminação do titular e registra o que foi preservado por guarda obrigatória
- a expiração é contada a partir do último registro, não da criação
- nenhuma política de ciclo de vida de bucket ou de banco apaga registro clínico por idade
- o contrato com o provedor tem cláusula de eliminação ao término

**Escalar se.** O provedor retém prompts por prazo próprio de segurança.

## D10 — Use base de teste sem dado real

Desenvolvimento, homologação, demonstração e conjunto de avaliação usam dado sintético. Restaurar dump de produção em ambiente inferior é tratamento de dado de paciente, com todos os deveres que isso implica. Prompt de exemplo em issue, documentação ou material de treinamento também.

**Base.** LGPD:art46 · LGPD:art49 · CEM:art75 · SEC:repouso.camadas

**Verificar.**
- os fixtures e seeds de teste vêm do gerador de dado sintético, e nenhum arquivo de seed contém CPF ou nome válidos
- homologação não é restaurada a partir de dump de produção
- desenvolvedor e analista não têm acesso corrente à base de prontuários
- ambientes de desenvolvimento e de produção são segregados, com credenciais distintas
- nenhum caso real aparece em prompt de exemplo, issue, wiki ou captura de tela
- dataset de avaliação não é versionado no repositório
- fine-tuning e exemplos few-shot não usam caso real identificável

**Escalar se.** O projeto é de pesquisa ou de saúde pública e depende de enviar coorte a serviço externo.

## D11 — Entregue o que a instituição precisa para classificar o risco

A classificação de risco é dever da instituição médica, e ela só a faz com informação que o time de desenvolvimento produz. Médico pessoa física fica fora do caput. Monte esse conjunto como artefato do projeto, versionado junto com o código, e atualize a cada mudança de modelo, de finalidade ou de escopo de dados. O nível de risco resultante é informado ao usuário.

**Base.** CFM-2454-2026:art12 · CFM-2454-2026:art13 · CFM-2454-2026:anexoII · CFM-2454-2026:anexoIII.II · LGPD:art37 · LGPD:art38

**Verificar.** Os seis fatores da classificação, na ordem da norma:
- impacto nos direitos fundamentais e na saúde dos pacientes
- criticidade do contexto de uso
- complexidade e grau de autonomia do sistema, incluindo ferramentas e permissões de agente
- finalidade pretendida e finalidades potenciais
- nível de intervenção humana no resultado, descrito por etapa do fluxo
- quantidade e sensibilidade dos dados tratados

E ainda:
- o nível de risco atribuído é exibido ao usuário do sistema
- as limitações e os vieses conhecidos do modelo constam da documentação do fornecedor, arquivada com data e URL
- existe métrica de erro em uso clínico e métrica estratificada por grupo populacional
- há rotina periódica de reavaliação, com data da última execução
- o fluxo de LLM consta do registro de operações de tratamento

**Escalar se.** A solução se aproxima da categoria "inaceitável", ou é escriba e transcrição de consulta, que a resolução não classifica.
