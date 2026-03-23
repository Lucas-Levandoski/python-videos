# Como LLMs Ficaram 1000x Mais Baratos

**Conceito:** A jornada completa de como modelos de linguagem passaram de proibitivamente caros para quase gratuitos -- e por que isso muda tudo.
**Público-alvo:** Entusiastas de tecnologia, desenvolvedores e profissionais curiosos sobre IA (25-40 anos) que usam LLMs mas não entendem o que acontece por trás.
**Duração estimada:** ~13 minutos (~1950 palavras a ~150 palavras/minuto)
**Tom:** Entusiasta mas substancial -- como um amigo inteligente explicando algo fascinante.

---

## ATO 1 -- O PROBLEMA

---

### Segmento 0 — Hook (0:00 - 0:30)

[MUSICA: eletronica tensa, pulso rapido, energia alta desde o primeiro segundo]

[VISUAL: Contador de preco animado caindo rapidamente -- $60.00 por milhao de tokens despencando ate $0.07]

Em 2020, *uma unica chamada* ao GPT-3 custava mais que a sua assinatura mensal da Netflix. Sessenta dolares por milhao de tokens. Pra resumir um livro, voce gastava cinco dolares. Pra rodar um chatbot de atendimento, *dois mil e quatrocentos dolares por mes*.

[PAUSE]

Hoje? Um modelo *dez vezes mais capaz* custa... sete centavos pelo mesmo milhao de tokens.

[SFX: impacto unico -- "tum"]

Isso e uma queda de *mil vezes*.

[PAUSE]

[VISUAL: Contador duplo aparecendo -- lado esquerdo: "Preco por token" caindo 1000x (verde). Lado direito: "Tokens consumidos por dia" subindo de milhoes para trilhoes (amarelo, acelerando). Os dois contadores correndo simultaneamente em direcoes opostas]

Mas aqui vai o que e *realmente* insano. Ao mesmo tempo que o preco caiu mil vezes... a quantidade de tokens que a gente consome *explodiu*. Em 2020, uma chamada ao GPT-3 usava algumas centenas de tokens. Hoje, voce abre o Cursor, o Copilot, qualquer agente de IA -- e *sem perceber*, uma unica sessao de trabalho queima *milhares, dezenas de milhares* de tokens. Aplicacoes inteiras rodam centenas de chamadas em cadeia por baixo dos panos.

[SFX: impacto unico -- "tum"]

[VISUAL: Comparativo animado -- icone de pessoa em 2020 com um balao pequeno "~500 tokens/dia" vs icone de pessoa em 2025 rodeada de agentes, copilots, apps, com balao gigante "~500.000+ tokens/dia" pulsando. Multiplicador "1000x mais tokens" aparece em amarelo]

A gente ta gastando *mil vezes mais tokens* do que gastava... e *nem percebe*. Porque ficou tao barato que virou invisivel. E como eletricidade -- voce usa o tempo todo e so lembra que existe quando chega a conta.

[SFX: impacto grave -- "tum tum tum"]

[PAUSE]

E nao -- nao foi so porque os computadores ficaram mais rapidos. A historia real e *muito* mais interessante. Sao pelo menos sete inovacoes diferentes que, juntas, fizeram a tecnologia mais poderosa da historia ficar quase de graca.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: contador de preco congela no $0.07 → fade to black]

---

### Segmento 1 — O Que Sao Parametros? (0:30 - 2:00)

[MUSICA: trocar para mood explicativo, suave, curiosa -- synth leve com pads]

[FACE CAM]

Mas antes da gente entender *como* ficou mais barato, a gente precisa entender *por que* era tao caro. E pra isso, eu preciso te explicar uma coisa fundamental: o que sao parametros.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → animacao de rede neural surgindo da direita]

[VISUAL: Rede neural animada com conexoes brilhantes. Zoom progressivo ate um unico peso mostrando o numero 0.00342 em ponto flutuante]

Imagina uma mesa de som gigante. Sabe aquelas mesas de estudio com centenas de botoes e deslizadores? Cada deslizador controla *quanto* o modelo presta atencao em um padrao especifico. O tom de uma frase. A relacao entre duas palavras. A probabilidade de uma resposta fazer sentido.

[PAUSE]

O GPT-3 tem *cento e setenta e cinco bilhoes* desses deslizadores.

