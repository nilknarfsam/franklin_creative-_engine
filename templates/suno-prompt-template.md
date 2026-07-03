# Suno Prompt — {{TITLE}}

> Template para `tracks/track-XX/suno/prompt.txt` e iterações

**Faixa:** {{TITLE}}  
**Referência:** {{SCRIPTURE}}  
**Data:** {{DATE}}

---

## Prompt principal

```
{{SUNO_PROMPT_LINE_1}},
{{SUNO_PROMPT_LINE_2}},
{{SUNO_PROMPT_LINE_3}},
Brazilian Portuguese vocals
```

**Regra FCE:** Sempre terminar com `Brazilian Portuguese vocals`.

---

## Letra

Colar conteúdo de `lyrics.md` (com tags `[Section]`) no campo de letra do Suno.

---

## Parâmetros sugeridos

| Parâmetro | Valor |
|-----------|-------|
| Vibe | {{VIBE}} |
| Duração alvo | {{DURATION}} |
| Ministração | {{MINISTRATION}} |

---

## Log de iterações (`suno/iterations/notes.md`)

| # | Data | Prompt variant | Resultado | Notas |
|---|------|----------------|-----------|-------|
| 1 | — | default | — | — |

### Critérios de aceite

- [ ] Dinâmica: intro íntima → refrão explosivo
- [ ] Vocais teatrais coerentes com ficha técnica
- [ ] Call-and-response audível no refrão
- [ ] Duração dentro da estimativa
- [ ] PT-BR inteligível

---

## Export

**Master alvo:** `assets/audio/track-{{NN}}-{{SLUG}}-master.wav`
