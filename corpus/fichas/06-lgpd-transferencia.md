---
norma: Lei nº 13.709/2018, arts. 33 a 36; Resolução CD/ANPD nº 19, de 23/08/2024; Resolução CD/ANPD nº 32, de 26/01/2026
recorte: transferência internacional de dados, mecanismos de transferência, cláusulas-padrão contratuais, decisão de adequação
alteracao: os arts. 33 a 36 da LGPD não foram alterados pela MP 1.317/2025 nem pela Lei nº 15.352, de 25/02/2026. A Res. CD/ANPD nº 19/2024 foi alterada pela RETIFICAÇÃO de 18/08/2025 (DOU de 18/08/2025, Edição 155, Seção 1, página 63), que mudou uma única remissão interna do Anexo II — no item 15.4, alínea b, onde se lia "no prazo previsto no item 15.2", leia-se "no prazo previsto no item 15.3". Nada mais foi alterado; o prazo do art. 2º, parágrafo único, permanece intacto.
status: vinculante
fonte: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · https://www.in.gov.br/web/dou/-/resolucao-n-32-de-26-de-janeiro-de-2026-683334547
verificado: 2026-08-11
origem: corpus/bruto/01_lgpd.md, seção 5 e subseções 5.1 e 5.2
---

# LGPD e ANPD — transferência internacional de dados

Cobre os arts. 33 a 36 da LGPD, os dispositivos operacionais do Regulamento de Transferência Internacional e a única decisão de adequação vigente.

---

## LGPD:art33

**Ementa.** Hipóteses que autorizam a transferência internacional de dados pessoais.

**Literal.**
> "Art. 33. A transferência internacional de dados pessoais somente é permitida nos seguintes casos:
> I - para países ou organismos internacionais que proporcionem grau de proteção de dados pessoais adequado ao previsto nesta Lei;
> II - quando o controlador oferecer e comprovar garantias de cumprimento dos princípios, dos direitos do titular e do regime de proteção de dados previstos nesta Lei, na forma de:
> a) cláusulas contratuais específicas para determinada transferência;
> b) cláusulas-padrão contratuais;
> c) normas corporativas globais;
> d) selos, certificados e códigos de conduta regularmente emitidos;
> III - quando a transferência for necessária para a cooperação jurídica internacional entre órgãos públicos de inteligência, de investigação e de persecução, de acordo com os instrumentos de direito internacional;
> IV - quando a transferência for necessária para a proteção da vida ou da incolumidade física do titular ou de terceiro;
> V - quando a autoridade nacional autorizar a transferência;
> VI - quando a transferência resultar em compromisso assumido em acordo de cooperação internacional;
> VII - quando a transferência for necessária para a execução de política pública ou atribuição legal do serviço público, sendo dada publicidade nos termos do inciso I do caput do art. 23 desta Lei;
> VIII - quando o titular tiver fornecido o seu consentimento específico e em destaque para a transferência, com informação prévia sobre o caráter internacional da operação, distinguindo claramente esta de outras finalidades; ou
> IX - quando necessário para atender as hipóteses previstas nos incisos II, V e VI do art. 7º desta Lei.
> Parágrafo único. Para os fins do inciso I deste artigo, as pessoas jurídicas de direito público referidas no parágrafo único do art. 1º da Lei nº 12.527, de 18 de novembro de 2011 (Lei de Acesso à Informação), no âmbito de suas competências legais, e responsáveis, no âmbito de suas atividades, poderão requerer à autoridade nacional a avaliação do nível de proteção a dados pessoais conferido por país ou organismo internacional."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** O mecanismo do art. 33 é exigido além da base legal do art. 7º ou do art. 11: são requisitos cumulativos, conforme o art. 9º da Res. 19/2024. Para dado de paciente enviado a API com processamento nos Estados Unidos, o inciso I está indisponível, porque não há decisão de adequação para os EUA. Na prática restam as cláusulas-padrão contratuais do Anexo II da Res. 19/2024, adotadas integralmente e sem alteração. Aceitar os termos de serviço ou o DPA padrão do fornecedor não substitui as cláusulas-padrão brasileiras.

