# Workflow — Franklin Creative Engine

Pipelines de produção ponta a ponta. Cada workflow indica **ferramenta principal**, **input**, **output** e **path no repositório**.

---

## Mapa de workflows

```
                    ┌─────────────────┐
                    │  Estudo Bíblico │
                    │    (ChatGPT)    │
                    └────────┬────────┘
                             │
┌──────────────┐    ┌────────▼────────┐    ┌──────────────┐
│   Conceito   │───►│  Letra + Ficha  │───►│     Suno     │
│  (ChatGPT)   │    │ (ChatGPT/Cursor)│    │   (Áudio)    │
└──────────────┘    └────────┬────────┘    └──────┬───────┘
                             │                     │
                    ┌────────▼────────┐    ┌────────▼───────┐
                    │ Estudo + Copy   │    │ Veo 3 + Filmora│
                    │   (ChatGPT)     │    │    (Vídeo)     │
                    └────────┬────────┘    └───────┬────────┘
                             │                     │
                    ┌────────▼─────────────────────▼────────┐
                    │           Canva (Visual)              │
                    └────────────────────┬────────────────────┘
                                         │
                    ┌────────────────────▼────────────────────┐
                    │     Campanha + Publicação (Multi)       │
                    └─────────────────────────────────────────┘
```

---

## Workflow 1 — Álbum completo

**Objetivo:** Definir visão macro antes de qualquer faixa.

| Etapa | Ferramenta | Output | Path |
|-------|------------|--------|------|
| 1. Tese do álbum | ChatGPT | `concept.md` | `albums/album-XX/concept.md` |
| 2. Tracklist + Salmos | ChatGPT | `album.yaml` | `albums/album-XX/album.yaml` |
| 3. Arco narrativo | ChatGPT | Seção em `concept.md` | — |
| 4. Identidade visual | ChatGPT → Canva | `library/canva/album-XX-brand.md` | `library/canva/` |
| 5. Dossiê legal | Cursor | `legal/dossie-direitos-autorais.md` | `albums/.../legal/` |

**Gate de qualidade:** Concept aprovado antes de iniciar Workflow 2 em lote.

---

## Workflow 2 — Faixa (letra + áudio)

**Objetivo:** Uma faixa do conceito ao áudio master pronto para vídeo.

### Fase A — Conceito e exegese

| Etapa | Ação | Ferramenta |
|-------|------|------------|
| A1 | Ler Salmo/passagem na íntegra | ChatGPT + Bíblia |
| A2 | Definir conceito de criação (1 parágrafo) | ChatGPT |
| A3 | Escolher Vibe Geral alinhada ao VibeCore | ChatGPT |
| A4 | Decidir ministração (sim/não + momento) | Humano + ChatGPT |

**Output:** `tracks/track-XX/concept.md`

### Fase B — Letra definitiva

| Etapa | Ação | Ferramenta |
|-------|------|------------|
| B1 | Rascunho poético fiel ao texto bíblico | ChatGPT |
| B2 | Estruturar seções (Intro, V1, Pre, Chorus, V2, Bridge, Outro) | ChatGPT |
| B3 | Inserir tags Suno e indicações vocais | Cursor |
| B4 | Adicionar call-and-response no refrão | ChatGPT |
| B5 | Auditoria teológica (VibeCore Alert se necessário) | Humano |
| B6 | Marcar `status: lyrics_final` | Cursor |

**Output:** `tracks/track-XX/lyrics.md`

**Padrão de dinâmica FCE:**
- Intro íntima → beat entra → pre-chorus tension → **chorus explosion** → verse 2 → repeat → bridge breakdown → outro epic

### Fase C — Ficha técnica e Suno

| Etapa | Ação | Ferramenta |
|-------|------|------------|
| C1 | Preencher vibe, tempo, ministração | Cursor |
| C2 | Escrever Suno prompt (inglês) | ChatGPT |
| C3 | Colar letra tagged no Suno | Suno |
| C4 | Iterar 3–10 gerações | Suno |
| C5 | Documentar melhor take + ajustes desejados | Humano → `suno/iterations/notes.md` |
| C6 | Export WAV/MP3 master | Suno + pós opcional |

**Output:** `technical-sheet.md`, `suno/prompt.txt`, `assets/audio/`

