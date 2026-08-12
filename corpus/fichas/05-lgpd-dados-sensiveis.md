---
norma: Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais)
abrangencia: arts. 5º, 7º, 8º, § 5º, 11, 12, 13, 15, 16, 18 e 20
recorte: definições, dado pessoal sensível, bases legais de dado sensível, revogação do consentimento, anonimização, estudos em saúde pública, término do tratamento, eliminação e conservação, direitos do titular, decisões automatizadas
alteracao: o texto vigente da LGPD foi alterado pela Lei nº 15.352, de 25 de fevereiro de 2026 (conversão da MP 1.317/2025), que deu nova redação aos incisos VIII e XIX do art. 5º, ao título do Capítulo IX, ao art. 55-A e aos incisos V-A e VI do art. 55-C, e incluiu o inciso V-B no art. 55-C. As alterações do art. 5º vêm com a marca (NR), de alteração de dispositivo existente, não de inclusão. A transformação da ANPD em autarquia de natureza especial é anterior e vem da Lei nº 14.460, de 25 de outubro de 2022. Os arts. 5º, II, 8º, 11, 12, 13, 15, 16, 18 e 20 não foram alterados pela Lei 15.352/2026 nem pela MP 1.317/2025 — verificado por varredura das marcações de redação no texto compilado. No art. 18, o inciso V e o § 6º têm redação da Lei nº 13.853, de 2019; os demais dispositivos do artigo são da redação originária. Os arts. 8º, § 5º, 15 e 16 são da redação originária.
vigencia: 24 meses após a publicação quanto aos dispositivos desta ficha (art. 65, II)
status: vinculante
fonte: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15352.htm
verificado: 2026-08-11
origem: corpus/bruto/01_lgpd.md, seções 0 a 4, 10 e 13
---

# LGPD — dado sensível, bases legais, anonimização, pesquisa e decisão automatizada

Esta ficha cobre 21 entradas. Reúne as definições do art. 5º usadas em auditoria, as bases legais do art. 7º, a revogação do consentimento do art. 8º, § 5º, o rol taxativo do art. 11, o teste de anonimização do art. 12, o regime de estudos em saúde pública do art. 13, o término do tratamento do art. 15, a eliminação e as hipóteses de conservação do art. 16, os direitos do titular do art. 18 e o direito de revisão do art. 20.

---

## LGPD:art5.I

**Ementa.** Definição de dado pessoal.

**Literal.**
> "I - dado pessoal: informação relacionada a pessoa natural identificada ou identificável;"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O critério é a identificabilidade, direta ou indireta. Texto clínico sem nome continua sendo dado pessoal quando o titular pode ser identificado por combinação de atributos.

**Relacionados.** LGPD:art5.II · LGPD:art12

---

## LGPD:art5.II

**Ementa.** Definição de dado pessoal sensível.

**Literal.**
> "II - dado pessoal sensível: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural;"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Prontuário, laudo, imagem, exame, prescrição, evolução, resultado genético e biometria de paciente são dado sensível. Basta um elemento que torne o titular identificável — nome, data de nascimento com iniciais, número de registro, contexto raro de caso — para o conteúdo inteiro seguir o regime do art. 11.

**Gatilhos.**
- variável ou coluna: cpf, rg, prontuario, nome_paciente, data_nascimento, cns
- campo de texto livre com evolução, anamnese ou laudo
- dataset de imagem médica com metadado DICOM não removido

**Relacionados.** LGPD:art11 · LGPD:art5.X · CFM-2454-2026:art6

---

## LGPD:art5.III

**Ementa.** Definição de dado anonimizado.

**Literal.**
> "III - dado anonimizado: dado relativo a titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento;"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A definição é datada: o que era anonimizado em uma época pode deixar de ser quando surgem meios técnicos novos. Registrar a data e a técnica da avaliação.

**Relacionados.** LGPD:art12 · LGPD:art5.XI

---

## LGPD:art5.X

**Ementa.** Definição de tratamento.

**Literal.**
> "X - tratamento: toda operação realizada com dados pessoais, como as que se referem a coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação, avaliação ou controle da informação, modificação, comunicação, transferência, difusão ou extração;"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Este inciso é o que subsome o uso de LLM. "Transmissão", "processamento", "comunicação" e "transferência" são, cada um isoladamente, tratamento. Colar texto de prontuário no prompt de um LLM é tratamento de dado pessoal sensível e exige hipótese do art. 11.

**Gatilhos.**
- chamada a API de LLM com payload contendo campo de paciente
- upload de arquivo clínico para serviço de terceiro
- cópia de trecho de prontuário para interface de chat

**Relacionados.** LGPD:art11 · LGPD:art33

---

## LGPD:art5.XI

**Ementa.** Definição de anonimização.

**Literal.**
> "XI - anonimização: utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo;"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A exigência alcança a associação indireta. Remoção de identificadores diretos não satisfaz a definição quando o cruzamento de atributos permite reassociação.

**Relacionados.** LGPD:art12 · LGPD:art13

---

## LGPD:art5.XV

**Ementa.** Definição de transferência internacional de dados.

**Literal.**
> "XV - transferência internacional de dados: transferência de dados pessoais para país estrangeiro ou organismo internacional do qual o país seja membro;"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Chamada a API cujo processamento ocorre fora do Brasil se enquadra na definição. O regime está nos arts. 33 a 36 e na Res. CD/ANPD nº 19/2024, tratados na ficha 06.

**Relacionados.** LGPD:art33 · ANPD-19-2024:art3.III

---

## LGPD:art5.XVIII

**Ementa.** Definição de órgão de pesquisa.

