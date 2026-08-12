---
norma: Lei nº 13.709/2018, arts. 37 a 49; Resolução CD/ANPD nº 15, de 24/04/2024; Resolução CD/ANPD nº 18, de 16/07/2024; Resolução CD/ANPD nº 2, de 27/01/2022
recorte: agentes de tratamento, registro de operações, encarregado, responsabilidade civil, segurança, sigilo, comunicação de incidente, regime de pequeno porte
alteracao: os arts. 37 a 49 da LGPD não foram alterados pela MP 1.317/2025 nem pela Lei nº 15.352, de 25/02/2026. O art. 5º, VIII (encarregado) recebeu nova redação da Lei nº 15.352/2026. A Res. CD/ANPD nº 2/2022 está vigente com a alteração do art. 14, II do seu Regulamento pelo art. 2º da Res. CD/ANPD nº 15/2024.
status: vinculante
fonte: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024 · https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074 · https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022
verificado: 2026-08-11
origem: corpus/bruto/01_lgpd.md, seções 0, 6 a 8 e 13
---

# LGPD e ANPD — agentes, responsabilidade, segurança e incidente

Cobre os papéis de controlador e operador, o registro de operações, o encarregado, o regime de responsabilidade, os deveres de segurança e sigilo, a comunicação de incidente e o tratamento diferenciado dos agentes de pequeno porte.

---

## LGPD:art5.VI-VII-IX

**Ementa.** Definições de controlador, operador e agentes de tratamento.

**Literal.**
> "VI - controlador: pessoa natural ou jurídica, de direito público ou privado, a quem competem as decisões referentes ao tratamento de dados pessoais;"
> "VII - operador: pessoa natural ou jurídica, de direito público ou privado, que realiza o tratamento de dados pessoais em nome do controlador;"
> "IX - agentes de tratamento: o controlador e o operador;"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O médico ou a clínica que decide a finalidade é controlador. O provedor do LLM é operador apenas se tratar os dados estritamente sob instruções do controlador e sem finalidade própria. Se o provedor usa os inputs para treinar ou melhorar modelos, define finalidade própria e tende a ser controlador autônomo. A consequência prática é contratar plano ou API com opção contratual de não usar os dados para treinamento e com retenção zero ou curta, que é o que sustenta juridicamente o enquadramento como operador.

**Gatilhos.**
- configuração padrão do provedor com uso dos inputs para treinamento
- ausência de cláusula de finalidade restrita às instruções do controlador
- uso de conta pessoal, gratuita ou de consumidor em fluxo clínico

**Incerteza.** Ponto não pacificado nº 1 do material bruto: enquadramento do provedor de LLM como operador ou como controlador. Não há decisão da ANPD nem jurisprudência consolidada verificada. Se controlador, incide a vedação do art. 11, §4º. Se operador, aplicam-se o art. 39 e o dever de instrução. A qualificação depende do fato contratual — uso ou não dos inputs para finalidade própria —, e não do rótulo adotado no contrato.

**Relacionados.** LGPD:art39 · LGPD:art11§4 · LGPD:art42

---

## LGPD:art5.VIII

**Ementa.** Definição de encarregado, com a redação da Lei 15.352/2026.

**Literal.**
> "encarregado: pessoa indicada pelo controlador e operador para atuar como canal de comunicação entre o controlador, os titulares dos dados e a Agência Nacional de Proteção de Dados (ANPD);"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Redação nova, dada pela Lei nº 15.352, de 25/02/2026. A referência passou a ser a Agência Nacional de Proteção de Dados. Documento interno que reproduza a redação anterior está desatualizado.

**Relacionados.** LGPD:art41 · ANPD-18-2024:art3

---

## LGPD:art37

**Ementa.** Dever de manter registro das operações de tratamento.

**Literal.**
> "Art. 37. O controlador e o operador devem manter registro das operações de tratamento de dados pessoais que realizarem, especialmente quando baseado no legítimo interesse."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** O dever alcança controlador e operador, sem depender de porte ou de volume. O registro é o documento que responde, em fiscalização, quais dados são tratados, com que finalidade, sob que base legal e para quem são transferidos. Agentes de pequeno porte podem cumpri-lo de forma simplificada (art. 9º da Res. 2/2022), desde que mantenham o regime diferenciado.

**Gatilhos.**
- ausência de registro de operações de tratamento
- inventário de dados desatualizado em relação aos provedores em uso
- fluxo de LLM ausente do inventário

**Relacionados.** ANPD-2-2022:art9 · ANPD-19-2024:art4 · LGPD:art38

---

## LGPD:art38

**Ementa.** Relatório de impacto à proteção de dados pessoais.

**Literal.**
> "Art. 38. A autoridade nacional poderá determinar ao controlador que elabore relatório de impacto à proteção de dados pessoais, inclusive de dados sensíveis, referente a suas operações de tratamento de dados, nos termos de regulamento, observados os segredos comercial e industrial.
> Parágrafo único. Observado o disposto no caput deste artigo, o relatório deverá conter, no mínimo, a descrição dos tipos de dados coletados, a metodologia utilizada para a coleta e para a garantia da segurança das informações e a análise do controlador com relação a medidas, salvaguardas e mecanismos de mitigação de risco adotados."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A elaboração depende de determinação da ANPD. Ter o relatório pronto antecipa a resposta a uma determinação e conta como política de boas práticas e governança para fins do art. 52, §1º, IX. A regulamentação do relatório é o item 2 da Agenda Regulatória 2025-2026, na redação da Res. CD/ANPD nº 31/2025, ainda não editada.

