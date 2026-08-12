---
tema: uso clínico de LLM e de IA no atendimento
aplica-se-a: médico assistente, responsável técnico de clínica
fichas: [01, 02, 04, 07]
verificado: 2026-08-11
---

# Uso clínico de LLM no atendimento

Diretrizes sobre o que o médico pode e não pode fazer ao usar LLM ou qualquer sistema de IA no cuidado de paciente. Escrito para o médico assistente e para o responsável técnico do serviço. O que depende de código ou de configuração é exigência a fazer à TI ou ao fornecedor; o critério técnico está em `desenvolvimento:D3`.

> Parte destas diretrizes decorre da Res. CFM 2.454/2026, em vigor a partir de 26/08/2026. Até essa data, o regime é o Código de Ética Médica, as Res. CFM 1.821/2007 e 2.314/2022 e a Lei 13.709/2018.

## D1 — Mantenha a decisão clínica com o médico

Use a IA como apoio. A decisão sobre diagnóstico, prognóstico, prescrição e qualquer outro ato médico é do médico, que acolhe ou rejeita a sugestão conforme seu julgamento. Não existe fluxo em que a saída do sistema vira conduta sem confirmação humana. A responsabilidade pelo ato permanece pessoal e não se transfere ao fornecedor por contrato ou por aviso de isenção.

**Leitura adotada.** Leitura nossa, extensiva: a vedação alcança sistemas. O ponto não está pacificado. A partir de 26/08/2026 o art. 15, parágrafo único, e o art. 18, §2º da Res. 2.454/2026 sustentam a regra sem depender desta leitura.

**Base.** CFM-2454-2026:art15 · CFM-2454-2026:art18 · CFM-2454-2026:art4 · CEM:art2 · CEM:art1

**Verificar.**
- existe etapa humana obrigatória entre a saída do sistema e o ato clínico, exigência a fazer à TI ou ao fornecedor
- a interface permite rejeitar e editar a sugestão
- nenhum campo clínico é gravado somente por preenchimento automático
- há registro de quem confirmou cada saída aplicada ao caso

**Escalar se.** A interface não permite rejeitar ou editar a sugestão, ou o fluxo aplica a saída sem confirmação.

## D2 — Não delegue à IA a comunicação sem mediação humana

Não delegue à IA a comunicação de diagnóstico, prognóstico ou decisão terapêutica sem mediação humana. Conteúdo gerado por IA para o paciente só sai depois de revisão e liberação médica registradas. Isso alcança o envio automatizado de resultado de exame e de laudo, e a resposta gerada a mensagem clínica de paciente.

**Base.** CFM-2454-2026:art5 · CEM:art37 · CEM:art10

**Verificar.**
- nenhum canal ao paciente publica resultado ou laudo sem liberação médica registrada
- chatbot voltado ao paciente não retorna conduta, dose nem indicação terapêutica
- respostas clínicas a mensagens de paciente passam por revisão antes do envio
- o médico responsável do serviço participa do fluxo de fato, e não apenas no cadastro

**Escalar se.** O serviço entrega ao paciente, de forma automatizada e com apoio de IA, resultado ou laudo antes da liberação médica.

## D3 — Registre o uso de IA no prontuário

> Vale a partir de 26/08/2026.

Todo uso de IA como apoio à decisão médica entra no prontuário do paciente. O registro traz ferramenta, versão, finalidade e confirmação de que houve revisão médica. O dever não depende de a IA ter sido determinante para a conduta.

**Base.** CFM-2454-2026:art4 · CEM:art87

**Verificar.**
- o sistema tem campo próprio para esse registro
- a versão do modelo é persistida junto com a saída, exigência a fazer à TI ou ao fornecedor
- há etapa de revisão antes de o texto virar registro clínico
- cada avaliação registrada tem data, hora, assinatura e número de CRM

**Escalar se.** O sistema não grava a versão do modelo usada em cada chamada.

## D4 — Informe o paciente e ofereça caminho alternativo funcional

> Vale a partir de 26/08/2026.

