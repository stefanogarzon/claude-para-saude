---
norma: Código Civil (Lei nº 10.406/2002), Código de Defesa do Consumidor (Lei nº 8.078/1990) e Marco Civil da Internet (Lei nº 12.965/2014)
ementa: Responsabilidade civil, responsabilidade do fornecedor de serviço e aplicação da lei brasileira a provedor estrangeiro, no uso de LLM com dado de paciente
abrangencia: CC arts. 12, 21, 186, 187, 188, 927, 932, 933, 934, 942 e 944; CDC arts. 3º, 14 e §4º, e 17; MCI arts. 7º, 8º, 10, 11 e 12; e uma seção de jurisprudência do STJ com onze precedentes
status: vigente
fontes:
  - https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm
  - https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
  - https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm
verificado: 2026-08-11
origem: corpus/bruto/03_penal_civil.md — download direto do HTML de planalto.gov.br, transcrição literal
auditado: no Marco Civil, a MP nº 1.068/2021, que alterava os arts. 8º-A, 11, §2º, e 12, foi rejeitada. O texto compilado exibe "(Rejeitada)". O CDC recebeu apenas a Lei nº 14.181/2021, que não toca o art. 14. O Código Civil traz alterações até a Lei nº 15.068/2024, nenhuma sobre os arts. 186, 187, 927, 932, 933, 942 ou 944. As redações desta ficha são as vigentes
revisao: reauditoria adversarial independente em 2026-08-11, feita direto das fontes primárias. Os onze campos Literal foram conferidos palavra por palavra contra o HTML de planalto.gov.br, e as citações de LGPD, CF e CDC verificadas nos textos compilados. Todos os precedentes foram reabertos no Informativo de Jurisprudência do STJ, com permalink próprio por nota. Seis erros de jurisprudência corrigidos: DESTAQUE trocado por fundamentação em dois precedentes, tese não firmada atribuída a um terceiro, ano de julgamento errado em um, identificação processual incompleta em dois, e três citações entre aspas que não conferiam com o texto oficial. Corrigida também a contagem de incisos do art. 33 da LGPD. Campos Fonte e Confiança acrescentados a todas as entradas
---

# Código Civil, CDC e Marco Civil da Internet

Onze dispositivos e uma seção de jurisprudência do STJ. A ficha separa em campo próprio o que é texto expresso e o que é construção doutrinária, em especial no art. 927, parágrafo único, do Código Civil, e na interação do art. 14, §4º, do CDC com a pessoa jurídica.

---

## CC:art21

**Ementa.** Inviolabilidade da vida privada e tutela inibitória.

**Literal.**
> **Art. 21.** A vida privada da pessoa natural é inviolável, e o juiz, a requerimento do interessado, adotará as providências necessárias para impedir ou fazer cessar ato contrário a esta norma. *(Vide ADIN 4815)*

**Literal — dispositivo conexo, art. 12.**
> **Art. 12.** Pode-se exigir que cesse a ameaça, ou a lesão, a direito da personalidade, e reclamar perdas e danos, sem prejuízo de outras sanções previstas em lei.
> Parágrafo único. Em se tratando de morto, terá legitimação para requerer a medida prevista neste artigo o cônjuge sobrevivente, ou qualquer parente em linha reta, ou colateral até o quarto grau.

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm · verificado em 2026-08-11 · CF, art. 5º, LXXIX, em https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc115.htm
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O art. 21 é base de tutela inibitória, não apenas indenizatória. Paciente que descobre que sua evolução clínica foi processada por LLM de terceiro pode pedir tutela de urgência para fazer cessar o tratamento e determinar a eliminação. O pedido não depende de comprovar dano. O art. 12, parágrafo único, dá legitimidade a cônjuge e parentes de paciente falecido, o que se soma à persistência do sigilo médico após a morte (CEM, art. 73, parágrafo único, "a").

O reforço constitucional é a CF, art. 5º, LXXIX, incluído pela Emenda Constitucional nº 115, de 10/02/2022, verificada: *"LXXIX - é assegurado, nos termos da lei, o direito à proteção dos dados pessoais, inclusive nos meios digitais."* A proteção de dados é direito fundamental autônomo desde 2022.

**Gatilhos.**
- ausência de rotina de eliminação de dado a pedido do titular
- retenção de prompts e respostas sem prazo definido no contrato com o provedor
- uso de base histórica de pacientes falecidos em teste ou treinamento

**Relacionados.** CC:art186 · CEM:art73 · LGPD:art18

---

## CC:art186

**Ementa.** Ato ilícito. Cláusula geral de responsabilidade subjetiva.

**Literal.**
> **Art. 186.** Aquele que, por ação ou omissão voluntária, negligência ou imprudência, violar direito e causar dano a outrem, ainda que exclusivamente moral, comete ato ilícito. *(Vide ADI nº 7055)* *(Vide ADI nº 6792)*

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** É o fundamento típico contra o médico pessoa física, que, sob o art. 14, §4º, do CDC, responde por culpa. A negligência é o vetor concreto: usar ferramenta de IA sem contrato de tratamento de dados, sem criptografia, sem controle de retenção, sem desidentificação e sem base legal do art. 11 da LGPD. O texto admite dano "ainda que exclusivamente moral". Não é preciso prejuízo patrimonial.

**Gatilhos.**
- ausência de contrato de tratamento de dados com o provedor de LLM
- ausência de desidentificação antes do envio
- ausência de registro de retenção e de descarte
- ausência de trilha que demonstre diligência na escolha da ferramenta

**Relacionados.** CC:art187 · CC:art927 · CDC:art14§4 · LGPD:art42

---

## CC:art187

**Ementa.** Abuso de direito. Exercício de direito fora de sua finalidade.

**Literal.**
> **Art. 187.** Também comete ato ilícito o titular de um direito que, ao exercê-lo, excede manifestamente os limites impostos pelo seu fim econômico ou social, pela boa-fé ou pelos bons costumes.

**Literal — dispositivo conexo, art. 188.**
> **Art. 188.** Não constituem atos ilícitos:
> I - os praticados em legítima defesa ou no exercício regular de um direito reconhecido; [...]

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O médico tem direito legítimo de acessar o prontuário do seu paciente. Exercer esse acesso para finalidade estranha ao cuidado — extrair coorte para treinar modelo, alimentar produto comercial — excede os limites impostos pelo fim econômico ou social e pela boa-fé. O art. 187 é a ponte entre "acesso autorizado" e "uso ilícito", que é o caso do desvio de finalidade da LGPD (art. 6º, I).

**Gatilhos.**
- consulta a prontuário sem vínculo com atendimento em curso
- extração em lote de registros clínicos para fora do sistema assistencial
- reuso de base assistencial em projeto de produto ou de pesquisa sem aprovação registrada

**Incerteza.** Se o abuso de direito do art. 187 é ato ilícito objetivo, dispensando culpa em sua configuração. A doutrina diverge. **Controvérsia doutrinária, não texto expresso.**

**Relacionados.** CC:art186 · LGPD:art6.I · CP:art325

---

## CC:art927

**Ementa.** Dever de reparar e responsabilidade objetiva por atividade de risco.

**Literal.**
> **Art. 927.** Aquele que, por ato ilícito (arts. 186 e 187), causar dano a outrem, fica obrigado a repará-lo. *(Vide ADI nº 7055)* *(Vide ADI nº 6792)*
> **Parágrafo único.** Haverá obrigação de reparar o dano, independentemente de culpa, nos casos especificados em lei, ou quando a atividade normalmente desenvolvida pelo autor do dano implicar, por sua natureza, risco para os direitos de outrem.

**Literal — dispositivos conexos, arts. 942 e 944.**
> **Art. 944.** A indenização mede-se pela extensão do dano.
> Parágrafo único. Se houver excessiva desproporção entre a gravidade da culpa e o dano, poderá o juiz reduzir, eqüitativamente, a indenização.
>
> **Art. 942.** Os bens do responsável pela ofensa ou violação do direito de outrem ficam sujeitos à reparação do dano causado; e, se a ofensa tiver mais de um autor, todos responderão solidariamente pela reparação.
> Parágrafo único. São solidariamente responsáveis com os autores os co-autores e as pessoas designadas no art. 932.

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm · verificado em 2026-08-11 · LGPD, arts. 42 a 46, em https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O parágrafo único tem duas partes com regimes distintos, e a auditoria precisa dizer em qual delas se apoia.

Primeira parte, "casos especificados em lei". Há casos especificados que incidem sobre tratamento de dado de saúde com LLM, todos verificados literalmente no bruto:
- CDC, art. 14, caput — responsabilidade objetiva do fornecedor de serviço. Ver `CDC:art14`.
- LGPD, art. 42, caput: *"O controlador ou o operador que, em razão do exercício de atividade de tratamento de dados pessoais, causar a outrem dano patrimonial, moral, individual ou coletivo, em violação à legislação de proteção de dados pessoais, é obrigado a repará-lo."*
- LGPD, art. 44, parágrafo único: *"Responde pelos danos decorrentes da violação da segurança dos dados o controlador ou o operador que, ao deixar de adotar as medidas de segurança previstas no art. 46 desta Lei, der causa ao dano."*
- Marco Civil, art. 7º, I: *"inviolabilidade da intimidade e da vida privada, sua proteção e indenização pelo dano material ou moral decorrente de sua violação"*.

