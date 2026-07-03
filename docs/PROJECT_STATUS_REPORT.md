# Project Status Report — Franklin Creative Engine

**Gerado em:** 2026-07-02  
**Versão do repositório (docs):** 0.4.0 (Sprint 5) + Sprint 5.1 local não commitada  
**Álbum ativo:** 04 — *O Trono Intocável* (Salmos 37–48)

---

## 1. Visão geral do projeto

O **Franklin Creative Engine (FCE)** é um sistema operacional criativo com IA para produção de campanhas completas de músicas cristãs. Não é apenas um repositório de letras — é uma **infraestrutura documentada** que orquestra conceito teológico, letra, áudio (Suno), vídeo (Veo + Filmora), design (Canva), copy e campanhas.

| Campo | Valor |
|-------|-------|
| Domínio | Produção criativa cristã — VibeCore (trap + teatral + arena) |
| Idioma de conteúdo | PT-BR |
| Projeto de referência | Álbum 4 — *O Trono Intocável* — 12 faixas |
| Estado macro | Fundação ✅ · Estrutura modular ✅ · Engines ✅ · Produção de assets 📋 |

### Stack criativa

| Camada | Ferramenta / Módulo |
|--------|---------------------|
| Ideação / copy | ChatGPT |
| Engenharia / docs | Cursor / Codex |
| Áudio | Suno |
| Direção criativa | CDS (`library/creative_direction_system/`) |
| Direção cinematográfica | Narrative Engine (`library/narrative_engine/`) |
| Vídeo IA | Veo 3 + Video Engine (`library/veo3/`) |
| Montagem | Filmora Pro |
| Design | Canva |

### Engines permanentes (biblioteca)

```
Música → CDS (estratégia) → ┬ Narrative Engine → Prompt Composer → Video Engine (Veo)
                            ├ Design (Canva)
                            └ Copy / Campanha
```

---

## 2. Árvore da arquitetura atual (4 níveis)

```
franklin_creative_engine/
├── README.md · VISION.md · ROADMAP.md · PROJECT_STRUCTURE.md
├── AGENTS.md · WORKFLOW.md · CHANGELOG.md · .gitignore
│
├── albums/
│   └── album-04-o-trono-intocavel/
│       ├── album.yaml · concept.md
│       ├── legal/                    # dossiê, créditos, vibecore-alerts
│       ├── assets/                   # binários (gitignored)
│       ├── campaigns/                # pendente
│       ├── bible-studies/              # pendente
│       └── tracks/
│           ├── track-01-o-legado/    # ★ faixa piloto — mais completa
│           │   ├── track.yaml · concept.md · lyrics.md · README.md
│           │   ├── identity/           # Sprint 5.1 — track_identity.md
│           │   ├── design/ · copy/ · suno/ · technical-sheet.md
│           │   └── video/
│           │       ├── narrative/      # Sprint 4 — Narrative Engine
│           │       ├── veo3-*.md · storyboard.md · filmora/
│           └── track-02 … track-12/    # letra + ficha; sem narrative/CDS
│
├── library/
│   ├── creative_direction_system/    # Sprint 5 — CDS
│   ├── narrative_engine/             # Sprint 4 — 8 módulos
│   └── veo3/                         # Sprint 3 — Video Engine
│
├── templates/                        # 8 templates reutilizáveis
├── scripts/
│   ├── migrate_album_04.py
│   └── video/                        # .env.example, README (sem scripts Veo)
└── docs/
    ├── API_VIDEO_AUTOMATION.md
    └── PROJECT_STATUS_REPORT.md      # este arquivo
```

---

## 3. Status das sprints concluídas

| Sprint / Versão | Entrega | Status | Commit |
|-----------------|---------|--------|--------|
| **v0.1.0** — Fundação | README, VISION, ROADMAP, AGENTS, WORKFLOW, CHANGELOG | ✅ | `df9c105` |
| **v0.2.0** — Fase 1 | Álbum 4 modular, 12 faixas, templates, legal, migrate script | ✅ | `df9c105` |
| **Sprint 3** — Vídeo API prep | `library/veo3/`, `docs/API_VIDEO_AUTOMATION.md`, templates Veo, `scripts/video/` | ✅ | `df9c105` |
| **Sprint 4** — Narrative Engine | 8 módulos `narrative_engine/` + retrofit Track 01 `video/narrative/` | ✅ | `b14a741` |
| **Sprint 5** — CDS | `creative_direction_system/` + integração WORKFLOW/AGENTS/PROJECT_STRUCTURE | ✅ | `b13a759` |
| **Sprint 5.1** — Track Identity | `track-01/identity/track_identity.md` + README da faixa | 🔄 Local | *não commitado* |

