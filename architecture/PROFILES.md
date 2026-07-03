# Profiles — Sistema Planejado FCE 2.0

**Versão:** 2.0.0-sprint1  
**Status:** Documentado — **arquivos reais não criados nesta sprint**

---

## Propósito

**Profiles** são pacotes de contexto que informam a IA **como operar** em um domínio específico, sem carregar o repositório inteiro.

Cada profile combina:

- Papel e responsabilidades
- Ordem de leitura mínima
- Referências a Knowledge e Modules
- Tom e restrições do domínio
- Ferramentas humanas esperadas (ChatGPT, Cursor, Suno, Canva, etc.)

Profiles **não substituem** `AGENTS.md` — futuramente `AGENTS.md` apontará para profiles como índice.

---

## Localização planejada

```
profiles/
└── franklin/
    ├── artist.md      # Identidade artística VibeCore, visão macro
    ├── music.md       # Suno, VibeShell, letras, ficha técnica
    ├── theology.md    # Exegese, fidelidade bíblica, VibeCore Alerts
    ├── visual.md      # CDS, Hero, Canva, identity tokens
    ├── social.md      # Reels, stories, carrosséis, calendário
    ├── writing.md     # Copy, legendas, estudos bíblicos
    └── coding.md      # Cursor, schemas, scripts, estrutura repo
```

**Sprint 1:** estrutura documentada apenas. Criação física em Sprint 2.

---

## Catálogo de profiles

### `profiles/franklin/artist.md`

| Campo | Valor |
|-------|-------|
| **Público** | Direção criativa geral, conceito de faixa/álbum |
| **Módulos** | CDS (visão), VISION, identity |
| **Knowledge** | `knowledge/design/vibecore.md` (futuro) |
| **Não faz** | Prompts Veo técnicos, schemas YAML |

**Contexto mínimo:** VibeCore, arco emocional da faixa, `concept.md`, `track_identity.md`.

---

### `profiles/franklin/music.md`

| Campo | Valor |
|-------|-------|
| **Público** | Produção Suno, letras, masterização |
| **Módulos** | `library/suno/` (VibeShell completo) |
| **Launchers** | `CREATE_SUNO_SONG.md`, `CREATE_TRACK.md` |
| **Knowledge** | `knowledge/music/` (futuro) |
| **Não faz** | Design Canva, prompts Veo |

**Contexto mínimo:** `lyrics.md`, `technical-sheet.md`, `suno/prompt.txt`, VibeShell Fase aplicável.

**Regras herdadas:** Verificação Teológica Estrita, Regra da Alma, `Brazilian Portuguese vocals`.

---

### `profiles/franklin/theology.md`

| Campo | Valor |
|-------|-------|
| **Público** | Exegese, auditoria teológica, estudos bíblicos |
| **Módulos** | `library/theology/` (futuro), WF6 |
| **Knowledge** | `knowledge/theology/` (futuro) |
| **Não faz** | Tags Suno, prompts de instrumentação |

**Contexto mínimo:** Texto bíblico da faixa, `lyrics.md`, `vibecore-alerts.md`.

---

### `profiles/franklin/visual.md`

| Campo | Valor |
|-------|-------|
| **Público** | CDS, Hero Asset, Canva, identity |
| **Módulos** | `library/creative_direction_system/`, `library/canva/` (futuro) |
| **Launchers** | CREATE_HERO_ASSET, CREATE_CAROUSEL, CREATE_INSTAGRAM_POST, CREATE_STORY |
| **Knowledge** | `knowledge/design/` (futuro) |
| **Não faz** | Narrative Engine completo (exceto alinhamento visual) |

**Contexto mínimo:** `design-specification.md`, `track_identity.md`, Hero Review checklist.

**Gates:** G2 antes de Hero; G2.5 antes de derivação.

---

### `profiles/franklin/social.md`

| Campo | Valor |
|-------|-------|
| **Público** | Reels, Shorts, stories, campanha social |
| **Módulos** | narrative, veo3 (quando vídeo); CDS (quando visual) |
| **Launchers** | CREATE_REEL, CREATE_SHORTS, CREATE_STORY, campanha |
| **Knowledge** | `knowledge/social/`, `knowledge/platforms/` (futuro) |
| **Não faz** | Refatoração de letras definitivas |

**Contexto mínimo:** Formato 9:16, calendário WF7, assets aprovados.

---

### `profiles/franklin/writing.md`

| Campo | Valor |
|-------|-------|
| **Público** | Legendas, posts, hooks, estudos devocionais |
| **Módulos** | `library/copy/` (futuro), WF5, WF6 |
| **Launchers** | CREATE_CAPTION |
| **Knowledge** | `knowledge/marketing/` (futuro) |
| **Não faz** | Geração de imagem, prompts Veo |

**Contexto mínimo:** `lyrics.md`, `creative-brief.md`, tom FCE (teatral, autêntico, sem clickbait).

---

### `profiles/franklin/coding.md`

| Campo | Valor |
|-------|-------|
| **Público** | Cursor, Codex, automação, schemas |
| **Módulos** | Todos (leitura para manutenção) |
| **Launchers** | IMPROVE_SYSTEM, CREATE_TRACK, CREATE_ALBUM |
| **Knowledge** | `knowledge/software/` (futuro) |
| **Não faz** | Decisões teológicas sem flag humana |

**Contexto mínimo:** `PROJECT_STRUCTURE.md`, `architecture/`, specs (futuro), `scripts/`.

---

## Mapeamento Profile → Launcher (futuro)

| Launcher | Profile primário | Profile secundário |
|----------|------------------|-------------------|
| CREATE_SUNO_SONG | music | theology |
| CREATE_HERO_ASSET | visual | artist |
| CREATE_VIDEO_VEO | social | visual |
| CREATE_CAPTION | writing | theology |
| CREATE_TRACK | music | theology |
| IMPROVE_SYSTEM | coding | — |
| Campanha completa | social | visual + writing + music |

---

## Relação Profile ↔ Knowledge ↔ Module

```
Profile (como operar)
    │
    ├── lê subset de Knowledge (políticas do domínio)
    │
    └── delega método a Module (library/)
```

Profile é a **lente**. Knowledge é a **verdade**. Module é o **processo**.

---

## Formato planejado de cada profile

```markdown
---
fce_profile: franklin/music
version: 1.0.0
modules: [suno]
knowledge: [knowledge/music/*]
launchers: [CREATE_SUNO_SONG]
---

# Profile — Franklin / Music

## Papel
...

## Leitura mínima
...

## Regras do domínio
...

## Não fazer
...
```

---

## Compatibilidade

Até Sprint 2, IAs continuam usando `AGENTS.md` como fonte operacional. Profiles são roadmap — não alteram comportamento atual.

---

**Versão:** Sprint 1 · 2026-07-03
