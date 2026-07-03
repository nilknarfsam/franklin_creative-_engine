# Dependências — Modelo FCE 2.0

**Versão:** 2.0.0-sprint1  
**Objetivo:** Definir o grafo ideal de dependências entre camadas, evitando leitura desnecessária e dependências circulares.

---

## Fluxo canônico

```
FCE.md (Router)
    │
    ▼
Launcher (launcher/CREATE_*.md)
    │
    ├──► Module / Library (library/*)     ← método e regras do domínio
    │
    ├──► Knowledge (knowledge/*)          ← políticas e referência [futuro]
    │
    ├──► Profile (profiles/franklin/*)    ← contexto por papel [futuro]
    │
    ├──► Template (templates/*)           ← formato de saída
    │
    └──► Spec (specs/*)                   ← contrato entrada/process/saída [futuro]
              │
              ▼
         Output (albums/.../tracks/...)
```

**Regra de ouro:** a dependência flui **sempre de cima para baixo**. Output nunca alimenta Router diretamente — apenas via releitura explícita em nova sessão.

---

## Direção permitida vs proibida

### Permitido

| De | Para | Exemplo |
|----|------|---------|
| Router | Launcher | FCE menu 7 → `CREATE_VIDEO_VEO.md` |
| Launcher | Module | Reel → `library/narrative_engine/` |
| Launcher | Template | Nova faixa → `templates/track-template.md` |
| Module | Module (acíclico) | Narrative → consome símbolos do CDS |
| Launcher | Output (leitura) | Carrossel → `design/design-specification.md` |
| Spec | Template | Spec define campos obrigatórios do template |
| Knowledge | Launcher (referência) | Policy linkada, não copiada |

### Proibido (dependências circulares)

| Padrão | Por quê |
|--------|---------|
| Output → Module (escrita) | Instância não altera método canônico |
| Template → Launcher | Template é contrato de saída, não roteiro |
| Module A ↔ Module B | Ciclos impedem ordem de leitura determinística |
| Knowledge → Output (geração) | KB é referência, não artefato de faixa |
| Profile → Module (substituição) | Profile contextualiza; não substitui engine |

---

## Grafo de módulos (estado atual + futuro)

```
                    ┌─────────────┐
                    │   track     │  (albums/.../track.yaml, concept, lyrics)
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
   ┌──────────┐     ┌──────────┐     ┌──────────────┐
   │   suno   │     │   cds    │     │ bible-study  │
   │ (audio)  │     │ (visual) │     │   (futuro)   │
   └────┬─────┘     └────┬─────┘     └──────────────┘
        │                │
        │         ┌──────┼──────┬────────────┐
        │         │      │      │            │
        │         ▼      ▼      ▼            ▼
        │    ┌────────┐ ┌────┐ ┌──────┐  ┌────────┐
        │    │identity│ │hero│ │narr. │  │ canva  │
        │    └────────┘ └──┬─┘ └──┬───┘  │(futuro)│
        │                    │      │      └────────┘
        │                    │      ▼
        │                    │  ┌───────┐
        │                    │  │ veo3  │
        │                    │  └───┬───┘
        │                    │      │
        └────────────────────┴──────┼──────────┐
                                    ▼          ▼
                              ┌─────────┐ ┌──────────┐
                              │ filmora │ │ campaign │
                              └─────────┘ └──────────┘
```

**Ordem de dependência (hard gates documentados):**

1. `track` — base de qualquer tarefa por faixa
2. `cds` G1 — brief aprovado antes de design spec
3. `cds` G2 — spec aprovada antes de Hero e Narrative
4. `hero` G2.5 — Hero aprovado antes de carrossel, story, thumbnail
5. `narrative` — completo antes de `veo3-prompts` e geração Veo
6. `suno` — paralelo a CDS (áudio independente de visual)
7. `campaign` — depende de CDS + assets individuais

---

## Leitura mínima por tarefa (princípio)

Cada launcher deve carregar apenas:

| Camada | Quando ler |
|--------|------------|
| **Core** | `AGENTS.md` — regras universais (resumo futuro via Profile) |
| **Launcher** | Sempre — roteiro da tarefa |
| **Module** | Apenas o(s) módulo(s) do domínio da tarefa |
| **Knowledge** | Políticas referenciadas pelo launcher (não o KB inteiro) |
| **Profile** | Um perfil alinhado ao papel (ex.: `visual.md` para Hero) |
| **Template** | Apenas o template da saída esperada |
| **Spec** | Contrato da tarefa (futuro) |
| **Output existente** | Somente arquivos listados no launcher para aquela faixa |

### Anti-padrões (leitura desnecessária)

- Ler `WORKFLOW.md` inteiro (679 linhas) para criar legenda → ler apenas WF5
- Ler `library/narrative_engine/` completo para Suno → ler apenas `library/suno/`
- Ler 12 faixas quando a tarefa é Track 01 → escopo explícito
- Copiar políticas do `AGENTS.md` no chat em vez de referenciar KB (futuro)

---

## Resolução de dependências (futuro)

Na Fase Router completa, o fluxo será:

```
1. Usuário escolhe tarefa + faixa
2. Router consulta task registry (fce/tasks.yaml — futuro)
3. Gate evaluator verifica pré-requisitos no path da faixa
4. Se BLOCKED → retorna tarefa/launcher que desbloqueia
5. Se OK → monta context_pack (lista mínima de arquivos)
6. Injeta Profile adequado
7. Abre Launcher thin
```

**Sprint 1:** apenas documentado. Comportamento atual permanece manual via launchers.

---

## Matriz launcher → dependências

| Launcher | Módulos | Gates | Templates |
|----------|---------|-------|-----------|
| CREATE_SUNO_SONG | suno | track (concept) | suno-prompt-template |
| CREATE_TRACK | — | album | track-template |
| CREATE_HERO_ASSET | cds | G2 | canva-kit-brief |
| CREATE_CAROUSEL | cds | G2, Hero G2.5 | canva-kit-brief |
| CREATE_VIDEO_VEO | narrative, veo3 | narrative complete | veo3-scene-template |
| CREATE_REEL | narrative, veo3 | narrative + audio ideal | — |
| CREATE_CAPTION | copy (futuro) | lyrics, brief | — |
| Campanha (menu 9) | cds, campaign | G1+G2, Hero | campaign-template |

---

## Compatibilidade

Este modelo **não altera** dependências já descritas em `WORKFLOW.md` e `AGENTS.md`. Formaliza e prepara automação futura (`fce check`, task registry).

---

**Versão:** Sprint 1 · 2026-07-03
