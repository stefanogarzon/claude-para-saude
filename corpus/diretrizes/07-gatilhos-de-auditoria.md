---
tema: catálogo de gatilhos de auditoria de conformidade
aplica-se-a: skill de auditoria de código, revisor de código, responsável técnico
fichas: [01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12]
verificado: 2026-08-11
---

# Gatilhos de auditoria

Padrões observáveis em código, configuração ou fluxo que acionam revisão. Cada linha traz o padrão a procurar, a severidade, os identificadores de dispositivo que a sustentam e a pergunta que decide o caso. Para o texto da norma, carregue a ficha pela coluna `Base`. O gatilho obriga a perguntar; não decide.

> Linhas com † decorrem da Res. CFM 2.454/2026, em vigor a partir de 26/08/2026. Até essa data, valem o Código de Ética Médica, as Res. CFM 1.821/2007 e 2.314/2022 e a Lei 13.709/2018.

Seções 1 a 9: repositório e configuração de nuvem. Seção 10: documento interno, contrato e console do provedor.

## Envio de dado a LLM

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| † payload serializado do registro, sem seleção de campos | `risco` | CFM-2454-2026:art6 · ANPD-19-2024:art9 | quais campos a tarefa exige |
| conta pessoal, gratuita ou de consumidor com dado identificável | `bloqueante` | PROV:comparativo · CFM-2314-2022:art3 | qual conta chamou, sob qual contrato |
| ausência de contrato de operador antes da primeira chamada em produção | `risco` | LGPD:art39 · PROV:comparativo | o instrumento declara finalidade e retenção |
| † configuração do provedor que permite treinar com os inputs | `bloqueante` | LGPD:art11§4 · CFM-2454-2026:art6 · CFM-2314-2022:art3§7 | há opt-out documentado e datado |
| endpoint, produto ou modelo fora do regime de retenção zero declarado | `risco` | PROV:comparativo | contra qual página datada se verificou |
| busca na web, grounding ou conector de arquivos em prompt clínico | `risco` | PROV:openai · PROV:google | o dado sai do escopo contratado |
| feedback 👍/👎 clínico, logging de requisição para data warehouse, chamada sem `store = false` | `risco` | PROV:anthropic · PROV:google | qual superfície do provedor retém conteúdo |
| exportação em lote de prontuários para treinamento ou demonstração | `bloqueante` | CEM:art89 · CP:art154 | qual base e qual autorização escrita amparam |
| índice vetorial ou retriever sem filtro por paciente na consulta | `risco` | SEC:llm.vetores-clinicos | o isolamento está no índice ou só no prompt |
| conteúdo externo — PDF, e-mail, laudo — no contexto de agente com ferramenta de rede ou de escrita | `risco` | SEC:llm.owasp-top10 · SEC:llm.agentic | o que o agente faz se o documento trouxer instrução |
| saída do modelo renderizada como HTML ou interpolada em SQL, shell ou `eval` | `risco` | SEC:llm.owasp-top10 | há sanitização entre a saída e o destino |
| interface que carrega recurso externo citado na saída — imagem, iframe, fetch | `risco` | SEC:llm.owasp-top10 | o dado sai na URL do recurso |
| agente com credencial de escrita em produção, token admin ou HTTP arbitrário | `risco` | SEC:llm.agentic | o que executa sem aprovação humana |
| skill, comando, servidor MCP, plugin ou extensão de origem não verificada | `risco` | SEC:llm.agentic | quem homologou a origem, e o que ela acessa |
| notebook ou pipeline de pesquisa que chama API externa sobre coorte identificada | `bloqueante` | LGPD:art13 | o estudo se ampara no art. 13 |
| dado identificável fora do escopo da certificação NGS2 do S-RES, ou eliminação de papel com NGS1 | `bloqueante` | CFM-1821-2007:art3 · CFM-1821-2007:art4 · CEM:art18 | qual o nível e o escopo da certificação vigente |
| plataforma de telemedicina sem sede no Brasil, sem inscrição no CRM ou sem responsável técnico | `bloqueante` | CFM-2314-2022:art17 · CEM:art18 | quem é o responsável técnico, e em qual CRM |