[SFX: impacto unico -- "tum"]

[VISUAL: Numero "175.000.000.000" aparece grande na tela, cada digito acendendo em sequencia]

Cada um desses deslizadores e um numero. Um valor decimal -- tipo 0.00342 -- que o modelo *aprendeu* durante o treinamento. E aqui tem um detalhe importante que muita gente confunde: parametros *nao sao* fatos armazenados como num banco de dados. Sao padroes estatisticos aprendidos. O modelo nao "sabe" que Paris e a capital da Franca da mesma forma que a Wikipedia sabe. Ele aprendeu padroes que fazem ele *gerar* essa resposta.

[VISUAL: Slider sendo ajustado -- mostra como mudar o valor de um parametro altera a saida do modelo]

E a logica e simples: *mais parametros*, mais capacidade de capturar padroes complexos, geralmente *mais qualidade*. Mas tambem... *mais computacao necessaria*. E mais computacao significa *mais custo*.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: rede neural faz zoom out, divide a tela ao meio]

---

### Segmento 2 — Treinamento vs. Inferencia: A Analogia da Fabrica (2:00 - 3:15)

[MUSICA: manter mood explicativo, adicionar leve beat]

[FACE CAM]

Beleza. Agora que voce sabe o que sao parametros, eu preciso te mostrar uma distincao que *muda completamente* como a gente pensa sobre custo de IA. Treinamento versus inferencia.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → split screen animado, fabrica de um lado, linha de producao do outro]

[VISUAL: Tela dividida -- esquerda mostra cluster massivo de GPUs com icone de relogio (meses), direita mostra uma unica chamada de API com icone de relogio (milissegundos)]

Pensa assim. O *treinamento* e como projetar e construir uma fabrica de carros. Voce gasta bilhoes, leva meses, mas faz isso *uma vez*.

A *inferencia* e como produzir cada carro na fabrica. Cada vez que alguem faz uma pergunta ao ChatGPT, isso e uma rodada de inferencia. E isso acontece *milhoes de vezes por dia*.

[PAUSE]

[VISUAL: Numeros aparecendo em destaque -- "$4.6 milhoes" no lado do treinamento, "$100 milhoes+" abaixo para o GPT-4]

O treinamento do GPT-3 custou cerca de quatro milhoes e seiscentos mil dolares. O do GPT-4? Mais de cem milhoes. Parece muito, ne?

Mas aqui vai o ponto que surpreende todo mundo: ao longo da vida util de um modelo, o custo de *inferencia* supera o treinamento de longe. Porque o treinamento voce faz uma vez. A inferencia, voce faz *bilhoes* de vezes.

[SFX: impacto unico -- "tum"]

[VISUAL: Balanca animada -- lado "Treinamento" sobe, lado "Inferencia" desce com peso muito maior]

E por isso que a maioria das otimizacoes que tornaram LLMs baratos focam em *inferencia*. E sobre elas que a gente vai falar.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: balanca desaparece → fade to black]

---

### Segmento 3 — O Problema do Preco (3:15 - 4:15)

[MUSICA: trocar para mood tenso, urgente -- beat mais rapido, notas menores]

[FACE CAM]

Agora, pra voce sentir na pele o quanto era caro... deixa eu te mostrar uns numeros *reais* de uso do GPT-3 nos precos originais.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → animacao de calculadora entrando pela esquerda]

[VISUAL: Calculadora animada somando custos em tempo real, numeros vermelhos]

Resumir *um* livro? Cinco dolares. Tudo bem, parece razoavel.

Mas um chatbot de atendimento ao cliente processando mil conversas por dia? *Dois mil e quatrocentos dolares por mes*.

[SFX: impacto unico -- "tum"]

Um assistente de codigo pra uma empresa com cem devs? *Quinze mil dolares. Por mes.*

[SFX: impacto unico -- "tum"]

[VISUAL: Numeros empilhando na tela -- $5, $2.400/mes, $15.000/mes -- cada um pulsando em vermelho]

Nesses precos, adocao em massa era *economicamente impossivel*. So as maiores empresas do mundo podiam bancar isso. O resto? Ficava assistindo de fora.

[PAUSE]

[MUSICA: build tension]

Alguma coisa precisava mudar.

[PAUSE]

E mudou. De pelo menos *sete direcoes diferentes*, ao mesmo tempo.

