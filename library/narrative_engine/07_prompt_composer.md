# Prompt Composer — Narrative Engine (FCE)

O Prompt Composer é o **último estágio** do Narrative Pipeline. Ele **monta** o Prompt Final a partir de módulos — nunca inventa cena do zero.

**Regra absoluta FCE:**  
> Nunca escrever prompts Veo manualmente. Sempre compor.

`library/veo3/prompt-rules.md` valida o output. Este documento **gera** o output.

---

## Fluxo de composição

```
┌─────────────┐
│  NARRATIVA  │  Arco do vídeo, atos, mensagem global
└──────┬──────┘
       ▼
┌─────────────┐
│ PERSONAGEM  │  02_character_engine → descriptor block
└──────┬──────┘
       ▼
┌─────────────┐
│    CENA     │  03_scene_builder → todos os campos
└──────┬──────┘
       ▼
┌─────────────┐
│   EMOÇÃO    │  04_emotion_engine → 7 dimensões
└──────┬──────┘
       ▼
┌─────────────┐
│  SÍMBOLO    │  05_symbol_library → metáfora visual
└──────┬──────┘
       ▼
┌─────────────┐
│ FOTOGRAFIA  │  06_cinematography_library → plano, luz, cor
└──────┬──────┘
       ▼
┌─────────────┐
│PROMPT FINAL │  Inglês → Veo (depois Filmora para texto)
└─────────────┘
```

**Hook (cena 01):** `01_hook_engine.md` alimenta **cena 1** antes do fluxo acima.

---

## Inputs obrigatórios

Antes de compor, o agente deve ter:

| Input | Fonte |
|-------|-------|
| `scene_id` | Scene document |
| `character_id` + descriptor | Character sheet |
| `emotion_id` | Emotion engine |
| `symbol_id` | Symbol library |
| `cinematography_block` | Scene document |
| `dramatic_objective` | Scene document |
| `aspect_ratio` | Default `9:16` |
| `duration_seconds` | 6–8 typical |

**Gate:** se faltar campo → **parar** e completar Scene Builder.

---

## Fórmula do Prompt Mestre

Montar em **inglês**, nesta ordem, parágrafo único ou dois blocos curtos:

### Bloco 1 — Técnico-visual

```
{ASPECT}. {SHOT_SIZE}, {LENS_FEEL}, {CAMERA_MOVE}. {COMPOSITION}.
```

### Bloco 2 — Sujeito

```
{CHARACTER_DESCRIPTOR}. {ACTION}. {EMOTION_PERFORMANCE}.
```

### Bloco 3 — Mundo

```
{ENVIRONMENT}. {WEATHER}. {TIME_OF_DAY}. {SYMBOL_VISUAL}.
```

### Bloco 4 — Luz e cor

```
{LIGHTING_STYLE}. {COLOR_PALETTE}. {DEPTH_OF_FIELD}.
```

### Bloco 5 — Intenção

```
Dramatic goal: {DRAMATIC_OBJECTIVE}. {EMOTION_CINEMATIC_FEEL}.
```

### Bloco 6 — Guardrails FCE (sempre)

```
Vertical 9:16, cinematic, photorealistic, 4K, no text, no words, no subtitles,
no watermark, no logos, contemporary Brazilian cinema, authentic working-class
when applicable, not cheesy, not kitsch religious imagery.
```

### Negative prompt (opcional, segunda caixa)

```
text, subtitles, readable signs, watermark, logo, cartoon, halo, crucifix close-up,
distorted hands, celebrity face, horizontal video
```

---

## Mapeamento automático — Emoção → linguagem EN

| emotion_id | Inserir em Bloco 4–5 |
|------------|----------------------|
| hope | warm golden light breaking through, uplifting atmosphere |
| repentance | chiaroscuro, heavy shadows, remorseful mood |
| fear | cold flickering light, claustrophobic tension |
| joy | bright high key, energetic celebratory mood |
| peace | soft diffused wrap light, stillness |
| victory | epic backlight lens flare, triumphant scale |
| silence | minimal motion, quiet ambient stillness |
| pain | desaturated blue-gray, heavy emotional weight |
| trust | steady natural warm light, grounded calm |
| worship | volumetric god rays, reverent awe without cliché |

