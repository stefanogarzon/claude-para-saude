---
tema: catálogo de gatilhos de auditoria de conformidade
aplica-se-a: médico, responsável técnico, skill de auditoria, revisor de código
fichas: [01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12]
verificado: 2026-08-11
---

# Gatilhos de auditoria

Padrões observáveis em código, configuração ou fluxo que acionam revisão. Cada linha traz o padrão a procurar, a severidade, os identificadores de dispositivo que a sustentam e a pergunta que decide o caso. Para o texto da norma, carregue a ficha pela coluna `Base`. O gatilho obriga a perguntar; não decide.

> A coluna `Norma` registra de que norma o gatilho decorre quando isso muda o regime. A Res. CFM 2.454/2026 está **em vigor desde 26/08/2026**: as linhas que a trazem são exigência corrente. As que não têm base fora dela são as que mudaram de natureza nessa data — de advertência preventiva a exigência autônoma — e o parecer as nomeia uma a uma.

Seções 1 a 9: repositório e configuração de nuvem. Seção 10: documento interno, contrato e console do provedor.

## Envio de dado a LLM

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G01 | payload serializado do registro, sem seleção de campos | `risco` | CFM-2454-2026:art6 · ANPD-19-2024:art9 | quais campos a tarefa exige | enviar só os campos que a tarefa exige, escolhidos um a um | CFM-2454-2026 | o registro inteiro do paciente é enviado ao fornecedor, não só o que a tarefa precisa |
| G02 | conta pessoal, gratuita ou de consumidor com dado identificável | `bloqueante` | PROV:comparativo · CFM-2314-2022:art3 | qual conta chamou, sob qual contrato | contratar plano corporativo em nome do CNPJ, com contrato de operador | — | — |
| G03 | ausência de contrato de operador antes da primeira chamada em produção | `risco` | LGPD:art39 · PROV:comparativo | o instrumento declara finalidade e retenção | assinar o contrato de operador antes da primeira chamada em produção | — | — |
| G04 | configuração do provedor que permite treinar com os inputs | `bloqueante` | LGPD:art11§4 · CFM-2454-2026:art6 · CFM-2314-2022:art3§7 | há registro escrito e datado de que o treino foi desligado | desligar o treino na configuração do provedor e guardar o comprovante datado | CFM-2454-2026 | — |
| G05 | endpoint, produto ou modelo fora do regime de retenção zero declarado | `risco` | PROV:comparativo | contra qual página datada se verificou | contratar o plano em que o fornecedor não retém o conteúdo, ou registrar por escrito a exceção, com data | — | o fornecedor guarda o que recebe, apesar do que foi contratado |
| G06 | busca na web, grounding ou conector de arquivos em prompt clínico | `risco` | PROV:openai · PROV:google | o dado sai do escopo contratado | desligar busca na web e acesso a arquivos externos durante o atendimento | — | o sistema busca informação fora do contrato durante o atendimento |
| G07 | feedback 👍/👎 clínico, logging de requisição para data warehouse, chamada sem `store = false` | `risco` | PROV:anthropic · PROV:google | qual superfície do provedor retém conteúdo | desligar, na configuração do fornecedor, todas as opções que guardam o conteúdo enviado | — | o fornecedor retém conteúdo de consulta por um caminho que não é o principal |
| G08 | exportação em lote de prontuários para treinamento ou demonstração | `bloqueante` | CEM:art89 · CP:art154 | qual base e qual autorização escrita amparam | suspender a exportação até haver base legal e autorização escrita | — | — |
| G09 | índice vetorial ou retriever sem filtro por paciente na consulta | `risco` | SEC:llm.vetores-clinicos | o isolamento está no índice ou só no prompt | filtrar por paciente no próprio índice, não no prompt | — | — |
| G10 | conteúdo externo — PDF, e-mail, laudo — no contexto de agente com ferramenta de rede ou de escrita | `risco` | SEC:llm.owasp-top10 · SEC:llm.agentic | o que o agente faz se o documento trouxer instrução | isolar conteúdo de terceiro do canal de instrução do agente | — | — |
| G11 | saída do modelo renderizada como HTML ou interpolada em SQL, shell ou `eval` | `risco` | SEC:llm.owasp-top10 | há sanitização entre a saída e o destino | sanitizar a saída do modelo antes de qualquer destino executável ou renderizado | — | — |
| G12 | interface que carrega recurso externo citado na saída — imagem, iframe, fetch | `risco` | SEC:llm.owasp-top10 | o dado sai na URL do recurso | bloquear o carregamento de recurso externo citado pela saída | — | — |
| G13 | agente com credencial de escrita em produção, token admin ou HTTP arbitrário | `risco` | SEC:llm.agentic | o que executa sem aprovação humana | retirar credencial de escrita do agente e exigir aprovação humana | — | — |
| G14 | skill, comando, servidor MCP, plugin ou extensão de origem não verificada | `risco` | SEC:llm.agentic | quem homologou a origem, e o que ela acessa | homologar a origem antes de habilitar, com registro de quem homologou | — | há componente de origem não conferida com acesso ao fluxo clínico |
| G15 | notebook ou pipeline de pesquisa que chama API externa sobre coorte identificada | `bloqueante` | LGPD:art13 | o estudo se ampara no art. 13 | amparar o estudo no art. 13, ou desidentificar antes da chamada | — | — |
| G16 | dado identificável fora do escopo da certificação NGS2 do S-RES, ou eliminação de papel com NGS1 | `bloqueante` | CFM-1821-2007:art3 · CFM-1821-2007:art4 · CEM:art18 | qual o nível e o escopo da certificação vigente | estender a certificação ao componente, ou manter o dado fora do escopo dele | — | o prontuário eletrônico não está certificado para guardar este dado |
| G17 | plataforma de telemedicina sem sede no Brasil, sem inscrição no CRM ou sem responsável técnico | `bloqueante` | CFM-2314-2022:art17 · CEM:art18 | quem é o responsável técnico, e em qual CRM | contratar plataforma com sede no Brasil, inscrição no CRM e responsável técnico | — | — |