O leque do inciso II é mais estreito do que a lista sugere. A página oficial de Transferência Internacional de Dados da ANPD declara, em 11/08/2026, que até a presente data não houve nenhuma decisão do Conselho Diretor sobre cláusulas contratuais específicas, cláusulas-padrão equivalentes ou normas corporativas globais. A alínea "d", selos, certificados e códigos de conduta, ficou fora da Res. 19/2024: o art. 1º da Resolução regulamenta o art. 33, II, apenas nas alíneas "a", "b" e "c". Sobra na prática uma via pronta para uso, as cláusulas-padrão do Anexo II. As cláusulas contratuais específicas existem como mecanismo, mas dependem de aprovação prévia da ANPD, e nenhuma foi aprovada até hoje. O inciso VIII é tecnicamente disponível e frágil: o consentimento é revogável a qualquer tempo e precisa ser distinto do consentimento do art. 11, I.

**Gatilhos.**
- endpoint de provedor em região fora de BR e UE
- variável de configuração de região ausente ou com valor padrão do fornecedor
- SDK sem parâmetro de região explícito na chamada
- contrato com o provedor sem anexo de cláusulas-padrão contratuais
- termo de consentimento sem menção ao caráter internacional da operação

**Relacionados.** LGPD:art5.XV · LGPD:art11 · ANPD-19-2024:art9 · ANPD-19-2024:art16

---

## LGPD:art34

**Ementa.** Critérios de avaliação do nível de proteção do país ou organismo de destino.

**Literal.**
> "Art. 34. O nível de proteção de dados do país estrangeiro ou do organismo internacional mencionado no inciso I do caput do art. 33 desta Lei será avaliado pela autoridade nacional, que levará em consideração:
> I - as normas gerais e setoriais da legislação em vigor no país de destino ou no organismo internacional;
> II - a natureza dos dados;
> III - a observância dos princípios gerais de proteção de dados pessoais e direitos dos titulares previstos nesta Lei;
> IV - a adoção de medidas de segurança previstas em regulamento;
> V - a existência de garantias judiciais e institucionais para o respeito aos direitos de proteção de dados pessoais; e
> VI - outras circunstâncias específicas relativas à transferência."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A avaliação é competência da ANPD. O controlador não pode declarar por conta própria que um país oferece grau adequado de proteção. Vale apenas a lista de decisões de adequação publicadas.

**Gatilhos.**
- documentação interna que afirma adequação de país sem decisão da ANPD

**Relacionados.** ANPD-32-2026:art1

---

## LGPD:art35

**Ementa.** Competência da ANPD sobre cláusulas-padrão, cláusulas específicas, normas corporativas e certificações.

**Literal.**
> "Art. 35. A definição do conteúdo de cláusulas-padrão contratuais, bem como a verificação de cláusulas contratuais específicas para uma determinada transferência, normas corporativas globais ou selos, certificados e códigos de conduta, a que se refere o inciso II do caput do art. 33 desta Lei, será realizada pela autoridade nacional.
> § 1º Para a verificação do disposto no caput deste artigo, deverão ser considerados os requisitos, as condições e as garantias mínimas para a transferência que observem os direitos, as garantias e os princípios desta Lei.
> § 2º Na análise de cláusulas contratuais, de documentos ou de normas corporativas globais submetidas à aprovação da autoridade nacional, poderão ser requeridas informações suplementares ou realizadas diligências de verificação quanto às operações de tratamento, quando necessário.
> § 3º A autoridade nacional poderá designar organismos de certificação para a realização do previsto no caput deste artigo, que permanecerão sob sua fiscalização nos termos definidos em regulamento.
> § 4º Os atos realizados por organismo de certificação poderão ser revistos pela autoridade nacional e, caso em desconformidade com esta Lei, submetidos a revisão ou anulados.
> § 5º As garantias suficientes de observância dos princípios gerais de proteção e dos direitos do titular referidas no caput deste artigo serão também analisadas de acordo com as medidas técnicas e organizacionais adotadas pelo operador, de acordo com o previsto nos §§ 1º e 2º do art. 46 desta Lei."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O conteúdo das cláusulas-padrão é definido pela ANPD, no Anexo II da Res. 19/2024. O §5º liga a suficiência das garantias às medidas técnicas do operador do art. 46: criptografia, controle de acesso e segregação entram na avaliação da transferência.

