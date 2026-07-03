# Plano de Vídeo Veo — {{TITLE}}

> Template para `tracks/track-XX/video/veo3-video-plan.md`

**Faixa:** {{TITLE}}  
**Referência:** {{SCRIPTURE}} ({{REF}})  
**Vibe:** {{VIBE}}  
**Formato prioritário:** **9:16** (Reels, TikTok, Shorts)  
**Status:** [PREENCHER]

---

## Objetivo do vídeo

[PREENCHER — ex.: Reel de lançamento 30–45s, teaser 15s, clip completo]

| Entregável | Formato | Duração alvo |
|------------|---------|--------------|
| Reel principal | 9:16 | [PREENCHER] |
| Clip YouTube | 16:9 | [PREENCHER — opcional] |

---

## Character sheet

```yaml
character_id: protagonist-track-{{NN}}
description: >
  [PREENCHER — descriptor block em inglês, reutilizar em todas as cenas]
wardrobe: [PREENCHER]
distinctive: [PREENCHER — opcional]
avoid: [PREENCHER]
```

Ver `library/veo3/character-continuity.md`.

---

## Archetype e direção

| Campo | Valor |
|-------|-------|
| Archetype principal | [PREENCHER — scene-archetypes.md] |
| Paleta | Ouro / roxo / preto / branco (Álbum 4) |
| Mood | [PREENCHER] |

---

## Mapa de cenas

| # | Seção musical | Timestamp | Archetype | Objetivo dramático | Arquivo |
|---|---------------|-----------|-----------|-------------------|---------|
| 01 | Intro | 0:00 | [PREENCHER] | [PREENCHER] | `scenes/scene-01.md` |
| 02 | Verse 1 | [PREENCHER] | [PREENCHER] | [PREENCHER] | `scenes/scene-02.md` |
| 03 | Pre-Chorus | [PREENCHER] | [PREENCHER] | [PREENCHER] | `scenes/scene-03.md` |
| 04 | Chorus | [PREENCHER] | [PREENCHER] | [PREENCHER] | `scenes/scene-04.md` |
| 05 | Verse 2 | [PREENCHER] | [PREENCHER] | [PREENCHER] | `scenes/scene-05.md` |
| 06 | Bridge | [PREENCHER] | [PREENCHER] | [PREENCHER] | `scenes/scene-06.md` |
| 07 | Outro | [PREENCHER] | [PREENCHER] | [PREENCHER] | `scenes/scene-07.md` |

> Duplicar linhas conforme necessário. Usar `templates/veo3-scene-template.md` por cena.

---

## Ordem de produção

1. [ ] Preencher character sheet
2. [ ] Definir cenas e archetypes
3. [ ] Escrever prompts (6 elementos cada — `prompt-rules.md`)
4. [ ] Gerar manualmente ou via script futuro
5. [ ] Selecionar takes → `assets/video/veo3/`
6. [ ] Montar no Filmora — `filmora/edit-notes.md`

---

## Estimativa de geração

| Métrica | Valor |
|---------|-------|
| Cenas planejadas | [PREENCHER] |
| Takes por cena | 2–3 (recomendado) |
| Total gerações | [PREENCHER] |
| Aspect ratio | **9:16** |
| Custo estimado | [PREENCHER — consultar pricing Google] |

---

## Log de geração

| Cena | Data | Método | Takes | Escolhido | Notas |
|------|------|--------|-------|-----------|-------|
| 01 | — | manual / api | — | — | — |

---

## Integração Filmora

| Cena MP4 | Timestamp reel | Transição | Notas |
|----------|----------------|-----------|-------|
| scene-01.mp4 | 0:00 | cut / fade | sync com intro |

---

## Referências

- [docs/API_VIDEO_AUTOMATION.md](../../../docs/API_VIDEO_AUTOMATION.md)
- [library/veo3/](../../../library/veo3/)
- [WORKFLOW.md § Workflow 9](../../../WORKFLOW.md)
- [track.yaml](../track.yaml)