**Gatilhos.**
- tratamento de dado sensível em escala sem relatório de impacto
- ausência de descrição documentada de salvaguardas por fluxo

**Relacionados.** LGPD:art52§1 · CFM-2454-2026:art12

---

## LGPD:art39

**Ementa.** Dever do operador de seguir as instruções do controlador.

**Literal.**
> "Art. 39. O operador deverá realizar o tratamento segundo as instruções fornecidas pelo controlador, que verificará a observância das próprias instruções e das normas sobre a matéria."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A verificação é dever do controlador, com registro. Instrução por escrito significa contrato com finalidade delimitada, vedação de uso para treinamento, prazo de retenção e sub-operadores declarados. Se o provedor trata os dados por conta própria, o art. 39 deixa de descrever a relação e entra a hipótese de controlador autônomo.

**Gatilhos.**
- ausência de contrato que delimite finalidade e retenção
- sub-operadores não declarados na cadeia do fornecedor
- ausência de evidência de verificação periódica do fornecedor

**Relacionados.** LGPD:art5.VI-VII-IX · LGPD:art42

---

## LGPD:art40

**Ementa.** Competência da ANPD sobre padrões de interoperabilidade e tempo de guarda.

**Literal.**
> "Art. 40. A autoridade nacional poderá dispor sobre padrões de interoperabilidade para fins de portabilidade, livre acesso aos dados e segurança, assim como sobre o tempo de guarda dos registros, tendo em vista especialmente a necessidade e a transparência."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** Competência não exercida quanto a tempo de guarda até 11/08/2026. Na ausência de padrão da ANPD, o prazo de retenção segue o princípio da necessidade e as normas setoriais de guarda de prontuário.

**Relacionados.** LGPD:art47

---

## LGPD:art41

**Ementa.** Indicação e atribuições do encarregado.

**Literal.**
> "Art. 41. O controlador deverá indicar encarregado pelo tratamento de dados pessoais.
> § 1º A identidade e as informações de contato do encarregado deverão ser divulgadas publicamente, de forma clara e objetiva, preferencialmente no sítio eletrônico do controlador.
> § 2º As atividades do encarregado consistem em: I - aceitar reclamações e comunicações dos titulares, prestar esclarecimentos e adotar providências; II - receber comunicações da autoridade nacional e adotar providências; III - orientar os funcionários e os contratados da entidade a respeito das práticas a serem tomadas em relação à proteção de dados pessoais; e IV - executar as demais atribuições determinadas pelo controlador ou estabelecidas em normas complementares.
> § 3º A autoridade nacional poderá estabelecer normas complementares sobre a definição e as atribuições do encarregado, inclusive hipóteses de dispensa da necessidade de sua indicação, conforme a natureza e o porte da entidade ou o volume de operações de tratamento de dados.
> § 4º (VETADO). (Incluído pela Lei nº 13.853, de 2019)"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** O dever é do controlador. A dispensa para agente de pequeno porte vem do art. 11 da Res. 2/2022 e depende de o agente manter o regime diferenciado, o que o uso de LLM sobre dado sensível pode afastar — ver ANPD-2-2022:art4. Quem se enquadra na dispensa ainda precisa oferecer canal de comunicação com o titular.

**Gatilhos.**
- ausência de encarregado indicado e de canal de contato publicado
- página de contato sem informação de encarregado
- ausência de ato formal de indicação

**Relacionados.** ANPD-18-2024:art3 · ANPD-2-2022:art11 · LGPD:art5.VIII

---

## LGPD:art42

**Ementa.** Reparação de dano e responsabilidade solidária.

**Literal.**
> "Art. 42. O controlador ou o operador que, em razão do exercício de atividade de tratamento de dados pessoais, causar a outrem dano patrimonial, moral, individual ou coletivo, em violação à legislação de proteção de dados pessoais, é obrigado a repará-lo.
> § 1º A fim de assegurar a efetiva indenização ao titular dos dados:
> I - o operador responde solidariamente pelos danos causados pelo tratamento quando descumprir as obrigações da legislação de proteção de dados ou quando não tiver seguido as instruções lícitas do controlador, hipótese em que o operador equipara-se ao controlador, salvo nos casos de exclusão previstos no art. 43 desta Lei;
> II - os controladores que estiverem diretamente envolvidos no tratamento do qual decorreram danos ao titular dos dados respondem solidariamente, salvo nos casos de exclusão previstos no art. 43 desta Lei.
> § 2º O juiz, no processo civil, poderá inverter o ônus da prova a favor do titular dos dados quando, a seu juízo, for verossímil a alegação, houver hipossuficiência para fins de produção de prova ou quando a produção de prova pelo titular resultar-lhe excessivamente onerosa.
> § 3º As ações de reparação por danos coletivos que tenham por objeto a responsabilização nos termos do caput deste artigo podem ser exercidas coletivamente em juízo, observado o disposto na legislação pertinente.
> § 4º Aquele que reparar o dano ao titular tem direito de regresso contra os demais responsáveis, na medida de sua participação no evento danoso."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A solidariedade do §1º protege o titular. O paciente pode acionar o médico e o provedor do LLM, e o médico responde integralmente, com direito de regresso apenas depois. Regresso contra empresa estrangeira é de execução difícil. O §2º permite inversão do ônus da prova, o que na prática obriga o médico a demonstrar que agiu corretamente. Isso torna a trilha de auditoria um ativo de defesa.

