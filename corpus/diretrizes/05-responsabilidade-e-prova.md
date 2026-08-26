---
tema: responsabilidade e prova de diligência no uso de IA com dado de paciente
aplica-se-a: médico assistente, responsável técnico, jurídico interno
fichas: [01, 02, 03, 06, 07, 08, 09, 10, 11]
verificado: 2026-08-11
---

# Responsabilidade e prova

Quem responde pelo uso de IA sobre dado de paciente, em quais esferas, e o que precisa estar registrado para provar diligência.

> Parte destas diretrizes decorre da Res. CFM 2.454/2026, **em vigor desde 26/08/2026**. Elas são exigência corrente. Cada diretriz traz a resolução no campo `Base`, ao lado das demais normas que a sustentam.

## D1 — Trate as quatro camadas de responsabilidade como simultâneas

Ética, civil, penal e administrativa incidem ao mesmo tempo sobre o mesmo fato. As sanções se somam: a ética não substitui a civil, a penal nem a administrativa, e o processo de uma não suspende o da outra. Planeje a conformidade para a camada mais exigente de cada tema.

**Base.** CFM-2454-2026:art8 · LGPD:art52§2-§7 · CP:art154 · CC:art927

**Verificar.**
- o mapa de risco do serviço lista as quatro esferas por fluxo, e não só a LGPD
- há responsável nomeado para cada esfera: diretor técnico na ética, jurídico na civil e na penal, encarregado na administrativa
- a política interna não trata sanção da ANPD como desfecho único

**Escalar se.** O caso depender do efeito de uma decisão criminal sobre as demais esferas: esse efeito não está no corpus.

## D2 — Trate a responsabilidade pelo ato médico como intransferível por contrato

A decisão clínica é do médico: ver `uso-clinico:D1`. No campo ético-profissional o médico permanece responsável pelo ato praticado com apoio de IA, e o CRM a apura. Contrato com fornecedor, cláusula de limitação e certificação de produto não a afastam, e a sanção ética corre sem prejuízo da civil e da penal. Perante o paciente nenhum contrato transfere responsabilidade; entre os contratantes ele define apenas quem paga ao final, por regresso.

**Base.** CFM-2454-2026:art7 · CFM-2454-2026:art8 · CFM-2454-2026:art15

**Verificar.**
- o contrato com o fornecedor não é apresentado internamente como transferência de responsabilidade clínica
- o contrato traz cláusula de regresso, e ela não é confundida com exclusão de responsabilidade perante o paciente

## D3 — Reavalie o regime civil quando o atendimento passa a ser prestado por pessoa jurídica

A apuração por culpa alcança a responsabilidade pessoal do profissional liberal. Não alcança a pessoa jurídica. Havendo relação de consumo, clínica, hospital e laboratório respondem como fornecedores de serviço, sem culpa, pelo que é do estabelecimento — acesso, contrato com o fornecedor, retenção, log. Respondem também sem culpa pelos atos de empregados, residentes, secretaria e TI terceirizado.

**Base.** CDC:art14§4 · CDC:art14 · CC:art932 · CC:art933 · LGPD:art45

**Verificar.**
- o contrato de prestação define quem é o fornecedor perante o paciente
- a pessoa jurídica não invoca internamente a exceção do profissional liberal como cobertura do serviço
- existe política interna de uso de IA aplicável a empregados, residentes e prestadores
- o acesso a dado de paciente por dispositivo pessoal está sob gestão

**Escalar se.** O atendimento for pelo SUS ou gratuito: não há relação de consumo e a base da responsabilidade do Estado não está no corpus. A cisão entre falha do estabelecimento e falha técnica do médico está em fonte secundária e não fundamenta.

## D4 — Trate a clínica como acionada e o médico como destinatário do regresso

O paciente pode acionar apenas a pessoa jurídica. A responsabilidade entre autor e empregador é solidária, e quem paga tem direito de regresso contra o causador do dano. Há solidariedade sobreposta entre controlador e operador. O médico empregado não fica protegido pelo fato de a clínica pagar.

**Base.** CC:art927 · CC:art932 · CC:art933 · LGPD:art42

**Verificar.**
- contrato de trabalho ou de prestação com cláusula de responsabilidade e de regresso
- contrato que identifique controlador e operador em cada fluxo com LLM
- fornecedor de TI com acesso à base clínica tem contrato de operador assinado

