---
tipo: esquema
versao: 1
atualizado: 2026-08-11
---

# Esquema das fichas do corpus

As fichas são a base de consulta das skills de auditoria. O formato existe para que a skill cite dispositivo, texto e fonte sem depender de memória, e para que interpretação nunca se misture com texto de lei.

## Regras de conteúdo

1. **Texto literal é intocável.** Transcrição exata do PDF ou do texto compilado oficial, sem corte que altere sentido. Supressão dentro de citação só com `[...]`.
2. **Interpretação vai em campo separado.** O campo `aplicação` é nosso, não da norma. Nunca misturar os dois no mesmo parágrafo.
3. **Toda ficha traz URL de fonte primária e data de verificação.** Sem os dois, a ficha não entra no corpus.
4. **Incerteza é declarada.** Ponto controverso ou não pacificado vai no campo `incerteza`, com as leituras concorrentes.
5. **Nada sem fonte.** Se não foi verificado, escrever `NÃO VERIFICADO` em vez de omitir.

## Identificador

Formato `NORMA:dispositivo`, estável e citável pela skill.

```
CFM-2454-2026:art6§3
CEM:art89
LGPD:art33
LGPD:art11.II.f
CP:art154
ANPD-19-2024:art16
```

## Campos por dispositivo

| Campo | Obrigatório | Conteúdo |
|---|---|---|
| `id` | sim | identificador estável |
| `ementa` | sim | do que trata, em uma linha |
| `literal` | sim | transcrição exata |
| `fonte` | sim | URL completa e data de verificação, no próprio bloco |
| `confiança` | sim | nível de verificação, ver abaixo |
| `severidade` | sim | `bloqueante`, `risco` ou `boa-prática` |
| `aplicação` | sim | o que significa para quem escreve código ou atende paciente |
| `gatilhos` | quando couber | padrões que devem acionar esta ficha em auditoria |
| `incerteza` | quando houver | leituras concorrentes, com as duas posições |
| `relacionados` | quando houver | ids de outros dispositivos |

O campo `fonte` fica no bloco, e não apenas no frontmatter. Uma skill que cita um dispositivo isolado precisa carregar a URL junto com o texto.

## Confiança

| Nível | Critério |
|---|---|
| `primária-conferida` | transcrição conferida palavra por palavra contra a fonte primária oficial, na data indicada |
| `primária-parcial` | fonte primária acessada, verificação incompleta. Exemplo: verbete de informativo lido, inteiro teor não lido |
| `secundária` | apenas fonte secundária disponível |
| `não-verificado` | não foi possível verificar |

A skill de auditoria só cita como norma o que está em `primária-conferida`. Os demais níveis podem informar, mas com a ressalva explícita.

## Campos por precedente judicial

Precedente não é dispositivo. Usa outro conjunto de campos.

| Campo | Obrigatório | Conteúdo |
|---|---|---|
| `id` | sim | `STJ:REsp2147374` |
| `ementa` | sim | do que trata, em uma linha |
| tabela de identificação | sim | processo, órgão, relator, julgamento, dados envolvidos |
| `tese` | sim | o que a decisão firmou |
| `verificação` | sim | fonte consultada, URL e data |
| `incerteza` | quando houver | o que o precedente não decidiu |

O campo `verificação` precisa distinguir inteiro teor de verbete de informativo. Precedente identificado só por verbete não sustenta citação de fundamentação.

## Severidade

| Nível | Critério |
|---|---|
| `bloqueante` | vedação expressa, tipo penal, ou requisito cuja falta caracteriza infração por si |
| `risco` | dever cujo descumprimento depende de circunstância, ou ponto de exposição relevante |
| `boa-prática` | recomendação técnica sem sanção direta |

A severidade é atribuída por nós, não pela norma. Vale como critério de triagem em auditoria.

## Gatilhos

Servem à skill de auditoria de código. São padrões observáveis, não conceitos.

```
gatilhos:
  - chamada a API de LLM com payload contendo campo de paciente
  - variável ou coluna: cpf, rg, prontuario, nome_paciente, data_nascimento
  - endpoint de provedor com região fora de BR ou UE
  - log ou print de payload de requisição
  - chave de API em código ou em .env versionado
```

## Arquivos

```
00-esquema.md                        este documento
00-indice.md                         lista de fichas e de dispositivos
01-cfm-2454-2026.md                  IA na medicina
02-cem-2217-2018.md                  Código de Ética Médica
03-cfm-1821-2007.md                  prontuário eletrônico e guarda
04-cfm-2314-2022.md                  telemedicina
05-lgpd-dados-sensiveis.md           arts. 5º, 7º, 11, 12, 13, 20
06-lgpd-transferencia.md             arts. 33 a 36 e resoluções da ANPD
07-lgpd-seguranca-incidente.md       arts. 37 a 49
08-lgpd-sancoes.md                   arts. 52 a 54
09-penal.md                          Código Penal
10-civil-consumo-mci.md              Código Civil, CDC, Marco Civil
11-seguranca-tecnica.md              criptografia, anonimização, OWASP
12-provedores-llm.md                 políticas de retenção e treinamento
```

## Manutenção

A ficha 12 tem meia-vida curta. Reverificar antes de qualquer publicação. As demais reverificar a cada seis meses ou quando houver alteração normativa.