**Literal.**
> "XVIII - órgão de pesquisa: órgão ou entidade da administração pública direta ou indireta ou pessoa jurídica de direito privado sem fins lucrativos legalmente constituída sob as leis brasileiras, com sede e foro no País, que inclua em sua missão institucional ou em seu objetivo social ou estatutário a pesquisa básica ou aplicada de caráter histórico, científico, tecnológico ou estatístico; e (Redação dada pela Lei nº 13.853, de 2019)"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O conceito é fechado e cumulativo. Quando de direito privado, exige pessoa jurídica sem fins lucrativos, constituída sob as leis brasileiras, com sede e foro no País, e finalidade de pesquisa declarada em missão institucional, objetivo social ou estatuto. Clínica privada, consultório, startup e empresa de saúde não são órgão de pesquisa. O art. 13 e a alínea "c" do art. 11, II não amparam, portanto, uso comercial de dado clínico rotulado de "pesquisa interna".

**Gatilhos.**
- invocação do art. 13 ou da alínea "c" do art. 11, II por entidade privada com fins lucrativos
- projeto de "pesquisa interna" em produto comercial usando dado de paciente

**Relacionados.** LGPD:art13 · LGPD:art11.II.f

---

## LGPD:art5.XIX

**Ementa.** Definição de autoridade nacional, com a redação da Lei 15.352/2026.

**Literal.**
> "XIX - autoridade nacional: entidade da administração pública responsável por zelar, implementar e fiscalizar o cumprimento desta Lei em todo o território nacional. (Redação dada pela Lei nº 15.352, de 2026)"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15352.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O inciso existe desde a redação originária da Lei 13.709/2018 e tem cadeia própria de alterações: MP 869/2018, Lei 13.853/2019, MP 1.317/2025 e Lei 15.352/2026. A única alteração de mérito é a troca de "órgão" por "entidade", já introduzida pela MP 1.317/2025 e mantida pela Lei 15.352/2026.

A transformação da ANPD em autarquia de natureza especial é de 2022, pela Lei nº 14.460, de 25 de outubro de 2022. O art. 55-A foi incluído pela Lei 13.853/2019, com redações posteriores da MP 1.124/2022, da Lei 14.460/2022, da MP 1.317/2025 e da Lei 15.352/2026. Documento que descreva a ANPD como órgão da administração pública federal integrante da Presidência da República está desatualizado desde 2022.

Redação vigente do art. 55-A:

> "Art. 55-A. Fica criada a Agência Nacional de Proteção de Dados (ANPD), autarquia de natureza especial vinculada ao Ministério da Justiça e Segurança Pública, dotada de autonomia funcional, técnica, decisória, administrativa e financeira, com patrimônio próprio e com sede e foro no Distrito Federal, nos termos da Lei nº 13.848, de 25 de junho de 2019."

A Lei 15.352/2026 renomeou a entidade de Autoridade para Agência Nacional de Proteção de Dados, explicitou a vinculação ao Ministério da Justiça e Segurança Pública, acrescentou autonomia funcional, administrativa e financeira e submeteu a entidade ao regime das agências reguladoras da Lei 13.848/2019.

Nota de fonte. O texto compilado do Planalto atribui a redação vigente do art. 55-A a "(Redação dada pela Lei nº 15.452, de 2026)". É erro de digitação do compilado: a Lei nº 15.352, de 25/02/2026, art. 1º, traz esse texto com a marca "(NR)". Citar 15.352.

**Relacionados.** LGPD:art52 · ANPD-30-2025:anexo

---

## LGPD:art7

**Ementa.** Bases legais para tratamento de dado pessoal não sensível.

**Literal.**
> "Art. 7º O tratamento de dados pessoais somente poderá ser realizado nas seguintes hipóteses:
> I - mediante o fornecimento de consentimento pelo titular;
> II - para o cumprimento de obrigação legal ou regulatória pelo controlador;
> III - pela administração pública, para o tratamento e uso compartilhado de dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres, observadas as disposições do Capítulo IV desta Lei;
> IV - para a realização de estudos por órgão de pesquisa, garantida, sempre que possível, a anonimização dos dados pessoais;
> V - quando necessário para a execução de contrato ou de procedimentos preliminares relacionados a contrato do qual seja parte o titular, a pedido do titular dos dados;
> VI - para o exercício regular de direitos em processo judicial, administrativo ou arbitral, esse último nos termos da Lei nº 9.307, de 23 de setembro de 1996 (Lei de Arbitragem);
> VII - para a proteção da vida ou da incolumidade física do titular ou de terceiro;
> VIII - para a tutela da saúde, exclusivamente, em procedimento realizado por profissionais de saúde, serviços de saúde ou autoridade sanitária; (Redação dada pela Lei nº 13.853, de 2019)
> IX - quando necessário para atender aos interesses legítimos do controlador ou de terceiro, exceto no caso de prevalecerem direitos e liberdades fundamentais do titular que exijam a proteção dos dados pessoais; ou
> X - para a proteção do crédito, inclusive quanto ao disposto na legislação pertinente."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O rol do art. 7º vale para dado pessoal não sensível. O inciso IX, legítimo interesse, não ampara tratamento de dado sensível, cujo rol é o do art. 11. O art. 33, IX remete aos incisos II, V e VI deste artigo como hipóteses que autorizam transferência internacional — remissão conferida no texto compilado. O art. 9º, II da Res. CD/ANPD nº 19/2024 exige hipótese legal do art. 7º ou do art. 11. O inciso VIII, na redação da Lei 13.853/2019, tem o mesmo conteúdo da alínea "f" do art. 11, II. A diferença é a partícula de abertura: "para a tutela da saúde" no art. 7º, "tutela da saúde" na alínea. Isso reforça o ponto controverso registrado em LGPD:art11.II.f. O art. 7º, VIII é objeto declarado do item 12 da Agenda Regulatória 2025-2026 da ANPD, ainda não editado.

**Incerteza.** Ponto não pacificado nº 2 do material bruto, registrado em LGPD:art11.II.f, tem reflexo aqui: a hipótese do art. 7º não substitui a do art. 11 quando o dado é de saúde.

**Relacionados.** LGPD:art11 · LGPD:art33 · ANPD-19-2024:art9

---

## LGPD:art8§5

**Ementa.** Revogação do consentimento a qualquer momento, por procedimento gratuito e facilitado.