## Identificadores e desidentificação

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| `cpf`, `nome_paciente`, `prontuario`, `cns` no payload, sem desidentificação nem base documentada | `risco` | CEM:art73 · CEM:art89 · LGPD:art11 | qual base ampara o envio, e onde está registrada |
| desidentificação que remove apenas identificadores diretos | `risco` | LGPD:art12 · SEC:anonimizacao.quase-identificadores | os quase-identificadores foram tratados |
| `data_nascimento`, `cep` de 8 dígitos, `data_internacao`, `data_alta`, `data_obito` em base dita anonimizada | `risco` | SEC:anonimizacao.quase-identificadores | qual generalização se aplicou |
| `evolucao`, `historia`, `observacao`, `laudo` exportados sem tratamento | `risco` | SEC:anonimizacao.quase-identificadores | o texto livre passa pela mesma rotina |
| DICOM sem remoção de `PatientName`, `PatientBirthDate`, `PatientID` | `risco` | SEC:anonimizacao.quase-identificadores | metadado e pixel foram tratados |
| tabela pseudônimo↔paciente no mesmo bucket, banco ou credencial do dataset | `risco` | LGPD:art12 · LGPD:art13 | quem abre os dois; no art. 13 é bloqueante |
| `md5(cpf)`, `sha256(prontuario)` como pseudônimo, ou dicionário versionado | `risco` | LGPD:art12 · LGPD:art13 | resiste a dicionário; no art. 13 é bloqueante |
| base dita anonimizada, ou destinada a compartilhamento, sem método e medição | `risco` | LGPD:art12 · SEC:anonimizacao.evidencia | quem assinou, e há classe com k=1 |

## Segredos e credenciais

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| `.env` versionado com segredo real | `bloqueante` | LGPD:art46 · SEC:segredos.armazenamento | a credencial já foi revogada |
| chave de API com valor literal em código, configuração ou `docker-compose.yml` | `bloqueante` | LGPD:art46 · SEC:segredos.armazenamento | quantos ambientes usam a mesma chave |
| histórico do Git com credencial ativa — `sk-`, `AKIA`, `ghp_`, `xoxb-`, chave privada | `bloqueante` | LGPD:art46 · SEC:segredos.deteccao | a credencial consta de revogação |
| credencial de prontuário compartilhada entre pessoas ou embutida em automação | `bloqueante` | CEM:art87 · CFM-1821-2007:art3 · LGPD:art46 | cada acesso é atribuível a uma pessoa |
| credencial de aplicação com DDL, `GRANT ALL`, `DROP`, `TRUNCATE`, superusuário, ou bucket aberto a `everyone` | `risco` | SEC:segredos.privilegio | qual o menor privilégio necessário |
| segredo ou regra confidencial dentro do system prompt | `risco` | SEC:llm.owasp-top10 | o system prompt é recuperável pela saída |

## Logs e telemetria

Classes da decisão R4: registro clínico, trilha de auditoria e log de aplicação. O log de aplicação nunca contém conteúdo de paciente.

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| `logging.info(request.json)`, `console.log(req.body)`, ou `prompt`, `completion`, `Authorization` como campo de log | `risco` | SEC:segredos.logs · LGPD:art49 | há allowlist de campos no log |
| ausência de trilha das chamadas — categoria de dado que saiu, momento, destino, referência do registro clínico | `risco` | LGPD:art37 · ANPD-15-2024:art6 | como se contam os titulares afetados |
| trilha de IA só no provedor, ou com retenção inferior à do registro clínico | `risco` | CEM:art6 · CFM-1821-2007:art7 | dá para exportar sob requisição do CRM |