### Sprints / itens planejados (não iniciados)

| Item | Status |
|------|--------|
| Regra Cursor `.cursor/rules/fce.mdc` | 📋 |
| `library/suno/`, `library/canva/`, `library/copy/` | 📋 |
| Scripts `generate_scene.py` / `generate_video_plan.py` | 📋 |
| Retrofit Narrative Engine tracks 02–12 | 📋 |
| Retrofit CDS por faixa | 📋 |
| Campanhas `campaign-track-XX/` | 📋 |
| Estudos bíblicos `bible-studies/` | 📋 |
| Primeiros assets binários (áudio/vídeo) | 📋 |

---

## 4. Status da Track 01 — O Legado

**Referência:** Salmo 37 · Vibe: Trap Acústico & Pop Teatral · `status: lyrics_final`

| Módulo | Path | Status | Notas |
|--------|------|--------|-------|
| Metadados | `track.yaml` | ✅ | Completo |
| Conceito | `concept.md` | ✅ | Links para identity e narrative |
| Letra | `lyrics.md` | ✅ | Definitiva, tags Suno |
| Ficha técnica | `technical-sheet.md` | ✅ | Suno prompt documentado |
| Suno | `suno/prompt.txt` | ✅ | Áudio master pendente |
| **Identity** | `identity/track_identity.md` | ✅ | Sprint 5.1 — tokens `legado-*`, 9 seções |
| README faixa | `README.md` | ✅ | Índice central |
| CDS brief | `design/creative-brief.md` | ❌ | Não criado |
| CDS design spec | `design/design-specification.md` | ❌ | Não criado |
| CDS review | `design/creative-review.md` | ❌ | Não criado |
| Canva brief | `design/canva-brief.md` | 🔄 | Stub — aponta para identity |
| Copy | `copy/posts.md`, `captions.md` | 🔄 | Stubs |
| **Narrative Engine** | `video/narrative/` | ✅ | 6 cenas, Rafael, prompts compostos |
| Vídeo plano | `veo3-video-plan.md`, `storyboard.md` | ✅ | Derivados de narrative |
| Prompts Veo | `veo3-prompts.md` | ✅ | Export operacional |
| Filmora | `filmora/edit-notes.md` | ✅ | Timeline documentada |
| Geração Veo | `assets/video/veo3/` | ❌ | 0 clips gerados |
| Áudio master | `assets/audio/` | ❌ | Pendente |
| Campanha | `campaigns/campaign-track-01/` | ❌ | Não criada |
| Estudo bíblico | `bible-studies/study-track-01-salmo-37/` | ❌ | Não criado |

### Narrative Engine — resumo Track 01

| Artefato | Conteúdo |
|----------|----------|
| Hook | Conflito (Sl 37:1) — exaustão urbana |
| Personagem | Rafael Santos — trabalhador SP |
| Cenas | 6 × 17 campos — arco pain → hope |
| Prompts | Compostos via Prompt Composer (EN, 9:16, no text) |
| Director commentary | Completo por cena |

### Faixas 02–12

Todas possuem estrutura base migrada do dossiê (`track.yaml`, `lyrics.md`, `technical-sheet.md`, stubs de `video/`, `design/`, `copy/`). **Nenhuma** possui Narrative Engine, identity ou CDS aplicados. **Track 03** tem VibeCore Alert (estrofe Eclesiastes → corrigir para imagem do Salmo 39).

---

## 5. Arquivos principais criados

### Raiz e governança

| Arquivo | Função |
|---------|--------|
| `AGENTS.md` v0.4.0 | Regras para IAs |
| `WORKFLOW.md` v0.4.0 | 9 workflows + Narrative + CDS pipelines |
| `PROJECT_STRUCTURE.md` | Paths, schemas, módulos |
| `CHANGELOG.md` | Histórico de versões |

### Biblioteca permanente

| Módulo | Arquivos |
|--------|----------|
| `library/narrative_engine/` | 9 arquivos (01–08 + README) |
| `library/creative_direction_system/` | 4 arquivos (01–03 + README) |
| `library/veo3/` | 4 arquivos (prompt-rules, camera, continuity, archetypes) |

### Track 01 (piloto)

| Path | Sprint |
|------|--------|
| `video/narrative/*` (7 arquivos) | 4 |
| `identity/track_identity.md` | 5.1 |
| `README.md` | 5.1 |
| `video/veo3-video-plan.md`, `storyboard.md`, `veo3-prompts.md` | 4 |

### Templates (8)

`track-template.md` · `campaign-template.md` · `bible-study-template.md` · `suno-prompt-template.md` · `veo3-brief-template.md` · `veo3-scene-template.md` · `veo3-video-plan-template.md` · `canva-kit-brief.md`