**Literal.**
> "§ 5º O consentimento pode ser revogado a qualquer momento mediante manifestação expressa do titular, por procedimento gratuito e facilitado, ratificados os tratamentos realizados sob amparo do consentimento anteriormente manifestado enquanto não houver requerimento de eliminação, nos termos do inciso VI do caput do art. 18 desta Lei."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O parágrafo é da redação originária. Não recebeu alteração da Lei 13.853/2019, da MP 1.317/2025 nem da Lei 15.352/2026 — conferido nas marcações do texto compilado em 11/08/2026.

A revogação exige manifestação expressa do titular. O procedimento é gratuito e facilitado. A saída não pode custar mais esforço que a entrada. A revogação vale para o futuro: o texto ratifica os tratamentos já realizados sob o consentimento anterior enquanto não houver requerimento de eliminação pelo art. 18, VI.

A revogação alcança o que estava amparado no consentimento. Não alcança o que tem outra base. Quando o mesmo dado de paciente é tratado sob a alínea "f" do art. 11, II, tutela da saúde, ou sob a alínea "a", cumprimento de obrigação legal, o tratamento sob essa base continua depois da revogação. O prontuário permanece sob guarda. Consequência de projeto: cada finalidade precisa ter base legal declarada, e o consentimento precisa estar amarrado às finalidades que dependem dele. Sem esse mapa, o efeito da revogação não é calculável.

Dois comportamentos incorretos aparecem em código. Um é tratar a revogação como apagamento total, o que remove registro sob guarda obrigatória. Outro é registrar a revogação sem efeito no pipeline, o que mantém finalidade sem base. O comportamento esperado é interromper as finalidades que dependiam do consentimento, preservar as demais e registrar o que foi interrompido e quando.

**Gatilhos.**
- ausência de rotina ou de endpoint de revogação de consentimento
- consentimento representado por campo booleano único, sem finalidade e sem versão
- ausência de mapa entre finalidade e base legal no código ou na configuração
- revogação que dispara exclusão em cascata sobre registro clínico
- evento de revogação gravado sem data, sem autor e sem finalidade atingida
- fluxo de revogação com contato manual, formulário em papel ou cobrança

**Relacionados.** LGPD:art11 · LGPD:art15 · LGPD:art18

---

## LGPD:art11

**Ementa.** Rol taxativo de hipóteses de tratamento de dado pessoal sensível.

**Literal.**
> "Art. 11. O tratamento de dados pessoais sensíveis somente poderá ocorrer nas seguintes hipóteses:
> I - quando o titular ou seu responsável legal consentir, de forma específica e destacada, para finalidades específicas;
> II - sem fornecimento de consentimento do titular, nas hipóteses em que for indispensável para:
> a) cumprimento de obrigação legal ou regulatória pelo controlador;
> b) tratamento compartilhado de dados necessários à execução, pela administração pública, de políticas públicas previstas em leis ou regulamentos;
> c) realização de estudos por órgão de pesquisa, garantida, sempre que possível, a anonimização dos dados pessoais sensíveis;
> d) exercício regular de direitos, inclusive em contrato e em processo judicial, administrativo e arbitral, este último nos termos da Lei nº 9.307, de 23 de setembro de 1996 (Lei de Arbitragem);
> e) proteção da vida ou da incolumidade física do titular ou de terceiro;
> f) tutela da saúde, exclusivamente, em procedimento realizado por profissionais de saúde, serviços de saúde ou autoridade sanitária; ou (Redação dada pela Lei nº 13.853, de 2019)
> g) garantia da prevenção à fraude e à segurança do titular, nos processos de identificação e autenticação de cadastro em sistemas eletrônicos, resguardados os direitos mencionados no art. 9º desta Lei e exceto no caso de prevalecerem direitos e liberdades fundamentais do titular que exijam a proteção dos dados pessoais."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** O rol é taxativo. Legítimo interesse não entra. Não há base legal para "melhorar o fluxo de trabalho com IA". O inciso I exige consentimento específico e destacado, por finalidade: cláusula genérica em contrato de prestação de serviço ou menção a "uso de tecnologias" não satisfaz. O consentimento é revogável (art. 8º, §5º), o que é operacionalmente incompatível com dado já ingerido em treinamento de modelo. Todo fluxo que envia dado de paciente a um LLM precisa indicar por escrito qual inciso ampara o tratamento.

**Gatilhos.**
- ausência de campo ou de documento que registre a base legal por finalidade
- termo de consentimento único cobrindo finalidades múltiplas
- consentimento sem mecanismo de revogação implementado
- pipeline de treinamento alimentado por dado de paciente

**Relacionados.** LGPD:art11.II.f · LGPD:art11§4 · LGPD:art12 · CFM-2454-2026:art6

---

## LGPD:art11.II.f

**Ementa.** Base de tutela da saúde, restrita ao procedimento realizado por profissional de saúde, serviço de saúde ou autoridade sanitária.

**Literal.**
> "f) tutela da saúde, exclusivamente, em procedimento realizado por profissionais de saúde, serviços de saúde ou autoridade sanitária; ou (Redação dada pela Lei nº 13.853, de 2019)"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** A Lei 13.853/2019 acrescentou o advérbio "exclusivamente" e substituiu "entidades sanitárias" por "serviços de saúde ou autoridade sanitária". A redação revogada, transcrita aqui só para contraste e sem valor de texto vigente, era:

> "f) tutela da saúde, em procedimento realizado por profissionais da área da saúde ou por entidades sanitárias; ou"

A base cobre o tratamento dentro do procedimento de cuidado. É defensável enquadrar o uso de LLM como ferramenta dentro do ato assistencial, por exemplo a sumarização de prontuário pelo próprio médico assistente para conduzir o caso. O alcance da base para amparar a remessa do dado a um terceiro tecnológico estrangeiro é controverso — ver Incerteza.