**Gatilhos.**
- ausência de trilha de auditoria das chamadas ao provedor
- ausência de registro de qual dado saiu, quando e para onde
- ausência de contrato que permita regresso em foro brasileiro

**Relacionados.** LGPD:art43 · LGPD:art44 · CFM-2454-2026:art3

---

## LGPD:art43

**Ementa.** Excludentes de responsabilidade.

**Literal.**
> "Art. 43. Os agentes de tratamento só não serão responsabilizados quando provarem:
> I - que não realizaram o tratamento de dados pessoais que lhes é atribuído;
> II - que, embora tenham realizado o tratamento de dados pessoais que lhes é atribuído, não houve violação à legislação de proteção de dados; ou
> III - que o dano é decorrente de culpa exclusiva do titular dos dados ou de terceiro."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Rol taxativo, com ônus de prova do agente. Desconhecimento do comportamento do fornecedor não consta do rol. Alegar que a API armazenava o payload sem que o agente soubesse não afasta a responsabilidade.

**Relacionados.** LGPD:art42 · LGPD:art44

---

## LGPD:art44

**Ementa.** Tratamento irregular e padrão de segurança esperado.

**Literal.**
> "Art. 44. O tratamento de dados pessoais será irregular quando deixar de observar a legislação ou quando não fornecer a segurança que o titular dele pode esperar, consideradas as circunstâncias relevantes, entre as quais:
> I - o modo pelo qual é realizado;
> II - o resultado e os riscos que razoavelmente dele se esperam;
> III - as técnicas de tratamento de dados pessoais disponíveis à época em que foi realizado.
> Parágrafo único. Responde pelos danos decorrentes da violação da segurança dos dados o controlador ou o operador que, ao deixar de adotar as medidas de segurança previstas no art. 46 desta Lei, der causa ao dano."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O inciso III transforma a existência de alternativas em padrão de conduta exigível. Modelo local, região de processamento no Brasil ou na UE, desidentificação prévia e contrato com retenção zero são técnicas disponíveis à época. Se a alternativa segura existia e não foi adotada, o tratamento é irregular.

**Gatilhos.**
- uso de provedor sem opção de retenção zero quando o mesmo provedor a oferece em outro plano
- envio de dado identificável quando existe rotina de desidentificação disponível no próprio sistema
- região externa selecionada havendo região adequada disponível

**Relacionados.** LGPD:art46 · CFM-2454-2026:art17

---

## LGPD:art45

**Ementa.** Relações de consumo.

**Literal.**
> "Art. 45. As hipóteses de violação do direito do titular no âmbito das relações de consumo permanecem sujeitas às regras de responsabilidade previstas na legislação pertinente."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Abre a via do Código de Defesa do Consumidor quando a relação é de consumo, como no atendimento particular, com responsabilidade objetiva e prazos próprios. O detalhamento fica na ficha 10.

**Relacionados.** LGPD:art42

---

## LGPD:art46

**Ementa.** Dever de adotar medidas de segurança, desde a concepção.

**Literal.**
> "Art. 46. Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito.
> § 1º A autoridade nacional poderá dispor sobre padrões técnicos mínimos para tornar aplicável o disposto no caput deste artigo, considerados a natureza das informações tratadas, as características específicas do tratamento e o estado atual da tecnologia, especialmente no caso de dados pessoais sensíveis, assim como os princípios previstos no caput do art. 6º desta Lei.
> § 2º As medidas de que trata o caput deste artigo deverão ser observadas desde a fase de concepção do produto ou do serviço até a sua execução."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** O dever é dos agentes de tratamento, sem depender de determinação prévia da ANPD. O §2º impõe segurança desde a concepção, o que alcança protótipo, ambiente de homologação e prova de conceito. Os padrões técnicos mínimos do §1º não foram editados até 11/08/2026 — é o item 5 da Agenda Regulatória, Fase 1, na redação da Res. CD/ANPD nº 31/2025. Na ausência deles, ancorar em referência técnica datada e registrar a data da avaliação.

**Gatilhos.**
- chave de API em código ou em .env versionado
- ausência de criptografia em repouso para base com dado de paciente
- transporte sem TLS ou com verificação de certificado desligada
- ausência de controle de acesso por perfil
- base de homologação populada com dado real de paciente

**Relacionados.** LGPD:art44 · LGPD:art47 · CFM-2454-2026:art17 · CFM-2454-2026:anexoI.XV-XVI

---

## LGPD:art47

**Ementa.** Dever de segurança mesmo após o término do tratamento.

**Literal.**
> "Art. 47. Os agentes de tratamento ou qualquer outra pessoa que intervenha em uma das fases do tratamento obriga-se a garantir a segurança da informação prevista nesta Lei em relação aos dados pessoais, mesmo após o seu término."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Alcança qualquer pessoa que intervenha em uma fase do tratamento, inclusive prestador eventual, estagiário e suporte técnico. A obrigação persiste após o fim do contrato ou da finalidade, o que impõe rotina de eliminação verificável e cláusula de devolução ou destruição.

**Gatilhos.**
- ausência de rotina de expurgo por prazo de retenção
- backup sem política de eliminação
- histórico de conversa ou log de prompts sem prazo definido
- ausência de cláusula de eliminação ao término do contrato com o provedor