Segunda parte, atividade de risco. O texto diz "risco para os direitos de outrem", e não risco à integridade física. Isso é o que o texto diz. Os arts. 12 e 21 do CC e o art. 5º, X e LXXIX, da CF protegem os direitos da personalidade, a vida privada e a proteção de dados pessoais. Nenhum deles enuncia que dado sensível é objeto de direito da personalidade: essa é leitura nossa, registrada no campo de incerteza abaixo.

**Ônus da prova — texto expresso.** LGPD, art. 42, §2º, verificado literalmente: *"O juiz, no processo civil, poderá inverter o ônus da prova a favor do titular dos dados quando, a seu juízo, for verossímil a alegação, houver hipossuficiência para fins de produção de prova ou quando a produção de prova pelo titular resultar-lhe excessivamente onerosa."* Na prática forense esta é a norma que mais pesa. Mesmo sem definir o regime de responsabilidade, ela transfere ao médico ou à clínica o ônus de provar que o pipeline era seguro. Consequência operacional: logs, contrato de tratamento de dados, registro de operações de tratamento (LGPD, art. 37) e relatório de impacto são o meio de descarregar esse ônus.

**Excludentes — texto expresso.** LGPD, art. 43, verificado literalmente:
> **Art. 43.** Os agentes de tratamento só não serão responsabilizados quando provarem:
> I - que não realizaram o tratamento de dados pessoais que lhes é atribuído;
> II - que, embora tenham realizado o tratamento de dados pessoais que lhes é atribuído, não houve violação à legislação de proteção de dados; ou
> III - que o dano é decorrente de culpa exclusiva do titular dos dados ou de terceiro.

O art. 43, III, exige prova de culpa exclusiva de terceiro. Nossa leitura: clínica que sofre exfiltração de base clínica via integração com LLM e invoca ataque externo precisa demonstrar que o incidente era inevitável apesar das medidas do art. 46. Isto é construção nossa sobre o texto do art. 43, III. **Nenhum precedente verificado firmou esse ônus.** Em `STJ:REsp2147374` a culpa exclusiva de terceiro foi tida por não comprovada no caso concreto, o que é descrição do julgado, não tese sobre ônus de prova.

**Gatilhos.**
- ausência de log de chamadas a LLM com dado de paciente
- ausência de registro das operações de tratamento
- ausência de relatório de impacto para fluxo com dado sensível
- ausência de contrato que identifique controlador e operador

**Incerteza.** Ponto controverso central desta ficha. A pergunta é: processar dado de saúde com IA é atividade de risco para fins do art. 927, parágrafo único?

**Não há resposta no texto legal. Não há, no levantamento, precedente do STJ verificado que aplique o art. 927, parágrafo único, a tratamento de dados por IA. NÃO VERIFICADO.**

Premissa nossa, e não texto de lei: dado sensível de saúde é objeto de direito da personalidade. O encadeamento é o dos arts. 12 e 21 do CC com o art. 5º, X e LXXIX, da CF. Nenhum desses dispositivos o afirma. A premissa é o que liga o dado de saúde à expressão "risco para os direitos de outrem" da segunda parte do parágrafo único. Quem a contesta derruba a tese pró-objetiva por inteiro.

As três posições abaixo são construção doutrinária, não direito posto. Nenhuma delas pode ser apresentada a médicos como regra vigente.

| Tese | Fundamento invocado | Status |
|---|---|---|
| Pró-objetiva. Tratar dado sensível de saúde em escala, com sistema opaco e transfronteiriço, é atividade que por sua natureza implica risco a direitos da personalidade | CC 927, pu, 2ª parte; LGPD 42 e 44; LGPD 5º, II; LGPD 46, §2º | Doutrina. Sem súmula, tema repetitivo ou precedente do STJ verificado |
| Contra-objetiva. A responsabilidade objetiva é excepcional, a LGPD não a nomeia expressamente, e o CDC, art. 14, §4º, ressalva o profissional liberal | CC 927, pu, 1ª parte, que exige "casos especificados em lei"; CDC 14, §4º; LGPD 43 | Doutrina. Também não resolvida em precedente vinculante |
| Intermediária, majoritária na literatura de proteção de dados. A LGPD instituiu regime próprio, de culpa normativa presumida, com inversão de ônus, sem se enquadrar puramente em subjetiva nem em objetiva | LGPD 42, §2º; LGPD 44 | Doutrina |

**Dado verificado que fortalece a tese intermediária.** LGPD, art. 44, caput, transcrição literal: *"O tratamento de dados pessoais será irregular quando deixar de observar a legislação ou quando não fornecer a segurança que o titular dele pode esperar, consideradas as circunstâncias relevantes, entre as quais: I - o modo pelo qual é realizado; II - o resultado e os riscos que razoavelmente dele se esperam; III - as técnicas de tratamento de dados pessoais disponíveis à época em que foi realizado."* O paralelismo textual com o art. 14, §1º, I a III, do CDC é quase exato. Esse é o argumento textual mais forte para tratar o vazamento como fato do serviço. Segue sendo argumento, não tese fixada em precedente.

**Precedente verificado que nomeia responsabilidade objetiva.** Em `STJ:REsp2201694`, o DESTAQUE oficial diz que o gestor de banco de dados para formação de histórico de crédito, que disponibiliza a terceiros consulentes informações cadastrais e de adimplemento sem prévia autorização do cadastrado, "deve responder objetivamente pelos danos morais, que são presumidos". É o único precedente deste levantamento em que o STJ nomeia responsabilidade objetiva por disponibilização indevida de dados. Três limites, todos verificados: o caso é de gestor de banco de dados sob a Lei nº 12.414/2011, não de agente de tratamento em saúde; a decisão foi por maioria; o fundamento é a lei específica do cadastro positivo, não o art. 927, parágrafo único, do CC. O precedente não resolve a pergunta desta seção. Reduz, porém, o alcance da frase "não há precedente verificado sobre regime de responsabilidade": há um, restrito ao seu objeto.

**Relacionados.** CC:art186 · CC:art932 · CDC:art14 · LGPD:art42 · LGPD:art43 · LGPD:art44 · STJ:REsp2147374 · STJ:REsp2201694

---

## CC:art932

**Ementa.** Responsabilidade por ato de terceiro, inclusive do empregador por preposto.

**Literal.**
> **Art. 932.** São também responsáveis pela reparação civil:
> I - os pais, pelos filhos menores que estiverem sob sua autoridade e em sua companhia;
> II - o tutor e o curador, pelos pupilos e curatelados, que se acharem nas mesmas condições;
> **III - o empregador ou comitente, por seus empregados, serviçais e prepostos, no exercício do trabalho que lhes competir, ou em razão dele;**
> IV - os donos de hotéis, hospedarias, casas ou estabelecimentos onde se albergue por dinheiro, mesmo para fins de educação, pelos seus hóspedes, moradores e educandos;
> V - os que gratuitamente houverem participado nos produtos do crime, até a concorrente quantia.

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O inciso III alcança clínica e hospital pelo médico empregado, pelo residente, pela secretária e pelo TI terceirizado, que é preposto do comitente, quando o dado de paciente vaza por uso indevido de LLM. A cláusula "ou em razão dele" é ampla: alcança o médico que usa LLM em casa, em celular pessoal, fora do horário, se o acesso ao dado decorreu do vínculo.

Pelo art. 942, parágrafo único, a responsabilidade é solidária entre autor e as pessoas do art. 932. O paciente pode acionar apenas a clínica.

Pelo art. 934, a clínica tem direito de regresso contra o médico. O médico empregado não está protegido pelo fato de a clínica pagar: ele é o destinatário do regresso, além de responder pessoalmente no penal (CP, arts. 154 e 325) e no ético (CEM, art. 73).

Convergência com a LGPD: o art. 42, §1º, I e II, estabelece solidariedade entre operador e controlador e entre controladores diretamente envolvidos. Se a clínica é controladora e o fornecedor de LLM é operador, há dois regimes de solidariedade sobrepostos.

**Gatilhos.**
- ausência de política interna de uso de IA para equipe e residentes
- uso de dispositivo pessoal sem gestão para acesso a dado de paciente
- fornecedor de TI com acesso à base clínica sem contrato de operador
- ausência de cláusula de regresso e de responsabilidade em contrato de trabalho ou de prestação

**Relacionados.** CC:art933 · CC:art927 · CDC:art14 · LGPD:art42 · CEM:art78

---

## CC:art933

**Ementa.** Responsabilidade sem culpa das pessoas indicadas no art. 932.

**Literal.**
> **Art. 933.** As pessoas indicadas nos incisos I a V do artigo antecedente, **ainda que não haja culpa de sua parte, responderão pelos atos praticados pelos terceiros ali referidos.**