**Gatilhos.**
- uso de dado de paciente fora de ato assistencial, com invocação da alínea "f"
- fluxo administrativo, comercial ou de marketing amparado na alínea "f"
- remessa a fornecedor que não é profissional nem serviço de saúde, sem outra base declarada

**Incerteza.** Ponto não pacificado nº 2 do material bruto. Leitura restritiva: a base cobre o ato assistencial e seus prestadores, sem alcançar a cadeia de fornecedores de tecnologia. Leitura ampliativa: o operador atua em nome do profissional e a base do controlador se estende à cadeia. Nenhum ato da ANPD verificado até 11/08/2026 enfrenta a questão. O item 12 da Agenda Regulatória 2025-2026 declara a alínea "f" como objeto de ação regulatória futura.

**Relacionados.** LGPD:art11 · LGPD:art33 · CFM-2454-2026:art6

---

## LGPD:art11§1-§3

**Ementa.** Extensão a dados que revelem dado sensível, publicidade da dispensa e competência da ANPD sobre compartilhamento com vantagem econômica.

**Literal.**
> "§ 1º Aplica-se o disposto neste artigo a qualquer tratamento de dados pessoais que revele dados pessoais sensíveis e que possa causar dano ao titular, ressalvado o disposto em legislação específica."
> "§ 2º Nos casos de aplicação do disposto nas alíneas “a” e “b” do inciso II do caput deste artigo pelos órgãos e pelas entidades públicas, será dada publicidade à referida dispensa de consentimento, nos termos do inciso I do caput do art. 23 desta Lei."
> "§ 3º A comunicação ou o uso compartilhado de dados pessoais sensíveis entre controladores com objetivo de obter vantagem econômica poderá ser objeto de vedação ou de regulamentação por parte da autoridade nacional, ouvidos os órgãos setoriais do Poder Público, no âmbito de suas competências."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O §1º alcança dado que apenas revela condição de saúde, como agendamento em serviço de especialidade, código de procedimento ou nome de medicamento. O §3º é a competência que fundamenta o item 12 da Agenda Regulatória; até 11/08/2026 a ANPD não editou essa regulamentação.

**Gatilhos.**
- tabela de agendamento com especialidade ou CID tratada como dado não sensível
- log de faturamento com código de procedimento fora do regime de dado sensível

**Relacionados.** LGPD:art11§4

---

## LGPD:art11§4

**Ementa.** Vedação de comunicação ou uso compartilhado de dado de saúde entre controladores com objetivo de vantagem econômica.

**Literal.**
> "§ 4º É vedada a comunicação ou o uso compartilhado entre controladores de dados pessoais sensíveis referentes à saúde com objetivo de obter vantagem econômica, exceto nas hipóteses relativas a prestação de serviços de saúde, de assistência farmacêutica e de assistência à saúde, desde que observado o § 5º deste artigo, incluídos os serviços auxiliares de diagnose e terapia, em benefício dos interesses dos titulares de dados, e para permitir: (Redação dada pela Lei nº 13.853, de 2019)
> I - a portabilidade de dados quando solicitada pelo titular; ou (Incluído pela Lei nº 13.853, de 2019)
> II - as transações financeiras e administrativas resultantes do uso e da prestação dos serviços de que trata este parágrafo. (Incluído pela Lei nº 13.853, de 2019)"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** A exceção é estreita: prestação de serviços de saúde, assistência farmacêutica e assistência à saúde, e apenas para portabilidade a pedido do titular ou para transações financeiras e administrativas. Se o provedor do LLM figurar como controlador — o que ocorre quando usa os inputs para finalidade própria, como treinar ou melhorar o modelo — a remessa de dado de saúde a ele em contrato oneroso tende a se enquadrar na vedação. Este é um dos pontos de maior exposição jurídica do médico. A qualificação do provedor é tratada em LGPD:art39 e na incerteza registrada na ficha 07.

**Gatilhos.**
- termos do provedor que autorizam uso dos inputs para treinamento
- contrato sem cláusula de finalidade restrita às instruções do controlador
- envio de dado de paciente a serviço gratuito ou de consumidor

**Relacionados.** LGPD:art39 · LGPD:art42 · ANPD-19-2024:art9

---

## LGPD:art11§5

**Ementa.** Vedação de seleção de riscos por operadoras de planos privados de assistência à saúde.

**Literal.**
> "§ 5º É vedado às operadoras de planos privados de assistência à saúde o tratamento de dados de saúde para a prática de seleção de riscos na contratação de qualquer modalidade, assim como na contratação e exclusão de beneficiários. (Incluído pela Lei nº 13.853, de 2019)"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A vedação é expressa, mas recai sobre a operadora de plano privado, não sobre o médico nem sobre o sistema auditado. Por isso a severidade aqui é `risco` com gatilho específico: a ficha só é acionada quando o fluxo exporta saída de modelo para operadora. Quem exporta escore, estratificação ou predição para operadora precisa declarar a finalidade e vedar em contrato o uso em seleção de riscos. Tratada como `bloqueante` de forma genérica, esta entrada produz falso positivo de alta severidade em auditoria de código de consultório ou de clínica.

**Gatilhos.**
- exportação de escore de risco de paciente para operadora de plano
- integração com sistema de underwriting alimentada por dado clínico

**Relacionados.** LGPD:art20 · LGPD:art11§4

---

## LGPD:art12

**Ementa.** Dados anonimizados fora do alcance da Lei, com teste de reversibilidade.