[SFX: impacto grave -- "tum tum tum"]
[MUSICA: drop]
[TRANSICAO VISUAL: numeros vermelhos explodem em particulas → tela limpa com titulo "AS OTIMIZACOES" surgindo em verde]

---

## ATO 2 -- AS OTIMIZACOES

---

### CLUSTER 1 -- TORNAR O MODELO MENOR

---

### Segmento 4 — Quantization (4:15 - 5:55)

[MUSICA: trocar para mood tecnico-empolgante -- synth progressivo, exploratorio]

[FACE CAM]

A primeira grande otimizacao e talvez a mais elegante. Quantization. E a ideia e surpreendentemente simples: e se a gente pudesse fazer cada parametro ocupar *menos espaco* na memoria?

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → zoom em um unico parametro brilhante da rede neural]

[VISUAL: Um parametro mostrado como numero FP32 -- "0.0034271845" com 32 blocos representando bits]

Lembra dos cento e setenta e cinco bilhoes de parametros? Cada um deles, no formato original, usa *trinta e dois bits* de precisao. Trinta e dois bits pra guardar um unico numero. Isso se chama FP32, ou ponto flutuante de 32 bits.

[VISUAL: Analogia visual -- imagem RAW de alta resolucao, nitida, pesada]

E como tirar uma foto em RAW. Qualidade maxima, cada detalhe preservado. Mas o arquivo e *enorme*.

[PAUSE]

Agora, o que acontece se a gente *reduzir* essa precisao?

[VISUAL: Progressao animada -- FP32 (32 blocos) → FP16 (16 blocos) → INT8 (8 blocos) → INT4 (4 blocos), com barras de tamanho diminuindo. Ao lado, exemplos de saida do modelo mostrando respostas quase identicas]

De FP32 pra FP16 -- metade dos bits. O numero fica menos preciso, mas a resposta do modelo? *Praticamente identica*.

De FP16 pra INT8 -- metade de novo. Ainda funciona surpreendentemente bem.

E agora o salto radical: INT4. *Quatro bits* por parametro. Um oitavo do original.

[SFX: impacto unico -- "tum"]

[VISUAL: Comparacao lado a lado -- resposta do modelo em FP32 vs INT4 -- textos quase identicos, com um highlight sutil nas diferencas minimas]

E aqui vem o numero que impressiona: a perda de qualidade de FP32 pra INT4 e de apenas *um a tres por cento* nos benchmarks. Quase imperceptivel.

Mas o ganho? *Oito vezes* menos memoria. *Quatro vezes* mais rapido na inferencia.

[VISUAL: Comparacao dramatica -- "Modelo 70B em FP32 = 280 GB de RAM" (vermelho, gigante) transformando em "Modelo 70B em INT4 = 35 GB de RAM" (verde, cabendo numa unica GPU)]

Pra colocar em perspectiva: um modelo de setenta bilhoes de parametros em FP32 precisa de duzentos e oitenta gigabytes de RAM. E impossivel rodar isso em qualquer hardware normal. Mas em INT4? *Trinta e cinco gigas*. Cabe numa unica GPU de consumidor.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: GPU brilha em verde → fade para diagrama professor-aluno]

---

### Segmento 5 — Distillation (5:55 - 7:05)

[MUSICA: trocar para mood leve, narrativo -- quase como uma historia sendo contada]

[FACE CAM]

A segunda tecnica e tipo um hack educacional. Ao inves de reduzir a precisao de um modelo grande, a gente cria um modelo *menor* que aprende com o grande. Isso se chama distillation, ou destilacao.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → animacao de chef grande ensinando chef pequeno]

[VISUAL: Diagrama animado -- modelo grande (professor/teacher) no topo gerando respostas, modelo pequeno (aluno/student) embaixo aprendendo a replicar essas respostas. O aluno vai ficando progressivamente melhor, com barra de progresso]

Imagina um chef estrelado -- tipo o GPT-4. Ele sabe preparar *qualquer* prato com perfeicao. Agora imagina que ele treina um aprendiz. O aprendiz nao vai aprender *tudo* que o mestre sabe. Mas pra noventa por cento dos pratos que os clientes pedem? Ele entrega *tao bem quanto*. E trabalha *dez vezes mais rapido*.

[PAUSE]