**Exemplo Suno prompt (Track 01):**
```
Acoustic guitar pluck, smooth trap beat, poetic rap flow,
theatrical pop-rock chorus, melodic hooks, massive dynamic shifts,
Brazilian Portuguese vocals
```

### Fase D — Dossiê e direitos

| Etapa | Ação | Ferramenta |
|-------|------|------------|
| D1 | Consolidar letra + ficha no dossiê do álbum | Cursor |
| D2 | Registrar créditos e data | Cursor → `legal/credits.md` |

---

## Workflow 3 — Vídeo

**Objetivo:** Lyric video, clip teatral ou reel a partir do áudio master.

### Fase A — Planejamento

| Etapa | Ação | Output |
|-------|------|--------|
| A1 | Definir formato (16:9 clip, 9:16 reel, lyric kinetic) | `video/storyboard.md` |
| A2 | Escrever brief de cenas Veo 3 | `video/veo3-brief.md` |
| A3 | Listar B-roll vs performance vs tipografia | Storyboard |

**Direção visual por vibe:**

| Vibe | Paleta / mood Veo 3 |
|------|---------------------|
| Dark Trap | Chuva, piano solitário, sombras, close emocional |
| Arena Rock | Multidão, luzes, montanhas, epic wide shots |
| Festivo | Palmas, cores quentes, movimento, brass visual |
| Power Ballad | Cervo/água, névoa, strings visuais, golden hour |

### Fase B — Geração Veo 3

| Etapa | Ação | Ferramenta |
|-------|------|------------|
| B1 | Gerar cenas 5–8s por prompt | Veo 3 |
| B2 | Selecionar takes coerentes com storyboard | Humano |
| B3 | Salvar em `assets/video/veo3/` | Local |

**Prompt Veo 3 — template:**
```
Cinematic biblical metaphor, [cena específica], dramatic lighting,
theatrical mood, [cor dominante], slow camera push-in,
4K, no text, contemporary Christian aesthetic, not cheesy
```

### Fase C — Montagem Filmora Pro

| Etapa | Ação | Ferramenta |
|-------|------|------------|
| C1 | Import áudio master + clips Veo 3 | Filmora |
| C2 | Sync cortes com dinâmica da faixa (explosão no chorus) | Filmora |
| C3 | Lyric text kinetic nos refrões (opcional) | Filmora |
| C4 | Color grade unificado | Filmora |
| C5 | Export 16:9 + 9:16 + legendas SRT | Filmora |
| C6 | Documentar decisões | `video/filmora/edit-notes.md` |

**Outputs:**
- `assets/video/track-XX-clip-16x9.mp4`
- `assets/video/track-XX-reel-9x16.mp4`
- `assets/video/track-XX-lyrics.srt`

---

## Workflow 4 — Design (Canva)

**Objetivo:** Capas, carrosséis devocionais, stories, thumbnails.

### Fase A — Brief

| Campo | Conteúdo |
|-------|----------|
| Faixa / álbum | Título + número |
| Versículo anchor | Ex.: Sl 37:5 |
| Mood visual | Dark / Epic / Festive |
| Elementos | Trono, montanhas, etc. |
| Formatos | 1080×1080, 1080×1920, 1280×720 |

**Output:** `design/canva-brief.md`

### Fase B — Produção Canva

| Asset | Slides / specs | Uso |
|-------|----------------|-----|
| Capa de faixa | 1 | Spotify, YouTube |
| Carrossel devocional | 5–10 | Instagram |
| Story teaser | 1–3 | IG/TikTok |
| Thumbnail | 1 | YouTube |

**Output:** Export PNG → `assets/images/` + link Canva no brief

---

## Workflow 5 — Copy e legendas

**Objetivo:** Textos prontos para publicação por plataforma.

| Etapa | Ação | Ferramenta | Output |
|-------|------|------------|--------|
| 1 | Hook (primeira linha do post) | ChatGPT | `copy/posts.md` |
| 2 | Legenda longa IG | ChatGPT | `copy/captions.md` |
| 3 | Legenda curta TikTok | ChatGPT | `platforms/tiktok.md` |
| 4 | Descrição YouTube + timestamps | ChatGPT | `platforms/youtube.md` |
| 5 | Hashtags BR cristãs | ChatGPT | `hashtags.md` |