Informe o paciente, em linguagem acessível, sempre que usar IA no cuidado dele. Explique que o sistema apoia o médico e não substitui a decisão humana. Respeite a recusa. O serviço precisa conseguir atender o paciente que recusa a IA. Em telemedicina, o consentimento de uso de IA é separado do consentimento de atendimento e de transmissão de imagens e dados, que já é exigido desde a Res. 2.314/2022.

**Leitura adotada.** Leitura nossa, conservadora: informar sempre. O ponto não está pacificado.

**Base.** CFM-2454-2026:art5 · CFM-2454-2026:art11 · CFM-2314-2022:art15

**Verificar.**
- o cadastro tem campo de consentimento e de recusa do uso de IA, com data, hora e versão do texto
- a recusa desliga a IA para aquele paciente, e o desligamento é efetivo no fluxo
- o termo de telemedicina e o termo de uso de IA podem ser aceitos em separado
- o registro do consentimento fica no prontuário, e não em sistema de agendamento ou de marketing

**Escalar se.** O serviço não consegue prestar o atendimento sem a ferramenta de IA.

## D5 — Use apenas sistema com segurança compatível com dado sensível

Está vedado usar sistema de IA que não garanta padrões mínimos de segurança da informação compatíveis com dado pessoal sensível. Conta pessoal, gratuita ou de consumidor não atende ao requisito em fluxo clínico. Exija contrato de tratamento de dados que vincule o operador às instruções do controlador e delimite finalidade, retenção e subprocessadores. Em telemedicina, o contrato reparte a guarda com a contratada por cláusula expressa. Verifique a configuração padrão da conta: proteção máxima precisa ser o estado de fábrica, sem depender de ação do usuário.

**Base.** CFM-2454-2026:art6 · CFM-2454-2026:anexoI.XV-XVI · LGPD:art39 · LGPD:art46 · CFM-2314-2022:art3 · CFM-2314-2022:art3§7 · CEM:art18

**Verificar.**
- existe contrato assinado com o provedor, e não apenas termos aceitos por clique
- o uso do conteúdo para treinamento e para melhoria do serviço está desligado, com evidência documental
- há criptografia de dado sensível em repouso e em trânsito
- em telemedicina, o registro do atendimento atende ao NGS2 e o padrão de assinatura invocado tem base legal identificada
- a cadeia de subprocessadores do provedor está documentada

**Escalar se.** O provedor de IA não tem sede no Brasil e o fluxo é de telemedicina.

## D6 — Minimize e desidentifique antes de enviar

Envie o mínimo necessário para a finalidade. Remova identificadores antes da chamada ao sistema de IA. A desidentificação precisa cobrir quase-identificadores: a combinação de idade, data, serviço e quadro clínico reidentifica paciente mesmo sem nome e CPF. Enviar conteúdo de prontuário a serviço externo é liberação de cópia e depende de autorização escrita do paciente, de ordem judicial ou de defesa própria.

**Leitura adotada.** Leitura nossa, conservadora: enviar a sistema de terceiro é revelação. O ponto não está pacificado. Para liberação de cópia de prontuário, o art. 89 sustenta a regra sem depender desta leitura.

**Base.** CFM-2454-2026:art6 · CEM:art73 · CEM:art89 · CEM:art75

**Verificar.**
- existe etapa de desidentificação antes do envio, e ela roda em todo o fluxo
- nenhum payload carrega nome, CPF, RG, número de prontuário ou data de nascimento
- há teste de reidentificação sobre amostra das saídas desidentificadas
- o uso de dado identificável, quando ocorre, tem consentimento escrito específico arquivado

**Escalar se.** A finalidade clínica exige enviar dado identificável e não há consentimento escrito específico do paciente.

## D7 — Não exponha caso identificável fora do atendimento

Não publique nem divulgue caso clínico que torne o paciente reconhecível. Em anúncio profissional, mídia social, fórum, comunidade de usuários, prompt compartilhado publicamente e demonstração pública, a vedação é absoluta: o consentimento do paciente não a afasta e a única via é a não reconhecibilidade. Fora da divulgação pública, em material de treinamento interno, repositório privado, documentação e conjunto de teste, a exposição de caso reconhecível é revelação de fato sigiloso e exige uma das três exceções do sigilo, na prática o consentimento escrito, além da base da LGPD. Remover só identificadores diretos não torna o caso não reconhecível.

