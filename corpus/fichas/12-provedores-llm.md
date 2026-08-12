---
tema: Políticas de retenção e de treinamento dos provedores de LLM
ementa: Estado declarado das políticas de Anthropic, OpenAI e Google, verificado em 2026-08-11
status: informativo e contratual; não normativo
meia_vida: curta
aviso: >-
  Reverificar cada URL antes de qualquer uso, publicação ou decisão de arquitetura.
  Datas declaradas pelas próprias páginas: Anthropic treino 16/03/2026, Anthropic ZDR
  09/06/2026, Anthropic consumidor e BAA 01/07/2026, OpenAI privacidade corporativa
  08/01/2026, Google HIPAA 11/08/2026, Google abuse monitoring e ZDR 07/08/2026;
  termos da Gemini API com effective date de 23/03/2026.
  Política de provedor não é norma e muda sem aviso.
verificado: 2026-08-11
fonte: cada afirmação traz a URL da página oficial no campo Literal
---

# Provedores de LLM — retenção e treinamento

> **Aviso de reverificação.** Esta ficha tem meia-vida curta. Cada linha foi verificada na página oficial em 2026-08-11, e a data de atualização declarada pela própria página está registrada em cada item. Nenhum item desta ficha deve ser citado, publicado ou usado como base de decisão sem reabrir a URL correspondente e conferir a data. Política de provedor é compromisso contratual revogável, não controle técnico.

| Página | Data declarada pela própria página |
|---|---|
| privacy.claude.com/en/articles/7996868 — treino | 16/03/2026 |
| privacy.claude.com/en/articles/8956058 — ZDR | 09/06/2026 |
| privacy.claude.com/en/articles/10023548 — consumidor | 01/07/2026 |
| support.claude.com/en/articles/15455031 — Covered Models e BAA | 01/07/2026 |
| openai.com/enterprise-privacy | 08/01/2026 |
| ai.google.dev/gemini-api/terms | effective date de 23/03/2026 |
| cloud.google.com/security/compliance/hipaa | 11/08/2026 |
| docs.cloud.google.com — abuse monitoring e ZDR | 07/08/2026 |

Itens: 5. Marcações `NÃO VERIFICADO` consolidadas ao final.

**BAA e direito brasileiro.** BAA (Business Associate Agreement) é instrumento do regime jurídico dos Estados Unidos, previsto na HIPAA. Assinar BAA com um provedor não cria base legal do art. 11 da LGPD para tratar dado de saúde, não é mecanismo de transferência internacional do art. 33, e não substitui o contrato de operador. A elegibilidade sob BAA é usada aqui como indicador do que o provedor aceita cobrir contratualmente, não como conformidade com a LGPD.

---

## PROV:anthropic

**Ementa.** Treino, retenção, Zero Data Retention e elegibilidade sob BAA nos produtos da Anthropic.

**Literal.**

*Treino em produtos comerciais.* https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training — verificado em 2026-08-11; a página declara "Last updated: March 16, 2026".
> "By default, we will not use your inputs or outputs from our commercial products to train our models"

A página exemplifica o alcance de "commercial products" assim, verbatim: "(e.g. Claude for Work, Anthropic API, Claude Gov, etc.)". Exceção declarada: feedback explícito (👍/👎) faz a conversa inteira ser armazenada por até 5 anos, deslinkada de user ID e customer ID, com possibilidade de uso em treino. Dado de conector (Google Drive, MCP) está excluído, salvo se copiado para o chat. Desligamento: Claude for Work → Organization settings → Data and Privacy → "Rate chats"; Workbench → Settings → Privacy, por administrador.

*Produtos de consumidor (Free, Pro, Max).* https://privacy.claude.com/en/articles/10023548 — verificado em 2026-08-11; a página declara "last updated July 1, 2026".
- Conversa deletada sai do histórico imediatamente e é removida do backend em até 30 dias.
- Com "model improvement" habilitado pelo usuário: retenção em forma de-identificada por até 5 anos no pipeline de treino, aplicável apenas a chats novos criados após habilitar.
- Chats "Incognito" nunca são usados para treino.
- Violação da Usage Policy: inputs e outputs retidos por até 2 anos; scores de classificação de segurança por até 7 anos.
- Aplica-se também a Claude Code usado com conta de consumidor.

