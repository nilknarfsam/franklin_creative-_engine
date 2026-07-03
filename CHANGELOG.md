# Changelog — Franklin Creative Engine

Todas as mudanças relevantes do projeto FCE são documentadas neste arquivo.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).
Versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/) para a **documentação e estrutura** do repositório (não confundir com versões de álbum ou faixa).

---

## [Unreleased]

### Planejado
- Regra Cursor `.cursor/rules/fce.mdc`
- Campanhas por faixa em `campaigns/campaign-track-XX/`
- Estudos bíblicos em `bible-studies/study-track-XX/`
- Biblioteca Suno/Canva em `library/` (além de veo3)
- Implementação scripts `scripts/video/generate_*.py` (Veo API)
- Primeiras gerações Suno e assets de áudio/vídeo
- Retrofit Narrative Engine para tracks 02–12
- Retrofit CDS para tracks 02–12

### Adicionado — FCE Launcher (interface conversacional)
- **FCE.md** — porta de entrada: menu 12 opções + regras universais
- **launcher/** — 11 playbooks de tarefa:
  - CREATE_INSTAGRAM_POST · CREATE_CAROUSEL · CREATE_HERO_ASSET
  - CREATE_STORY · CREATE_REEL · CREATE_SHORTS · CREATE_VIDEO_VEO
  - CREATE_CAPTION · CREATE_TRACK · CREATE_ALBUM · IMPROVE_SYSTEM
- **README.md** — FCE.md como porta de entrada
- **AGENTS.md v0.6.0** — ordem de leitura começa por FCE.md + launcher
- **WORKFLOW.md v0.6.0** — Launcher como camada de uso conversacional
- **PROJECT_STRUCTURE.md** — módulo `launcher/`

### Adicionado — Sprint 5.2: Hero Asset Workflow
- **Hero Asset Workflow** — etapa entre Design Specification e Produção dos Assets:
  - Hero Asset → Hero Review → Hero Approved → Asset Derivation
- **docs/PRODUCTION_PHILOSOPHY.md** — por que Hero primeiro, por que derivar, benefícios comprovados
- **WORKFLOW.md v0.5.0** — § Hero Asset Workflow + CDS2.5 + WF4 atualizado
- **AGENTS.md v0.5.0** — regras Hero, Hero Review Checklist (8 critérios)
- **PROJECT_STRUCTURE.md** — `assets/hero/`, `assets/hero/approved/`, `assets/exports/`
- **README.md** — seção Production Philosophy
- **Track 01** — Hero Asset APPROVED ✅ · `assets/hero/` documentado

### Adicionado — Track 01 CDS + assets P0 (produção Canva)
- **Track 01 — Creative Direction System aplicado** (`design/`):
  - `creative-brief.md` — brief estratégico 14 seções (Gate G1 approved)
  - `design-specification.md` — sistema visual 14 elementos + outline carrossel (Gate G2 approved)
  - `creative-review.md` — checklists G1+G2 aprovados; G4/G5 pendentes assets
  - `canva-brief.md` — atualizado para execução P0
- **Track 01 — Pacote produção visual P0** (`design/`):
  - `assets-p0-plan.md` — inventário post 4:5, carrossel, story, thumbnail
  - `carousel-production.md` — 6 slides devocionais spec Canva
  - `story-production.md` — 3 frames teaser 9:16
  - `thumbnail-production.md` — YouTube 1280×720

### Adicionado — Sprint 5.1: Track Identity (O Legado)
- **Track 01 — Identidade visual permanente** (`tracks/track-01-o-legado/identity/`):
  - `track_identity.md` — Creative DNA, Design/Photography/Color/Typography Language, Visual Symbols, Do Not Use, Moodboard Description, Brand Alignment
- **Track 01** — `README.md` da faixa como entrada e índice
- **Track 01** — `concept.md` e `design/canva-brief.md` linkam para identity

### Adicionado — Sprint 5: Creative Direction System
- **Creative Direction System (CDS)** — framework permanente em `library/creative_direction_system/`:
  - `README.md` — propósito, arquitetura e conexões (Narrative, Prompt, Design, Veo)
  - `01_creative_brief.md` — brief estratégico de nível agência + template
  - `02_design_specification.md` — 14 elementos de sistema visual + template
  - `03_creative_review.md` — gates G1–G5 e 6 checklists de aprovação
- **WORKFLOW.md § Creative Direction Pipeline** — obrigatório antes de design e campanha
- **PROJECT_STRUCTURE.md** — módulo `creative_direction_system/` + paths `design/creative-brief.md`, etc.
- **AGENTS.md v0.4.0** — CDS obrigatório para campanha/design; ordem de leitura atualizada
- **README.md** — estado Sprint 5

### Alterado — Sprint 5
- **Workflow 4 (Design)** — pré-requisito CDS G2; `canva-brief.md` derivado da design spec
- **Workflow 9 (Veo)** — pré-requisito CDS G1 além do Narrative Pipeline
- **Checklist nova faixa** — inclui documentos CDS em `design/`
- **Controle de qualidade** — CDS como gate antes de publicação

### Adicionado
- **Track 01 — Retrofit Narrative Engine** (`tracks/track-01-o-legado/video/narrative/`):
  - `hook.md` — hook tipo Conflito (Sl 37:1)
  - `character.md` — Rafael Santos via Character Engine
  - `scenes.md` — 6 cenas × 17 campos (Scene Builder)
  - `prompt-composition.md` — prompts compostos com linhagem documentada
  - `director-commentary.md` — comentário do diretor por cena
  - `narrative-manifest.yaml` — manifest conectando track, cenas, símbolos, emoções

### Alterado
- **Track 01** — `veo3-video-plan.md`, `storyboard.md`, `veo3-prompts.md` apontam para `video/narrative/` como fonte principal

### Adicionado — Sprint 4: Narrative Engine
- **Narrative Engine** — framework cinematográfico permanente em `library/narrative_engine/`:
  - `01_hook_engine.md` — psicologia dos 3 primeiros segundos
  - `02_character_engine.md` — construção de personagem + template
  - `03_scene_builder.md` — anatomia de cena (17 campos) + template
  - `04_emotion_engine.md` — 10 emoções × 7 dimensões cinematográficas
  - `05_symbol_library.md` — 12 símbolos bíblicos
  - `06_cinematography_library.md` — plano, lente, luz, composição, ritmo
  - `07_prompt_composer.md` — montagem obrigatória do Prompt Final
  - `08_director_commentary.md` — documentação do porquê por vídeo/cena
  - `README.md` — índice e pipeline do módulo
- **WORKFLOW.md § Narrative Pipeline** — obrigatório antes do Workflow 9 (Veo)
- **PROJECT_STRUCTURE.md** — módulo `narrative_engine/` + path `video/narrative/`
- **AGENTS.md v0.3.0** — Narrative Engine obrigatório; proíbe prompts Veo manuais

### Alterado — Sprint 4
- **Workflow 9** — pré-requisito Narrative Pipeline; Fase B valida prompts compostos
- **Ordem de leitura AGENTS** — `library/narrative_engine/` para tarefas de vídeo

### Adicionado — Sprint 3 (vídeo API prep)
- **Módulo de automação de vídeo (preparação)** — sem chamada real à API
  - `docs/API_VIDEO_AUTOMATION.md` — Gemini API vs Vertex AI, segurança, workflow manual/futuro
  - `library/veo3/` — `prompt-rules.md`, `camera-moves.md`, `character-continuity.md`, `scene-archetypes.md`
  - `templates/veo3-scene-template.md`, `veo3-video-plan-template.md`
  - `scripts/video/README.md`, `scripts/video/.env.example`
- **WORKFLOW.md § Workflow 9** — Geração de vídeo com Veo API
- **AGENTS.md** — regras de segurança Veo (keys, .env, 9:16, 6 elementos, no text)
- **`.gitignore`** — exceção `!.env.example` para templates de ambiente

---

## [0.2.0] — 2026-07-02

### Adicionado
- **Estrutura modular** `albums/album-04-o-trono-intocavel/` com `album.yaml`, `concept.md`, pastas `tracks/`, `campaigns/`, `bible-studies/`, `assets/`, `legal/`
- **12 faixas** em `tracks/track-01` … `track-12`, cada uma com:
  - `track.yaml`, `concept.md`, `lyrics.md`, `technical-sheet.md`
  - `suno/prompt.txt`, `suno/iterations/notes.md`
  - Stubs: `video/`, `design/`, `copy/`, `assets/`
- **`legal/dossie-direitos-autorais.md`** — cópia do dossiê monolítico (original preservado na raiz)
- **`legal/credits.md`** — créditos e registro Suno (template)
- **`legal/vibecore-alerts.md`** — alerta Track 03 documentado
- **Templates** em `templates/`:
  - `track-template.md`, `campaign-template.md`, `bible-study-template.md`
  - `suno-prompt-template.md`, `veo3-brief-template.md`, `canva-kit-brief.md`
- **`.gitignore`** — política para áudio, vídeo, imagens pesadas, Filmora, ambiente
- **`scripts/migrate_album_04.py`** — script de migração reutilizável

### Alterado
- Álbum 4 passa de dossiê monolítico para unidades modulares por faixa
- Track 03 marcada como `needs_review` (VibeCore Alert — sem alteração de letra)

### Notas
- Dossiê original na raiz **não removido**: `DOSSIÊ DE DIREITOS AUTORAIS_ ÁLBUM 4 - O TRONO INTOCÁVEL.md`
- Letras definitivas copiadas verbatim do dossiê (incluindo escapes markdown do source)
- Fase 1 do ROADMAP concluída (estrutura + templates + gitignore)

---

## [0.1.0] — 2026-07-02

### Adicionado
- **README.md** — Ponto de entrada do Franklin Creative Engine (FCE): missão, stack criativa, tipos de entrega, início rápido para humanos e agentes de IA
- **VISION.md** — Missão, visão 3–5 anos, identidade VibeCore, princípios teológicos e de produção, métricas de sucesso
- **ROADMAP.md** — Fases 0–5 com marcos, entregas do Álbum 4, biblioteca criativa, automação e distribuição
- **PROJECT_STRUCTURE.md** — Árvore de diretórios, convenções de nomenclatura, schemas `album.yaml` e `track.yaml`, política de assets
- **AGENTS.md** — Regras operacionais para ChatGPT, Cursor/Codex e demais agentes; contexto do Álbum 4; checklists de qualidade
- **WORKFLOW.md** — Oito pipelines: álbum, faixa, vídeo, design, copy, estudo bíblico, campanha e ministração
- **CHANGELOG.md** — Este arquivo

### Contexto
- Projeto iniciado como SO criativo para campanhas completas de música cristã
- Álbum de referência: **Álbum 4 — O Trono Intocável** (Salmos 37–48, 12 faixas)
- Dossiê de direitos autorais existente na raiz (migração prevista Fase 1)
- Pendência documentada: Track 03 (*O Sopro do Tempo*) — ajuste teológico na estrofe com referência a Eclesiastes

### Stack documentada
- ChatGPT, Cursor/Codex, Suno, Veo 3, Filmora Pro, Canva

---

## Histórico de versões — guia

| Versão | Significado |
|--------|-------------|
| **MAJOR** | Reestruturação radical (ex.: novo schema YAML, breaking change de paths) |
| **MINOR** | Novos módulos, templates, workflows ou fases concluídas do ROADMAP |
| **PATCH** | Correções, clarificações, typos em documentação |

---

## Registro por álbum (separado)

Versões de conteúdo musical não usam semver do repo. Registrar aqui como notas:

### Álbum 4 — O Trono Intocável

| Data | Evento |
|------|--------|
| — | Dossiê de direitos autorais com 12 faixas (letras definitivas + fichas técnicas) |
| — | VibeCore Alert: Track 03 pendente micro-refatoração |
| 2026-07-02 | Referenciado na fundação documental FCE v0.1.0 |
| 2026-07-02 | Estrutura modular migrada — FCE v0.2.0 |

---

## Como contribuir com entradas

Ao concluir trabalho significativo:

```markdown
## [X.Y.Z] — YYYY-MM-DD

### Adicionado
- ...

### Alterado
- ...

### Corrigido
- ...

### Removido
- ...
```

Mover itens de `[Unreleased]` para a nova versão datada.

---

[Unreleased]: https://github.com/franklin-creative-engine/fce/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/franklin-creative-engine/fce/releases/tag/v0.2.0
[0.1.0]: https://github.com/franklin-creative-engine/fce/releases/tag/v0.1.0