**Incerteza.** Ponto não pacificado nº 6 do material bruto: retenção de logs e prompts pelo provedor por período contratual, por exemplo trinta dias para monitoramento de abuso, e sua compatibilidade com o princípio da necessidade (art. 6º, III) e com este artigo. Leitura permissiva: a retenção curta para segurança é finalidade legítima do próprio provedor. Leitura restritiva: retenção de dado sensível sem base do art. 11 descumpre a necessidade. Nenhum ato da ANPD verificado enfrenta a questão.

**Relacionados.** LGPD:art46 · LGPD:art40

---

## LGPD:art48

**Ementa.** Comunicação de incidente à autoridade nacional e ao titular.

**Literal.**
> "Art. 48. O controlador deverá comunicar à autoridade nacional e ao titular a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante aos titulares.
> § 1º A comunicação será feita em prazo razoável, conforme definido pela autoridade nacional, e deverá mencionar, no mínimo:
> I - a descrição da natureza dos dados pessoais afetados;
> II - as informações sobre os titulares envolvidos;
> III - a indicação das medidas técnicas e de segurança utilizadas para a proteção dos dados, observados os segredos comercial e industrial;
> IV - os riscos relacionados ao incidente;
> V - os motivos da demora, no caso de a comunicação não ter sido imediata; e
> VI - as medidas que foram ou que serão adotadas para reverter ou mitigar os efeitos do prejuízo.
> § 2º A autoridade nacional verificará a gravidade do incidente e poderá, caso necessário para a salvaguarda dos direitos dos titulares, determinar ao controlador a adoção de providências, tais como: I - ampla divulgação do fato em meios de comunicação; e II - medidas para reverter ou mitigar os efeitos do incidente.
> § 3º No juízo de gravidade do incidente, será avaliada eventual comprovação de que foram adotadas medidas técnicas adequadas que tornem os dados pessoais afetados ininteligíveis, no âmbito e nos limites técnicos de seus serviços, para terceiros não autorizados a acessá-los."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** O dever é do controlador, com prazo definido pela Res. 15/2024. O §3º dá efeito jurídico à criptografia: dado ininteligível para terceiro não autorizado reduz a gravidade aferida. Isso torna a criptografia com chave sob controle próprio uma medida com valor sancionatório direto.

**Gatilhos.**
- ausência de rotina de notificação de incidente
- ausência de responsável designado para acionar a comunicação
- ausência de criptografia que torne o dado ininteligível a terceiro

**Relacionados.** ANPD-15-2024:art6 · ANPD-15-2024:art9 · LGPD:art46

---

## LGPD:art49

**Ementa.** Estruturação dos sistemas conforme requisitos de segurança e governança.

**Literal.**
> "Art. 49. Os sistemas utilizados para o tratamento de dados pessoais devem ser estruturados de forma a atender aos requisitos de segurança, aos padrões de boas práticas e de governança e aos princípios gerais previstos nesta Lei e às demais normas regulamentares."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Requisito de arquitetura, dirigido ao sistema e não apenas ao uso. Alcança decisão de projeto: segregação de ambientes, minimização no schema, campos sensíveis isolados, política de logs.

**Gatilhos.**
- log de aplicação que persiste payload de requisição
- rastreamento de erro que envia contexto com dado de paciente a serviço externo
- ausência de segregação entre ambiente de desenvolvimento e produção

**Relacionados.** LGPD:art46 · CFM-2454-2026:art9

---

## LGPD:art50§2.I.g

**Ementa.** Plano de resposta a incidentes no programa de governança em privacidade.

**Literal.**
> "g) conte com planos de resposta a incidentes e remediação; e"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** Requisito mínimo do programa de governança em privacidade. Ter o plano documentado sustenta o atenuante do art. 52, §1º, IX e do art. 13, II da Res. 4/2023.

**Gatilhos.**
- ausência de plano de resposta a incidente documentado

**Relacionados.** LGPD:art52§1 · ANPD-4-2023:art13

---

## ANPD-15-2024:art5

**Ementa.** Critérios do incidente que pode acarretar risco ou dano relevante.

**Literal.**
> "Art. 5º O incidente de segurança pode acarretar risco ou dano relevante aos titulares quando puder afetar significativamente interesses e direitos fundamentais dos titulares e, cumulativamente, envolver, pelo menos, um dos seguintes critérios: I - dados pessoais sensíveis; II - dados de crianças, de adolescentes ou de idosos; III - dados financeiros; IV - dados de autenticação em sistemas; V - dados protegidos por sigilo legal, judicial ou profissional; ou VI - dados em larga escala."

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Dado de saúde é dado sensível (art. 5º, II da LGPD) e dado protegido por sigilo profissional. Qualquer incidente com dado de paciente satisfaz dois critérios do inciso ao mesmo tempo. Resta apenas o requisito de afetar significativamente interesses e direitos fundamentais, que em contexto clínico é a regra.

**Relacionados.** LGPD:art5.II · ANPD-15-2024:art6

---

## ANPD-15-2024:art6

**Ementa.** Prazo e conteúdo da comunicação à ANPD.

