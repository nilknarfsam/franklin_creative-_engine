# Estrutura do Projeto — Franklin Creative Engine

Este documento define a organização modular do repositório FCE. **Agentes de IA devem seguir estes paths e convenções** antes de criar, mover ou renomear arquivos.

---

## Visão geral da árvore

```
franklin_creative_engine/
│
├── README.md                    # Entrada do projeto
├── VISION.md                    # Missão e identidade
├── ROADMAP.md                   # Fases e marcos
├── PROJECT_STRUCTURE.md         # Este arquivo
├── AGENTS.md                    # Instruções para IAs
├── WORKFLOW.md                  # Pipelines de produção
├── CHANGELOG.md                 # Histórico de versões
│
├── albums/                      # Unidade principal: álbum
│   └── album-XX-{slug}/
│       ├── album.yaml           # Metadados do álbum
│       ├── concept.md           # Conceito macro e arco narrativo
│       ├── tracks/              # Faixas numeradas
│       ├── campaigns/           # Campanhas por faixa ou álbum
│       ├── bible-studies/       # Estudos derivados
│       ├── assets/              # Binários (gitignored parcialmente)
│       └── legal/               # Dossiês e direitos autorais
│
├── templates/                   # Modelos reutilizáveis
├── library/                     # Biblioteca criativa (prompts, estilos)
├── scripts/                     # Automações (futuro)
└── docs/                        # Documentação expandida (futuro)
```

---

## Convenções de nomenclatura

### Slugs

| Tipo | Padrão | Exemplo |
|------|--------|---------|
| Álbum | `album-{NN}-{slug-kebab}` | `album-04-o-trono-intocavel` |
| Faixa | `track-{NN}-{slug-kebab}` | `track-01-o-legado` |
| Campanha | `campaign-track-{NN}` ou `campaign-album-launch` | `campaign-track-01` |
| Estudo | `study-track-{NN}-{slug}` | `study-track-01-salmo-37` |

- **NN** = número com zero à esquerda (01, 02, … 12)
- **slug-kebab** = minúsculas, hífens, sem acentos
- Títulos display ficam em YAML ou frontmatter, não no nome do arquivo

### Idioma

- **Documentação técnica:** Português Brasileiro
- **Suno prompts:** Inglês (padrão Suno) + tag `Brazilian Portuguese vocals`
- **Nomes de pasta:** inglês ou português sem acento — preferir inglês para compatibilidade

---

## Módulo: Álbum (`albums/`)

### `album.yaml` — schema

```yaml
id: album-04
number: 4
title: "O Trono Intocável"
slug: o-trono-intocavel
scripture_range: "Salmos 37-48"
track_count: 12
status: in_production          # concept | in_production | released
vibe_core:
  - trap-acustico
  - pop-teatral
  - cinematic-trap-rock
  - arena-anthem
language: pt-BR
created: 2026-01-01
updated: 2026-07-02
```

### `concept.md`

Contém:
- Tese do álbum (ex.: "O Trono Intocável" como fio condutor)
- Arco emocional das 12 faixas
- Referências visuais e sonoras
- Conexão teológica entre Salmos

### `legal/`

| Arquivo | Conteúdo |
|---------|----------|
| `dossie-direitos-autorais.md` | Letras definitivas, fichas, pendências |
| `credits.md` | Autores, ferramentas, datas de geração Suno |
| `vibecore-alerts.md` | Pendências teológicas ou de fidelidade bíblica |

---

## Módulo: Faixa (`tracks/track-XX-{slug}/`)

Cada faixa é uma **unidade autônoma** com metadados e assets.

```
track-01-o-legado/
├── track.yaml              # Metadados machine-readable
├── concept.md              # Resumo / conceito de criação
├── lyrics.md               # Letra definitiva com tags Suno
├── technical-sheet.md      # Ficha técnica (vibe, tempo, ministração)
├── suno/
│   ├── prompt.txt          # Prompt principal
│   └── iterations/         # Variantes testadas (notas)
├── video/
│   ├── veo3-brief.md
│   ├── veo3-video-plan.md
│   ├── veo3-prompts.md
│   ├── storyboard.md
│   ├── narrative/              # Narrative Engine (obrigatório antes de prompts Veo)
│   │   ├── hook.md
│   │   ├── character-{slug}.md
│   │   ├── scenes/scene-{NN}.md
│   │   └── director-commentary.md
│   └── filmora/
│       └── edit-notes.md   # Notas de montagem
├── design/
│   ├── creative-brief.md           # CDS 01 — brief estratégico
│   ├── design-specification.md     # CDS 02 — sistema visual
│   ├── creative-review.md          # CDS 03 — aprovações
│   └── canva-brief.md              # Brief operacional Canva (derivado)
├── copy/
│   ├── captions.md         # Legendas por plataforma
│   └── posts.md            # Copy de posts
└── assets/                 # Áudio, vídeo, imagens (ver gitignore)
    ├── audio/
    ├── video/
    └── images/
```

