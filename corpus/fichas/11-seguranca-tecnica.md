---
tema: Segurança técnica — criptografia, anonimização, riscos de LLM e higiene de segredos
ementa: Parâmetros técnicos que dão conteúdo ao art. 46 da LGPD e ao art. 17 da Res. CFM 2.454/2026
escopo: IETF (BCP 195), NIST, OWASP, ANPD, EDPB, literatura de reidentificação
status: referência técnica; não vinculante por si, salvo nos itens que remetem a norma
fonte: cada item traz a URL primária no campo Literal
verificado: 2026-08-11
meia_vida: média — reverificar a cada seis meses; SP 800-52 Rev. 2 e AI RMF 1.0 estão em revisão ativa
---

# Segurança técnica

O art. 46 da LGPD exige "medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados", obrigatórias "desde a fase de concepção do produto ou do serviço até a sua execução". O art. 17 da Res. CFM 2.454/2026 exige medidas "compatíveis com o estado da arte". Nenhum dos dois indica parâmetro. Esta ficha reúne os parâmetros e a fonte de cada um.

O guia de segurança da ANPD também não traz parâmetro numérico (ver `SEC:anpd-guias.pequeno-porte`). A ancoragem numérica vem de IETF, NIST e OWASP.

Itens: 26. Marcações `NÃO VERIFICADO` consolidadas ao final.

---

## SEC:tls.versoes

**Ementa.** Versões de TLS aceitáveis em serviço que trafega dado de saúde.

**Literal.**
> RFC 8996, "Deprecating TLS 1.0 and TLS 1.1", março/2021, integrante do BCP 195: "TLS 1.0 **MUST NOT** be used"; "TLS 1.1 **MUST NOT** be used". A negociação de ambas não deve ser permitida. Deprecia DTLS 1.0.
> RFC 9325, "Recommendations for Secure Use of TLS and DTLS", novembro/2022, integrante do BCP 195: MUST NOT negociar SSL 2.0, SSL 3.0, TLS 1.0 e TLS 1.1; MUST suportar TLS 1.2; SHOULD suportar e preferir TLS 1.3.
> RFC 9852, "New Protocols Using TLS Must Require TLS 1.3", 16/07/2026, integrante do BCP 195 e que atualiza a RFC 9325: protocolos **novos** que usam TLS "MUST require TLS 1.3". Exclui DTLS, por implantação limitada.
> NIST SP 800-52 Rev. 2, final de 29/08/2019, não retirado, com nota "This publication is currently being reviewed": TLS 1.2 com cipher suites FIPS obrigatório em servidores e clientes de governo; suporte a TLS 1.3 exigido a partir de 1º/01/2024.
> OWASP TLS Cheat Sheet: suportar TLS 1.3 como padrão e TLS 1.2 por compatibilidade; desabilitar TLS 1.0, TLS 1.1, SSLv2 e SSLv3.

Fontes: https://www.rfc-editor.org/info/bcp195 · https://www.rfc-editor.org/info/rfc9852 · https://www.rfc-editor.org/rfc/rfc9325.html · https://csrc.nist.gov/pubs/sp/800/52/r2/final · https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html — todas verificadas em 2026-08-11.

**Fonte.** https://www.rfc-editor.org/info/bcp195 · https://www.rfc-editor.org/rfc/rfc8996.txt · https://www.rfc-editor.org/rfc/rfc9325.txt · https://www.rfc-editor.org/rfc/rfc9852.txt · https://csrc.nist.gov/pubs/sp/800/52/r2/final · https://csrc.nist.gov/News/2026/tls-comment-on-sp-800-52-rev-2 · https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Para sistema novo em saúde: exigir TLS 1.3 e manter TLS 1.2 apenas por compatibilidade documentada com integração existente. Desabilitar TLS 1.0 e 1.1 em servidor e em cliente. A verificação é externa e leva minutos: SSL Labs, Mozilla Observatory, `testssl.sh`, `sslyze`, `sslscan`, `O-Saft`, `CipherScan`, `CryptoLyzer`, `tls-scan`, CryptCheck, Hardenize, ImmuniWeb, Scanigma, Stellastra (ferramentas nomeadas no cheat sheet da OWASP). O escopo inclui o tráfego interno: backend ↔ banco, backend ↔ integração com laboratório e HIS. Criptografia fim a fim de aplicativo de mensagem protege o trânsito; não protege a retenção no aparelho, o backup em nuvem nem o encaminhamento da mensagem.

**Gatilhos.**
- `ssl_protocols`, `SSLProtocol` ou equivalente aceitando `TLSv1` ou `TLSv1.1`
- `ssl.PROTOCOL_TLSv1`, `PROTOCOL_SSLv23` sem restrição por `options`
- ausência de `minimum_tls_version` em load balancer, CDN, API gateway ou bucket
- `verify=False` (requests), `rejectUnauthorized: false` (Node), `InsecureSkipVerify: true` (Go)
- `curl -k` ou `--insecure` em script de integração
- string de conexão de banco sem `sslmode=require` ou `verify-full`
- chamada interna em `http://` dentro da VPC ou do cluster
- webhook de laboratório ou de HIS recebido em endpoint HTTP

**Incerteza.** O IETF veda TLS 1.0 e 1.1 sem exceção. O NIST abriu consulta pública sobre a SP 800-52 Rev. 2 em 07/05/2026, encerrada em 10/07/2026, com três perguntas, verbatim: "Is there a strong reason for NIST to continue to recommend that servers *should* support TLS 1.2, or can the recommendation be changed such that servers *may* support TLS 1.2?"; "Are there sectors or applications where it is common for non-government client devices that do not support TLS 1.3 (or TLS 1.2) to connect to government servers?"; "Is there a compelling reason to conditionally allow support for TLS 1.0 or TLS 1.1 if the system administrator determines that it is necessary?". Em 30/07/2026 o NIST publicou os comentários recebidos; a revisão segue na Fase 1, sem proposta de decisão. Adotamos a posição do IETF e da OWASP, porque o art. 46 é avaliado por adequação ao estado da arte.

**Relacionados.** LGPD:art46 · CFM-2454-2026:art17 · SEC:tls.suites · SEC:tls.hsts

---

## SEC:tls.suites

**Ementa.** Cipher suites, grupos de troca de chave e parâmetros de certificado.

**Literal.**
> RFC 9325, §4.2 — cipher suites para TLS 1.2. Qualificação verbatim: "implementation and deployment of the following cipher suites is RECOMMENDED" — `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`. Não é lista fechada: o mesmo §4.2 admite AES-CCM em dispositivos sem suporte a GCM. As proibições nominais estão no §4.1, verbatim: "Implementations MUST NOT negotiate the cipher suites with NULL encryption"; "Implementations MUST NOT negotiate RC4 cipher suites"; "Implementations MUST NOT negotiate cipher suites offering less than 112 bits of security, including so-called 'export-level' encryption (which provides 40 or 56 bits of security)". Um degrau acima, no mesmo §4.1, verbatim: "Implementations SHOULD NOT negotiate cipher suites that use algorithms offering less than 128 bits of security." Forward secrecy MUST ser suportado e preferido; preferir ECDH; suportar P-256 e X25519. DH ≥ 2048 bits, verbatim: "DH key lengths of at least 2048 bits are REQUIRED". Curvas elípticas de no mínimo 224 bits — §4.5, verbatim: "Curves of less than 224 bits MUST NOT be used." Módulo RSA ≥ 2048 bits; hash SHA-256 RECOMMENDED, SHA-1 e MD5 MUST NOT. Chaves de cifragem de session ticket com rotação regular, verbatim: "Ticket-encryption keys MUST be changed regularly, e.g., once every week". Extensões obrigatórias em TLS 1.2: `renegotiation_info` e `extended_master_secret`. Compressão TLS SHOULD NOT (§3.3). 0-RTT deve ser evitado salvo orientação específica do protocolo (§3.10; HTTP: RFC 8470; QUIC: RFC 9001). SNI MUST (§3.7) e ALPN MUST (§3.8).
> RFC 8446, TLS 1.3, agosto/2018 — cipher suites definidas: `TLS_AES_128_GCM_SHA256`, `TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`. Conjunto mandatory-to-implement, §9.1, verbatim, com a condicional que abre a seção: "In the absence of an application profile standard specifying otherwise: A TLS-compliant application MUST implement the TLS_AES_128_GCM_SHA256 [GCM] cipher suite and SHOULD implement the TLS_AES_256_GCM_SHA384 [GCM] and TLS_CHACHA20_POLY1305_SHA256 [RFC8439] cipher suites (see Appendix B.4). A TLS-compliant application MUST support digital signatures with rsa_pkcs1_sha256 (for certificates), rsa_pss_rsae_sha256 (for CertificateVerify and certificates), and ecdsa_secp256r1_sha256. A TLS-compliant application MUST support key exchange with secp256r1 (NIST P-256) and SHOULD support key exchange with X25519 [RFC7748]."
> As listas mais amplas de grupos (secp256r1, secp384r1, secp521r1, x25519, x448) e de esquemas de assinatura (rsa_pss_rsae_sha256/384/512, ecdsa_secp256r1_sha256, ecdsa_secp384r1_sha384, ecdsa_secp521r1_sha512, ed25519, ed448) são as enumerações de code points das §§4.2.7 (`supported_groups`) e 4.2.3 (`signature_algorithms`). Não são o conjunto obrigatório.
> OWASP TLS Cheat Sheet — em TLS 1.2, preferir AEAD e evitar modos CBC. Desabilitar sempre: null, anônimos, EXPORT, RSA key transport e DH estático. Grupos recomendados, string literal do documento: `X25519MLKEM768:x25519:prime256v1:x448:ffdhe2048:ffdhe3072`. Certificados: RSA ≥ 2048 bits, SHA-256, FQDN em `subjectAlternativeName`; evitar wildcard salvo necessidade real; ACME para automação. Redirecionamento HTTP→HTTPS com 301 permanente; cookie com flag `Secure`; `Cache-Control: no-store`.

Fontes: https://www.rfc-editor.org/rfc/rfc9325.html · https://www.rfc-editor.org/rfc/rfc8446.html · https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html — verificadas em 2026-08-11.

**Fonte.** https://www.rfc-editor.org/rfc/rfc9325.txt · https://www.rfc-editor.org/rfc/rfc8446.txt · https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** As quatro suites da RFC 9325 são o conjunto a habilitar em TLS 1.2. A qualificação é RECOMMENDED, e há a alternativa de AES-CCM para dispositivo sem GCM; fora disso não há margem, porque o piso de 112 bits e as proibições nominais são MUST NOT. Em TLS 1.3, só `TLS_AES_128_GCM_SHA256` é obrigatória de implementar; as outras duas são SHOULD. Em documento normativo interno, não descrever as três como obrigatórias. Pelo mesmo motivo, o mínimo interoperável de troca de chave é secp256r1, com X25519 como SHOULD. O primeiro grupo da string da OWASP é híbrido pós-quântico (`X25519MLKEM768`), o que torna a migração PQC uma decisão de configuração de servidor, não um projeto futuro. Certificado wildcard amplia o raio de comprometimento de uma chave; em serviço com dado de paciente, emitir certificado por FQDN.