*Zero Data Retention — artigo do Privacy Center.* https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to — verificado em 2026-08-11; a página declara "June 9, 2026". O artigo é curto e delimita o alcance em uma frase, verbatim: "Under these agreements, the only products to which zero data retention applies are eligible Anthropic APIs, Anthropic products that use your Commercial organization API key (including Claude Code accessed via the API), and Claude Code for Enterprise plans."
- Ressalva no mesmo artigo, verbatim: "Under these arrangements, Anthropic still retains User Safety classifier results in order to enforce our Usage Policy."
- Também verbatim: "zero data retention requests are reviewed and applied on a per-organization basis". Estado verificável em "Settings > Privacy Controls > Data retention period". Obtenção via Sales.
- Sobre o BAA, verbatim: "customers of Anthropic's HIPAA-eligible services are subject to certain configuration requirements and limitations on what features/integrations are available (e.g., the BAA would not apply to use of the web search functionality)".

*Zero Data Retention — escopo detalhado.* https://platform.claude.com/docs/en/manage-claude/api-and-data-retention — verificado em 2026-08-11. As listas abaixo estão nesta página, não no artigo do Privacy Center.
- Definição, verbatim: "Under a ZDR arrangement, Anthropic does not store customer prompts or responses at rest after the API response is returned." ZDR é habilitado por organização, e cada organização nova exige habilitação própria.
- "What ZDR covers": Claude Messages e Token Counting APIs, para as features marcadas como elegíveis na tabela de elegibilidade; Claude Code com chave de API de organização Commercial ou via Claude Enterprise com ZDR habilitado, com a ressalva de que dados de produtividade do metrics logging ficam de fora do ZDR; Claude Platform on AWS, mediante pedido.
- "What ZDR does not cover", lista completa da página: Console e Workbench; Claude Managed Agents, recurso stateful cujas transcrições persistem até deleção; produtos de consumidor Free, Pro e Max, inclusive quando usam Claude Code; interfaces de produto do Claude Teams e do Claude Enterprise, salvo Claude Code via Enterprise com ZDR; Claude for Excel; Claude Fable 5 e Claude Mythos 5, que exigem 30 dias; integrações de terceiros; CORS, que exige proxy no backend; conteúdo flagrado e legal holds.
- Features stateful — Batch API, Files API, code execution — não estão nessa lista de exclusões: aparecem como "No" na tabela de elegibilidade. A página é explícita sobre o efeito, verbatim: "Under ZDR, the API does **not** block these features; using one is a choice to step outside your ZDR arrangement for that specific data, and the feature's own documented retention policy applies."
- Conteúdo flagrado, verbatim: "if a chat or session is flagged, Anthropic may retain inputs and outputs for up to 2 years."
- HIPAA readiness e ZDR são arranjos distintos. Verbatim: "If your organization handles PHI, HIPAA readiness is the arrangement to use; you do not also need ZDR."

*Retenções específicas declaradas.* https://platform.claude.com/docs/en/manage-claude/api-and-data-retention — verificado em 2026-08-11.

| Item | Retenção |
|---|---|
| Covered Models (exemplos citados: Claude Fable 5, Claude Mythos 5) | 30 dias obrigatórios |
| Batch processing | 29 dias |
| Code execution (container) | até 30 dias |
| Compliance API: Activity Feed e transcrições de sessão remota | 6 anos |
| Compliance API: transcrições de sessão local — Cowork e Claude Code na máquina do usuário | 6 anos por padrão, ou o prazo de retenção customizado da organização |
| Prompt caching | KV cache em memória durante o TTL, deletado depois |
| Structured outputs (JSON schemas) | até 24 horas desde o último uso |
| Files API | "until explicitly deleted" — sem prazo |
| Conteúdo flagrado ou sob legal hold | até 2 anos |

*HIPAA e BAA.* https://support.claude.com/en/articles/15455031-covered-models-under-a-business-associate-agreement-baa — artigo datado de 01/07/2026, verificado em 2026-08-11.
> "Cowork is not an Eligible Service under Anthropic's BAA in any configuration"
> "There's currently no configuration that allows BAA-covered access to Covered Models in Claude Code or Cowork"

Tabela "Coverage at a glance" do artigo, transcrita na íntegra, com as dez linhas:

| Produto | Acesso | Retenção | Eligible Service sob BAA | Acessa Covered Models |
|---|---|---|---|---|
| Chat | Claude Enterprise | padrão | sim | sim |
| Claude Code | Claude Enterprise | ZDR | sim | não |
| Claude Code | Claude Enterprise | padrão | não | sim |
| Claude Code | organização de API 1P | ZDR | sim | não |
| Claude Code | organização de API 1P | padrão | não | sim |
| Claude Code | API 3P (somente Google Vertex)* | padrão | não | sim |
| Cowork | Claude Enterprise | padrão | não | sim |
| Claude API (1P) | HIPAA-ready API | padrão | sim | sim |
| Claude API (1P) | API regular | ZDR | sim | não |
| Claude API (1P) | API regular | padrão | não | sim |

\* Nota da própria tabela, verbatim: "Anthropic's BAA doesn't apply to services purchased through a third-party cloud provider."