**Literal.**
> "Art. 6º A comunicação de incidente de segurança à ANPD deverá ser realizada pelo controlador no prazo de três dias úteis, ressalvada a existência de prazo para comunicação previsto em legislação específica.
> § 1º O prazo a que se refere o caput será contado do conhecimento pelo controlador de que o incidente afetou dados pessoais.
> § 2º A comunicação de incidente de segurança deverá conter as seguintes informações: I - a descrição da natureza e da categoria de dados pessoais afetados; II - o número de titulares afetados, discriminando, quando aplicável, o número de crianças, de adolescentes ou de idosos; III - as medidas técnicas e de segurança utilizadas para a proteção dos dados pessoais, adotadas antes e após o incidente [...]; IV - os riscos relacionados ao incidente com identificação dos possíveis impactos aos titulares; V - os motivos da demora [...]; VI - as medidas que foram ou que serão adotadas para reverter ou mitigar os efeitos do incidente sobre os titulares; VII - a data da ocorrência do incidente, quando possível determiná-la, e a de seu conhecimento pelo controlador; VIII - os dados do encarregado ou de quem represente o controlador; IX - a identificação do controlador e, se for o caso, declaração de que se trata de agente de tratamento de pequeno porte; X - a identificação do operador, quando aplicável; XI - a descrição do incidente, incluindo a causa principal, caso seja possível identificá-la; e XII - o total de titulares cujos dados são tratados nas atividades de tratamento afetadas pelo incidente.
> § 3º As informações poderão ser complementadas, de maneira fundamentada, no prazo de vinte dias úteis, a contar da data da comunicação.
> § 4º A comunicação de incidente de segurança deverá ocorrer por meio de formulário eletrônico disponibilizado pela ANPD.
> § 5º A comunicação [...] deverá ser realizada pelo controlador, por meio do encarregado, acompanhada de documento comprobatório de vínculo contratual, empregatício ou funcional, ou por meio de representante constituído, acompanhada de instrumento com poderes de representação junto à ANPD.
> § 6º Os documentos de que trata o § 5º deverão ser apresentados juntamente com a comunicação do incidente de segurança, no prazo previsto no caput deste artigo.
> § 7º No caso de descumprimento do previsto no § 6º, a ANPD poderá apurar a ocorrência do incidente de segurança por meio do procedimento de apuração de incidente de segurança.
> § 8º Os prazos constantes no caput e no § 3º deste artigo são contados em dobro para os agentes de pequeno porte [...]"

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Três dias úteis do conhecimento, seis dias úteis para agente de pequeno porte que mantenha o regime diferenciado. O §8º dobra também o prazo do §3º, de vinte para quarenta dias úteis. A comunicação ao titular tem regra própria de contagem em dobro, no § 6º do art. 9º. A base do regime é o art. 14, II do Regulamento da Res. 2/2022, na redação dada pelo art. 2º da própria Res. 15/2024. O §2º exige dados que só existem se houver instrumentação prévia: número de titulares afetados, data da ocorrência, causa principal, identificação do operador. Sem log e sem inventário, o prazo não é cumprível. Os §§ 5º e 6º acrescentam um requisito documental com o mesmo prazo: a comunicação é protocolada pelo encarregado, com comprovante de vínculo, ou por representante constituído, com instrumento de representação. Quem não tem encarregado indicado nem procuração pronta não consegue protocolar dentro do prazo. Pelo § 7º, o descumprimento do § 6º permite à ANPD apurar o incidente por procedimento próprio. Preparar o ato de indicação e o comprovante de vínculo antes do incidente. Incidentes típicos em contexto de LLM: prompt com dado de paciente enviado a conta pessoal ou gratuita cujo provedor usa inputs para treino; log de conversa exposto; chave de API vazada; histórico de chat compartilhado por link público; extensão de navegador capturando prompts.

**Gatilhos.**
- ausência de rotina de notificação de incidente com prazo definido
- ausência de log que permita contar titulares afetados
- ausência de ato de indicação do encarregado ou de instrumento de representação disponível para protocolo
- histórico de chat com compartilhamento por link habilitado
- extensão de navegador com acesso a interface clínica
- chave de API exposta em repositório

**Relacionados.** LGPD:art48 · ANPD-15-2024:art9 · ANPD-2-2022:art2.I

---

## ANPD-15-2024:art9

**Ementa.** Prazo e forma da comunicação ao titular.

**Literal.**
> "Art. 9º A comunicação de incidente de segurança ao titular deverá ser realizada pelo controlador no prazo de três dias úteis contados do conhecimento pelo controlador de que o incidente afetou dados pessoais [...] § 1º [...] I - fazer uso de linguagem simples e de fácil entendimento; e II - ocorrer de forma direta e individualizada, caso seja possível identificá-los. [...] § 3º Caso a comunicação direta e individualizada mostre-se inviável [...] pelos meios de divulgação disponíveis [...] pelo período de, no mínimo, três meses. § 4º O controlador deverá juntar ao processo [...] uma declaração de que foi realizada a comunicação aos titulares [...] em até três dias úteis, contados do término do prazo de que trata o caput deste artigo. [...] § 6º O prazo constante no caput deste artigo é contado em dobro para os agentes de pequeno porte [...]"

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** A comunicação ao paciente corre no mesmo prazo da comunicação à ANPD e deve ser individualizada quando o titular puder ser identificado. Exige canal de contato atualizado no cadastro e modelo de mensagem pronto.

**Gatilhos.**
- cadastro sem canal de contato válido do paciente
- ausência de modelo de comunicação ao titular

**Relacionados.** ANPD-15-2024:art6

---

## ANPD-15-2024:art10