## Identificadores e desidentificação

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G18 | `cpf`, `nome_paciente`, `prontuario`, `cns` no payload, sem desidentificação nem base documentada | `risco` | CEM:art73 · CEM:art89 · LGPD:art11 | qual base ampara o envio, e onde está registrada | desidentificar antes da chamada, ou registrar a base do envio identificado | — | nome, CPF e número de prontuário saem da clínica sem base registrada |
| G19 | desidentificação que remove apenas identificadores diretos | `risco` | LGPD:art12 · SEC:anonimizacao.quase-identificadores | os quase-identificadores foram tratados | tratar os quase-identificadores, não apenas os identificadores diretos | — | — |
| G20 | `data_nascimento`, `cep` de 8 dígitos, `data_internacao`, `data_alta`, `data_obito` em base dita anonimizada | `risco` | SEC:anonimizacao.quase-identificadores | qual generalização se aplicou | generalizar data e CEP antes de declarar a base anonimizada | — | data de nascimento, CEP e datas de internação permitem reidentificar o paciente na base dita anônima |
| G21 | `evolucao`, `historia`, `observacao`, `laudo` exportados sem tratamento | `risco` | SEC:anonimizacao.quase-identificadores | o texto livre passa pela mesma rotina | passar o texto livre pela mesma rotina aplicada às colunas estruturadas | — | — |
| G22 | DICOM sem remoção de `PatientName`, `PatientBirthDate`, `PatientID` | `risco` | SEC:anonimizacao.quase-identificadores | metadado e pixel foram tratados | remover do arquivo de imagem o nome e a data de nascimento do paciente, inclusive o que está gravado na própria imagem | — | o arquivo de imagem sai com nome e data de nascimento do paciente embutidos |
| G23 | tabela pseudônimo↔paciente no mesmo bucket, banco ou credencial do dataset | `risco` | LGPD:art12 · LGPD:art13 | quem abre os dois; no art. 13 é bloqueante | guardar a tabela que liga o código ao paciente longe de quem acessa a base | — | quem acessa a base anônima também acessa a tabela que revela quem é cada paciente |
| G24 | `md5(cpf)`, `sha256(prontuario)` como pseudônimo, ou dicionário versionado | `risco` | LGPD:art12 · LGPD:art13 | resiste a dicionário; no art. 13 é bloqueante | gerar o pseudônimo com sal secreto, nunca por hash do identificador | — | o código que substitui o nome do paciente pode ser revertido por tentativa |
| G25 | base dita anonimizada, ou destinada a compartilhamento, sem método e medição | `risco` | LGPD:art12 · SEC:anonimizacao.evidencia | quem assinou, e há classe com k=1 | medir o risco residual e registrar método, responsável e data | — | — |

