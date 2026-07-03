# MASTER BLUEPRINT — Franklin Creative Engine (FCE)

**Documento:** Especificação oficial da plataforma  
**Versão do Blueprint:** 1.0.0  
**Horizonte:** 10 anos (2026–2036)  
**Status:** Canônico — projeto alvo 100% concluído  
**Autoridade:** Este documento supersede visões parciais em sprints quando houver conflito de longo prazo  
**Implementação atual:** FCE 1.x operacional — ver [MASTER_MIGRATION_PLAN.md](./MASTER_MIGRATION_PLAN.md)

---

## Prefácio

O Franklin Creative Engine não é um repositório de letras. É um **sistema operacional criativo** — uma plataforma declarativa que orquestra teologia, música, vídeo, design, copy e campanha com agentes de IA e humanos em loop.

Este Blueprint descreve o **estado final** da plataforma. Nenhuma limitação da estrutura atual restringe esta visão. A migração é tratada separadamente.

**Prioridades de design (ordem):**

1. Simplicidade conceitual  
2. Escalabilidade (álbuns, faixas, colaboradores, IAs)  
3. Baixo consumo de contexto por tarefa  
4. Compatibilidade entre IAs (ChatGPT, Claude, Gemini, Cursor, Codex, local, futuras)  
5. Manutenção simples — mudança localizada  
6. Evolução contínua sem breaking changes  
7. Modularidade e reutilização  
8. Independência entre componentes  

---

# 1. Visão da Plataforma

## 1.1 O que é o Franklin Creative Engine

O **Franklin Creative Engine (FCE)** é uma plataforma de produção criativa cristã contemporânea que transforma Escritura em obras completas: faixa musical, identidade visual, vídeo cinematográfico, conteúdo escrito, estudo bíblico e campanha de lançamento — com fidelidade teológica, estética **VibeCore** e rastreabilidade documental.

| Dimensão | Definição |
|----------|-----------|
| **Tipo** | Creative OS — sistema operacional criativo |
| **Domínio** | Arte cristã de alto impacto (música + multimídia + ministério) |
| **Unidade de produção** | Faixa (`track`) dentro de Álbum (`album`) |
| **Unidade de distribuição** | Campanha (`campaign`) + derivados devocionais |
| **Memória** | Repositório git + manifests declarativos — não chat |
| **Execução** | Humanos + IAs guiados por Registry, Packs e Specs |

## 1.2 Missão

Produzir e distribuir arte cristã que conduza o ouvinte da **Escritura à adoração**, da **dor à esperança**, da **passividade ao engajamento com a Palavra** — sem conteúdo genérico de motivação.

Cada Salmo vira faixa. Cada faixa vira campanha. Cada campanha vira jornada devocional.

## 1.3 Propósito

Resolver a fragmentação da produção criativa cristã:

- Letristas sem pipeline visual  
- Produtores sem continuidade teológica  
- Designers sem contexto sonoro  
- IAs sem memória entre sessões  
- Campanhas sem arco narrativo unificado  

O FCE unifica silos em **pipelines declarativos** com gates, validação e contexto mínimo.

## 1.4 Filosofia

### Obras completas, não posts isolados

Produção orientada a **ciclo fechado**: conceito → letra → áudio → estratégia visual → hero → vídeo → copy → calendário → publicação → estudo derivado.

### Repositório como verdade

O chat é interface. O repositório é memória. Decisões vivem em arquivos versionados.

### Declarativo sobre imperativo

A plataforma descreve **o que deve ser verdade** (Registry, Specs, Gates). Execução (IA, humano, script) materializa essa verdade.

### Hero primeiro, derivação depois

Identidade visual nasce no Hero aprovado. Demais peças derivam — não competem.

### Narrative antes de Veo

Nenhum prompt de vídeo é manual. Direção cinematográfica precede geração.

### Teologia com humildade e rigor

Adaptação poética com **VibeCore Alerts** — dúvida documentada, nunca silenciada.

### VibeCore

Trap acústico, pop teatral, cinematic trap-rock, arena anthem — dinâmica cinematográfica, vocal teatral, simbolismo bíblico moderno (não gospel stock).

## 1.5 Princípios fundamentais (P1–P14)

