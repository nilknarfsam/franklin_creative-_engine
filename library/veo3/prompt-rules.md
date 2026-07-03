# Regras de Prompt — Veo 3 (FCE)

Regras curadas para geração de vídeo no Franklin Creative Engine. Aplicar a **toda cena** antes de enviar ao Veo (manual ou script futuro).

---

## Os 6 elementos obrigatórios

Cada prompt de cena **deve** declarar explicitamente:

| # | Elemento | Pergunta-guia |
|---|----------|---------------|
| 1 | **Personagem** | Quem aparece? Idade, vestimenta, postura, etnia (se relevante) |
| 2 | **Ambiente** | Onde? Interior/exterior, época, clima, profundidade |
| 3 | **Emoção** | O que sente? Expressão facial, linguagem corporal |
| 4 | **Câmera** | Como enquadra? Ver `camera-moves.md` |
| 5 | **Iluminação** | Qual luz? Golden hour, chiaroscuro, backlight, etc. |
| 6 | **Objetivo dramático** | Por que esta cena existe na narrativa da faixa? |

**Sem os 6 elementos → prompt incompleto.** Agentes devem recusar entregar prompt parcial.

---

## Regras universais FCE

### Texto no vídeo

```
DEFAULT: no text, no words, no subtitles, no letters, no watermark
EXCEÇÃO: apenas quando humano solicitar explicitamente (ex.: lyric kinetic no Filmora, não no Veo)
```

Letras e versículos entram na **montagem Filmora**, não na geração Veo.

### Idioma do prompt

- **Prompts Veo:** inglês (melhor aderência do modelo)
- **Conteúdo ministerial:** coerente com PT-BR da faixa, mas descrito em inglês no prompt
- **Diálogo falado no vídeo:** evitar — FCE usa áudio da faixa Suno

### Aspect ratio

| Prioridade | Ratio | Uso |
|------------|-------|-----|
| **1** | **9:16** | Reels, TikTok, Shorts |
| 2 | 16:9 | YouTube clip |
| 3 | 1:1 | Post estático animado (raro) |

Incluir no prompt: `vertical 9:16 aspect ratio` ou `portrait orientation`.

### Duração

- **5–8 segundos** por cena (sweet spot para edição)
- Uma ação principal por clip — evitar múltiplos beats narrativos

### Estética VibeCore

```
cinematic, theatrical, contemporary Christian aesthetic, not cheesy, not kitsch,
biblical metaphor, dramatic lighting, high production value, 4K quality
```

### Proibido / evitar

- Ícones religiosos caricatos (coroinha de ouro genérica, halos clichê)
- Violência gráfica explícita
- Texto legível gerado pela IA (distorsão comum)
- Logos, marcas, rostos de celebridades
- Estilo cartoon unless faixa pedir (não é padrão FCE)

---

## Template de prompt (inglês)

```
[CAMERA]: [move type], [framing]
[SUBJECT/CHARACTER]: [description], [emotion], [action]
[ENVIRONMENT]: [location], [weather/time], [depth]
[LIGHTING]: [style], [direction], [color temperature]
[MOOD]: [dramatic goal aligned with track section]
[TECH]: vertical 9:16, cinematic, 4K, no text, no watermark,
contemporary Christian aesthetic, not cheesy
```

### Exemplo — Track 01 *O Legado* (Intro)

```
Slow push-in, medium close-up. A young Brazilian man in simple dark clothing,
eyes closed, peaceful expression, hands open in surrender. Sitting by a window
at dawn, soft rain on glass, shallow depth of field, city blurred outside.
Warm golden side light breaking through clouds, hope emerging from anxiety.
Dramatic goal: intimate trust before the beat drops. Vertical 9:16, cinematic,
4K, no text, contemporary Christian aesthetic, not cheesy.
```

---

## Sincronia com seções musicais

| Seção da faixa | Energia visual | Câmera típica |
|----------------|----------------|---------------|
| Intro | Contida, íntima | Slow push-in, static wide |
| Verse | Narrativa, flow | Tracking, medium shot |
| Pre-Chorus | Tensão crescente | Handheld subtle, faster cut prep |
| Chorus | Explosão | Crane up, wide epic, lens flare |
| Bridge | Breakdown | Static, silhouette, minimal |
| Outro | Resolução | Pull back, aerial or wide hold |

---

## Negative prompt (quando suportado)

```
text, subtitles, watermark, logo, blurry faces, distorted hands,
cartoon, anime, low quality, oversaturated, cheesy religious imagery,
crucifix close-up, neon colors, horizontal layout
```

---

## Validação antes de gerar

- [ ] 6 elementos presentes
- [ ] `no text` incluído (salvo exceção documentada)
- [ ] 9:16 declarado
- [ ] Coerente com `track.yaml` → vibe
- [ ] Objetivo dramático ligado a seção do storyboard
- [ ] Continuidade de personagem (ver `character-continuity.md`)

---

## Referências

- `camera-moves.md` — vocabulário de movimento
- `character-continuity.md` — consistência entre cenas
- `scene-archetypes.md` — metáforas bíblicas por vibe
- `templates/veo3-scene-template.md` — formulário por cena