## Segredos e credenciais

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G26 | `.env` versionado com segredo real | `bloqueante` | LGPD:art46 · SEC:segredos.armazenamento | a credencial já foi revogada | revogar a credencial, retirá-la do histórico e movê-la para cofre | — | a senha de acesso ao sistema está guardada junto com o código, ao alcance de quem o tenha |
| G27 | chave de API com valor literal em código, configuração ou `docker-compose.yml` | `bloqueante` | LGPD:art46 · SEC:segredos.armazenamento | quantos ambientes usam a mesma chave | mover a chave para cofre, com uma credencial por ambiente | — | a chave de acesso ao fornecedor está escrita no próprio sistema, e serve a todos os ambientes |
| G28 | histórico do Git com credencial ativa — `sk-`, `AKIA`, `ghp_`, `xoxb-`, chave privada | `bloqueante` | LGPD:art46 · SEC:segredos.deteccao | a credencial consta de revogação | revogar o que vazou e rotacionar todas as credenciais alcançadas pelo histórico | — | uma senha ativa ficou registrada no histórico de alterações do sistema |
| G29 | credencial de prontuário compartilhada entre pessoas ou embutida em automação | `bloqueante` | CEM:art87 · CFM-1821-2007:art3 · LGPD:art46 | cada acesso é atribuível a uma pessoa | credencial nominal por pessoa, com registro de cada acesso ao prontuário | — | — |
| G30 | credencial de aplicação com DDL, `GRANT ALL`, `DROP`, `TRUNCATE`, superusuário, ou bucket aberto a `everyone` | `risco` | SEC:segredos.privilegio | qual o menor privilégio necessário | reduzir a credencial ao menor privilégio que a tarefa exige | — | a credencial do sistema pode apagar ou alterar a base inteira de prontuários |
| G31 | segredo ou regra confidencial dentro do system prompt | `risco` | SEC:llm.owasp-top10 | o system prompt é recuperável pela saída | retirar o segredo do system prompt e tratá-lo como conteúdo recuperável | — | — |

## Logs e telemetria

Classes da decisão R4: registro clínico, trilha de auditoria e log de aplicação. O log de aplicação nunca contém conteúdo de paciente.

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G32 | `logging.info(request.json)`, `console.log(req.body)`, ou `prompt`, `completion`, `Authorization` como campo de log | `risco` | SEC:segredos.logs · LGPD:art49 | existe lista escrita dos campos que o registro técnico pode guardar | definir por escrito quais campos o registro técnico pode guardar; conteúdo de consulta nunca entra | — | o conteúdo da consulta está sendo copiado para o registro técnico do sistema |
| G33 | ausência de trilha das chamadas — categoria de dado que saiu, momento, destino, referência do registro clínico | `risco` | LGPD:art37 · ANPD-15-2024:art6 | como se contam os titulares afetados | registrar categoria de dado, momento, destino e referência ao registro clínico | — | — |
| G34 | trilha de IA só no provedor, ou com retenção inferior à do registro clínico | `risco` | CEM:art6 · CFM-1821-2007:art7 | dá para exportar sob requisição do CRM | manter trilha própria, com retenção igual à do registro clínico | — | — |

