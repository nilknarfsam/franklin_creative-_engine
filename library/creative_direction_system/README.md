# Creative Direction System (CDS) — Franklin Creative Engine

**Framework permanente de direção criativa estratégica.** Ensina qualquer agente de IA a transformar uma **música** em um **projeto criativo profissional** — antes de qualquer pixel, prompt ou export.

| Regra | Detalhe |
|-------|---------|
| Gera imagens? | **Não** |
| Gera vídeos? | **Não** |
| Gera prompts Veo/Suno? | **Não** |
| Escopo | Todos os álbuns, todas as faixas, todas as campanhas |
| Output | Brief estratégico + especificação de design + revisão aprovada |

---

## Propósito

O CDS responde à pergunta que vem **depois** da letra e **antes** da produção:

> *Como esta faixa deve existir no mundo — visualmente, emocionalmente, teologicamente e comercialmente — como um projeto coerente de nível profissional?*

Enquanto o Narrative Engine pensa como **diretor de cinema** e o Video Engine executa **clips**, o CDS pensa como **diretor de criação de agência**: estratégia, sistema visual, tom de campanha e critérios de aprovação.

**Problema que resolve:** Música excelente com design genérico, vídeo desconectado, copy inconsistente e campanha sem fio condutor.

**Solução CDS:** Uma camada documentada que alinha **todos** os entregáveis de uma faixa antes da execução em ferramentas.

---

## Posição na arquitetura FCE

```
                    ┌─────────────────────────┐
                    │   Música (letra + áudio) │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  CREATIVE DIRECTION     │  ← CDS (este módulo)
                    │  Brief → Spec → Review  │
                    └────────────┬────────────┘
           ┌─────────────────────┼─────────────────────┐
           │                     │                     │
  ┌────────▼────────┐   ┌────────▼────────┐   ┌──────▼──────┐
  │ Narrative Engine │   │ Design (Canva)  │   │ Copy / Campanha │
  │ (direção vídeo)  │   │ (assets visuais)│   │ (publicação)    │
  └────────┬────────┘   └─────────────────┘   └─────────────────┘
           │
  ┌────────▼────────┐
  │  Prompt Engine  │  (Prompt Composer — narrative_engine/07)
  └────────┬────────┘
           │
  ┌────────▼────────┐
  │  Video Engine   │  (library/veo3/ — execução Veo)
  └─────────────────┘
```

**Ordem obrigatória para campanha completa:**

1. Faixa documentada (`track.yaml`, `lyrics.md`, `concept.md`)
2. **CDS** — brief → design spec → creative review aprovado
3. Módulos de execução em paralelo ou sequência conforme entregável

---

## Módulos do CDS

| # | Arquivo | Função |
|---|---------|--------|
| 01 | [01_creative_brief.md](./01_creative_brief.md) | Brief estratégico de nível agência |
| 02 | [02_design_specification.md](./02_design_specification.md) | Brief → especificações visuais sistemáticas |
| 03 | [03_creative_review.md](./03_creative_review.md) | Aprovação, checklists e gates de qualidade |

---

## Conexão com o Narrative Engine

| CDS fornece | Narrative Engine consome |
|-------------|--------------------------|
| Tom emocional dominante da campanha | `emotion_id` por cena |
| Símbolos visuais aprovados (estratégia) | `symbol_id` em Scene Builder |
| Público e promessa de retenção | Decisão de hook |
| Paleta e mood visual macro | Cinematography + color palette |
| Proibições de brand (anti-kitsch) | Guardrails no Prompt Composer |

**Regra:** O Narrative Engine **não** redefine estratégia de campanha. Se houver conflito entre `creative-brief.md` e `hook.md`, o brief CDS prevalece — registrar divergência no creative review.

**Path por faixa (vídeo):** `tracks/.../video/narrative/` executa após CDS aprovado.

---

## Conexão com o Prompt Engine

