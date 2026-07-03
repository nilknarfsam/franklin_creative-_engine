# Registry — Índice Declarativo da Plataforma FCE 2.0

**Versão:** 2.0.0-sprint1.5  
**Status:** Conceito documentado — **arquivos físicos em `fce/` não criados até Sprint 2**

---

## Propósito

O **Registry** é o índice declarativo machine-readable da plataforma FCE. Centraliza o que existe, como se relaciona e como é encontrado — sem duplicar conteúdo metodológico de `library/` ou políticas de `knowledge/`.

**Analogia:** Registry é o **catálogo e mapa**; Modules são os **manuais**; Knowledge é a **constituição**; Output são as **obras produzidas**.

---

## O que o Registry é

| Característica | Descrição |
|----------------|-----------|
| **Declarativo** | Descreve estado desejado e referências — não executa produção |
| **Indexador** | Aponta para paths, IDs e dependências |
| **Versionável** | YAML/JSON em git com histórico |
| **Consultável** | Humano, IA ou script (`fce check` futuro) leem o mesmo índice |
| **Evolutivo** | Cresce por sprint sem quebrar entradas anteriores |

---

## O que o Registry não é

| Anti-padrão | Por quê |
|-------------|---------|
| Substituto de `library/` | Registry indexa — não ensina método |
| Substituto de `AGENTS.md` | AGENTS permanece operacional até consolidação KB |
| Banco de letras ou prompts | Instâncias vivem em `albums/` |
| Executor de tarefas | Router + Launcher executam; Registry informa |
| Configuração de secrets | `.env` local — nunca no Registry |

---

## Localização planejada

```
fce/
├── README.md              # Índice da camada declarativa
├── tasks.yaml             # Catálogo de tarefas (menu FCE → launcher)
├── modules.yaml           # Catálogo de módulos e dependências
├── gates.yaml             # Definição de gates G1, G2, G2.5, narrative...
├── profiles-index.yaml    # Mapeamento tarefa → profile
└── context-packs/         # Packs por task_id [ou embutido em tasks.yaml]
    ├── create_reel.yaml
    ├── create_suno_song.yaml
    └── ...
```

**Sprint 1.5:** estrutura e conceito documentados aqui.  
**Sprint 2:** criação física de `fce/README.md`, `fce/tasks.yaml`, `fce/modules.yaml`.

---

## Componentes do Registry

### 1. Task Registry (`fce/tasks.yaml`)

Mapeia cada tarefa do menu FCE para launcher, módulos, gates e context pack.

```yaml
# Exemplo conceitual — NÃO IMPLEMENTADO
fce_version: "2.0.0"
tasks:
  create_reel:
    menu_id: 5
    title: "Criar Reel"
    launcher: launcher/CREATE_REEL.md
    profile: profiles/franklin/social.md
    modules: [narrative, veo3]
    gates: [cds_g1, narrative_complete]
    context_pack: context-packs/create_reel.yaml
    outputs:
      - "assets/video/track-{NN}-reel-9x16.mp4"
    spec: specs/veo-prompt.spec.yaml  # futuro
```

**Responsabilidade:** responder "o que é esta tarefa e do que ela precisa?"

---

### 2. Module Registry (`fce/modules.yaml`)

Catálogo de módulos com path, dependências e outputs típicos.

```yaml
# Exemplo conceitual — NÃO IMPLEMENTADO
modules:
  narrative:
    id: narrative
    path: library/narrative_engine/
    depends_on: [track, cds]
    blocks: [veo3-prompts, veo_generation, reel]
    outputs:
      - video/narrative/hook.md
      - video/narrative/scenes.md
      - video/narrative/director-commentary.md
    spec: specs/narrative.spec.yaml  # futuro

  suno:
    id: suno
    path: library/suno/
    depends_on: [track]
    parallel: true
    blocks: []
    outputs:
      - lyrics.md
      - suno/prompt.txt
      - technical-sheet.md
```

**Responsabilidade:** responder "quais módulos existem e como se ordenam?"

---

### 3. Gate Registry (`fce/gates.yaml`)

Define gates, critérios e arquivos que comprovam aprovação.

