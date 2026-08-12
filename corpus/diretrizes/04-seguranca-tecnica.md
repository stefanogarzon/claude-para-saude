---
tema: requisitos técnicos de segurança para sistema que trata dado de saúde
aplica-se-a: desenvolvedor, responsável técnico, encarregado
fichas: [01, 05, 07, 11]
verificado: 2026-08-11
---

# Segurança técnica de sistema com dado de saúde

Requisitos de implementação e de configuração para quem trata dado de paciente. A ANPD não editou os padrões técnicos mínimos do art. 46, §1º, da LGPD. Os parâmetros vêm de IETF, NIST e OWASP.

Quatro diretrizes usam também entradas `primária-parcial` da ficha 11: ANPD sobre incidente e sobre anonimização, técnicas de anonimização, pseudonimização e memorização em LLM. Elas informam; não são citadas como norma. A norma é a da linha `Base.`

Retenção e log seguem as três classes de R4, em `00-decisoes.md`: registro clínico (A), trilha de auditoria (B), log de aplicação e telemetria (C).

## D1 — Exigir TLS 1.3 e desabilitar TLS 1.0 e TLS 1.1

Serviço novo exige TLS 1.3. É decisão nossa de estado da arte para o art. 46: no IETF, TLS 1.2 é MUST e TLS 1.3 é SHOULD, e o MUST da RFC 9852 alcança protocolo novo, não implantação nova. TLS 1.2 fica por compatibilidade documentada. TLS 1.0, TLS 1.1, SSL 2.0 e SSL 3.0 ficam desabilitados no servidor e no cliente, vedação de nível MUST NOT. O escopo inclui o tráfego interno: banco, laboratório e HIS.

**Base.** SEC:tls.versoes · LGPD:art46 · CFM-2454-2026:art17

**Verificar.**
- varredura externa do endpoint com `testssl.sh`, `sslyze` ou SSL Labs
- ausência de `TLSv1` e `TLSv1.1` em servidor, balanceador, CDN e gateway
- ausência de verificação de certificado desligada no cliente (`verify=False`, `curl -k`)
- banco com `sslmode=verify-full`, endurecimento nosso sobre o `require` da ficha

**Escalar se.** Integração existente não suporta TLS 1.2 e pede exceção.

## D2 — Habilitar apenas cifras, grupos e certificados dentro dos parâmetros

Em TLS 1.2, habilitar as quatro suites ECDHE com AES-GCM recomendadas pela RFC 9325 e preferir AEAD. A lista não é fechada: AES-CCM entra em dispositivo sem suporte a GCM, com registro.

São MUST NOT do §4.1: NULL, anônimas, EXPORT, RC4 e suites abaixo de 112 bits de segurança. 3DES tem 112 bits efetivos, não cai nesse piso e cai no SHOULD NOT de menos de 128 bits. A vedação obrigatória do 3DES vem da nota 68 da Tabela 2 da SP 800-57 Rev. 5, que o desautoriza para proteção criptográfica desde 2023. Desabilitar também DES e MD5.

Grupo obrigatório P-256; X25519 recomendado. DH de no mínimo 2048 bits. Certificado RSA de no mínimo 2048 bits, SHA-256, FQDN em `subjectAlternativeName`.

**Base.** SEC:tls.suites · SEC:repouso.chaves

**Verificar.**
- ausência de suite CBC em TLS 1.2; a RFC as admite com `encrypt_then_mac`, a OWASP as desabilita
- compressão TLS e 0-RTT desabilitados; cookie com `Secure`; `Cache-Control: no-store`
- certificado renovado por ACME, com expiração monitorada

**Escalar se.** A decisão envolve grupo híbrido pós-quântico, cujo cronograma segue em revisão.

## D3 — Publicar o cabeçalho de transporte estrito

Enviar `Strict-Transport-Security: max-age=63072000; includeSubDomains` em todas as respostas HTTPS, inclusive nas da API. Confirmar HTTPS em todos os subdomínios antes de incluir a diretiva de subdomínios. O redirecionamento de HTTP para HTTPS usa 301.

**Base.** SEC:tls.hsts

**Verificar.**
- header no domínio principal e na API, com `max-age` de produção
- inventário de subdomínios servindo HTTPS, inclusive homologação e ferramenta interna

**Escalar se.** Alguém propõe enviar `preload`, cujo efeito é permanente.

## D4 — Cifrar em repouso com AES-GCM de 256 bits

Campo de prontuário é cifrado com AES-GCM e chave de 256 bits, decisão nossa acima do piso: o piso de 128 bits de força admite AES-128, RSA de 3072 bits e ECC de 256 bits. Nonce de 96 bits de CSPRNG, sem reúso por par de chave e dado. Tag de 128 bits, também decisão nossa: a SP 800-38D admite tags menores, e o gatilho da ficha dispara abaixo de 96 bits. Senha é derivada com KDF calibrada.

