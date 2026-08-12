---
norma: Código Penal — Decreto-Lei nº 2.848, de 7 de dezembro de 1940 (texto compilado)
ementa: Tipos penais aplicáveis à quebra de sigilo de dado de paciente e ao acesso indevido a sistema
abrangencia: arts. 153, 154, 154-A, 154-B, 325 e 327
status: vigente
fonte: https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm
verificado: 2026-08-11
origem: corpus/bruto/03_penal_civil.md — download direto do HTML de planalto.gov.br, transcrição literal
auditado: o texto compilado traz alterações até a Lei nº 15.487/2026. Varredura das leis alteradoras de 2021 a 2026 confirmou que nenhuma delas alterou os arts. 153, 154, 154-A, 154-B, 325 ou 327
revisao: reauditoria adversarial independente em 2026-08-11, feita direto do HTML de planalto.gov.br. Os cinco campos Literal foram conferidos palavra por palavra, com penas, remissões de alteração e marcação de texto revogado. Conferidas também a prescrição do art. 153 (art. 109, VI) e a do art. 154 (art. 109, V), a decadência do art. 103, o art. 2º da Lei 7.209/1984, o art. 61 da Lei 9.099/1995 e o art. 10 da Lei 9.296/1996. Um erro corrigido: a pena do art. 155, §4º-B, citada no delta da Lei 14.155/2021, foi alterada pela Lei nº 15.397/2026. Campos Fonte e Confiança acrescentados a todas as entradas
---

# Código Penal — segredo, invasão de dispositivo e sigilo funcional

Cinco entradas e seis dispositivos: o art. 154-B é transcrito na entrada do art. 154-A. Toda a repressão penal ao vazamento de dado de saúde no Brasil é feita por tipos anteriores à IA generativa: 1940 (arts. 153 caput, 154, 325 caput), 2000 (art. 153, §§1º-A e 2º; art. 325, §§1º e 2º; art. 327, §1º), 2012 (art. 154-A) e 2021 (redação vigente do art. 154-A). Ver a seção final sobre a ausência de tipo penal criado após 2018.

Severidade de todos os dispositivos desta ficha: `bloqueante`. Tipo penal é sempre bloqueante.

---

## CP:art153

**Ementa.** Divulgação de segredo contido em documento particular, em correspondência confidencial ou em base da Administração Pública.

**Literal.**
> **Divulgação de segredo**
> **Art. 153** - Divulgar alguém, sem justa causa, conteúdo de documento particular ou de correspondência confidencial, de que é destinatário ou detentor, e cuja divulgação possa produzir dano a outrem:
> Pena - detenção, de um a seis meses, ou multa, de trezentos mil réis a dois contos de réis. *(Vide Lei nº 7.209, de 1984)*
> ~~Parágrafo único - Somente se procede mediante representação.~~
> **§ 1º** Somente se procede mediante representação. *(Parágrafo único renumerado pela Lei nº 9.983, de 2000)*
> **§ 1º-A.** Divulgar, sem justa causa, informações sigilosas ou reservadas, assim definidas em lei, contidas ou não nos sistemas de informações ou banco de dados da Administração Pública: *(Incluído pela Lei nº 9.983, de 2000)*
> Pena - detenção, de 1 (um) a 4 (quatro) anos, e multa. *(Incluído pela Lei nº 9.983, de 2000)*
> **§ 2º** Quando resultar prejuízo para a Administração Pública, a ação penal será incondicionada. *(Incluído pela Lei nº 9.983, de 2000)*

**Fonte.** https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm#art153 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Cenário do caput: médico recebe laudo ou relatório de colega — documento particular confidencial de que é detentor — e cola o conteúdo em prompt de LLM público cuja política de uso permite retenção ou treinamento, com exposição do conteúdo. O núcleo típico é "divulgar".

Cenário do §1º-A: médico em hospital público insere em LLM informação sigilosa "assim definida em lei", contida em sistema ou banco de dados da Administração. A pena do §1º-A é de 1 a 4 anos, superior à do art. 154. O §2º retira a exigência de representação quando há prejuízo para a Administração.