Nota que precede a tabela, verbatim: "Coverage under Anthropic's BAA always requires (a) signing the BAA, and (b) accessing Anthropic's products via their HIPAA-ready or (in the case of Claude Code) zero data retention configurations."

Restrições operacionais declaradas no artigo, verbatim: "HIPAA readiness and ZDR cannot coexist on a single 1P API organization."; "Claude Code isn't an Eligible Service on a HIPAA-ready API organization."; "Requests to a Covered Model from a ZDR-enabled organization or workspace return an error."

Exclusões declaradas: planos de consumidor; provedores de nuvem terceiros, aos quais o BAA não se aplica; e organizações de API padrão sem configuração HIPAA e sem ZDR. HIPAA readiness não está disponível em Claude Platform on AWS nem em Microsoft Foundry, conforme platform.claude.com/docs, verbatim: "Claude Platform on AWS and Microsoft Foundry: HIPAA readiness is not available on these platforms." Cláusula de responsabilidade do cliente: a organização deve garantir que "PHI is only submitted through Eligible Services".

O conflito entre Covered Models e Claude Code sob BAA é estrutural nos termos do próprio artigo: Covered Models exigem 30 dias de retenção, e Claude Code sob BAA exige ZDR.

**Fonte.** https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training · https://privacy.claude.com/en/articles/10023548 · https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to · https://platform.claude.com/docs/en/manage-claude/api-and-data-retention · https://support.claude.com/en/articles/15455031-covered-models-under-a-business-associate-agreement-baa · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A página de treino nomeia como exemplo Claude for Work, a API e o Claude Gov. Team e Enterprise são planos de Claude for Work, e por isso os lemos como abrangidos. A extensão é nossa, não da página; em documento contratual, citar os exemplos que a página traz.

Este projeto entrega skills e prompts para uso em Claude Cowork e Claude Code. Verificado em 2026-08-11: Cowork não tem cobertura de BAA em nenhuma configuração, e Claude Code só é elegível sob Enterprise ou API 1P com ZDR. Material do projeto que sugira uso de Cowork com dado de paciente precisa carregar esse aviso.

Há duas rotas de API 1P elegíveis, e elas são excludentes na mesma organização: HIPAA-ready API com retenção padrão, ou API regular com ZDR. Quem escolhe HIPAA-ready abre mão do ZDR e passa a conviver com a retenção padrão. A escolha entre as duas é decisão de arquitetura e precisa estar registrada, porque muda o que existe armazenado no provedor em caso de incidente ou de ordem judicial estrangeira. Quem precisa das duas coisas — API HIPAA-ready em produção e Claude Code sob ZDR — precisa de duas organizações, porque o Claude Code não é serviço elegível em organização HIPAA-ready.

O ZDR da Anthropic não bloqueia a chamada a feature não elegível. Batch API, Files API e code execution continuam disponíveis e continuam retendo pelo prazo próprio; a página de documentação diz que usá-las é sair do arranjo de ZDR para aquele dado. Em fluxo com dado de paciente, isso precisa ser barrado no código, e não confiado ao arranjo contratual. O BAA também não cobre a funcionalidade de web search.

A elegibilidade sob BAA não resolve a LGPD. Continua sendo necessário: base legal do art. 11 para dado sensível; mecanismo do art. 33 para a transferência internacional; contrato de operador; e o registro no prontuário exigido pelo art. 4º, V, da Res. CFM 2.454/2026. O caminho defensável para dado identificável é ZDR contratado antes do primeiro envio, com o estado conferido em Privacy Controls, e desidentificação antes da chamada.

**Gatilhos.**
- skill, prompt, script ou documento do projeto que instrua envio de dado de paciente em Cowork
- uso de Claude Code com conta de consumidor em fluxo clínico
- chamada a Files API, Batch API ou code execution em pipeline declarado como ZDR
- uso do Console ou do Workbench para testar prompt com dado real
- feedback 👍/👎 habilitado em interface clínica
- ausência de verificação do estado de ZDR em Privacy Controls antes do primeiro envio
- uso de Covered Model em fluxo que depende de ZDR
- chamada à API a partir do navegador (CORS) em aplicação clínica, sem proxy no backend
- conector (Google Drive, MCP) apontando para pasta com dado de paciente
- ferramenta de web search habilitada em fluxo declarado como coberto por BAA
- uso de Claude Code em organização de API HIPAA-ready, tratado como serviço elegível
- transcrição local de sessão de Cowork ou de Claude Code tratada como efêmera, sem contar os 6 anos de retenção da Compliance API

**Incerteza.** `NÃO VERIFICADO`: a data exata e os termos da mudança de política de treino para contas de consumidor anunciada em 2025 (opt-out ou opt-in). A página atual descreve o regime vigente; o histórico da mudança não foi confirmado em fonte primária.