## Criptografia e transporte

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G35 | `verify=False`, `rejectUnauthorized: false`, `InsecureSkipVerify: true` em caminho com dado de paciente | `bloqueante` | LGPD:art46 · SEC:tls.versoes | por que a verificação foi desligada | religar a verificação de certificado em todo caminho com dado de paciente | — | o sistema aceita conexão sem conferir com quem está falando |
| G36 | `TLSv1`/`TLSv1.1`, `http://` interno, `sslmode` diferente de `verify-full`, cifras `RC4`, `DES`, `3DES` | `risco` | SEC:tls.versoes · SEC:tls.suites | onde o dado corre sem cifra ou sem validar certificado | exigir da TI conexão cifrada em versão corrente, com verificação de certificado | — | o dado do paciente trafega sem cifra, ou com cifra que já foi quebrada |
| G37 | `AES.MODE_ECB`, `PKCS1v15`, CBC sem HMAC, `md5(`, `Math.random()`/`uuid1()` para chave ou IV, nonce constante | `risco` | SEC:repouso.algoritmo · SEC:repouso.nonce | qual primitiva autenticada está disponível | usar primitiva autenticada, com IV e chave de fonte criptográfica | — | a cifragem usada não protege de fato o dado guardado |
| G38 | chave literal no código, ou no mesmo repositório, banco ou volume do dado cifrado | `bloqueante` | LGPD:art46 · SEC:repouso.chaves | quem acessa a chave acessa o dado | separar chave e dado cifrado, com custódia e rotação próprias | — | — |
| G39 | base com dado de paciente sem criptografia em repouso | `risco` | LGPD:art46 · CFM-2454-2026:anexoI.XV-XVI | o dado ficaria ininteligível a terceiro | cifrar em repouso, incluindo backup e réplica | CFM-2454-2026 | — |
| G40 | cifragem declarada só por disco ou TDE com campos em claro, ou backup e réplica sem cifragem | `risco` | SEC:repouso.camadas | a declaração corresponde ao implementado | cifrar em camada de aplicação ou de campo, além do disco | — | — |
| G41 | endpoint que recebe `paciente_id` e consulta sem checar o vínculo do usuário autenticado, ou papel único | `bloqueante` | LGPD:art46 · CEM:art73 | onde está a checagem de vínculo | checar o vínculo do usuário autenticado a cada acesso ao paciente | — | o sistema entrega o prontuário a quem pedir pelo número, sem checar se aquela pessoa cuida daquele paciente |

## Retenção e descarte

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G42 | ausência de prazo e de expurgo fora do registro clínico — log, histórico, backup, dataset | `risco` | LGPD:art15 · LGPD:art16 | qual o termo declarado, e qual inciso ampara a conservação | definir prazo e expurgo por classe de dado, fora do registro clínico | — | cópias do dado do paciente ficam guardadas sem prazo, fora do prontuário |
| G43 | ciclo de vida de bucket ou banco que apaga registro clínico por idade | `bloqueante` | CFM-1821-2007:art7 | houve parecer de comissão interna | excluir o registro clínico de qualquer política de expiração por idade | — | uma rotina automática apaga registro clínico por idade, e o prontuário tem prazo próprio |
| G44 | registro clínico com prazo de expiração definido pelo provedor | `bloqueante` | CFM-1821-2007:art7 · CEM:art90 | a instituição mantém cópia exportável | manter cópia exportável sob controle da instituição, independente do provedor | — | — |
| G45 | ausência de rotina de eliminação a pedido do titular, ou rotina que apaga registro sob guarda | `risco` | LGPD:art18 · LGPD:art16 | o pedido alcança log e backup, e para no prontuário | rotina que alcança log e backup, e que para no registro clínico sob guarda | — | — |