**Literal.**
> "Art. 12. Os dados anonimizados não serão considerados dados pessoais para os fins desta Lei, salvo quando o processo de anonimização ao qual foram submetidos for revertido, utilizando exclusivamente meios próprios, ou quando, com esforços razoáveis, puder ser revertido.
> § 1º A determinação do que seja razoável deve levar em consideração fatores objetivos, tais como custo e tempo necessários para reverter o processo de anonimização, de acordo com as tecnologias disponíveis, e a utilização exclusiva de meios próprios.
> § 2º Poderão ser igualmente considerados como dados pessoais, para os fins desta Lei, aqueles utilizados para formação do perfil comportamental de determinada pessoa natural, se identificada.
> § 3º A autoridade nacional poderá dispor sobre padrões e técnicas utilizados em processos de anonimização e realizar verificações acerca de sua segurança, ouvido o Conselho Nacional de Proteção de Dados Pessoais."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** É a única porta de saída limpa para uso de LLM: dado genuinamente anonimizado fica fora da LGPD. O teste é de reversibilidade com esforços razoáveis, medido por custo, tempo e tecnologias disponíveis. Em texto clínico livre, remover nome e CPF não basta: a combinação de idade, data de internação, hospital e doença rara é reidentificável. A Lei não define percentual, técnica nem padrão. O §3º delega à ANPD, que até 11/08/2026 não editou a regulamentação — é o item 9 da Agenda Regulatória 2025-2026, Fase 1. Quem anonimiza carrega o ônus de demonstrar a irreversibilidade. Pseudonimização (art. 13, §4º) permanece integralmente sob a LGPD.

Documentos técnicos da ANPD sobre o tema, orientativos e não vinculantes: "Estudo técnico sobre anonimização de dados na LGPD — análise jurídica" (nov/2023), "…visão de processo baseado em risco e técnicas computacionais" (nov/2023) e "Estudos de casos sobre anonimização de dados na LGPD" (set/2023), em https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos

**Gatilhos.**
- função de desidentificação que remove apenas identificadores diretos
- tabela de correspondência entre pseudônimo e identidade no mesmo banco ou no mesmo repositório
- ausência de teste de reidentificação documentado
- variável de data completa, CEP completo ou identificador de unidade preservados em base dita anonimizada
- texto livre enviado a LLM sem etapa de desidentificação

**Incerteza.** Ponto não pacificado nº 3 do material bruto: se um prompt com texto clínico desidentificado é ou não dado pessoal. A resposta depende do teste do §1º, cujos padrões técnicos a ANPD não editou. Leitura conservadora: tratar como dado pessoal enquanto não houver teste de reidentificação documentado. Leitura permissiva: considerar anonimizado após remoção dos identificadores previstos em padrão técnico adotado. O ônus prático recai sobre o agente.

**Relacionados.** LGPD:art5.XI · LGPD:art13 · CFM-2454-2026:anexoI.XV-XVI

---

## LGPD:art13

**Ementa.** Estudos em saúde pública por órgão de pesquisa, com vedação de transferência a terceiro.

**Literal.**
> "Art. 13. Na realização de estudos em saúde pública, os órgãos de pesquisa poderão ter acesso a bases de dados pessoais, que serão tratados exclusivamente dentro do órgão e estritamente para a finalidade de realização de estudos e pesquisas e mantidos em ambiente controlado e seguro, conforme práticas de segurança previstas em regulamento específico e que incluam, sempre que possível, a anonimização ou pseudonimização dos dados, bem como considerem os devidos padrões éticos relacionados a estudos e pesquisas.
> § 1º A divulgação dos resultados ou de qualquer excerto do estudo ou da pesquisa de que trata o caput deste artigo em nenhuma hipótese poderá revelar dados pessoais.
> § 2º O órgão de pesquisa será o responsável pela segurança da informação prevista no caput deste artigo, não permitida, em circunstância alguma, a transferência dos dados a terceiro.
> § 3º O acesso aos dados de que trata este artigo será objeto de regulamentação por parte da autoridade nacional e das autoridades da área de saúde e sanitárias, no âmbito de suas competências.
> § 4º Para os efeitos deste artigo, a pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** É o dispositivo mais restritivo do conjunto para uso de LLM em pesquisa. O caput impõe três exigências cumulativas: tratamento exclusivamente dentro do órgão, em ambiente controlado e seguro, com anonimização ou pseudonimização sempre que possível. O §2º veda a transferência a terceiro em circunstância alguma. Enviar dados de base de pesquisa em saúde pública a uma API de LLM operada por terceiro é transferência a terceiro na leitura literal. O quadro favorece arquitetura de modelo local ou on-premise para pesquisa.

O artigo só alcança quem é órgão de pesquisa na definição do art. 5º, XVIII, transcrita em LGPD:art5.XVIII. Quando de direito privado, o conceito exige pessoa jurídica sem fins lucrativos, constituída sob as leis brasileiras, com sede e foro no País, e finalidade de pesquisa em missão institucional, objetivo social ou estatuto. Clínica, consultório e empresa de saúde não se enquadram e não podem invocar o art. 13 nem a alínea "c" do art. 11, II para uso comercial de dado clínico rotulado de "pesquisa interna".

A regulamentação conjunta prevista no §3º não foi editada até 11/08/2026. Há Guia Orientativo da ANPD pertinente ao tema — "Tratamento de dados pessoais para fins acadêmicos e para a realização de estudos e pesquisas" —, orientativo e sem força vinculante.

**Gatilhos.**
- base de pesquisa em saúde pública com egresso de rede para provedor externo
- notebook de análise que chama API de LLM sobre coorte identificada
- exportação de dataset de estudo para serviço de terceiro
- ausência de segregação de ambiente entre pesquisa e produção

**Incerteza.** Ponto não pacificado nº 4 do material bruto. Leitura literal: "terceiro" abrange qualquer entidade externa ao órgão, o que veda a API de LLM de forma absoluta. Leitura alternativa: "terceiro" não abarca operador contratado que trate os dados sob instruções do órgão. Não pacificado; o risco na leitura literal é alto.

**Relacionados.** LGPD:art11.II.f · LGPD:art12 · LGPD:art33

---

## LGPD:art15

**Ementa.** Hipóteses de término do tratamento de dados pessoais.

**Literal.**
> "Art. 15. O término do tratamento de dados pessoais ocorrerá nas seguintes hipóteses:
> I - verificação de que a finalidade foi alcançada ou de que os dados deixaram de ser necessários ou pertinentes ao alcance da finalidade específica almejada;
> II - fim do período de tratamento;
> III - comunicação do titular, inclusive no exercício de seu direito de revogação do consentimento conforme disposto no § 5º do art. 8º desta Lei, resguardado o interesse público; ou
> IV - determinação da autoridade nacional, quando houver violação ao disposto nesta Lei."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Texto da redação originária, sem alteração posterior — conferido nas marcações do compilado em 11/08/2026.