**Relacionados.** PROV:comparativo · CFM-2454-2026:art6 · LGPD:art11 · LGPD:art33 · SEC:llm.memorizacao

---

## PROV:openai

**Ementa.** Treino, retenção, ZDR, BAA e o efeito da ordem judicial de preservação.

**Literal.**

*Privacidade em produtos corporativos e API.* https://openai.com/enterprise-privacy/ — verificado em 2026-08-11; a página declara "Updated: January 8, 2026".
> "We do not train our models on your data by default"

Abrange ChatGPT Business, Enterprise, Healthcare, Edu, Teachers e a API Platform. Exceção: opt-in explícito em mecanismos de feedback.
- ChatGPT Enterprise, Edu e Healthcare, verbatim: "Your workspace admins control how long your data is retained. Any deleted conversations are removed from our systems within 30 days, unless we are legally required to retain them."
- ChatGPT Business, verbatim: "Any deleted or unsaved conversations are removed from our systems within 30 days."
- API Platform, verbatim: "OpenAI may securely retain API inputs and outputs for up to 30 days to provide the services" e "You can also request zero data retention (ZDR) for eligible endpoints if you have a qualifying use-case".
- DPA disponível para Business, Enterprise e API. ChatGPT Edu e Teachers usam Student Data Privacy Agreement, e não DPA.
- BAA, em seção de FAQ da API Platform, verbatim: "We are able to sign Business Associate Agreements (BAA) in support of customers' compliance with [HIPAA]".

*Endpoints elegíveis a Zero Data Retention.* https://developers.openai.com/api/docs/guides/your-data — verificado em 2026-08-11.
- Elegíveis: `/v1/chat/completions`, `/v1/responses`, `/v1/images/generations`, `/v1/images/edits`, `/v1/embeddings`, `/v1/audio/transcriptions`, `/v1/audio/translations`, `/v1/audio/speech`, `/v1/realtime`, `/v1/completions`, `/v1/moderations`.
- Não elegíveis: `/v1/conversations` e `/v1/conversations/items`, `/v1/chatkit/threads`, `/v1/assistants`, `/v1/threads` (e `messages`, `runs`, `runs/steps`), `/v1/vector_stores`, `/v1/files`, `/v1/fine_tuning/jobs`, `/v1/evals`, `/v1/batches`, `/v1/videos`.
- Efeito sobre logs, verbatim: "Zero Data Retention excludes customer content from abuse monitoring logs in the same way as Modified Abuse Monitoring."
- Sem ZDR, verbatim: "abuse monitoring logs are generated for all API feature usage and retained for up to 30 days".
- Condição de acesso, verbatim: "Currently, these controls are subject to prior approval by OpenAI and acceptance of additional requirements."
- Efeito do ZDR sobre o parâmetro de armazenamento, verbatim: "When Zero Data Retention is enabled for an organization, the store parameter will always be treated as false, even if the request attempts to set the value to true."
- Web search e BAA, verbatim: "Web Search with live internet access is not HIPAA eligible and is not covered by a BAA. Web Search in offline/cache-only mode (`external_web_access: false`) is eligible to be covered by a BAA when used with an API key from a ZDR-enabled project within a ZDR organization."
- Imagens e arquivos de entrada, verbatim: "Image and file inputs are scanned for CSAM content upon submission. If the classifier detects potential CSAM content, the image will be retained for manual review, even if Zero Data Retention, Modified Abuse Monitoring, or Eyes Off is enabled."
- A página nomeia um "OpenAI Business Associate and Healthcare Addendum" e trabalha com o conceito de endpoints elegíveis a BAA.

*Ordem judicial de preservação (caso NYT).* https://openai.com/index/response-to-nyt-data-demands/ — verificado em 2026-08-11; página atualizada em 22/10/2025.
- A obrigação de retenção indefinida terminou em 26/09/2025. A página confirma que a OpenAI "no longer under a legal order to retain consumer ChatGPT and API content indefinitely".
- Afetados durante a vigência: ChatGPT Free, Plus, Pro e Team, e API sem ZDR.
- Isentos durante a vigência: ChatGPT Enterprise, ChatGPT Edu e API com ZDR.
- Residual: a OpenAI ainda deve guardar de forma segura dado limitado de usuários do período de abril a setembro de 2025, acessível apenas a equipe jurídica e de segurança restrita.
- Prática restabelecida: conversas deletadas e Temporary Chats removidas em até 30 dias; dado de API deletado em 30 dias.