### `track.yaml` — schema

```yaml
id: track-01
album_id: album-04
number: 1
title: "O Legado"
slug: o-legado
scripture: "Salmo 37"
scripture_ref: "Sl 37"
duration_estimate: "4:30-5:00"
vibe: "Trap Acústico & Pop Teatral"
ministration: true
ministration_notes: "Oração falada no meio — clima confessional"
suno_prompt: "Acoustic guitar pluck, smooth trap beat..."
status: lyrics_final          # concept | lyrics_draft | lyrics_final | audio | video | published
vibecore_alerts: []
updated: 2026-07-02
```

### `lyrics.md` — formato obrigatório

```markdown
# O Legado — Letra Definitiva

**Idioma:** Português Brasileiro  
**Referência:** Salmo 37  
**Status:** final | draft | needs_review

---

[Language: Brazilian Portuguese]

[Intro - Intimate acoustic guitar pluck, no beat, Clean Soft Vocal]
Texto da intro...

[Verse 1 - Smooth trap beat enters, poetic rap flow]
Texto...
```

**Regras de tags Suno:**
- Colchetes `[Section - production notes, Vocal type]`
- Call-and-response entre parênteses: `(Não te indigna!)`
- Marcar `[End]` no encerramento
- Indicar tipo vocal: Clean Soft, Powerful Theatrical, Aggressive, etc.

---

## Módulo: Campanha (`campaigns/`)

```
campaigns/
├── campaign-album-launch/
│   ├── calendar.md           # Calendário editorial
│   ├── funnel.md               # Pré-lançamento → lançamento → pós
│   └── assets-checklist.md
└── campaign-track-01/
    ├── calendar.md
    ├── hooks.md                # Frases de abertura para reels
    ├── hashtags.md
    └── platforms/
        ├── instagram.md
        ├── tiktok.md
        └── youtube.md
```

---

## Módulo: Estudo bíblico (`bible-studies/`)

```
bible-studies/
└── study-track-01-salmo-37/
    ├── study.md                # Conteúdo principal
    ├── discussion-guide.md     # Perguntas para célula
    └── carousel-outline.md     # Roteiro slide a slide para Canva
```

---

## Módulo: Templates (`templates/`)

Arquivos `.md` com placeholders `{{VAR}}` ou seções `[PREENCHER]`.

| Template | Uso |
|----------|-----|
| `track-template.md` | Nova faixa |
| `campaign-template.md` | Campanha de lançamento |
| `bible-study-template.md` | Estudo derivado |
| `suno-prompt-template.md` | Iteração Suno |
| `veo3-brief-template.md` | Produção de vídeo IA |
| `canva-kit-brief.md` | Design visual |

**Regra:** Copiar template → preencher → salvar no path do módulo correspondente. Nunca editar o template original.

---

## Módulo: Narrative Engine (`library/narrative_engine/`)

**Framework cinematográfico permanente.** Não gera vídeo — ensina agentes a pensar como diretor de cinema.

| Arquivo | Função |
|---------|--------|
| `01_hook_engine.md` | Primeiros 3 segundos |
| `02_character_engine.md` | Fichas de personagem |
| `03_scene_builder.md` | Anatomia de cena + template |
| `04_emotion_engine.md` | Emoção → câmera/luz/cor/ritmo |
| `05_symbol_library.md` | Símbolos bíblicos |
| `06_cinematography_library.md` | Plano, lente, luz, composição |
| `07_prompt_composer.md` | Montagem do Prompt Final |
| `08_director_commentary.md` | Documentação do porquê |

**Regra FCE:** Todo vídeo passa pelo Narrative Pipeline (WORKFLOW.md) **antes** de `veo3-prompts.md` ou geração Veo.

**Output por faixa:** `tracks/.../video/narrative/`

---

## Módulo: Creative Direction System (`library/creative_direction_system/`)

**Framework permanente de direção criativa estratégica.** Não gera imagens nem vídeos — define como uma campanha deve ser pensada antes da execução.