**Gatilhos.**
- lista de cifras com `RC4`, `NULL`, `EXPORT`, `DES`, `3DES`, `MD5`, `anon`
- suite CBC habilitada em TLS 1.2 (`AES128-SHA`, `AES256-SHA`, `...-CBC-...`)
- geração de chave com `key_size=1024` ou `rsa:1024`
- certificado assinado com SHA-1
- certificado sem `subjectAlternativeName`, ou wildcard usado como padrão do serviço
- compressão TLS habilitada
- 0-RTT (`early_data`) habilitado em endpoint que aceita requisição não idempotente com dado de paciente
- cookie de sessão sem `Secure`
- resposta com dado de paciente sem `Cache-Control: no-store`
- renovação manual de certificado sem ACME, com data de expiração não monitorada

**Relacionados.** SEC:tls.versoes · SEC:repouso.pqc

---

## SEC:tls.hsts

**Ementa.** HTTP Strict Transport Security e o efeito da lista de preload.

**Literal.**
> HSTS é definido pela RFC 6797, "HTTP Strict Transport Security (HSTS)", novembro/2012.
> Exemplos do cheat sheet, valores literais: `Strict-Transport-Security: max-age=63072000` — descrito no próprio documento como perigoso por não trazer `includeSubDomains`; `Strict-Transport-Security: max-age=63072000; includeSubDomains`; e `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`. O `max-age` de 63072000 segundos é apresentado como "a long (2 years = 63072000 seconds) max-age".
> Advertência literal do cheat sheet: enviar `preload` "can have PERMANENT CONSEQUENCES", podendo impedir o acesso ao domínio caso seja necessário reverter para HTTP; o processo de remoção da preload list deve ser revisado antes.
> Omitir `includeSubDomains` "permits a broad range of cookie-related attacks"; incluí-lo bloqueia HTTP em todos os subdomínios, que precisam servir HTTPS antes.

Fonte: https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html — verificada em 2026-08-11.

**Fonte.** https://www.rfc-editor.org/rfc/rfc6797.txt · https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** Habilitar o header com `max-age` de dois anos e `includeSubDomains` depois de confirmar HTTPS em todos os subdomínios, inclusive os de homologação e de ferramenta interna. Decidir `preload` como decisão de infraestrutura registrada, não como linha copiada de exemplo.

**Gatilhos.**
- resposta HTTPS sem header `Strict-Transport-Security`
- `max-age` curto em produção (valores de teste como 300 ou 600 mantidos)
- `preload` presente sem HTTPS em todos os subdomínios
- redirecionamento HTTP→HTTPS com 302 em vez de 301
- header presente apenas no domínio principal, ausente na API

**Relacionados.** SEC:tls.versoes

---

## SEC:tls.pinning

**Ementa.** Certificate pinning e mTLS.

**Literal.**
> OWASP TLS Cheat Sheet, verbatim: public key pinning "has subsequently been deprecated and is no longer recommended or supported by modern browsers" — referência ao HPKP.
> No mesmo documento, verbatim: "However, public key pinning can still provide security benefits for mobile applications, thick clients and server-to-server communication."
> mTLS, verbatim: "Despite these challenges, client certificates and mTLS should be considered for high-value applications or APIs, particularly where users are technically sophisticated or part of the same organization." As "challenges" referidas são o overhead administrativo descrito no parágrafo anterior do documento.

Fonte: https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html — verificada em 2026-08-11.

**Fonte.** https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** Não implantar HPKP em aplicação web. Considerar pinning em aplicativo móvel de saúde e em integração servidor-a-servidor com laboratório ou HIS, sempre com pin de backup e plano de rotação. Considerar mTLS na integração entre serviços que trafegam dado de paciente, com inventário dos certificados de cliente.

**Gatilhos.**
- header `Public-Key-Pins` em servidor web
- pinning implementado com um único pin, sem pin de backup
- pin embutido no binário do aplicativo sem rota de atualização
- integração servidor-a-servidor com dado de paciente autenticada apenas por chave de API em header
- certificado de cliente mTLS sem data de expiração monitorada

**Relacionados.** SEC:tls.versoes · SEC:segredos.privilegio

---

## SEC:repouso.algoritmo

**Ementa.** Algoritmos e modos aceitáveis para cifragem em repouso.