O artigo define quando o tratamento termina. Não fixa prazo. O prazo decorre da finalidade declarada, pelo inciso I, ou do período de tratamento que o próprio agente definiu, pelo inciso II. Sistema que guarda dado de paciente sem finalidade declarada e sem período definido não tem como identificar o término. Sem término identificado, o dever de eliminação do art. 16 não é executável.

Este é o dispositivo que transforma retenção indefinida em achado objetivo de auditoria. O ponto de verificação é a existência de uma definição de término no código, no contrato ou na política. Bucket sem regra de ciclo de vida, tabela sem coluna de expiração, índice vetorial sem descarte e histórico de conversa mantido no provedor sem prazo são casos de término indefinido.

O inciso III liga a revogação do consentimento ao término do tratamento. A ressalva do interesse público não é cláusula de conveniência do controlador. O inciso II exige que o período de tratamento exista como parâmetro declarado, e não como efeito colateral da infraestrutura.

**Gatilhos.**
- ausência de definição de término do tratamento em código, contrato ou política
- retenção sem prazo declarado
- bucket, tabela ou coleção sem política de ciclo de vida
- índice vetorial, cache de embeddings ou histórico de sessão sem rotina de descarte
- base rotulada como temporária, de teste ou de staging, sem data de descarte
- evento de revogação do titular sem efeito sobre o pipeline

**Relacionados.** LGPD:art8§5 · LGPD:art16 · LGPD:art18

---

## LGPD:art16

**Ementa.** Eliminação dos dados após o término do tratamento e hipóteses de conservação.

**Literal.**
> "Art. 16. Os dados pessoais serão eliminados após o término de seu tratamento, no âmbito e nos limites técnicos das atividades, autorizada a conservação para as seguintes finalidades:
> I - cumprimento de obrigação legal ou regulatória pelo controlador;
> II - estudo por órgão de pesquisa, garantida, sempre que possível, a anonimização dos dados pessoais;
> III - transferência a terceiro, desde que respeitados os requisitos de tratamento de dados dispostos nesta Lei; ou
> IV - uso exclusivo do controlador, vedado seu acesso por terceiro, e desde que anonimizados os dados."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Texto da redação originária, sem alteração posterior — conferido nas marcações do compilado em 11/08/2026.

A regra é a eliminação após o término. A conservação é exceção e depende de uma das quatro finalidades do rol. Quem conserva precisa indicar qual inciso ampara a conservação, por base e por finalidade.

Interação com o prontuário. A guarda do prontuário se apoia no inciso I, cumprimento de obrigação legal ou regulatória. O prazo dessa guarda não está na LGPD. Vem de norma do CFM e de lei específica: guarda permanente para o prontuário arquivado em meio óptico, microfilmado ou digitalizado, pela Res. CFM 1.821/2007, art. 7º, e prazo mínimo de 20 anos a partir do último registro para o papel não arquivado eletronicamente, pelo art. 8º da mesma resolução. A Lei 13.787/2018 dispõe sobre eliminação após 20 anos do último registro, e a tensão com a guarda permanente está registrada em CFM-1821-2007:art7. A LGPD autoriza a conservação; o prazo é fixado fora dela. Política de retenção que declara um "prazo da LGPD" para prontuário está errada na origem.

O inciso I ampara o prontuário e o que a ele se integra por norma do CFM. Não ampara cópia derivada. Prompt enviado ao provedor, saída de modelo não incorporada ao prontuário, log de requisição, cache, planilha de apoio e base de treinamento não têm obrigação legal de guarda. Esses artefatos seguem a regra da eliminação, com prazo próprio e mais curto que o do registro clínico.

O inciso IV autoriza uso exclusivo do controlador, com acesso de terceiro vedado e dado anonimizado. Não ampara envio a API de terceiro nem base pseudonimizada cuja chave de reversão esteja acessível. A expressão "no âmbito e nos limites técnicos das atividades" qualifica a execução da eliminação, e não dispensa o dever quando a eliminação é apenas trabalhosa.

**Gatilhos.**
- ausência de rotina de eliminação após o término do tratamento
- conservação invocada sem indicação do inciso do art. 16 que a ampara
- expurgo que alcança o banco primário e não alcança backup, réplica, log, fila ou cache
- prompt, saída de modelo e log de requisição retidos sob o mesmo prazo do registro clínico
- política de retenção que atribui à LGPD o prazo de guarda do prontuário
- base descrita como anonimizada, conservada pelo inciso IV, com tabela de reversão no mesmo ambiente
- conservação para "estudo" pelo inciso II em entidade que não é órgão de pesquisa

**Incerteza.** O art. 16 remete o prazo da conservação à obrigação legal ou regulatória, e essa obrigação, no caso do prontuário, não é pacífica. Leitura 1: guarda permanente, pela Res. CFM 1.821/2007, art. 7º. Leitura 2: eliminação possível após 20 anos do último registro, pelo art. 6º da Lei 13.787/2018. As duas posições estão registradas em CFM-1821-2007:art7. Em auditoria, adotar a guarda permanente como regra de projeto e registrar a tensão quando o prazo de 20 anos for invocado.

**Relacionados.** LGPD:art15 · LGPD:art18 · LGPD:art5.XVIII · CFM-1821-2007:art7 · CFM-1821-2007:art8

---

## LGPD:art18

**Ementa.** Direitos do titular e deveres de atendimento do requerimento.

