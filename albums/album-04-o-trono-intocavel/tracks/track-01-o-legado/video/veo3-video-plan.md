# Plano de Vídeo Veo — O Legado

**Faixa:** O Legado  
**Referência:** Salmo 37 (Sl 37)  
**Vibe:** Trap Acústico & Pop Teatral  
**Formato prioritário:** **9:16** (Reels, TikTok, Shorts)  
**Status:** Narrative Pipeline completo — pronto para geração Veo (Workflow 9)  
**Projeto:** Primeiro ciclo criativo completo FCE

> **Fonte narrativa principal:** [`video/narrative/`](./narrative/)  
> Hook, personagem, cenas (17 campos), prompts compostos e director commentary vivem no Narrative Engine. Este arquivo é o **plano operacional** derivado.

| Narrative Engine | Path |
|------------------|------|
| Manifest | [narrative/narrative-manifest.yaml](./narrative/narrative-manifest.yaml) |
| Hook | [narrative/hook.md](./narrative/hook.md) |
| Personagem | [narrative/character.md](./narrative/character.md) |
| Cenas | [narrative/scenes.md](./narrative/scenes.md) |
| Prompts (composição) | [narrative/prompt-composition.md](./narrative/prompt-composition.md) |
| Director commentary | [narrative/director-commentary.md](./narrative/director-commentary.md) |

---

## Objetivo do vídeo

Curta cinematográfico vertical que traduz o Salmo 37 em narrativa contemporânea brasileira: um trabalhador enfrenta pressão e comparação, permanece fiel, encontra paz na Palavra e encerra com esperança no refrão da faixa.

| Entregável | Formato | Duração alvo |
|------------|---------|--------------|
| **Curta principal** | 9:16 | **45–60 s** |
| Teaser (derivado) | 9:16 | 15 s (cenas 1 + 6) |
| Clip YouTube | 16:9 | Opcional — reframe no Filmora |

**Áudio:** Trecho da faixa Suno (*O Legado*) — Intro → Verse 1 → Pre-Chorus → refrão parcial (ver `filmora/edit-notes.md`).

---

## Sinopse narrativa (6 cenas)

1. **Pressão** — Trabalhador brasileiro exausto no fim de um dia longo; ansiedade visível.
2. **Comparação** — Ele observa (celular / colegas) quem parece prosperar mais rápido; inveja contida.
3. **Fidelidade** — Retoma o trabalho com honestidade; gesto de “plantar o bem” (metáfora Sl 37:3).
4. **Pausa** — Momento de silêncio; reflete sobre o Salmo 37 (livro fechado / olhar contemplativo — sem texto legível no Veo).
5. **Transfiguração** — A luz muda: de fria/ansiosa para dourada; paz no rosto.
6. **Esperança** — Caminha em direção à luz matinal; abertura emocional alinhada a Sl 37:5.

**Versículo anchor (Filmora only):** *“Entrega o teu caminho ao Senhor; confia nele, e ele agirá.”* (Sl 37:5, NVI)

---

## Character sheet

**Fonte canônica:** [narrative/character.md](./narrative/character.md) (`character_id: char-rafael-legado`)

Resumo operacional: Rafael Santos, 32, auxiliar de logística em São Paulo — descriptor block EN e regras de continuidade no Character Engine.

Ver também `library/veo3/character-continuity.md`.

---

## Archetype e direção

| Campo | Valor |
|-------|-------|
| Archetype principal | `trust-surrender` |
| Archetypes secundários | Comparação (tensão verse), plantio (semente Sl 37) |
| Paleta | Atos 1–2: azul frio, cinza urbano · Atos 3–4: neutro · Atos 5–6: ouro, âmbar, roxo suave no céu |
| Mood | Cinematográfico, realista, emocional, brasileiro contemporâneo |
| Referência letra | Intro → V1 → Pre-Chorus → Chorus (parcial) |
| Referência Salmo | 37:1, 3, 5, 7 |

---

## Mapa de cenas

| # | Duração | Seção musical (Filmora) | Archetype | Objetivo dramático | Sl 37 |
|---|---------|-------------------------|-----------|-------------------|-------|
| 01 | 7 s | Intro / início V1 | trust-surrender | Estabelecer cansaço e pressão do dia a dia | v.1 — não te indignes |
| 02 | 8 s | Verse 1 | — | Mostrar comparação e inveja silenciosa | v.1–2 |
| 03 | 8 s | Verse 1 / Pre | trust-surrender | Fidelidade no trabalho honesto; plantar o bem | v.3 |
| 04 | 8 s | Bridge / ministração | trust-surrender | Pausa contemplativa; encontro com a Palavra | v.7 — descansa |
| 05 | 8 s | Pre-Chorus | trust-surrender | Mudança de luz: ansiedade → paz | v.5, 7 |
| 06 | 8 s | Chorus (hook) | trust-surrender | Esperança; entrega do caminho | v.5 |

