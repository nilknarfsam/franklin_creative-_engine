# Character Engine — Narrative Engine (FCE)

O Character Engine constrói **pessoas**, não manequins. Aparência é a última camada — depois de história, desejo, medo e contradição. Todo vídeo FCE com protagonista humano **deve** ter ficha completa antes da primeira cena.

**Escopo:** permanente, multi-álbum. Personagens podem recorrer entre projetos (universo FCE) ou ser únicos por faixa.

---

## Por que personagem antes de prompt

Veo e qualquer IA visual **alucinam rostos** sem âncora psicológica. Um descriptor block rico reduz deriva e dá ao diretor (humano ou agente) linguagem para corrigir takes.

| Camada | Função cinematográfica |
|--------|------------------------|
| História / medo / sonho | Motiva **ação** na cena |
| Personalidade | Define **ritmo** e gesto |
| Tom emocional | Liga cena a `04_emotion_engine.md` |
| Continuidade | Liga cena a `library/veo3/character-continuity.md` |
| Tratamento de câmera | Define **como** o mundo enquadra essa pessoa |

---

## Campos obrigatórios

Cada personagem documenta **todos** os campos abaixo.

### Identidade

| Campo | Descrição |
|-------|-----------|
| **Nome** | Nome próprio + sobrenome opcional |
| **Idade** | Faixa etária exata ou aproximada |
| **Profissão** | Trabalho, contexto de classe, rotina |

### Interior

| Campo | Descrição |
|-------|-----------|
| **História** | 3–5 frases: de onde veio, o que marcou |
| **Família** | Quem importa; ausências; dependências |
| **Sonhos** | O que deseja honestamente |
| **Medos** | O que evita (concreto, não abstrato) |
| **Objetivos** | O que persegue **neste** vídeo/álbum |
| **Personalidade** | Traços, contradições, humor, silêncio |

### Exterior

| Campo | Descrição |
|-------|-----------|
| **Roupa** | Peças, estado (gasto, limpo), evolução por ato |
| **Características físicas** | Pele, cabelo, porte, marcas — sem estereótipo ofensivo |
| **Forma de andar** | Ritmo, ombros, peso nos pés |
| **Forma de olhar** | Direto, evita, fixa horizonte, baixa |
| **Expressão default** | Rosto em repouso antes da cena |

### Cinematografia

| Campo | Descrição |
|-------|-----------|
| **Tom emocional** | Paleta interior dominante no arco |
| **Continuidade** | `character_id`, variações por ato, o que não muda |
| **Tratamento de câmera** | Como a câmera o honra ou opressa |

---

## Tratamento de câmera por tipo de personagem

| Arquétipo | Plano dominante | Movimento | Luz |
|-----------|-----------------|-----------|-----|
| **Oprimido** | Close, claustro | Handheld, push-in lento | Fria, top light dura |
| **Buscador** | Medium, tracking | Steadicam follow | Neutra → warm |
| **Testemunha** | Wide + insert | Static, observacional | Naturalista |
| **Celebrante** | Wide épico, crane | Orbit, pull-back | High key, golden |
| **Sábio / ancião** | Medium close, nível olhos | Static respeitoso | Soft side, warm low |

O personagem FCE **não é tipo fixo** — pode migrar de Oprimido → Buscador → Celebrante no mesmo vídeo.

---

## Template reutilizável — Character Sheet

Salvar em: `tracks/track-XX/video/narrative/character-{slug}.md`

```yaml
---
character_id: char-{slug}
fce_universe: standalone    # standalone | recurring | album-cast
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# {Nome completo}

## Identidade

| Campo | Valor |
|-------|-------|
| Nome | |
| Idade | |
| Profissão | |
| Cidade / contexto | |

## Interior

### História

[PREENCHER — 3–5 frases narrativas]

### Família

[PREENCHER]

### Sonhos

[PREENCHER]

### Medos

[PREENCHER — específicos: "perder o emprego", não "o futuro"]

### Objetivos (neste vídeo)

[PREENCHER]

### Personalidade

[PREENCHER — traços + contradição: "gentil mas orgulhoso"]

## Exterior

### Roupa

| Ato | Vestuário |
|-----|-----------|
| Ato I | |
| Ato II | |
| Ato III | |

### Características físicas

[PREENCHER]

### Corpo na cena

| Campo | Valor |
|-------|-------|
| Forma de andar | |
| Forma de olhar | |
| Expressão em repouso | |
| Gestos recorrentes | |

## Cinematografia

| Campo | Valor |
|-------|-------|
| Tom emocional dominante | |
| Arco emocional | Ato I → II → III |
| Continuidade | Descriptor block EN abaixo |
| Tratamento de câmera | |

### Descriptor block (copiar em todo prompt via Composer)

```
[PREENCHER — inglês, 2–4 frases, mesma pessoa em todas as cenas]
```

### Evitar (Veo drift)

```
[PREENCHER — ex.: different age, suit, beard change, celebrity look]
```

## Ligação narrativa

| Campo | Valor |
|-------|-------|
| Versículo anchor | |
| Símbolo pessoal | ver 05_symbol_library.md |
| Hook recomendado | ver 01_hook_engine.md |
```

---

## Exemplo canônico (ilustrativo — adaptar por projeto)

> **Nota:** Exemplo de estrutura, não personagem obrigatório do Álbum 4.

**Elena Marques, 34** — enfermeira noturna, mãe solo. História de dupla jornada e fé silenciosa. Medo: não ser suficiente para o filho. Sonho: estabilidade sem perder a alma. Câmera: começa claustro (corredor hospital); termina wide (janela alvorada). Descriptor: *"Brazilian woman, mid-30s, tired gentle eyes, nurse scrubs or simple clothes..."*

---

## Múltiplos personagens

| Regra | Detalhe |
|-------|---------|
| Protagonista | Ficha completa obrigatória |
| Antagonista / pressão | Pode ser **força** (sistema, tempo) sem rosto |
| Coletivo | "Multidão" sem rosto dominante — diversidade, não individualização |
| Deus / divino | **Nunca** rosto humanizado — luz, espaço, símbolo |

---

## Checklist Character Engine

- [ ] Todos os campos preenchidos
- [ ] Medos e sonhos são **específicos**
- [ ] Descriptor block EN pronto para Composer
- [ ] Tratamento de câmera declarado
- [ ] Evolução de roupa por ato (se houver)
- [ ] `character_id` único no repositório
- [ ] Comentário do diretor cita motivação do personagem

---

## Referências

- [03_scene_builder.md](./03_scene_builder.md)
- [04_emotion_engine.md](./04_emotion_engine.md)
- [07_prompt_composer.md](./07_prompt_composer.md)
- [library/veo3/character-continuity.md](../veo3/character-continuity.md)