## D5 — Produza a prova de diligência antes do incidente

As excludentes de responsabilidade civil e os atenuantes administrativos só valem se o agente os provar, e o rol das excludentes é taxativo. A inversão do ônus da prova em favor do titular é faculdade do juiz, condicionada a verossimilhança, hipossuficiência ou onerosidade excessiva. Trabalhe como se fosse ocorrer. Prova de diligência é documento datado e anterior ao fato, não narrativa posterior.

**Base.** LGPD:art42 · LGPD:art43 · ANPD-4-2023:art13 · LGPD:art37 · LGPD:art38

**Verificar.**
- registro das operações de tratamento existe, com data e versão
- relatório de impacto dos fluxos com dado sensível, elaborado por antecipação: a lei o exige mediante determinação da autoridade, e tê-lo pronto conta como governança documentada
- documentação de segurança obtida do fornecedor, arquivada com a data da avaliação
- decisões de conformidade registradas com data, autor e fundamento

**Escalar se.** A tese de responsabilidade objetiva por atividade de risco aplicada a IA for invocada: é doutrina, sem texto expresso e sem precedente verificado.

## D6 — Use o registro do uso de IA no prontuário como prova de supervisão

O registro do uso de IA no prontuário é `uso-clinico:D3`. Aqui ele vale como prova: sem ele não se demonstra que houve revisão médica antes do ato. O conteúdo produzido pela IA que integrou o prontuário é classe A de retenção e segue o regime de guarda do prontuário.

**Base.** CFM-2454-2026:art4 · CFM-1821-2007:art7

**Verificar.**
- a revisão médica é identificável por pessoa, data e hora
- o conteúdo produzido pela IA que integra o prontuário é exportado e guardado sob controle do serviço

## D7 — Separe as três classes de retenção e escreva o prazo de cada uma

A trilha que comprova o uso diligente é `uso-clinico:D12`. Separe três destinos. Classe A, conteúdo revisado que integrou o prontuário: regime de guarda do prontuário, sem expurgo por rotina de aplicação. Classe B, trilha de auditoria — data e hora, usuário, finalidade, ferramenta e versão do modelo, base legal, desidentificação e confirmação da revisão humana: repositório do serviço, com prazo declarado. Classe C, log de aplicação e telemetria: metadado apenas, sem conteúdo de paciente e sem corpo de requisição, com retenção curta. Registro de incidente tem guarda mínima de cinco anos, inclusive quando não comunicado.

**Base.** CFM-2454-2026:art3 · CFM-2454-2026:art9 · LGPD:art37 · ANPD-15-2024:art10 · CFM-1821-2007:art7 · CFM-1821-2007:art8 · SEC:segredos.logs

**Verificar.**
- o log identifica pessoa, e não conta de serviço compartilhada
- o log permite contar titulares afetados em caso de incidente
- o log de aplicação registra quem, quando, qual modelo e qual finalidade, e não o conteúdo do payload enviado ao modelo
- cada classe tem prazo escrito e rotina de expurgo compatível com ele

## D8 — Trate a revelação de dado de paciente a terceiro como conduta criminal

Revelar segredo obtido em razão da profissão é crime. Basta que uma pessoa não autorizada tome ciência. Não é preciso divulgação a público indeterminado, nem dano consumado. Colar evolução clínica identificada em ferramenta de terceiro sem contrato de tratamento de dados, ou usar conta pessoal ou gratuita em fluxo clínico, é o cenário direto. O mesmo alcança quem acessa a base em razão de ofício, inclusive equipe técnica e desenvolvedor.

> Leitura nossa, conservadora: enviar a sistema de terceiro é revelação. O ponto não está pacificado.

**Base.** CP:art154 · CFM-2454-2026:art6 · CEM:art73

**Verificar.**
- nenhuma chamada a LLM em fluxo clínico parte de conta pessoal ou gratuita
- todo provedor em uso tem contrato de tratamento de dados assinado
- há etapa de desidentificação antes do envio, ou base legal registrada para o envio identificado
- a configuração do provedor não usa os inputs para treinamento
- desenvolvedor e analista não acessam base de prontuário em ambiente de desenvolvimento