E o pulo do gato e este: o aluno *nao precisa* ser treinado do zero com dados brutos. Ele aprende com as *respostas do professor*. E as respostas de um modelo treinado sao um sinal de treinamento *muito mais rico* do que dados crus. E como ter um tutor particular ao inves de aprender sozinho por livro.

[VISUAL: Logos aparecendo em sequencia -- GPT-4o-mini, Claude Haiku, Gemini Flash -- com setas ligando a seus modelos maiores]

Na pratica, e assim que nasceram modelos como o GPT-4o-mini, o Claude Haiku, o Gemini Flash. Variantes menores, otimizadas, que entregam qualidade impressionante por uma *fracao* do custo.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: logos dos modelos fazem zoom out → novo diagrama com roteador aparece]

---

### CLUSTER 2 -- TORNAR O MODELO MAIS INTELIGENTE NO TRABALHO

---

### Segmento 6 — Mixture of Experts (7:05 - 8:35)

[MUSICA: trocar para mood de revelacao -- build lento, synth crescente]

[FACE CAM]

Agora a gente entra no territorio que, na minha opiniao, e a inovacao *mais genial* dessa lista toda. Mixture of Experts. Ou simplesmente MoE. E a ideia e tao elegante que quase parece obvia depois que voce entende.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → diagrama de hospital com triagem]

[VISUAL: Analogia do hospital -- paciente chega → passa pela triagem → e encaminhado para o especialista correto, nao para todos os medicos]

Pensa num hospital. Quando voce chega, voce *nao* passa por *todos* os medicos. Tem uma triagem que avalia o que voce precisa e te encaminha pro especialista certo. Cardiologista, ortopedista, dermatologista. Cada um e expert na sua area.

[PAUSE]

[VISUAL: Comparacao animada lado a lado:
1. Modelo tradicional: token entra → TODOS os 175B parametros ativam (tudo vermelho, lento)
2. Modelo MoE: token entra → rede roteadora seleciona 2 de 8 experts → so esses ativam (verde, rapido)]

Num modelo *tradicional*, cada token que voce manda ativa *todos* os cento e setenta e cinco bilhoes de parametros. Cada. Um. Deles. Nao importa se a pergunta e sobre culinaria ou astrofisica.

[SFX: impacto unico -- "tum"]

Num modelo MoE, existe uma rede *roteadora* que olha cada token e decide: "esse token precisa dos experts dois e cinco". E *so* esses experts sao ativados. O resto fica em repouso.

[MUSICA: drop]

[VISUAL: Diagrama do Mixtral 8x7B -- 8 blocos de experts, destaque mostrando "47B parametros totais" mas "apenas 13B ativos por token", com setas do roteador]

O caso mais famoso: Mixtral 8x7B. O modelo tem quarenta e sete bilhoes de parametros no *total*. Mas pra cada token, so *treze bilhoes* estao ativos. Voce tem a *capacidade de conhecimento* de um modelo gigante, com o *custo computacional* de um modelo pequeno.

[VISUAL: Logos -- Mixtral 8x7B, GPT-4 (com "?" e "rumores de MoE"), DeepSeek-V2]

E nao e so o Mixtral. Existem fortes indicios de que o GPT-4 usa MoE. O DeepSeek-V2 tambem. Essa arquitetura virou *padrao* nos modelos mais eficientes do mercado.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: diagrama MoE gira e transforma em esteira de producao]

---

### Segmento 7 — Flash Attention e KV Cache (8:35 - 9:55)

[MUSICA: trocar para mood tecnico focado -- beat preciso, minimalista]

[FACE CAM]

Beleza. As ultimas duas otimizacoes eram sobre *o que* o modelo calcula. Agora a gente vai falar sobre *como* ele calcula. E especificamente sobre a operacao mais cara dentro de um transformer: o mecanismo de *atencao*.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → animacao de esteira industrial]

[VISUAL: Analogia da esteira -- metodo antigo: carregar TUDO numa mesa gigante, processar → mesa transborda. Metodo novo (Flash Attention): processar em pequenos lotes numa bancada rapida, sem acumular]

Flash Attention. O nome ja sugere: atencao *rapida*. E a ideia e sobre *onde* os dados ficam durante o calculo.

O metodo padrao de atencao computa tudo, armazena tudo na memoria principal da GPU -- que e grande mas *lenta* -- e depois processa. O gargalo nao e a computacao em si. E a *memoria*.