Se dado de saúde é "informação sigilosa assim definida em lei" é leitura nossa, não texto expresso. A LGPD o classifica como sensível (art. 5º, II) e lhe impõe o regime do art. 11, sem declará-lo sigiloso. Ver a incerteza 2 abaixo e a incerteza de `CP:art154-A`.

**Nota de pena.** Os valores em réis do caput estão cancelados pela Lei nº 7.209/1984, art. 2º, verificado literalmente: *"São canceladas, na Parte Especial do Código Penal e nas leis especiais alcançadas pelo art. 12 do Código Penal, quaisquer referências a valores de multas, substituindo-se a expressão 'multa de' por 'multa'."* A pena vigente do caput é detenção de 1 a 6 meses, ou multa em dias-multa. Prescrição do caput: 3 anos, pelo art. 109, VI, na redação da Lei nº 12.234, de 2010, verificada literalmente: *"VI - em 3 (três) anos, se o máximo da pena é inferior a 1 (um) ano."* A redação anterior, de 2 anos, está revogada e aparece riscada no texto compilado. Decadência do direito de representação: 6 meses (art. 103).

**Gatilhos.**
- conteúdo de laudo ou relatório de terceiro colado em prompt de LLM
- envio de documento clínico recebido de colega a serviço externo sem contrato
- exportação de registro oriundo de sistema de hospital público para ferramenta de terceiro
- uso de conta pessoal ou gratuita de LLM em ambiente de instituição pública

**Incerteza.**
1. **Alcance do verbo "divulgar".** A doutrina majoritária exige divulgação a número indeterminado de pessoas. Sob essa leitura, o dado que apenas transita para operador contratualmente vinculado a sigilo tem tipicidade discutível. Leitura concorrente: a exposição a base de treinamento de terceiro já é divulgação. Isto é interpretação doutrinária, não texto expresso. O art. 154 não tem essa fragilidade, porque seu verbo é "revelar".
2. **Dado sensível como "informação sigilosa assim definida em lei".** O §1º-A usa a mesma fórmula do art. 154-A, §3º. A subsunção do dado de saúde nessa fórmula é leitura nossa, com duas posições concorrentes. Estão tabuladas na incerteza de `CP:art154-A` e valem aqui. **NÃO VERIFICADO em precedente.**

**Relacionados.** CP:art154 · CP:art154-A · CP:art325 · LGPD:art11 · LGPD:art5.II

---

## CP:art154

**Ementa.** Violação do segredo profissional. Núcleo penal do sigilo médico.

**Literal.**
> **Violação do segredo profissional**
> **Art. 154** - Revelar alguém, sem justa causa, segredo, de que tem ciência em razão de função, ministério, ofício ou profissão, e cuja revelação possa produzir dano a outrem:
> Pena - detenção, de três meses a um ano, ou multa de um conto a dez contos de réis. *(Vide Lei nº 7.209, de 1984)*
> Parágrafo único - Somente se procede mediante representação.

**Fonte.** https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm#art154 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Cenário: médico cola evolução clínica identificada — nome, CPF, diagnóstico — em ferramenta de LLM de terceiro cujos termos autorizam uso para treinamento, ou usa conta pessoal ou gratuita sem contrato de tratamento de dados. O verbo é "revelar". Basta a ciência por uma única pessoa não autorizada. Diferentemente do art. 153, não se exige divulgação a público indeterminado. Este é o ponto de exposição penal direta do médico no uso corrente de LLM.

Cinco elementos precisam concorrer, todos de texto expresso: segredo; obtido em razão da profissão; revelação a terceiro; ausência de justa causa; potencialidade de dano ("possa produzir dano" — crime de perigo, que não exige dano consumado).

Cenário de operador: engenheiro de healthtech que acessa base de prontuários em razão de ofício e a usa para fine-tuning fora da finalidade contratada. Pela literalidade do tipo, é sujeito ativo.

**Nota de pena e processo.**
- Pena: detenção de 3 meses a 1 ano, ou multa. Valores em réis cancelados pela Lei 7.209/1984, art. 2º.
- Ação penal: pública condicionada à representação do ofendido (parágrafo único).
- Decadência da representação: 6 meses do conhecimento da autoria (art. 103).
- Prescrição: 4 anos (art. 109, V, máximo de 1 ano).
- Rito: infração de menor potencial ofensivo, JECRIM, cabível transação penal — Lei 9.099/95, art. 61, redação da Lei 11.313/2006, verificada: "pena máxima não superior a 2 (dois) anos".