## Criptografia e transporte

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| `verify=False`, `rejectUnauthorized: false`, `InsecureSkipVerify: true` em caminho com dado de paciente | `bloqueante` | LGPD:art46 · SEC:tls.versoes | por que a verificação foi desligada |
| `TLSv1`/`TLSv1.1`, `http://` interno, `sslmode` diferente de `verify-full`, cifras `RC4`, `DES`, `3DES` | `risco` | SEC:tls.versoes · SEC:tls.suites | onde o dado corre sem cifra ou sem validar certificado |
| `AES.MODE_ECB`, `PKCS1v15`, CBC sem HMAC, `md5(`, `Math.random()`/`uuid1()` para chave ou IV, nonce constante | `risco` | SEC:repouso.algoritmo · SEC:repouso.nonce | qual primitiva autenticada está disponível |
| chave literal no código, ou no mesmo repositório, banco ou volume do dado cifrado | `bloqueante` | LGPD:art46 · SEC:repouso.chaves | quem acessa a chave acessa o dado |
| † base com dado de paciente sem criptografia em repouso | `risco` | LGPD:art46 · CFM-2454-2026:anexoI.XV-XVI | o dado ficaria ininteligível a terceiro |
| cifragem declarada só por disco ou TDE com campos em claro, ou backup e réplica sem cifragem | `risco` | SEC:repouso.camadas | a declaração corresponde ao implementado |
| endpoint que recebe `paciente_id` e consulta sem checar o vínculo do usuário autenticado, ou papel único | `bloqueante` | LGPD:art46 · CEM:art73 | onde está a checagem de vínculo |

## Retenção e descarte

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| ausência de prazo e de expurgo fora do registro clínico — log, histórico, backup, dataset | `risco` | LGPD:art15 · LGPD:art16 | qual o termo declarado, e qual inciso ampara a conservação |
| ciclo de vida de bucket ou banco que apaga registro clínico por idade | `bloqueante` | CFM-1821-2007:art7 | houve parecer de comissão interna |
| registro clínico com prazo de expiração definido pelo provedor | `bloqueante` | CFM-1821-2007:art7 · CEM:art90 | a instituição mantém cópia exportável |
| ausência de rotina de eliminação a pedido do titular, ou rotina que apaga registro sob guarda | `risco` | LGPD:art18 · LGPD:art16 | o pedido alcança log e backup, e para no prontuário |

## Supervisão humana e registro clínico

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| † endpoint, job ou webhook que grava saída de modelo em registro clínico sem revisão | `bloqueante` | CFM-2454-2026:art15 · CEM:art2 | onde está a etapa humana no fluxo |
| † conduta, dose ou diagnóstico entregue ao paciente por chatbot | `bloqueante` | CEM:art37 · CFM-2454-2026:art5 | há mediação humana antes do envio |
| † interface sem opção de rejeitar ou editar a sugestão | `bloqueante` | CFM-2454-2026:art18 | o médico pode divergir do sistema |
| registro clínico gravado sem campo de autor, CRM, data e hora | `bloqueante` | CEM:art87 · CFM-2314-2022:art13.d | quem responde pelo conteúdo gravado |
| assinatura digital antes da revisão, ou emissão em lote com autorização única | `bloqueante` | CEM:art11 · CFM-1821-2007:art5 | o titular do certificado autorizou cada documento |
| † texto clínico gerado sem campo de registro do uso de IA — ferramenta, versão, revisão | `bloqueante` | CFM-2454-2026:art4 · CEM:art87 | a saída persistida identifica o modelo |
| saída de IA que influenciou a decisão registrada, persistida fora do prontuário | `bloqueante` | CEM:art87 · CFM-1821-2007:art7 | o conteúdo entra na exportação do prontuário |
| conteúdo de IA fora da exportação integral do prontuário ao paciente e ao CRM | `risco` | CEM:art88 · CEM:art90 | a exportação alcança o sistema onde ele vive |
| triagem, priorização de fila ou negativa gerada por modelo, sem canal de revisão | `risco` | LGPD:art20 | os critérios da decisão estão documentados |

## Consentimento e recusa

