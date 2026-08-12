---
tipo: decisões de projeto
versao: 1
atualizado: 2026-08-11
---

# Decisões que as diretrizes seguem

Sete decisões que resolvem pontos onde o corpus é ambíguo, onde a norma exige recorte, ou onde vários arquivos divergiam. Toda diretriz precisa estar conforme a este documento. A auditoria de 11/08/2026 mostrou que a ausência destas decisões produziu erro repetido em seis arquivos.

Estas decisões são nossas. Não são norma. Cada uma diz em que se apoia e onde é leitura, não texto.

---

## R1 — Vigência da Resolução CFM 2.454/2026

A resolução entra em vigor em **26 de agosto de 2026**. Até 25/08/2026 ela não produz efeitos.

Regra: toda diretriz que dependa dela traz a marcação abaixo, no início do bloco.

> Vale a partir de 26/08/2026.

O arquivo que tiver mais de três diretrizes dependentes traz também esta nota no cabeçalho:

> Parte destas diretrizes decorre da Res. CFM 2.454/2026, em vigor a partir de 26/08/2026. Até essa data, o regime é o Código de Ética Médica, as Res. CFM 1.821/2007 e 2.314/2022 e a Lei 13.709/2018.

Diretriz que se sustenta em outra base além da 2.454 não recebe a marcação. Ela vale hoje.

**Base.** CFM-2454-2026:art23

---

## R2 — Escopo da Resolução CFM 2.314/2022

Os arts. 3º, 13, 15 e 17 da Res. 2.314/2022 são subordinados à telemedicina. O caput do art. 3º diz "nos serviços prestados por telemedicina", e os oito parágrafos seguem o caput.

Regra: nenhuma diretriz enuncia como geral o que a 2.314/2022 impõe à telemedicina. O enunciado abre com "Em telemedicina," ou equivalente.

Fora da telemedicina, a base é outra:

| Tema | Em telemedicina | Fora da telemedicina |
|---|---|---|
| guarda do prontuário | CFM-2314-2022:art3 §3º | CEM:art87 |
| repartição da guarda com terceiro | CFM-2314-2022:art3 §4º | LGPD:art39 |
| segurança do tratamento | CFM-2314-2022:art3 §2º | LGPD:art46 · CFM-2454-2026:art17 |
| assinatura do documento | CFM-2314-2022:art13.d | CEM:art87 · CFM-1821-2007:art5 |
| sede no Brasil e responsável técnico | CFM-2314-2022:art17 | não há exigência equivalente |

A última linha importa. Fora da telemedicina, a exigência de sede no Brasil não tem equivalente. Diretriz que a estenda a todo atendimento está errada.

---

## R3 — Desidentificação sem parâmetro estrangeiro

O art. 12 da LGPD adota padrão de risco. Não há no Brasil lista fechada de identificadores nem limiar numérico em norma.

Regra: nenhuma diretriz apresenta parâmetro do Safe Harbor da HIPAA como exigência brasileira. Isso alcança o CEP truncado a três dígitos, a idade acima de 89 anos e a lista dos dezoito identificadores.

O Safe Harbor pode ser usado como referência de engenharia, desde que a diretriz declare que é regime dos Estados Unidos e que cumpri-lo não caracteriza anonimização no Brasil.

Regra: existe uma única lista canônica de quase-identificadores, em `SEC:anonimizacao.quase-identificadores`. Os arquivos 02 e 06 remetem a ela e não mantêm listas próprias.

**Base.** LGPD:art12 · SEC:anonimizacao.anpd · SEC:anonimizacao.quase-identificadores

---

## R4 — Três classes de retenção

A contradição mais frequente do conjunto vem de tratar como uma só coisa três objetos com regimes distintos.

**Classe A — registro clínico.** O que a IA produziu, foi revisado e integrou o prontuário. Segue o prazo de guarda do prontuário. Não é expurgado por rotina de retenção de aplicação.

