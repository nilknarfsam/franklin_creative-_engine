# {{TITLE}} — Template de Faixa

> Copie este arquivo para `albums/album-XX-{slug}/tracks/track-NN-{slug}/` e preencha. **Não edite o template original.**

---

## Metadados (`track.yaml`)

```yaml
id: track-{{NN}}
album_id: album-{{ALBUM_NN}}
number: {{N}}
title: "{{TITLE}}"
slug: {{SLUG}}
scripture: "{{SCRIPTURE}}"
scripture_ref: "{{REF}}"
duration_estimate: "{{DURATION}}"
vibe: "{{VIBE}}"
ministration: {{true|false}}
ministration_notes: "{{MINISTRATION_NOTES}}"
suno_prompt: "{{SUNO_PROMPT}}"
status: concept          # concept | lyrics_draft | lyrics_final | audio | video | published
vibecore_alerts: []
updated: {{DATE}}
```

---

## Conceito (`concept.md`)

### Resumo

[PREENCHER — 1 parágrafo: conceito de criação, emoção central, conexão bíblica]

### Referência bíblica

- Texto base: {{SCRIPTURE}}
- Versículos-chave: [PREENCHER]

---

## Letra (`lyrics.md`)

```markdown
# {{TITLE}} — Letra Definitiva

**Idioma:** Português Brasileiro
**Referência:** {{SCRIPTURE}}
**Status:** draft

---

[Language: Brazilian Portuguese]

[Intro - {{PRODUCTION_NOTES}}, {{VOCAL_TYPE}}]
[PREENCHER]

[Verse 1 - {{PRODUCTION_NOTES}}, {{VOCAL_TYPE}}]
[PREENCHER]

[Pre-Chorus - {{PRODUCTION_NOTES}}, {{VOCAL_TYPE}}]
[PREENCHER]

[Chorus - {{PRODUCTION_NOTES}}, {{VOCAL_TYPE}}]
[PREENCHER]

[Verse 2 - {{PRODUCTION_NOTES}}, {{VOCAL_TYPE}}]
[PREENCHER]

[Bridge - {{PRODUCTION_NOTES}}, {{VOCAL_TYPE}}]
[PREENCHER]

[Outro / Big Finish - {{PRODUCTION_NOTES}}, {{VOCAL_TYPE}}]
[PREENCHER]
[End]
```

---

## Ficha técnica (`technical-sheet.md`)

| Campo | Valor |
|-------|-------|
| Vibe Geral | [PREENCHER] |
| Tempo estimado | [PREENCHER] |
| Ministração | Sim / Não — [notas] |
| Suno Prompt | Ver `suno/prompt.txt` |

---

## Checklist

- [ ] `track.yaml` preenchido
- [ ] Tags Suno em todas as seções
- [ ] Call-and-response no refrão
- [ ] `[End]` presente
- [ ] Auditoria teológica (VibeCore Alerts se necessário)
- [ ] Links para campanha e estudo bíblico
