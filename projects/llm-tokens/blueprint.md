# Blueprint: What Is a Token? (How AI Actually Reads Text)

**Format:** YouTube Shorts — vertical 9:16, ≤ 90 seconds
**Language:** Portuguese (Brazil)
**Target audience:** Curious general public, no technical background
**Bloom's level:** Comprehension + Analysis

---

## Learning Objectives

By the end of this video, the viewer will be able to:

1. **Describe** what a token is in the context of LLMs (Comprehension)
2. **Distinguish** tokens from words using subword and punctuation examples (Analysis)
3. **Explain** the generative mechanism in simple terms: tokens in → probabilities out → next token chosen (Comprehension)

---

## Misconception to Attack

> "AI reads and writes text the same way humans do — word by word, sentence by sentence."

This is shattered in the first 3 seconds by showing a sentence fragmenting into unexpected pieces.

---

## Segment Breakdown (~90s total)

| # | Segment | Duration | Purpose |
|---|---------|----------|---------|
| 1 | Hook | ~8s | Sentence shatters into tokens — visual shock |
| 2 | Definição de Token | ~15s | "Este pedaço é o que chamamos de token" |
| 3 | Token ≠ Palavra | ~20s | 3 flash-card examples with real tokenizer splits |
| 4 | Mecanismo Generativo | ~35s | 3 visual steps: tokens → net → probs → winner cycles |
| 5 | Fechamento | ~12s | Mantra + 3s silence over tokenized phrase |

---

## Segment Details

### 1. Hook (0:00–0:08)

- Sentence appears whole: *"Inteligência artificial muda o mundo"*
- Then it **shatters** into colored token boxes
- Narrator: challenges the viewer's assumption

**Key visual:** colored bounding boxes around each token, not word boundaries

---

### 2. Definição de Token (0:08–0:23)

- Define token as "a menor unidade que a IA processa"
- Simple analogy: like letters are the smallest unit of a word, tokens are the smallest unit for the AI
- Yellow highlight box surrounds the definition

---

### 3. Token ≠ Palavra (0:23–0:43)

Three flash-card examples using **real cl100k_base splits**:

| Word | Tokens | Count |
|------|--------|-------|
| `gato` | `gato` | 1 token |
| `inacreditável` | `in` + `acredit` + `ável` | 3 tokens |
| `Olá, mundo!` | `Ol` + `á` + `,` + ` mundo` + `!` | 5 tokens |

> ⚠️ Scriptwriter must verify splits against cl100k_base or o200k_base before finalizing.

**Key insight to land:** punctuation is its own token; common words may be 1 token; rare/long words split into subword pieces.

---

### 4. Mecanismo Generativo (0:43–1:18) — most important

Three visual sub-steps:

**Step 1 — Tokens enter the network:**
- Token boxes flow into a stylized neural network diagram
- Network nodes light up (FadeIn animations)

**Step 2 — Probability list appears:**
- Right side shows candidate next-tokens with probability bars
- Top candidate highlighted in YELLOW

**Step 3 — Token selected, cycle repeats:**
- Winning token flies back into the input sequence
- Cycle runs 2–3 more times in fast-forward
- Assembled phrase builds up token by token

**Forbidden verbs:** pensar, entender, saber, querer
**Approved verbs:** calcular, prever, processar, escolher, gerar

---

### 5. Fechamento (1:18–1:30)

Mantra (2 lines, centered):

> *"A IA não escreve frases.*
> *Ela prevê um pedacinho de cada vez."*

Hold 3 seconds. Fade to black.

---

## Word Budget

- Spoken narration: ~173 words (~75 seconds at 2.3 wps)
- Visual-only moments: ~15 seconds (no narration, animation speaks)
- Total: ≤ 90 seconds

---

## Scope Lock

The following topics are **explicitly excluded** to maintain the 90s budget:

- BPE (Byte Pair Encoding) algorithm details
- Embeddings and vector space
- Attention mechanism
- Sampling parameters (temperature, top-p)

The video stops at: *"LLMs predict one token at a time."*