**Tom FCE:** Teatral, autêntico, bíblico, sem clickbait secular.

**Estrutura legenda IG:**
```
[Hook — linha do refrão ou pergunta devocional]

[2-3 frases de contexto do Salmo]

[CTA — ouça / compartilhe / comente Amém]

[Hashtags]
```

---

## Workflow 6 — Estudo bíblico

**Objetivo:** Material devocional derivado da faixa para células e carrosséis.

| Etapa | Ação | Ferramenta | Output |
|-------|------|------------|--------|
| 1 | Contexto histórico do Salmo | ChatGPT | `study.md` §1 |
| 2 | Versículos-chave (NVI ou ARA) | ChatGPT | `study.md` §2 |
| 3 | Conexão com a letra da faixa | ChatGPT | `study.md` §3 |
| 4 | Aplicação prática (3 pontos) | ChatGPT | `study.md` §4 |
| 5 | Perguntas de discussão | ChatGPT | `discussion-guide.md` |
| 6 | Outline carrossel | ChatGPT | `carousel-outline.md` |

**Gate:** Estudo revisado por humano antes de publicar como ensino.

---

## Workflow 7 — Campanha de lançamento

**Objetivo:** Orquestrar todos os assets em calendário editorial.

### Timeline tipo — lançamento de faixa (7 dias)

| Dia | Tipo | Conteúdo | Formato |
|-----|------|----------|---------|
| D-3 | Teaser | Trecho 15s refrão | Reel 9:16 |
| D-2 | Devocional | Carrossel Salmo | IG carousel |
| D-1 | Behind | Suno prompt / storyboard | Story |
| D0 | Launch | Clip completo + post | YT + IG |
| D+1 | Estudo | Link carrossel + legenda | IG |
| D+2 | Lyric | Trecho com letra on screen | Reel |
| D+3 | CTA | "Qual versículo te tocou?" | Story poll |

**Output:** `campaigns/campaign-track-XX/calendar.md`

### Checklist de assets antes do D0

- [ ] Áudio master
- [ ] Clip 16:9
- [ ] Reel 9:16
- [ ] Capa Canva
- [ ] Carrossel devocional
- [ ] Legendas todas plataformas
- [ ] Estudo bíblico publicável

---

## Workflow 8 — Roteiro de ministração

**Objetivo:** Texto falado para inserção na faixa ou vídeo ao vivo.

| Etapa | Ação | Output |
|-------|------|--------|
| 1 | Identificar momento (bridge, intro, outro) | `technical-sheet.md` |
| 2 | Escrever 30–90s de fala | `scripts/ministration.md` |
| 3 | Tom: confessional, teatral, íntimo | — |
| 4 | Gravar ou gerar TTS (futuro) | `assets/audio/ministration.wav` |

**Exemplo de uso:** Track 01 — oração falada no bridge; Track 10 — "Aquietai-vos" no Salmo 46.

---

## Narrative Pipeline — Direção cinematográfica (obrigatório)

**Objetivo:** Pensar como diretor de cinema **antes** de qualquer prompt Veo. Não gera vídeo.

**Documentação:** [library/narrative_engine/README.md](./library/narrative_engine/README.md)

```
Hook → Character → Scene(s) → Emotion → Symbol → Cinematography → Prompt Composer → Director Commentary
                                                                              ↓
                                                                    Workflow 9 (Veo)
```

### Fase N1 — Hook (3 segundos)

| Etapa | Ação | Output | Módulo |
|-------|------|--------|--------|
| N1.1 | Analisar faixa, emoção, plataforma | Decisão de hook | `01_hook_engine.md` |
| N1.2 | Documentar tipo + justificativa | `video/narrative/hook.md` | Template em hook_engine |

**Gate:** Hook definido antes do personagem.

### Fase N2 — Personagem

| Etapa | Ação | Output | Módulo |
|-------|------|--------|--------|
| N2.1 | Construir pessoa (não só rosto) | Character sheet completo | `02_character_engine.md` |
| N2.2 | Definir tratamento de câmera | Seção cinematografia do personagem | |

**Output:** `video/narrative/character-{slug}.md`

### Fase N3 — Cenas