[PAUSE]

Flash Attention resolve isso processando os dados em *blocos*, mantendo tudo na SRAM da GPU -- a memoria *rapida*, que fica direto no chip. Resultado? *Duas a quatro vezes* mais rapido.

[SFX: impacto unico -- "tum"]

[VISUAL: Animacao token-by-token -- modelo gerando texto. Sem cache: recalcula atencao pra TODOS os tokens anteriores a cada novo token (setas vermelhas, redundantes). Com KV Cache: tokens anteriores ja cacheados (setas verdes, eficientes)]

E tem mais. KV Cache -- cache de chave e valor. Quando o modelo gera texto token por token, o metodo ingenuo recalcula a atencao pra *todos* os tokens anteriores. Cada vez. Do zero.

Com KV Cache, voce guarda as matrizes de chave e valor dos tokens ja processados. Por que recalcular o que voce *ja sabe*?

[VISUAL: Tecnicas modernas aparecendo -- Multi-Query Attention (MQA), Grouped-Query Attention (GQA) -- compartilhando cabecas de atencao para reduzir tamanho do cache]

E tecnicas mais recentes como Multi-Query Attention e Grouped-Query Attention vao alem -- compartilham partes do cache entre cabecas de atencao, reduzindo ainda mais o uso de memoria.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: animacao do cache faz zoom out → fade to black → novo titulo "CLUSTER 3" aparece]

---

### CLUSTER 3 -- TORNAR O ECOSSISTEMA MAIS BARATO

---

### Segmento 8 — Chinchilla Scaling Laws e Dados Melhores (9:55 - 10:45)

[MUSICA: trocar para mood de descoberta -- piano sutil com strings crescentes]

[FACE CAM]

Ate agora a gente falou de otimizacoes no modelo e no hardware. Mas em 2022 veio uma descoberta que sacudiu a industria inteira. Uma equipe da DeepMind publicou o paper Chinchilla e provou que todo mundo tava treinando modelos *do jeito errado*.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → grafico animado da fronteira otima de Chinchilla]

[VISUAL: Grafico com eixo X = parametros, eixo Y = tokens de treinamento. Linha da fronteira otima de Chinchilla. GPT-3 plotado MUITO acima da linha (muitos parametros, poucos dados). LLaMA plotado na linha otima]

A logica era: quer um modelo melhor? Coloca *mais parametros*. O GPT-3 tinha cento e setenta e cinco bilhoes de parametros mas foi treinado com "apenas" trezentos bilhoes de tokens.

[PAUSE]

Chinchilla mostrou que existia um *equilibrio otimo* entre tamanho do modelo e quantidade de dados. E que a industria tava gastando computacao demais com parametros e de menos com dados.

[SFX: impacto unico -- "tum"]

Resultado? O LLaMA da Meta, com "apenas" sessenta e cinco bilhoes de parametros treinados com *um trilhao e quatrocentos bilhoes* de tokens, *superou* o GPT-3 de cento e setenta e cinco bilhoes.

[VISUAL: Comparacao -- GPT-3 (175B params, 300B tokens, vermelho) vs LLaMA (65B params, 1.4T tokens, verde, com medalha de ouro)]

*Qualidade dos dados importa mais que quantidade de parametros.* Essa unica descoberta redirecionou bilhoes de dolares em investimento de pesquisa.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: grafico Chinchilla faz morph para timeline de GPUs]

---

### Segmento 9 — Evolucao do Hardware (10:45 - 11:30)

[MUSICA: trocar para mood de progresso tecnologico -- beat constante, futurista]

[FACE CAM]

E claro, nao da pra contar essa historia sem falar de hardware. As GPUs *ficaram* muito melhores. Mas tem um detalhe importante aqui.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → timeline horizontal animada de GPUs]

[VISUAL: Timeline animada -- A100 (2020) → H100 (2022, "3x mais rapida pra IA") → B200 (2024, "2.5x mais rapida que H100"). Cada GPU brilha ao aparecer]

A NVIDIA A100, de 2020. Depois a H100, em 2022, *tres vezes* mais rapida pra cargas de IA. E agora a B200, *duas vezes e meia* mais rapida que a H100.

[PAUSE]

Impressionante? Com certeza. Mas aqui vai o ponto critico.