**Literal.**
> "Art. 18. O titular dos dados pessoais tem direito a obter do controlador, em relação aos dados do titular por ele tratados, a qualquer momento e mediante requisição:
> I - confirmação da existência de tratamento;
> II - acesso aos dados;
> III - correção de dados incompletos, inexatos ou desatualizados;
> IV - anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade com o disposto nesta Lei;
> V - portabilidade dos dados a outro fornecedor de serviço ou produto, mediante requisição expressa, de acordo com a regulamentação da autoridade nacional, observados os segredos comercial e industrial; (Redação dada pela Lei nº 13.853, de 2019)
> VI - eliminação dos dados pessoais tratados com o consentimento do titular, exceto nas hipóteses previstas no art. 16 desta Lei;
> VII - informação das entidades públicas e privadas com as quais o controlador realizou uso compartilhado de dados;
> VIII - informação sobre a possibilidade de não fornecer consentimento e sobre as consequências da negativa;
> IX - revogação do consentimento, nos termos do § 5º do art. 8º desta Lei.
> § 1º O titular dos dados pessoais tem o direito de peticionar em relação aos seus dados contra o controlador perante a autoridade nacional.
> § 2º O titular pode opor-se a tratamento realizado com fundamento em uma das hipóteses de dispensa de consentimento, em caso de descumprimento ao disposto nesta Lei.
> § 3º Os direitos previstos neste artigo serão exercidos mediante requerimento expresso do titular ou de representante legalmente constituído, a agente de tratamento.
> § 4º Em caso de impossibilidade de adoção imediata da providência de que trata o § 3º deste artigo, o controlador enviará ao titular resposta em que poderá:
> I - comunicar que não é agente de tratamento dos dados e indicar, sempre que possível, o agente; ou
> II - indicar as razões de fato ou de direito que impedem a adoção imediata da providência.
> § 5º O requerimento referido no § 3º deste artigo será atendido sem custos para o titular, nos prazos e nos termos previstos em regulamento.
> § 6º O responsável deverá informar, de maneira imediata, aos agentes de tratamento com os quais tenha realizado uso compartilhado de dados a correção, a eliminação, a anonimização ou o bloqueio dos dados, para que repitam idêntico procedimento, exceto nos casos em que esta comunicação seja comprovadamente impossível ou implique esforço desproporcional. (Redação dada pela Lei nº 13.853, de 2019)
> § 7º A portabilidade dos dados pessoais a que se refere o inciso V do caput deste artigo não inclui dados que já tenham sido anonimizados pelo controlador.
> § 8º O direito a que se refere o § 1º deste artigo também poderá ser exercido perante os organismos de defesa do consumidor."

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Duas alterações no artigo, ambas da Lei 13.853/2019 e ambas conferidas no compilado em 11/08/2026: no inciso V, a remissão passou de "regulamentação do órgão controlador" para "regulamentação da autoridade nacional"; o §6º recebeu nova redação. O caput, os demais incisos e os demais parágrafos são da redação originária.

O artigo cria obrigações operacionais, e não apenas direitos declarados. O exercício depende de requerimento expresso do titular ou de representante legalmente constituído, pelo §3º. O atendimento é sem custos, nos prazos e termos de regulamento, pelo §5º. Quando a providência imediata é impossível, o controlador responde indicando as razões de fato ou de direito, pelo §4º, II. O §6º impõe propagar correção, eliminação, anonimização e bloqueio aos agentes com quem houve uso compartilhado. Em arquitetura com operador externo, o pedido do titular precisa alcançar o provedor, o backup e a réplica, e o controlador precisa saber a quem o dado foi compartilhado, o que o inciso VII também exige.

Eliminação diante da guarda obrigatória. O inciso VI é limitado no próprio texto: alcança os dados tratados com o consentimento do titular e ressalva as hipóteses do art. 16. Dado de prontuário conservado por obrigação legal de guarda não é eliminado a pedido do titular. A resposta adequada não é o silêncio nem o apagamento. É a negativa fundamentada, com a razão de direito registrada na forma do §4º, II, e o registro do pedido e da resposta. Recusa sem fundamentação e apagamento indevido de registro clínico são falhas de naturezas diferentes, e as duas aparecem em produção.

O inciso IV tem alcance maior que o do inciso VI e é o mais aplicável a fluxo de IA. Ele cobre anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade, sem depender de o tratamento ter base no consentimento. Cópia de prontuário em prompt, log de payload e dataset montado sem base declarada caem nessa hipótese, mesmo quando o atendimento assistencial está amparado no art. 11, II, "f".

O art. 18 é objeto do item 1 da Agenda Regulatória 2025-2026 da ANPD, "Direitos dos titulares", que aponta os arts. 9º, 18, 19 e 20 como pontos a regulamentar. Em consulta de 11/08/2026 à página oficial de regulamentações da ANPD, não foi localizada regulamentação dos prazos a que se refere o §5º.

**Gatilhos.**
- ausência de rotina de atendimento a pedido do titular
- ausência de canal declarado para requerimento e de prazo de resposta
- pedido atendido apenas no banco primário, sem propagação a operador, backup, réplica, log e índice
- ausência de registro de com quais agentes o dado foi compartilhado
- cobrança ou exigência de deslocamento para atendimento do requerimento
- eliminação total acionada por pedido do titular, sem verificação das hipóteses do art. 16
- negativa de eliminação sem razão de direito registrada
- exportação de portabilidade que inclui dado já anonimizado pelo controlador

**Incerteza.** O inciso VI ressalva o art. 16, e o art. 16, I, ampara a guarda obrigatória do prontuário. O ponto não resolvido é o alcance dessa ressalva. Leitura restritiva: ela cobre o prontuário e o que é necessário ao cumprimento da obrigação de guarda; cópias derivadas, prompts, logs, caches e bases auxiliares permanecem elimináveis a pedido. Leitura ampla: incidindo obrigação legal de guarda sobre o atendimento, todo o conjunto de dados daquele atendimento fica conservado. Não foi localizado ato da ANPD nem do CFM enfrentando a questão até 11/08/2026. Soma-se a divergência sobre o próprio prazo de guarda, registrada em CFM-1821-2007:art7. Em auditoria, adotar a leitura restritiva: conservar o prontuário e eliminar o derivado.