**Relacionados.** ANPD-19-2024:anexoII · LGPD:art46

---

## LGPD:art36

**Ementa.** Dever de comunicar alterações nas garantias apresentadas.

**Literal.**
> "Art. 36. As alterações nas garantias apresentadas como suficientes de observância dos princípios gerais de proteção e dos direitos do titular referidas no inciso II do art. 33 desta Lei deverão ser comunicadas à autoridade nacional."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Troca de provedor, mudança de região de processamento ou alteração unilateral dos termos pelo fornecedor podem alterar a garantia apresentada. Manter registro datado das versões contratuais e das regiões em uso.

**Gatilhos.**
- ausência de versionamento do contrato ou dos termos do provedor
- mudança de região de processamento sem registro

**Relacionados.** ANPD-19-2024:art4

---

## ANPD-19-2024:art2

**Ementa.** Vigência do Regulamento e prazo de incorporação das cláusulas-padrão.

**Literal.**
> "Art. 2º Esta Resolução entra em vigor na data de sua publicação.
> Parágrafo único. Os agentes de tratamento que utilizam cláusulas contratuais para realizar transferências internacionais de dados deverão incorporar as cláusulas-padrão contratuais aprovadas pela ANPD aos seus respectivos instrumentos contratuais, no prazo de até 12 (doze) meses, contados da data de publicação desta Resolução."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** O prazo de doze meses contados de 23/08/2024 esgotou-se em 23/08/2025. Em agosto de 2026 a obrigação é exigível, e não prospectiva. Contrato de API firmado antes dessa data e nunca aditado está em descumprimento.

**Gatilhos.**
- contrato de provedor anterior a 23/08/2025 sem aditivo de cláusulas-padrão

**Relacionados.** ANPD-19-2024:art16

---

## ANPD-19-2024:art3.III

**Ementa.** Definição de transferência no Regulamento.

**Literal.**
> "Art. 3º [...] III - transferência: operação de tratamento por meio da qual um agente de tratamento transmite, compartilha ou disponibiliza acesso a dados pessoais a outro agente de tratamento;"

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Disponibilizar acesso já é transferência. Conceder credencial de leitura a fornecedor estrangeiro, montar bucket em região externa ou expor banco a suporte remoto se enquadram, mesmo sem cópia de arquivo.

**Gatilhos.**
- concessão de acesso remoto a base de dados para fornecedor estrangeiro
- bucket, índice vetorial ou banco provisionado em região fora de BR e UE
- backup replicado para região externa

**Relacionados.** LGPD:art5.X · LGPD:art5.XV

---

## ANPD-19-2024:art4

**Ementa.** Dever do controlador de verificar a caracterização e o amparo da transferência.

**Literal.**
> "Art. 4º Cabe ao controlador verificar, nos termos da Lei nº 13.709, de 14 de agosto de 2018, e deste Regulamento, se a operação de tratamento: I - caracteriza transferência internacional de dados; II - submete-se à legislação nacional de proteção de dados pessoais; e III - está amparada em hipótese legal e em mecanismo de transferência internacional válidos. [...]"

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A verificação é dever do controlador, com registro. O médico ou a clínica que contrata a ferramenta é o controlador. Manter documento datado que responda aos três incisos para cada provedor em uso.

A transcrição acima cobre o caput e os incisos. O art. 4º tem ainda §§ 1º e 2º, elididos no campo Literal e não transcritos nesta ficha. O §2º é pertinente ao recorte: trata de accountability, com comprovação do cumprimento compatível com o grau de risco da transferência. Obter o texto na fonte antes de citá-lo.

**Gatilhos.**
- ausência de inventário de provedores com região de processamento
- ausência de documento que declare hipótese legal e mecanismo por fluxo