**Fonte.** https://openai.com/enterprise-privacy/ · https://developers.openai.com/api/docs/guides/your-data · https://openai.com/index/response-to-nyt-data-demands/ · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Durante cerca de quatro meses de 2025, uma ordem judicial em jurisdição estrangeira se sobrepôs à política de retenção contratada, e a única configuração imune foi ZDR ou Enterprise. Para dado de paciente brasileiro, isso demonstra que "a política diz que deleta em 30 dias" é promessa contratual sujeita a processo judicial estrangeiro, não controle técnico. A mitigação estrutural é ZDR.

O ZDR é por endpoint, não por conta. Ficam fora da lista de elegíveis os endpoints de arquivo, vector store, batch, fine-tuning, evals, vídeo e a API de conversas. Um pipeline que chama `/v1/chat/completions` sob ZDR e sobe o laudo em `/v1/files` não está sob ZDR na parte que importa. Conferir o endpoint, não o plano.

**Gatilhos.**
- uso de conta ChatGPT Free, Plus, Pro ou Team com dado de paciente
- chamada à API sem ZDR contratado em fluxo com dado de paciente
- pipeline declarado como ZDR sem confirmação de que o endpoint usado está na lista de elegíveis
- ausência de DPA assinado antes do primeiro envio
- mecanismo de feedback com opt-in habilitado em interface clínica
- documento interno que apresenta a retenção de 30 dias como controle técnico
- ferramenta de web search com acesso à internet habilitada em fluxo declarado como coberto por BAA
- upload de imagem ou de arquivo de paciente em pipeline sob ZDR, sem considerar a retenção para revisão manual em caso de flag do classificador

**Incerteza.** `NÃO VERIFICADO`: os termos de BAA específicos do ChatGPT Healthcare. A página de privacidade corporativa afirma a assinatura de BAA em seção de FAQ da API Platform, e a documentação de dados da API nomeia um "OpenAI Business Associate and Healthcare Addendum" e endpoints elegíveis a BAA; não foi localizada página oficial com o texto do addendum nem com os termos do produto Healthcare.

**Relacionados.** PROV:comparativo · LGPD:art33 · LGPD:art46

---

## PROV:google

**Ementa.** Diferença entre tier gratuito e pago do Gemini, abuse monitoring e retenção no Gemini Enterprise Agent Platform (antigo Vertex AI generativo), e produtos cobertos por BAA.

**Literal.**

*Gemini API e Google AI Studio — termos adicionais.* https://ai.google.dev/gemini-api/terms — verificado em 2026-08-11; a página declara effective date de 23/03/2026.
- Unpaid Services (AI Studio e quota gratuita): o Google usa prompts e respostas "to provide, improve, and develop Google products and services and machine learning technologies".
> "To help with quality and improve our products, human reviewers may read, annotate, and process your API input and output."
> "Do not submit sensitive, confidential, or personal information to the Unpaid Services."
- Paid Services (quota paga): "Google doesn't use your prompts [...] or responses to improve our products". O processamento ocorre sob o Data Processing Addendum, na condição de operador. Prompts e respostas são logados "for a limited period of time", apenas para detecção de violação de política e conformidade legal.
- Ressalva declarada, verbatim e na íntegra: "For Paid Services, Google logs prompts and responses for a limited period of time, solely for detecting and preventing violations of the Prohibited Use Policy to maintain the safety and security of the Services, and any required legal or regulatory disclosures. This data may be stored transiently or cached in any country in which Google or its agents maintain facilities."
- Critério de enquadramento, verbatim: "Your access to Google AI Studio is a 'Paid Service' even when it is offered free of charge, as long as the account you are using to access Google AI Studio has access to a Cloud Project with an associated and active Cloud Billing account or is a Workspace enterprise account. Your access to Gemini API is a 'Paid Service' only when accessing the API through a Cloud Project associated with an active billing account."
- Exceção geográfica, verbatim: "If you're in the European Economic Area, Switzerland, or the United Kingdom, the terms under 'How Google uses Your Data' in 'Paid Services' apply to all Services, including Google AI Studio and unpaid quota in the Gemini API, even though they are offered free of charge." Não há exceção equivalente para o Brasil.