## Supervisão humana e registro clínico

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G46 | endpoint, job ou webhook que grava saída de modelo em registro clínico sem revisão | `bloqueante` | CFM-2454-2026:art15 · CEM:art2 | onde está a etapa humana no fluxo | etapa de revisão médica antes de a saída virar registro clínico | CFM-2454-2026 | o texto gerado pela IA entra no prontuário sem nenhum médico ler antes |
| G47 | conduta, dose ou diagnóstico entregue ao paciente por chatbot | `bloqueante` | CEM:art37 · CFM-2454-2026:art5 | há mediação humana antes do envio | mediação humana antes de qualquer envio de conduta ao paciente | CFM-2454-2026 | — |
| G48 | interface sem opção de rejeitar ou editar a sugestão | `bloqueante` | CFM-2454-2026:art18 | o médico pode divergir do sistema | permitir rejeitar e editar a sugestão antes de ela valer | CFM-2454-2026 | — |
| G78 | resultado apoiado em IA entregue ao paciente como conclusão do serviço, sem médico identificado que responda por ele | `risco` | CFM-2454-2026:art10 · CEM:art87 | quem é o médico responsável pelo resultado, e como o paciente o alcança | identificar o médico responsável no resultado entregue ao paciente | CFM-2454-2026 | — |
| G79 | ausência de caminho para aditar ou retificar, de forma rastreada, registro clínico já gravado com apoio de IA | `risco` | CFM-2454-2026:art18 · CEM:art87 | como se retifica o que já foi gravado, sem apagar o original | aditamento ou retificação rastreada, preservando o registro original e a ordem cronológica | CFM-2454-2026 | — |
| G80 | ausência de trilha que permita reconstruir uma chamada passada ao modelo, fora do registro clínico | `risco` | CFM-2454-2026:art9 | dá para reconstruir o que o sistema respondeu num atendimento passado | trilha própria da chamada, distinta do registro clínico do art. 4º, V | CFM-2454-2026 | — |
| G49 | registro clínico gravado sem campo de autor, CRM, data e hora | `bloqueante` | CEM:art87 · CFM-2314-2022:art13.d | quem responde pelo conteúdo gravado | gravar autor, CRM, data e hora em cada registro clínico | — | — |
| G50 | assinatura digital antes da revisão, ou emissão em lote com autorização única | `bloqueante` | CEM:art11 · CFM-1821-2007:art5 | o titular do certificado autorizou cada documento | assinar depois da revisão, com autorização por documento | — | — |
| G51 | texto clínico gerado sem campo de registro do uso de IA — ferramenta, versão, revisão | `bloqueante` | CFM-2454-2026:art4 · CEM:art87 | a saída persistida identifica o modelo | campo próprio registrando ferramenta, versão do modelo e quem revisou | CFM-2454-2026 | — |
| G52 | saída de IA que influenciou a decisão registrada, persistida fora do prontuário | `bloqueante` | CEM:art87 · CFM-1821-2007:art7 | o conteúdo entra na exportação do prontuário | trazer para o prontuário a saída de IA que influenciou a decisão registrada | — | — |
| G53 | conteúdo de IA fora da exportação integral do prontuário ao paciente e ao CRM | `risco` | CEM:art88 · CEM:art90 | a exportação alcança o sistema onde ele vive | incluir o conteúdo de IA na exportação integral do prontuário | — | — |
| G54 | triagem, priorização de fila ou negativa gerada por modelo, sem canal de revisão | `risco` | LGPD:art20 | os critérios da decisão estão documentados | canal de revisão humana, com os critérios da decisão documentados | — | — |

## Consentimento e recusa

Recusa do uso de IA e base legal da LGPD são exigências distintas e cumulativas. A recusa desliga a ferramenta; não revoga a base legal nem autoriza eliminar o prontuário.

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G55 | ausência de campo de recusa do uso de IA, ou de caminho alternativo funcional | `bloqueante` | CFM-2454-2026:art5 | o serviço atende com a ferramenta desligada | campo de recusa do uso de IA, e caminho alternativo que atenda de fato | CFM-2454-2026 | — |
| G56 | base legal declarada é o consentimento e não há campo específico e destacado | `risco` | LGPD:art11 | qual hipótese do art. 11 o fluxo declarou | campo específico e destacado para o consentimento, ou outra hipótese do art. 11 | — | — |
| G57 | ausência de campo ou documento que registre a base legal por finalidade | `bloqueante` | LGPD:art11 · LGPD:art37 | qual base ampara cada fluxo, e onde consta | registrar a base legal por finalidade, em campo ou documento próprio | — | — |
| G58 | termo único cobrindo finalidades múltiplas, ou que funde telemedicina e uso de IA | `bloqueante` | LGPD:art11 · CFM-2314-2022:art15 | o paciente pode aceitar um e recusar outro | separar o termo por finalidade, de modo que o paciente aceite uma e recuse outra | — | — |
| G59 | consentimento sem revogação implementada, ou revogação tratada como apagamento total | `bloqueante` | LGPD:art11 · LGPD:art8§5 | a revogação preserva o que tem outra base | implementar revogação que preserve o que tem outra base legal | — | — |
| G60 | consentimento sem data, hora e versão do texto, ou fora do registro clínico | `bloqueante` | CEM:art87 · CFM-2314-2022:art15 | dá para provar qual texto o paciente aceitou | gravar data, hora e versão do texto aceito, dentro do registro clínico | — | — |
| G61 | termo de uso de IA redigido como exclusão de responsabilidade médica | `risco` | CEM:art4 · CFM-2454-2026:art7 | o termo passa ao paciente risco do médico | retirar do termo a cláusula que transfere ao paciente risco do médico | CFM-2454-2026 | — |
| G62 | mecanismo de transferência declarado é o consentimento, e o termo não informa o caráter internacional | `bloqueante` | LGPD:art33 | qual mecanismo do art. 33 o fluxo declarou | informar o caráter internacional da transferência, ou adotar outro mecanismo do art. 33 | — | — |
| G63 | portal que libera prontuário de menor ao responsável sem controle de faixa etária | `risco` | CEM:art74 | quem é o titular do sigilo naquela faixa | controlar a liberação por faixa etária, conforme o titular do sigilo | — | — |