**Relacionados.** LGPD:art37 · LGPD:art38

---

## ANPD-19-2024:art7

**Ementa.** Âmbito de aplicação da legislação nacional à transferência.

**Literal.**
> "Art. 7º A transferência internacional de dados deverá observar as disposições da Lei nº 13.709 [...] quando: I - a operação de tratamento for realizada no território nacional [...]; II - a atividade de tratamento tiver por objetivo a oferta ou o fornecimento de bens ou serviços ou o tratamento de dados de indivíduos localizados no território nacional; ou III - os dados pessoais, objeto do tratamento, forem coletados no território nacional.
> Parágrafo único. A aplicação da legislação nacional à transferência internacional de dados independe do meio utilizado para sua realização, do país de sede dos agentes de tratamento ou do país onde estejam localizados os dados."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O parágrafo único afasta o argumento de que a lei brasileira não se aplica porque o servidor é estrangeiro. Dado coletado no Brasil permanece sob a LGPD qualquer que seja a sede do fornecedor ou o local de armazenamento.

**Gatilhos.**
- documentação interna que invoca lei estrangeira do fornecedor como regime aplicável

**Relacionados.** ANPD-19-2024:art9

---

## ANPD-19-2024:art9

**Ementa.** Requisitos cumulativos: hipótese legal e mecanismo de transferência, com minimização.

**Literal.**
> "Art. 9º A transferência internacional de dados somente poderá ser realizada para atender a propósitos legítimos, específicos, explícitos e informados ao titular, sem possibilidade de tratamento posterior de forma incompatível com essas finalidades, e desde que amparada em: I - uma das hipóteses legais previstas no art. 7º ou no art. 11 da Lei nº 13.709 [...]; e II - um dos seguintes mecanismos válidos de realização da transferência internacional: a) para países ou organismos internacionais que proporcionem grau de proteção de dados pessoais adequado [...] conforme reconhecido por decisão de adequação emitida pela ANPD; b) cláusulas-padrão contratuais, normas corporativas globais ou cláusulas contratuais específicas, na forma deste Regulamento; ou c) nas hipóteses previstas nos incisos II, "d", e III a IX do art. 33 da Lei [...].
> Parágrafo único. A transferência internacional de dados deverá se limitar ao mínimo necessário para o alcance de suas finalidades, com abrangência dos dados pertinentes, proporcionais e não excessivos em relação às finalidades do tratamento de dados."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Os incisos I e II são cumulativos. Para dado de saúde, o inciso I remete ao art. 11, com o rol taxativo. O parágrafo único torna a minimização exigível na própria transferência: enviar o prontuário inteiro quando a tarefa exige três campos descumpre a regra.

**Gatilhos.**
- payload que envia registro completo para tarefa que usa poucos campos
- envio de histórico de conversa acumulado a cada requisição
- ausência de filtro de campos antes da chamada externa

**Relacionados.** LGPD:art11 · LGPD:art33 · ANPD-19-2024:art16

---

## ANPD-19-2024:art16

**Ementa.** Adoção integral e sem alteração das cláusulas-padrão do Anexo II.

**Literal.**
> "Art. 16. A validade da transferência internacional de dados, quando amparada na adoção das cláusulas-padrão, pressupõe a adoção integral e sem alteração do texto disponibilizado no Anexo II, mediante instrumento contratual firmado entre o exportador e o importador."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Cláusula adaptada, resumida ou traduzida invalida o mecanismo. O instrumento precisa ser firmado entre exportador e importador. Um DPA do fornecedor que não incorpore o Anexo II não satisfaz o art. 33, II, "b". A alternativa são cláusulas contratuais específicas aprovadas pela ANPD (arts. 21 a 24 do Regulamento), inviável na prática para médico individual.

**Gatilhos.**
- DPA do fornecedor apresentado como cumprimento do art. 33, II, "b"
- anexo contratual com cláusulas-padrão editadas ou parciais
- ausência de instrumento assinado entre exportador e importador

**Relacionados.** ANPD-19-2024:anexoII · ANPD-19-2024:art2

---

## ANPD-19-2024:art17

