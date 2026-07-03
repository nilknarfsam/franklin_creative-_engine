# Módulos — Conceito e Fronteiras FCE 2.0

**Versão:** 2.0.0-sprint1

---

## O que é um módulo no FCE

Um **módulo** é uma unidade de capacidade com:

- **Domínio claro** — o que resolve (ex.: direção cinematográfica, áudio Suno)
- **Entradas declaradas** — o que precisa existir antes
- **Processo documentado** — método em `library/` ou workflow em `WORKFLOW.md`
- **Saídas padronizadas** — paths sob `albums/.../tracks/`
- **Independência relativa** — pode evoluir sem quebrar outros módulos se contratos forem respeitados

Módulos **não** são pastas de faixa. `albums/.../track-01/` é uma **instância de produção**, não um módulo.

---

## Taxonomia de componentes

| Conceito | Onde vive | Contém | Não contém |
|----------|-----------|--------|------------|
| **Launcher** | `launcher/` | Roteiro conversacional, perguntas, checklist | Método profundo, políticas globais |
| **Module / Library** | `library/` | Método, engines, regras de domínio | Letras, prompts de faixa, binários |
| **Knowledge** | `knowledge/` [futuro] | Políticas SSOT, glossário, referências | Instâncias de track |
| **Profile** | `profiles/` [futuro] | Contexto por papel criativo | Workflows completos |
| **Template** | `templates/` | Scaffold de saída com placeholders | Lógica de decisão |
| **Spec** | `specs/` [futuro] | Contrato: entrada, processo, saída, validação | Prosa longa de método |
| **Output** | `albums/` | Artefatos finais por faixa/álbum | Método reutilizável |

---

## Launcher vs Module

```
┌─────────────────────────────────────────────────────────────┐
│  LAUNCHER = "O que fazer agora" (tarefa conversacional)      │
│  - Qual faixa?                                               │
│  - Quais arquivos consultar?                                 │
│  - Qual checklist antes de entregar?                         │
└────────────────────────────┬────────────────────────────────┘
                             │ delega método
┌────────────────────────────▼────────────────────────────────┐
│  MODULE = "Como fazer bem" (engine permanente)               │
│  - Fases do VibeShell                                        │
│  - 8 módulos do Narrative Engine                             │
│  - CDS brief → spec → review                                 │
└─────────────────────────────────────────────────────────────┘
```

**Exemplo:** `CREATE_VIDEO_VEO.md` (launcher) aponta para `library/narrative_engine/07_prompt_composer.md` (módulo). O launcher não reescreve o Prompt Composer.

---

## Module vs Knowledge

| Module | Knowledge |
|--------|-----------|
| Ensina **processo** | Armazena **verdade estável** |
| `library/suno/vibeshell-method.md` — 6 fases | `knowledge/music/vibecore-principles.md` — princípios VibeCore |
| Pode ter 400+ linhas de método | Políticas curtas, referenciáveis por ID |
| Versão evolui com método | Mudança rara, revisão humana |

**Futuro:** launchers referenciam `@fce/knowledge/...` em vez de copiar trechos de `AGENTS.md`.

---

## Module vs Template

| Module | Template |
|--------|----------|
| Explica **por quê** e **como pensar** | Define **formato do arquivo de saída** |
| `library/creative_direction_system/01_creative_brief.md` | `templates/` não existe creative-brief-template ainda — output segue módulo CDS |
| Leitura durante produção | Cópia uma vez por instância |

Templates **derivam** de specs (futuro). Modules **informam** o preenchimento.

---

## Module vs Spec

| Module | Spec |
|--------|------|
| Documentação humana legível | Contrato verificável (YAML/JSON) |
| Narrativa, exemplos, filosofia | Campos obrigatórios, gates, paths |
| `library/narrative_engine/03_scene_builder.md` | `specs/narrative.spec.yaml` (futuro) |

Specs permitem `fce check track-01` validar conformidade sem ler 1.700 linhas.

---

## Catálogo de módulos implementados

| ID | Path | Status | Outputs típicos |
|----|------|--------|-----------------|
| `cds` | `library/creative_direction_system/` | ✅ | `design/creative-brief.md`, `design-specification.md`, `creative-review.md` |
| `narrative` | `library/narrative_engine/` | ✅ | `video/narrative/*`, `director-commentary.md` |
| `veo3` | `library/veo3/` | ✅ | `video/veo3-prompts.md` |
| `suno` | `library/suno/` | ✅ | `lyrics.md`, `suno/prompt.txt`, `technical-sheet.md` |

## Catálogo de módulos planejados

| ID | Path futuro | Domínio |
|----|-------------|---------|
| `canva` | `library/canva/` | Brand kit, tokens por álbum |
| `copy` | `library/copy/` | Hooks, CTAs, tom cristão |
| `theology` | `library/theology/` | Notas exegéticas por Salmo |
| `campaign` | Orquestrado via WF7 + launcher futuro | Calendário editorial |

---

## Fronteiras entre módulos

### CDS → Narrative

CDS fornece: tom, paleta, símbolos, guardrails visuais.  
Narrative consome: `design-specification.md`, `identity/track_identity.md`.  
Narrative **não** redefine estratégia de campanha.

### Narrative → Veo3

Narrative produz: cenas, personagem, emoção, composição via Prompt Composer.  
Veo3 valida: 6 elementos, `no text`, 9:16, continuidade.  
Veo3 **não** substitui Narrative Pipeline.

### Suno ∥ CDS

Produção musical é **paralela** à direção visual. Campanha une ambos.

### Hero → Derivação Canva

Hero é output do módulo CDS + execução visual. Carrossel/story/thumb **derivam** do Hero aprovado — não são módulos separados, são tarefas (launchers) sobre o mesmo módulo CDS.

---

## Como adicionar um novo módulo

1. Documentar em `architecture/MODULES.md` (este arquivo) — ID, path, dependências
2. Criar `library/{modulo}/` com README index
3. Adicionar seção em `PROJECT_STRUCTURE.md`
4. Criar launcher se houver tarefa conversacional dedicada
5. Atualizar `WORKFLOW.md` se novo pipeline ponta a ponta
6. Registrar em `CHANGELOG.md`
7. (Futuro) Adicionar `specs/{modulo}.spec.yaml`

---

## Compatibilidade FCE 1.x

Todos os módulos em `library/` existentes **permanecem** a autoridade metodológica. Esta taxonomia não renomeia pastas nem move arquivos.

---

**Versão:** Sprint 1 · 2026-07-03