*Gemini Enterprise Agent Platform — abuse monitoring.* https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/abuse-monitoring — verificado em 2026-08-11; a página declara "Last updated 2026-08-07 UTC".
- Dado de abuse monitoring armazenado por até 90 dias, na mesma região ou multi-região do projeto, para prompts sinalizados por classificador.
> "Authorized Google employees may assess the flagged prompts"
- Isenção por padrão, verbatim: "Customers in scope: Only customers whose use of Google Cloud is governed by the Google Cloud Platform Terms of Service. This means that customers with a Google Cloud Master Agreement are exempt from prompt logging for this abuse monitoring by default."
- Isenção por formulário, verbatim: "Customer opt-out: Customers may request for an exception by filling out this form. If approved, Google won't store any prompts associated with the approved Google Cloud account."
- Regime Advanced AI, verbatim: "As outlined in the Advanced AI Safety Addendum, Google Cloud has implemented a more rigorous abuse monitoring system for models designated as 'Advanced AI'. Prompt and response logging: All prompts and responses will be logged and securely stored for up to 30 days for the sole purpose of monitoring for abuse. [...] It may not be possible to opt-out of prompt-response logging when using some Advanced AI features."
- Modelos em escopo de Advanced AI, lista da página: Claude Mythos, todas as versões; Claude Fable, todas as versões; Claude Sonnet ≥ 5 e Claude Opus ≥ 4.7 quando usados em casos de alto risco de uso dual ou de uso proibido cobertos pelo Cyber Verification Program da Anthropic. Verbatim: "Consent to the Advanced AI Safety Addendum is required once per project before Advanced AI models can be enabled in that project."
- Chaves gerenciadas pelo cliente, verbatim, nos dois regimes: "Prompt logs for the purposes of abuse monitoring are not encrypted by Customer-managed encryption keys (CMEK)."
- Explicitamente não usado para treino nem para fine-tuning.

*Gemini Enterprise Agent Platform — data governance e ZDR.* https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention — verificado em 2026-08-11; a página declara "Last updated 2026-08-07 UTC". As URLs `cloud.google.com/vertex-ai/generative-ai/docs/data-governance` e a versão em `docs.cloud.google.com` retornam HTTP 200 e redirecionam para esta página.
- Treino, verbatim: "As outlined in 'Training Restriction' in the Service Terms section of the Service Specific Terms, Google won't use your data to train or fine-tune any AI/ML models without your prior permission or instruction. This applies to all managed models on Gemini Enterprise Agent Platform, including GA and pre-GA models."
- Cache, verbatim: "By default, Google's published Gemini models cache Customer Data (inputs, outputs, and derived data) in-memory to reduce latency [...] is stored only in-memory (not at-rest), is isolated at the project level, and has a 24-hour TTL". O cache pode ser desligado por projeto.
- Interactions API, verbatim: "When using the Interactions API with `store = true`, Google stores user data (such as prompts, responses, and conversation state) [...] If you do not specify a value for `store`, it defaults to `true` for all models. To achieve zero data retention, explicitly set `store = false`."
- Grounding: com Google Search, logs por até 3 dias, e "There is no way to disable the storage of this information"; com Google Maps, prompts, contexto e saída por 30 dias, também sem opção de desativar.
- Request-response logging: desabilitado por padrão; se habilitado, grava em tabela do BigQuery.
- Limite declarado do ZDR, verbatim: "Zero data retention may not be possible when using some Advanced AI features."

*Mudança de nome do produto.* A documentação de IA generativa do Vertex AI foi migrada para "Gemini Enterprise Agent Platform". A lista de Covered Products do BAA traz "Gemini Enterprise Agent Platform" e "Generative AI on Gemini Enterprise Agent Platform", e não traz "Vertex AI" como produto — apenas "Vertex AI Workbench instances".

*HIPAA e BAA no Google Cloud.* https://cloud.google.com/security/compliance/hipaa — a página declara "Last updated 2026-08-11 UTC"; verificada em 2026-08-11.
- "Google will enter into Business Associate Agreements with customers as necessary under HIPAA". Execução via https://support.google.com/cloud/answer/6329727.
- Ressalva declarada: não existe certificação de HIPAA reconhecida pelo HHS; a conformidade é responsabilidade compartilhada.
- Produtos de IA relevantes na lista de Covered Products: Vertex AI Workbench instances; AI Platform Training and Prediction; Gemini Code Assist; Gemini Enterprise; Gemini Enterprise Agent Platform; Generative AI on Gemini Enterprise Agent Platform; Gemini in BigQuery; Gemini in Colab Enterprise; Gemini Notebook Enterprise. Também constam Cloud Healthcare API, Healthcare Data Engine e Cloud KMS.
- A lista de produtos cobertos é normativa para o BAA e muda: apenas o que está na lista está coberto.

**Fonte.** https://ai.google.dev/gemini-api/terms · https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/abuse-monitoring · https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention · https://cloud.google.com/security/compliance/hipaa · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O tier gratuito do Google AI Studio usa o conteúdo para desenvolvimento de produtos e submete a revisão humana, com aviso literal na página de termos. Um teste "para ver se funciona" com evolução clínica no tier gratuito é envio de dado sensível a revisão humana. A separação entre Unpaid e Paid não é a interface: os próprios termos a definem pela vinculação da conta ou do projeto a uma conta de faturamento ativa. Verificar a vinculação. O usuário no EEE, na Suíça e no Reino Unido cai no regime pago mesmo no gratuito; o usuário no Brasil, não.

