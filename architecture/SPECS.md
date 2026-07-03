# Specs — Padrão Planejado FCE 2.0

**Versão:** 2.0.0-sprint1  
**Status:** Padrão documentado — **arquivos `specs/*.yaml` não criados nesta sprint**

---

## Propósito

**Specs** são contratos verificáveis por tarefa ou módulo. Definem o que entra, o que acontece, o que sai e como validar — permitindo automação futura (`fce check`, gate evaluator).

Specs complementam:

- **Modules** (`library/`) — método legível por humanos
- **Templates** (`templates/`) — formato de arquivo de saída
- **Launchers** — roteiro conversacional

---

## Localização planejada

```
specs/
├── track.spec.yaml
├── narrative.spec.yaml
├── cds.spec.yaml
├── suno.spec.yaml
├── veo-prompt.spec.yaml
├── hero-asset.spec.yaml
├── campaign.spec.yaml
└── README.md
```

---

## Estrutura padrão de uma spec

Cada spec deve declarar cinco blocos:

### 1. Entrada esperada (inputs)

O que deve existir **antes** de iniciar a tarefa.

```yaml
inputs:
  required:
    - path: "tracks/track-XX-*/track.yaml"
      fields: [id, title, scripture, status]
    - path: "tracks/track-XX-*/concept.md"
  optional:
    - path: "tracks/track-XX-*/identity/track_identity.md"
```

### 2. Arquivos necessários (dependencies)

Módulos, knowledge e templates a consultar — **leitura mínima**.

```yaml
dependencies:
  modules:
    - library/narrative_engine/07_prompt_composer.md
  knowledge:
    - "@fce/knowledge/social/formats-916"
  templates: []
  gates:
    - narrative_complete
```

### 3. Processo (process)

Referência ao workflow e fases — não duplicar método inteiro.

```yaml
process:
  workflow: "WORKFLOW.md#narrative-pipeline"
  launcher: "launcher/CREATE_VIDEO_VEO.md"
  phases:
    - id: validate_narrative
      action: "Confirmar video/narrative/ completo"
    - id: compose_prompts
      action: "Executar Prompt Composer — sem escrita manual"
    - id: export
      action: "Atualizar video/veo3-prompts.md"
```

### 4. Saída esperada (outputs)

Paths e critérios de completude.

```yaml
outputs:
  required:
    - path: "video/veo3-prompts.md"
      format: markdown
      rules:
        - language: en
        - each_scene: 6_elements
        - suffix: "no text, no watermark"
  optional:
    - path: "video/veo3-video-plan.md"
```

### 5. Checklist de validação (validation)

Critérios pass/fail para humano ou script.

```yaml
validation:
  checklist:
    - id: narrative_exists
      check: "file_exists(video/narrative/scenes.md)"
      blocking: true
    - id: no_manual_prompts
      check: "prompt-composition.md references composer"
      blocking: true
    - id: aspect_ratio
      check: "default 9:16 unless documented exception"
      blocking: false
```

---

## Spec completa — exemplo (referência futura)

```yaml
# specs/veo-prompt.spec.yaml (NÃO CRIADO — exemplo)
fce_spec: veo-prompt
version: 1.0.0
task_id: create_video_veo
menu_id: 7

inputs:
  required:
    - path: "video/narrative/hook.md"
    - path: "video/narrative/character.md"
    - path: "video/narrative/scenes.md"
    - path: "video/narrative/director-commentary.md"

dependencies:
  modules:
    - narrative
    - veo3
  gates:
    - cds_g1
    - narrative_complete

process:
  workflow: "WORKFLOW.md#workflow-9"
  launcher: "launcher/CREATE_VIDEO_VEO.md"
  invariant: "Prompt Composer obrigatório — nunca prompt manual"

outputs:
  required:
    - path: "video/veo3-prompts.md"
    - path: "video/narrative/prompt-composition.md"

validation:
  checklist:
    - id: scenes_min
      rule: "scenes >= 1"
    - id: six_elements
      rule: "each scene declares character, environment, emotion, camera, lighting, dramatic_goal"
    - id: no_text
      rule: "all prompts include no text"
```

---

## Mapeamento Spec → Tarefa FCE

| Spec (futuro) | Menu FCE | Launcher |
|---------------|----------|----------|
| `suno.spec.yaml` | 13 | CREATE_SUNO_SONG |
| `track.spec.yaml` | 10 | CREATE_TRACK |
| `cds.spec.yaml` | 9 (parcial) | Campanha / CDS pipeline |
| `hero-asset.spec.yaml` | 3 | CREATE_HERO_ASSET |
| `narrative.spec.yaml` | 7 (pré) | Narrative Pipeline |
| `veo-prompt.spec.yaml` | 7 | CREATE_VIDEO_VEO |
| `campaign.spec.yaml` | 9 | Campanha completa |

---

## Spec vs Template

| Spec | Template |
|------|----------|
| Define **regras** e **validação** | Define **layout** do arquivo |
| `outputs.required` com invariantes | Seções `[PREENCHER]` |
| Machine-readable | Human-fillable |
| `specs/narrative.spec.yaml` | `templates/veo3-scene-template.md` |

Template deve declarar no frontmatter (futuro):

```yaml
---
fce_template: veo3-scene
fce_spec: narrative
version: 1.0.0
---
```

---

## Spec vs Module README

| Module README | Spec |
|---------------|------|
| Explica filosofia e fases | Lista campos obrigatórios |
| 200–400 linhas | 50–100 linhas YAML |
| Para aprendizado | Para verificação |

---

## Aliases e compatibilidade Track 01

Specs futuras devem aceitar variações do piloto sem quebrar validação:

| Spec path | Alias aceito (Track 01) |
|-----------|-------------------------|
| `video/narrative/character-{slug}.md` | `video/narrative/character.md` |
| `scenes/scene-{NN}.md` | `video/narrative/scenes.md` (monolítico) |
| `veo3-brief.md` | `veo3-video-plan.md` |

---

## Ferramentas futuras

| Ferramenta | Usa spec para |
|------------|---------------|
| `fce check track-01` | Validar gates e paths |
| `fce tasks.yaml` | Resolver dependencies |
| `fce export-context` | Montar pacote mínimo para ChatGPT |

**Sprint 1:** nenhuma ferramenta implementada.

---

## Compatibilidade

Specs não existem fisicamente. Validação continua manual via checklists em launchers e `AGENTS.md`.

---

**Versão:** Sprint 1 · 2026-07-03
