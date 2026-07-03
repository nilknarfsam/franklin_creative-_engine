# Arquitetura FCE 2.0 — Visão Geral

**Versão:** 2.0.0-sprint1.5 (consolidação arquitetural)  
**Status:** Em migração incremental — compatível com FCE 1.x  
**Autoridade operacional atual:** `FCE.md`, `AGENTS.md`, `WORKFLOW.md` (inalterados)

---

## Propósito

O Franklin Creative Engine (FCE) evolui de um repositório documentado para um **sistema operacional criativo modular**. A arquitetura FCE 2.0 organiza o crescimento futuro sem quebrar paths, letras, assets ou workflows existentes.

Esta pasta (`architecture/`) é a **fonte de verdade arquitetural** — define conceitos, dependências, princípios, registry, context packs e plano de migração. A implementação física de `fce/`, `profiles/`, `knowledge/` e `specs/` ocorre em sprints posteriores.

---

## Arquitetura declarativa (modelo alvo)

O fluxo canônico FCE 2.0 segue esta cadeia — da restrição à instância:

```
PRINCÍPIOS → REGISTRY → CONTEXT PACKS → ROUTER → LAUNCHERS
    → MODULES → KNOWLEDGE → TEMPLATES → OUTPUT
```

### Diagrama da cadeia declarativa

```
┌─────────────────────────────────────────────────────────────────────┐
│  PRINCÍPIOS (PRINCIPLES.md)                                         │
│  Constraints inegociáveis — P1–P14                                  │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ informa
┌───────────────────────────────▼─────────────────────────────────────┐
│  REGISTRY (fce/tasks · modules · gates)          [Sprint 2+]        │
│  Índice declarativo — o que existe, IDs, dependências               │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ resolve
┌───────────────────────────────▼─────────────────────────────────────┐
│  CONTEXT PACKS (fce/context-packs/*)             [Sprint 2+]        │
│  Leitura mínima — lista fechada de arquivos por tarefa + escopo     │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ alimenta
┌───────────────────────────────▼─────────────────────────────────────┐
│  ROUTER (FCE.md → evolução declarativa)                             │
│  Hoje: menu · Futuro: resolve task + gates + pack                   │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│  LAUNCHERS (launcher/CREATE_*.md)                                   │
│  Roteiro conversacional thin → delega método e política             │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
┌────────▼────────┐   ┌─────────▼─────────┐   ┌───────▼────────┐
│ MODULES         │   │ KNOWLEDGE         │   │ TEMPLATES      │
│ library/*       │   │ knowledge/*       │   │ templates/*    │
│ método          │   │ políticas SSOT    │   │ formato saída  │
└────────┬────────┘   └─────────┬─────────┘   └───────┬────────┘
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│  OUTPUT — albums/.../tracks/ · campaigns/ · assets/                 │
│  Instâncias de produção (letras, design, vídeo, binários)           │
└─────────────────────────────────────────────────────────────────────┘
```

### Papel de cada elo

| Elo | Função | Documento |
|-----|--------|-----------|
| **Princípios** | Por quê e limites de decisão | [PRINCIPLES.md](./PRINCIPLES.md) |
| **Registry** | Índice declarativo da plataforma | [REGISTRY.md](./REGISTRY.md) |
| **Context Packs** | Leitura mínima por tarefa | [CONTEXT_PACKS.md](./CONTEXT_PACKS.md) |
| **Router** | Entrada e orquestração | `FCE.md` |
| **Launchers** | Playbook conversacional | `launcher/` |
| **Modules** | Engines metodológicas | `library/` |
| **Knowledge** | Políticas canônicas | `knowledge/` [futuro] |
| **Templates** | Contratos de saída | `templates/` |
| **Output** | Artefatos por faixa | `albums/` |

**Specs** (`specs/` — futuro) validam contratos entre elos; ver [SPECS.md](./SPECS.md).  
**Profiles** (`profiles/franklin/` — futuro) filtram contexto por papel; ver [PROFILES.md](./PROFILES.md).

---

## Camadas da arquitetura (visão estrutural)

```
┌─────────────────────────────────────────────────────────────────┐
│                    CORE (Governança)                             │
│  VISION · ROADMAP · AGENTS · WORKFLOW · PROJECT_STRUCTURE       │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│              ARCHITECTURE META-CAMADA (architecture/)            │
│  PRINCIPLES · REGISTRY* · CONTEXT_PACKS* · DEPENDENCIES · ...   │
│  * conceito Sprint 1.5 — implementação física Sprint 2+         │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│         CAMADA DECLARATIVA (fce/ — Sprint 2+)                    │
│  tasks.yaml · modules.yaml · gates.yaml · context-packs/        │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    ROUTER — FCE.md                               │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
              Launchers → Modules → Knowledge → Templates → Output
```

---

## Princípios

Os 14 princípios fundamentais estão documentados em **[PRINCIPLES.md](./PRINCIPLES.md)**.

Resumo executivo:

1. Escritura como fonte · 2. Repositório SSOT · 3. Additive not destructive  
4. Leitura mínima · 5. Módulos independentes · 6. Router-first (evolução)  
7. Separação método/política/instância · 8. Gates explícitos · 9. Hero primeiro  
10. Narrative antes de Veo · 11. Compatibilidade FCE 1.x · 12. Idioma e tom  
13. Segurança · 14. Qualidade sobre velocidade genérica

---

## Componentes

### Core