**Ementa.** Direito do titular de obter a íntegra das cláusulas utilizadas.

**Literal.**
> "Art. 17. O controlador deverá disponibilizar ao titular, em caso de solicitação, a íntegra das cláusulas utilizadas para a realização da transferência internacional de dados, observados os segredos comercial e industrial."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O paciente pode pedir o texto das cláusulas. Manter cópia acessível do instrumento e do anexo, com processo de atendimento ao pedido.

**Gatilhos.**
- ausência de repositório do contrato acessível ao encarregado
- ausência de fluxo de atendimento a pedido do titular

**Relacionados.** LGPD:art41

---

## ANPD-19-2024:anexoII

**Ementa.** Cláusulas-Padrão Contratuais brasileiras.

**Literal.** Transcrição parcial. O Anexo II tem 24 cláusulas e está publicado na íntegra na URL do campo `fonte`. Estão transcritos abaixo os trechos pertinentes ao recorte desta ficha, com as elisões marcadas.

Cláusula 1, quadros de identificação de papel:
> "( ) Exportador/Controlador ( ) Exportador/Operador"
> [...]
> "( ) Importador/Controlador ( ) Importador/Operador"

Observação que acompanha cada um dos dois quadros:
> "assinalar a opção correspondente a "Controlador" ou "Operador" [...]"

Observação de abertura da Seção II:
> "Esta Seção contém Cláusulas que devem ser adotadas integralmente e sem qualquer alteração em seu texto a fim de assegurar a validade da transferência internacional de dados"

Cláusulas da Seção II pertinentes ao recorte:
> "CLÁUSULA 11. Dados pessoais sensíveis
> 11.1. Caso a Transferência Internacional de Dados envolva Dados Pessoais sensíveis, as Partes aplicarão salvaguardas adicionais, incluindo medidas de segurança específicas e proporcionais aos riscos da atividade de tratamento, à natureza específica dos dados e aos interesses, direitos e garantias a serem protegidos, conforme descrito na Seção III."

> "CLÁUSULA 21. Segurança no tratamento dos dados
> [...]
> 21.2. As Partes informarão, na Seção III, as Medidas de Segurança adotadas, considerando a natureza das informações tratadas, as características específicas e a finalidade do tratamento, o estado atual da tecnologia e os riscos para os direitos dos Titulares, especialmente no caso de dados pessoais sensíveis e de crianças e adolescentes."

> "CLÁUSULA 22. Legislação do país destinatário dos dados
> 22.1. O Importador declara que não identificou leis ou práticas administrativas do país destinatário dos Dados Pessoais que o impeçam de cumprir as obrigações assumidas nestas Cláusulas.
> 22.2. Sobrevindo alteração normativa que altere esta situação, o Importador notificará, de imediato, o Exportador para avaliação da continuidade do contrato."

**Fonte.** https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Estrutura do Anexo II, verificada em 11/08/2026:

- Seção I — Informações Gerais: Cláusula 1 (Identificação das Partes), 2 (Objeto), 3 (Transferências Posteriores, com Opção A e Opção B), 4 (Responsabilidades das Partes).
- Seção II — Cláusulas Mandatórias: 5 (Finalidade), 6 (Definições), 7 (Legislação aplicável e fiscalização da ANPD), 8 (Interpretação), 9 (Possibilidade de adesão de terceiros), 10 (Obrigações gerais das Partes), 11 (Dados pessoais sensíveis), 12 (Dados pessoais de crianças e adolescentes), 13 (Uso legal dos dados), 14 (Transparência), 15 (Direitos do Titular), 16 (Comunicação de Incidente de Segurança), 17 (Responsabilidade e ressarcimento de danos), 18 (Salvaguardas para Transferência Posterior), 19 (Notificação de Solicitação de Acesso), 20 (Término do tratamento e eliminação dos dados), 21 (Segurança no tratamento dos dados), 22 (Legislação do país destinatário dos dados), 23 (Descumprimento das Cláusulas pelo Importador), 24 (Eleição do foro e jurisdição).
- Seção III — Medidas de Segurança. Seção IV — Cláusulas Adicionais e Anexos.