**Relacionados.** LGPD:art8§5 · LGPD:art15 · LGPD:art16 · LGPD:art20 · CFM-1821-2007:art7

---

## LGPD:art20

**Ementa.** Direito de revisão de decisões tomadas unicamente com base em tratamento automatizado.

**Literal.**
> "Art. 20. O titular dos dados tem direito a solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado de dados pessoais que afetem seus interesses, incluídas as decisões destinadas a definir o seu perfil pessoal, profissional, de consumo e de crédito ou os aspectos de sua personalidade. (Redação dada pela Lei nº 13.853, de 2019)
> § 1º O controlador deverá fornecer, sempre que solicitadas, informações claras e adequadas a respeito dos critérios e dos procedimentos utilizados para a decisão automatizada, observados os segredos comercial e industrial.
> § 2º Em caso de não oferecimento de informações de que trata o § 1º deste artigo baseado na observância de segredo comercial e industrial, a autoridade nacional poderá realizar auditoria para verificação de aspectos discriminatórios em tratamento automatizado de dados pessoais.
> § 3º (VETADO). (Incluído pela Lei nº 13.853, de 2019)"

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A redação original previa revisão "por pessoa natural". A Lei 13.853/2019 retirou a expressão, e o §3º, que a reinseriria, foi vetado. Citar "revisão por pessoa natural" como texto vigente é erro. O artigo incide sobre decisões tomadas unicamente com base em tratamento automatizado. Enquanto o médico mantém decisão própria e o LLM opera como apoio, o art. 20 tende a não incidir, o que sustenta juridicamente a arquitetura com revisão humana registrada. Sistema que emite triagem, priorização ou negativa sem intervenção médica aciona o art. 20.

Quanto ao enquadramento como alto risco, o art. 4º da Res. CD/ANPD nº 2/2022 exige combinação:

> "Art. 4º Para fins deste regulamento, e sem prejuízo do disposto no art. 16, será considerado de alto risco o tratamento de dados pessoais que atender cumulativamente a pelo menos um critério geral e um critério específico [...]"

A alínea "c" do inciso II é critério específico e sozinha não caracteriza alto risco: exige também um critério geral, larga escala ou afetação significativa de interesses e direitos fundamentais. O enquadramento vale "para fins deste regulamento", que é o Regulamento de aplicação da LGPD para agentes de tratamento de pequeno porte. Em fluxo com dado de paciente, a alínea "d" do mesmo inciso, utilização de dados pessoais sensíveis, já basta como critério específico.

**Gatilhos.**
- fluxo que aplica saída de modelo sem etapa humana obrigatória
- triagem, priorização de fila ou negativa gerada por modelo
- ausência de canal para o titular pedir revisão
- ausência de documentação dos critérios da decisão automatizada

**Incerteza.** Ponto não pacificado nº 5 do material bruto: se o uso de LLM como apoio configura decisão tomada unicamente com base em tratamento automatizado quando o médico homologa a sugestão sem crítica. Leitura formal: havendo etapa humana, o art. 20 não incide. Leitura material: supervisão meramente formal é desconsiderada e o art. 20 incide. Não há parâmetro regulatório. O art. 20 é objeto declarado de dois itens da Agenda Regulatória 2025-2026, ambos em Fase 1 e ambos pendentes: o item 6, "Inteligência Artificial", que prevê o estabelecimento de parâmetros interpretativos para a aplicação do art. 20, e o item 1, "Direitos dos titulares", que aponta os arts. 9º, 18, 19 e 20 como pontos a regulamentar.

**Relacionados.** ANPD-2-2022:art4 · CFM-2454-2026:art15 · CFM-2454-2026:art18

---

## Estado da regulamentação em 11/08/2026

Verificado na página oficial de regulamentações da ANPD, modificada em 10/08/2026: não existe regulamentação da ANPD específica sobre inteligência artificial nem sobre dados de saúde. Os dois temas constam apenas da Agenda Regulatória 2025-2026 (Res. CD/ANPD nº 23/2024, com a redação da Res. CD/ANPD nº 31/2025), como ações não concluídas — item 6, "Inteligência Artificial", Fase 1, e item 12, "Dados pessoais sensíveis: dados de saúde", Fase 2.

Não há Guia Orientativo da ANPD sobre IA nem sobre dados de saúde. A lista oficial de Guias Orientativos tem nove títulos, nenhum sobre esses temas. Há documentos técnicos e notas técnicas sobre os dois temas, sem força vinculante, úteis como indicação de leitura da Autoridade:

- IA: "Radar Tecnológico nº 3 — IA Generativa"; Nota Técnica nº 27/2024/FIS/CGF/ANPD, tratamento de dados de terceiros para desenvolver modelo de IA generativa; Nota Técnica nº 39/2024/FIS/ANPD, plano de conformidade para treinamento de modelos de IA generativa; Nota Técnica nº 1/2026/FIS/CGF/ANPD, sistema de IA Grok e possíveis violações à LGPD; Nota Técnica nº 16/2023/CGTP/ANPD, subsídios ao PL 2338/2023.
- Saúde: Nota Técnica nº 4/2023/CGTP/ANPD, farmácias.

Guia Orientativo pertinente ao art. 13 e à alínea "c" do art. 11, II: "Tratamento de dados pessoais para fins acadêmicos e para a realização de estudos e pesquisas". Também orientativo, sem força vinculante.

Listas oficiais em https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos e https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes

Pendências de regulamentação que afetam esta ficha: art. 12, §3º (padrões de anonimização, item 9 da Agenda, Fase 1); art. 13, §3º (acesso a dados para estudos em saúde pública, regulamentação conjunta com autoridades sanitárias); art. 18, §5º (prazos e termos de atendimento do requerimento do titular, item 1 da Agenda, "Direitos dos titulares"); art. 20 (parâmetros de revisão de decisão automatizada, item 6 da Agenda).

Não existe, em 11/08/2026, lei brasileira geral de inteligência artificial em vigor — ver ficha 08, PL-2338-2023:status.