[MUSICA: build tension]

Se a gente *so tivesse* melhorias de hardware, sem nenhuma das otimizacoes algoritmicas que eu acabei de explicar, o custo do GPT-3 teria caido de quatro milhoes e seiscentos mil pra... mais ou menos um milhao. Ainda caro. Ainda inacessivel.

[SFX: impacto unico -- "tum"]

[VISUAL: Barra de progresso mostrando "Hardware: 4-5x de melhoria" vs "Total: 1000x de melhoria" -- hardware e uma fatia pequena do total]

Hardware explica *quatro a cinco vezes* de melhoria. Das *mil vezes* de reducao total. O trabalho pesado foi feito pelas inovacoes *algoritmicas*.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: barra de progresso dissolve → diagrama de especulative decoding]

---

### Segmento 10 — Speculative Decoding e Infraestrutura (11:30 - 12:10)

[MUSICA: trocar para mood rapido, energetico -- beat acelerado]

[FACE CAM]

E pra fechar as otimizacoes, mais duas tecnicas de infraestrutura que fazem uma diferenca enorme no dia a dia.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → animacao de dois modelos, um pequeno e rapido, um grande e lento]

[VISUAL: Modelo pequeno (rapido, azul) gerando 5 tokens de rascunho em sequencia rapida → modelo grande (verde) verificando todos os 5 de uma vez → aceita 4, rejeita 1 → resultado final aparece]

Speculative decoding. A ideia e brilhante: voce usa um modelo *pequeno e rapido* pra gerar varios tokens de rascunho. Depois, o modelo grande confere todos eles *de uma vez* -- em paralelo. Na maioria das vezes, o modelo pequeno acerta. E o resultado? Aceleracao de *tres a quatro vezes*.

[SFX: impacto unico -- "tum"]

[VISUAL: Tres tecnicas aparecendo em sequencia rapida com icones -- Batching (multiplas requisicoes em paralelo), Model Parallelism (modelo dividido entre GPUs), Continuous Batching (fila dinamica)]

E tem mais no nivel de infraestrutura. *Batching* -- processar multiplas requisicoes ao mesmo tempo. *Model parallelism* -- dividir o modelo entre varias GPUs. *Continuous batching* -- gerenciar uma fila dinamica de requisicoes pra manter as GPUs sempre ocupadas.

Cada uma dessas tecnicas sozinha da um ganho modesto. Mas *todas juntas*? O efeito e multiplicativo.

[SFX: impacto grave -- "tum tum tum"]
[MUSICA: drop -- silencio dramatico por 1 segundo]
[TRANSICAO VISUAL: tudo desaparece → fade to black lento → titulo "O RESULTADO" aparece em dourado]

---

## ATO 3 -- O RESULTADO

---

### Segmento 11 — A Linha do Tempo dos Precos (12:10 - 13:40)

[MUSICA: trocar para mood epico-crescente -- orquestra sintetica, sensacao de grandiosidade]

[FACE CAM]

Agora que voce entende *como* cada peca funciona, deixa eu te mostrar o resultado. A linha do tempo completa do colapso de precos. E *de arrepiar*.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → timeline dupla animada surgindo do centro]

[VISUAL: Timeline animada com duas trilhas -- trilha de cima mostra modelos proprietarios, trilha de baixo mostra modelos open-source como "eventos de disrupcao". Cada entrada aparece com animacao e o preco pulsa antes de fixar]

Junho de 2020. GPT-3. *Sessenta dolares* por milhao de tokens de entrada.

[SFX: impacto unico -- "tum"]

Marco de 2023. GPT-3.5-turbo chega. Dois dolares. Trinta vezes mais barato. Destilacao e otimizacao pura.

[VISUAL: Na trilha open-source, LLaMA aparece como explosao]

Fevereiro de 2024. LLaMA 2 self-hosted. Vinte centavos. Open-source entrando no jogo e *forcando* os precos pra baixo.

Janeiro de 2024. Mixtral 8x7B. Vinte e cinco centavos. Mixture of Experts em acao.

[SFX: impacto unico -- "tum"]

Maio de 2024. GPT-4o. Cinco dolares -- mas *muito* mais capaz que o GPT-4 original que custava trinta.

Julho de 2024. GPT-4o-mini. *Quinze centavos*. Destilacao levada ao limite.