**Ementa.** Registro de incidentes por cinco anos, inclusive dos não comunicados.

**Literal.**
> "Art. 10. O controlador deverá manter o registro do incidente de segurança, inclusive daquele não comunicado à ANPD e aos titulares, pelo prazo mínimo de cinco anos, contado a partir da data do registro [...]"

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Obriga a manter livro de incidentes mesmo para casos avaliados como não relevantes, com a avaliação registrada. O registro é o que demonstra, em fiscalização, que a decisão de não comunicar foi fundamentada.

**Gatilhos.**
- ausência de registro interno de incidentes
- decisão de não comunicar sem justificativa documentada

**Relacionados.** ANPD-15-2024:art5

---

## ANPD-15-2024:art21

**Ementa.** Processo sancionador por não adoção de medidas determinadas.

**Literal.**
> "Art. 21. A ANPD poderá instaurar processo administrativo sancionador caso o controlador não adote as medidas para reverter ou mitigar os efeitos do incidente de segurança no prazo e nas condições determinadas pela Autoridade."

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Descumprir medida determinada abre processo sancionador autônomo e agrava a dosimetria — ver o art. 12, III e IV da Res. 4/2023.

**Relacionados.** ANPD-4-2023:art12

---

## ANPD-18-2024:art3

**Ementa.** Indicação do encarregado por ato formal.

**Literal.**
> "Art. 3º A indicação do encarregado deve ser realizada por ato formal do agente de tratamento, do qual constem as formas de atuação e as atividades a serem desempenhadas.
> § 1º Entende-se por ato formal o documento escrito, datado e assinado, que, de maneira clara e inequívoca, demonstre a intenção do agente de tratamento em designar como encarregado uma pessoa natural ou uma pessoa jurídica.
> § 2º O documento referido no caput deverá ser apresentado à ANPD, quando solicitado.
> § 3º Os Agentes de Tratamento de Pequeno Porte dispensados de indicar encarregado devem disponibilizar um canal de comunicação com o titular de dados, nos termos do art. 11 do Regulamento [...] aprovado pela Resolução CD/ANPD nº 2, de 27 de janeiro de 2022."

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Documento escrito, datado e assinado, com descrição das atividades. Menção em política interna não substitui o ato formal.

**Gatilhos.**
- encarregado citado em política sem ato formal de indicação

**Relacionados.** LGPD:art41 · ANPD-2-2022:art11

---

## ANPD-18-2024:art6

**Ementa.** Indicação de encarregado por operadores.

**Literal.**
> "Art. 6º A indicação de encarregado por operadores é facultativa e será considerada política de boas práticas de governança para fins do disposto no art. 52, § 1º, inciso IX, da Lei nº 13.709 [...]"

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** Para quem atua como operador, a indicação é facultativa e conta como atenuante na dosimetria.

**Relacionados.** LGPD:art52§1 · ANPD-4-2023:art13

---

## ANPD-18-2024:art9

**Ementa.** Divulgação pública da identidade e do contato do encarregado.

**Literal.**
> "Art. 9º A identidade e as informações de contato do encarregado deverão ser divulgadas publicamente, de forma clara e objetiva, em local de destaque e de fácil acesso, no sítio eletrônico do agente de tratamento, ressalvada a hipótese do § 3º deste artigo.
> [...]
> § 3º O agente de tratamento que não possuir sítio eletrônico poderá realizar a divulgação da identidade e das informações de contato do encarregado por quaisquer outros meios de comunicação disponíveis, especialmente aqueles usualmente utilizados para contato com os titulares."

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Quem tem site divulga no site, em local de destaque e de fácil acesso. Contato enterrado em documento anexo não cumpre o dispositivo. Quem não tem site divulga por outro meio disponível, na forma do § 3º, com preferência pelos canais já usados no contato com o paciente — recepção, cartão de visita, mensagem de agendamento, perfil profissional. A ausência de site não caracteriza descumprimento do artigo. O descumprimento ocorre quando não há divulgação por nenhum meio.

**Gatilhos.**
- agente de tratamento com site, sem página ou seção de contato do encarregado
- contato do encarregado apenas dentro de PDF de política
- agente de tratamento sem site e sem qualquer meio de divulgação do contato do encarregado

**Relacionados.** LGPD:art41

---

## ANPD-18-2024:art11

**Ementa.** Responsabilidade permanece com o agente de tratamento.

**Literal.**
> "Art. 11. O agente de tratamento é o responsável pela conformidade do tratamento dos dados pessoais, nos termos da Lei nº 13.709, de 14 de agosto de 2018."

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A indicação de encarregado não transfere responsabilidade. Contratar DPO externo não desloca o dever de conformidade do médico ou da clínica.

**Relacionados.** LGPD:art42

---

## ANPD-18-2024:art12-art14

**Ementa.** Quem pode ser encarregado, comunicação e ausência de exigência de certificação.

**Literal.**
> "Art. 12. O encarregado poderá ser: I - uma pessoa natural, integrante do quadro organizacional do agente de tratamento ou externo a esse; ou II - uma pessoa jurídica."
> "Art. 13. O encarregado deverá ser capaz de comunicar-se com os titulares e com a ANPD, de forma clara e precisa e em língua portuguesa."
> "Art. 14. O exercício da atividade de encarregado não pressupõe a inscrição em qualquer entidade nem qualquer certificação ou formação profissional específica."

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** Não há exigência de certificação. O encarregado pode ser interno, externo ou pessoa jurídica, e precisa atuar em português.