Detalhes completos: `04_emotion_engine.md`.

---

## Mapeamento — Símbolo → frase visual EN

| symbol_id | Frase composável |
|-----------|------------------|
| tree | solitary tree in wind, roots visible |
| root | hands touching soil and roots |
| seed | planting seeds in earth, small seedling |
| light | god rays through window, dawn breaking |
| water | flowing river reflection, rain on skin |
| rock | feet standing firm on wet rock |
| door | hand on doorframe, light through crack |
| desert | vast dry horizon heat haze |
| mountain | aerial mountain peak above clouds |
| river | walking along riverbank at dawn |
| path | wet sidewalk leading lines forward |
| storm | heavy rain wind dramatic clouds |

Personalizar com contexto da cena — não copiar cegamente.

---

## Exemplo de composição (genérico)

**Inputs resumidos:**  
- Character: Brazilian worker, 30s, navy shirt  
- Emotion: trust → peace  
- Symbol: seed  
- Shot: MCU, 50mm, slow push-in  
- Objective: "Show faithful planting despite exhaustion"

**Output:**

```
Vertical 9:16, cinematic photorealistic. Medium close-up, 50mm lens feel,
slow push-in, subject lower third with negative space above. Brazilian man
early 30s brown skin short black hair light stubble faded navy work shirt,
planting a small seedling in a pot on a windowsill, gentle careful hands,
expression shifting from tired to quietly determined. Small urban workplace
interior, overcast morning, soft rain on window. Symbol of seed and new growth.
Soft natural diffused light transitioning warmer on hands, muted earth tones
with warm highlights. Shallow depth of field. Dramatic goal: faithful planting
of good despite exhaustion Psalm 37. Trust and emerging peace. 4K, no text,
no words, no subtitles, no watermark, contemporary Brazilian cinema,
not cheesy, not kitsch religious imagery.
```

---

## Checklist pós-composição

- [ ] Descriptor do personagem **idêntico** ao Character sheet
- [ ] `no text` presente
- [ ] `9:16` / vertical declarado
- [ ] Objetivo dramático explícito
- [ ] Símbolo visível na descrição
- [ ] Emoção refletida em luz + performance
- [ ] Não contradiz versículo / VibeCore Alerts
- [ ] Negative prompt anexado se plataforma suportar
- [ ] Prompt salvo em `scene-NN.md` campo **Prompt Final**
- [ ] Cópia consolidada em `veo3-prompts.md` (opcional por track)

---

## O que o Composer NÃO faz

| Não | Por quê |
|-----|---------|
| Gerar vídeo | Workflow 9 + Veo |
| Adicionar legendas | Filmora |
| Substituir Director Commentary | `08_director_commentary.md` |
| Ignorar módulos vazios | Qualidade |

---

## Integração com veo3/

| Narrative Engine | veo3/ |
|----------------|-------|
| Pensa como diretor | Traduz para API / valida formato |
| Prompt Composer gera | prompt-rules valida |
| Scene Builder | scene-archetypes (legado) pode cruzar |

**Ordem de leitura para vídeo:**  
`narrative_engine/*` → `07_prompt_composer` → `veo3/prompt-rules` → Veo

---

## Template — Composition Log

```yaml
scene_id: scene-03
composed_at: YYYY-MM-DD
composer_version: narrative_engine_1.0
inputs_hash: [character, emotion, symbol, cinematography blocks]
prompt_final: |
  [OUTPUT EN]
negative_prompt: |
  [OUTPUT EN]
validated_against: library/veo3/prompt-rules.md
manual_edits: none   # se humano editar, documentar aqui — desencorajado
```

---

## Referências

- [03_scene_builder.md](./03_scene_builder.md)
- [08_director_commentary.md](./08_director_commentary.md)
- [library/veo3/prompt-rules.md](../veo3/prompt-rules.md)
- [docs/API_VIDEO_AUTOMATION.md](../../docs/API_VIDEO_AUTOMATION.md)