**Literal — dispositivo conexo, art. 934.**
> **Art. 934.** Aquele que ressarcir o dano causado por outrem pode reaver o que houver pago daquele por quem pagou, salvo se o causador do dano for descendente seu, absoluta ou relativamente incapaz.

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A combinação do art. 932, III, com o art. 933 é responsabilidade objetiva do empregador por ato do preposto. Isto é texto expresso, não doutrina: "ainda que não haja culpa de sua parte". Para a clínica, o argumento de que "o médico agiu por conta própria" não afasta a responsabilidade civil perante o paciente. Ele serve ao regresso do art. 934, em ação posterior contra o médico.

**Relacionados.** CC:art932 · CC:art942

---

## CDC:art14

**Ementa.** Fato do serviço. Responsabilidade objetiva do fornecedor de serviço.

**Literal.**
> **Art. 14.** O fornecedor de serviços responde, **independentemente da existência de culpa**, pela reparação dos danos causados aos consumidores por defeitos relativos à prestação dos serviços, bem como por informações insuficientes ou inadequadas sobre sua fruição e riscos.
> **§ 1°** O serviço é defeituoso quando não fornece a segurança que o consumidor dele pode esperar, levando-se em consideração as circunstâncias relevantes, entre as quais:
> I - o modo de seu fornecimento;
> II - o resultado e os riscos que razoavelmente dele se esperam;
> III - a época em que foi fornecido.
> **§ 2º** O serviço não é considerado defeituoso pela adoção de novas técnicas.
> **§ 3°** O fornecedor de serviços só não será responsabilizado quando provar:
> I - que, tendo prestado o serviço, o defeito inexiste;
> II - a culpa exclusiva do consumidor ou de terceiro.

**Literal — dispositivos conexos, arts. 3º e 17.**
> **Art. 17.** Para os efeitos desta Seção, equiparam-se aos consumidores **todas as vítimas do evento.**
>
> **Art. 3°** Fornecedor é toda pessoa física ou jurídica, pública ou privada, nacional ou estrangeira, bem como os entes despersonalizados, que desenvolvem atividade de produção, montagem, criação, construção, transformação, importação, exportação, distribuição ou comercialização de produtos ou prestação de serviços.
> [...]
> § 2° Serviço é qualquer atividade fornecida no mercado de consumo, mediante remuneração, inclusive as de natureza bancária, financeira, de crédito e securitária, salvo as decorrentes das relações de caráter trabalhista.

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm · verificado em 2026-08-11 · LGPD, art. 45, em https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O caput impõe responsabilidade objetiva ao fornecedor de serviços. Clínica, hospital, laboratório e healthtech são fornecedores pelo art. 3º.

O §1º define defeito como falta da "segurança que o consumidor dele pode esperar". O consumidor de serviço médico espera sigilo, por definição legal (CP, art. 154; CEM, art. 73). Vazamento por LLM subsome em defeito do serviço.

O §2º é frequentemente mal citado. "O serviço não é considerado defeituoso pela adoção de novas técnicas" não significa que adotar IA imuniza. Significa que a superveniência de técnica melhor não torna a anterior defeituosa. Ler o §2º como salvo-conduto para IA é erro de leitura, e a skill de auditoria deve sinalizá-lo.

O art. 17 equipara a consumidor todas as vítimas do evento. Em vazamento de base, todos os pacientes da base são consumidores por equiparação, ainda que não fossem pacientes daquele médico. É base para ação coletiva.

Interação com a LGPD, texto expresso do art. 45: *"As hipóteses de violação do direito do titular no âmbito das relações de consumo permanecem sujeitas às regras de responsabilidade previstas na legislação pertinente."* Na relação clínica-paciente, a LGPD remete ao CDC, e não o contrário. O regime do art. 14 prevalece para a clínica pessoa jurídica.

**Gatilhos.**
- integração de LLM em serviço prestado a paciente sem avaliação de segurança documentada
- ausência de informação ao paciente sobre riscos do uso da ferramenta
- base clínica única para vários profissionais, sem segmentação de acesso
- alegação de "estado da técnica" usada como justificativa para ausência de controle

**Relacionados.** CDC:art14§4 · CC:art927 · LGPD:art44 · LGPD:art45 · STJ:REsp2077278

---

## CDC:art14§4

**Ementa.** Exceção do profissional liberal. Alcance pessoal e não empresarial.

**Literal.**
> **§ 4°** A responsabilidade pessoal dos profissionais liberais será apurada mediante a verificação de culpa.

**Fonte.** https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm · verificado em 2026-08-11
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Este é o ponto que mais gera erro em material dirigido a médicos. O que o texto diz:

1. O §4º ressalva apenas "a responsabilidade **pessoal** dos profissionais liberais". A palavra é pessoal. O texto não estende a ressalva à pessoa jurídica.
2. Pela literalidade: médico pessoa física autônomo responde por culpa, pelo §4º. Clínica, hospital ou laboratório, pessoa jurídica, não é profissional liberal e não é alcançado pela ressalva. Responde pelo caput. Se essa responsabilidade permanece objetiva quando o dano decorre de ato do médico é questão cindida pelo STJ, tratada na incerteza 1.
3. A consequência prática é direta. O médico que atende como pessoa jurídica, ou que integra clínica, não leva consigo a exceção do §4º para dentro da empresa. A clínica responde pelo caput, e ainda pelo art. 932, III, com o art. 933, por ato do preposto.
4. Reorganizar o atendimento como pessoa jurídica, por razão tributária ou operacional, muda o regime de responsabilidade civil do serviço. Isso precisa ser dito ao colega antes, não depois do incidente.

**Gatilhos.**
- atendimento por pessoa jurídica em vez de profissional liberal
- clínica que apresenta a exceção do §4º como cobertura para o serviço prestado
- contrato de prestação de serviço médico sem definição de quem é o fornecedor perante o paciente
- integração de LLM contratada em nome da pessoa jurídica, com uso individual pelo médico

**Incerteza.**
1. **Cisão do regime dentro da pessoa jurídica.** O STJ separa dois regimes no mesmo estabelecimento. Para os serviços do estabelecimento, a responsabilidade é objetiva. Para o dano decorrente de falha técnica restrita ao profissional médico, é subjetiva, dependente da culpa do médico. O trecho reproduzido nesta ficha — *"A responsabilidade objetiva para o prestador de serviço [...] limita-se aos serviços relacionados ao estabelecimento empresarial, tais como estadia do paciente (internação e alimentação), instalações, equipamentos e serviços auxiliares (enfermagem, exames, radiologia)"* — vem da sistematização de jurisprudência do TJDFT, e não de leitura direta do acórdão do STJ.

   **Estado da verificação em 11/08/2026.** A página do TJDFT foi reaberta e confirma a identificação do precedente: AgInt no REsp n. 2.220.066/TO, Rel. Ministra Nancy Andrighi, Terceira Turma, julgado em 13/10/2025, DJEN 16/10/2025. A busca por "2220066" no Informativo de Jurisprudência do STJ não retorna verbete, e a pesquisa de acórdãos do STJ recusa acesso automatizado. **Não foi possível conferir o trecho em fonte do próprio STJ.**

   **Fonte.** https://www.tjdft.jus.br/consultas/jurisprudencia/jurisprudencia-em-temas/cdc-na-visao-do-tjdft-1/responsabilidade-civil-no-cdc/responsabilidade-do-hospital-quanto-a-atuacao-tecnico-profissional-do-medico · verificado em 2026-08-11
   **Confiança.** secundária — **citação de segunda mão, não usar como fundamentação.**

   Leitura nossa, marcada como tal: essa linha foi construída sobre erro médico. A quebra de sigilo por vazamento de dados não é ato técnico do médico. É falha do estabelecimento e do seu pipeline — controle de acesso, contrato com o fornecedor, retenção, log. Sob a cisão do próprio STJ, ela cai do lado dos serviços do estabelecimento, e não do lado da falha técnica profissional. Este é o modo honesto de sustentar a responsabilidade objetiva da clínica em vazamento: pela natureza da falha, não por negar a cisão. **Não há tema repetitivo ou súmula do STJ verificada nesta pesquisa sobre essa questão aplicada a vazamento de dados. NÃO VERIFICADO.**
2. **Transposição da obrigação de meio.** A discussão clássica do §4º na jurisprudência é sobre erro médico e obrigação de meio, não sobre quebra de sigilo. Transpor essa lógica para o dever de sigilo é salto argumentativo. A tese de que o dever de sigilo é obrigação de resultado — ou se guardou, ou se revelou — é doutrina, não jurisprudência verificada.

**Relacionados.** CDC:art14 · CC:art186 · CC:art932 · STJ:sem-numero-2021

---

## MCI:art7

**Ementa.** Direitos do usuário de internet: sigilo, consentimento destacado, exclusão e aplicação do CDC.