O título oficial da Cláusula 2 é "Objeto". "Descrição da transferência internacional de dados" é o rótulo do quadro a preencher dentro dela.

A marcação de papel é um par. Além do quadro do Exportador, a Cláusula 1 traz o quadro do Importador, com as opções "Importador/Controlador" e "Importador/Operador". Para uso de LLM, o quadro que importa é o do Importador, que é o provedor estrangeiro: assinalá-lo obriga a definir o papel do provedor antes da assinatura, o que reabre a questão da qualificação registrada na ficha 07. Marcar o provedor como operador e conviver com termos que autorizam uso dos inputs para finalidade própria é contradição documental.

A Cláusula 11 exige salvaguardas adicionais quando a transferência envolve dado sensível, descritas na Seção III. A Cláusula 21.2 obriga a descrever as medidas de segurança na Seção III, com menção expressa a dado sensível. As duas são o ponto de contato entre o contrato e a arquitetura: criptografia, controle de acesso e segregação precisam estar escritos no instrumento, não apenas implementados.

A Cláusula 22.1 é declaração do importador de que não identificou leis ou práticas do país de destino que o impeçam de cumprir as cláusulas. Para destino nos Estados Unidos, é a cláusula que concentra o risco de acesso governamental. A 22.2 impõe notificação imediata em caso de alteração normativa.

As demais cláusulas não estão transcritas aqui. Antes de auditar um contrato contra o Anexo II, obter o texto integral na página oficial da Res. 19/2024.

**Relacionados.** ANPD-19-2024:art16 · ANPD-19-2024:art17 · LGPD:art35 · LGPD:art39

---

## ANPD-32-2026:art1

**Ementa.** Reconhecimento da União Europeia como destino adequado.

**Literal.**
> "Art. 1º Fica reconhecida a União Europeia como organismo internacional que proporciona grau de proteção de dados pessoais adequado ao previsto na Lei nº 13.709, de 14 de agosto de 2018, para fins de transferência internacional de dados.
> Parágrafo único. O reconhecimento previsto no caput autoriza a realização de transferências internacionais de dados com base no mecanismo previsto no art. 33, I, da Lei nº 13.709, de 14 de agosto de 2018, para todos os Estados membros da União Europeia, os três países da Associação Europeia de Livre Comércio - AELC que integram o Espaço Econômico Europeu - EEE (Islândia, Liechtenstein e Noruega), bem como as instituições, órgãos e agências da União Europeia, nos termos do Regulamento (UE) 2016/679, da Decisão nº 154/2018, de 6 de julho, do Comitê Misto do EEE, e do Regulamento (UE) 2018/1725."

**Fonte.** https://www.in.gov.br/web/dou/-/resolucao-n-32-de-26-de-janeiro-de-2026-683334547 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** O artigo não impõe dever: abre um mecanismo. A severidade `boa-prática` marca a orientação de escolher região de processamento na UE ou no EEE, e não uma infração por si.

A União Europeia e o EEE são, em 11/08/2026, o único destino com decisão de adequação da ANPD. Não há decisão de adequação para os Estados Unidos. Verificado por leitura integral da página oficial de regulamentações da ANPD, com última modificação registrada em 10/08/2026: a Res. 32/2026 é a única decisão de adequação da lista. A página oficial de Transferência Internacional de Dados da ANPD registra ainda que decisões de adequação emitidas por outros países não são válidas para o Brasil, o que afasta o argumento de que o EU-US Data Privacy Framework aproveitaria ao exportador brasileiro.

Se o processamento ocorrer em região de data center na UE ou no EEE, o art. 33, I fica disponível, o que torna a escolha da região uma decisão jurídica além de técnica. A hipótese do art. 11 continua exigível de qualquer forma.

**Gatilhos.**
- região de processamento configurada em us-east, us-west ou equivalente para fluxo com dado de paciente
- provedor sem oferta de residência de dados na UE ou no EEE
- roteamento automático entre regiões sem fixação por configuração