| Etapa | Ação | Output | Módulo |
|-------|------|--------|--------|
| N3.1 | Definir número de cenas e atos | Arco documentado | `03_scene_builder.md` |
| N3.2 | Por cena: 17 campos obrigatórios | `video/narrative/scenes/scene-NN.md` | |
| N3.3 | Atribuir emoção + símbolo + versículo | Cross-ref 04 + 05 | |

**Gate:** Nenhum campo vazio antes do Composer.

### Fase N4 — Composição e documentação

| Etapa | Ação | Output | Módulo |
|-------|------|--------|--------|
| N4.1 | Aplicar Emotion + Cinematography | Blocos nas cenas | `04`, `06` |
| N4.2 | **Compor** Prompt Final (nunca manual) | Campo em cada scene-NN.md | `07_prompt_composer.md` |
| N4.3 | Consolidar prompts | `video/veo3-prompts.md` | |
| N4.4 | Escrever comentário do diretor | `video/narrative/director-commentary.md` | `08_director_commentary.md` |
| N4.5 | Validar | `library/veo3/prompt-rules.md` | |

**Gate:** Director commentary completo antes de Workflow 9 Fase C (geração Veo).

### Fase N5 — Storyboard e plano operacional

| Etapa | Ação | Output |
|-------|------|--------|
| N5.1 | Traduzir cenas em timing | `video/storyboard.md` |
| N5.2 | Plano de produção | `video/veo3-video-plan.md` |
| N5.3 | Notas de montagem | `video/filmora/edit-notes.md` |

### Checklist Narrative Pipeline

- [ ] `hook.md` com tipo e justificativa
- [ ] Character sheet completo (todos os campos)
- [ ] Cada cena com 17 campos + versículo + símbolo
- [ ] Prompts **compostos** via Prompt Composer
- [ ] `director-commentary.md` por cena respondido
- [ ] Nenhum texto no prompt Veo (legendas = Filmora)

---

## Workflow 9 — Geração de vídeo com Veo API

**Objetivo:** Planejar, promptar e gerar cenas Veo (manual hoje; script futuro) com segurança e prioridade **9:16** para social.

**Pré-requisito:** **Narrative Pipeline concluído** (prompts compostos + director commentary).

**Documentação principal:** [docs/API_VIDEO_AUTOMATION.md](./docs/API_VIDEO_AUTOMATION.md)

### Fase A — Planejamento

| Etapa | Ação | Output | Ferramenta |
|-------|------|--------|------------|
| A0 | Verificar Narrative Pipeline completo | Checklist OK | Cursor |
| A1 | Ler `track.yaml`, `concept.md`, `video/narrative/` | Contexto | Cursor / ChatGPT |
| A2 | Confirmar `veo3-video-plan.md` e `storyboard.md` | Plano operacional | Cursor |
| A3 | Revisar prompts em `veo3-prompts.md` (compostos) | Prompts validados | Cursor |

**Gate:** Narrative Pipeline + plano aprovado antes de gerar.

### Fase B — Prompts por cena

| Etapa | Ação | Output | Ferramenta |
|-------|------|--------|------------|
| B1 | Ler prompts de `video/narrative/scenes/` ou `veo3-prompts.md` | **Não reescrever** | Cursor |
| B2 | Validar regras Veo | `library/veo3/prompt-rules.md` | Cursor |
| B3 | Validar continuidade | `library/veo3/character-continuity.md` | Cursor |
| B4 | Confirmar `no text` + **9:16** | Checklist | Humano / Agente |

**Regra FCE:** Prompts em inglês. Sem texto legível no vídeo (legendas ficam no Filmora).

### Fase C — Geração (manual — hoje)

| Etapa | Ação | Ferramenta |
|-------|------|------------|
| C1 | Configurar `.env` local a partir de `scripts/video/.env.example` | Humano |
| C2 | Colar prompt no Google AI Studio ou Vertex console | Gemini / Vertex |
| C3 | Aspect ratio: **9:16** | UI da API |
| C4 | Gerar 2–3 takes por cena | Veo |
| C5 | Baixar MP4 → `assets/video/veo3/scene-NN.mp4` | Local |
| C6 | Registrar take escolhido no plano / scene md | Cursor |

### Fase D — Geração (semiautomática — futuro)