## Ambiente de teste

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G64 | teste, homologação ou avaliação com dado real — dump de produção, seed, planilha | `bloqueante` | LGPD:art46 · SEC:repouso.camadas | quem acessa, e há gerador de dado sintético | gerador de dado sintético para teste, homologação e avaliação | — | — |
| G65 | prompt de exemplo, issue, wiki ou captura de tela com caso real | `bloqueante` | CEM:art75 · CP:art154 | o conteúdo já está público ou versionado | remover o conteúdo e tratar a exposição como incidente | — | — |
| G66 | fine-tuning ou few-shot a partir de caso real identificável | `bloqueante` | LGPD:art11 · CEM:art89 | qual base e qual autorização amparam | base legal e autorização escrita, ou treinar com dado sintético | — | — |
| G67 | acesso corrente de desenvolvedor ou analista à base de prontuários | `risco` | LGPD:art46 · CEM:art73 | o acesso é nominal, temporário e registrado | acesso nominal, temporário e registrado, com revisão periódica | — | — |
| G81 | piloto ou teste A/B cuja saída chega ao médico ou ao paciente, sem consentimento específico de participação | `risco` | CFM-2454-2026:art10 · CFM-2454-2026:art20 | o paciente consentiu em participar, e não apenas em ser atendido | consentimento específico de participação, distinto do termo de atendimento | CFM-2454-2026 | o paciente participa de um teste sem ter consentido em participar |
| G82 | avaliação de modelo em fluxo assistencial sem parecer de comissão de ética nem decisão registrada de dispensa | `risco` | CFM-2454-2026:art20 | quem decidiu que não é pesquisa, e onde consta | submeter ao CEP, ou registrar por escrito a decisão de que não é pesquisa | CFM-2454-2026 | — |

## Governança e classificação de risco