**Gatilhos.**
- chamada a API de LLM com payload contendo dado identificável de paciente
- uso de conta pessoal, gratuita ou de consumidor em fluxo clínico
- provedor de LLM sem contrato de tratamento de dados assinado
- acesso de desenvolvedor ou analista a base de prontuários em ambiente de desenvolvimento
- reuso de base clínica para treinamento fora da finalidade contratada

**Incerteza.**
1. **Sujeito ativo.** Texto expresso: o tipo diz "Revelar **alguém**", qualificado pelo vínculo funcional ou profissional. Pela literalidade alcança o médico, e também secretária, técnico de enfermagem, biomédico e o desenvolvedor ou analista contratado que teve acesso ao dado em razão de ofício. Doutrina, marcada como tal: a classificação como crime próprio, a extensão do dever a estagiários e prestadores terceirizados, e a condição de sujeito ativo do sócio-administrador de clínica que não é profissional de saúde. **Não há, no levantamento, precedente do STJ verificado sobre o art. 154 do CP aplicado a médico. NÃO VERIFICADO.**
2. **Justa causa.** Fontes de justa causa verificadas no levantamento: consentimento por escrito do paciente e dever legal (CEM, art. 73). Se o médico obtém consentimento específico e destacado para o processamento por IA, e há base legal sob a LGPD, art. 11, I, a configuração de justa causa é sustentável. Isto é construção doutrinária, não texto expresso do art. 154.
3. **Anonimização.** Se a anonimização ou a pseudonimização afasta o "segredo", o texto legal não responde. A LGPD, art. 5º, III, define dado anonimizado. Se a reidentificação é razoavelmente possível, o dado continua pessoal e sensível. Interpretação, não texto expresso.

**Relacionados.** CP:art153 · CP:art325 · CEM:art73 · CEM:art85 · CFM-2454-2026:art6 · LGPD:art11

---

## CP:art154-A

**Ementa.** Invasão de dispositivo informático. Redação vigente, dada pela Lei nº 14.155/2021.

**Origem.** Incluído pela Lei nº 12.737/2012. Caput, §2º e pena do §3º alterados pela Lei nº 14.155/2021.

**Literal.**
> **Invasão de dispositivo informático** *(Incluído pela Lei nº 12.737, de 2012)*
> **Art. 154-A.** Invadir dispositivo informático de uso alheio, conectado ou não à rede de computadores, com o fim de obter, adulterar ou destruir dados ou informações sem autorização expressa ou tácita do usuário do dispositivo ou de instalar vulnerabilidades para obter vantagem ilícita: *(Redação dada pela Lei nº 14.155, de 2021)*
> Pena — reclusão, de 1 (um) a 4 (quatro) anos, e multa. *(Redação dada pela Lei nº 14.155, de 2021)*
> **§ 1º** Na mesma pena incorre quem produz, oferece, distribui, vende ou difunde dispositivo ou programa de computador com o intuito de permitir a prática da conduta definida no caput. *(Incluído pela Lei nº 12.737, de 2012)*
> **§ 2º** Aumenta-se a pena de 1/3 (um terço) a 2/3 (dois terços) se da invasão resulta prejuízo econômico. *(Redação dada pela Lei nº 14.155, de 2021)*
> **§ 3º** Se da invasão resultar a obtenção de conteúdo de comunicações eletrônicas privadas, segredos comerciais ou industriais, informações sigilosas, assim definidas em lei, ou o controle remoto não autorizado do dispositivo invadido: *(Incluído pela Lei nº 12.737, de 2012)*
> Pena — reclusão, de 2 (dois) a 5 (cinco) anos, e multa. *(Redação dada pela Lei nº 14.155, de 2021)*
> **§ 4º** Na hipótese do § 3º, aumenta-se a pena de um a dois terços se houver divulgação, comercialização ou transmissão a terceiro, a qualquer título, dos dados ou informações obtidos. *(Incluído pela Lei nº 12.737, de 2012)*
> **§ 5º** Aumenta-se a pena de um terço à metade se o crime for praticado contra: *(Incluído pela Lei nº 12.737, de 2012)*
> I - Presidente da República, governadores e prefeitos;
> II - Presidente do Supremo Tribunal Federal;
> III - Presidente da Câmara dos Deputados, do Senado Federal, de Assembleia Legislativa de Estado, da Câmara Legislativa do Distrito Federal ou de Câmara Municipal; ou
> IV - dirigente máximo da administração direta e indireta federal, estadual, municipal ou do Distrito Federal.