| Etapa | Ação | Ferramenta |
|-------|------|------------|
| D1 | `cp scripts/video/.env.example scripts/video/.env` | Shell |
| D2 | `python generate_scene.py --track ... --scene NN` | Script (futuro) |
| D3 | Ou batch: `python generate_video_plan.py --track ...` | Script (futuro) |
| D4 | Verificar `generation-log.json` (sem secrets) | Humano |

> Scripts ainda **não implementados** — ver `scripts/video/README.md`.

### Fase E — Montagem e publicação

| Etapa | Ação | Output |
|-------|------|--------|
| E1 | Import cenas + áudio Suno | Filmora |
| E2 | Sync cortes com chorus/bridge | `filmora/edit-notes.md` |
| E3 | Legendas PT-BR (burn-in opcional) | SRT / Filmora |
| E4 | Export **9:16** reel + 16:9 opcional | `assets/video/` |
| E5 | Publicar via Workflow 7 (campanha) | Calendário |

### Checklist Workflow 9

- [ ] Character sheet definido
- [ ] Cada cena com 6 elementos documentados
- [ ] Prompts com `no text` e `9:16`
- [ ] MP4s em `assets/video/veo3/` (gitignored)
- [ ] Nenhum secret no repositório
- [ ] Log de takes no plano de vídeo

### Paths

| Recurso | Path |
|---------|------|
| Doc API | `docs/API_VIDEO_AUTOMATION.md` |
| Library | `library/veo3/` |
| Templates | `templates/veo3-scene-template.md`, `veo3-video-plan-template.md` |
| Scripts | `scripts/video/` |
| Output | `tracks/.../assets/video/veo3/` |

---

## Matriz ferramenta × entrega

| Entrega | ChatGPT | Cursor | Suno | Veo 3 | Filmora | Canva |
|---------|---------|--------|------|-------|---------|-------|
| Conceito álbum | ● | ○ | — | — | — | ○ |
| Letra + tags | ● | ● | — | — | — | — |
| Áudio | ○ | ○ | ● | — | ○ | — |
| Storyboard | ● | ○ | — | ○ | — | — |
| Clipes IA | ○ | — | — | ● | — | — |
| Montagem final | — | — | — | — | ● | — |
| Carrosséis | ● | — | — | — | — | ● |
| Legendas | ● | ○ | — | — | ● | — |
| Estudo bíblico | ● | ○ | — | — | — | ○ |
| Campanha | ● | ● | — | — | — | ○ |
| Docs / YAML | ○ | ● | — | — | — | — |

● = principal · ○ = suporte · — = não aplicável

---

## Workflow rápido — "Só preciso de X"

| Pedido | Workflow | Tempo estimado |
|--------|----------|----------------|
| Letra nova | WF2 Fase A–B | 2–4 h |
| Suno prompt | WF2 Fase C1–C2 | 30 min |
| Reel de lançamento | WF3 + WF5 ou WF9 | 4–8 h |
| Veo — direção narrativa | Narrative Pipeline | 2–4 h |
| Veo — plano + prompts | Narrative Pipeline N4 | 1–2 h |
| Veo — geração manual | WF9 Fase C | 2–4 h |
| Carrossel devocional | WF6 + WF4 | 2–3 h |
| Estudo para célula | WF6 | 1–2 h |
| Campanha 7 dias | WF7 | 1 h (planejamento) |

*Tiempos assumem humano + IA; geração Suno/Veo pode adicionar iterações.*

---

## Controle de qualidade final

Antes de marcar faixa como `published`:

1. **Teologia** — VibeCore Alerts zerados
2. **Áudio** — Master sem clipping; dinâmica coerente com letra
3. **Vídeo** — Cortes no beat; legendas corretas
4. **Visual** — Brand do álbum consistente
5. **Copy** — Versículos citados corretamente
6. **Legal** — Entrada no dossiê de direitos autorais
7. **CHANGELOG** — Versão registrada

---

## Evolução dos workflows

Novos workflows (podcast, live worship, merch) serão adicionados como seções numeradas.

Alterações de pipeline → atualizar CHANGELOG.md + notificar em AGENTS.md se regras mudarem.

**Versão:** 0.3.0 — 2026-07-02 (Narrative Engine Sprint 4)