[MUSICA: build tension]

[VISUAL: DeepSeek-V3 aparece com efeito de impacto, numero "$0.07" brilha em verde neon]

Janeiro de 2025. DeepSeek-V3. Sete centavos. MoE, quantization, open-source -- *tudo* combinado num unico modelo.

[SFX: impacto grave -- "tum tum tum"]
[MUSICA: drop]

[VISUAL: Zoom out mostrando a timeline completa -- a queda de $60 para $0.07 e visualmente dramatica, quase vertical]

De sessenta dolares pra sete centavos. *Quase mil vezes*. Em menos de cinco anos.

[PAUSE]

E repara num padrao: cada vez que um modelo open-source era lancado... os precos dos modelos proprietarios *despencavam* logo em seguida. A competicao do open-source nao foi so tecnica. Foi *economica*.

[SFX: impacto grave -- "tum tum tum"]
[TRANSICAO VISUAL: timeline colapsa num ponto → duas curvas crescem a partir dele]

---

### Segmento 12 — Por Que Mais Barato E Tambem Melhor (13:40 - 14:40)

[MUSICA: trocar para mood inspiracional-reflexivo -- piano com pads eterea, sensacao de conclusao grandiosa]

[FACE CAM]

E aqui a gente chega na parte mais contraintuitiva de toda essa historia. Porque normalmente, quando algo fica mais barato, fica *pior*, ne? Produto generico, versao econamica, qualidade inferior. Mas com LLMs aconteceu o *oposto*.

[SFX: whoosh transicao]
[TRANSICAO VISUAL: face cam → grafico com duas curvas]

[VISUAL: Grafico animado com duas curvas no mesmo eixo temporal -- curva de custo caindo exponencialmente (vermelho → verde), curva de capacidade/benchmarks subindo (azul). As curvas se cruzam, criando uma regiao destacada: "A Era Dourada"]

Os modelos ficaram mil vezes mais baratos *e significativamente mais capazes* ao mesmo tempo.

[PAUSE]

E isso nao e coincidencia. E um *ciclo virtuoso*.

[VISUAL: Diagrama circular animado -- "Computacao mais barata" → "Treinar modelos maiores com o mesmo orcamento" → "Modelos melhores" → "Otimizar ainda mais" → "Computacao mais barata" -- ciclo girando]

Cada otimizacao nao so reduziu custo -- ela *liberou orcamento* pra treinar modelos *maiores* e *melhores*. Computacao mais barata permite treinar mais. Treinar mais gera modelos melhores. Modelos melhores podem ser otimizados ainda mais. E o ciclo se repete.

[SFX: impacto unico -- "tum"]

[MUSICA: build para o momento final]

Quantization. Destilacao. Mixture of Experts. Flash Attention. KV Cache. Chinchilla scaling laws. Hardware melhor. Speculative decoding. Open-source. *Cada uma* contribuiu. Mas o verdadeiro poder foi a *combinacao multiplicativa* de todas elas.

[PAUSE]

[MUSICA: drop suave -- emocional, nao dramatico]

[VISUAL: Texto aparecendo letra por letra, elegante: "A tecnologia mais poderosa da historia esta ficando tao barata quanto eletricidade."]

A tecnologia mais poderosa da historia esta ficando tao barata quanto eletricidade. A pergunta nao e mais *se* IA vai ser acessivel.

A pergunta e: *o que voce vai construir quando ela custar quase nada?*

[SFX: impacto grave -- "tum tum tum"]

[PAUSE -- 2 segundos de silencio]

---

### Call to Action (14:40 - 15:00)

[MUSICA: suave, final -- diminuindo gradualmente]

[FACE CAM]

Se esse video te ajudou a entender como a IA ficou mil vezes mais barata, deixa o like. Serio -- isso ajuda *demais* o canal.

E se voce quer entender o *proximo* passo -- como essas otimizacoes vao evoluir e o que vem por ai -- se inscreve e ativa o sino. Eu to preparando conteudo sobre isso.

[PAUSE]

Comenta ai embaixo: qual dessas otimizacoes te surpreendeu mais? Quantization, MoE, ou o impacto do open-source?

Valeu. Nos vemos no proximo.

[VISUAL: Tela final com logo do canal, botao de inscrever-se, e sugestao de video relacionado]
[MUSICA: fade out]
