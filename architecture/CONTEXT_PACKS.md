# Context Packs — Leitura Mínima de Contexto FCE 2.0

**Versão:** 2.0.0-sprint1.5  
**Status:** Conceito documentado — **packs físicos em `fce/context-packs/` não criados até Sprint 2**

---

## Propósito

Um **Context Pack** é uma lista **fechada e priorizada** de arquivos que uma IA deve ler para executar uma tarefa específica — nem mais, nem menos.

Context Packs implementam o princípio **P4 — Leitura mínima de contexto** (`PRINCIPLES.md`) e são resolvidos pelo **Registry** (`REGISTRY.md`) a partir de `task_id` + escopo da faixa.

---

## Problema que resolve

| Situação atual | Com Context Pack |
|----------------|------------------|
| Launcher lista 15+ arquivos "obrigatórios" | Pack lista 4–8 arquivos **para esta tarefa** |
| IA lê `WORKFLOW.md` inteiro (679 linhas) | Pack aponta âncora `#workflow-5` ou KB equivalente |
| Políticas copiadas do `AGENTS.md` no chat | Pack referencia `@fce/knowledge/...` |
| Sem distinção Track 01 vs álbum inteiro | Pack recebe `{album_id, track_id}` como escopo |
| Gates verificados manualmente | Pack só é emitido se gates passarem (futuro) |

**Meta:** reduzir tokens e tempo de onboarding em 50–70% por tarefa.

---

## Definição formal

```
Context Pack = {
  task_id,           # ex.: create_reel
  scope: { album, track },
  always:  [],       # arquivos sempre lidos
  modules: [],       # subset de library/ — não o módulo inteiro
  knowledge: [],     # IDs @fce/knowledge/...
  track: [],         # paths relativos à faixa
  conditional: [],   # se arquivo X ausente, ler Y
  excludes: []       # explicitamente NÃO ler
}
```

---

## Anatomia de um Context Pack

### Camada 1 — `always` (universal da tarefa)

Arquivos mínimos independentes da faixa — ou com path parametrizado.

```yaml
always:
  - architecture/PRINCIPLES.md          # opcional: só P4,P8 para tarefas simples
  - launcher/CREATE_REEL.md
  - knowledge/software/agent-conventions.md  # futuro — formato de entrega
```

**Regra:** `always` deve ter **≤ 3 entradas** após consolidação KB.

---

### Camada 2 — `modules` (subset do método)

Referência a **arquivos específicos** dentro de `library/` — nunca "ler pasta inteira".

```yaml
modules:
  - library/narrative_engine/07_prompt_composer.md
  - library/veo3/prompt-rules.md
  # NÃO: library/narrative_engine/ (inteiro)
```

---

### Camada 3 — `knowledge` (políticas por ID)

```yaml
knowledge:
  - "@fce/knowledge/social/formats-916"
  - "@fce/knowledge/software/security"
```

Equivalente markdown até KB existir — Registry mantém tabela de fallback.

---

### Camada 4 — `track` (instância da faixa)

Paths relativos a `albums/.../tracks/track-{NN}-{slug}/`:

```yaml
track:
  - track.yaml
  - concept.md
  - video/narrative/hook.md
  - video/narrative/scenes.md
  - video/veo3-prompts.md
```

**Parametrização:** `{track_path}` resolvido em runtime a partir de escopo.

---

### Camada 5 — `conditional` (leitura sob demanda)

```yaml
conditional:
  - if_missing: design/design-specification.md
    read:
      - library/creative_direction_system/01_creative_brief.md
    action: "Executar CDS G2 antes de continuar"
  - if_gate_failed: hero_g25
    read:
      - launcher/CREATE_HERO_ASSET.md
    action: "BLOCKED — aprovar Hero primeiro"
```

---

### Camada 6 — `excludes` (anti-padrões explícitos)

```yaml
excludes:
  - WORKFLOW.md                    # inteiro — usar âncora via knowledge
  - albums/*/tracks/track-02-*     # outras faixas fora do escopo
  - library/suno/                  # domínio música irrelevante para reel
```

Tornar explícito o que **não** carregar evita over-reading por IAs cautelosas.

---

## Exemplo completo (conceitual)

