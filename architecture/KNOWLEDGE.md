# Knowledge Base — Sistema Planejado FCE 2.0

**Versão:** 2.0.0-sprint1  
**Status:** Documentado — **pastas e arquivos reais não criados nesta sprint**

---

## Propósito

A **Knowledge Base (KB)** será a fonte única de verdade para políticas, princípios e referências estáveis — eliminando duplicação entre `FCE.md`, `AGENTS.md`, launchers e `WORKFLOW.md`.

**Princípio SSOT:** escrever uma vez, referenciar por ID em todo o sistema.

Exemplo futuro de referência:

```markdown
Ver @fce/knowledge/theology/fidelity-rules
```

---

## Localização planejada

```
knowledge/
├── theology/
│   ├── fidelity-rules.md        # Fidelidade bíblica, VibeCore Alerts
│   ├── exegesis-principles.md   # Adaptação vs adulteração
│   └── salmos-overview.md       # Contexto Salmos 37–48 (álbum 4)
│
├── music/
│   ├── vibecore-principles.md   # Identidade sonora
│   ├── suno-safety.md           # Regra da Alma, bypass lírico
│   └── dynamics-fce.md          # Intro → chorus explosion
│
├── design/
│   ├── hero-first.md            # Filosofia Hero Asset
│   ├── typography-rules.md      # Texto no Canva, nunca na fotografia
│   └── tokens-conventions.md    # legado-*, track identity
│
├── marketing/
│   ├── tone-fce.md              # Teatral, autêntico, sem clickbait
│   ├── cta-christian.md         # CTAs cristãos autênticos
│   └── campaign-structure.md    # Calendário 7 dias
│
├── software/
│   ├── repo-rules.md            # Paths, slugs, não inventar faixas
│   ├── security.md              # API keys, .env
│   └── agent-conventions.md     # Formato de entrega FCE
│
├── social/
│   ├── formats-916.md           # Reels, stories, shorts
│   ├── platform-ig.md           # Instagram específico
│   └── platform-yt-tiktok.md    # YouTube, TikTok
│
└── platforms/
    ├── suno.md                  # Notas operacionais Suno
    ├── veo.md                   # Notas operacionais Veo 3
    ├── canva.md                 # Notas operacionais Canva
    └── filmora.md               # Notas operacionais Filmora
```

**Sprint 1:** árvore documentada. Conteúdo extraído de `AGENTS.md` em sprints futuras.

---

## Domínios da Knowledge Base

### `knowledge/theology/`

| Conteúdo | Origem atual (extração futura) |
|----------|-------------------------------|
| Fidelidade bíblica | `VISION.md`, `AGENTS.md` |
| VibeCore Alerts | `legal/vibecore-alerts.md` |
| Verificação Teológica Estrita | `AGENTS.md`, `library/suno/` |

**Consumidores:** Profile `theology`, launcher Suno, estudos bíblicos.

---

### `knowledge/music/`

| Conteúdo | Origem atual |
|----------|--------------|
| VibeCore sonoro | `VISION.md` |
| Regra da Alma | `library/suno/bypass-and-safety.md` |
| Dinâmica de faixa | `WORKFLOW.md` WF2 |

**Consumidores:** Profile `music`, `CREATE_SUNO_SONG.md`.

---

### `knowledge/design/`

| Conteúdo | Origem atual |
|----------|--------------|
| Hero-first | `docs/PRODUCTION_PHILOSOPHY.md` |
| Hero Review 8 critérios | `AGENTS.md` |
| Espaço negativo 35–40% | `AGENTS.md`, CDS |

**Consumidores:** Profile `visual`, launchers de design.

---

### `knowledge/marketing/`

| Conteúdo | Origem atual |
|----------|--------------|
| Tom de copy | `WORKFLOW.md` WF5 |
| Estrutura legenda IG | `WORKFLOW.md` WF5 |
| Campanha 7 dias | `WORKFLOW.md` WF7 |

**Consumidores:** Profile `writing`, `social`, campanha.

---

### `knowledge/software/`

| Conteúdo | Origem atual |
|----------|--------------|
| Convenções de path | `PROJECT_STRUCTURE.md` |
| Segurança vídeo/API | `AGENTS.md`, `docs/API_VIDEO_AUTOMATION.md` |
| Formato de resposta agente | `AGENTS.md` |

**Consumidores:** Profile `coding`, `IMPROVE_SYSTEM.md`.

---

### `knowledge/social/`

| Conteúdo | Origem atual |
|----------|--------------|
| 9:16 first | `AGENTS.md`, `library/veo3/` |
| Formatos por entregável | `WORKFLOW.md` WF4, WF3 |

**Consumidores:** Profile `social`, launchers REEL/SHORTS/STORY.

---

### `knowledge/platforms/`

Notas operacionais por ferramenta externa — complementam `library/` (método) com dicas de execução humana.

**Diferença Module vs Platform KB:**

| `library/suno/` (Module) | `knowledge/platforms/suno.md` (KB) |
|--------------------------|-------------------------------------|
| VibeShell 6 fases | Onde clicar, limites da UI, iteração |
| Regras de prompt | Troubleshooting, export WAV |

---

## IDs estáveis (convenção futura)

```
@fce/knowledge/{domínio}/{slug}
```

Exemplos:

- `@fce/knowledge/theology/fidelity-rules`
- `@fce/knowledge/design/hero-review-checklist`
- `@fce/knowledge/software/security`

Launchers e Profiles referenciam IDs — não copiam parágrafos.

---

## O que NÃO entra na Knowledge Base

| Tipo | Onde fica |
|------|-----------|
| Letras de faixa | `albums/.../lyrics.md` |
| Prompts Suno/Veo finais | `suno/prompt.txt`, `veo3-prompts.md` |
| Método passo a passo longo | `library/` (Modules) |
| Instâncias CDS por faixa | `design/creative-brief.md` etc. |
| Binários | `assets/` |

---

## Migração de conteúdo (roadmap)

| Sprint | Ação KB |
|--------|---------|
| 1 | Documentar estrutura (este arquivo) |
| 2 | Criar `knowledge/software/security.md` + `knowledge/design/hero-review.md` |
| 3 | Extrair políticas universais de AGENTS → `knowledge/software/repo-rules.md` |
| 4 | Glossário unificado `knowledge/glossary.yaml` |
| 5 | Launchers passam a referenciar IDs |

**Regra:** durante migração, originais em `AGENTS.md` permanecem até sprint de consolidação explícita.

---

## Compatibilidade

Nenhuma pasta `knowledge/` é criada na Sprint 1. `AGENTS.md` e `FCE.md` permanecem autoridade operacional.

---

**Versão:** Sprint 1 · 2026-07-03
