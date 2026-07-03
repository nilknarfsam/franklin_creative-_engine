# Prompt Composition — O Legado

**Track:** track-01 — O Legado  
**Compositor:** Narrative Engine `07_prompt_composer.md`  
**Regra FCE:** Prompts montados a partir de campos documentados — não escritos manualmente soltos.

**Fontes:**
- [character.md](./character.md) — descriptor block
- [scenes.md](./scenes.md) — 17 campos por cena
- [hook.md](./hook.md) — Cena 01
- [library/narrative_engine/04_emotion_engine.md](../../../../../library/narrative_engine/04_emotion_engine.md)
- [library/narrative_engine/05_symbol_library.md](../../../../../library/narrative_engine/05_symbol_library.md)
- [library/narrative_engine/06_cinematography_library.md](../../../../../library/narrative_engine/06_cinematography_library.md)

**Validação:** [library/veo3/prompt-rules.md](../../../../../library/veo3/prompt-rules.md)

---

## Fórmula aplicada (por cena)

```
Bloco 1 — Técnico-visual:   ASPECT + SHOT + LENS + CAMERA_MOVE + COMPOSITION
Bloco 2 — Sujeito:           CHARACTER_DESCRIPTOR + ACTION + EMOTION_PERFORMANCE
Bloco 3 — Mundo:             ENVIRONMENT + WEATHER + TIME + SYMBOL_VISUAL
Bloco 4 — Luz e cor:         LIGHTING + PALETTE + DEPTH_OF_FIELD
Bloco 5 — Intenção:          DRAMATIC_OBJECTIVE + EMOTION_CINEMATIC_FEEL
Bloco 6 — Guardrails FCE:    9:16, 4K, no text, Brazilian cinema, not kitsch
```

---

## Cena 01 — Pressão

### Linhagem de composição

| Bloco | Fonte | Elemento extraído |
|-------|-------|-------------------|
| 1 | scenes.md §01 | MS, 35mm, tracking lateral, rule of thirds |
| 2 | character.md | Descriptor block + ombros caídos, exaustão |
| 3 | scenes.md §01 | Prédio comercial SP, dusk, símbolo `path` |
| 4 | emotion `pain` + scenes.md | Fluorescente fria, desaturado, shallow DOF |
| 5 | scenes.md §01 | Objetivo: pressão diária · Sl 37:1 |
| 6 | 07_prompt_composer | Guardrails FCE |

### Prompt Final

```
Vertical 9:16, cinematic photorealistic. Medium shot, 35mm lens feel, slow lateral
tracking shot, subject lower third with wet sidewalk leading lines forward.
Brazilian man, early 30s, brown skin, short black hair, light stubble, tired but
dignified expression, natural build, faded navy blue work shirt, dark jeans, worn
boots, small backpack, shoulders heavy, walking out of a modest commercial building
at dusk, exhausted expression, urban Brazil, blurred bus and traffic in background.
Dry urban air, dusk twilight. Symbol of daily path and journey not yet surrendered.
Cold fluorescent mixed with gray twilight, desaturated blue-gray color grade,
shallow depth of field. Dramatic goal: establish daily pressure and exhaustion
Psalm 37. Desaturated blue-gray, heavy emotional weight, working-class authenticity.
4K, no text, no words, no subtitles, no watermark, no logos, contemporary Brazilian
cinema, authentic working-class, not cheesy, not kitsch religious imagery.
```

### Negative prompt

```
text, subtitles, readable signs, logo, cartoon, halo, crucifix, smiling influencer,
office suit, horizontal video, blurry face, extra fingers
```

```yaml
scene_id: scene-01
composed_at: 2026-07-02
composer_version: narrative_engine_1.0
manual_edits: none
```

---

## Cena 02 — Comparação

### Linhagem de composição

| Bloco | Fonte | Elemento extraído |
|-------|-------|-------------------|
| 1 | scenes.md §02 | CU, 85mm, static + micro handheld |
| 2 | character.md | Descriptor + mandíbula tensa, celular |
| 3 | scenes.md §02 | Ponto de ônibus noite, símbolo `storm` interior |
| 4 | emotion `pain` | Azul tela, chiaroscuro, shallow DOF |
| 5 | scenes.md §02 | Comparação/inveja · Sl 37:1–2 |
| 6 | Guardrails FCE | no text, phone blur |

### Prompt Final