**Base.** CEM:art75 · CEM:art73

**Verificar.**
- prompts de exemplo e documentação usam caso sintético
- material de treinamento e de divulgação não traz captura de prontuário real
- conjuntos de teste e de demonstração são sintéticos ou passaram por desidentificação avaliada
- há teste de reidentificação documentado antes de o material sair do serviço

**Escalar se.** Não está pacificado se prompt desidentificado é dado pessoal para efeito da base legal.

## D8 — Oriente a equipe e mantenha política interna escrita

O médico responde por orientar auxiliares, residentes e estagiários quanto ao sigilo, e por zelar para que o sigilo seja mantido. A orientação precisa deixar evidência. A política interna de uso de IA cobre: ferramentas autorizadas e proibidas; o que pode e o que não pode ser colado em ferramenta de IA; regra de desidentificação; registro no prontuário; consentimento e recusa do paciente; canal para reportar falha; controle de acesso; e responsabilidades do responsável técnico.

**Base.** CEM:art78 · CFM-2454-2026:art14 · CFM-2454-2026:art7 · CFM-2314-2022:art18

**Verificar.**
- existe política interna escrita, datada e com versão
- há registro de treinamento da equipe, com lista de presença ou aceite nominal
- estações com acesso a prontuário têm controle de saída de dados e bloqueio de ferramentas não autorizadas
- há inventário dos destinos externos de dados clínicos
- instituição com sistema próprio de IA tem Comissão de IA e Telemedicina sob coordenação médica e subordinada à diretoria técnica

**Escalar se.** A equipe usa ferramenta de IA de consumo em máquina com acesso a prontuário e não há controle técnico de saída de dados.

## D9 — Use apenas sistema conforme, e registre o motivo da recusa

> Vale a partir de 26/08/2026.

Use apenas sistema de IA que atenda às normas éticas, técnicas, legais e regulatórias vigentes no país. Esse é o dever. Como direito, recuse sistema sem validação científica adequada, sem certificação regulatória pertinente ou que contrarie princípios éticos, técnicos e legais da medicina, e exija do fornecedor informação clara sobre funcionamento, finalidades, limitações, riscos e grau de evidência. Não siga sugestão de IA de forma automática. Desligue a ferramenta quando julgar inadequada para a situação, e registre a decisão. A proteção contra penalização depende de atuação conforme os preceitos técnicos e éticos.

**Base.** CFM-2454-2026:art4 · CFM-2454-2026:art3 · CFM-2454-2026:art18 · CFM-2454-2026:art19

**Verificar.**
- o serviço mantém a documentação de limitações e de evidência entregue pelo fornecedor
- há registro do motivo clínico quando o médico rejeita a sugestão
- nenhuma meta ou métrica de desempenho cobra aderência às sugestões da IA
- o médico pode desligar a ferramenta por atendimento

**Escalar se.** A instituição cobra aderência às sugestões da IA como métrica de desempenho do médico.

## D10 — Trate gravação de consulta como transmissão de dado sigiloso

Gravação de áudio, transcrição e escriba de IA processam conteúdo sigiloso da consulta. Em telemedicina, o consentimento é explícito e informa que as informações podem ser compartilhadas e que o paciente pode negar permissão, salvo em emergência médica. Fora da telemedicina, a base é o sigilo profissional e o consentimento é por escrito. Em qualquer caso, o consentimento é separado do de atendimento e do de uso de IA, e fica registrado no prontuário, com data, hora e versão do texto. O áudio bruto tem prazo de retenção próprio, definido pelo serviço. A transcrição revisada que virou nota clínica segue o regime do prontuário, por `custodia:D13`.

**Base.** CFM-2314-2022:art15 · CEM:art73 · CFM-2454-2026:art5 · CFM-2454-2026:art6