**Literal — ação penal, art. 154-B.**
> **Ação penal** *(Incluído pela Lei nº 12.737, de 2012)*
> **Art. 154-B.** Nos crimes definidos no art. 154-A, somente se procede mediante representação, salvo se o crime é cometido contra a administração pública direta ou indireta de qualquer dos Poderes da União, Estados, Distrito Federal ou Municípios ou contra empresas concessionárias de serviços públicos. *(Incluído pela Lei nº 12.737, de 2012)*

**Fonte.** https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm#art154a · verificado em 2026-08-11 · art. 154-B em https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm#art154b
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Cenário direto: agente de IA ou script com credenciais do médico varre pastas, bancos ou o prontuário eletrônico de um dispositivo de uso alheio — estação de trabalho compartilhada do hospital, servidor da clínica — sem autorização do usuário daquele dispositivo, com a finalidade de obter dados. Depois de 2021 não é preciso ter havido quebra de senha. Se o que se obtém é informação sigilosa assim definida em lei, incide o §3º, com reclusão de 2 a 5 anos. Se dado de saúde entra nessa categoria é leitura nossa, tratada no campo Incerteza. Se houver transmissão a terceiro a qualquer título, inclusive envio a API de LLM de terceiro, incide o §4º, com aumento de 1/3 a 2/3.

Cenário de instalação de vulnerabilidade: plugin, extensão ou servidor MCP não homologado instalado em estação clínica, abrindo canal de exfiltração. O verbo "instalar vulnerabilidades para obter vantagem ilícita" está literalmente no caput.

Ponto de atenção em auditoria de código: o caput não exige dolo de lucro. A exigência de "vantagem ilícita" está na modalidade de instalar vulnerabilidade. A modalidade "obter dados sem autorização expressa ou tácita do usuário" é autônoma.

Limite do tipo, por distinção de texto e não de doutrina: o art. 154-A não alcança o médico que usa o próprio dispositivo com dados a que tem acesso legítimo. Nesse caso o enquadramento é o art. 154, por revelação.

**Deltas da Lei 14.155/2021, verificados no texto da lei alteradora.** Leitura literal, não doutrina.
1. Eliminou o elemento normativo "mediante violação indevida de mecanismo de segurança". Não é mais preciso quebrar barreira técnica. Acesso a dispositivo de uso alheio sem autorização, com finalidade de obter dados, já é típico.
2. Trocou "titular do dispositivo" por "usuário do dispositivo". Desloca a proteção de quem é dono para quem usa.
3. Pena do caput: de detenção de 3 meses a 1 ano para reclusão de 1 a 4 anos. Deixou de ser infração de menor potencial ofensivo e deixou de admitir transação penal pelo art. 61 da Lei 9.099/95.
4. §2º: majorante de 1/6 a 1/3 passou a 1/3 a 2/3.
5. §3º: pena de reclusão de 6 meses a 2 anos passou a reclusão de 2 a 5 anos, e foi suprimida a cláusula de subsidiariedade "se a conduta não constitui crime mais grave".
6. A mesma lei inseriu o art. 155, §§4º-B e 4º-C (furto mediante fraude por dispositivo eletrônico, reclusão de 4 a 8 anos na redação de 2021; §4º-C, I, majorante de 1/3 a 2/3 se o servidor for mantido fora do território nacional; §4º-C, II, majorante de 1/3 ao dobro se contra idoso ou vulnerável) e o art. 171, §§2º-A e 2º-B (fraude eletrônica, reclusão de 4 a 8 anos, mesma majorante por servidor no exterior), além do art. 70, §4º, do CPP.

