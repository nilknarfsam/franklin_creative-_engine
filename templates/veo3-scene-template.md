# Cena Veo — {{SCENE_ID}}

> Template para `tracks/track-XX/video/scenes/scene-{{NN}}.md` ou entrada no plano de vídeo.

**Faixa:** {{TITLE}} ({{SCRIPTURE}})  
**Seção musical:** {{SECTION}} — ex.: Intro, Verse 1, Chorus  
**Archetype:** {{ARCHETYPE}} — ver `library/veo3/scene-archetypes.md`  
**Status:** [PREENCHER]

---

## Metadados

| Campo | Valor |
|-------|-------|
| scene_id | scene-{{NN}} |
| character_id | {{CHARACTER_ID}} |
| aspect_ratio | **9:16** |
| duration_target | 5–8s |
| continuity | same / broken — symbolic |

---

## Os 6 elementos

### 1. Personagem

[PREENCHER — copiar descriptor block do plano se `continuity: same`]

```
[PREENCHER — descrição em inglês para prompt]
```

### 2. Ambiente

[PREENCHER]

```
[PREENCHER]
```

### 3. Emoção

[PREENCHER — expressão, postura, ação]

```
[PREENCHER]
```

### 4. Câmera

[PREENCHER — ver library/veo3/camera-moves.md]

```
[PREENCHER — ex.: Slow push-in, medium close-up, shallow depth of field]
```

### 5. Iluminação

[PREENCHER]

```
[PREENCHER — ex.: Golden hour side light, warm 3200K, soft shadows]
```

### 6. Objetivo dramático

[PREENCHER — por que esta cena existe; ligação com letra/seção]

---

## Prompt Veo (consolidado)

> Colar no AI Studio / script futuro. **Inglês. Sem texto no vídeo.**

```
[PREENCHER — prompt único consolidando os 6 elementos]

Vertical 9:16 aspect ratio, cinematic, 4K, no text, no watermark,
contemporary Christian aesthetic, not cheesy.
```

### Negative prompt (opcional)

```
text, subtitles, watermark, logo, blurry, distorted hands, cartoon, kitsch religious imagery
```

---

## Pós-geração

| Campo | Valor |
|-------|-------|
| take_escolhido | [PREENCHER — v1, v2, v3] |
| arquivo | `assets/video/veo3/scene-{{NN}}.mp4` |
| timestamp_no_reel | [PREENCHER] |
| notas | [PREENCHER] |

---

## Referências

- [Plano de vídeo](./veo3-video-plan.md)
- [Storyboard](./storyboard.md)
- [Brief Veo 3](./veo3-brief.md)