**Classe B — trilha de auditoria.** Prompt, resposta, versão do modelo, identificação de quem revisou, data e hora. Existe para provar diligência. Fica sob controle do serviço, em repositório próprio, com prazo declarado. Não vive no provedor.

**Classe C — log de aplicação e telemetria.** Registro operacional. **Nunca contém conteúdo de paciente nem corpo de requisição.** Retenção curta, definida por necessidade operacional.

Regra: toda diretriz sobre retenção, persistência, log ou expurgo diz de qual classe fala. Gatilho de auditoria idem.

Isto resolve a contradição entre "persista prompt e resposta" e "nunca registre prompt em log": a primeira regra é da classe B, a segunda da classe C.

**Base.** CFM-1821-2007:art7 · CFM-2454-2026:art3 · LGPD:art37 · SEC:segredos.logs

---

## R5 — Controvérsias resolvidas, e declaradas como tais

Três pontos não pacificados foram resolvidos pela leitura conservadora. A resolução é nossa e precisa aparecer no texto.

Regra: cada diretriz que dependa de uma destas leituras traz a linha correspondente, literal.

**C1 — informar o paciente sempre.** O art. 5º, §1º fala em "apoio relevante"; o art. 11 fala em "qualquer utilização". A resolução não concilia os dois.

> Leitura nossa, conservadora: informar sempre. O ponto não está pacificado.

**C2 — delegação a sistema.** O art. 2º do CEM veda delegar a "outros profissionais" atos privativos. Se alcança sistemas é leitura extensiva.

> Leitura nossa, extensiva: a vedação alcança sistemas. O ponto não está pacificado. A partir de 26/08/2026 o art. 15, parágrafo único, e o art. 18, §2º da Res. 2.454/2026 sustentam a regra sem depender desta leitura.

**C3 — revelação a sistema automatizado.** O art. 73 do CEM veda revelar fato conhecido no exercício da profissão. Se o envio a um sistema, sem leitura humana, é "revelar" não tem pronunciamento do CFM.

> Leitura nossa, conservadora: enviar a sistema de terceiro é revelação. O ponto não está pacificado. Para liberação de cópia de prontuário, o art. 89 sustenta a regra sem depender desta leitura.

---

## R6 — Critério de severidade dos gatilhos

Um gatilho é `bloqueante` quando cumpre as três condições:

1. existe vedação expressa, tipo penal, ou requisito cuja falta caracteriza infração por si;
2. a entrada de ficha que o sustenta é `bloqueante`;
3. o padrão não ocorre em arquitetura lícita e comum.

A terceira condição é a que mais reprova gatilho. Gatilho que dispara em fluxo conforme não é bloqueante, é ruído.

Regra: nenhum gatilho é mais severo que a entrada que o sustenta. Onde a ficha qualificar a severidade por escopo, o gatilho carrega o qualificador.

Regra: gatilho não procurável é retirado. Se um revisor não consegue buscar aquilo em repositório, configuração ou fluxo, não serve.

---

## R7 — Recusa da IA e base legal

A recusa do paciente ao uso de IA é direito da relação médico-paciente. Ela não revoga a base legal do tratamento de dados, não obriga a eliminar o prontuário e não interrompe a guarda obrigatória.

Regra: diretriz e gatilho sobre recusa de IA não invocam base legal da LGPD como se fossem a mesma coisa. Consentimento do CFM e base legal da LGPD são exigências distintas e cumulativas.

Regra correlata: pedido de eliminação pelo titular, na LGPD, encontra o limite da guarda obrigatória do prontuário. A diretriz sobre eliminação diz isso.

**Base.** CFM-2454-2026:art5 · LGPD:art11 · LGPD:art18 · CFM-1821-2007:art7

---

## Aplicação

Estas decisões valem para os sete arquivos de diretrizes e para o catálogo de gatilhos. Diretriz que conflite com uma delas é corrigida, não mantida com ressalva.

Quando uma decisão for revista, o número permanece e a data de atualização muda. Diretriz que cite `R4` continua válida.