**Base.** SEC:repouso.algoritmo · SEC:repouso.nonce

**Verificar.**
- ausência de ECB, PKCS#1 v1.5, DES, 3DES, MD5 e SHA-1 em uso criptográfico
- chave, IV, token e identificador de CSPRNG, sem chave literal no código
- nonce de 12 bytes, nunca constante nem preso a contador em memória de processo

## D5 — Declarar a camada de cifragem e o que ela não protege

Disco cifrado e TDE protegem contra furto do disco, da VM desligada e do backup físico. Nenhum dos dois protege contra SQL injection, credencial vazada, dump lógico ou acesso administrativo ao banco. Para CPF, nome e texto livre, aplicar cifragem em nível de campo com envelope encryption: DEK por registro ou por tenant, KEK em KMS ou HSM.

**Base.** SEC:repouso.camadas · LGPD:art48

**Verificar.**
- documento que declara dados criptografados indica a camada
- backup, dump e exportação em planilha cifrados
- réplica, data warehouse e bucket de anexo com a cifragem da origem

## D6 — Guardar a chave fora do host do dado e manter inventário

A chave vive em KMS ou HSM, separada do repositório, do banco e do volume do dado cifrado. Cada chave tem identificador, data de criação, criptoperíodo, dado que protege e sistema que a usa. Segredo compartilhado alcança no máximo duas entidades; chave privada, uma. Em incidente, o inventário é o que delimita o escopo.

**Base.** SEC:repouso.chaves · LGPD:art48

**Verificar.**
- versão da chave persistida junto do registro cifrado
- chaves distintas em desenvolvimento, homologação e produção
- inventário criptográfico e política de gestão de chaves documentados e datados

**Escalar se.** A chave fica sob custódia exclusiva de terceiro, o que enfraquece a comprovação do art. 48, §3º na dosimetria da gravidade. Não dispensa a comunicação: a Res. 15/2024 não tem exceção por criptografia.

## D7 — Rotacionar por tempo e por volume de uso

O período de uso de origem da chave simétrica de cifragem vai até dois anos em volume pequeno; em grande volume cifrado em curto período, cai para a ordem de um dia a uma semana. A chave segue disponível para decifrar por no máximo três anos além do fim desse período.

A rotação também ocorre por comprometimento, suspeita, volume cifrado e mudança na segurança do algoritmo. Em AES-GCM com nonce aleatório de 96 bits, o limite é de 2^32 operações por chave. Chave de session ticket rotaciona em intervalo regular e curto — a RFC 9325 exemplifica com uma semana —, é destruída ao fim da validade, e a validade do ticket é limitada, tipicamente à metade da validade da chave.

**Base.** SEC:repouso.chaves · SEC:repouso.nonce

**Verificar.**
- contagem de operações por chave, ou DEK por registro ou por tenant, em alto volume
- rotação executada, com data do último ciclo, e chave de ticket vencida destruída
- ausência de 34 GB como limite para AES, valor de cifra de bloco de 64 bits

## D8 — Manter a chave de API fora do código e do repositório

A chave de API não fica em constante do código, em configuração versionada, em `docker-compose.yml`, em notebook, em screenshot nem em mensagem. O destino é cofre de segredos, com recuperação em tempo de execução. O CI/CD guarda apenas segredo de vida curta e raio pequeno. Uma chave por ambiente e por serviço, com escopo mínimo.

**Base.** SEC:segredos.armazenamento · LGPD:art46

**Verificar.**
- `.gitignore` com `.env*` desde o primeiro commit; `.env.example` só com nomes
- credencial de banco de curta duração, requisitada no start da aplicação
- token de integração com laboratório e HIS com expiração definida

## D9 — Detectar segredo no repositório e responder na ordem certa

Instalar `detect-secrets` como pre-commit hook em todo repositório clínico. Diante de segredo exposto, revogar, rotacionar e remover de código e de logs. Reescrever histórico não substitui a revogação.

A proteção de push no nível do repositório, que é a que gera alerta quando alguém contorna o bloqueio, exige GitHub Secret Protection, de Team ou Enterprise Cloud, e vem desabilitada. Onde o plano não permitir, o controle é o hook local com varredura em CI, e a limitação fica registrada.

**Base.** SEC:segredos.deteccao

**Verificar.**
- hook de detecção ativo, com execução também em CI
- histórico varrido por `sk-`, `AKIA`, `ghp_`, `xoxb-`, `-----BEGIN PRIVATE KEY-----`
- cada contorno de proteção de push com justificativa e rotação subsequente

## D10 — Aplicar menor privilégio ao segredo e ao dado