**Literal.**
> **Art. 7º** O acesso à internet é essencial ao exercício da cidadania, e ao usuário são assegurados os seguintes direitos:
> **I** - inviolabilidade da intimidade e da vida privada, sua proteção e indenização pelo dano material ou moral decorrente de sua violação;
> **II** - inviolabilidade e sigilo do fluxo de suas comunicações pela internet, salvo por ordem judicial, na forma da lei;
> **III** - inviolabilidade e sigilo de suas comunicações privadas armazenadas, salvo por ordem judicial;
> [...]
> **VII** - não fornecimento a terceiros de seus dados pessoais, inclusive registros de conexão, e de acesso a aplicações de internet, salvo mediante consentimento livre, expresso e informado ou nas hipóteses previstas em lei;
> **VIII** - informações claras e completas sobre coleta, uso, armazenamento, tratamento e proteção de seus dados pessoais, que somente poderão ser utilizados para finalidades que: a) justifiquem sua coleta; b) não sejam vedadas pela legislação; e c) estejam especificadas nos contratos de prestação de serviços ou em termos de uso de aplicações de internet;
> **IX** - consentimento expresso sobre coleta, uso, armazenamento e tratamento de dados pessoais, que deverá ocorrer de forma destacada das demais cláusulas contratuais;
> **X** - exclusão definitiva dos dados pessoais que tiver fornecido a determinada aplicação de internet, a seu requerimento, ao término da relação entre as partes, ressalvadas as hipóteses de guarda obrigatória de registros previstas nesta Lei **e na que dispõe sobre a proteção de dados pessoais**; *(Redação dada pela Lei nº 13.709, de 2018)*
> [...]
> **XIII** - aplicação das normas de proteção e defesa do consumidor nas relações de consumo realizadas na internet.

**Literal — dispositivo conexo, art. 8º.**
> **Art. 8º** A garantia do direito à privacidade e à liberdade de expressão nas comunicações é condição para o pleno exercício do direito de acesso à internet.
> Parágrafo único. São **nulas de pleno direito** as cláusulas contratuais que violem o disposto no caput, tais como aquelas que:
> I - impliquem ofensa à inviolabilidade e ao sigilo das comunicações privadas, pela internet; ou
> **II - em contrato de adesão, não ofereçam como alternativa ao contratante a adoção do foro brasileiro para solução de controvérsias decorrentes de serviços prestados no Brasil.**

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm#art7 · verificado em 2026-08-11 · art. 8º em https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm#art8 · CDC, art. 51, VII, em https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O inciso VII é a base direta: fornecer dados pessoais a terceiro, aqui o provedor de LLM, exige consentimento livre, expresso e informado, ou hipótese legal. Combina com a LGPD, art. 11, para dado sensível de saúde, que exige consentimento específico e destacado, ou uma das hipóteses do inciso II, entre elas a alínea "f", "tutela da saúde, exclusivamente, em procedimento realizado por profissionais de saúde, serviços de saúde ou autoridade sanitária", redação da Lei 13.853/2019.

O inciso IX, somado ao art. 8º, parágrafo único, II, tem valor prático imediato. Cláusula de foro estrangeiro em termos de uso de provedor de LLM, em contrato de adesão, sem oferecer o foro brasileiro como alternativa, é nula de pleno direito. Isto é texto expresso, e alcança foro.

Arbitragem é outra coisa. O art. 8º, parágrafo único, II, do Marco Civil não trata dela. A vedação à arbitragem compulsória em contrato de consumo tem outro fundamento: o CDC, art. 51, VII, que declara nula a cláusula que determine a utilização compulsória de arbitragem. Ao responder ao argumento de que os termos do fornecedor preveem arbitragem no exterior, citar o CDC, art. 51, VII, e não o Marco Civil.

O inciso XIII confirma a aplicação do CDC mesmo quando a relação é digital.

**Gatilhos.**
- termos de uso do provedor com foro ou arbitragem exclusivamente no exterior
- consentimento de tratamento embutido em cláusula geral, sem destaque
- ausência de fluxo de exclusão de dado a pedido do titular
- envio de dado a terceiro sem base legal registrada

**Relacionados.** MCI:art11 · CDC:art14 · LGPD:art11 · CFM-2454-2026:art6

---

## MCI:art10

**Ementa.** Guarda e disponibilização de registros, e dever de informar as medidas de segurança.

**Literal.**
> **Art. 10.** A guarda e a disponibilização dos registros de conexão e de acesso a aplicações de internet de que trata esta Lei, bem como de dados pessoais e do conteúdo de comunicações privadas, devem atender à preservação da intimidade, da vida privada, da honra e da imagem das partes direta ou indiretamente envolvidas.
> **§ 1º** O provedor responsável pela guarda somente será obrigado a disponibilizar os registros mencionados no caput, de forma autônoma ou associados a dados pessoais ou a outras informações que possam contribuir para a identificação do usuário ou do terminal, **mediante ordem judicial**, na forma do disposto na Seção IV deste Capítulo, respeitado o disposto no art. 7º.
> **§ 2º** O conteúdo das comunicações privadas somente poderá ser disponibilizado **mediante ordem judicial**, nas hipóteses e na forma que a lei estabelecer, respeitado o disposto nos incisos II e III do art. 7º.
> **§ 3º** O disposto no caput não impede o acesso aos dados cadastrais que informem qualificação pessoal, filiação e endereço, na forma da lei, pelas autoridades administrativas que detenham competência legal para a sua requisição.
> **§ 4º** As medidas e os procedimentos de segurança e de sigilo devem ser informados pelo responsável pela provisão de serviços de forma clara e atender a padrões definidos em regulamento, respeitado seu direito de confidencialidade quanto a segredos empresariais.

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm#art10 · verificado em 2026-08-11 · LGPD, art. 46, em https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O §4º fundamenta a exigência de transparência técnica do fornecedor de LLM: as medidas e os procedimentos de segurança e de sigilo devem ser informados de forma clara. Médico ou clínica que contrata IA sem obter documentação de segurança do fornecedor não pode alegar desconhecimento.

Combina com a LGPD, art. 46, verificado: *"Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito"*, e com o §2º do mesmo artigo: *"As medidas de que trata o caput deste artigo deverão ser observadas desde a fase de concepção do produto ou do serviço até a sua execução"*. Segurança e privacidade desde a concepção são texto expresso, não recomendação opcional.

**Gatilhos.**
- contratação de provedor sem documentação de segurança obtida e arquivada
- ausência de descrição de retenção e de acesso a logs no contrato
- entrega de registros a terceiro ou a autoridade sem ordem judicial nos casos dos §§1º e 2º

**Relacionados.** MCI:art11 · LGPD:art46 · CFM-2454-2026:art17

---

## MCI:art11

**Ementa.** Aplicação obrigatória da lei brasileira, inclusive a provedor sediado no exterior.

**Literal.**
> **Art. 11.** Em qualquer operação de coleta, armazenamento, guarda e tratamento de registros, de dados pessoais ou de comunicações por provedores de conexão e de aplicações de internet **em que pelo menos um desses atos ocorra em território nacional**, deverão ser **obrigatoriamente respeitados a legislação brasileira** e os direitos à privacidade, à proteção dos dados pessoais e ao sigilo das comunicações privadas e dos registros.
> **§ 1º** O disposto no caput aplica-se aos dados coletados em território nacional e ao conteúdo das comunicações, desde que pelo menos um dos terminais esteja localizado no Brasil.
> **§ 2º** O disposto no caput aplica-se **mesmo que as atividades sejam realizadas por pessoa jurídica sediada no exterior**, desde que oferte serviço ao público brasileiro ou pelo menos uma integrante do mesmo grupo econômico possua estabelecimento no Brasil.
> **§ 3º** Os provedores de conexão e de aplicações de internet deverão prestar, na forma da regulamentação, informações que permitam a verificação quanto ao cumprimento da legislação brasileira referente à coleta, à guarda, ao armazenamento ou ao tratamento de dados, bem como quanto ao respeito à privacidade e ao sigilo de comunicações.
> **§ 4º** Decreto regulamentará o procedimento para apuração de infrações ao disposto neste artigo.

**Literal — sanções, art. 12.**
> **Art. 12.** Sem prejuízo das demais sanções cíveis, criminais ou administrativas, as infrações às normas previstas nos arts. 10 e 11 ficam sujeitas, conforme o caso, às seguintes sanções, aplicadas de forma isolada ou cumulativa:
> I - advertência, com indicação de prazo para adoção de medidas corretivas;
> **II - multa de até 10% (dez por cento) do faturamento do grupo econômico no Brasil no seu último exercício**, excluídos os tributos, considerados a condição econômica do infrator e o princípio da proporcionalidade entre a gravidade da falta e a intensidade da sanção;
> III - suspensão temporária das atividades que envolvam os atos previstos no art. 11; ou
> IV - proibição de exercício das atividades que envolvam os atos previstos no art. 11.
> Parágrafo único. Tratando-se de empresa estrangeira, **responde solidariamente pelo pagamento da multa de que trata o caput sua filial, sucursal, escritório ou estabelecimento situado no País.**

**Fonte.** https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm#art11 · verificado em 2026-08-11 · art. 12 em https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm#art12 · LGPD, arts. 3º e 33, em https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Basta que um dos atos ocorra em território nacional. A coleta do dado de saúde ocorre no consultório. Ainda que armazenamento, inferência e logging ocorram inteiramente no exterior, a legislação brasileira é obrigatória. Isto é texto expresso.