**Atualização posterior ao delta de 2021, conferida no texto compilado em 11/08/2026.** A Lei nº 15.397, de 2026, deu nova redação ao art. 155, §4º-B (reclusão de 4 a 10 anos) e ao art. 171, §2º-A, que passou a incluir a "duplicação de dispositivo eletrônico ou aplicação de internet". As penas correntes desses dois dispositivos não são mais as de 2021. Os arts. 153, 154, 154-A, 154-B, 325 e 327 não foram alterados.

**Nota de direito intertemporal.** Para fatos anteriores a 28/05/2021 vale a redação da Lei 12.737/2012, transcrita no bruto: exigia "mediante violação indevida de mecanismo de segurança", falava em "titular" do dispositivo, e a pena do caput era detenção de 3 meses a 1 ano e multa.

**Gatilhos.**
- agente ou script com credencial de usuário varrendo diretórios ou bancos de estação compartilhada
- automação que lê prontuário eletrônico sem autorização do usuário do dispositivo
- plugin, extensão de navegador ou servidor MCP não homologado instalado em estação clínica
- credencial de acesso a prontuário compartilhada entre usuários ou embutida em automação
- transmissão a terceiro de dado obtido por acesso não autorizado

**Incerteza.** Dado de saúde como "informações sigilosas, assim definidas em lei" (§3º). Esta é leitura nossa, não texto expresso. O §3º exige que a lei defina a informação como sigilosa. A LGPD classifica dado de saúde como sensível (art. 5º, II) e lhe impõe regime restritivo (art. 11); não o declara sigiloso. Duas posições:

1. **Restritiva.** O §3º só alcança informação que uma lei submeta a sigilo em sentido próprio — CP, art. 154; CEM, art. 73; Lei 9.296/1996. Dado sensível, sem norma de sigilo, fica no caput.
2. **Ampliativa.** O regime do art. 11 da LGPD equivale a definição legal de sigilo, e o §3º incide.

A escolha decide entre reclusão de 1 a 4 anos e reclusão de 2 a 5 anos. **NÃO VERIFICADO em precedente.** A mesma fórmula aparece no art. 153, §1º-A, com a mesma dúvida.

**Relacionados.** CP:art153 · CP:art154 · CP:art325 · LGPD:art46 · LGPD:art11 · LGPD:art5.II · CFM-2454-2026:art17

---

## CP:art325

**Ementa.** Violação de sigilo funcional, fornecimento de acesso a sistema da Administração e uso indevido de acesso restrito.

**Literal.**
> **Violação de sigilo funcional**
> **Art. 325** - Revelar fato de que tem ciência em razão do cargo e que deva permanecer em segredo, ou facilitar-lhe a revelação:
> Pena - detenção, de seis meses a dois anos, ou multa, se o fato não constitui crime mais grave.
> **§ 1º** Nas mesmas penas deste artigo incorre quem: *(Incluído pela Lei nº 9.983, de 2000)*
> **I** - permite ou facilita, mediante atribuição, fornecimento e empréstimo de senha ou qualquer outra forma, o acesso de pessoas não autorizadas a sistemas de informações ou banco de dados da Administração Pública; *(Incluído pela Lei nº 9.983, de 2000)*
> **II** - se utiliza, indevidamente, do acesso restrito. *(Incluído pela Lei nº 9.983, de 2000)*
> **§ 2º** Se da ação ou omissão resulta dano à Administração Pública ou a outrem: *(Incluído pela Lei nº 9.983, de 2000)*
> Pena - reclusão, de 2 (dois) a 6 (seis) anos, e multa. *(Incluído pela Lei nº 9.983, de 2000)*

**Fonte.** https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm#art325 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** Cenário do caput: médico servidor — SUS, hospital universitário, secretaria municipal — cola prontuário do sistema público em LLM. É revelação de fato de que tem ciência em razão do cargo. A ação penal é pública incondicionada: não há a cláusula de representação que existe no art. 153, caput, e no art. 154.

Cenário do §1º, I: compartilhar credencial de acesso ao sistema hospitalar público com agente, automação ou serviço de terceiro. O texto diz "senha ou qualquer outra forma". Configurar agente de IA com credenciais de servidor para consultar banco público é subsunção literal.