Nos Paid Services, a menção a revisores humanos aparece só na seção de Unpaid Services. A leitura de que não há revisão humana para anotação no tier pago é inferência nossa, por contraste entre as duas seções, e não afirmação dos termos.

O abuse monitoring tem duas rotas de isenção: cliente com Google Cloud Master Agreement já é isento por padrão; os demais dependem de formulário aprovado. Verificar qual contrato rege a conta antes de preencher formulário.

O nome do produto mudou. A documentação de IA generativa e a lista de Covered Products dizem "Gemini Enterprise Agent Platform"; "Vertex AI" aparece na lista apenas como "Vertex AI Workbench instances". Auditoria que procura por "Vertex AI" no contrato ou no código pode não encontrar o serviço efetivamente contratado. Procurar pelos dois nomes.

A retenção padrão do Google é maior do que a linha de 90 dias sugere. Três camadas se somam: prompts sinalizados por classificador, até 90 dias; modelos designados como Advanced AI, todos os prompts e respostas por até 30 dias, possivelmente sem opt-out; e a Interactions API, que armazena por padrão porque `store` assume `true` quando não é declarado. Em fluxo com dado de paciente, declarar `store = false` de forma explícita e conferir se o modelo escolhido é Advanced AI, porque nesse caso o ZDR pode não ser alcançável.

A ressalva de armazenamento "transiently or cached in any country" é relevante para o art. 33 da LGPD. Ela vale para os logs de prompt e resposta mantidos para fins de política, não para o dado tratado em geral; citar a frase inteira, com o antecedente.

**Gatilhos.**
- chave de API do Google AI Studio em código que processa dado de paciente
- integração com Gemini sem projeto de faturamento vinculado (quota gratuita)
- uso do Gemini Enterprise Agent Platform com dado de paciente sem isenção de abuse monitoring, por Master Agreement ou por formulário aprovado
- chamada à Interactions API sem `store = false` explícito em fluxo com dado de paciente
- uso de modelo designado como Advanced AI em fluxo que depende de retenção zero
- grounding com Google Search ou Google Maps em prompt que contém dado de paciente
- request-response logging habilitado para BigQuery em projeto com dado de paciente
- uso de produto Google fora da lista de Covered Products em fluxo declarado como coberto por BAA
- contrato ou documento interno que nomeia "Vertex AI" como serviço coberto por BAA para IA generativa
- ausência de definição de região do projeto em serviço com dado de paciente

**Relacionados.** PROV:comparativo · LGPD:art33 · CFM-2454-2026:anexoI.XVI

---

## PROV:comparativo

**Ementa.** Quadro comparativo dos três provedores, estado em 2026-08-11.

**Literal.** Item derivado. Cada célula remete ao item de origem — `PROV:anthropic`, `PROV:openai`, `PROV:google` — onde estão a URL oficial, a data de verificação e a data declarada de atualização da página.

| | Anthropic | OpenAI | Google |
|---|---|---|---|
| Treino em dado comercial por padrão | Não (API, Team, Enterprise) | Não (Business, Enterprise, Healthcare, Edu, API) | Não em Paid Services; sim em Unpaid Services (AI Studio gratuito), com revisão humana |
| Retenção padrão na API | ver tabela em PROV:anthropic; ZDR disponível | até 30 dias; ZDR em endpoints elegíveis | prompt sinalizado por até 90 dias; Advanced AI loga todos os prompts e respostas por até 30 dias; Interactions API armazena por padrão (`store` = `true`) |
| ZDR | Sim, por organização, com exclusões extensas | Sim, em lista fechada de endpoints elegíveis | Sim, no Gemini Enterprise Agent Platform, com `store = false` explícito; pode não ser possível em recursos Advanced AI |
| DPA | Sim, produtos comerciais | Sim (Business, Enterprise, API) | Sim, para Paid Services |
| BAA | Sim — Chat via Enterprise, HIPAA-ready API com retenção padrão, API 1P regular com ZDR, Claude Code com ZDR. Cowork: não, em nenhuma configuração | Sim — API Platform | Sim — lista de Covered Products, que inclui Gemini Enterprise Agent Platform e Vertex AI Workbench instances |
| Conta de consumidor com dado de paciente | Vedada | Vedada | Vedada (AI Studio gratuito: uso para desenvolvimento e revisão humana) |

**Fonte.** item derivado; as três páginas de origem foram abertas e conferidas nesta sessão — https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to · https://developers.openai.com/api/docs/guides/your-data · https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** bloqueante quanto ao uso de conta de consumidor com dado identificável de paciente