| Arquivo | Função |
|---------|--------|
| `01_creative_brief.md` | Brief estratégico de nível agência |
| `02_design_specification.md` | Brief → especificações visuais sistemáticas |
| `03_creative_review.md` | Aprovação, checklists e gates de qualidade |

**Regra FCE:** CDS aprovado (G1–G2) **antes** de design executável (Canva) e **antes** do Narrative Pipeline (vídeo).

**Output por faixa:** `tracks/.../design/creative-brief.md`, `design-specification.md`, `creative-review.md`

---

## Módulo: Biblioteca (`library/`)

Conteúdo **curado e versionado**, não rascunhos de projeto.

```
library/
├── suno/
│   ├── vibes/
│   │   ├── dark-trap.md
│   │   ├── arena-rock.md
│   │   └── festive-trap-pop.md
│   └── vocal-tags.md
├── veo3/
│   ├── prompt-rules.md
│   ├── camera-moves.md
│   ├── character-continuity.md
│   └── scene-archetypes.md
├── narrative_engine/          # Framework cinematográfico (OBRIGATÓRIO antes de Veo)
│   ├── README.md
│   ├── 01_hook_engine.md
│   ├── 02_character_engine.md
│   ├── 03_scene_builder.md
│   ├── 04_emotion_engine.md
│   ├── 05_symbol_library.md
│   ├── 06_cinematography_library.md
│   ├── 07_prompt_composer.md
│   └── 08_director_commentary.md
├── creative_direction_system/ # Framework de direção criativa (OBRIGATÓRIO antes de campanha)
│   ├── README.md
│   ├── 01_creative_brief.md
│   ├── 02_design_specification.md
│   └── 03_creative_review.md
├── canva/
│   └── album-04-brand.md
├── copy/
│   ├── hooks-christian-ptbr.md
│   └── cta-library.md
└── theology/
    └── salmos-notas-exegeticas.md
```

---

## Módulo: Assets binários

### Política de versionamento

| Tipo | Git | Storage alternativo |
|------|-----|---------------------|
| `.md`, `.yaml`, `.txt` | ✅ Versionado | — |
| `.wav`, `.mp3`, `.mp4` | ❌ Gitignore | Drive / NAS / LFS futuro |
| `.png`, `.jpg`, `.psd` | ❌ Gitignore (exceto docs) | Canva / Drive |
| `.prj`, projetos Filmora | ❌ Gitignore | Local + backup |

### `.gitignore` recomendado (Fase 1)

```
# Audio / Video
*.wav
*.mp3
*.flac
*.mp4
*.mov

# Design sources
*.psd
*.aep

# Filmora
*.wfp
*.filmora

# OS
.DS_Store
Thumbs.db

# Env
.env
```

Paths de assets **devem ser referenciados** em markdown mesmo quando binários estão fora do git:

```markdown
**Áudio master:** `assets/audio/track-01-o-legado-master.wav` (local)
```

---

## Migração do estado atual

| Arquivo existente | Destino previsto |
|-------------------|------------------|
| `DOSSIÊ DE DIREITOS AUTORAIS_ ÁLBUM 4 - O TRONO INTOCÁVEL.md` | `albums/album-04-o-trono-intocavel/legal/dossie-direitos-autorais.md` |

**Ação Fase 1:** Split do dossiê monolítico em 12 pastas `tracks/` + `album.yaml`.

---

## Links cruzados

Todo documento de faixa deve linkar:

- `albums/{album}/concept.md`
- Estudo bíblico correspondente em `bible-studies/`
- Campanha em `campaigns/campaign-track-{NN}/`

Formato de link relativo:

```markdown
Ver também: [Campanha Track 01](../campaigns/campaign-track-01/calendar.md)
```

---

## Expansão futura

Para adicionar um novo módulo:

1. Documentar path e schema aqui
2. Adicionar template em `templates/` se aplicável
3. Atualizar AGENTS.md com regras do módulo
4. Registrar em CHANGELOG.md

Módulos candidatos: `podcasts/`, `merch/`, `live-performance/`, `translations/`.

---

## Checklist para nova faixa

- [ ] Pasta `tracks/track-XX-{slug}/` criada
- [ ] `track.yaml` preenchido
- [ ] `lyrics.md` com tags Suno completas
- [ ] `technical-sheet.md` com vibe, tempo, ministração
- [ ] `suno/prompt.txt` exportado
- [ ] CDS: `design/creative-brief.md` + `design-specification.md` + `creative-review.md`
- [ ] Links para campanha e estudo bíblico
- [ ] Entrada no CHANGELOG se alteração estrutural