Cenário do §1º, II: médico que usa acesso legítimo para finalidade não autorizada, por exemplo extrair coorte para treinar modelo próprio sem aprovação institucional ou de comitê de ética.

Cenário do §2º: quando resulta dano ao paciente — o texto diz "ou a outrem" —, a pena passa a reclusão de 2 a 6 anos e multa. É a faixa de pena mais alta desta ficha para o médico servidor.

**Gatilhos.**
- credencial de acesso a prontuário compartilhada entre usuários
- credencial de servidor público embutida em script, agente ou integração
- conta de serviço de sistema público sem vínculo com pessoa identificada
- extração de coorte de sistema público sem aprovação registrada
- exportação de prontuário sem controle de acesso ou sem registro de finalidade

**Incerteza.** O caput traz cláusula de subsidiariedade expressa, "se o fato não constitui crime mais grave", o que remete ao art. 153, §1º-A (1 a 4 anos) e ao art. 154-A, §3º (2 a 5 anos), conforme o caso. A resolução concreta do concurso aparente é matéria doutrinária e jurisprudencial. **NÃO VERIFICADO em precedente.**

**Relacionados.** CP:art327 · CP:art153 · CP:art154-A · CEM:art78 · CEM:art85

---

## CP:art327

**Ementa.** Conceito de funcionário público para efeitos penais, com equiparação de empregado de empresa prestadora de serviço.

**Literal.**
> **Funcionário público**
> **Art. 327** - Considera-se funcionário público, para os efeitos penais, quem, embora transitoriamente ou sem remuneração, exerce cargo, emprego ou função pública.
> **§ 1º** - Equipara-se a funcionário público quem exerce cargo, emprego ou função em entidade paraestatal, **e quem trabalha para empresa prestadora de serviço contratada ou conveniada para a execução de atividade típica da Administração Pública.** *(Incluído pela Lei nº 9.983, de 2000)*
> **§ 2º** - A pena será aumentada da terça parte quando os autores dos crimes previstos neste Capítulo forem ocupantes de cargos em comissão ou de função de direção ou assessoramento de órgão da administração direta, sociedade de economia mista, empresa pública ou fundação instituída pelo poder público. *(Incluído pela Lei nº 6.799, de 1980)*

**Fonte.** https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm#art327 · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** bloqueante

**Aplicação.** O §1º define o alcance subjetivo do art. 325. Empregado de empresa prestadora de serviço contratada ou conveniada para executar atividade típica da Administração é equiparado a funcionário público. O desenvolvedor de healthtech contratada por secretaria de saúde pode responder pelo art. 325, e não apenas pelo art. 154. O mesmo vale para médico cooperado ou terceirizado que atua em serviço público por contrato ou convênio.

O §2º majora a pena em um terço quando o autor ocupa cargo em comissão ou função de direção ou assessoramento. Alcança diretor técnico, chefe de serviço e coordenador de TI de hospital público, de fundação estatal ou de empresa pública de saúde. A majorante vale para os crimes do Capítulo, e portanto para o art. 325 em todas as suas figuras.

**Gatilhos.**
- integração de fornecedor privado com sistema de saúde público
- contrato ou convênio com secretaria de saúde sem cláusula de sigilo para a equipe técnica
- acesso de equipe de fornecedor a base de dados da Administração
- decisão de adoção de LLM tomada por ocupante de cargo de direção em serviço público de saúde

**Relacionados.** CP:art325

---

## Achado — não há tipo penal específico para vazamento de dado pessoal criado após 2018

Resposta verificada no bruto: **não existe.** Evidência primária colhida em 11/08/2026.