O §2º alcança pessoa jurídica sediada no exterior que oferte serviço ao público brasileiro, ou cujo grupo econômico tenha estabelecimento no Brasil. Provedores de LLM que ofertam serviço em português, com faturamento em reais ou com entidade brasileira, estão alcançados.

O art. 12, parágrafo único, torna a filial brasileira solidária pela multa da matriz estrangeira, e o inciso II fixa teto de 10% do faturamento do grupo econômico no Brasil.

Redundância deliberada com a LGPD, art. 3º, verificado: *"Esta Lei aplica-se a qualquer operação de tratamento realizada por pessoa natural ou por pessoa jurídica de direito público ou privado, independentemente do meio, do país de sua sede ou do país onde estejam localizados os dados, desde que: I - a operação de tratamento seja realizada no território nacional; II - a atividade de tratamento tenha por objetivo a oferta ou o fornecimento de bens ou serviços ou o tratamento de dados de indivíduos localizados no território nacional (Redação dada pela Lei nº 13.853, de 2019); ou III - os dados pessoais objeto do tratamento tenham sido coletados no território nacional. § 1º Consideram-se coletados no território nacional os dados pessoais cujo titular nele se encontre no momento da coleta."*

Enviar dado de paciente a LLM hospedado no exterior é transferência internacional e exige uma das bases da LGPD, art. 33 — na prática, cláusulas contratuais específicas ou cláusulas-padrão comprovadas, do inciso II. Conta pessoal ou gratuita sem instrumento contratual não satisfaz o inciso II, que é o caminho usual para uso institucional.

O art. 33 tem nove incisos. Só o inciso II depende de instrumento contratual. Conferido no texto compilado em 11/08/2026: os outros oito não exigem contrato, e cinco deles são invocáveis por agente privado fora de contexto de órgão público — o I (país com grau de proteção adequado reconhecido pela ANPD), o IV (proteção da vida ou da incolumidade física), o V (autorização da autoridade nacional), o VIII (consentimento específico e em destaque do titular para a transferência, com informação prévia sobre o caráter internacional da operação) e o IX (hipóteses dos incisos II, V e VI do art. 7º). Os incisos III, VI e VII também dispensam contrato, mas pressupõem cooperação jurídica internacional, acordo de cooperação ou execução de política pública. Dizer que a conta pessoal não satisfaz "nenhum inciso" é falso, e qualquer leitor que abra o art. 33 desfaz o argumento.

O inciso VIII merece nota, porque é o que o médico tende a invocar. Consentimento como base de transferência não resolve o caso clínico por três razões, todas de texto: ele não dispensa base autônoma do art. 11 para dado sensível; é revogável pelo titular a qualquer momento; e não substitui os deveres de segurança do art. 46 nem os deveres do CFM. Consentimento válido para transferir não torna lícito o tratamento a jusante.

**Gatilhos.**
- endpoint de provedor em região fora do Brasil sem instrumento de transferência internacional
- termos de uso do provedor sem entidade ou foro no Brasil
- uso de conta pessoal ou gratuita para enviar dado de paciente a serviço estrangeiro
- ausência de documentação de cláusulas-padrão ou específicas de transferência

**Incerteza.** **NÃO VERIFICADO:** quais países foram reconhecidos pela ANPD como de grau de proteção adequado, e o teor atual da regulamentação da ANPD sobre transferência internacional e cláusulas-padrão. Requer verificação autônoma em gov.br/anpd antes de qualquer afirmação. **NÃO VERIFICADO** também o prazo definido pela ANPD para a comunicação de incidente da LGPD, art. 48, §1º.

**Relacionados.** MCI:art7 · MCI:art10 · LGPD:art33 · LGPD:art3 · LGPD:art48 · CFM-2454-2026:art6

---

# Jurisprudência do STJ

Advertência metodológica, refeita na reauditoria de 11/08/2026 com os acessos testados um a um.

O que responde e o que não responde:
- `processo.stj.jus.br` bloqueia acesso automatizado.
- A busca de acórdãos em `scon.stj.jus.br/SCON/pesquisar.jsp` devolve HTTP 403 a cliente automatizado. Não foi possível ler ementa nem inteiro teor por essa via.
- O Informativo de Jurisprudência em `scon.stj.jus.br/jurisprudencia/externo/informativo/` responde com HTTP 200. Todas as identificações processuais e todos os campos DESTAQUE desta seção vieram daí. Cada precedente traz o permalink da própria nota, no formato `?livre=@CNOT=nnnnnn`.
- Notícias oficiais em `www.stj.jus.br` devolvem HTTP 403 a curl e respondem a leitura por navegador. São fonte oficial, mas de redação jornalística: o que está fora de aspas na notícia é do redator, não do voto.

A afirmação anterior desta ficha, de que "`scon.stj.jus.br` não bloqueia", era ampla demais. O domínio bloqueia a pesquisa de acórdãos e libera o Informativo.

**Regra de campo.** O campo `Tese` só recebe o DESTAQUE oficial do Informativo, que é a tese publicada pelo tribunal. Frase colhida em "Informações do Inteiro Teor", em título de verbete ou em notícia é fundamentação ou descrição, vai em campo separado e não é tese. Na reauditoria, sete entradas tinham no campo `Tese` texto que não era o DESTAQUE: `STJ:AREsp2130619`, `STJ:REsp2201694`, `STJ:REsp2077278`, `STJ:REsp2135783`, `STJ:REsp2092096`, `STJ:REsp1914596` e `STJ:RMS55819`. Todas foram corrigidas, e a correção está registrada em cada uma.

**O inteiro teor dos acórdãos continua não lido.** Por isso nenhum precedente desta seção passa de `primária-parcial`. Não citar processo que não esteja nesta seção.

---

## STJ:AREsp2130619

**Ementa.** Vazamento de dado pessoal comum não gera dano moral presumido.

| Campo | Conteúdo |
|---|---|
| Processo | AREsp 2.130.619-SP |
| Órgão | Segunda Turma |
| Relator | Ministro Francisco Falcão |
| Julgamento | 07/03/2023, unânime — DJe 10/03/2023 |
| Informativo | STJ, Informativo de Jurisprudência n. 766, de 14/03/2023 |
| Dados envolvidos | Comuns: nome, data de nascimento, endereço, número de documento. Não envolvia dado sensível |

**Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=019794 · verificado em 2026-08-11
**Confiança.** primária-parcial

**Tese.** DESTAQUE oficial do Informativo n. 766, transcrito na íntegra: *"O vazamento de dados pessoais não gera dano moral presumido."*

O destaque tem uma frase só e não traz o qualificativo "comuns". É mais amplo do que a leitura de que só o dado comum está coberto. O caso julgado, porém, envolvia dados comuns.

**Correção da redação anterior.** A frase antes registrada aqui como DESTAQUE — *"O vazamento de dados pessoais, a despeito de se tratar de falha indesejável no tratamento de dados de pessoa natural por pessoa jurídica, não tem o condão, por si só, de gerar dano moral indenizável."* — não é o DESTAQUE. Ela está em "Informações do Inteiro Teor" do mesmo verbete. É fundamentação, e continua transcrita corretamente, mas não é a tese publicada.

**Fundamentação, do campo "Informações do Inteiro Teor" do Informativo 766.** *"Os dados objeto da lide são aqueles que se fornece em qualquer cadastro, inclusive nos sites consultados no dia a dia, não sendo, portanto, acobertados por sigilo, e o conhecimento por terceiro em nada violaria o direito de personalidade da recorrida."* Em seguida: *"Ou seja, o dano moral não é presumido, sendo necessário que o titular dos dados comprove eventual dano decorrente da exposição dessas informações."*

**Obiter em sentido contrário, sobre dado sensível.** Também do campo "Informações do Inteiro Teor": *"Diferente seria se, de fato, estivéssemos diante de vazamento de dados sensíveis, que dizem respeito à intimidade da pessoa natural."* **É obiter dictum, não tese firmada.** Não sustenta afirmação de que vazamento de dado de saúde gera dano moral presumido. É a melhor indicação disponível da direção da Corte, e nada além disso.

**Trecho retirado na reauditoria.** A redação anterior atribuía ao colegiado a expressão *"salvo no caso de informações consideradas sensíveis"*. A expressão não aparece no verbete do Informativo 766 nem na notícia oficial. Sem fonte oficial que a sustente, foi removida. Não citar.

**Verificação.** Verbete completo do Informativo de Jurisprudência n. 766, de 14/03/2023, lido em 11/08/2026 em https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=019794 — identificação processual completa: processo, relator, órgão, unanimidade, data de julgamento e DJe, além do DESTAQUE e do campo de fundamentação. Notícia oficial do STJ, também consultada em 11/08/2026: https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2023/17032023-Titular-de-dados-vazados-deve-comprovar-dano-efetivo-ao-buscar-indenizacao--decide-Segunda-Turma.aspx — confirma processo, relator, órgão e o caso concreto, concessionária de energia elétrica e cliente idoso. **Inteiro teor não lido.**

