---
tema: desidentificação e risco de reidentificação
aplica-se-a: desenvolvedor, responsável técnico, pesquisador
fichas: [05, 11]
verificado: 2026-08-11
---

# Desidentificação de dado de saúde

Como reduzir a identificabilidade de dado de paciente antes de enviá-lo a um sistema de terceiro, e como medir o que sobra. Separado do arquivo de segurança técnica porque é decisão de dado, não de infraestrutura.

Os parâmetros do Safe Harbor citados aqui são regime dos Estados Unidos. Cumpri-los não caracteriza anonimização no Brasil, onde o art. 12 da LGPD adota padrão de risco e nenhuma norma traz limiar numérico. Ver a decisão R3 em `00-decisoes.md`.

Esta é a referência canônica de quase-identificadores do projeto. Os arquivos 02 e 06 remetem a ela.

---

## D1 — Remover os campos que reidentificam antes de compartilhar

Remover ou generalizar nome, CPF, prontuário, matrícula, carteirinha, telefone, e-mail, endereço, IP, URL e número de série de dispositivo. Data de nascimento vira ano ou faixa quinquenal. Datas de procedimento, internação, alta e óbito viram intervalo em dias desde a linha de base. Esta é a lista canônica de quase-identificadores do conjunto: `custodia:D12` e `desenvolvimento:D2` remetem a ela.

Os parâmetros de truncamento vêm do Safe Harbor da HIPAA, regime dos Estados Unidos, e servem como piso operacional de varredura: CEP mantido só nos três primeiros dígitos, e apenas quando a área desses três dígitos tiver mais de 20.000 pessoas, com 17 prefixos convertidos em `000`; idade acima de 89 recodificada como "90 ou mais". O CEP brasileiro tem oito dígitos, e nenhuma norma brasileira fixa faixa equivalente. Cumpri-los não caracteriza anonimização no Brasil: o art. 12 pede a demonstração de que a reversão não se faz com esforços razoáveis, e a regulamentação do §3º não foi editada até 11/08/2026.

**Base.** SEC:anonimizacao.quase-identificadores · LGPD:art12

**Verificar.**
- schema do arquivo exportado conferido coluna a coluna
- `PatientName`, `PatientBirthDate`, `PatientID` e `AccessionNumber` removidos do DICOM, com defacing em imagem de crânio
- texto livre e PDF de laudo digitalizado tratados antes da exportação
- CID de doença rara tratado em coorte pequena

## D2 — Tratar remoção de identificador direto como insuficiente

Retirar nome e CPF não produz dado anonimizado. Os números vêm de população estrangeira e assim devem ser citados. CEP de cinco dígitos, que é o ZIP dos Estados Unidos, com sexo e data de nascimento, torna 87,1% da população dos Estados Unidos provavelmente única; município, sexo e data de nascimento, 58,38%; condado, sexo e data de nascimento, 18,1%. Quinze atributos demográficos tornam 99,98% das pessoas de Massachusetts únicas, no corpo do artigo; o abstract generaliza para "Americans". Amostrar a base não reduz esse risco.

**Base.** SEC:anonimizacao.evidencia · LGPD:art12

**Verificar.**
- ausência de data de nascimento completa e de CEP completo em base dita anonimizada
- amostragem não apresentada como medida de anonimização em protocolo ou DPIA

## D3 — Medir e registrar o risco residual de reidentificação

A ANPD, em estudo técnico orientativo de novembro de 2023, trata a anonimização como processo contínuo baseado em risco. O documento não é vinculante, e a regulamentação do art. 12, §3º não foi editada. Adotar o método assim mesmo, porque é ele que produz a prova exigida pelo art. 12, §1º.

Definir o risco aceito, aplicar as técnicas, medir o risco residual e registrar técnica, parâmetro, métrica, responsável e data. Rodar teste de reidentificação no pipeline, e estudo de reidentificação antes de compartilhar.

**Base.** LGPD:art12

**Verificar.**
- k declarado e medido na base a compartilhar, sem classe de equivalência com k=1
- ausência de classes em que todos os registros têm o mesmo valor de atributo sensível
- responsável nomeado pela decisão de liberação

**Escalar se.** O valor de k, de ℓ ou de ε precisa ser fixado: nenhuma norma brasileira traz parâmetro numérico.

## D4 — Separar a informação que permite reidentificar

A tabela de correspondência entre pseudônimo e paciente fica em banco separado, com credencial separada, sob custódia de pessoa distinta de quem analisa. Pseudônimo derivado de CPF ou de prontuário usa sal secreto. Dado pseudonimizado continua sendo dado pessoal, pelo art. 12.

Em estudo de saúde pública por órgão de pesquisa, o art. 13 é bloqueante, e o §2º veda a transferência a terceiro em circunstância alguma, o que alcança o envio a API de provedor. Fora desse escopo o art. 13 não se aplica — clínica, consultório e empresa de saúde não o invocam — e a exigência é de risco.

**Base.** LGPD:art12 · LGPD:art13

**Verificar.**
- ausência de tabela de correspondência na mesma pasta, bucket, banco ou Drive do dataset
- ausência de chave ou dicionário de pseudonimização no repositório
- custodiante nomeado, distinto do analista

**Escalar se.** Alguém trata base pseudonimizada como fora do alcance da LGPD.