Documentação normativa e identidade do projeto na raiz e em `docs/`.

| Artefato | Função |
|----------|--------|
| `VISION.md` | Missão, VibeCore, princípios teológicos |
| `AGENTS.md` | Regras operacionais para IAs |
| `WORKFLOW.md` | Pipelines ponta a ponta (9 workflows + CDS + Narrative) |
| `PROJECT_STRUCTURE.md` | Paths, schemas, convenções |
| `ROADMAP.md` | Fases de entrega |
| `CHANGELOG.md` | Histórico de versões |

O Core **não é substituído** pela camada `architecture/` — complementa com visão estrutural de longo prazo.

### Registry (conceito — Sprint 1.5)

Índice declarativo machine-readable: tarefas, módulos, gates, profiles. Ver [REGISTRY.md](./REGISTRY.md).

**Implementação física:** `fce/` — Sprint 2.

### Context Packs (conceito — Sprint 1.5)

Listas fechadas de arquivos por tarefa + escopo da faixa. Ver [CONTEXT_PACKS.md](./CONTEXT_PACKS.md).

**Implementação física:** `fce/context-packs/` — Sprint 2.

### Router

**Atual:** `FCE.md` apresenta menu de 13 tarefas e aponta para launchers.

**Futuro:** consome Registry + Context Packs + gate evaluation antes de abrir launcher.

### Launchers

Playbooks conversacionais em `launcher/`. Orientam a IA sem substituir `AGENTS.md` ou `WORKFLOW.md`.

Cada launcher: objetivo → ordem de leitura → perguntas → arquivos → saídas → checklist → proibições.

**Evolução:** thin launchers referenciam Context Pack por ID em vez de listar arquivos inline.

### Modules / Library

Engines metodológicas permanentes em `library/`. Contêm **como** executar (método), não **instâncias** de produção.

| Módulo | Path | Domínio |
|--------|------|---------|
| CDS | `library/creative_direction_system/` | Direção criativa estratégica |
| Narrative | `library/narrative_engine/` | Direção cinematográfica |
| Video Engine | `library/veo3/` | Validação e execução Veo |
| Suno / VibeShell | `library/suno/` | Produção musical |

### Knowledge (futuro)

Base de conhecimento canônica em `knowledge/` — políticas, glossário, referências por domínio. Ver [KNOWLEDGE.md](./KNOWLEDGE.md).

### Profiles (futuro)

Perfis de contexto por papel criativo em `profiles/franklin/`. Ver [PROFILES.md](./PROFILES.md).

### Specs (futuro)

Contratos machine-readable por tarefa/módulo em `specs/`. Ver [SPECS.md](./SPECS.md).

### Templates

Modelos de saída em `templates/`. Copiar → preencher → salvar sob `albums/`. Nunca editar originais.

### Assets

Binários (áudio, vídeo, imagens) em `albums/.../assets/`. Gitignored conforme política. Paths referenciados em markdown.

### Examples (futuro)

Pasta reservada para exemplos completos e referências de implementação (ex.: Track 01 como golden path).

### History

Documentos históricos permanecem onde estão (raiz, manuais VibeShell, dossiê legado). **Não mover nesta migração.**

---

## Relação com a estrutura atual (FCE 1.x)

| FCE 1.x | FCE 2.0 |
|---------|---------|
| Governança na raiz | Core + `architecture/` meta-camada |
| FCE.md = menu | FCE.md → router declarativo |
| Leitura ad hoc | Context Packs por tarefa |
| Deps implícitas | Registry (`fce/*.yaml`) |
| Launchers fatos | Launchers thin + pack refs |
| Políticas duplicadas | Knowledge SSOT |
| library/ = método | Modules indexados no Registry |

---

## Documentos desta pasta

| Arquivo | Conteúdo |
|---------|----------|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | Este documento — visão geral e cadeia declarativa |
| [PRINCIPLES.md](./PRINCIPLES.md) | 14 princípios fundamentais |
| [REGISTRY.md](./REGISTRY.md) | Índice declarativo da plataforma |
| [CONTEXT_PACKS.md](./CONTEXT_PACKS.md) | Leitura mínima por tarefa |
| [DEPENDENCIES.md](./DEPENDENCIES.md) | Modelo de dependências e fluxo de leitura |
| [MODULES.md](./MODULES.md) | Conceito de módulo e fronteiras |
| [PROFILES.md](./PROFILES.md) | Sistema de perfis (planejado) |
| [KNOWLEDGE.md](./KNOWLEDGE.md) | Knowledge base (planejada) |
| [SPECS.md](./SPECS.md) | Padrão de specs por tarefa |
| [MIGRATION.md](./MIGRATION.md) | Plano de migração por sprints |

---

## Leitura recomendada

1. [PRINCIPLES.md](./PRINCIPLES.md) — constraints antes de qualquer mudança
2. Este arquivo — visão geral e cadeia declarativa
3. [REGISTRY.md](./REGISTRY.md) + [CONTEXT_PACKS.md](./CONTEXT_PACKS.md) — modelo de execução mínima
4. [DEPENDENCIES.md](./DEPENDENCIES.md) — antes de criar novos módulos
5. [MIGRATION.md](./MIGRATION.md) — estado da migração e próximas sprints

Para operação do dia a dia, continue usando **FCE.md → launcher → WORKFLOW/AGENTS**.

---

**Versão:** Sprint 1.5 — Consolidação Arquitetural · 2026-07-03