**Relacionados.** ANPD-18-2024:art3

---

## ANPD-2-2022:art2.I

**Ementa.** Definição de agente de tratamento de pequeno porte.

**Literal.**
> "Art. 2º [...] I - agentes de tratamento de pequeno porte: microempresas, empresas de pequeno porte, startups, pessoas jurídicas de direito privado, inclusive sem fins lucrativos, nos termos da legislação vigente, bem como pessoas naturais e entes privados despersonalizados que realizam tratamento de dados pessoais, assumindo obrigações típicas de controlador ou de operador;"

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O médico pessoa natural está expressamente incluído. O enquadramento é o ponto de partida, e depende dos arts. 3º e 4º para se manter.

**Relacionados.** ANPD-2-2022:art3 · ANPD-2-2022:art4

---

## ANPD-2-2022:art3

**Ementa.** Exclusões do regime diferenciado.

**Literal.**
> "Art. 3º Não poderão se beneficiar do tratamento jurídico diferenciado previsto neste Regulamento os agentes de tratamento de pequeno porte que: I - realizem tratamento de alto risco para os titulares, ressalvada a hipótese prevista no art. 8º; II - aufiram receita bruta superior ao limite estabelecido no art. 3º, II, da Lei Complementar nº 123, de 2006 ou, no caso de startups, no art. 4º, § 1º, I, da Lei Complementar nº 182, de 2021; ou III - pertençam a grupo econômico de fato ou de direito, cuja receita global ultrapasse os limites referidos no inciso II, conforme o caso."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O inciso I é o que atinge o uso de LLM em saúde. Tratamento de alto risco afasta o regime diferenciado, com as consequências descritas em ANPD-2-2022:art4.

**Relacionados.** ANPD-2-2022:art4

---

## ANPD-2-2022:art4

**Ementa.** Critérios de tratamento de alto risco.

**Literal.**
> "Art. 4º Para fins deste regulamento, e sem prejuízo do disposto no art. 16, será considerado de alto risco o tratamento de dados pessoais que atender cumulativamente a pelo menos um critério geral e um critério específico, dentre os a seguir indicados: I - critérios gerais: a) tratamento de dados pessoais em larga escala; ou b) tratamento de dados pessoais que possa afetar significativamente interesses e direitos fundamentais dos titulares; II - critérios específicos: a) uso de tecnologias emergentes ou inovadoras; b) vigilância ou controle de zonas acessíveis ao público; c) decisões tomadas unicamente com base em tratamento automatizado de dados pessoais, inclusive aquelas destinadas a definir o perfil pessoal, profissional, de saúde, de consumo e de crédito ou os aspectos da personalidade do titular; ou d) utilização de dados pessoais sensíveis ou de dados pessoais de crianças, de adolescentes e de idosos."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Uso de LLM sobre dado de paciente aciona ao mesmo tempo os critérios específicos "a" (tecnologias emergentes ou inovadoras) e "d" (dados sensíveis), e o critério "c" quando há apoio à decisão clínica automatizada. Basta então um critério geral — larga escala ou possibilidade de afetar significativamente interesses e direitos fundamentais, que inclui dano material ou moral, discriminação e violação à integridade física — para o agente perder as flexibilizações. Perdidas as flexibilizações, voltam a ser exigíveis a indicação de encarregado (art. 41), o registro completo de operações (art. 37) e os prazos simples de comunicação de incidente. Este é o ponto de conformidade mais frequentemente ignorado por consultórios e clínicas.

**Gatilhos.**
- fluxo com LLM sobre dado de paciente em serviço que se declara pequeno porte
- documentação interna que invoca regime simplificado sem análise de alto risco
- apoio à decisão clínica automatizado em agente de pequeno porte

**Incerteza.** Ponto não pacificado nº 7 do material bruto: qualificação do médico pessoa física como agente de tratamento de pequeno porte e a perda automática do regime pelo art. 3º, I combinado com o art. 4º quando há uso de tecnologia emergente sobre dado sensível. Leitura literal: a combinação de critérios é automática e o regime cai. Leitura alternativa: "larga escala" e "afetar significativamente" exigem análise concreta, que pode não se configurar em consultório individual. A ANPD reconhece a lacuna: o item 7 da Agenda Regulatória, "Tratamento de Dados Pessoais de Alto Risco", Fase 1, na redação da Res. CD/ANPD nº 31/2025, existe para dar parâmetros e não foi editado até 11/08/2026.

**Relacionados.** LGPD:art20 · LGPD:art37 · LGPD:art41 · CFM-2454-2026:art12

---

## ANPD-2-2022:art6

**Ementa.** Dispensa e flexibilização não isentam do restante da Lei.

**Literal.**
> "Art. 6º A dispensa ou flexibilização das obrigações dispostas neste regulamento não isenta os agentes de tratamento de pequeno porte do cumprimento dos demais dispositivos da LGPD, inclusive das bases legais e dos princípios [...]"

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O regime diferenciado alcança forma de cumprimento, sem afastar base legal, princípios e deveres de segurança.

**Relacionados.** LGPD:art11 · LGPD:art46

---

## ANPD-2-2022:art9

**Ementa.** Registro simplificado de operações.