```
Vertical 9:16, cinematic photorealistic. Close-up, 85mm portrait lens feel, static
with subtle handheld tension, shallow depth of field, face centered lower third.
Same Brazilian man early 30s, brown skin, short black hair, light stubble, faded
navy work shirt, sitting at a city bus stop at night, holding smartphone, phone
screen showing only soft blurred colorful bokeh light with no readable content,
face illuminated by cold blue phone glow, jaw slightly tense, eyes comparing and
hurting but controlled, blurred happy people in background. Dry night air, urban
Brazil. Interior storm of silent envy without physical rain. Cold urban artificial
lighting, chiaroscuro, desaturated blue-gray with cold screen highlights. Dramatic
goal: temptation to compare with others who seem to prosper faster Psalm 37.
Heavy emotional weight, claustrophobic inner tension. 4K, no text, no words,
no subtitles, no watermark, contemporary Brazilian urban drama, not religious,
not cheesy.
```

### Negative prompt

```
readable phone screen, instagram UI, text messages, logo, cartoon, violent anger,
horizontal layout, distorted hands
```

```yaml
scene_id: scene-02
composed_at: 2026-07-02
composer_version: narrative_engine_1.0
manual_edits: none
```

---

## Cena 03 — Fidelidade

### Linhagem de composição

| Bloco | Fonte | Elemento extraído |
|-------|-------|-------------------|
| 1 | scenes.md §03 | MS → ECU, 50mm, focus pull |
| 2 | character.md | Descriptor + mãos gentis, mangas arregaçadas |
| 3 | scenes.md §03 | Depósito, manhã nublada, símbolo `seed` |
| 4 | emotion `trust` | Luz difusa neutra, tons terra |
| 5 | scenes.md §03 | Plantar o bem · Sl 37:3 |
| 6 | Guardrails FCE | |

### Prompt Final

```
Vertical 9:16, cinematic photorealistic. Medium wide shot then gentle focus pull
to extreme close-up on hands, 50mm lens feel, subject centered with window light.
Same Brazilian man early 30s, brown skin, faded navy work shirt with rolled sleeves,
organizing boxes carefully in a small warehouse workspace, honest diligent work,
then planting a small green seedling in a pot on a windowsill, hands firm and gentle,
spreading seeds in a tiny urban community garden bed. Overcast morning, dry cloudy
sky. Symbol of seed and planting good in earth. Soft natural diffused light, neutral
earth tones with green seedling accent, moderate depth of field. Dramatic goal:
faithful honest labor and planting good seeds metaphor Psalm 37. Steady natural warm
light emerging, grounded calm integrity. 4K, no text, no words, no subtitles,
no watermark, Brazilian workplace realism, not cheesy, not kitsch religious symbols.
```

### Negative prompt

```
text, logo on uniform, construction brand, cartoon, golden halo, horizontal video
```

```yaml
scene_id: scene-03
composed_at: 2026-07-02
composer_version: narrative_engine_1.0
manual_edits: none
```

---

## Cena 04 — Pausa

### Linhagem de composição

| Bloco | Fonte | Elemento extraído |
|-------|-------|-------------------|
| 1 | scenes.md §04 | MS static, 50mm, composição central |
| 2 | character.md | Descriptor + livro fechado, olhos fechados |
| 3 | scenes.md §04 | Terraço meio-dia, símbolo `light` contida |
| 4 | emotion `silence` | Low key difuso frio |
| 5 | scenes.md §04 | Descanso na Palavra · Sl 37:7 |
| 6 | Guardrails FCE | livro sem texto legível |

### Prompt Final

```
Vertical 9:16, cinematic photorealistic. Static centered medium shot, 50mm lens
feel, minimalist composition, subject centered with soft urban skyline behind.
Same Brazilian man early 30s, brown skin, faded navy work shirt, sitting alone on
a quiet building rooftop or empty corridor during lunch break, simple dark closed
book resting on his lap with plain cover and no readable title, eyes closed in deep
reflection, slow calm breathing, vulnerable peaceful posture, urban skyline soft
and blurred behind. Still dry air, overcast noon. Symbol of contained inner light
and scripture off-screen. Soft diffused cool daylight, low contrast gray-lavender
palette, stillness and sacred pause. Dramatic goal: contemplative rest and reflection
on scripture off-screen Psalm 37. Minimal motion, quiet ambient stillness. 4K,
no text, no words, no subtitles, no watermark, no cross, no church, Brazilian
contemporary emotional cinema, not cheesy.
```

### Negative prompt

```
open bible with readable text, church interior, priest, halo, rosary close-up,
horizontal video, praying hands cliché
```