Nenhum desenvolvedor tem acesso a todos os segredos, e os cofres são segregados por sensibilidade. A credencial usada pelo LLM e pelo agente é de leitura, com escopo por tabela. A credencial da aplicação grava no registro clínico e segue `desenvolvimento:D6`: sem DDL, sem DELETE, sem superusuário. O acesso a segredo é auditado: quem pediu, para qual sistema, quando e com que resultado.

**Base.** SEC:segredos.privilegio · SEC:llm.agentic

**Verificar.**
- ausência de chave de provedor de LLM compartilhada por toda a equipe
- ausência de papel amplo (`everyone`, `authenticated`) em bucket com dado de paciente
- revisão periódica de quem tem acesso, com data

## D11 — Não registrar dado de paciente nem segredo em log

Esta diretriz é da classe C: log de aplicação, telemetria e rastreador de erro. Nenhum deles recebe dado de saúde, identificador do paciente, senha, token, chave, string de conexão nem conteúdo de prompt e de resposta. A cópia probatória é da classe B, e fica onde D14 e `custodia:D13` determinam.

Instalar redaction antes do logger, derrubando `messages`, `prompt`, `completion`, `Authorization`, `api_key`, `cpf`, `nome` e texto livre. Logger que serializa o corpo da requisição cria cópia do prontuário fora da cifragem do banco e fora da política de retenção.

**Base.** SEC:segredos.logs · LGPD:art49 · LGPD:art47

**Verificar.**
- ausência de serialização do corpo da requisição ou da resposta em rota clínica
- rastreador de erro com scrubbing, ou ausente do serviço clínico
- log de query com parâmetros desabilitado em produção
- amostra de log de produção inspecionada por pessoa, com data

**Escalar se.** O provedor retém prompt ou log de conversa por período contratual, ponto não pacificado diante do princípio da necessidade.

## D12 — Registrar o evento de acesso e proteger o registro

Registrar acesso a dado sensível, autenticação, falha de autorização, ação administrativa, atividade de criptografia, importação, exportação e upload. O registro traz quem, quando, qual recurso por identificador pseudonimizado e qual resultado, sem o conteúdo acessado. Tem detecção de violação, acesso restrito, transporte cifrado e prazo declarado.

É trilha de auditoria, classe B. O expurgo alcança essa trilha e o log da classe C, nunca o registro clínico da classe A. O art. 6º da Res. 15/2024 não impõe dever de log: impõe conteúdo de comunicação, e é o que exige a capacidade de contar titulares.

**Base.** SEC:segredos.logs · LGPD:art46 · LGPD:art49 · ANPD-15-2024:art6

**Verificar.**
- consulta que responde quantos titulares foram afetados em uma janela de tempo
- privilégio de leitura do registro restrito e revisado
- prazo de retenção definido por classe, com expurgo executado

## D13 — Tratar todo conteúdo que entra no contexto como não confiável

PDF, laudo, e-mail e documento do paciente entram no contexto do modelo como conteúdo não confiável. Não colocar no mesmo contexto o documento externo e a ferramenta capaz de exfiltrar dado. Saída do modelo não vai para HTML, markdown, SQL, shell ou `eval` sem sanitização. Agente com acesso a base clínica usa credencial de leitura e aprovação humana em qualquer escrita.

**Base.** SEC:llm.owasp-top10 · SEC:llm.agentic · SEC:llm.nist

**Verificar.**
- separação entre instrução de sistema e conteúdo do documento no payload
- ausência de segredo, credencial e regra confidencial no system prompt
- carregamento automático de recurso externo desligado na interface que renderiza a saída
- filtro de paciente ou de tenant aplicado no índice vetorial, não no prompt

## D14 — Fechar os caminhos de vazamento da integração com o modelo

Desidentificar antes da chamada ao provedor, montando o payload por seleção explícita de campos. Usar apenas plano comercial ou API.

Contratar retenção zero antes do primeiro envio para todo recurso elegível. O arranjo é concedido por organização, por endpoint ou por recurso, e não cobre tudo: o critério é o de `fornecedor:D12`. O recurso que ficar de fora é bloqueado em código.

No log da aplicação, classe C, registrar identificador da requisição, versão do modelo, contagem de tokens, latência e status, sem o conteúdo enviado. A cópia probatória de prompt e resposta é da classe B, e fica no repositório clínico governado, com retenção declarada, na forma de `custodia:D13`.

**Base.** SEC:llm.vetores-clinicos · SEC:segredos.logs · LGPD:art44 · LGPD:art42 · CFM-2454-2026:art6

**Verificar.**
- etapa de desidentificação executada antes da chamada
- configuração de retenção conferida no painel do provedor, com data
- recursos fora do arranjo de retenção zero listados, com o bloqueio em código