**Incerteza.** O verbete do Informativo 766 é intitulado *"Vazamento de dados pessoais. Dados comuns e sensíveis. Dano moral presumido. Impossibilidade."* O título e o destaque puxam para a leitura ampla; o obiter transcrito acima puxa para a restrita. As duas leituras estão no mesmo julgado. **Não se pode afirmar, a partir deste precedente, que vazamento de dado de saúde gera dano moral presumido. O precedente não decidiu isso. Afirmação nesse sentido é TESE NÃO VERIFICADA.**

---

## STJ:REsp2147374

**Ementa.** Vazamento por ataque externo não afasta os deveres de informação do agente de tratamento perante o titular.

| Campo | Conteúdo |
|---|---|
| Processo | REsp 2.147.374-SP |
| Órgão | Terceira Turma |
| Relator | Ministro Ricardo Villas Bôas Cueva |
| Julgamento | 03/12/2024, unânime — DJEN 06/12/2024 |
| Informativo | STJ, Informativo de Jurisprudência n. 838, de 04/02/2025 |
| Dados envolvidos | Não sensíveis |

**Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=021293 · verificado em 2026-08-11
**Confiança.** primária-parcial

**Título do verbete oficial, íntegro.** *"Lei Geral de Proteção de Dados Pessoais. Direito à privacidade, à liberdade e à autodeterminação informativa. Agente de tratamento. Vazamento de dados não sensíveis do titular. Incidente de segurança. Ataque hacker. Responsabilidade exclusiva de terceiro. Não comprovada. Responsabilidade civil proativa. Expectativa de legítima proteção. Compliance e regulação de risco da atividade. Direitos do titular. Concretização. Aplicabilidade."*

O título não é truncado na fonte oficial. O truncamento estava na fonte secundária usada na primeira redação desta ficha.

**Tese.** Campo DESTAQUE do Informativo n. 838, transcrito: *"É passível a imputação das obrigações previstas no art. 19, II, da Lei Geral de Proteção de Dados Pessoais (LGPD), ao agente de tratamento de dados, na ocasião de vazamento de dados pessoais não sensíveis do titular, decorrente de atividade alegadamente ilícita (ataque hacker)."*

**Aplicação.** O que o julgado firmou é um dever de informação, não um dever de indenizar. O ataque externo não afasta as obrigações do art. 19, II, da LGPD: prestar ao titular, em até 15 dias, declaração clara e completa sobre a origem dos dados, os critérios utilizados e a finalidade do tratamento. Clínica ou hospital que sofre exfiltração continua obrigado a responder ao paciente que pergunta o que foi tratado, de onde veio e para quê. Consequência operacional: manter registro das operações de tratamento e da origem dos dados é condição para cumprir o prazo de 15 dias.

Os elementos "Responsabilidade exclusiva de terceiro. Não comprovada" constam do tema do verbete. São descrição do caso julgado, não tese. Não usar este precedente para afirmar que o agente tem o ônus de provar a inevitabilidade do incidente. Essa proposição é leitura nossa sobre o art. 43, III, da LGPD, e está em `CC:art927`.

**Verificação.** Verbete completo do Informativo de Jurisprudência n. 838, de 04/02/2025, lido em 11/08/2026 em https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=021293 — identificação processual completa, título, DESTAQUE e campo de fundamentação. Reconferidos nesta reauditoria, contra a fonte, o número do processo, o órgão, o relator, a votação por unanimidade, a data de julgamento e o DJEN. Todos conferem. **Inteiro teor não lido.** Não citar fundamentação do acórdão como se fosse tese.

**Incerteza.** **Não afirmar qual regime de responsabilidade foi fixado no acórdão, objetiva ou subjetiva. NÃO VERIFICADO.** O acórdão trata de dados não sensíveis. A extensão do dever do art. 19, II, a incidente com dado de saúde é leitura nossa, sustentada no texto da LGPD, que não distingue nesse ponto.

**Relacionados.** CC:art927 · CDC:art14 · LGPD:art43

---

## STJ:REsp2201694

**Ementa.** Disponibilização deliberada de informação cadastral a terceiro gera dano moral presumido.

| Campo | Conteúdo |
|---|---|
| Processo | REsp 2.201.694-SP |
| Órgão | Terceira Turma |
| Relator | Ministro Ricardo Villas Bôas Cueva |
| Relatora para acórdão | Ministra Nancy Andrighi |
| Julgamento | 05/08/2025, por maioria — DJEN 15/08/2025 |
| Informativo | STJ, Informativo de Jurisprudência, Edição Extraordinária n. 29, de 20/01/2026 |
| Dados envolvidos | Não sensíveis. A notícia registra que "os dados compartilhados não eram sensíveis", embora o acórdão tenha reconhecido caráter sigiloso ao número de telefone |

**Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=022029 · verificado em 2026-08-11
**Confiança.** primária-parcial

Houve divergência. Nancy Andrighi não foi relatora do recurso: foi relatora para acórdão, com o voto que prevaleceu. A linha de identificação no Informativo é *"REsp 2.201.694-SP, Rel. Ministro Ricardo Villas Bôas Cueva, Rel. para acórdão Ministra Nancy Andrighi, Terceira Turma, por maioria, julgado em 5/8/2025, DJEN 15/8/2025"*. A data 05/09/2025, registrada na primeira redação desta ficha, é a da notícia no portal, não a do julgamento.

**Título do verbete oficial.** *"Banco de dados para a formação de histórico de crédito. Lei n. 12.414/2011. Disponibilização de dados cadastrais e de adimplemento sem a prévia autorização do cadastrado. Disponibilização indevida. Dano moral presumido."*

**Tese.** DESTAQUE oficial do Informativo Edição Extraordinária n. 29, transcrito: *"O gestor de banco de dados para formação de histórico de crédito, que disponibiliza para terceiros consulentes o acesso a informações cadastrais e de adimplemento, sem a prévia autorização do cadastrado, deve responder objetivamente pelos danos morais, que são presumidos."*

O advérbio "objetivamente" está no destaque e fixa o regime de responsabilidade. Não pode ser suprimido na citação. A tese é restrita a gestor de banco de dados sob a Lei nº 12.414/2011, e a decisão foi por maioria.

**Correção da redação anterior.** O campo `Tese` trazia uma frase da notícia do portal — *"o gestor de banco de dados que, em desacordo com a legislação, disponibiliza a terceiros informações cadastrais ou de adimplemento do consumidor deve responder objetivamente pelos danos morais causados"* —, que é paráfrase jornalística da conclusão do voto vencedor, não o DESTAQUE. Foi substituída pelo destaque oficial. O sentido não muda, mas a frase da notícia não é a tese publicada e não deve ser citada como tal.

**Fundamentação, do campo "Informações do Inteiro Teor".** O verbete registra que a Terceira Turma já decidira no mesmo sentido no REsp 2.115.461/SP e no REsp 2.133.261/SP, e transcreve daquele julgamento: *"se um terceiro consulente tem interesse em obter as informações cadastrais do cadastrado, ainda que sejam dados pessoais não sensíveis, deve ele obter o prévio e expresso consentimento do titular, com base na autonomia da vontade, pois não há autorização legal para que o gestor de banco de dados disponibilize tais dados aos consulentes."* Registra ainda que não se aplicam o Tema 710/STJ nem a Súmula 550/STJ, que tratam de credit scoring. **Os REsp 2.115.461/SP e 2.133.261/SP não foram verificados nesta pesquisa. Não citar por número.**

**Trecho da notícia oficial.** Entre aspas na fonte, sobre os danos: *"são presumidos, diante da forte sensação de insegurança"*. As expressões "esses danos" e "experimentada pela vítima" são do redator da notícia, fora das aspas, e não integram a citação.

**Verificação.** Verbete completo do Informativo de Jurisprudência, Edição Extraordinária n. 29, de 20/01/2026, lido em 11/08/2026 em https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=022029 — identificação processual completa, incluindo relator, relatora para acórdão, órgão, julgamento por maioria, data e DJEN, além do título, do DESTAQUE e da fundamentação. Notícia oficial do STJ também consultada em 11/08/2026: https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2025/05092025-Disponibilizacao-indevida-de-informacoes-pessoais-em-banco-de-dados-gera-dano-moral-presumido.aspx **Inteiro teor não lido.**

**Incerteza.** O resultado diverge do AREsp 2.130.619. A distinção fática entre vazamento acidental e disponibilização deliberada a terceiro sem base legal é sustentável. A aproximação entre esse segundo grupo e o envio de dado a fornecedor de LLM — que não é vazamento acidental, mas disponibilização deliberada — **é argumento interpretativo nosso, não tese do STJ. Doutrina.**

O regime objetivo nomeado no voto vencedor vale para gestor de banco de dados sob a Lei nº 12.414/2011. Não foi estendido a agente de tratamento em saúde, nem fundado no art. 927, parágrafo único, do CC. A decisão foi por maioria, o que reduz seu peso como sinal de orientação da Turma. Ver `CC:art927`.

---

## STJ:REsp2221650

**Ementa.** Dado não sensível em cadastro positivo. Distinção entre dado sensível e dado comum como critério de presunção do dano.