**Escalar se.** A defesa depender de justa causa por consentimento do paciente, da tese de que a desidentificação afasta o segredo, ou de que o processamento automatizado sem leitura humana não configura revelação: são leituras registradas no corpus, sem pronunciamento do CFM e sem precedente verificado.

## D9 — Aplique regime mais rígido no serviço público

Médico servidor que expõe dado obtido em razão do cargo responde por violação de sigilo funcional, e a ação penal independe de representação do paciente. Compartilhar credencial de sistema público com agente, automação ou terceiro, e usar acesso legítimo para finalidade não autorizada, são condutas típicas. Empregado de empresa contratada ou conveniada para executar atividade típica da Administração é equiparado a funcionário público e responde pelo sigilo funcional. A majorante de um terço alcança quem ocupa cargo em comissão, função de direção ou de assessoramento em órgão da administração direta, sociedade de economia mista, empresa pública ou fundação instituída pelo poder público.

**Base.** CP:art325 · CP:art327

**Verificar.**
- nenhuma credencial de sistema público está embutida em script, agente ou integração
- não há conta de serviço sem vínculo com pessoa identificada
- extração de coorte de base pública tem aprovação institucional ou de comitê registrada
- contrato ou convênio com órgão de saúde tem cláusula de sigilo para a equipe técnica do fornecedor

**Escalar se.** O caso concreto envolver concurso entre sigilo funcional e os demais tipos: a resolução do concurso não está verificada em precedente.

## D10 — Bloqueie acesso automatizado a dispositivo e sistema de uso alheio

Agente, script ou automação que acessa dispositivo de uso alheio sem autorização do usuário daquele dispositivo, com a finalidade de obter dados, configura invasão. Desde 2021 não é preciso quebrar barreira técnica. Instalar plugin, extensão ou servidor não homologado que abra canal de exfiltração pode configurar a modalidade de instalar vulnerabilidade, que exige finalidade de vantagem ilícita. A falta de homologação, por si, não é conduta típica. Se o que se obtém for enquadrado como informação sigilosa definida em lei, a pena sobe, e só nessa hipótese a transmissão a terceiro majora.

**Base.** CP:art154-A · CFM-2454-2026:art17 · LGPD:art46

**Verificar.**
- há lista de plugins, extensões e servidores homologados, com bloqueio do que está fora
- nenhuma automação usa credencial de outro usuário
- estação compartilhada tem controle de acesso por pessoa
- integração com prontuário eletrônico tem autorização registrada do responsável pelo sistema

**Escalar se.** O enquadramento depender de classificar dado de saúde como informação sigilosa definida em lei: a leitura não está verificada em precedente e decide se a majorante por transmissão existe.

## D11 — Aplique a lei brasileira ao provedor estrangeiro

Basta que um dos atos ocorra em território nacional, e a coleta acontece no consultório. Armazenamento, inferência e log no exterior não afastam a lei brasileira, que alcança pessoa jurídica sediada fora do país e ofertante ao público brasileiro. Enviar dado de paciente a modelo hospedado no exterior é transferência internacional e exige mecanismo próprio, além da base legal. Conta pessoal ou gratuita não satisfaz esse caminho.

**Base.** MCI:art11 · LGPD:art33 · ANPD-19-2024:anexoII · MCI:art7 · MCI:art10

**Verificar.**
- a região do endpoint de cada provedor está documentada
- o instrumento de transferência internacional está arquivado com data e traz as cláusulas-padrão do Anexo II da Res. ANPD 19/2024, adotadas integralmente e sem alteração
- o DPA padrão do fornecedor não é apresentado como substituto das cláusulas-padrão brasileiras
- os termos do provedor não impõem foro exclusivo no exterior em contrato de adesão sem alternativa brasileira

**Escalar se.** A base invocada for o consentimento do paciente para a transferência: ele não dispensa base autônoma para dado sensível nem os deveres de segurança. Para decisão de adequação e escolha do mecanismo, ver `fornecedor:D2` e `fornecedor:D4`.

## D12 — Prepare a defesa administrativa antes da fiscalização