**Duração bruta Veo:** ~47 s · **Com transições Filmora:** 45–60 s

Detalhes narrativos: [narrative/scenes.md](./narrative/scenes.md) · Timing: `storyboard.md` · Prompts export: `veo3-prompts.md` (derivado de [prompt-composition.md](./narrative/prompt-composition.md)).

---

## Conexão letra ↔ cena

| Cena | Linha / ideia da faixa |
|------|------------------------|
| 01 | *"Não esquenta a cabeça... Deixa o tempo mostrar..."* |
| 02 | *"Não te indigna por causa de quem faz o mal... A inveja é uma folha"* |
| 03 | *"Confia no Senhor, planta o bem na tua terra"* |
| 04 | *"Então silencia! Descansa no Senhor"* + ministração |
| 05 | *"O legado de paz vem da mão do Criador"* |
| 06 | *"Entrega o teu caminho, confia no Senhor! E o mais Ele fará!"* |

---

## Ordem de produção

1. [x] Narrative Pipeline completo (`video/narrative/`)
2. [x] Character sheet — Character Engine (`character.md`)
3. [x] 6 cenas com 17 campos cada (`scenes.md`)
4. [x] Prompts compostos via Prompt Composer (`prompt-composition.md`)
5. [x] Director commentary (`director-commentary.md`)
6. [ ] Gerar 2–3 takes por cena no AI Studio / Veo
7. [ ] Selecionar takes → `assets/video/veo3/scene-01.mp4` … `scene-06.mp4`
8. [ ] Montar no Filmora — `filmora/edit-notes.md`
9. [ ] Export reel 9:16 + SRT legendas

---

## Estimativa de geração

| Métrica | Valor |
|---------|-------|
| Cenas | 6 |
| Takes por cena | 3 |
| Total gerações Veo | 18 |
| Aspect ratio | **9:16** |
| Duração por clip | 6–8 s |
| Custo estimado | Consultar pricing Gemini/Vertex antes do batch |

---

## Log de geração

| Cena | Data | Método | Takes | Escolhido | Notas |
|------|------|--------|-------|-----------|-------|
| 01 | — | manual | — | — | — |
| 02 | — | manual | — | — | Evitar tela legível no celular |
| 03 | — | manual | — | — | — |
| 04 | — | manual | — | — | Livro sem texto legível |
| 05 | — | manual | — | — | Match de luz com cena 4 |
| 06 | — | manual | — | — | — |

---

## Integração Filmora

| Cena MP4 | Início reel | Fim reel | Transição | Áudio |
|----------|-------------|----------|-----------|-------|
| scene-01.mp4 | 0:00 | ~0:07 | fade in | Intro guitarra |
| scene-02.mp4 | ~0:07 | ~0:15 | cut | Verse 1 entra |
| scene-03.mp4 | ~0:15 | ~0:23 | cut | Verse continua |
| scene-04.mp4 | ~0:23 | ~0:31 | dissolve lento | Beat reduz / bridge |
| scene-05.mp4 | ~0:31 | ~0:39 | dissolve + lift | Pre-chorus |
| scene-06.mp4 | ~0:39 | ~0:55 | cut no drop | Chorus hook |

Ver `filmora/edit-notes.md` para versículo, legendas e mix.

---

## Pendências

| ID | Descrição | Responsável |
|----|-----------|-------------|
| P01 | Áudio master Suno ainda não registrado em `assets/audio/` | Produção |
| P02 | Validar continuidade facial entre takes Veo (gerar cenas em sequência) | Editor |
| P03 | Campanha `campaigns/campaign-track-01/` ainda não criada | Próxima fase |
| P04 | Post de letra e carrossel existem fora do repo — importar links quando disponível | Humano |

---

## Referências

- [narrative/](./narrative/) — **fonte principal (Narrative Engine)**
- [storyboard.md](./storyboard.md)
- [veo3-prompts.md](./veo3-prompts.md)
- [filmora/edit-notes.md](./filmora/edit-notes.md)
- [docs/API_VIDEO_AUTOMATION.md](../../../../../docs/API_VIDEO_AUTOMATION.md)
- [library/veo3/](../../../../../library/veo3/)
- [lyrics.md](../lyrics.md)
- [WORKFLOW.md § Workflow 9](../../../../../WORKFLOW.md)