O **Prompt Engine** no FCE é o [Prompt Composer](../narrative_engine/07_prompt_composer.md) — montagem técnica de prompts Veo a partir de campos narrativos.

| CDS fornece | Prompt Engine consome |
|-------------|----------------------|
| Visual style e photography direction | Blocos de luz, cor, estética |
| Hierarquia emocional da campanha | `emotion_id` e modifiers |
| Restrições de brand | Guardrails FCE reforçados |
| Objetivo dramático macro | Objetivo por cena (derivado) |

**Regra:** O Prompt Engine **nunca** recebe brief cru. Recebe cenas já documentadas no Narrative Engine, que por sua vez foram alinhadas ao CDS.

```
CDS (estratégia) → Narrative Engine (cenas) → Prompt Composer (prompts EN) → Video Engine (Veo)
```

---

## Conexão com Design

| CDS fornece | Design (Canva) consome |
|-------------|------------------------|
| `02_design_specification.md` completo | `design/design-specification.md` por faixa |
| Grid, tipografia, cores, hierarquia | Templates e kits visuais |
| Formatos e responsividade | Dimensões por plataforma |
| Tom fotográfico e composição | Direção de arte em carrosséis e capas |

**Output operacional:** `tracks/.../design/design-specification.md` derivado do template CDS.  
**Execução:** `design/canva-brief.md` traduz spec em tarefas Canva — não substitui a spec.

**Regra:** Nenhum asset Canva entra em produção sem design specification aprovada no creative review.

---

## Conexão com Veo (Video Engine)

O **Video Engine** (`library/veo3/`) é a camada de **execução** — regras de prompt, continuidade, aspect ratio e validação API.

| CDS fornece | Video Engine valida |
|-------------|---------------------|
| Mood visual e paleta macro | Coerência com `prompt-rules.md` |
| Proibições de iconografia | Negative prompts e guardrails |
| Prioridade 9:16 para social | Aspect ratio em todo prompt |
| Objetivo de campanha (reel vs clip) | Duração e formato por entregável |

**Regra:** Veo só é acionado após **CDS aprovado** + **Narrative Pipeline completo** + **prompts compostos**.

Ver [WORKFLOW.md](../../WORKFLOW.md) § Creative Direction Pipeline e § Workflow 9.

---

## Outputs por faixa

```
tracks/track-XX-{slug}/design/
├── creative-brief.md           # CDS 01 — estratégia
├── design-specification.md     # CDS 02 — sistema visual
├── creative-review.md          # CDS 03 — aprovações e checklists
└── canva-brief.md              # Operacional (derivado da spec)
```

**Manifest opcional:** `design/creative-manifest.yaml` — IDs, status, versões (futuro).

---

## Quando usar o CDS

| Situação | Ação |
|----------|------|
| Nova faixa com campanha planejada | CDS completo antes de Canva/Veo |
| Apenas letra + Suno | CDS pode aguardar — marcar `status: concept` |
| Retrofit de faixa existente | CDS antes de redesign ou novo vídeo |
| Lançamento de álbum | CDS por faixa + CDS de álbum (macro brand) |
| Rebrand visual | Atualizar spec + novo creative review |

---

## Checklist CDS (gate global)

- [ ] `creative-brief.md` completo (todos os campos do template 01)
- [ ] `design-specification.md` completo (todos os elementos do 02)
- [ ] `creative-review.md` com aprovações assinadas (03)
- [ ] Narrative Engine alinhado ao brief (se vídeo)
- [ ] Nenhum VibeCore Alert aberto
- [ ] Status em `track.yaml` ou manifest atualizado

---

## Links externos

- [VISION.md](../../VISION.md) — VibeCore e princípios teológicos
- [WORKFLOW.md](../../WORKFLOW.md) — Creative Direction Pipeline
- [AGENTS.md](../../AGENTS.md) — regras para agentes
- [library/narrative_engine/](../narrative_engine/) — direção cinematográfica
- [library/veo3/](../veo3/) — Video Engine

**Versão:** 1.0.0 — Sprint 5