A sanção administrativa é aplicada pela autoridade nacional de proteção de dados, em processo próprio. Infração com dado de saúde tende a ser classificada como grave, o que puxa a multa simples. Agrava descumprir medida de orientação ou corretiva. Atenua cessar a infração de forma espontânea, ter governança documentada, comprovar mitigação e cooperar. Corrigir só depois de determinação administrativa ou judicial não conta como atenuante. Dado de saúde e IA são prioridades de fiscalização no biênio 2026-2027.

**Base.** LGPD:art52 · LGPD:art52§1 · ANPD-4-2023:art8 · ANPD-4-2023:art12 · ANPD-4-2023:art13 · ANPD-30-2025:anexo

**Verificar.**
- política de boas práticas e governança com data e versão
- evidência de controles internos em operação, não apenas o documento
- registro datado de cada correção de fluxo, anterior a qualquer notificação
- rotina que garante resposta a determinação da autoridade dentro do prazo

**Escalar se.** O serviço for de pequeno porte e a multa calculada for desproporcional: o pedido de afastamento da metodologia de dosimetria é decisão do jurídico, sustentada desde a primeira manifestação no processo.

## D13 — Cumpra o prazo de comunicação de incidente

O reporte de falha, risco e uso inadequado de IA é `uso-clinico:D13`. Incidente de segurança tem regime próprio: comunicação à autoridade e ao titular em três dias úteis do conhecimento. Planeje para três dias úteis. Ataque externo não suspende os deveres de informação ao titular. Sem log e sem inventário, o prazo não é cumprível.

**Base.** LGPD:art48 · ANPD-15-2024:art6 · ANPD-15-2024:art9 · ANPD-15-2024:art10 · ANPD-2-2022:art4

**Verificar.**
- encarregado indicado, com ato de indicação e comprovante de vínculo prontos antes do incidente
- modelo de comunicação ao paciente pronto, em linguagem simples
- cadastro de pacientes com canal de contato atualizado
- registro de todo incidente, inclusive o não comunicado
- o serviço não está apoiado no regime de pequeno porte sem análise de alto risco registrada

**Escalar se.** O serviço pretender usar o prazo em dobro do agente de pequeno porte: o enquadramento não está pacificado no uso de LLM sobre dado sensível.

## D14 — Construa a prova exigida pela proteção contra falha do sistema

No âmbito ético-disciplinar, o CRM só reconhece a proteção do médico contra responsabilização por falha atribuível exclusivamente ao sistema mediante prova de uso diligente, crítico e ético. A proteção de quem não segue a orientação da ferramenta é condicionada do mesmo modo. Nas esferas civil e penal essa proteção não é oponível: a resolução ressalva as duas. Sem registro de entrada, saída, versão do modelo, revisão humana e fundamento da decisão, a condição não se prova. O exercício desses direitos perante fornecedor e instituição é `uso-clinico:D9`.

**Base.** CFM-2454-2026:art3 · CFM-2454-2026:art8 · CFM-2454-2026:art19 · CFM-2454-2026:art15

**Verificar.**
- cada uso relevante tem entrada, saída, versão e revisão persistidas na trilha de auditoria (classe B), não no log de aplicação
- a decisão divergente da sugestão da IA está fundamentada no prontuário

**Escalar se.** O fornecedor não entregar documentação de limitações e de evidência, ou não permitir registrar a versão em uso.

---

## Lacunas que sobem para o jurídico

Pontos sem entendimento consolidado. Nenhuma diretriz se constrói sobre eles:

- responsabilidade objetiva por atividade de risco aplicada a tratamento de dado por IA: doutrina, sem texto expresso e sem precedente verificado
- dano moral por vazamento de dado de saúde: não há decisão consolidada do tribunal superior; os precedentes levantados tratam de dado não sensível e foram lidos por verbete
- efeito de decisão criminal sobre as demais esferas
- cisão do regime de responsabilidade dentro da pessoa jurídica entre serviço do estabelecimento e ato técnico do médico: registrada em fonte secundária
- dado de saúde como informação sigilosa definida em lei, para efeito de agravamento penal
- justa causa penal por consentimento, e efeito da desidentificação sobre o segredo
- perda do regime de pequeno porte por tratamento de alto risco, e o prazo de comunicação de incidente que dela decorre
- retenção de prompts e logs pelo provedor diante do princípio da necessidade
- guarda permanente do prontuário eletrônico diante da eliminação autorizada por lei posterior
