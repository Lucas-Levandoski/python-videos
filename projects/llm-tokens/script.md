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
> Veja a diferença.

---

**Flash-card 1:**

[VISUAL: Palavra "gato" aparece → seta para baixo → 1 caixa azul com "gato"]
[VISUAL: Label verde abaixo: "1 token"]

**NARRADOR:**
> "Gato" — um token só.

---

**Flash-card 2:**

[VISUAL: FadeOut do anterior. Palavra "inacreditável" aparece → seta → 3 caixas: "in" | "acredit" | "ável"]
[VISUAL: Label verde: "3 tokens"]

**NARRADOR:**
> "Inacreditável" — três tokens.

---

**Flash-card 3:**

[VISUAL: FadeOut. "Olá, mundo!" aparece → seta → 5 caixas: "Ol" | "á" | "," | " mundo" | "!"]
[VISUAL: Label verde: "pontuação = token próprio"]

**NARRADOR:**
> Até a vírgula é um token separado.

---

## SEGMENTO 4 — MECANISMO GENERATIVO (0:43–1:18)

[VISUAL: Transição para layout do mecanismo]

**NARRADOR:**
> Mas como a IA gera o próximo token?

---

**Passo 1 — Tokens entram na rede:**

[VISUAL: 4 caixas de token à esquerda/topo: "Int" | "el" | "ig" | "ência"]
[VISUAL: Setas fluem para um diagrama de rede neural estilizado no centro — nós acendem em sequência]

**NARRADOR:**
> Os tokens de entrada são processados pela rede neural.

---

**Passo 2 — Lista de probabilidades aparece:**

[VISUAL: À direita/abaixo da rede, lista vertical de candidatos com barras de probabilidade:]
```
▁artificial   ████████ 42%
▁incrível     ███░░░░░ 18%
▁muda         ██░░░░░░ 11%
▁é            █░░░░░░░  7%
...
```
[VISUAL: Linha do topo destacada com borda AMARELA, leve aumento de escala]

**NARRADOR:**
> A rede calcula a probabilidade de cada possível próximo token.

---

**Passo 3 — Token vencedor, ciclo se repete:**

[VISUAL: O token "▁artificial" voa da lista e se junta à sequência de entrada]
[VISUAL: Nova sequência agora tem 5 tokens. O ciclo roda mais 2 vezes em fast-forward]
[VISUAL: A frase vai se construindo token por token: "Inteligência" → "Inteligência artificial" → "Inteligência artificial muda" → ...]

**NARRADOR:**
> O mais provável é escolhido.
> E o ciclo se repete — um pedacinho de cada vez.

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