**Escalar se.** Não há recurso equivalente com retenção zero para a função necessária, ou o enquadramento do provedor como operador ou como controlador precisa ser afirmado, ponto não pacificado.

## D15 — Não treinar nem ajustar modelo com dado identificável

Não usar dado identificável de paciente em treino, ajuste fino, validação ou avaliação. Usar dataset desidentificado.

A regra é decisão nossa de engenharia, e não vedação da Res. 2.454/2026: o art. 6º, §2º sujeita o uso de dado pessoal em treinamento, validação e aprimoramento a princípios éticos, científicos e de proteção de dados, e não o proíbe. Sustentam a regra o art. 6º, §1º, que só admite compartilhamento quando estritamente necessário, a exigência de base legal do art. 11 da LGPD, e o fato de o alinhamento do modelo não eliminar memorização, com dado de treino extraível depois.

Exemplo few-shot dentro do prompt é dado enviado ao provedor. Base vetorial construída com prontuário identificável exige isolamento no índice.

**Base.** CFM-2454-2026:art6 · LGPD:art11

**Verificar.**
- dataset de treino e de avaliação sem identificador, e fora do repositório
- exemplos few-shot construídos a partir de caso sintético
- configuração do provedor que não usa os inputs para treinamento
- base legal do art. 11 registrada quando houver dado pessoal em avaliação

## D16 — Aplicar segurança desde a concepção e privacidade por padrão

As medidas valem desde o desenho, o protótipo e a prova de conceito. O schema minimiza campos, isola os sensíveis e define retenção por dado e por classe. A configuração padrão é a mais restritiva: compartilhamento desligado, acesso por perfil, MFA, backup separado e não sincronizado em tempo real, bibliotecas em versão suportada.

**Base.** LGPD:art37 · LGPD:art46 · LGPD:art49 · SEC:anpd-guias.pequeno-porte

**Verificar.**
- fluxo de LLM presente no registro de operações antes de ir a produção
- segregação entre desenvolvimento, homologação e produção
- expurgo de log, telemetria e histórico de conversa (classe C) e da trilha no prazo declarado (classe B), sem alcançar o registro clínico (classe A)

**Escalar se.** O documento de conformidade cita apenas guia gerencial, sem parâmetro técnico.

## D17 — Comunicar incidente em três dias úteis e manter o registro

O critério do art. 5º da Res. 15/2024 é cumulativo: exige afetar significativamente interesses e direitos fundamentais e, além disso, ao menos um dos seis critérios. Incidente com dado de paciente satisfaz dois deles, dado sensível e dado sob sigilo profissional, e em contexto clínico a afetação significativa é a regra.

A comunicação à ANPD e ao titular ocorre em três dias úteis contados do conhecimento pelo controlador de que o incidente afetou dados pessoais, por formulário eletrônico, protocolada pelo encarregado com comprovante de vínculo ou por representante com instrumento de poderes. A complementação vai até vinte dias úteis contados da data da comunicação.

A comunicação ao titular é individualizada e em linguagem simples; se essa forma for inviável, a divulgação pelos meios disponíveis dura no mínimo três meses. A declaração de que ela foi realizada é juntada em até três dias úteis do término do prazo do caput. Todo incidente é registrado por no mínimo cinco anos da data do registro, inclusive o não comunicado, com a justificativa.

**Base.** ANPD-15-2024:art5 · ANPD-15-2024:art6 · ANPD-15-2024:art9 · ANPD-15-2024:art10 · LGPD:art48 · ANPD-2-2022:art3 · ANPD-2-2022:art4

**Verificar.**
- runbook que conta o prazo em dias úteis, com responsável nomeado
- ato de indicação do encarregado e comprovante de vínculo prontos antes do incidente
- capacidade de informar titulares afetados, data da ocorrência, causa principal e operador
- cadastro com contato válido do paciente e modelo de mensagem pronto

**Escalar se.** Alguém propõe não comunicar por os dados estarem criptografados, ou aplicar o prazo em dobro de agente de pequeno porte — seis dias úteis no caput, quarenta na complementação, com regra própria para o titular —, enquadramento não pacificado no uso de LLM sobre dado sensível.

## D18 — Proibir dado real de paciente em teste e homologação

Homologação, desenvolvimento e demonstração usam dado sintético ou desidentificado pelo pipeline testado. Restaurar dump de produção em teste replica o prontuário para fora dos controles de produção. Credenciais, chaves e cofres são separados por ambiente.

**Base.** LGPD:art46 · SEC:repouso.camadas · SEC:segredos.armazenamento

**Verificar.**
- origem dos dados de homologação documentada
- ausência de rotina de cópia de produção para homologação
- HTTPS, controle de acesso e política de log ativos também em homologação

**Escalar se.** A área de negócio exige dado real em homologação para validar um fluxo.