**Verificar.**
- a recusa da gravação é possível e o atendimento continua
- o fluxo trata a hipótese de emergência médica de forma explícita
- o áudio bruto tem prazo declarado, e a transcrição integrada ao prontuário não é expurgada por essa rotina
- o provedor de transcrição está coberto pelo contrato de tratamento de dados

**Escalar se.** A Res. CFM 2.454/2026 não classifica gravação, transcrição nem escriba de IA em nenhum nível de risco, e a classificação sobe para o responsável técnico.

## D11 — Assine o documento clínico depois de revisar o conteúdo

Documento clínico gerado com apoio de IA é assinado pelo médico depois de revisado. A assinatura incide sobre conteúdo que já existe. Está vedado assinar em branco e autorizar previamente a emissão de documento cujo conteúdo será gerado depois. Cada documento traz identificação do médico, CRM e jurisdição. Em emissão a distância, o prontuário registra nome, CRM, endereço profissional, dados e local do paciente, data e hora, assinatura com certificação digital e a indicação de que o documento foi emitido em telemedicina.

**Base.** CEM:art11 · CEM:art87 · CFM-2314-2022:art13.d

**Verificar.**
- a assinatura é aplicada após a revisão, e a ordem fica registrada
- não há emissão em lote com autorização única de assinatura
- o certificado exige autenticação do titular a cada uso
- o prontuário tem campo que marca a emissão em modalidade de telemedicina

**Escalar se.** O certificado de assinatura está acessível a processo automatizado sem autenticação do titular.

## D12 — Guarde a trilha que comprova o uso diligente

A proteção do médico contra responsabilização por falha do sistema depende de prova. Guarde prompt, resposta, versão do modelo, identificação de quem revisou e o resultado da revisão. Essa trilha é a classe B de `custodia:D13`: fica em repositório próprio sob controle do serviço, com prazo declarado, e não vive no provedor. O conteúdo de apoio que influenciou a decisão é registro clínico, integra o prontuário e segue a guarda do prontuário, com o direito de acesso do paciente e a requisição do CRM. Log de aplicação e telemetria não recebem conteúdo de paciente.

**Base.** CEM:art6 · CFM-2454-2026:art3 · CEM:art87 · CEM:art88 · CEM:art90 · CEM:art17

**Verificar.**
- prompt e resposta são persistidos em repositório sob controle do serviço, exigência a fazer à TI ou ao fornecedor
- a trilha tem prazo de retenção declarado, e ele não é o prazo do provedor
- a exportação integral do prontuário inclui o conteúdo de apoio à decisão
- existe rotina para responder a requisição do CRM em prazo

**Escalar se.** A retenção da trilha depende do provedor e o serviço não consegue manter cópia própria.

## D13 — Reporte falha e reavalie o sistema em uso

> Vale a partir de 26/08/2026.

Comunique às instâncias competentes falhas, riscos relevantes e usos inadequados de IA que possam comprometer a segurança do paciente ou a qualidade da assistência. Esse dever é do médico, e o serviço mantém canal e registro para isso. Quem desenvolve ou contrata o sistema, médico ou instituição, monitora o desempenho das saídas com resultados estratificados por grupo populacional e corrige viés detectado. Em caso grave em que o viés não possa ser eliminado, o sistema é descontinuado. A avaliação e a reavaliação do nível de risco e a auditoria especializada são da instituição médica.

**Base.** CFM-2454-2026:art7 · CFM-2454-2026:art12 · CFM-2454-2026:art14 · CFM-2454-2026:art9 · CFM-2454-2026:anexoII · CFM-2454-2026:anexoIII.II · CFM-2314-2022:art18

**Verificar.**
- existe canal interno de reporte de falha, com registro e prazo de tratamento
- há data da última reavaliação de risco de cada sistema em uso
- atualização de modelo dispara reavaliação registrada
- há métrica de desempenho estratificada por grupo populacional
- ambiente de teste e de homologação não usa dado real de paciente

**Escalar se.** O viés grave exige descontinuação e a resolução não disciplina o procedimento.