1. **A LGPD não contém tipo penal.** Busca textual por "crime", "criminal" e "Pena -" no texto compilado integral da Lei 13.709/2018 retornou zero ocorrências. As sanções da LGPD são administrativas (art. 52) e civis (arts. 42 a 45).
2. **O Código Penal não recebeu artigo novo sobre vazamento ou tratamento indevido de dado pessoal após 2018.** A Seção "Dos crimes contra a inviolabilidade dos segredos" termina em 154-A e 154-B. Resultado da busca textual no texto compilado, refeito em 11/08/2026: "banco de dados", no singular, ocorre duas vezes, no art. 153, §1º-A, e no art. 325, §1º, I; "bancos de dados", no plural, ocorre uma vez, no art. 313-A; "dado pessoal" tem zero ocorrências; "dados pessoais" ocorre uma única vez, no art. 297, §4º, que trata de falsificação de documento previdenciário e não de vazamento. As quatro passagens vêm da Lei 9.983/2000. Todas anteriores a 2018.
3. **O Código Penal menciona inteligência artificial uma única vez, e não em matéria de dado.** Art. 147-B, parágrafo único, incluído pela Lei nº 15.123, de 2025, transcrito literalmente: *"A pena é aumentada de metade se o crime é cometido mediante uso de inteligência artificial ou de qualquer outro recurso tecnológico que altere imagem ou som da vítima."* É majorante do crime de violência psicológica contra a mulher. Não alcança tratamento de dado de paciente. O dado é registrado aqui para que a skill não conclua, de uma busca por "inteligência artificial" no CP, que existe tipo penal de IA aplicável a saúde.
4. **Não há Marco Legal da IA vigente no Brasil em 11/08/2026.** O PL 2338/2023 foi aprovado pelo Plenário do Senado em 10/12/2024 e o autógrafo foi remetido à Câmara dos Deputados em 17/03/2025. A ficha de tramitação da Câmara, consultada em 11/08/2026, registra o projeto em Comissão Especial, aguardando parecer do relator. Não aprovado pela Câmara, não sancionado.

**Fonte.** https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm · https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm · https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262 · verificado em 2026-08-11
**Confiança.** primária-conferida

Consequência para a auditoria: a repressão penal ao vazamento de dado de saúde é feita pelos tipos desta ficha. O silêncio legislativo posterior a 2018 não reduz a exposição, porque os tipos de 1940, 2000, 2012 e 2021 continuam aplicáveis.

**Vetor adicional verificado.** Lei nº 9.296/1996, art. 10, redação da Lei 13.869/2019, transcrito literalmente: *"Constitui crime realizar interceptação de comunicações telefônicas, de informática ou telemática, promover escuta ambiental ou quebrar segredo da Justiça, sem autorização judicial ou com objetivos não autorizados em lei: Pena - reclusão, de 2 (dois) a 4 (quatro) anos, e multa. [...]"* — suprimido o parágrafo único, que trata da autoridade judicial que determina a execução da conduta. Relevante quando o vetor de exfiltração for interceptação de comunicação telemática, por exemplo proxy ou MITM em rede hospitalar.

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/l9296.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

---

## Fontes primárias desta ficha

| Norma | URL | Verificado |
|---|---|---|
| Código Penal (DL 2.848/1940, compilado) | https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm | 2026-08-11 |
| Lei 7.209/1984 (art. 2º, cancelamento de valores de multa) | https://www.planalto.gov.br/ccivil_03/leis/1980-1988/l7209.htm | 2026-08-11 |
| Lei 12.737/2012 | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12737.htm | 2026-08-11 |
| Lei 14.155/2021 | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/L14155.htm | 2026-08-11 |
| Lei 9.296/1996 (art. 10) | https://www.planalto.gov.br/ccivil_03/leis/l9296.htm | 2026-08-11 |
| Lei 9.099/1995 (art. 61) | https://www.planalto.gov.br/ccivil_03/leis/l9099.htm | 2026-08-11 |
| LGPD (Lei 13.709/2018, compilada) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm | 2026-08-11 |
| PL 2338/2023 — não sancionado | https://www25.senado.leg.br/web/atividade/materias/-/materia/157233 | 2026-08-11 |

## Itens NÃO VERIFICADOS nesta ficha

- Precedente do STJ, ou de qualquer tribunal, aplicando o art. 154 do CP a médico.
- Precedente de qualquer tribunal sobre uso de LLM ou IA generativa com dado de paciente.
- Resolução do concurso aparente entre o art. 325, caput, e os arts. 153, §1º-A, e 154-A, §3º.
- Precedente sobre a subsunção de dado sensível de saúde em "informação sigilosa assim definida em lei", exigida pelo art. 153, §1º-A, e pelo art. 154-A, §3º.