---

## 6. Pendências por prioridade

### P0 — Bloqueiam ciclo completo Track 01

| ID | Pendência | Impacto |
|----|-----------|---------|
| P01 | Commit local Sprint 5.1 (identity + README) | Perda de trabalho; remote desatualizado conceitualmente |
| P02 | `design/creative-brief.md` + `design-specification.md` (CDS) | Gate G1/G2 antes de Canva formal |
| P03 | Áudio master Suno em `assets/audio/` | Vídeo e campanha sem sync |
| P04 | Geração Veo (6 cenas × 2–3 takes) | Reel 9:16 inexistente |
| P05 | Montagem Filmora + export reel | Entregável social |

### P1 — Campanha e ministério

| ID | Pendência |
|----|-----------|
| P06 | `campaigns/campaign-track-01/` — calendário 7 dias |
| P07 | `bible-studies/study-track-01-salmo-37/` |
| P08 | Assets Canva (capa, carrossel, story, thumbnail) via identity |
| P09 | `library/canva/album-04-brand.md` — brand kit álbum |

### P2 — Escala e qualidade

| ID | Pendência |
|----|-----------|
| P10 | VibeCore Alert Track 03 — letra Eclesiastes |
| P11 | Retrofit Narrative Engine tracks 02–12 |
| P12 | Retrofit CDS + identity por faixa |
| P13 | Regra Cursor `.cursor/rules/fce.mdc` |
| P14 | Scripts Veo API (`scripts/video/generate_*.py`) |
| P15 | Remover/arquivar dossiê monolítico na raiz |

### P3 — Backlog ROADMAP

| ID | Pendência |
|----|-----------|
| P16 | `library/suno/vibes/` |
| P17 | 3 faixas em ciclo completo (critério Fase 1 ROADMAP) |
| P18 | Distribuição e métricas (Fase 5) |

---

## 7. Próximo passo recomendado

**Sequência sugerida para fechar o primeiro ciclo criativo completo (Track 01):**

1. **Commit** Sprint 5.1 (`identity/`, `README.md`, CHANGELOG)
2. **Derivar CDS** — `design/creative-brief.md` + `design-specification.md` a partir de `track_identity.md` + templates CDS
3. **Canva** — executar `canva-brief.md` com tokens `legado-*` (capa P0 + carrossel devocional)
4. **Suno** — exportar áudio master
5. **Veo** — gerar cenas 04→05→01→02→03→06 (ordem documentada)
6. **Filmora** — montar reel 9:16 + legenda Sl 37:5
7. **Campanha** — `campaign-track-01/calendar.md` (7 dias)

**Alternativa paralela:** Iniciar retrofit Narrative Engine na **Track 02** enquanto assets Track 01 são gerados manualmente.

---

## 8. Últimos commits locais

| Hash | Mensagem | Data (aprox.) |
|------|----------|---------------|
| `b13a759` | docs: adiciona creative direction system | 2026-07-02 |
| `b14a741` | docs: migra track 01 para narrative engine | 2026-07-02 |
| `df9c105` | docs: fundacao inicial do Franklin Creative Engine | 2026-07-02 |

---

## 9. Status do Git

| Campo | Valor |
|-------|-------|
| **Branch atual** | `main` |
| **Tracking** | `origin/main` @ `b13a759` |
| **Commits à frente do remote** | 0 (branch reportada como up to date) |
| **Commits atrás do remote** | 0 |
| **Push pendente** | Nenhum commit local não enviado |

### Remote configurado

```
origin  https://github.com/nilknarfsam/franklin_creative-_engine.git (fetch)
origin  https://github.com/nilknarfsam/franklin_creative-_engine.git (push)
```

### Working tree (2026-07-02)

**Modificados (não staged):**

- `CHANGELOG.md`
- `albums/.../track-01-o-legado/concept.md`
- `albums/.../track-01-o-legado/design/canva-brief.md`

**Não rastreados:**

- `albums/.../track-01-o-legado/README.md`
- `albums/.../track-01-o-legado/identity/` (contém `track_identity.md`)

**Este relatório** (`docs/PROJECT_STATUS_REPORT.md`) também está não rastreado até commit.

---

## Métricas rápidas

| Métrica | Valor |
|---------|-------|
| Faixas documentadas | 12 / 12 |
| Faixas com Narrative Engine | 1 / 12 |
| Faixas com Track Identity | 1 / 12 |
| Faixas com CDS aplicado | 0 / 12 |
| Clips Veo gerados | 0 |
| Áudios master versionados | 0 |
| VibeCore Alerts abertos | 1 (Track 03) |

---

*Relatório gerado para orientação humana e agentes de IA. Atualizar após cada sprint ou marco significativo.*