**Literal.**
> OWASP Cryptographic Storage Cheat Sheet — simétrica: "AES with a key that's at least 128 bits (ideally 256 bits)". Modos: "GCM and CCM, which should be used as a first preference"; CTR e CBC apenas com Encrypt-then-MAC; ECB proibido. Assimétrica: preferir ECC com curva segura como Curve25519; RSA como alternativa, com no mínimo 2048 bits e padding aleatório (OAEP). Senhas nunca com criptografia reversível; usar hashing de senha. CSPRNG por linguagem: `crypto.randomBytes()` em Node, módulo `secrets` em Python.
> OWASP ASVS 5.0, V11 Cryptography — 11.2.3: mínimo de 128 bits de segurança, por exemplo ECC de 256 bits ou RSA de 3072 bits. 11.3.1: proibido modo inseguro (ECB) e padding fraco (PKCS#1 v1.5). 11.3.2: apenas cifras e modos aprovados, como AES com GCM. 11.3.5: operar em modo encrypt-then-MAC. 11.4.1: apenas funções de hash aprovadas; MD5 proibido para qualquer uso criptográfico. 11.4.2: senhas com KDF computacionalmente intensiva, com parâmetros calibrados. 11.5.1: CSPRNG com no mínimo 128 bits de entropia.

Fontes: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html · https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x20-V11-Cryptography.md — verificadas em 2026-08-11.

**Fonte.** https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html · https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x20-V11-Cryptography.md · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Em campo de prontuário, usar AES-GCM com chave de 256 bits. Senha de usuário nunca é cifrada; é derivada com KDF. Todo material aleatório usado como chave, IV, token de sessão ou identificador de recurso sai de CSPRNG.

**Gatilhos.**
- `AES.MODE_ECB`, `AES/ECB/PKCS5Padding`, `-aes-256-ecb`
- `Math.random()`, `random.random()`, `rand()`, `uuid1()` para gerar chave, IV, token ou identificador de recurso
- `md5(`, `sha1(` em uso criptográfico, de assinatura ou de integridade
- senha armazenada com cifragem reversível ou com codificação base64
- `PKCS1v15` em operação de cifragem RSA
- `AES/CBC/...` sem HMAC associado
- chave literal em constante do código (`KEY = "..."`, `SECRET = "..."`)
- `DES`, `3DES`, `Blowfish` em código novo

**Relacionados.** SEC:repouso.nonce · SEC:repouso.chaves · CFM-2454-2026:anexoI.XV-XVI

---

## SEC:repouso.nonce

**Ementa.** Limites operacionais do AES-GCM: IV, número de invocações e tamanho de tag.

**Literal.**
> NIST SP 800-38D, novembro/2007 — IV de 96 bits é o recomendado: "restricting support to the length of 96 bits, to promote interoperability, efficiency, and simplicity of design". Duas construções admitidas: determinística (campo fixo mais campo de invocação) e baseada em RBG (no mínimo 96 bits de saída de gerador aleatório). Limite duro: com IV determinístico de tamanho diferente de 96 bits, ou com construção RBG, "the total number of invocations of the authenticated encryption function shall not exceed 2^32" para uma dada chave. Máximo por invocação: 2^39 − 256 bits de plaintext; AAD ≤ 2^64 − 1 bits. Tags de 128, 120, 112, 104 e 96 bits; 64 e 32 bits apenas sob as restrições do Apêndice C.
> OWASP ASVS 5.0, 11.3.4: nonces e IVs não podem ser reutilizados para mais de um par (chave, elemento de dado).

Fontes: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf · https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x20-V11-Cryptography.md — verificadas em 2026-08-11.

**Fonte.** https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf · https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x20-V11-Cryptography.md · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Com nonce aleatório de 96 bits, o gatilho de rotação de chave em sistema de alto volume é a contagem de operações (2^32), não o tempo. Colisão de nonce em GCM causa perda de confidencialidade e de integridade, com recuperação da chave de autenticação. Contar as operações por chave, ou reduzir o volume por chave com DEK por registro ou por tenant.

**Gatilhos.**
- IV ou nonce constante, ou derivado de valor fixo (`iv = b"\x00" * 12`)
- contador de nonce mantido em variável de processo, reiniciado a cada boot ou a cada réplica
- nonce gerado por PRNG não criptográfico
- tamanho de nonce diferente de 12 bytes sem justificativa registrada
- tag truncada abaixo de 96 bits
- mesma chave AES-GCM usada para todo o dataset, sem DEK por registro ou por tenant
- ausência de contagem de operações por chave em serviço de alto volume

**Relacionados.** SEC:repouso.chaves · SEC:repouso.algoritmo

---

## SEC:repouso.chaves

**Ementa.** Tamanho de chave, criptoperíodo, custódia, rotação e inventário.

**Literal.**
> NIST SP 800-57 Part 1 Rev. 5, "Recommendation for Key Management: Part 1 – General", final de maio/2020, supersede a Rev. 4 de janeiro/2016. Correspondência de força de segurança, Tabela 2: 112 bits → 3TDEA (simétrica), FFC L=2048/N=224, IFC (RSA) k=2048, ECC f=224–255; 128 bits → AES-128, FFC L=3072/N=256, IFC (RSA) k=3072, ECC f=256–383. Nota 68 da Tabela 2, verbatim: "Although 3TDEA is listed as providing 112 bits of security strength, its use has been deprecated (see SP 800-131A) through 2023, after which it will be disallowed for applying cryptographic protection."
> Criptoperíodos (§5.3.6 e Tabela 1). Chave privada de assinatura, item 1.b, verbatim: "a maximum cryptoperiod of about one to three years is recommended. A private signature key shall be destroyed at the end of its cryptoperiod." Chave simétrica de cifragem de dados, item 6.b, verbatim: "The originator-usage period recommended for the encryption of large volumes of data over a short period of time (e.g., for link encryption) is on the order of a day or a week. An encryption key used to encrypt smaller volumes of data might have an originator-usage period of up to two years. A recipient-usage period of no more than three years beyond the end of the originator-usage period is recommended." Key-wrapping key simétrica, item 7.b: originator-usage period na ordem de um dia ou uma semana para grande volume e "could be up to two years" para pequeno volume; recipient-usage period "no more than three years beyond the end of the originator-usage period".
> Tabela 1, valores tabelados: Private Signature Key, "1 to 3 years"; Symmetric Data Encryption Keys, originator-usage period < 2 anos e recipient-usage period < OUP + 3 anos; Symmetric Key-Wrapping Key, originator-usage period < 2 anos e recipient-usage period < OUP + 3 anos.
> OWASP Cryptographic Storage Cheat Sheet — quatro critérios de rotação: chave comprometida ou sob suspeita de comprometimento; decurso do criptoperíodo, com remissão à seção 5.3 da SP 800-57; volume de dados já cifrado sob a chave; alteração relevante na segurança do algoritmo. O critério de volume, verbatim: "This would typically be 2^35 bytes (~34GB) for 64-bit keys and 2^68 bytes (~295 exabytes) for 128-bit block size." Separação de custódia: armazenar as chaves separadamente dos dados cifrados. Envelope encryption: a DEK cifra o dado, a KEK cifra a DEK e permanece isolada, e a DEK cifrada pode acompanhar o dado.
> OWASP ASVS 5.0 — 11.1.1: política documentada de gestão de chaves seguindo padrão como o NIST SP 800-57, com chaves não compartilhadas em excesso (máximo de 2 entidades para segredo compartilhado, máximo de 1 entidade para chave privada). 11.1.2: inventário criptográfico com todas as chaves, algoritmos e certificados, documentando onde cada chave pode ser usada e que dado protege.

Fontes: https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final · https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf · https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html · https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x20-V11-Cryptography.md — verificadas em 2026-08-11.

**Fonte.** https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf · https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final · https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html · https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x20-V11-Cryptography.md · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Para dado de saúde, o piso é a linha de 128 bits da Tabela 2. A linha de 112 bits tem 3TDEA como algoritmo simétrico, depreciado e vedado para aplicar proteção criptográfica desde 2023; não existe "AES de 112 bits". Na prática: AES-128 ou AES-256, RSA de 3072 bits, ECC de 256 bits ou mais.

O criptoperíodo é limite de tempo. O limite de 2^32 é outra coisa: é o número máximo de invocações da função de cifragem autenticada do GCM sob uma mesma chave, fixado pela SP 800-38D, §8.3, e registrado em `SEC:repouso.nonce`. Em serviço de alto volume os dois limites correm em paralelo, e a rotação ocorre no primeiro que vencer. O limite de volume da OWASP é um terceiro número, e o valor citado com frequência — 34 GB — é o de bloco de 64 bits. Para AES, de bloco de 128 bits, o valor da mesma passagem é 2^68 bytes. Quem cita 34 GB para AES aperta a rotação por engano e deixa de contar as invocações, que é o limite que morde.

Guardar a chave em KMS ou HSM, fora do repositório e do host do dado cifrado. Registrar, por chave: identificador, data de criação, criptoperíodo, dado que protege e sistema que a usa. Persistir a versão da chave junto do registro cifrado, sem o que a rotação exige reprocessar toda a base. Em incidente, o inventário é o que define o escopo do que vazou.

**Gatilhos.**
- chave de criptografia no mesmo repositório, banco ou volume do dado cifrado
- chave em variável de ambiente do mesmo host, sem KMS ou HSM
- ausência de campo de versão de chave no registro cifrado
- ausência de inventário de chaves e de política documentada
- chave sem data de criação nem criptoperíodo declarado
- mesma chave em desenvolvimento, homologação e produção
- chave privada acessível a mais de uma entidade ou serviço
- código de rotação inexistente, ou existente e nunca executado

**Relacionados.** SEC:repouso.nonce · SEC:segredos.armazenamento · LGPD:art46

---

## SEC:repouso.camadas

**Ementa.** Camadas de cifragem em repouso e o que cada uma não protege.

**Literal.**
> OWASP Cryptographic Storage Cheat Sheet — a cifragem pode ocorrer na aplicação, no banco (por exemplo SQL Server TDE), no filesystem (BitLocker, LUKS) ou em hardware. O documento não elege uma camada: o modelo de ameaça determina a camada.

Fonte: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html — verificada em 2026-08-11.

**Fonte.** https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A tabela abaixo é inferência de engenharia a partir da fonte, não citação.

| Camada | Protege contra | Não protege contra |
|---|---|---|
| Disco ou volume (LUKS, BitLocker, EBS encryption) | Furto físico do disco ou da VM desligada | Qualquer acesso com o sistema ligado: SQL injection, credencial vazada, backup lógico, dump, DBA malicioso |
| Banco inteiro, TDE | Furto do arquivo de dados e do backup físico | Os mesmos cenários acima: a query autenticada vê texto claro |
| Campo, em nível de aplicação | Acesso ao banco, dump, backup, DBA, log de query | Comprometimento do processo da aplicação que detém a DEK |

Disco e TDE são piso. Para CPF, nome e campos de texto livre com dado de paciente, cifragem em nível de campo com envelope encryption (DEK por registro ou por tenant, KEK em KMS ou HSM) é o que sobrevive ao cenário de credencial vazada e dump de banco. Descrever "servidor criptografado" em DPIA ou em resposta a incidente sem indicar a camada não descreve o controle existente.

**Gatilhos.**
- documentação, DPIA ou resposta a incidente que declara dados criptografados com base apenas em disco cifrado ou TDE
- CPF, nome e campos de texto livre em claro no banco, com apenas TDE
- backup, dump de desenvolvimento ou exportação em planilha sem cifragem
- ambiente de homologação restaurado a partir de dump de produção
- réplica de leitura ou data warehouse sem a cifragem aplicada na origem
- anexo (PDF de laudo, DICOM) em bucket sem cifragem em nível de objeto

**Relacionados.** SEC:repouso.chaves · SEC:anonimizacao.quase-identificadores

---

## SEC:repouso.pqc

**Ementa.** Migração para criptografia pós-quântica.

**Literal.**
> OWASP ASVS 5.0, 11.1.4: exige plano documentado de migração para PQC.
> OWASP TLS Cheat Sheet: a lista recomendada de grupos começa por `X25519MLKEM768`, esquema híbrido pós-quântico.
> OWASP Cryptographic Storage Cheat Sheet: nenhuma orientação sobre PQC (ausência verificada em 2026-08-11).

Fontes: https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x20-V11-Cryptography.md · https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html · https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html — verificadas em 2026-08-11.

**Fonte.** https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x20-V11-Cryptography.md · https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html · https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html · https://csrc.nist.gov/pubs/ir/8547/ipd · verificado em 2026-08-11

**Confiança.** primária-parcial

**Severidade.** boa-prática

**Aplicação.** Prontuário tem retenção legal de décadas, o que expõe o dado ao cenário de captura hoje e decifragem depois. O requisito da ASVS é um plano documentado, e o pré-requisito do plano é o inventário criptográfico da 11.1.2. Em TLS, a adoção do grupo híbrido é configuração de servidor.

**Gatilhos.**
- ausência de plano de migração PQC em sistema com retenção legal longa
- ausência de inventário criptográfico
- lista de grupos TLS sem `X25519MLKEM768` em serviço novo

**Incerteza.** As fontes da OWASP divergem: o Cryptographic Storage Cheat Sheet não trata de PQC, a ASVS 5.0 exige plano, e o TLS Cheat Sheet já coloca o híbrido em primeiro lugar. Adotamos a ASVS. `PARCIALMENTE VERIFICADO`: NIST IR 8547, "Transition to Post-Quantum Cryptography Standards", consta como Initial Public Draft de 12/11/2024, com comentários encerrados em 10/01/2025; a publicação de versão final não foi confirmada até 2026-08-11. `NÃO VERIFICADO`: o cronograma de depreciação em 2030 e proibição em 2035, que não foi extraído da fonte primária, e não deve ser citado. `NÃO VERIFICADO`: datas e números de FIPS 203, 204 e 205.

**Relacionados.** SEC:tls.suites · SEC:repouso.chaves

---

## SEC:anonimizacao.evidencia

**Ementa.** Evidência quantitativa de reidentificação a partir de atributos demográficos.

**Literal.**
> Sweeney, L. "Simple Demographics Often Identify People Uniquely". Carnegie Mellon University, Data Privacy Working Paper 3, Pittsburgh, 2000. CEP de 5 dígitos, sexo e data de nascimento completa tornam 87,1% da população dos Estados Unidos provavelmente única — 216 de 248 milhões, Experimento B. Município ou cidade, sexo e data de nascimento: 58,38%, Experimento F, Figura 29, verbatim: "58.38% of the population of the United States is likely to be uniquely identified". Condado, sexo e data de nascimento: 18,1%, Experimento J, Figura 31. A Figura 32 consolida os três, com o valor de Place arredondado: County 18.1 · Place 58.4 · ZIP 87.1. https://dataprivacylab.org/projects/identifiability/paper1.pdf
> Divergência interna do próprio paper: o abstract informa "132 million of 248 million or 53%" para a combinação de município, sexo e data de nascimento, contra os 58,38% medidos no corpo.
> Rocher, L.; Hendrickx, J. M.; de Montjoye, Y.-A. "Estimating the success of re-identifications in incomplete datasets using generative models". Nature Communications 10, 3069 (2019). DOI 10.1038/s41467-019-10933-3. Quinze atributos demográficos tornam 99,98% das pessoas de Massachusetts únicas. Modelo treinado com amostra de 1% da população alcançou erro absoluto médio de 0,041, com AUC entre 0,84 e 0,97 em 210 populações. Conclusão dos autores: datasets fortemente amostrados "are unlikely to satisfy the modern standards for anonymization set forth by GDPR". https://www.nature.com/articles/s41467-019-10933-3

Ambas verificadas em 2026-08-11.

**Fonte.** https://dataprivacylab.org/projects/identifiability/paper1.pdf · https://www.nature.com/articles/s41467-019-10933-3 · https://api.crossref.org/works/10.1038/s41467-019-10933-3 · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Remover nome e CPF não produz dado anonimizado na acepção do art. 12 da LGPD. Rocher 2019 responde ao argumento de que enviar uma amostra reduz o risco: a amostragem não protege. Estes dois números são a evidência a citar em protocolo de pesquisa, DPIA e parecer interno.

Ao citar os 58,38%, indicar Experimento F e Figura 29, que é onde o número aparece com duas casas. A Figura 32 traz o mesmo resultado arredondado para 58,4. O abstract do mesmo paper traz 53%. Quem citar só o número, sem a localização, pode ser confrontado com o abstract. Vale a mesma cautela em Rocher 2019: o corpo do artigo fala em pessoas de Massachusetts e o abstract fala em "99.98% of Americans".

**Gatilhos.**
- dataset descrito como anonimizado contendo data de nascimento completa
- CEP completo em base de pesquisa ou em arquivo compartilhado
- combinação de sexo, data de nascimento e município em arquivo enviado a terceiro
- amostragem apresentada como medida de anonimização em protocolo ou DPIA
- exportação de subconjunto de pacientes com a justificativa de que "são poucos casos"

**Relacionados.** LGPD:art12 · SEC:anonimizacao.quase-identificadores

---

## SEC:anonimizacao.quase-identificadores

**Ementa.** Quase-identificadores em prontuário e as regras numéricas do Safe Harbor.

**Literal.**
> HIPAA Safe Harbor, 18 identificadores (lista verificada): nome; subdivisões geográficas (endereço, cidade, condado, CEP completo); todos os elementos de data exceto o ano, quando ligados ao indivíduo; telefone; fax; e-mail; número de seguro social; número de prontuário; número de beneficiário de plano; número de conta; certificado ou licença; identificador de veículo; identificador de dispositivo; URL; IP; identificador biométrico; foto de face inteira; e qualquer outro número, característica ou código único.
> Regras numéricas do Safe Harbor (verificadas): CEP — apenas os três primeiros dígitos podem permanecer, e somente se a unidade geográfica formada por todos os CEPs com os mesmos três dígitos iniciais contiver mais de 20.000 pessoas; 17 prefixos restritos devem ser convertidos em `000`. Idade — todas as idades acima de 89 e todos os elementos de data, inclusive o ano, que indiquem tal idade devem ser recodificados como "90 ou mais". Datas — apenas o ano.

Fonte: https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html — publicada em 07/09/2012, última modificação em 03/02/2025, verificada em 2026-08-11.

**Fonte.** https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O Safe Harbor é regime dos Estados Unidos. O Brasil não tem equivalente: o art. 12 da LGPD adota padrão de risco ("esforços razoáveis"). Usar a lista como piso operacional de varredura, não como salvo-conduto jurídico. Quase-identificadores de prontuário que costumam ficar de fora da varredura:

| Campo | Por que reidentifica |
|---|---|
| Data de nascimento completa | Componente do resultado de 87% de Sweeney. Recodificar para ano ou faixa quinquenal |
| CEP completo | Idem. Truncar para três dígitos com teste de população |
| Data do procedimento, da internação ou do óbito | Cruzável com registro hospitalar, obituário, mídia social e agenda cirúrgica pública |
| CID de doença rara | Identificador direto em população pequena; generalização de CEP não resolve |
| Sexo, idade, serviço e hospital em combinação | Em serviço com poucos casos por ano, produz k=1 |
| Texto livre da evolução | Contém nome de familiar, profissão, endereço e referência ao próprio paciente |
| Imagem DICOM | Metadados carregam nome, data de nascimento e prontuário; CT e MRI de crânio permitem reconstrução facial |
| Número de série de dispositivo (marca-passo, CDI, stent) | Identificador único, item 13 da lista |

O que a análise costuma precisar é o intervalo em dias desde a linha de base, não a data-calendário.

**Gatilhos.**
- coluna `data_nascimento`, `dt_nasc`, `dob`, `nascimento` em dataset dito anonimizado
- coluna `cep` com 8 dígitos
- colunas `data_procedimento`, `data_internacao`, `data_alta`, `data_obito` em data-calendário
- idade acima de 89 preservada em dataset a compartilhar
- campo de texto livre (`evolucao`, `historia`, `observacao`, `laudo`) exportado sem tratamento
- arquivo DICOM sem remoção de `PatientName`, `PatientBirthDate`, `PatientID`, `AccessionNumber`
- imagem de crânio compartilhada sem defacing
- coluna de número de série de dispositivo
- CID de doença rara em coorte pequena
- PDF de laudo digitalizado anexado a base declarada anonimizada
- colunas `prontuario`, `matricula`, `carteirinha`, `ip`, `url` mantidas

**Incerteza.** O Brasil não tem lista fechada equivalente. Não existe checklist que garanta anonimização no direito brasileiro.

**Relacionados.** LGPD:art12 · SEC:anonimizacao.anpd · SEC:anonimizacao.evidencia

---

## SEC:anonimizacao.anpd

**Ementa.** Posição da ANPD: anonimização como processo contínuo baseado em risco.

**Literal.**
> ANPD, "Estudo Técnico sobre Anonimização de Dados na LGPD: Uma Visão de Processo Baseado em Risco e Técnicas Computacionais", v1.0, novembro/2023. Autores: Marcelo Santiago Guedes (coord.), Diego Carvalho Machado e Albert França Josuá Costa.
> Relato de literatura, p. 7, verbatim: "Narayanan e Shmatikov (2010) discorrem sobre os mitos e as falácias associados à anonimização de dados ao afirmarem que não há técnica com eficácia plena, estando todas elas sujeitas a ataques de reidentificação, isto é, riscos de reidentificação."
> Posição própria da ANPD, na sequência imediata da mesma passagem, verbatim: "Por esse motivo, a anonimização deve ser entendida como um processo contínuo baseado em riscos [...]"
> Processo em três fases: determinar o Risco de Reidentificação Aceitável (RRA) conforme o contexto, incluindo presença de dado sensível e de dado financeiro; aplicar técnicas até não exceder o RRA; medir o Risco de Reidentificação (RRM). Fórmula: RRM = VC × θ, em que VC é a ponderação de variáveis contextuais e θ o valor da métrica geral. O modelo se baseia em classes de equivalência.
> Técnicas citadas para texto estruturado: generalização, mascaramento, permutação e adição de ruído. Para imagens: tarja nos olhos, permutação por blocos, ruído gaussiano, desfoque gaussiano, pixelação e DP Pix.
> Citação sobre parâmetros, referida à etapa de determinação do RRA, verbatim com o antecedente: "Essa primeira etapa é de extrema importância e possui uma gama de variáveis dependentes do contexto que devem ser observadas pelo agente de tratamento. Desse modo, não é possível estabelecer uma metodologia padronizada a todos os casos."
> Ausências verificadas no documento: k-anonimato, l-diversidade e t-proximidade aparecem apenas como referência bibliográfica, sem tratamento técnico; privacidade diferencial e dados sintéticos não aparecem como técnicas para dado estruturado, e "DP Pix" é citado só na lista de técnicas para imagem; o estudo não define explicitamente "quase-identificador", trabalhando com classes de equivalência.

Fonte: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos/estudo_tecnico_sobre_anonimizacao_de_dados_na_lgpd_uma_visao_de_processo_baseado_em_risco_e_tecnicas_computacionais.pdf — verificada em 2026-08-11. Documento jurídico companheiro: `estudo_tecnico_sobre_anonimizacao_de_dados_na_lgpd___analise_juridica.pdf`, novembro/2023.

Referência complementar, NIST:
> NIST SP 800-188, "De-Identifying Government Datasets: Techniques and Governance", final de 14/09/2023: exige Disclosure Review Board para supervisionar o processo e estudos de reidentificação antes da publicação ("perform re-identification studies to gauge the risk"); descreve quatro modelos de liberação (publicar de-identificado, publicar sintético, interface de consulta com de-identificação, enclave protegido não-público); não fixa valores de k nem de ε (verificado no abstract). https://csrc.nist.gov/pubs/sp/800/188/final
> NIST SP 800-226, "Guidelines for Evaluating Differential Privacy Guarantees", final publicado em 06/03/2025 (draft de 11/12/2023): estrutura em pirâmide de privacidade diferencial e documenta "privacy hazards"; notebooks Jupyter suplementares em repositório GitHub. https://csrc.nist.gov/pubs/sp/800/226/final

**Fonte.** https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos/estudo_tecnico_sobre_anonimizacao_de_dados_na_lgpd_uma_visao_de_processo_baseado_em_risco_e_tecnicas_computacionais.pdf · https://csrc.nist.gov/pubs/sp/800/188/final · https://csrc.nist.gov/pubs/sp/800/226/final · verificado em 2026-08-11

**Confiança.** primária-parcial

**Severidade.** risco

**Aplicação.** A frase sobre ausência de técnica com eficácia plena é relato de Narayanan e Shmatikov feito pela ANPD, não formulação da Autoridade. Atribuí-la à ANPD em parecer expõe a citação a refutação fácil. O que é da ANPD é a conclusão: a anonimização é processo contínuo baseado em riscos, e não estado binário irreversível.

Não existe norma brasileira com parâmetro numérico de anonimização. Quem precisa justificar a anonimização importa k, ℓ ou ε da literatura ou do NIST e documenta a escolha: qual risco foi aceito, qual técnica foi aplicada, qual métrica foi medida, quem revisou e em que data. A declaração "os dados foram anonimizados" sem esse registro não sustenta o art. 12 em fiscalização.

**Gatilhos.**
- documento interno declarando dados anonimizados sem registro de método, risco aceito e medição
- protocolo de pesquisa que trata anonimização como estado binário
- ausência de estudo de reidentificação antes de publicar ou compartilhar base
- pipeline de desidentificação sem teste automatizado de reidentificação
- ausência de responsável nomeado pela decisão de liberação da base

**Incerteza.** `NÃO VERIFICADO`: valores concretos de ε e a lista de "privacy hazards" do NIST SP 800-226, dos quais só o abstract foi lido.

**Relacionados.** LGPD:art12 · LGPD:art13 · SEC:anonimizacao.tecnicas

---

## SEC:anonimizacao.tecnicas

**Ementa.** k-anonimato, l-diversidade e privacidade diferencial: definição e limite de cada uma.

**Literal.**
> k-anonimato: Sweeney, L. "k-ANONYMITY: A MODEL FOR PROTECTING PRIVACY". *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, v. 10, n. 5, p. 557–570, outubro/2002. DOI 10.1142/S0218488502001648. https://www.worldscientific.com/doi/abs/10.1142/s0218488502001648 — a página da editora retorna HTTP 403; volume, número, páginas, mês e DOI confirmados por metadados do Crossref.
> l-diversidade: Machanavajjhala, A.; Kifer, D.; Gehrke, J.; Venkitasubramaniam, M. "L-diversity: Privacy beyond k-anonymity". *ACM Transactions on Knowledge Discovery from Data*, v. 1, n. 1, 2007. DOI 10.1145/1217299.1217302. https://dl.acm.org/doi/10.1145/1217299.1217302 — verificada. Versão anterior em conferência: ICDE 2006.
> t-proximidade (t-closeness): Li, N.; Li, T.; Venkatasubramanian, S. "t-Closeness: Privacy Beyond k-Anonymity and l-Diversity". *2007 IEEE 23rd International Conference on Data Engineering (ICDE)*, p. 106–115. DOI 10.1109/ICDE.2007.367856 — confirmada por metadados do Crossref.
> Privacidade diferencial: Dwork, C.; McSherry, F.; Nissim, K.; Smith, A. "Calibrating Noise to Sensitivity in Private Data Analysis". *Theory of Cryptography Conference (TCC 2006)*, Lecture Notes in Computer Science, p. 265–284. DOI 10.1007/11681878_14 — confirmada por metadados do Crossref.

Metadados de Sweeney 2002, t-proximidade e privacidade diferencial confirmados na API do Crossref, https://api.crossref.org, em 2026-08-11. A referência de l-diversidade já constava verificada.

**Fonte.** https://api.crossref.org/works/10.1142/S0218488502001648 · https://api.crossref.org/works/10.1145/1217299.1217302 · https://api.crossref.org/works/10.1109/ICDE.2007.367856 · https://api.crossref.org/works/10.1007/11681878_14 · verificado em 2026-08-11

**Confiança.** primária-parcial

**Severidade.** risco

**Aplicação.** Definições operacionais, nossas:

- k-anonimato: cada combinação de quase-identificadores aparece em pelo menos k registros. Falha residual: se todos os k pacientes da classe têm o mesmo CID, o atacante aprende o diagnóstico sem precisar distinguir qual paciente é qual (ataque de homogeneidade).
- l-diversidade: exige pelo menos ℓ valores bem representados do atributo sensível dentro de cada classe de equivalência. Responde ao ataque de homogeneidade.
- Privacidade diferencial: garantia matemática sobre o mecanismo de consulta, não sobre o dataset publicado, parametrizada pelo orçamento ε. Em coorte clínica pequena, o ε útil e o ε protetor raramente coexistem. É ferramenta de estatística agregada, com pouco uso no compartilhamento de prontuário.

O valor de k e de ε não vem de norma brasileira. Escolher, registrar a justificativa e medir.

**Gatilhos.**
- base a compartilhar sem k declarado e medido
- classe de equivalência com k=1 (registro único) na base
- todos os registros de uma classe com o mesmo valor de atributo sensível
- uso de privacidade diferencial para liberar registro individual em vez de estatística agregada
- generalização aplicada a CEP e idade sem verificar o efeito nas classes de equivalência

**Relacionados.** SEC:anonimizacao.anpd · SEC:anonimizacao.quase-identificadores

---

## SEC:anonimizacao.pseudonimizacao

**Ementa.** Separação da informação adicional que permite reidentificar.

**Literal.**
> EDPB, Guidelines 01/2025 on Pseudonymisation. **STATUS: DRAFT.** Consulta pública de 17/01/2025 a 14/03/2025. A adoção de versão final não foi confirmada até 2026-08-11; a página consultada continua marcando o documento como draft em consulta. Não citar como diretriz final do EDPB.
> Posições centrais do draft: o dado pseudonimizado permanece dado pessoal enquanto a reidentificação for tecnicamente possível por meio de informação adicional; o conceito de "pseudonymisation domain" delimita quem pode reidentificar; a informação adicional deve ser mantida separada, com acesso restrito, protegida por medidas técnicas e organizacionais; medidas citadas: criptografia, gestão segura de chaves e RBAC.
> https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-012025-pseudonymisation_en · PDF do draft: https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf — verificadas em 2026-08-11.
> LGPD, art. 13, §4º: a pseudonimização é o tratamento por meio do qual o dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro.
> LGPD, art. 13, caput: na realização de estudos em saúde pública, os órgãos de pesquisa poderão ter acesso a bases de dados pessoais, "que serão tratados exclusivamente dentro do órgão e estritamente para a finalidade de realização de estudos e pesquisas e mantidos em ambiente controlado e seguro, conforme práticas de segurança previstas em regulamento específico e que incluam, sempre que possível, a anonimização ou pseudonimização dos dados". O §2º veda, "em circunstância alguma, a transferência dos dados a terceiro".

**Fonte.** https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-012025-pseudonymisation_en · https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf · https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm · verificado em 2026-08-11

**Confiança.** primária-parcial

**Severidade.** bloqueante no escopo do art. 13 da LGPD; risco nos demais usos

**Aplicação.** O "pseudonymisation domain" do EDPB e o art. 13, §4º, da LGPD descrevem o mesmo arranjo: tabela de correspondência entre identificador e paciente em banco separado, com credencial separada, sob custódia de pessoa distinta de quem analisa. Manter a planilha de correspondência na mesma pasta do dataset colapsa o domínio e equivale a não pseudonimizar. Pseudônimo derivado do próprio dado do paciente sem segredo é reversível por força bruta.

**Gatilhos.**
- planilha ou tabela de correspondência ID↔paciente na mesma pasta, bucket, banco ou Drive do dataset
- mesma credencial dá acesso ao dataset e à tabela de correspondência
- chave ou dicionário de pseudonimização versionado no repositório
- pseudônimo gerado por hash de CPF ou de prontuário sem sal secreto (`md5(cpf)`, `sha256(prontuario)`)
- dataset pseudonimizado tratado como fora do alcance da LGPD
- ausência de responsável nomeado pela custódia da tabela de correspondência

**Relacionados.** LGPD:art13 · LGPD:art12 · SEC:segredos.privilegio

---

## SEC:llm.owasp-top10

**Ementa.** OWASP Top 10 for LLM Applications, versão vigente.

**Literal.**
> Página oficial do recurso: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/, datada de 3 de agosto de 2026. PDF oficial: https://genai.owasp.org/download/56857/, 122 páginas, baixado e conferido em 2026-08-11. A lista abaixo é o índice do PDF oficial.
> Metodologia, verbatim da "Letter from the Project Leads": "We pulled together a corpus of 7,714 real incidents from public vulnerability databases and an AI-harm database, and we built classifiers that read them and placed the 6,639 that carried enough detail to sort." E: "The community vote carries three-quarters of the weight. The incident data covers the remaining quarter." Os riscos são mapeados para NIST, MITRE ATLAS, CWE e para o OWASP Top 10 for Agentic Applications.
> Movimentações, verbatim da seção "What's New in the 2026 Top 10": Excessive Agency "climbed to third"; Unbounded Consumption "rose four places"; Improper Output Handling "fell the furthest, from fifth to tenth"; "What used to be System Prompt Leakage is now Hidden Context Exposure".
> A lista de 2025 permanece referenciada em https://genai.owasp.org/llm-top-10/ e foi verificada em fonte oficial: LLM01 Prompt Injection … LLM10 Unbounded Consumption.

| 2026 | Título | 2025 | Mudança |
|---|---|---|---|
| LLM01 | Prompt Injection | #1 | Escopo ampliado: ataques cross-modais, persistência em memória, blast radius agêntico |
| LLM02 | Sensitive Information Disclosure | #2 | Manteve a segunda posição; segundo o documento, "the one place at the top where belief and evidence simply agree" |
| LLM03 | Excessive Agency | #6 | Subida de três posições, atribuída a deploys agênticos reais |
| LLM04 | Supply Chain | #3 | Absorve falha de confiança em artefato |
| LLM05 | Data and Model Poisoning | #4 | Absorve subversão de fine-tuning |
| LLM06 | Unbounded Consumption | #10 | Reenquadrado de DoS para assimetria de custo; cadeias de ferramentas MCP; controle de custo por token |
| LLM07 | Misinformation | #9 | Passa a cobrir chamadas de ferramenta e falha em sistema downstream |
| LLM08 | Hidden Context Exposure | #7 | Renomeado de "System Prompt Leakage"; amplia para schemas de ferramenta, políticas de RAG e instruções de desenvolvedor |
| LLM09 | Vector and Embedding Weaknesses | #8 | Escopo inalterado |
| LLM10 | Improper Output Handling | #5 | Queda de cinco posições; cobre sinks ANSI e terminal e renderizadores com auto-fetch como canais de exfiltração |

Numeração e títulos vêm do índice do PDF oficial. A coluna "Mudança" é resumo nosso da seção "What's New in the 2026 Top 10", cujas passagens literais estão acima.

**Fonte.** https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ · https://genai.owasp.org/download/56857/ · https://genai.owasp.org/llm-top-10/ · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Usar a lista como taxonomia de auditoria de integração com LLM. A numeração de 2026 pode ser citada como fonte primária: veio do índice do PDF oficial. Ao citar, registrar a data da página do recurso, 3 de agosto de 2026, porque a lista é revista por versão anual.

**Gatilhos.**
- conteúdo de documento do paciente concatenado no mesmo prompt que a instrução de sistema (LLM01)
- saída de LLM renderizada como HTML ou markdown sem sanitização (LLM10)
- interface que carrega automaticamente recurso externo referenciado na saída do modelo (LLM10)
- resposta de LLM interpolada em query SQL, comando de shell ou `eval` (LLM10)
- segredo, credencial ou regra de negócio confidencial no system prompt (LLM08)
- ausência de limite de tokens e de custo por requisição e por usuário (LLM06)
- índice vetorial sem filtro de paciente ou de tenant aplicado no índice (LLM09)
- filtro de isolamento entre pacientes implementado apenas por instrução no prompt (LLM09)
- dependência de modelo, plugin ou pacote de prompt sem verificação de origem (LLM04)

**Relacionados.** SEC:llm.agentic · SEC:llm.vetores-clinicos · SEC:segredos.logs

---

## SEC:llm.agentic

**Ementa.** OWASP Top 10 for Agentic Applications 2026.

**Literal.**
> Anúncio oficial de 09 a 10/12/2025: https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/ — verificado. Página do recurso: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/, datada de 9 de dezembro de 2025.
> Ameaças destacadas no anúncio oficial: Agent Behavior Hijacking, Tool Misuse and Exploitation, Identity and Privilege Abuse.
> Lista completa, índice do PDF oficial https://genai.owasp.org/download/52117/, baixado e conferido em 2026-08-11: ASI01 Agent Goal Hijack · ASI02 Tool Misuse and Exploitation · ASI03 Identity and Privilege Abuse · ASI04 Agentic Supply Chain Vulnerabilities · ASI05 Unexpected Code Execution (RCE) · ASI06 Memory & Context Poisoning · ASI07 Insecure Inter-Agent Communication · ASI08 Cascading Failures · ASI09 Human-Agent Trust Exploitation · ASI10 Rogue Agents.

**Fonte.** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ · https://genai.owasp.org/download/52117/ · https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/ · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Claude Code e Claude Cowork são agentes com ferramentas e memória, e entram nesta taxonomia. Antes de dar a um agente acesso a base clínica: credencial de leitura, escopo por tabela, sem DELETE, e aprovação humana em qualquer escrita. A Res. CFM 2.454/2026, art. 15, parágrafo único, torna a supervisão humana obrigatória em decisão clínica.

**Gatilhos.**
- agente com credencial de banco de produção com permissão de escrita (ASI03)
- agente sem etapa de aprovação humana em operação de escrita ou de exclusão
- memória persistente compartilhada entre casos ou entre pacientes (ASI06)
- ferramenta de execução de código com acesso à rede no mesmo contexto em que trafega dado de paciente (ASI05)
- token de nuvem com escopo de owner ou admin entregue ao agente (ASI03)
- ferramenta de requisição HTTP arbitrária disponível ao agente que lê documento externo (ASI02)
- comunicação entre agentes sem autenticação (ASI07)
- arquivo de configuração de agente (skill, comando, MCP) obtido de fonte não verificada (ASI04)

**Relacionados.** CFM-2454-2026:art15 · SEC:llm.owasp-top10 · SEC:segredos.privilegio

---

## SEC:llm.nist

**Ementa.** NIST AI RMF e o perfil de IA generativa.

**Literal.**
> NIST AI 100-1, AI Risk Management Framework 1.0, publicado em 26/01/2023. A página oficial declara: "The AI RMF 1.0 is being revised". Não há versão 2.0 publicada até 2026-08-11. Funções centrais: GOVERN, MAP, MEASURE, MANAGE. Em 07/04/2026 o NIST publicou concept note para um AI RMF Profile on Trustworthy AI in Critical Infrastructure. https://www.nist.gov/itl/ai-risk-management-framework
> NIST AI 600-1, "AI RMF: Generative Artificial Intelligence Profile", julho/2024, release de 26/07/2024. Doze riscos de IA generativa, lista verbatim: CBRN Information or Capabilities; Confabulation; Dangerous, Violent, or Hateful Content; Data Privacy; Environmental Impacts; Harmful Bias or Homogenization; Human-AI Configuration; Information Integrity; Information Security; Intellectual Property; Obscene, Degrading, and/or Abusive Content; Value Chain and Component Integration. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
> Data Privacy, verbatim do documento: modelos podem revelar informação sensível via "data memorization", vazando ou inferindo corretamente PII; "GAI models may be able to correctly infer PII or sensitive data that was not in their training data" pela combinação de fontes díspares; há riscos de privacidade agravados "even for data present only in a small number of training samples".
> Information Security: prompt injection é definida como modificação de entrada para induzir comportamento inesperado; indirect prompt injection é a injeção remota de prompt em dados que o modelo consome, podendo levar a roubo de dado ou execução de código malicioso.

Verificadas em 2026-08-11.

**Fonte.** https://www.nist.gov/itl/ai-risk-management-framework · https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** "Confabulation" é o termo do NIST para alucinação, e dá vocabulário auditável em parecer e em protocolo. A lista de 12 riscos serve de mapa para a avaliação preliminar exigida pelo art. 12 da Res. CFM 2.454/2026. As funções GOVERN, MAP, MEASURE e MANAGE só são verificáveis se houver registro de prompt, resposta, versão do modelo e revisão humana.

**Gatilhos.**
- ausência de avaliação de risco documentada antes de colocar LLM em fluxo clínico
- ausência de registro da versão do modelo em cada chamada
- ausência de registro do prompt e da resposta para auditoria
- documentação do fornecedor sem descrição de limitações e de vieses
- ausência de métrica de erro do modelo em uso clínico

**Relacionados.** CFM-2454-2026:art12 · CFM-2454-2026:art3 · SEC:llm.memorizacao

---

## SEC:llm.memorizacao

**Ementa.** Memorização e extração de dado de treino.

**Literal.**
> Nasr, M.; Carlini, N.; Hayase, J.; Jagielski, M.; Cooper, A. F.; Ippolito, D.; Choquette-Choo, C. A.; Wallace, E.; Tramèr, F.; Lee, K. "Scalable Extraction of Training Data from (Production) Language Models". arXiv:2311.17035, 28/11/2023. https://arxiv.org/abs/2311.17035 — verificado em 2026-08-11.
> Resultados: gigabytes de dado de treino extraídos de modelos open-source (Pythia, GPT-Neo), semi-abertos (LLaMA, Falcon) e fechados (ChatGPT). O "divergence attack" faz o modelo alinhado divergir do estilo de chatbot e emitir dado de treino a taxa 150 vezes maior. Conclusão citável: "current alignment techniques do not eliminate memorization".
> `NÃO EXTRAÍDOS do abstract`: custo do ataque e taxa específica de extração de PII.
> Carlini, N. et al. "Extracting Training Data from Large Language Models", USENIX Security 2021. https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting — existência e venue verificados por busca; conteúdo não fetchado.

**Fonte.** https://arxiv.org/abs/2311.17035 · https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting · verificado em 2026-08-11

**Confiança.** primária-parcial

**Severidade.** risco

**Aplicação.** Fine-tuning e treino com dado identificável de paciente criam risco de extração posterior, e o alinhamento do modelo não elimina esse risco. O art. 6º, §2º, da Res. CFM 2.454/2026 sujeita o uso de dado pessoal para treinamento, validação e aprimoramento aos princípios de proteção de dados. Exemplos few-shot dentro do prompt são dado enviado ao provedor como qualquer outro.

**Gatilhos.**
- fine-tuning ou treino com dataset contendo dado identificável de paciente
- exemplos few-shot no prompt construídos a partir de caso real identificável
- base vetorial de RAG construída com prontuário identificável e exposta a múltiplos usuários
- dataset de avaliação com dado real versionado no repositório
- uso de provedor cuja configuração padrão utiliza os inputs para treinamento

**Relacionados.** CFM-2454-2026:art6 · CFM-2454-2026:anexoI.XV-XVI · PROV:comparativo

---

## SEC:llm.vetores-clinicos

**Ementa.** Vetores de vazamento em aplicação clínica com LLM.

**Literal.** Item derivado. As âncoras são as fontes já citadas: OWASP Top 10 for LLM Applications 2026 (`SEC:llm.owasp-top10`), OWASP Top 10 for Agentic Applications 2026 (`SEC:llm.agentic`), NIST AI 600-1 (`SEC:llm.nist`), OWASP Logging Cheat Sheet (`SEC:segredos.logs`) e as políticas de provedor da ficha 12.

**Fonte.** item derivado; âncoras abertas e conferidas nesta sessão — https://genai.owasp.org/download/56857/ · https://genai.owasp.org/download/52117/ · https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf · https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Mapeamento operacional, nosso, com a âncora de cada linha.

| Vetor | Âncora | Controle |
|---|---|---|
| Dado de paciente no prompt vai para o log da aplicação | LLM02:2026; OWASP Logging Cheat Sheet | Não logar `messages[]`; logar identificador da requisição, hash, contagem de tokens, latência e status |
| Dado persistido pelo provedor | Políticas de retenção, ficha 12 | ZDR contratado antes do primeiro envio; verificar em Privacy Controls |
| Dado usado para treino | NIST AI 600-1, Data Privacy; políticas de provedor | Apenas planos comerciais ou API; nunca conta de consumidor |
| Prompt injection indireta via documento do paciente | NIST AI 600-1, Information Security; LLM01:2026 | Tratar PDF, laudo e e-mail como conteúdo não confiável; não dar ao agente ferramenta de exfiltração no mesmo contexto |
| Exfiltração por renderizador com auto-fetch | LLM10:2026 | Desabilitar carregamento automático de recurso externo na UI que renderiza saída de LLM |
| Contexto oculto exposto (system prompt, schema de ferramenta, política de RAG) | LLM08:2026 | Nenhum segredo, credencial ou regra confidencial no system prompt |
| Agência excessiva do agente sobre a base de produção | LLM03:2026; ASI03 | Credencial de leitura, escopo por tabela, sem DELETE, aprovação humana na escrita |
| Memória ou contexto envenenado entre sessões | ASI06 | Não persistir memória entre pacientes; uma sessão por caso |
| Vazamento entre pacientes por RAG mal isolado | LLM09:2026 | Filtro de tenant ou de paciente no índice, não no prompt |

**Gatilhos.**
- ausência de etapa de desidentificação antes da chamada ao provedor
- payload da chamada montado a partir do registro do paciente sem seleção de campos
- documento externo (PDF, e-mail, laudo) inserido no contexto do agente que também tem ferramenta de rede
- memória de agente compartilhada entre atendimentos
- retriever sem filtro por paciente aplicado na consulta ao índice
- resposta do provedor gravada em prontuário sem etapa de revisão

**Relacionados.** CFM-2454-2026:art6 · SEC:llm.owasp-top10 · SEC:segredos.logs · PROV:comparativo

---

## SEC:segredos.armazenamento

**Ementa.** Onde a chave de API deve viver.

**Literal.**
> OWASP Secrets Management Cheat Sheet, §3.2 "Where should a secret be?" — o documento lista os lugares onde um segredo pode ficar para execução de CI/CD, sem ordená-los como hierarquia: no próprio ferramental de CI/CD (GitLab, GitHub, Jenkins), com a ressalva de que "This is not the same as committing it to code"; em sistema de gestão de segredos, de provedor de nuvem (AWS Secrets Manager, Azure Key Vault, Google Secret Manager) ou dedicado (HashiCorp Vault, Conjur, Keeper); ou cifrado pelo próprio pipeline via Encryption as a Service e commitado já cifrado. Nota do mesmo parágrafo, verbatim: "not all secrets must be in the CI/CD pipeline to get to the actual deployment. Instead, make sure that the deployed services take care of part of their secrets management at their own lifecycle".
> Restrição ao segredo guardado no ferramental de CI/CD, §3.2.1, verbatim: "No 'big secret': ensure that secrets in your CI/CD tooling that are not long-term, don't have a wide blast radius, and don't have a high value."
> Sobre arquivos de configuração, crítica verbatim: "Many organizations have them hardcoded within the source code in plaintext, littered throughout configuration files". A orientação é centralização.
> Rotação, verbatim: "Depending on a secret's function and what it protects, the lifetime could be from minutes... to years". Credenciais de usuário só devem rotacionar "if there is suspicion or evidence that they have been compromised". A automação é obrigatória.
> Segredos dinâmicos: a aplicação requisita a credencial de banco no start; ao reiniciar, "they would be expired", o que limita a janela de exposição e permite detecção.
> TTLs mencionados: credenciais de CI/CD "rotate frequently and expire after a job completes"; segredos injetados por sidecar com "periodic refresh"; tokens com "short-lived access tokens and... secure refresh token rotation strategy".

Fonte: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html — verificada em 2026-08-11.

**Fonte.** https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** A ordem de preferência é nossa: cofre dedicado primeiro, ferramental de CI/CD só para segredo de vida curta e raio pequeno, e recuperação em runtime pela própria aplicação em vez de o pipeline empurrar o segredo. O documento fornece os critérios; a classificação em níveis não está nele.

Uma chave de API de LLM por ambiente e por serviço, com escopo mínimo e workspace separado. Nunca a mesma chave em desenvolvimento, teste e produção. `.env` fora do controle de versão desde antes do primeiro commit; `.env.example` apenas com nomes de variáveis. O documento não fixa frequência universal de rotação: a frequência é decidida por função do segredo e registrada.

**Gatilhos.**
- `.env` versionado, ou `.gitignore` sem `.env*`
- chave de API em constante do código, em arquivo de configuração ou em `docker-compose.yml` versionado
- notebook `.ipynb` com chave no código ou em output salvo
- mesma chave de API em desenvolvimento, teste e produção
- token sem expiração em integração com laboratório ou HIS
- credencial de banco estática de longa duração em aplicação com dado de paciente
- segredo em screenshot de material de treinamento
- segredo enviado por aplicativo de mensagem ou por e-mail

**Relacionados.** SEC:segredos.deteccao · SEC:repouso.chaves

---

## SEC:segredos.deteccao

**Ementa.** Detecção de segredo commitado e remediação.

**Literal.**
> OWASP Secrets Management Cheat Sheet — ferramenta nomeada: Yelp `detect-secrets`, descrita como "mature and has signature matching for around 20 secrets". Estratégia, verbatim: "Consider enabling secrets detection at the developer level to avoid checking secrets into code before commit/PR either in the IDE, as part of test-driven development, or via pre-commit hook".
> Remediação pós-vazamento, três passos verbatim: revogação — "Keys that were exposed should undergo immediate revocation"; rotação — novo segredo criado e implantado rapidamente, preferencialmente de forma automatizada; deleção — "Secrets revoked/rotated must be removed from the exposed system immediately, including secrets discovered in code or logs".
> GitHub secret scanning: varre histórico do Git, issues, pull requests, discussions, wikis e gists. Gratuito e automático em repositórios públicos; em repositórios privados ou internos exige GitHub Secret Protection (GitHub Team ou Enterprise Cloud). Orientação verbatim: "rotate the affected credential immediately"; reescrever o histórico "is time-intensive and often unnecessary if you've already revoked the credential". https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning
> GitHub push protection: o documento distingue duas formas. *Push protection for users* é específica da conta, só existe no GitHub.com, é habilitada por padrão, bloqueia push de segredo para repositório público e, verbatim, "Does not generate alerts when you bypass push protection unless push protection is also enabled at the repository level". *Push protection for repositories* exige GitHub Secret Protection, é desabilitada por padrão e é habilitada por administrador de repositório, owner de organização, security manager ou enterprise owner; nela, por padrão, qualquer pessoa com permissão de escrita pode contornar informando um motivo, e o contorno cria alerta na aba Security and quality do repositório, da organização e da enterprise, registra o evento no audit log e dispara e-mail para donos de conta, de organização e de enterprise, security managers e administradores do repositório que o acompanham. O motivo informado determina o estado do alerta: "used in tests" e "false positive" criam alerta já fechado; "I'll fix it later" cria alerta aberto. Delegated bypass restringe quem pode contornar. https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection

Verificadas em 2026-08-11.

**Fonte.** https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html · https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning · https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Ordem da resposta a vazamento: revogar, rotacionar, remover de código e de logs. Apagar o commit ou tornar o repositório privado não resolve, porque a credencial já foi exposta. Instalar `detect-secrets` como pre-commit hook em todo repositório clínico.

**Gatilhos.**
- repositório sem pre-commit hook de detecção de segredo
- histórico do Git contendo `sk-`, `AKIA`, `ghp_`, `-----BEGIN PRIVATE KEY-----`, `xoxb-`
- resposta a vazamento consistindo em reescrita de histórico sem revogação da credencial
- repositório privado sem Secret Protection tratado como se tivesse varredura
- bypass de push protection registrado sem justificativa e sem rotação subsequente
- repositório clínico que conta apenas com a push protection de conta, sem push protection de repositório, e por isso não gera alerta quando alguém contorna o bloqueio
- chave de API presente em issue, pull request, wiki ou gist

**Incerteza.** gitleaks e TruffleHog aparecem em comparativos, mas a funcionalidade não foi verificada em documentação primária nesta sessão: `FONTE SECUNDÁRIA`.

**Relacionados.** SEC:segredos.armazenamento · SEC:segredos.privilegio

---

## SEC:segredos.privilegio

**Ementa.** Menor privilégio e auditoria de acesso ao segredo.

**Literal.**
> OWASP Secrets Management Cheat Sheet, verbatim: "Engineers should not have access to all secrets in the secrets management system, and the Least Privilege principle should be applied", com controle de acesso fino por objeto e por componente.
> Nota específica de Azure: as permissões são atribuídas no nível do Key Vault, o que exige Key Vaults separados para cargas de trabalho e para níveis de sensibilidade distintos.
> Segredo em log, proibição: "implement either an encryption or masking approach in place to avoid logging plaintext secrets".
> O log de auditoria do cofre deve registrar: quem pediu o segredo, para qual sistema e papel; quando foi usado e por quem ou pelo quê; tentativas de reuso de segredo expirado; erros de autenticação e de autorização.
> ANPD, Guia de Segurança da Informação para Agentes de Tratamento de Pequeno Porte: "o menor nível de acesso necessário"; controle de acesso em três componentes — autenticação, autorização e auditoria.

Fontes: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html · https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-vf.pdf — verificadas em 2026-08-11.

**Fonte.** https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html · https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-vf.pdf · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** Segregar cofres por sensibilidade. Nenhum desenvolvedor com acesso a todos os segredos. Em serviço clínico, a credencial de aplicação usada pelo LLM ou pelo agente é de leitura, com escopo por tabela.

**Gatilhos.**
- chave de API única compartilhada por toda a equipe
- chave de provedor de LLM sem workspace ou projeto separado por serviço
- todos os segredos no mesmo cofre, sem separação por sensibilidade
- ausência de log de quem requisitou qual segredo
- credencial de aplicação com permissão de DDL, DELETE ou de superusuário no banco
- papel de acesso concedido a grupo amplo (`everyone`, `authenticated`) em bucket com dado de paciente
- ausência de revisão periódica de quem tem acesso

**Relacionados.** SEC:llm.agentic · SEC:anonimizacao.pseudonimizacao

---

## SEC:segredos.logs

**Ementa.** Logs que capturam dado de paciente.

**Literal.**
> OWASP Logging Cheat Sheet — o que não logar, lista verbatim, com tratamento "removed, masked, sanitized, hashed, or encrypted": código-fonte da aplicação; session IDs (se necessário, valor hasheado); access tokens e chaves de criptografia; senhas de autenticação; strings de conexão de banco; dados de cartão e de conta bancária; dados pessoais sensíveis e PII, incluindo informação de saúde e documentos de identidade; informação comercialmente sensível; e dados cuja coleta o usuário não consentiu.
> O que logar sempre: falhas de validação de entrada; sucessos e falhas de autenticação; falhas de autorização e de controle de acesso; falhas de gestão de sessão; erros de aplicação e eventos de sistema; ações administrativas, como criação e exclusão de usuário e mudança de privilégio; acesso a dado sensível; atividades de criptografia; import e export de dados e upload de arquivo; e atividades suspeitas de lógica de negócio, cuja primeira subalínea é, verbatim: "Attempts to perform a set actions out of order/bypass flow control".
> Proteção do log, em repouso: "Build in tamper detection so you know if a record has been modified or deleted"; cópia em mídia read-only o quanto antes; "All access to the logs must be recorded and monitored"; privilégio de leitura restrito e revisado periodicamente.
> Em trânsito: protocolo seguro em rede não confiável. Retenção: conforme obrigação legal ou regulatória, com destruição após o prazo e sem manter além do necessário.

Fonte: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html — verificada em 2026-08-11.

**Fonte.** https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** risco

**Aplicação.** O documento manda logar o acesso a dado sensível e proíbe logar dado de saúde. A implementação que atende às duas regras registra o evento de acesso — quem, quando, qual recurso por identificador pseudonimizado, resultado — e nunca o conteúdo acessado. Middleware de redaction antes do logger, derrubando `messages[]`, `prompt`, `completion`, `Authorization`, `api_key`, `cpf`, `nome` e campos de texto livre. O log da aplicação costuma ficar fora da criptografia do banco e fora da política de retenção; quando recebe dado de paciente, cria uma cópia não governada do prontuário. Rastreadores de erro (Sentry, Rollbar) enviam variáveis locais no stack trace: configurar `before_send` com scrubbing, ou não usar em serviço com dado de paciente.

**Gatilhos.**
- `logging.info(request.json)`, `console.log(req.body)`, `print(response)` em rota que trafega dado de paciente
- logger que serializa o corpo da requisição ou o objeto de resposta do provedor
- `messages`, `prompt`, `completion` como campo de log
- header `Authorization` ou `api_key` em log
- Sentry, Rollbar ou equivalente sem `before_send` com scrubbing em serviço com dado de paciente
- stack trace com variáveis locais enviado a serviço externo
- log de aplicação sem prazo de retenção definido
- ausência de log de acesso a dado sensível
- log gravado em arquivo local sem cifragem, fora da política de backup e de retenção
- log de query de banco com parâmetros habilitado em produção

**Relacionados.** CP:art154 · LGPD:art46 · SEC:llm.vetores-clinicos

---

## SEC:anpd-guias.pequeno-porte

**Ementa.** Guia Orientativo de Segurança da Informação para Agentes de Tratamento de Pequeno Porte.

**Literal.**
> ANPD, "Guia Orientativo — Segurança da Informação para Agentes de Tratamento de Pequeno Porte", versão 1.0, outubro/2021. Verificado no PDF em 2026-08-11. Não há versão 2.0.
> https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-vf.pdf · página índice: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-sobre-seguranca-da-informacao-para-agentes-de-tratamento-de-pequeno-porte
> Recomendações extraídas, citações do texto: trânsito — "utilizar conexões cifradas (com uso de TLS/HTTPS) ou aplicativos com criptografia fim a fim" para comunicação e e-mail com dados pessoais. Repouso — pseudonimização para dados sensíveis, com criptografia citada como exemplo; para mídia externa, "cifrar os dados". MFA preferencialmente em sistemas com dados pessoais, por SMS, e-mail ou aplicativo autenticador. Menor privilégio: "o menor nível de acesso necessário". Controle de acesso em três componentes: autenticação, autorização e auditoria. Backup regular, completo, em local separado e não sincronizado online em tempo real, com justificativa explícita de propagação de ransomware. Antivírus não desabilitável pelo usuário. Patches: "manter todos os sistemas e aplicativos em suas últimas versões". Nuvem: contrato de SLA com garantias de segurança e MFA no acesso. Administrativas: política de segurança da informação, que pode ser simplificada, treinamento, NDA e cláusulas de segurança em contratos de TI.
> Limitação verificada por extração direta: o guia não fornece nenhum parâmetro numérico — nenhum tamanho de chave, nenhum comprimento mínimo de senha, nenhum prazo de retenção de log, nenhuma versão mínima de TLS.
> Na lista completa de "Materiais Educativos e Publicações" (https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes, verificada em 2026-08-11), o único guia de segurança é o de pequeno porte. Não existe guia orientativo de segurança para agentes de grande porte. Demais guias: encarregado (v2.0, 2022); legítimo interesse; tratamento para fins acadêmicos, estudos e pesquisas; Poder Público; cookies; contexto eleitoral. Há também o fascículo "Vazamento de Dados".

**Fonte.** https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-vf.pdf · https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes · verificado em 2026-08-11

**Confiança.** primária-conferida

**Severidade.** boa-prática

**Aplicação.** O guia é de nível gerencial e não é implementável sozinho. A defesa técnica do art. 46 exige parâmetros que ele não traz, importados de NIST, OWASP e IETF, que é o conteúdo dos demais itens desta ficha. Um documento de conformidade que cita apenas o guia da ANPD não demonstra adequação técnica.

**Gatilhos.**
- documento de conformidade que cita apenas o guia da ANPD, sem parâmetro técnico
- backup sincronizado em tempo real apresentado como backup
- ausência de MFA em sistema com dado de paciente
- ausência de política de segurança da informação, ainda que simplificada
- contrato de TI sem cláusula de segurança e sem NDA
- sistema ou biblioteca sem atualização, com versão fora de suporte
- mídia externa (pendrive, HD) com dado de paciente sem cifragem

**Relacionados.** LGPD:art46 · SEC:tls.versoes · SEC:repouso.algoritmo

---

## SEC:anpd-guias.incidente

**Ementa.** Comunicação de incidente de segurança, Resolução CD/ANPD nº 15/2024.

**Literal.**
> Resolução CD/ANPD nº 15, de 24/04/2024. Texto oficial no DOU: https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024. Canal oficial: https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis. Cópia oficial estadual consultada: https://www.lgpd.ms.gov.br/wp-content/uploads/2024/05/REGULAMENTO-DE-COMUNICACAO-DE-INCIDENTE-DE-SEGURANCA-ABRIL-2024-ANPD-.pdf. Verificados em 2026-08-11.
> Prazo: 3 dias úteis contados da ciência do incidente (arts. 6º e 9º, para ANPD e titulares). Complementação das informações: 20 dias úteis (art. 6º, §3º).
> Agente de pequeno porte — art. 6º, §8º, verbatim: "Os prazos constantes no caput e no § 3º deste artigo são contados em dobro para os agentes de pequeno porte, nos termos do disposto no Regulamento de aplicação da Lei nº 13.709 [...] aprovado pela Resolução CD/ANPD nº 2, de 27 de janeiro de 2022."
> Gatilho cumulativo: ocorrência confirmada; envolvimento de dados pessoais; e possibilidade de causar risco ou dano relevante.
> Risco relevante (art. 5º): afetar significativamente interesses e direitos fundamentais dos titulares e, cumulativamente, envolver ao menos um dos seis critérios — I, dados pessoais sensíveis; II, dados de crianças, de adolescentes ou de idosos; III, dados financeiros; IV, dados de autenticação em sistemas; V, dados protegidos por sigilo legal, judicial ou profissional; VI, dados em larga escala.
> Conteúdo da comunicação: art. 6º, §2º, com 12 elementos obrigatórios.
> Registro: art. 10 — manter registro de incidentes por no mínimo 5 anos, inclusive dos não comunicados.
> Exceção por criptografia: não existe. Verificado que o regulamento não contém cláusula de dispensa para dados criptografados ou anonimizados.
> Canal: SEI! ANPD, https://sei.anpd.gov.br/, com login gov.br disponível.

**Fonte.** https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024 · texto conferido palavra por palavra na cópia oficial https://www.lgpd.ms.gov.br/wp-content/uploads/2024/05/REGULAMENTO-DE-COMUNICACAO-DE-INCIDENTE-DE-SEGURANCA-ABRIL-2024-ANPD-.pdf · verificado em 2026-08-11

**Confiança.** primária-parcial

**Severidade.** bloqueante

**Aplicação.** Dado de saúde é sensível e satisfaz o inciso I do art. 5º. Na prática, incidente envolvendo prontuário atinge o gatilho de comunicação. O prazo é em dias úteis, não corridos. O registro interno dos incidentes que a instituição decidiu não comunicar é obrigatório por 5 anos.

Consultório, clínica pequena e médico pessoa física em regra são agentes de tratamento de pequeno porte pela Resolução CD/ANPD nº 2/2022. Nessa condição, o prazo do caput passa a 6 dias úteis e o prazo de complementação do §3º também é contado em dobro. O enquadramento como pequeno porte precisa estar registrado, porque é ele que sustenta o prazo maior. Na dúvida, comunicar em 3 dias úteis: o prazo curto é a decisão prudente e não gera prejuízo.

**Gatilhos.**
- ausência de registro interno de incidentes
- runbook de incidente que conta o prazo em dias corridos
- prazo em dobro aplicado sem registro do enquadramento como agente de pequeno porte
- política que dispensa comunicação por os dados estarem criptografados
- ausência de responsável e de canal definidos para a comunicação
- ausência de mecanismo para identificar titulares afetados e escopo do vazamento
- ausência de inventário de chaves, que impede delimitar o escopo

**Incerteza.** O GDPR prevê dispensa de comunicação ao titular quando os dados estão criptografados (art. 34(3)(a)). A Resolução 15/2024 não tem dispositivo equivalente. Não transportar a lógica europeia.

**Relacionados.** LGPD:art48 · SEC:repouso.chaves · SEC:anpd-guias.pequeno-porte

---

## SEC:anpd-guias.documentos

**Ementa.** Documentos técnicos orientativos da ANPD e prioridades de fiscalização.

**Literal.**
> Página de documentos técnicos orientativos: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos — verificada em 2026-08-11.
> Radar Tecnológico nº 3 — IA Generativa: PDF criado em 29/11/2024 e modificado em 23/01/2025. https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos/radar_tecnologico_ia_generativa_anpd.pdf — `NÃO VERIFICADO`: o conteúdo interno não foi extraído; o fetch retornou apenas metadados. Os riscos e recomendações específicos do documento não podem ser citados.
> Demais Radares Tecnológicos: nº 6 (deepfakes), nº 5 (verificação etária), nº 4 (neurotecnologias), nº 2 (biometria), nº 1 (cidades inteligentes).
> Notas técnicas: Nota Técnica 2026 sobre Grok e possíveis violações à LGPD; Nota Técnica 2024 sobre o plano de conformidade de IA generativa da Meta; Nota Técnica 2024 sobre tratamento de dados de terceiros para desenvolvimento de modelos de IA generativa.
> Mapa de Temas Prioritários 2026–2027, publicado em 24/12/2025: https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-publica-mapa-de-temas-prioritarios-para-o-bienio-2026-2027-e-atualiza-agenda-regulatoria-2025-2026. Quatro temas: direitos dos titulares; crianças e adolescentes; tratamento pelo Poder Público; inteligência artificial e tecnologias emergentes.

**Fonte.** https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos · https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-publica-mapa-de-temas-prioritarios-para-o-bienio-2026-2027-e-atualiza-agenda-regulatoria-2025-2026 · verificado em 2026-08-11

**Confiança.** primária-parcial

**Severidade.** boa-prática

**Aplicação.** Dados de saúde não figuram como tema prioritário nomeado para 2026–2027. Inteligência artificial figura. Aplicação clínica de LLM está no tema prioritário por ser IA, não por ser saúde.

**Gatilhos.**
- documento interno que cita o Radar Tecnológico nº 3 com conteúdo específico, sem leitura do PDF
- avaliação de risco de projeto de IA em saúde sem menção ao Mapa de Temas Prioritários vigente
- material que atribui à ANPD prioridade de fiscalização em saúde, com base em fonte secundária

**Incerteza.** Afirmações de blogs de que a ANPD concentrará fiscalização em saúde em 2026: `FONTE SECUNDÁRIA, NÃO CONFIRMADA em fonte primária`. `NÃO VERIFICADO`: conteúdo do Radar Tecnológico nº 3.

**Relacionados.** SEC:anpd-guias.pequeno-porte · SEC:llm.owasp-top10

---

## Itens não verificados nesta ficha

Marcações carregadas do levantamento bruto, estado em 2026-08-11, depois da reauditoria independente da mesma data. Cada entrada da ficha traz agora `Fonte.` e `Confiança.` no próprio bloco.

| Item | Estado |
|---|---|
| Conteúdo interno do ANPD Radar Tecnológico nº 3 (IA Generativa) | NÃO VERIFICADO |
| Publicação final do NIST IR 8547 | PARCIALMENTE VERIFICADO; a página do CSRC ainda traz apenas o Initial Public Draft de 12/11/2024, com comentários encerrados em 10/01/2025. Reconferido em 2026-08-11 |
| Texto integral dos papers de k-anonimato, t-proximidade e privacidade diferencial | NÃO LIDO; só os metadados foram conferidos no Crossref. A página da editora de Sweeney 2002 retorna HTTP 403 |
| Decisão do NIST sobre a SP 800-52 Rev. 2 | PENDENTE; consulta encerrada em 10/07/2026, comentários publicados em 30/07/2026, revisão na Fase 1 sem proposta de decisão |
| Cronograma de PQC com depreciação em 2030 e proibição em 2035 | NÃO VERIFICADO; não citar |
| NIST SP 800-131A (transições de algoritmos) | NÃO VERIFICADO |
| NIST SP 800-111 (storage encryption) | NÃO VERIFICADO |
| Datas e números de FIPS 203, 204 e 205 | NÃO VERIFICADO |
| Valores de ε e lista de "privacy hazards" do NIST SP 800-226 | NÃO VERIFICADO; apenas o abstract foi lido |
| Adoção final das EDPB Guidelines 01/2025 on Pseudonymisation | NÃO CONFIRMADA; permanecem como draft nas páginas consultadas |
| Conteúdo de Carlini et al., USENIX Security 2021 | Existência e venue verificados; conteúdo não fetchado |
| Custo do ataque e taxa de extração de PII em Nasr et al. (arXiv:2311.17035) | NÃO EXTRAÍDOS do abstract |
| Funcionalidade de gitleaks e TruffleHog | FONTE SECUNDÁRIA |
| Prioridade de fiscalização da ANPD em saúde para 2026 | FONTE SECUNDÁRIA, NÃO CONFIRMADA |