Recusa do uso de IA e base legal da LGPD são exigências distintas e cumulativas. A recusa desliga a ferramenta; não revoga a base legal nem autoriza eliminar o prontuário.

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| † ausência de campo de recusa do uso de IA, ou de caminho alternativo funcional | `bloqueante` | CFM-2454-2026:art5 | o serviço atende com a ferramenta desligada |
| base legal declarada é o consentimento e não há campo específico e destacado | `risco` | LGPD:art11 | qual hipótese do art. 11 o fluxo declarou |
| ausência de campo ou documento que registre a base legal por finalidade | `bloqueante` | LGPD:art11 · LGPD:art37 | qual base ampara cada fluxo, e onde consta |
| termo único cobrindo finalidades múltiplas, ou que funde telemedicina e uso de IA | `bloqueante` | LGPD:art11 · CFM-2314-2022:art15 | o paciente pode aceitar um e recusar outro |
| consentimento sem revogação implementada, ou revogação tratada como apagamento total | `bloqueante` | LGPD:art11 · LGPD:art8§5 | a revogação preserva o que tem outra base |
| consentimento sem data, hora e versão do texto, ou fora do registro clínico | `bloqueante` | CEM:art87 · CFM-2314-2022:art15 | dá para provar qual texto o paciente aceitou |
| † termo de uso de IA redigido como exclusão de responsabilidade médica | `risco` | CEM:art4 · CFM-2454-2026:art7 | o termo passa ao paciente risco do médico |
| mecanismo de transferência declarado é o consentimento, e o termo não informa o caráter internacional | `bloqueante` | LGPD:art33 | qual mecanismo do art. 33 o fluxo declarou |
| portal que libera prontuário de menor ao responsável sem controle de faixa etária | `risco` | CEM:art74 | quem é o titular do sigilo naquela faixa |

## Ambiente de teste

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| teste, homologação ou avaliação com dado real — dump de produção, seed, planilha | `bloqueante` | LGPD:art46 · SEC:repouso.camadas | quem acessa, e há gerador de dado sintético |
| prompt de exemplo, issue, wiki ou captura de tela com caso real | `bloqueante` | CEM:art75 · CP:art154 | o conteúdo já está público ou versionado |
| fine-tuning ou few-shot a partir de caso real identificável | `bloqueante` | LGPD:art11 · CEM:art89 | qual base e qual autorização amparam |
| acesso corrente de desenvolvedor ou analista à base de prontuários | `risco` | LGPD:art46 · CEM:art73 | o acesso é nominal, temporário e registrado |

## Governança e classificação de risco

| Gatilho | Severidade | Base | O que checar |
|---|---|---|---|
| fluxo de LLM ausente do registro de operações ou do inventário | `bloqueante` | LGPD:art37 | o inventário traz produto, endpoint e região |
| variável de região ausente, com padrão do fornecedor, ou com roteamento automático | `risco` | LGPD:art33 · ANPD-19-2024:art3.III | a região é lida da configuração em execução |
| região fora do Brasil, da União Europeia e do EEE sem cláusulas-padrão assinadas | `bloqueante` | ANPD-19-2024:art16 · ANPD-19-2024:anexoII | quem assinou o instrumento, e em que data |
| ausência de registro interno de incidentes, ou não comunicação sem justificativa | `bloqueante` | ANPD-15-2024:art10 | o registro cobre os incidentes não comunicados |
| runbook que dispensa comunicação ao titular por os dados estarem criptografados | `bloqueante` | ANPD-15-2024:art9 · LGPD:art48 | a dispensa tem base na Res. 15/2024 |
| † ausência de avaliação de risco documentada antes de pôr LLM em fluxo clínico | `risco` | CFM-2454-2026:art12 · LGPD:art38 | os seis fatores foram percorridos |
| † ausência de métrica de erro estratificada, ou mudança de modelo sem reavaliação | `risco` | CFM-2454-2026:anexoIII.II · CFM-2454-2026:anexoII | como um viés seria detectado antes do dano |
| † documentação do fornecedor sem limitações e vieses, ou sem data de verificação | `risco` | CFM-2454-2026:art3 · PROV:erros-comuns | contra qual documento datado se decidiu |
| ausência de evidência de orientação da equipe quanto ao sigilo — política, treinamento ou termo | `risco` | CEM:art78 | quem responde pelo uso por não médicos |
| descrição clínica ou CID em cobrança, agendamento ou faturamento, como dado não sensível | `risco` | CEM:art79 · LGPD:art11§1-§3 | o fluxo financeiro segrega o campo clínico |

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