```yaml
# fce/context-packs/create_reel.yaml — NÃO IMPLEMENTADO
fce_context_pack: create_reel
version: 1.0.0
task_id: create_reel
profile: franklin/social

always:
  - launcher/CREATE_REEL.md

modules:
  - library/narrative_engine/07_prompt_composer.md
  - library/veo3/prompt-rules.md

knowledge:
  - "@fce/knowledge/social/formats-916"

track:
  - track.yaml
  - video/narrative/hook.md
  - video/narrative/scenes.md
  - video/veo3-prompts.md
  - video/filmora/edit-notes.md

conditional:
  - if_gate_failed: narrative_complete
    read:
      - WORKFLOW.md#narrative-pipeline
    action: BLOCKED
  - if_missing: assets/audio/
    action: WARN — reel ideal com áudio master

excludes:
  - library/suno/
  - design/carousel-production.md
  - WORKFLOW.md

estimated_files: 8
estimated_lines_max: 2500
```

---

## Context Pack por categoria de tarefa

| Categoria | Pack típico (arquivos) | Módulos | Excluir |
|-----------|------------------------|---------|---------|
| **Música** | 6–8 | suno | narrative, veo3 |
| **Visual / Hero** | 8–10 | cds | suno, veo3 |
| **Vídeo / Veo** | 8–12 | narrative, veo3 | suno |
| **Copy** | 4–6 | copy (futuro) | veo3, suno |
| **Campanha** | 12–15 | cds, campaign | — (orquestra) |
| **Nova faixa** | 5–7 | suno (parcial) | narrative |

---

## Resolução de Context Pack

```
┌─────────────────────────────────────────────────────────┐
│ 1. Registry: task_id → context_pack template            │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│ 2. Scope: resolver {album_id, track_id} → track_path  │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│ 3. Gate Evaluator: filtrar conditional blocked          │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│ 4. Expandir track[] com paths absolutos relativos       │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│ 5. Aplicar excludes                                     │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│ 6. OUTPUT: lista ordenada para IA + metadata            │
│    { files[], blocked, warnings, profile }              │
└─────────────────────────────────────────────────────────┘
```

---

## Context Pack vs Launcher

| Context Pack | Launcher |
|--------------|----------|
| **O que ler** | **Como conduzir** a conversa |
| Lista fechada de arquivos | Perguntas ao usuário |
| Machine-readable (YAML) | Markdown conversacional |
| Gerado pelo Registry | Escrito por humano/arquiteto |
| Varia por escopo da faixa | Estrutura estável por tarefa |

**Futuro thin launcher:** launcher referencia `context_pack: create_reel` em vez de listar 15 arquivos inline.

---

## Context Pack vs Profile

| Profile | Context Pack |
|---------|--------------|
| Define **papel** e tom | Define **arquivos** |
| `franklin/music.md` | `create_suno_song.yaml` |
| Estável por domínio | Estável por tarefa |
| Injetado uma vez | Resolvido com escopo track |

Profile + Pack = contexto completo mínimo.

---

## Fallback sem Registry (hoje)

Até Sprint 2, IAs devem simular Context Pack manualmente:

1. Abrir launcher da tarefa
2. Ler apenas arquivos listados em "Arquivos que a IA deve consultar"
3. Não ler `WORKFLOW.md` inteiro — só seção referenciada
4. Escopo: uma faixa por sessão

---

## Métricas de qualidade de um Pack

| Critério | Meta |
|----------|------|
| Arquivos em `always` | ≤ 3 |
| Total de arquivos | ≤ 12 (exceto campanha) |
| Linhas estimadas | ≤ 3.000 |
| Módulos como pasta inteira | 0 |
| Duplicação de AGENTS | 0 — usar knowledge IDs |
| `excludes` declarados | ≥ 1 para tarefas especializadas |

---

## Evolução por sprint

| Sprint | Entrega Context Pack |
|--------|---------------------|
| 1.5 | Conceito (este documento) |
| 2 | `create_suno_song.yaml`, `create_hero_asset.yaml` |
| 3 | Packs para todas tarefas vídeo + CDS |
| 4 | Launchers thin referenciam packs |
| 5 | `fce export-context --task X --track 01` |

---

## Compatibilidade

- Packs não existem fisicamente na Sprint 1.5
- Launchers atuais mantêm listas inline — válidas até thin refactor
- Nenhum arquivo operacional alterado

---

**Versão:** Sprint 1.5 · 2026-07-03