| # | Gatilho | Severidade | Base | O que checar | Mitigação | Norma | Efeito |
|---|---|---|---|---|---|---|---|
| G68 | fluxo de LLM ausente do registro de operações ou do inventário | `bloqueante` | LGPD:art37 | o inventário diz qual produto, qual serviço e em que país é processado | inventariar o uso de IA: qual produto, qual serviço e em que país é processado | — | o uso de IA não consta do inventário de tratamento de dados da clínica |
| G69 | variável de região ausente, com padrão do fornecedor, ou com roteamento automático | `risco` | LGPD:art33 · ANPD-19-2024:art3.III | a região é lida da configuração em execução | fixar a região na configuração, lida em execução | — | — |
| G70 | região fora do Brasil, da União Europeia e do EEE sem cláusulas-padrão assinadas | `bloqueante` | ANPD-19-2024:art16 · ANPD-19-2024:anexoII | quem assinou o instrumento, e em que data | assinar cláusulas-padrão, ou mover o processamento para região adequada | — | o dado do paciente é processado fora do Brasil, da União Europeia e do Espaço Econômico Europeu, sem o contrato que a ANPD exige |
| G71 | ausência de registro interno de incidentes, ou não comunicação sem justificativa | `bloqueante` | ANPD-15-2024:art10 | o registro cobre os incidentes não comunicados | manter registro interno de incidentes, inclusive dos não comunicados | — | — |
| G72 | runbook que dispensa comunicação ao titular por os dados estarem criptografados | `bloqueante` | ANPD-15-2024:art9 · LGPD:art48 | a dispensa tem base na Res. 15/2024 | rever a dispensa de comunicação contra a Res. ANPD 15/2024 | — | — |
| G73 | ausência de avaliação de risco documentada antes de pôr LLM em fluxo clínico | `risco` | CFM-2454-2026:art12 · LGPD:art38 | os seis fatores foram percorridos | avaliação de risco documentada antes de pôr o LLM em fluxo clínico | CFM-2454-2026 | a IA entrou no atendimento sem avaliação de risco escrita |
| G83 | diretrizes de segurança, ética e transparência no uso de IA sem aprovação do Diretor Técnico | `risco` | CFM-2454-2026:art14 · CFM-2454-2026:art8 | quem aprovou as diretrizes, e quando | submeter as diretrizes de IA à aprovação do Diretor Técnico | CFM-2454-2026 | — |
| G84 | trilha de auditoria de IA e configuração não exportáveis sob requisição de órgão de controle | `risco` | CFM-2454-2026:art14 · CFM-2454-2026:art9 | como se atende a uma requisição do CRM ou do MP | rotina de exportação de log, relatório e configuração, com prazo de retenção declarado | CFM-2454-2026 | — |
| G85 | instituição médica sem relatório periódico de desempenho, limitações e vieses do sistema de IA | `risco (instituição que desenvolve ou contrata, art. 14)` | CFM-2454-2026:art14 · CFM-2454-2026:art3 | qual a periodicidade declarada, e qual a data do último | relatório recorrente em linguagem clara, com data e periodicidade declaradas | CFM-2454-2026 | — |
| G86 | sistema de IA em produção sem rotina declarada de revisão periódica | `risco` | CFM-2454-2026:art14 · CFM-2454-2026:art12 | de quanto em quanto tempo o sistema é reavaliado | rotina de revisão periódica em produção, com atualização de modelo controlada | CFM-2454-2026 | — |
| G74 | ausência de métrica de erro estratificada, ou mudança de modelo sem reavaliação | `risco` | CFM-2454-2026:anexoIII.II · CFM-2454-2026:anexoII | como um viés seria detectado antes do dano | métrica de erro estratificada, e reavaliação a cada troca de modelo | CFM-2454-2026 | — |
| G75 | documentação do fornecedor sem limitações e vieses, ou sem data de verificação | `risco` | CFM-2454-2026:art3 · PROV:erros-comuns | contra qual documento datado se decidiu | exigir do fornecedor documento datado com limitações e vieses | CFM-2454-2026 | — |
| G76 | ausência de evidência de orientação da equipe quanto ao sigilo — política, treinamento ou termo | `risco` | CEM:art78 | quem responde pelo uso por não médicos | política interna e treinamento da equipe quanto ao sigilo, com evidência | — | — |
| G77 | descrição clínica ou CID em cobrança, agendamento ou faturamento, como dado não sensível | `risco` | CEM:art79 · LGPD:art11§1-§3 | o fluxo financeiro segrega o campo clínico | segregar o campo clínico do fluxo financeiro | — | — |

## Escalar se

Pontos sem entendimento consolidado. A decisão sobe ao responsável técnico ou ao jurídico.

- O provedor de LLM é operador ou controlador autônomo no fluxo em exame.
- A base do art. 11, II, "f" alcança ou não a cadeia de fornecedores de tecnologia.
- Prompt desidentificado é ou não dado pessoal para efeito da base legal adotada.
- Supervisão humana existente, mas exercida em lote e sem leitura efetiva.
- Retenção de prompts e logs pelo provedor por prazo próprio de segurança.
- Solução próxima da categoria "inaceitável", sem critério normativo definido.
- Escriba e transcrição de consulta, não classificados em nenhum nível de risco.
- Perda do regime de pequeno porte por tratamento de alto risco.
- Alcance da certificação NGS2 sobre componente de IA de terceiro.