**Relacionados.** LGPD:art33 · LGPD:art34 · ANPD-19-2024:art9

---

## ANPD-32-2026:art2-art6

**Ementa.** Exclusões da decisão de adequação, monitoramento e reavaliação, não exclusividade dos mecanismos e vigência.

**Literal.** Transcrição parcial dos arts. 2º a 6º. Omitidos o art. 3º, sobre cooperação, e o §2º do art. 4º; as elisões estão marcadas.
> "Art. 2º Esta decisão de adequação não se aplica às transferências internacionais de dados realizadas para fins exclusivos de segurança pública, defesa nacional, segurança do Estado ou atividades de investigação e repressão de infrações penais.
> [...]
> Art. 4º A ANPD realizará monitoramento contínuo do nível de proteção de dados pessoais mantido pela União Europeia, podendo solicitar informações adicionais e realizar avaliações periódicas.
> §1º A decisão de adequação será objeto de reavaliação no prazo de quatro anos, a contar da entrada em vigor desta Resolução.
> [...]
> Art. 5º O disposto nesta decisão de adequação não impede a realização de transferências internacionais de dados para os países referidos no parágrafo único do art. 1º desta Resolução com base nos demais mecanismos de transferência previstos no art. 33 da Lei nº 13.709, de 14 de agosto de 2018.
> Art. 6º Esta Resolução entra em vigor na data de sua publicação."

**Fonte.** https://www.in.gov.br/web/dou/-/resolucao-n-32-de-26-de-janeiro-de-2026-683334547 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O prazo de reavaliação é do art. 4º, §1º, e não do art. 2º. São quatro anos a contar de 27/01/2026, data da publicação no DOU (Edição 18, Seção 1, página 49) e da entrada em vigor pelo art. 6º. 26/01/2026 é a data de assinatura, não o termo inicial. Arquitetura que depende do art. 33, I precisa de reverificação periódica.

As exclusões do art. 2º não alcançam o uso assistencial comum. O art. 5º deixa claro que a decisão de adequação é alternativa, não regime exclusivo: para destino na UE ou no EEE continuam disponíveis os demais mecanismos do art. 33 da LGPD.

Estrutura da Resolução: art. 1º e parágrafo único (reconhecimento); art. 2º (exclusões); art. 3º (cooperação, incisos I a III); art. 4º, caput, §1º e §2º (monitoramento e reavaliação); art. 5º (não exclusividade dos mecanismos); art. 6º (vigência).

**Relacionados.** ANPD-32-2026:art1 · LGPD:art33

---

## Estado da regulamentação em 11/08/2026

Não existe regulamentação da ANPD específica sobre inteligência artificial nem sobre dados de saúde, verificado na página oficial de regulamentações modificada em 10/08/2026. Os dois temas constam apenas da Agenda Regulatória 2025-2026 como ações não concluídas. Não há, portanto, regra própria de transferência internacional para dado de saúde ou para uso de IA: aplica-se o regime geral dos arts. 33 a 36 e da Res. 19/2024.

Não há Guia Orientativo da ANPD sobre IA nem sobre dados de saúde. A lista oficial de Guias Orientativos tem nove títulos, nenhum sobre esses temas. Há documentos técnicos e notas técnicas sobre os dois temas, sem força vinculante, úteis como indicação de leitura da Autoridade; a relação está na seção final da ficha 05.

Decisões de adequação vigentes: uma, a Res. CD/ANPD nº 32/2026, para a União Europeia e o EEE. Não há decisão de adequação para os Estados Unidos. Nenhuma cláusula contratual específica, nenhuma cláusula-padrão equivalente e nenhuma norma corporativa global foi aprovada pelo Conselho Diretor da ANPD até hoje, conforme a página oficial de Transferência Internacional de Dados.

O Anexo II da Res. 19/2024 foi verificado em 11/08/2026 na página oficial da Resolução, onde está publicado na íntegra. A ficha transcreve apenas os trechos pertinentes ao recorte e registra a estrutura completa das 24 cláusulas em ANPD-19-2024:anexoII. As demais cláusulas não estão transcritas neste corpus.