**Aplicação.** A vedação de conta de consumidor não vem do provedor: vem do art. 6º, §3º, da Res. CFM 2.454/2026, que proíbe ao médico usar sistema que não garanta padrões mínimos de segurança compatíveis com dados sensíveis, e do art. 46 da LGPD. As políticas dos três provedores apenas confirmam que a configuração de consumidor não oferece esses padrões: sem BAA, sem DPA, com retenção declarada de 30 dias ou mais, e com possibilidade de uso em treino após opt-in.

A leitura correta do quadro é por configuração, não por fornecedor. O mesmo provedor tem configurações que aceitam dado de paciente e configurações que não aceitam. A verificação é por produto, por plano e por endpoint.

**Gatilhos.**
- conta pessoal ou de consumidor de qualquer provedor em fluxo clínico
- chave de API de tier gratuito em código que processa dado de paciente
- ausência de DPA ou de contrato de operador assinado antes do primeiro envio
- ausência de registro de qual configuração (produto, plano, endpoint, região) trata dado de paciente
- documentação interna que trata "temos BAA com o fornecedor" como cobertura de todos os produtos daquele fornecedor
- ausência de base legal do art. 11 e de mecanismo do art. 33 registrados, ainda que haja BAA

**Relacionados.** CFM-2454-2026:art6 · LGPD:art11 · LGPD:art33 · LGPD:art46

---

## PROV:erros-comuns

**Ementa.** Erros recorrentes na avaliação de política de provedor.

**Literal.** Item derivado. Cada linha remete ao item de origem, onde estão a citação e a URL.

**Fonte.** item derivado; as páginas de origem foram abertas e conferidas nesta sessão — https://support.claude.com/en/articles/15455031-covered-models-under-a-business-associate-agreement-baa · https://openai.com/index/response-to-nyt-data-demands/ · https://ai.google.dev/gemini-api/terms · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.**

1. Usar conta pessoal Pro ou Plus com dado de paciente por ser plano pago. Pagar pelo plano não contrata BAA, DPA nem ZDR. Origem: `PROV:anthropic`, `PROV:openai`.
2. Testar no tier gratuito do Google AI Studio antes de migrar para o plano pago. Os termos informam que o conteúdo é usado para desenvolvimento e que revisores humanos podem lê-lo. Origem: `PROV:google`.
3. Assumir que ZDR está ativo sem conferir em Privacy Controls, e sem saber que Files API, batch processing, code execution, Console e Workbench estão fora do ZDR. Na OpenAI, o ZDR é por endpoint, e arquivos, vector stores, batches, fine-tuning, evals e a API de conversas não são elegíveis. No Google, a Interactions API armazena por padrão se `store` não for declarado. Origem: `PROV:anthropic`, `PROV:openai`, `PROV:google`.
4. Assumir que um BAA assinado com o fornecedor cobre todos os produtos do fornecedor. As três políticas trabalham com lista de serviços ou de produtos elegíveis. Origem: `PROV:anthropic`, `PROV:google`.
5. Tratar "deletamos em 30 dias" como controle técnico. A ordem judicial no caso OpenAI × NYT, vigente de abril a setembro de 2025, suspendeu a deleção para todas as configurações exceto ZDR e Enterprise. Origem: `PROV:openai`.
6. Ler a política uma vez e não reverificar. As páginas consultadas em 2026-08-11 declaram atualização em 08/01/2026, 16/03/2026, 09/06/2026, 01/07/2026, 07/08/2026 e 11/08/2026. A página de HIPAA do Google mudou de data no intervalo entre dois levantamentos desta ficha. Origem: `PROV:anthropic`, `PROV:openai`, `PROV:google`.
7. Tratar BAA como suficiente para a LGPD. BAA é regime dos Estados Unidos, não cria base legal do art. 11 nem mecanismo de transferência do art. 33.
8. Usar Cowork com dado de paciente por ser produto do mesmo fornecedor que tem BAA. Verificado em 2026-08-11: "Cowork is not an Eligible Service under Anthropic's BAA in any configuration". Origem: `PROV:anthropic`.

**Gatilhos.**
- avaliação de fornecedor registrada sem data de verificação da política
- decisão de arquitetura fundamentada em política de provedor sem URL e sem data
- material de treinamento interno que recomenda superfície de produto sem verificar elegibilidade
- ausência de rotina de reverificação das páginas de política

**Relacionados.** PROV:comparativo · CFM-2454-2026:art6 · CFM-2454-2026:art3

---

## Itens não verificados nesta ficha

Estado em 2026-08-11. Reverificar junto com as URLs.

| Item | Estado |
|---|---|
| Data e termos da mudança de política de treino para contas de consumidor da Anthropic anunciada em 2025 | NÃO VERIFICADO |
| Termos de BAA específicos do ChatGPT Healthcare | NÃO VERIFICADO; a assinatura de BAA consta apenas em FAQ da API Platform |