| Campo | Conteúdo |
|---|---|
| Processo | REsp 2.221.650-SP |
| Órgão | Quarta Turma |
| Relatora | Ministra Maria Isabel Gallotti |
| Julgamento | 04/11/2025, por unanimidade |
| Informativo | STJ, Informativo de Jurisprudência n. 871, de 18/11/2025 |
| Dados envolvidos | Não sensíveis |

**Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=021939 · verificado em 2026-08-11
**Confiança.** primária-parcial

A data 13/02/2026, registrada na primeira redação desta ficha, é a da notícia no portal, não a do julgamento. O Informativo não registra DJe para este acórdão.

**Título do verbete oficial.** *"Disponibilização de dados pessoais não sensíveis. Lei Geral de Proteção de Dados (LGPD). Lei do Cadastro Positivo. Ausência de consentimento prévio. Ausência de dano moral presumido (in re ipsa)."*

**Tese.** DESTAQUE oficial do Informativo n. 871, transcrito na íntegra: *"A disponibilização de dados pessoais, por si só, não configura dano moral presumido, sendo imprescindível a comprovação de que a conduta do gestor de banco de dados resultou em abalo significativo aos direitos de personalidade do titular."*

**Correção da redação anterior.** Duas coisas foram corrigidas aqui. Primeira: o destaque não está truncado na fonte. A redação anterior o dava como *"[...] sendo imprescindível a comprova[ção] [...]"*, com colchete de completação; o texto integral está acima. Segunda: o trecho antes citado entre aspas — *"é indispensável a comprovação de que a conduta do gestor do banco de dados causou abalo significativo"* — não corresponde ao texto oficial, que diz "imprescindível", "gestor de banco de dados" e "resultou em abalo significativo aos direitos de personalidade do titular". Não citar a versão antiga.

**Distinção entre dado sensível e comum.** Do campo "Informações do Inteiro Teor", transcrito: *"[...] diferentemente dos dados sensíveis, cuja proteção é reforçada em razão de seu potencial discriminatório, os dados pessoais correspondem às informações ordinárias, frequentemente fornecidas em cadastros diversos, inclusive em plataformas digitais de uso cotidiano, não estando, via de regra, submetidos a regime jurídico de sigilo."* É fundamentação, não tese.

O mesmo campo registra que a Segunda Turma decidiu no mesmo sentido no AREsp 2.130.619/SP. As duas entradas desta ficha convergem.

**Verificação.** Verbete completo do Informativo de Jurisprudência n. 871, de 18/11/2025, lido em 11/08/2026 em https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=021939 — identificação processual completa, título, DESTAQUE integral e fundamentação. Notícia oficial do STJ também consultada em 11/08/2026: https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/13022026-Disponibilizacao-nao-autorizada-de-dados-pessoais-nao-sensiveis-em-cadastro-positivo-nao-gera-dano-moral-presumido.aspx **Inteiro teor não lido.**

**Incerteza.** Verificado: a Corte reconhece o regime diferenciado do dado sensível. **Não verificado: que a Corte tenha decidido que dado sensível de saúde gera dano moral in re ipsa.** Os quatro precedentes acima tratam de dados não sensíveis.

---

## Outros precedentes de LGPD identificados

A redação anterior desta seção tinha fonte única, a notícia oficial do STJ de 27/10/2024 sobre os quatro primeiros anos da LGPD. Na reauditoria de 11/08/2026 cada um dos cinco processos foi reaberto no Informativo de Jurisprudência, com permalink próprio. A identificação processual mudou em dois casos e o campo de tese mudou em quatro.

| Id | Identificação processual, conforme o Informativo | Tese — DESTAQUE oficial |
|---|---|---|
| STJ:REsp2077278 | REsp 2.077.278-**SP**, Rel. Ministra Nancy Andrighi, Terceira Turma, por unanimidade, julgado em 3/10/2023, DJe 9/10/2023. Informativo n. 791, de 18/10/2023 | *"A instituição financeira responde pelo defeito na prestação de serviço consistente no tratamento indevido de dados pessoais bancários, quando tais informações são utilizadas por estelionatário para facilitar a aplicação de golpe em desfavor do consumidor."* O título do verbete invoca a Súmula 479/STJ |
| STJ:REsp2135783 | REsp 2.135.783-**DF**, Relatoria Ministra Nancy Andrighi, Terceira Turma, por unanimidade, julgado em 18/6/2024, DJe 21/6/2024. Informativo n. 817, de 25/06/2024 | *"Não há óbice para a imediata suspensão do perfil profissional de motorista de aplicativo que pratica ato suficientemente gravoso, com a possibilidade de posterior exercício de defesa visando ao recredenciamento."* |
| STJ:REsp2092096 | REsp 2.092.096-**SP**, Rel. Ministra Nancy Andrighi, Terceira Turma, por unanimidade, julgado em 12/12/2023, DJe 15/12/2023. Informativo n. 799, de 19/12/2023 | *"A B3, na condição de agente de tratamento de dados, tem a obrigação de excluir os dados cadastrais inseridos indevidamente por terceiros que obtiveram acesso não autorizado ao perfil do investidor em sua plataforma virtual."* O mesmo julgamento gerou segunda nota, com o destaque *"A LGPD e o Marco Civil da Internet são aplicáveis aos dados armazenados e transmitidos pela B3, no âmbito de plataforma virtual por ela mantida."* |
| STJ:REsp1914596 | REsp 1.914.596-**RJ**, Rel. Min. Luis Felipe Salomão, Quarta Turma, por unanimidade, julgado em **23/11/2021**. Informativo n. 720, de 06/12/2021 | *"Os provedores de conexão à internet devem fornecer os dados cadastrais (nome, endereço, RG e CPF) dos usuários responsáveis por publicação de vídeos no Youtube com ofensas à memória de pessoa falecida."* |
| STJ:RMS55819 | **AgInt nos EDcl no** RMS 55.819-**MG**, Rel. Min. Gurgel de Faria, Primeira Turma, por unanimidade, julgado em 08/08/2022, DJe 17/08/2022. Informativo n. 747, de 05/09/2022 | *"Não extrapola o poder regulamentar da Administração Pública, ou os princípios que a regem, Decreto Estadual que dispõe sobre o dever de agentes púbicos disponibilizarem informações sobre seus bens e evolução patrimonial."* A grafia "púbicos" está na fonte |

**Fonte e confiança, por precedente.** Verbete do Informativo lido na íntegra em cada caso, inteiro teor não lido em nenhum.

- `STJ:REsp2077278` — **Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=020280 · verificado em 2026-08-11 · **Confiança.** primária-parcial
- `STJ:REsp2135783` — **Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=020795 · verificado em 2026-08-11 · **Confiança.** primária-parcial
- `STJ:REsp2092096` — **Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=020378 · verificado em 2026-08-11 · **Confiança.** primária-parcial
- `STJ:REsp1914596` — **Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=018693 · verificado em 2026-08-11 · **Confiança.** primária-parcial
- `STJ:RMS55819` — **Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=019324 · verificado em 2026-08-11 · **Confiança.** primária-parcial

**Correções feitas nesta reauditoria.** Cinco, todas conferidas contra o Informativo:

1. **`STJ:REsp2135783` tinha tese que o tribunal não firmou.** A ficha atribuía a este acórdão a tese de que "decisão automatizada e perfilamento por algoritmo são tratamento de dados sob a LGPD" e de que "o titular tem direito de saber a razão e de pedir revisão". O DESTAQUE decide o oposto no ponto processual: a suspensão imediata do perfil é possível, e a notificação prévia é desnecessária. A proposição sobre informação e revisão está na fundamentação, e não isolada: *"[...] entende-se que o titular de dados pessoais deve ser informado sobre a razão da suspensão de seu perfil, bem como pode requerer a revisão dessa decisão, garantido o seu direito de defesa."* Continua sendo o precedente mais próximo de decisão algorítmica no levantamento, e não trata de saúde. **Citar como fundamentação, nunca como tese.**
2. **`STJ:REsp1914596` estava com o ano errado.** Julgado em 23/11/2021, não em 2022. Também faltava a UF: é -RJ. Além disso, a frase antes citada entre aspas — *"A LGPD não exclui a possibilidade da quebra de sigilo. Ao contrário, apresenta regras sobre tal ocorrência"* — só tem primeira parte confirmada. O Informativo traz *"Assim, a LGPD não exclui a possibilidade da quebra de sigilo."* A segunda oração não consta do verbete e foi retirada. O verbete do STJ grafa a LGPD como "Lei n. 13.790/2018"; o número correto é 13.709/2018.
3. **`STJ:RMS55819` estava com identificação processual incompleta.** O julgado do Informativo é o AgInt nos EDcl no RMS 55.819-MG, não o RMS. A tese antes atribuída, "direito à proteção de dados não é absoluto e se compatibiliza com transparência administrativa", é síntese nossa da fundamentação, não o destaque. A fundamentação registra, em transcrição conferida: *"A entrega dos dados à Administração não implica dizer que eles deverão ser expostos ao público em geral, cabendo àquela, já com as informações em mãos, adotar as cautelas necessárias para dar concretude ao art. 5º, LXXIX, da CF/1988, e à Lei Geral de Proteção de Dados Pessoais (LGPD) [...]."*
4. **`STJ:REsp2077278` tinha aspas em texto que não é do julgado.** A frase *"O tratamento indevido de dados pessoais bancários configura defeito na prestação de serviço, notadamente quando tais informações são utilizadas por estelionatário"* não aparece no verbete. É paráfrase do destaque. Substituída pelo destaque.
5. **`STJ:REsp2092096` tinha acréscimo à tese.** A expressão "mediante requisição do titular" não está no destaque. Retirada.