```yaml
# Exemplo conceitual — NÃO IMPLEMENTADO
gates:
  cds_g2:
    id: cds_g2
    label: "Design Specification aprovada"
  hero_g25:
    id: hero_g25
    label: "Hero Asset aprovado"
    validates:
      - path: assets/hero/approved/
        rule: directory_not_empty_or_readme_approved
  narrative_complete:
    id: narrative_complete
    requires_files:
      - video/narrative/hook.md
      - video/narrative/character.md
      - video/narrative/scenes.md
      - video/narrative/director-commentary.md
```

**Responsabilidade:** responder "esta faixa pode iniciar esta tarefa?"

---

### 4. Profile Index (`fce/profiles-index.yaml`)

Mapeia tarefas e domínios a profiles Franklin.

```yaml
# Exemplo conceitual — NÃO IMPLEMENTADO
profiles:
  franklin/music:
    path: profiles/franklin/music.md
    domains: [suno, lyrics, mastering]
  franklin/visual:
    path: profiles/franklin/visual.md
    domains: [cds, hero, canva]

task_profile_map:
  create_suno_song: [franklin/music, franklin/theology]
  create_hero_asset: [franklin/visual, franklin/artist]
```

---

## Fluxo Registry no sistema

```
                    ┌──────────────────┐
                    │   PRINCIPLES     │
                    │  (constraints)   │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │     REGISTRY     │
                    │ tasks · modules  │
                    │ gates · profiles │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼────────┐    │    ┌─────────▼─────────┐
     │ Context Pack    │    │    │ Gate Evaluator    │
     │ (leitura mín.)  │    │    │ [fce check futuro]│
     └────────┬────────┘    │    └─────────┬─────────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────▼─────────┐
                    │  Router (FCE.md) │
                    └────────┬─────────┘
                             ▼
                    Launcher → Modules → Output
```

---

## IDs estáveis

Convenção de identificadores no Registry:

| Tipo | Padrão | Exemplo |
|------|--------|---------|
| Task | `snake_case` | `create_reel`, `create_suno_song` |
| Module | `snake_case` | `narrative`, `cds`, `suno` |
| Gate | `{domínio}_g{n}` ou descritivo | `cds_g2`, `hero_g25` |
| Profile | `franklin/{nome}` | `franklin/music` |
| Knowledge | `@fce/knowledge/{domínio}/{slug}` | `@fce/knowledge/design/hero-review` |
| Context Pack | mesmo id da task | `create_reel` |

IDs são **imutáveis** após publicação — mudanças de path atualizam campo `path`, não o `id`.

---

## Relação Registry ↔ documentos existentes

| Hoje (FCE 1.x) | Registry (FCE 2.0) |
|----------------|-------------------|
| Menu em `FCE.md` | `tasks.yaml` espelha menu 1–13 |
| Ordem de leitura em launchers | `context_pack` por task |
| Grafo em `DEPENDENCIES.md` | `modules.yaml` machine-readable |
| Gates em `AGENTS.md` / `WORKFLOW.md` | `gates.yaml` |
| Catálogo em `MODULES.md` | `modules.yaml` |
| Profiles em `PROFILES.md` | `profiles-index.yaml` + arquivos |

**Durante migração:** documentos markdown permanecem autoridade legível; Registry é camada adicional.

---

## Resolução de tarefa (algoritmo futuro)

```
INPUT: task_id, album_id, track_id

1. LOAD task from fce/tasks.yaml
2. EVALUATE gates against track path
   IF any gate FAIL → RETURN blocked + remediation launcher
3. BUILD context_pack from task.context_pack + track scope
4. LOAD profile from profiles-index
5. OPEN launcher (thin)
6. RETURN { pack, profile, launcher, gates_passed }
```

**Sprint 1.5:** algoritmo documentado. Implementação em Sprint 2–5.

---

## Extensibilidade

Para adicionar nova tarefa ao Registry (futuro):

1. Definir princípios aplicáveis (`PRINCIPLES.md`)
2. Registrar módulo se novo (`modules.yaml`)
3. Criar entrada em `tasks.yaml`
4. Definir `context_pack`
5. Criar ou referenciar launcher
6. Atualizar `FCE.md` menu (quando router humano)
7. Registrar em `CHANGELOG.md`

---

## Compatibilidade

- Nenhum arquivo em `fce/` existe na Sprint 1.5
- `FCE.md` não é alterado
- Produção continua via menu + launchers manuais
- Registry é especificação — implementação Sprint 2

---

**Versão:** Sprint 1.5 · 2026-07-03
