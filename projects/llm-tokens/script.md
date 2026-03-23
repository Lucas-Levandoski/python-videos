# Script: What Is a Token? (How AI Actually Reads Text)

**Formato:** YouTube Shorts — vertical 9:16, ≤ 90 segundos
**Idioma:** Português (Brasil)
**Palavras narradas:** ~173 palavras (~75s falados + ~15s visual-only)

---

## SEGMENTO 1 — HOOK (0:00–0:08)

[VISUAL: A frase "Inteligência artificial muda o mundo" aparece inteira na tela em texto branco.]

[VISUAL: A frase se fragmenta em caixas coloridas — cada token recebe uma cor diferente:]
`Int` | `el` | `ig` | `ência` | ` artificial` | ` muda` | ` o` | ` mundo`

**NARRADOR:**
> Você acha que a IA lê texto igual a você?
> Olha de novo.

---

## SEGMENTO 2 — DEFINIÇÃO DE TOKEN (0:08–0:23)

[VISUAL: FadeOut dos tokens. Texto centralizado aparece com Write():]
`"Token = menor unidade que a IA processa"`
[VISUAL: Caixa amarela com cantos arredondados envolve a definição.]

**NARRADOR:**
> Cada um desses pedaços se chama **token**.
> Não é uma palavra. Não é uma letra.
> É a menor unidade que a inteligência artificial consegue processar.

*(~3 segundos visual-only: a caixa amarela pulsa)*

---

## SEGMENTO 3 — TOKEN ≠ PALAVRA (0:23–0:43)

[VISUAL: Título fixo no topo: "Token ≠ Palavra" em AMARELO]

**NARRADOR:**
> Veja a diferença. E preste atenção: cada token é, na verdade, um número.

---

**Flash-card 1:**

[VISUAL: Palavra "gato" aparece → seta para baixo → caixa dupla:]
- Linha superior: caixa AZUL com texto `"gato"`
- Linha inferior: caixa CINZA com `ID: 85316`
[VISUAL: Label verde abaixo: "1 token = 1 número"]

**NARRADOR:**
> "Gato" — um token. Para a IA, esse token é o número 85316.

---

**Flash-card 2:**

[VISUAL: FadeOut do anterior. Palavra "inacreditável" aparece → seta → 3 pares de caixas:]
- `"in"` / `ID: 258` | `"acredit"` / `ID: 36735` | `"ável"` / `ID: 26193`
[VISUAL: Label verde: "3 tokens = 3 números"]

**NARRADOR:**
> "Inacreditável" — três tokens. Três números diferentes.

---

**Flash-card 3:**

[VISUAL: FadeOut. "Olá, mundo!" aparece → seta → destaque na vírgula:]
- `","` / `ID: 11` em destaque AMARELO
[VISUAL: Label: "pontuação = número próprio"]

**NARRADOR:**
> Até a vírgula tem o seu próprio número no vocabulário da IA.

---

## SEGMENTO 4 — MECANISMO GENERATIVO (0:43–1:18)

[VISUAL: Transição para layout do mecanismo]

**NARRADOR:**
> Mas como a IA gera o próximo token?

---

**Passo 1 — Tokens (como números) entram na rede:**

[VISUAL: 4 caixas de token com dois níveis: texto acima (`"Int"`, `"el"`, `"ig"`, `"ência"`) e ID abaixo (`258`, `301`, `328`, `9808`)]
[VISUAL: Setas fluem para um diagrama de rede neural estilizado no centro — nós acendem em sequência]

**NARRADOR:**
> A rede não recebe letras. Ela recebe números — os IDs de cada token.

---

**Passo 2 — Saída: uma lista de IDs com probabilidades:**

[VISUAL: À direita/abaixo da rede, lista vertical de candidatos — cada linha mostra ID + texto + barra:]
```
ID 9578  ▁artificial   ████████ 42%
ID 1079  ▁incrível     ███░░░░░ 18%
ID 2724  ▁muda         ██░░░░░░ 11%
ID  374  ▁é            █░░░░░░░  7%
...
```
[VISUAL: Linha do topo (ID 9578) destacada com borda AMARELA]
[VISUAL: Label acima da lista: "saída da IA = número"]

**NARRADOR:**
> A rede calcula qual número vem a seguir. O output é um número — não uma palavra.

---

**Passo 3 — Número vencedor é decodificado para texto:**

[VISUAL: O `ID 9578` em destaque AMARELO se transforma visualmente → `" artificial"` (texto aparecem sobre o número)]
[VISUAL: Seta com label: `"vocabulário: 9578 → artificial"`]

**NARRADOR:**
> Esse número é consultado no vocabulário. Aí sim vira texto.

---

**Passo 4 — Texto decodificado entra na sequência, ciclo se repete:**

[VISUAL: O token `" artificial"` voa e se junta à sequência de entrada]
[VISUAL: Nova sequência agora tem 5 tokens. O ciclo roda mais 2 vezes em fast-forward]
[VISUAL: A frase vai se construindo token por token]

**NARRADOR:**
> E o ciclo se repete — número, decodifica, próximo número.

*(~3 segundos visual-only: ciclos em fast-forward)*

---

## SEGMENTO 5 — FECHAMENTO (1:18–1:30)

[VISUAL: FadeOut de tudo. Tela preta. Três linhas de texto aparecem em sequência centralizada:]

```
A IA não escreve frases.
Ela prevê um pedacinho
de cada vez.           ← esta linha em AMARELO
```

[VISUAL: Pausa de 3 segundos. FadeOut para preto total.]

**NARRADOR:**
> *(silêncio — o texto fala por si)*

---

## Notas de Produção

- **Verbos aprovados:** calcular, prever, processar, escolher, gerar
- **Verbos proibidos:** pensar, entender, saber, querer, sentir
- **Splits verificados:** cl100k_base — `inacreditável` → `in` + `acredit` + `ável`; `Olá,` → `Ol` + `á` + `,`
- **Fonte mínima:** 28pt corpo, 36pt mantra final
- **Fundo:** PRETO em toda a cena