```yaml
scene_id: scene-04
composed_at: 2026-07-02
composer_version: narrative_engine_1.0
manual_edits: none
```

---

## Cena 05 — Transfiguração

### Linhagem de composição

| Bloco | Fonte | Elemento extraído |
|-------|-------|-------------------|
| 1 | scenes.md §05 | MCU, 65mm, slow push-in |
| 2 | character.md | Descriptor + mesmo local, ombros relaxam |
| 3 | scenes.md §05 | Mesmo terraço, nuvens abrindo, `light` |
| 4 | emotion `peace` | Cool → warm 3200K, god rays |
| 5 | scenes.md §05 | Ansiedade → paz · Sl 37:5, 7 |
| 6 | Guardrails FCE | continuidade com cena 04 |

### Prompt Final

```
Vertical 9:16, cinematic photorealistic. Slow push-in medium close-up, 65mm portrait
lens feel, subject centered, negative space above for breaking sky.
Same Brazilian man early 30s, brown skin, faded navy work shirt, same rooftop
location as before, clouds parting, warm golden sunbeam breaking through and
illuminating his face, visible light transition from cool gray to warm gold on skin,
shoulders dropping with relief, gentle peaceful smile, soft wind moving shirt,
emotional transformation from anxiety to peace. Light breeze, clouds parting.
Symbol of god rays through window of sky, dawn breaking on face. God rays, golden
hour breakthrough, soft diffused wrap light transitioning warmer. Dramatic goal:
light changes as inner peace arrives Psalm 37. Soft diffused wrap light, stillness
and emerging peace. 4K, no text, no words, no subtitles, no watermark, not religious
kitsch, Brazilian cinematic emotional realism.
```

### Negative prompt

```
halo, angel, crucifix, cartoon light, horizontal, different person, different shirt color
```

```yaml
scene_id: scene-05
composed_at: 2026-07-02
composer_version: narrative_engine_1.0
manual_edits: none
```

---

## Cena 06 — Esperança

### Linhagem de composição

| Bloco | Fonte | Elemento extraído |
|-------|-------|-------------------|
| 1 | scenes.md §06 | WS, steadicam → crane, 35–24mm |
| 2 | character.md | Descriptor + passos firmes, mãos abertas |
| 3 | scenes.md §06 | Calçada arborizada sunrise, `path` |
| 4 | emotion `hope` | Golden hour, ouro + roxo álbum |
| 5 | scenes.md §06 | Entregar caminho · Sl 37:5 |
| 6 | Guardrails FCE | |

### Prompt Final

```
Vertical 9:16, cinematic photorealistic epic emotional finale. Steadicam follow from
behind then slight crane up, 35mm widening to 24mm feel, subject walking into upper
third toward golden horizon, tree-lined path leading lines forward.
Same Brazilian man early 30s, brown skin, faded navy work shirt, walking confidently
along a tree-lined sidewalk or urban viewpoint at sunrise, Brazilian city skyline
in background, hands slightly open at sides in quiet surrender not theatrical, firm
hopeful steps walking toward the light. Clean morning air, soft breeze. Symbol of
path surrendered and walking toward light. Golden hour light, deep purple and gold
tones in sky, subtle lens flare, epic backlight, shallow to deep depth of field on
crane reveal. Dramatic goal: hope and commit your way to the Lord Psalm 37:5.
Warm golden light breaking through, uplifting atmosphere, legacy of peace. 4K,
no text, no words, no subtitles, no watermark, no religious clichés, contemporary
Brazilian cinema, not cheesy.
```

### Negative prompt

```
text overlay, church building dominant, halo, horizontal, running dramatically,
superhero pose, cartoon sunrise
```

```yaml
scene_id: scene-06
composed_at: 2026-07-02
composer_version: narrative_engine_1.0
manual_edits: none
```

---

## Ordem de geração recomendada

1. **Cena 04 → 05** (mesmo location — continuidade)
2. **Cena 01 → 02 → 03** (arco urbano)
3. **Cena 06** (golden hour independente)

---

## Checklist pós-composição

- [x] Descriptor idêntico ao [character.md](./character.md)
- [x] `no text` em todos os prompts
- [x] `9:16` / vertical declarado
- [x] Objetivo dramático explícito por cena
- [x] Símbolo visível na descrição
- [x] Emoção refletida em luz + performance
- [x] Linhagem documentada por cena
- [ ] Takes gerados em `assets/video/veo3/` (pendente produção)

**Módulo:** [library/narrative_engine/07_prompt_composer.md](../../../../../library/narrative_engine/07_prompt_composer.md)