**Literal.**
> "Art. 9º Os agentes de tratamento de pequeno porte podem cumprir a obrigação de elaboração e manutenção de registro das operações de tratamento de dados pessoais, constante do art. 37 da LGPD, de forma simplificada. Parágrafo único. A ANPD fornecerá modelo para o registro simplificado de que trata o caput."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** A simplificação alcança a forma, não a existência do registro. Quem perde o regime por alto risco volta ao registro completo.

**Relacionados.** LGPD:art37 · ANPD-2-2022:art3

---

## ANPD-2-2022:art11

**Ementa.** Dispensa de indicação de encarregado e canal de comunicação.

**Literal.**
> "Art. 11. Os agentes de tratamento de pequeno porte não são obrigados a indicar o encarregado pelo tratamento de dados pessoais exigido no art. 41 da LGPD. § 1º O agente de tratamento de pequeno porte que não indicar um encarregado deve disponibilizar um canal de comunicação com o titular de dados para atender o disposto no art. 41, § 2º, I da LGPD. § 2º A indicação de encarregado por parte dos agentes de tratamento de pequeno porte será considerada política de boas práticas e governança para fins do disposto no art. 52, § 1º, IX da LGPD."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A dispensa vale enquanto o regime diferenciado se mantém. O canal de comunicação com o titular continua obrigatório. Indicar encarregado mesmo dispensado conta como atenuante.

**Gatilhos.**
- ausência de canal de comunicação com o titular em serviço que se declara pequeno porte

**Relacionados.** LGPD:art41 · ANPD-2-2022:art4

---

## ANPD-2-2022:art12

**Ementa.** Dever de adotar medidas de segurança essenciais, para agente de pequeno porte.

**Literal.**
> "Art. 12. Os agentes de tratamento de pequeno porte devem adotar medidas administrativas e técnicas essenciais e necessárias, com base em requisitos mínimos de segurança da informação para proteção dos dados pessoais [...] Parágrafo único. O atendimento às recomendações e às boas práticas de prevenção e segurança divulgadas pela ANPD, inclusive por meio de guias orientativos, será considerado como observância ao disposto no art. 52, § 1º VIII da LGPD."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O caput usa "devem". O dispositivo impõe dever. Ele veicula para o agente de pequeno porte o mesmo dever de segurança do art. 46 da LGPD, com forma simplificada de cumprimento. Seguir o "Guia Orientativo — Segurança da informação para agentes de tratamento de pequeno porte" (ANPD, versão 1.0, out/2021) conta como observância do art. 52, §1º, VIII, por força do parágrafo único. O guia está em https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-sobre-seguranca-da-informacao-para-agentes-de-tratamento-de-pequeno-porte

**Gatilhos.**
- ausência de medidas técnicas mínimas de segurança em serviço que se declara pequeno porte
- serviço de pequeno porte que invoca o regime diferenciado como dispensa de segurança

**Relacionados.** LGPD:art46 · LGPD:art52§1 · ANPD-2-2022:art13

---

## ANPD-2-2022:art13

**Ementa.** Faculdade de política simplificada de segurança da informação.

**Literal.**
> "Art. 13. Os agentes de tratamento de pequeno porte podem estabelecer política simplificada de segurança da informação [...]"

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** O artigo é facultativo: usa "podem". A faculdade é quanto à forma da política, não quanto ao dever de segurança do art. 12. Política simplificada e datada serve de evidência na dosimetria.

**Gatilhos.**
- ausência de política de segurança da informação, ainda que simplificada

**Relacionados.** ANPD-2-2022:art12 · LGPD:art52§1

---

## Estado da regulamentação em 11/08/2026

Não existe regulamentação da ANPD específica sobre inteligência artificial nem sobre dados de saúde, verificado na página oficial de regulamentações consultada em 11/08/2026. Também não há guia orientativo da ANPD sobre esses dois temas.

Pendências que afetam esta ficha: art. 46, §1º, padrões técnicos mínimos de segurança (item 5 da Agenda Regulatória 2025-2026, Fase 1); tratamento de alto risco (item 7, Fase 1); relatório de impacto (item 2, Fase 1); tempo de guarda dos registros (art. 40, não exercido). A numeração dos itens é a da Agenda Regulatória na redação da Res. CD/ANPD nº 31, de 22/12/2025, que suprimiu o item 4 original, "Tratamento de dados pessoais de crianças e adolescentes", e renumerou a lista. Na redação original da Resolução nº 23, de 9 de dezembro de 2024, os mesmos temas são os itens 6, 8 e 2. Conferido item a item nos dois textos em 11/08/2026.

A página oficial de regulamentações, consultada em 11/08/2026, lista as Resoluções 1, 2, 4, 5, 10, 11, 15, 18, 19, 23, 30, 31 e 32. Não foi verificada a existência de eventuais resoluções da ANPD de nº 3, 6, 7, 8, 9, 12, 13, 14, 16, 17, 20, 21, 22 e 24 a 29, que não constam daquela página.

Duas resoluções listadas não estão transcritas neste corpus e não alteram esta ficha: a Res. CD/ANPD nº 31, de 22/12/2025, que altera a Agenda Regulatória, e a Res. CD/ANPD nº 32, de 26/01/2026, que reconhece a União Europeia como organismo internacional com grau de proteção adequado para fins de transferência internacional. A Res. 32/2026 é matéria da ficha 06 e exige reverificação cruzada. A Res. CD/ANPD nº 1/2021, sobre processo de fiscalização e processo administrativo sancionador, também não foi transcrita neste corpus.