**Verificação.** Verbete de Informativo de cada um dos cinco processos, lido na íntegra em 11/08/2026 nos permalinks acima: identificação processual, órgão, relator, votação, data de julgamento, DJe quando publicado, título e DESTAQUE. **Inteiro teor não lido em nenhum deles.**

---

## Responsabilidade civil médica e inversão do ônus da prova

| Id | Processo | Órgão e relator | Conteúdo |
|---|---|---|---|
| STJ:AgIntAREsp1872697 | AgInt no AREsp n. 1.872.697/DF | 1ª Turma, Rel. Min. Sérgio Kukina — DJe 24/02/2022 | Acórdão indicado pelo STJ como representativo do tema de Pesquisa Pronta de responsabilidade civil por erro médico. **Não há DESTAQUE de Informativo para este processo: a busca no Informativo de Jurisprudência por "1872697" não retorna resultado.** A proposição de que, comprovada a hipossuficiência técnica do autor, cabe a inversão do ônus da prova ao réu é síntese nossa do tema, não tese transcrita de fonte oficial |
| STJ:REsp1985977 | REsp 1.985.977-DF | 1ª Turma, Rel. Min. Sérgio Kukina, por unanimidade, j. 18/06/2024, DJe 26/06/2024 | Título do verbete: *"Responsabilidade civil do Estado. Erro na prestação de serviços médico-hospitalares. Morte de bebê. Descumprimento de orientação do Ministério da Saúde. Inversão do ônus da prova. Teoria da perda de uma chance."* DESTAQUE oficial: *"Aplica-se a responsabilidade civil pela perda de uma chance no caso de atuação dos profissionais médicos que não observam orientação do Ministério da Saúde, retirando do paciente uma chance concreta e real de ter um diagnóstico correto e de alçar as consequências normais que dele se poderia esperar."* A inversão do ônus da prova aparece no título do verbete, não no destaque |

**Fonte e confiança, por precedente.** URLs verificadas em 2026-08-11.

- `STJ:AgIntAREsp1872697` — **Fonte.** https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/26052022-Pesquisa-Pronta-destaca-erro-medico-e-nao-cabimento-de-embargos-de-divergencia-contra-monocratica-.aspx · verificado em 2026-08-11 · **Confiança.** primária-parcial. A notícia oficial confirma processo, relator, órgão e DJe. Não há verbete de Informativo, e o inteiro teor não foi lido. Não citar tese.
- `STJ:REsp1985977` — **Fonte.** https://scon.stj.jus.br/jurisprudencia/externo/informativo/?livre=@CNOT=020822 · verificado em 2026-08-11 · **Confiança.** primária-parcial. Verbete da Edição Extraordinária n. 19, de 16/07/2024, lido na íntegra, com identificação processual, título e DESTAQUE. Inteiro teor não lido.

**Aplicação.** A inversão do ônus da prova por hipossuficiência técnica é o vetor processual decisivo no cenário de LLM. O paciente não tem como provar que seu dado foi enviado a um modelo. A prova documental do pipeline é do médico ou da clínica: logs, contrato de tratamento de dados, política de retenção e relatório de impacto. Duas bases de texto expresso sustentam isso: a inversão consumerista do CDC e o art. 42, §2º, da LGPD. Os dois acórdãos acima indicam que o tribunal trabalha com inversão em erro médico, mas nenhum deles firmou tese sobre o ponto em destaque publicado. **Não apresentar essa linha jurisprudencial como tese fixada.**

---

## STJ:sem-numero-2021 — precedente não citável por número

Tese divulgada em notícia oficial do STJ de 29/07/2021, Terceira Turma, Rel. Min. Ricardo Villas Bôas Cueva: *"a responsabilidade do médico é subjetiva e fica configurada se demonstrada a culpa, nos termos do CDC, pois sua atividade é obrigação de meio"*. Trecho adicional: *"O nexo de causalidade, como pressuposto da responsabilidade civil, é mais bem aferido, no plano jurídico-normativo, segundo a teoria da causalidade adequada"*.

**O número do processo não foi divulgado pelo STJ, por segredo de justiça. NÃO CITÁVEL POR NÚMERO.** Usar apenas como referência de notícia oficial.

A reauditoria de 11/08/2026 releu a notícia e confirmou: ausência de número por segredo de justiça, Terceira Turma, relator Ministro Ricardo Villas Bôas Cueva, e a presença dos dois trechos entre aspas transcritos acima. Não há verbete de Informativo correspondente, porque o processo corre em segredo.

**Fonte.** https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/29072021-Mantida-condenacao-de-medico-que-negligenciou-preenchimento-de-prontuario-de-gestante.aspx · verificado em 2026-08-11
**Confiança.** primária-parcial

---

## Itens NÃO VERIFICADOS nesta ficha

- Precedente do STJ que aplique o art. 927, parágrafo único, do CC a tratamento de dados por IA.
- Decisão consolidada do STJ sobre dano moral por vazamento de dado de saúde. Os quatro precedentes principais tratam de dados não sensíveis. Lacuna jurisprudencial real, reconfirmada em busca dirigida em 11/08/2026. O único sinal em sentido contrário é obiter dictum no AREsp 2.130.619, registrado em `STJ:AREsp2130619`. Obiter não é tese.
- Tema repetitivo ou súmula do STJ sobre o alcance do art. 14, §4º, do CDC quanto ao hospital, aplicado a vazamento de dados.
- Decisão de qualquer tribunal sobre uso de LLM ou IA generativa com dado de paciente. Nenhuma encontrada.
- Decisão do STJ sobre quebra de sigilo médico ou divulgação de diagnóstico com número de processo. Não encontrada.
- Inteiro teor de todos os acórdãos desta ficha. Nenhum foi lido. Por isso nenhum precedente passa de `primária-parcial`.
- Teor da Súmula 479/STJ, citada no verbete do REsp 2.077.278. Não citar teor.
- Teor da Súmula 550/STJ e do Tema 710/STJ, citados no verbete do REsp 2.201.694 como inaplicáveis ao caso. Não citar teor.
- Teor da Súmula 608/STJ.
- REsp 2.115.461/SP e REsp 2.133.261/SP, citados como precedentes da Terceira Turma no verbete do REsp 2.201.694. Não pesquisados.
- Trecho do AgInt no REsp 2.220.066/TO em fonte do próprio STJ. Verificado apenas na sistematização do TJDFT.
- Tese firmada em destaque publicado sobre inversão do ônus da prova por hipossuficiência técnica em erro médico. Os dois acórdãos levantados não têm destaque nesse sentido.
- Edição e enunciados da Jurisprudência em Teses do STJ sobre responsabilidade civil médica e hospitalar.
- Decisões e sanções da ANPD sobre dados de saúde ou IA. Não pesquisadas.
- Países reconhecidos pela ANPD como de grau de proteção adequado, e teor atual da regulamentação da ANPD sobre transferência internacional e cláusulas-padrão.
- Prazo definido pela ANPD para a comunicação de incidente (LGPD, art. 48, §1º).
- Objeto e resultado das ADI 7055 e ADI 6792, referenciadas como "Vide" ao lado dos arts. 186 e 927 do CC. A nota "Vide" no Planalto é remissão, não alteração de texto. Não afirmar que afetam a redação.
- Texto da CF, art. 37, §6º, referido no bruto como base da responsabilidade do Estado.
- Número do processo da tese de responsabilidade subjetiva do médico divulgada em 29/07/2021. Segredo de justiça.

---

## Fontes primárias desta ficha

| Norma | URL | Verificado |
|---|---|---|
| Código Civil (Lei 10.406/2002, compilado) | https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm | 2026-08-11 |
| CDC (Lei 8.078/1990, compilado) | https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm | 2026-08-11 |
| Marco Civil da Internet (Lei 12.965/2014) | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm | 2026-08-11 |
| LGPD (Lei 13.709/2018, compilada) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm | 2026-08-11 |
| EC 115/2022 (CF, art. 5º, LXXIX) | https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc115.htm | 2026-08-11 |
| STJ — Informativo de Jurisprudência | permalinks `?livre=@CNOT=nnnnnn` em cada precedente | 2026-08-11 |
| STJ — notícias oficiais | URLs individuais em cada precedente | 2026-08-11 |
| TJDFT — sistematização de jurisprudência sobre CDC (fonte secundária) | https://www.tjdft.jus.br/consultas/jurisprudencia/jurisprudencia-em-temas/cdc-na-visao-do-tjdft-1/responsabilidade-civil-no-cdc/responsabilidade-do-hospital-quanto-a-atuacao-tecnico-profissional-do-medico | 2026-08-11 |