| ID | Princípio | Essência |
|----|-----------|----------|
| P1 | Escritura como fonte | Ancoragem bíblica em toda faixa |
| P2 | Repositório SSOT | Git + manifests — não chat |
| P3 | Evolução aditiva | Sem remoção destrutiva sem fase explícita |
| P4 | Leitura mínima | Context Packs — só o necessário |
| P5 | Módulos independentes | Contratos claros em `library/` |
| P6 | Router-first | `FCE.md` orquestra antes de produzir |
| P7 | Método / política / instância | `library/` ≠ `knowledge/` ≠ `albums/` |
| P8 | Gates explícitos | G1, G2, G2.5, narrative, etc. |
| P9 | Hero primeiro | Derivação visual após Hero approved |
| P10 | Narrative antes de Veo | Prompt Composer obrigatório |
| P11 | Compatibilidade | Aliases e versionamento semântico |
| P12 | Idioma | PT-BR conteúdo · EN prompts Suno/Veo |
| P13 | Segurança | Secrets fora do repo |
| P14 | Qualidade sobre velocidade | Obras completas, não conteúdo raso |

Detalhamento: `architecture/PRINCIPLES.md` (espelho estável deste Blueprint).

---

# 2. Arquitetura Geral

## 2.1 Diagrama de camadas (estado final)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              HUMAN / AI ACTORS                               │
│         ChatGPT · Claude · Gemini · Cursor · Codex · Local LLM · Future     │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────────┐
│  CORE — Identidade, missão, governança humana                              │
│  VISION · CHARTER · GOVERNANCE · ADR · CHANGELOG · LICENSE                 │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────────┐
│  ROUTER — FCE.md + fce/router/                                               │
│  Entrada única · resolve task · scope · gates · emite session bundle         │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────────┐
│  REGISTRY — fce/registry/                                                    │
│  tasks · modules · gates · pipelines · plugins · profiles-index · packs-index│
└───────────────┬───────────────────────────────┬─────────────────────────────┘
                │                               │
    ┌───────────▼──────────┐         ┌──────────▼──────────┐
    │  CONTEXT PACKS       │         │  EXECUTION PACKS     │
    │  fce/context-packs/  │         │  fce/execution-packs/│
    │  O que LER           │         │  O que FAZER (ordem) │
    └───────────┬──────────┘         └──────────┬──────────┘
                │                               │
    ┌───────────▼───────────────────────────────▼──────────┐
    │  SESSION BUNDLE (gerado, não versionado por faixa)      │
    │  { profile, context_pack, execution_pack, gates, scope }│
    └───────────┬────────────────────────────────────────────┘
                │
    ┌───────────▼──────────┐
    │  LAUNCHERS (thin)    │  launcher/*.md — conversa mínima
    └───────────┬──────────┘
                │
    ┌───────────▼──────────────────────────────────────────┐
    │  PROFILES · KNOWLEDGE · SPECS · VALIDATORS            │
    └───────────┬──────────────────────────────────────────┘
                │
    ┌───────────▼──────────┐
    │  MODULES (library/)  │  + PLUGINS (plugins/)
    └───────────┬──────────┘
                │
    ┌───────────▼──────────┐
    │  TEMPLATES           │  → OUTPUT (albums/) + ASSETS
    └───────────┬──────────┘
                │
    ┌───────────▼──────────┐
    │  PIPELINES · TESTS   │  Automação e qualidade
    └──────────────────────┘
```

## 2.2 Árvore de diretórios (estado final)

```
franklin_creative_engine/
│
├── MASTER_BLUEPRINT.md              # Este documento
├── MASTER_MIGRATION_PLAN.md         # Plano de migração
├── FCE.md                           # Router humano + entry CLI
├── README.md
│
├── core/                            # Governança canônica (evolução de raiz)
│   ├── VISION.md
│   ├── CHARTER.md                   # Missão + princípios consolidados
│   ├── AGENTS.md                    # Índice → knowledge + profiles
│   ├── WORKFLOW.md                  # Narrativa humana dos pipelines
│   └── ROADMAP.md
│
├── fce/                             # Camada declarativa machine-readable
│   ├── registry/
│   │   ├── tasks.yaml
│   │   ├── modules.yaml
│   │   ├── gates.yaml
│   │   ├── pipelines.yaml
│   │   ├── plugins.yaml
│   │   └── profiles-index.yaml
│   ├── context-packs/
│   ├── execution-packs/
│   ├── router/
│   │   └── resolution.md            # Algoritmo de resolução
│   └── schema/                      # JSON Schema dos registros
│
├── architecture/                    # Meta-arquitetura + ADR
│   ├── adr/                         # Architecture Decision Records
│   └── [docs de referência]
│
├── launcher/                        # Playbooks thin
├── library/                         # Modules (engines)
├── plugins/                         # Extensões third-party / futuras
├── knowledge/                       # Knowledge Base SSOT
├── profiles/                        # Perfis por ator e domínio
│   ├── franklin/                    # Domínio criativo Franklin
│   ├── agents/                      # Perfis por ferramenta IA
│   └── human/                       # Perfis por papel humano
├── specs/                           # Contratos verificáveis
├── templates/                       # Scaffolds versionados
├── pipelines/                       # Orquestrações multi-tarefa
├── validators/                      # Regras de validação + fce check
├── tests/                           # Fixtures, golden files, contract tests
├── examples/                        # Golden paths documentados
├── history/                         # Legado arquivado (redirects)
│
├── albums/                          # Instâncias de produção
├── scripts/                         # CLI: fce, migrate, generate
├── docs/                            # Docs operacionais expandidas
└── .fce/                            # Local only: cache, session (gitignored)
```

---

## 2.3 Componentes — especificação

### CORE

**Função:** Identidade imutável ou de mudança rara. Missão, princípios, governança, ADRs.

| Artefato | Papel |
|----------|-------|
| `core/VISION.md` | Por quê existimos |
| `core/CHARTER.md` | Princípios P1–P14 + filosofia |
| `core/AGENTS.md` | Índice operacional — aponta para Knowledge e Profiles |
| `core/WORKFLOW.md` | Narrativa legível dos pipelines (humanos) |
| `architecture/adr/` | Decisões arquiteturais datadas |

**Regra:** Core não contém instâncias de faixa nem prompts finais.

---

### REGISTRY

**Função:** Índice declarativo único da plataforma. Responde: *o que existe, como se relaciona, como resolver uma tarefa*.

| Registro | Conteúdo |
|----------|----------|
| `tasks.yaml` | Tarefas, menu, launcher, packs, spec, gates |
| `modules.yaml` | Engines, paths, deps, outputs típicos |
| `gates.yaml` | Critérios de aprovação verificáveis |
| `pipelines.yaml` | Composições de tarefas (campanha, álbum) |
| `plugins.yaml` | Extensões registradas |
| `profiles-index.yaml` | task → profile(s) |

**Propriedades:** IDs estáveis, versionamento semântico por registro, schema validado em CI.

**Não é:** executor, banco de letras, armazenamento de secrets.

---

### ROUTER

**Função:** Porta de entrada única. Resolve `task_id + scope` → Session Bundle.

**Interface humana:** `FCE.md` — menu conversacional que invoca resolução.

**Interface machine:** `fce resolve --task create_reel --track 01` → JSON bundle.

**Algoritmo:**

```
INPUT:  task_id, album_id, track_id?, actor_profile?
1. LOAD task from registry
2. EVALUATE gates on scope → { passed | blocked[], remediation[] }
3. IF blocked → RETURN blocked bundle (launchers de desbloqueio)
4. RESOLVE context_pack(scope)
5. RESOLVE execution_pack(scope) [opcional por tarefa]
6. RESOLVE profile(actor, task)
7. RETURN session_bundle
```

---

### CONTEXT PACKS

**Função:** Lista **fechada** do que ler — implementa P4.

**Estrutura:**

```yaml
context_pack:
  id: create_reel
  version: 1.2.0
  always: []          # ≤3 após maturidade
  modules: []         # arquivos específicos em library/
  knowledge: []       # @fce/knowledge/ids
  track: []           # paths relativos à faixa
  conditional: []
  excludes: []
  budget:
    max_files: 12
    max_lines: 3000
```

**Resolução:** parametriza `{track_path}`, avalia conditional, aplica excludes.

---

### EXECUTION PACKS

**Função:** Lista **ordenada** do que fazer — passos, handoffs humano/IA, artefatos por etapa.

**Por que existe (além de Context Packs):**

| Context Pack | Execution Pack |
|--------------|----------------|
| Leitura mínima | Ação mínima |
| Para qualquer IA | Para orquestração e automação |
| Estático por tarefa | Pode variar por estado da faixa |

**Estrutura:**

```yaml
execution_pack:
  id: create_reel
  steps:
    - id: validate_narrative
      actor: validator
      gate: narrative_complete
    - id: confirm_prompts
      actor: human|ai
      reads: [video/veo3-prompts.md]
    - id: generate_veo
      actor: human
      tool: veo
      handoff: scripts/video/generate_scene.py
    - id: filmora_assembly
      actor: human
      tool: filmora
      output: assets/video/*-reel-9x16.mp4
```

**Regra:** Tarefas simples (legenda) podem ter execution_pack mínimo ou omitido. Campanhas e vídeo **exigem** execution pack.

---

### LAUNCHERS

**Função:** Roteiro conversacional **thin** — perguntas, tom, entrega.

**Estado final (~30–50 linhas cada):**

- Objetivo (1 parágrafo)  
- `task_id` + link registry  
- Perguntas ao usuário  
- Referência `@fce/session` — não lista 15 arquivos  
- Formato de entrega FCE  
- `remediation` se blocked  

**Não contém:** método duplicado de `library/`, políticas copiadas de KB.

---

### MODULES (`library/`)

**Função:** Engines metodológicas permanentes — o **como** pensar e executar.

| Módulo | Domínio |
|--------|---------|
| `creative_direction_system` | CDS — brief, spec, review |
| `narrative_engine` | Direção cinematográfica |
| `veo3` | Validação/execução vídeo |
| `suno` | VibeShell — áudio |
| `canva` | Brand e execução design |
| `copy` | Tom, hooks, CTAs |
| `theology` | Exegese, alerts |
| `campaign` | Orquestração editorial |
| `distribution` | Plataformas, métricas (FCE 4+) |

**Contrato:** cada módulo registra-se em `modules.yaml` com `inputs`, `outputs`, `depends_on`, `spec`.

---

### KNOWLEDGE (`knowledge/`)

**Função:** SSOT de políticas, glossário, referências estáveis.

Ver Seção 5.

---

### PROFILES (`profiles/`)

**Função:** Lente de operação por ator e domínio.

Ver Seção 6.

---

### SPECS (`specs/`)

**Função:** Contratos verificáveis.

Ver Seção 7.

---

### TEMPLATES (`templates/`)

**Função:** Scaffolds de saída versionados.

Ver Seção 8.

---

### ASSETS

**Função:** Binários e exports — áudio, vídeo, imagens, legendas.

| Política | Regra |
|----------|-------|
| Versionamento git | Apenas markdown + manifests |
| Binários | Gitignore / LFS / storage externo |
| Manifest | `assets/manifest.yaml` por faixa — paths, checksums, status |
| Hero | `assets/hero/approved/` gate G2.5 |

---

### EXAMPLES (`examples/`)

**Função:** Golden paths reproduzíveis.

| Exemplo | Referência |
|---------|------------|
| `examples/track-complete/` | Aponta para Track 01 piloto |
| `examples/minimal-track/` | Stub mínimo válido |
| `examples/plugin-hello/` | Plugin de demonstração |

**Regra:** Examples referenciam `albums/` — não duplicam letras definitivas.

---

### PLUGINS (`plugins/`)

**Função:** Extensão sem alterar Core.

Ver Seção 10.

---

### VALIDATORS (`validators/`)

**Função:** Implementação de gates e specs.

```
validators/
├── fce_check.py           # CLI principal
├── rules/                 # Uma regra por gate
├── schemas/               # JSON Schema
└── reports/               # Output human-readable
```

**Comandos:**

```bash
fce check track 01                    # todos gates da faixa
fce check task create_carousel --track 01
fce validate-spec specs/narrative.spec.yaml --path albums/.../track-01
```

**Integração CI:** PR que altera `albums/` dispara validação de specs afetadas.

---

### PIPELINES (`pipelines/`)

**Função:** Orquestrações multi-tarefa declarativas.

```yaml
# pipelines/album-track-launch.yaml
pipeline:
  id: track_launch
  tasks:
    - create_suno_song
    - cds_full
    - create_hero_asset
    - narrative_full
    - create_video_veo
    - create_reel
    - create_campaign
  parallel_groups:
    - [create_suno_song, cds_full]
```

Registry `pipelines.yaml` indexa. Router executa sequencial ou paralelo conforme deps.

---

### HISTORY (`history/`)

**Função:** Legado arquivado com redirects — dossiê monolítico, manuais VibeShell V1.

**Regra:** Nunca delete — `history/README.md` mapeia path antigo → canônico.

---

### TESTS (`tests/`)

**Função:** Qualidade de plataforma (não de conteúdo teológico).

| Tipo | O que testa |
|------|-------------|
| Contract | Registry schema, spec compliance |
| Golden | Context pack resolution para Track 01 |
| Snapshot | `fce resolve` output estável |
| Link | Referências `@fce/` e paths existem |
| Fixture | Faixas stub mínimas em `tests/fixtures/` |

---

### FUTURE EXTENSIONS (reservado)

| Extensão | Fase |
|----------|------|
| `fce-portal/` | App devocional consumindo manifests |
| `fce-sdk/` | TypeScript/Python SDK para automação |
| `fce-i18n/` | Localização PT → ES, EN |
| `fce-metrics/` | Analytics de campanha |
| `fce-collab/` | Multi-autor, review workflows |
| Local LLM profiles | Ollama, LM Studio — profile `agents/local.md` |

---

# 3. Fluxo Completo de Execução

## 3.1 Fluxo macro: Salmo → Campanha publicada

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Salmo   │───►│ Conceito │───►│  Letra   │───►│  Suno    │
│  (fonte) │    │  + exegese│    │ definitiva│    │  master  │
└──────────┘    └──────────┘    └──────────┘    └────┬─────┘
                                                     │
     ┌───────────────────────────────────────────────┘
     │
     ▼
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│   CDS    │───►│ Identity │───►│   Hero   │───►│ Derivação│
│  G1→G2   │    │  tokens  │    │ approved │    │  Canva   │
└────┬─────┘    └──────────┘    └──────────┘    └──────────┘
     │
     ▼
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│Narrative │───►│   Veo    │───►│ Filmora  │───►│   Reel   │
│ Pipeline │    │  clips   │    │  montagem│    │  9:16    │
└──────────┘    └──────────┘    └──────────┘    └────┬─────┘
                                                       │
     ┌─────────────────────────────────────────────────┘
     ▼
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│   Copy   │───►│ Estudo   │───►│ Campanha │───►│ Publica  │
│ legendas │    │ bíblico  │    │ 7 dias   │    │ multi-plat│
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

## 3.2 Fluxo de sessão IA (detalhado)

```
USUÁRIO
  │ "Quero criar um Reel da Track 01"
  ▼
FCE.md / fce resolve
  │ task_id=create_reel, scope={album:04, track:01}
  ▼
REGISTRY
  │ load task · modules · gates · packs
  ▼
VALIDATORS (gates)
  │ narrative_complete? audio_warn?
  ├─ BLOCKED → remediation launcher + o que falta
  └─ OK
  ▼
SESSION BUNDLE gerado
  │ context_pack (8 arquivos)
  │ execution_pack (5 steps)
  │ profile: franklin/social + agents/chatgpt
  ▼
LAUNCHER thin (CREATE_REEL.md)
  │ perguntas · confirma escopo
  ▼
IA + HUMANO executam EXECUTION PACK
  │ read → produce → validate step
  ▼
OUTPUT
  │ assets/video/track-01-reel-9x16.mp4
  │ manifest atualizado
  ▼
fce check task create_reel --track 01
  │ spec validation → PASS
  ▼
ENTREGA
```

## 3.3 Fluxo de adição de módulo

```
PROPOSTA → ADR → spec nova → registry modules.yaml
    → knowledge (se política) → library/ → validator rules
    → template (se output) → test fixture → CHANGELOG
```

---

# 4. Modelo Declarativo

## 4.1 Registry resolve tarefas

1. **Lookup** — `task_id` → registro completo  
2. **Scope binding** — `album_id`, `track_id` → paths absolutos relativos  
3. **Gate evaluation** — ordem topológica de `depends_on`  
4. **Pack resolution** — merge template pack + overrides de scope  
5. **Profile selection** — actor override ou default do task  
6. **Emit bundle** — artefato consumível por IA/humano/CLI  

## 4.2 Context Packs — regras

- Budget obrigatório (`max_files`, `max_lines`)  
- `modules[]` — somente arquivos, nunca diretórios inteiros  
- `knowledge[]` — IDs, não paths arbitrários  
- `excludes[]` — obrigatório para tarefas especializadas  
- Versionamento semântico — minor = add file, major = remove/rename  

## 4.3 Launchers minimalistas

Template final:

```markdown
# Launcher — {title}
task_id: {id}
registry: fce/registry/tasks.yaml#{id}

## Objetivo
[1 parágrafo]

## Pré-requisitos
Resolvidos pelo Router. Se blocked, ver remediation.

## Perguntas
[lista]

## Execução
Seguir execution_pack:{id} · profile:{profile}

## Entrega
Formato FCE · spec:{spec_id}
```

## 4.4 Novos módulos

1. ADR aprovado  
2. `library/{module}/` + README  
3. Entrada em `modules.yaml`  
4. `specs/{module}.spec.yaml`  
5. Validators  
6. Context packs das tarefas afetadas  
7. Plugin manifest (se extensão isolada)  
8. Test contract  
9. Documentação WORKFLOW (narrativa humana)  

---

# 5. Sistema de Conhecimento

## 5.1 Arquitetura KB

```
knowledge/
├── index.yaml                 # Catálogo de todos os IDs
├── theology/
│   ├── fidelity-rules.md
│   ├── exegesis-principles.md
│   ├── vibecore-alerts-guide.md
│   └── canon/
│       └── salmos-37-48.md
├── music/
│   ├── vibecore-principles.md
│   ├── suno-safety.md
│   ├── dynamics-fce.md
│   └── mastering.md
├── design/
│   ├── hero-first.md
│   ├── hero-review-checklist.md
│   ├── typography-rules.md
│   └── tokens-conventions.md
├── narrative/
│   ├── six-elements.md
│   ├── aspect-ratio-policy.md
│   └── no-text-policy.md
├── marketing/
│   ├── tone-fce.md
│   ├── cta-christian.md
│   └── campaign-7-day.md
├── software/
│   ├── repo-rules.md
│   ├── security.md
│   ├── agent-conventions.md
│   └── naming-slugs.md
├── social/
│   ├── formats-916.md
│   └── platform-matrix.md
└── platforms/
    ├── suno.md
    ├── veo.md
    ├── canva.md
    ├── filmora.md
    └── landr.md
```

## 5.2 IDs e referência

Formato: `@fce/knowledge/{domain}/{slug}`

Cada arquivo KB inclui frontmatter:

```yaml
---
fce_knowledge: theology/fidelity-rules
version: 1.0.0
stability: stable | draft | deprecated
supersedes: []
---
```

## 5.3 Regras KB

| Regra | Detalhe |
|-------|---------|
| SSOT | Uma política — um arquivo canônico |
| Tamanho | Preferir <150 linhas por política |
| Sem instância | KB não contém letras de faixa |
| Extração | `core/AGENTS.md` vira índice — não duplica |
| Deprecation | `stability: deprecated` + redirect no index |

## 5.4 Resolução na sessão

Context Pack referencia IDs → Router expande para paths → IA lê apenas esses arquivos.

---

# 6. Sistema de Profiles

## 6.1 Taxonomia

```
profiles/
├── franklin/           # Domínio criativo (o quê produzir)
│   ├── artist.md
│   ├── music.md
│   ├── theology.md
│   ├── visual.md
│   ├── social.md
│   ├── writing.md
│   └── coding.md
├── agents/             # Ferramenta IA (como navegar)
│   ├── chatgpt.md
│   ├── claude.md
│   ├── gemini.md
│   ├── cursor.md
│   ├── codex.md
│   └── local.md
└── human/              # Papel humano
    ├── producer.md
    ├── theologian-reviewer.md
    └── social-media-manager.md
```

## 6.2 Composição de profiles

Tarefa resolve **profile stack**:

```
effective_profile = merge(
  agents/{actor}.md,
  franklin/{domain}.md,
  human/{role}? 
)
```

Exemplo Reel via ChatGPT:

- `agents/chatgpt.md` — conversação, sem filesystem  
- `franklin/social.md` — 9:16, tom, formatos  
- `franklin/visual.md` — coerência visual leve  

## 6.3 Crescimento

| Estágio | Ação |
|---------|------|
| Novo domínio criativo | `profiles/franklin/{domain}.md` + KB + module |
| Nova ferramenta IA | `profiles/agents/{tool}.md` — capacidades, limites |
| Novo colaborador | `profiles/human/{role}.md` |

## 6.4 Utilização

- Registry `profiles-index.yaml` mapeia `task_id → [franklin/*, agents default]`  
- Router permite override: `--agent claude`  
- Profile declara: leitura mínima, tom, ferramentas, anti-padrões  

---

# 7. Sistema de Specs

## 7.1 Anatomia de spec

```yaml
fce_spec:
  id: narrative
  version: 2.0.0
  module: narrative

inputs:
  required: [...]
  optional: [...]

dependencies:
  modules: [cds]
  gates: [cds_g1]

process:
  workflow_anchor: WORKFLOW.md#narrative-pipeline
  launcher: CREATE_VIDEO_VEO.md
  invariants:
    - prompt_composer_mandatory
    - no_manual_veo_prompts

outputs:
  required:
    - path: video/narrative/scenes.md
      schema: schemas/scenes.json
  optional: [...]

validation:
  gates:
    - id: narrative_complete
      rules: [...]
  checklist:
    - id: scenes_count
      rule: "count >= 1"
    - id: fields_per_scene
      rule: "fields == 17"

aliases:
  character.md: character-{slug}.md
  scenes.md: scenes/scene-*.md

compatibility:
  min_fce: "2.0.0"
```

## 7.2 Gates como specs

`fce/registry/gates.yaml` referencia `validators/rules/{gate}.py` e opcionalmente `specs/gates/{gate}.spec.yaml`.

## 7.3 Validação em camadas

1. **Schema** — YAML/JSON válido  
2. **Spec** — inputs/outputs presentes  
3. **Gate** — pré-requisitos de tarefa  
4. **Theological** — flag humana em VibeCore Alerts (não automatizar julgamento doutrinário final)  

---

# 8. Sistema de Templates

## 8.1 Organização

```
templates/
├── index.yaml              # Catálogo + spec binding
├── track/
├── campaign/
├── bible-study/
├── suno/
├── narrative/
├── veo3/
├── design/
└── copy/
```

## 8.2 Frontmatter obrigatório

```yaml
---
fce_template: track/base
fce_spec: track
version: 1.0.0
module: suno
language: pt-BR
---
```

## 8.3 Reutilização

- **Compose** — templates podem `include:` outros  
- **Override** — álbum pode ter `templates/overrides/album-04/`  
- **Derive** — carrossel deriva de hero template slice  

## 8.4 Versionamento

| Mudança | Versão |
|---------|--------|
| Typo, clarificação | PATCH |
| Nova seção opcional | MINOR |
| Remoção/rename campo | MAJOR — exige migração |

`fce migrate-template --from 1.x --to 2.x` (FCE 3+).

---

# 9. Sistema de IA

## 9.1 Modelo de navegação universal

Toda IA segue:

```
1. Entrada via FCE.md ou bundle exportado (fce export-session)
2. Router resolve task + scope
3. Profile stack aplicado
4. Context Pack — leitura ONLY listed files
5. Launcher thin — conversa
6. Execution Pack — ações
7. Entrega formato FCE
8. fce check (se agente tem shell)
```

## 9.2 Por ferramenta

| Ferramenta | Profile | Particularidades |
|------------|---------|------------------|
| **ChatGPT** | `agents/chatgpt.md` | Bundle exportado; sem filesystem; user cola pack |
| **Claude** | `agents/claude.md` | Projects + artefatos; long context — ainda respeitar budget |
| **Gemini** | `agents/gemini.md` | Multimodal; assets via manifest URLs |
| **Cursor** | `agents/cursor.md` | Filesystem; `fce check` local; edição repo |
| **Codex** | `agents/codex.md` | CI/automation; schema-first |
| **IA Local** | `agents/local.md` | Ollama etc.; bundle mínimo; offline KB subset |
| **Futuras** | `agents/_template.md` | Plugin registry adiciona profile |

## 9.3 Export de sessão

```bash
fce export-session \
  --task create_reel \
  --track 01 \
  --agent chatgpt \
  --format markdown \
  > session-bundle.md
```

Conteúdo: profile resumo + context pack inlined ou links + execution steps + gates status.

## 9.4 Anti-padrões globais IA

- Ler repo inteiro  
- Inventar faixas não no registry  
- Alterar `lyrics_final` sem `needs_review`  
- Prompt Veo manual  
- Pular gates  
- Expor secrets  

---

# 10. Sistema de Plugins

## 10.1 Modelo

```
plugins/
└── {publisher}.{name}/
    ├── plugin.yaml          # Manifest
    ├── module/              # Opcional: mini library
    ├── knowledge/           # Opcional: KB extension
    ├── specs/               # Opcional
    ├── validators/
    └── README.md
```

## 10.2 Manifest

```yaml
plugin:
  id: acme.podcast-engine
  version: 1.0.0
  fce_min: "3.0.0"
  registers:
    modules: [podcast]
    tasks: [create_podcast_episode]
    pipelines: [podcast_launch]
  dependencies:
    modules: [cds, copy]
```

## 10.3 Registro

`fce registry load plugins/acme.podcast-engine` → merge em `plugins.yaml` — CI valida aciclicidade.

## 10.4 Isolamento

Plugins **não** alteram `core/`, `fce/registry/tasks.yaml` core tasks, ou `FCE.md` — apenas estendem via registry merge.

---

# 11. Governança

## 11.1 Decisões arquiteturais — ADR

```
architecture/adr/
├── 0001-router-first.md
├── 0002-context-packs.md
└── template.md
```

Formato: Status · Context · Decision · Consequences · Alternatives.

## 11.2 Versionamento

| Artefato | Esquema |
|----------|---------|
| Blueprint | MAJOR.MINOR.PATCH |
| Registry packs | Semver por arquivo |
| Specs | Semver independente |
| KB | `stability` + semver |
| FCE platform | `fce_platform: "3.2.1"` em `fce/platform.yaml` |

## 11.3 Compatibilidade

- **Aliases** em specs para paths legados  
- **Deprecation window** — 2 versões MINOR antes de remover  
- **`fce_min`** em plugins e packs  

## 11.4 Evolução

| Nível | Quem aprova |
|-------|-------------|
| KB patch | Maintainer |
| Spec minor | Maintainer + review |
| Registry major | ADR + Blueprint amendment |
| Core charter | Franklin + ADR |

## 11.5 CHANGELOG

Keep a Changelog — toda fase de migração e release de plataforma documentada.

---

# 12. Roadmap Oficial

## FCE 2 — Plataforma Declarativa (2026–2027)

**Tema:** Fundação machine-readable.

| Entrega |
|---------|
| `fce/registry/*` completo |
| Context Packs todas as 13+ tarefas |
| Knowledge SSOT extraída de AGENTS |
| 7 profiles franklin + 6 agents |
| Specs core modules |
| `fce check` v1 |
| Launchers thin |
| Track 01 golden path validado |
| 3 faixas ciclo completo |

## FCE 3 — Automação e Escala (2027–2028)

**Tema:** Validar, orquestrar, replicar.

| Entrega |
|---------|
| Execution Packs completos |
| Pipelines declarativos |
| `scripts/fce` CLI maduro |
| Retrofit 12 faixas Álbum 4 |
| Plugins v1 |
| Template migration tool |
| CI contract tests |
| `library/canva`, `copy`, `theology` |
| Veo API scripts opcionais |

## FCE 4 — Plataforma Estendida (2028–2030)

**Tema:** Distribuição, métricas, colaboração.

| Entrega |
|---------|
| Asset manifest + storage abstraction |
| Segundo álbum template-ready |
| `fce export-session` maduro |
| Métricas campanha |
| Perfis human colaborativos |
| Portal devocional (MVP) |
| i18n pipeline (ES, EN) |
| SDK mínimo |

## FCE 5 — Ecossistema (2030–2036)

**Tema:** Referência aberta, comunidade, semi-automação ponta a ponta.

| Entrega |
|---------|
| Marketplace de plugins certificados |
| Multi-tenant ministries template |
| Salmo → reel publicado semi-automático |
| Dezenas de álbuns documentados |
| FCE como modelo aberto (licença definida) |
| IA local first-class |
| Métricas de impacto ministerial (opt-in) |

---

# 13. Manifesto de instância (faixa)

Estado final por track — `fce-status.yaml`:

```yaml
track:
  id: track-01
  album_id: album-04
  fce_platform: "3.0.0"

gates:
  lyrics_final: { status: passed, at: "2026-01-15" }
  cds_g1: { status: passed }
  cds_g2: { status: passed }
  hero_g25: { status: passed }
  narrative_complete: { status: passed }
  audio_master: { status: pending }

modules_applied:
  - suno
  - cds
  - narrative
  - veo3

assets_manifest: assets/manifest.yaml
campaign: campaigns/campaign-track-01/
```

---

# Apêndice A — Glossário

| Termo | Definição |
|-------|-----------|
| Session Bundle | Pacote gerado pelo Router para uma sessão |
| Gate | Pré-requisito verificável |
| Module | Engine metodológica em `library/` |
| Plugin | Extensão registrada sem alterar core |
| VibeCore | Identidade artística FCE |
| VibeShell | Método Suno |
| Golden Path | Track 01 como referência |

---

# Apêndice B — Relação com documentos existentes

| Documento atual | Evolução no estado final |
|-----------------|--------------------------|
| `FCE.md` | Router humano |
| `AGENTS.md` | Índice → `knowledge/` |
| `WORKFLOW.md` | Narrativa humana — complementa specs |
| `architecture/*` | Subset deste Blueprint — mantidos como referência rápida |
| `library/*` | Modules — inalterados em espírito |
| `launcher/*` | Thin — mesmos task_ids |

---

**Franklin Creative Engine — MASTER BLUEPRINT v1.0.0**  
*Especificação oficial. Implementação: ver MASTER_MIGRATION_PLAN.md.*
