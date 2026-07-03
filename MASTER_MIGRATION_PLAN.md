# MASTER MIGRATION PLAN — Franklin Creative Engine

**Documento:** Plano mestre de migração FCE 1.x → estado final (MASTER_BLUEPRINT v1.0.0)  
**Versão:** 1.0.0  
**Metodologia:** Engenharia orientada por arquitetura — fases com critérios de aceite, não micro-sprints  
**Referência:** [MASTER_BLUEPRINT.md](./MASTER_BLUEPRINT.md)  
**Estado de partida:** FCE 1.x — `architecture/` Sprint 1–1.5 concluídas; Registry físico ausente

---

## Visão geral das fases

```
FASE 0          FASE 1           FASE 2           FASE 3           FASE 4           FASE 5
Consolidação    Declarativa      Knowledge &      Validação &      Automação &      Ecossistema
Blueprint       Registry         Profiles         Thin Layer       Pipelines        (FCE 4–5)
    │               │                │                │                │                │
    ▼               ▼                ▼                ▼                ▼                ▼
 MASTER_*      fce/registry/    knowledge/       launchers thin   execution-packs   plugins SDK
 docs          context-packs    profiles/        fce check        veo scripts       portal
```

| Fase | Alinhamento Blueprint | Horizonte estimado |
|------|----------------------|-------------------|
| 0 | Documentação canônica | Concluída com este plano |
| 1 | FCE 2 — Registry + Router prep | 2–3 meses |
| 2 | FCE 2 — KB + Profiles + Specs | 2–3 meses |
| 3 | FCE 2 — Validators + Launchers | 2 meses |
| 4 | FCE 3 — Execution + Pipelines | 3–4 meses |
| 5 | FCE 3–4 — Produção Álbum 4 + CLI | 4–6 meses |
| 6 | FCE 4 — Assets + Colaboração | 6+ meses |
| 7 | FCE 5 — Plugins + Ecossistema | longo prazo |

---

## Estado atual (baseline)

| Componente | Status |
|------------|--------|
| `FCE.md` | Menu 13 tarefas — operacional |
| `launcher/` | 13 playbooks — fat (~90L cada) |
| `library/` | CDS, Narrative, Veo3, Suno — maduro |
| `architecture/` | 10 docs conceituais |
| `albums/album-04/` | 12 faixas; Track 01 piloto (~32 arquivos) |
| `fce/registry/` | ❌ Não existe |
| `knowledge/` | ❌ Não existe |
| `profiles/` | ❌ Não existe |
| `specs/` | ❌ Não existe |
| `validators/` | ❌ Não existe |
| Legado raiz | Dossiê + manuais VibeShell — presentes |

---

# FASE 0 — Consolidação do Blueprint

## Objetivo

Estabelecer especificação oficial de longo prazo e plano de migração sem alterar operação.

## Arquivos envolvidos

| Ação | Arquivos |
|------|----------|
| Criar | `MASTER_BLUEPRINT.md`, `MASTER_MIGRATION_PLAN.md` |
| Referenciar | `architecture/*`, `VISION.md`, `AGENTS.md` |
| Atualizar | `CHANGELOG.md`, `PROJECT_STRUCTURE.md` (índice aos MASTER_*) |

## Dependências

Nenhuma — fase fundacional.

## Critérios de aceite

- [ ] Blueprint cobre 13 seções obrigatórias + apêndices
- [ ] Migration Plan com ≥7 fases detalhadas
- [ ] Nenhum arquivo operacional alterado
- [ ] ADR template referenciado em Blueprint §11

## Rollback

Remover `MASTER_*.md` — zero impacto operacional.

## Riscos

| Risco | Mitigação |
|-------|-----------|
| Blueprint desalinhado da realidade | Baseline documentado; aliases Track 01 |
| Paralisia por escopo | Fases com entregáveis incrementais |

## Validação

Revisão humana Franklin — aprovação explícita do Blueprint como north star.

**Status:** ✅ Em conclusão com entrega deste documento.

---

# FASE 1 — Camada Declarativa (Registry)

## Objetivo

Materializar Registry machine-readable: tasks, modules, gates — sem alterar `FCE.md` como router ativo.

## Arquivos envolvidos

| Criar | Atualizar |
|-------|-----------|
| `fce/README.md` | `PROJECT_STRUCTURE.md` |
| `fce/registry/tasks.yaml` (13 tarefas) | `CHANGELOG.md` |
| `fce/registry/modules.yaml` | `architecture/MIGRATION.md` → deprecar sprints |
| `fce/registry/gates.yaml` | `core/` ou manter raiz (decisão ADR-0003) |
| `fce/schema/*.json` | |
| `fce/context-packs/*.yaml` (13 packs) | |
| `architecture/adr/0001-registry.md` | |

## Dependências

- Fase 0 aprovada
- `architecture/REGISTRY.md`, `CONTEXT_PACKS.md`, `PRINCIPLES.md`

## Critérios de aceite

- [ ] `tasks.yaml` espelha menu FCE 1–13 com IDs estáveis
- [ ] `modules.yaml` acíclico — validado por script ou review
- [ ] `gates.yaml` cobre G1, G2, G2.5, narrative_complete, lyrics_final
- [ ] 13 context packs com `budget.max_files ≤ 12` (exceto campanha ≤18)
- [ ] JSON Schema valida todos os YAMLs em CI (ou `fce validate-registry`)
- [ ] Track 01 paths resolvíveis em todos os packs de tarefas aplicáveis
- [ ] `FCE.md` **inalterado**

## Rollback

```bash
git revert <commit-fase-1>
# Remove fce/ — launchers e library intactos
```

## Riscos

| Risco | Prob | Impacto | Mitigação |
|-------|------|---------|-----------|
| Drift registry vs launchers | Alta | Médio | Geração futura a partir de registry |
| YAML churn | Média | Baixo | Schema + review |
| Over-spec Track 01 aliases | Média | Baixo | `aliases` em gates |

## Validação

```bash
fce validate-registry          # schema OK
fce resolve --task create_reel --track 01 --dry-run  # bundle preview
```

Manual: comparar cada `context-pack` com launcher equivalente — mesmos arquivos essenciais.

---

# FASE 2 — Knowledge Base + Profiles + Specs

## Objetivo

SSOT de políticas; profiles operacionais; contratos verificáveis por módulo.

## Arquivos envolvidos

| Criar | Extrair de |
|-------|------------|
| `knowledge/index.yaml` | — |
| `knowledge/theology/fidelity-rules.md` | `VISION.md`, `AGENTS.md` |
| `knowledge/design/hero-review-checklist.md` | `AGENTS.md` Hero § |
| `knowledge/software/security.md` | `AGENTS.md` |
| `knowledge/software/repo-rules.md` | `AGENTS.md`, `PROJECT_STRUCTURE.md` |
| `knowledge/music/vibecore-principles.md` | `VISION.md` |
| `knowledge/narrative/*.md` | `library/veo3/`, `AGENTS.md` |
| `knowledge/marketing/tone-fce.md` | `WORKFLOW.md` WF5 |
| `profiles/franklin/*.md` (7) | `architecture/PROFILES.md` |
| `profiles/agents/*.md` (6) | Novo |
| `specs/track.spec.yaml` | `PROJECT_STRUCTURE.md` |
| `specs/narrative.spec.yaml` | `library/narrative_engine/` |
| `specs/cds.spec.yaml` | `library/creative_direction_system/` |
| `specs/suno.spec.yaml` | `library/suno/` |
| `specs/veo-prompt.spec.yaml` | `library/veo3/` |
| `specs/hero-asset.spec.yaml` | `AGENTS.md` |
| `specs/campaign.spec.yaml` | `WORKFLOW.md` WF7 |
| `specs/README.md` | — |

| Atualizar | Mudança |
|-----------|---------|
| `AGENTS.md` | Reduzir a índice + links `@fce/knowledge/` |
| `fce/registry/tasks.yaml` | Adicionar `knowledge[]` e `spec` por task |
| Context packs | Referenciar knowledge IDs |

## Dependências

- Fase 1 completa
- Aprovação teológica para extração KB `theology/`

## Critérios de aceite

- [ ] Zero duplicação: cada política crítica existe em **um** arquivo KB
- [ ] `AGENTS.md` ≤50% tamanho atual — resto em KB
- [ ] 7 profiles franklin + 6 agents com frontmatter `fce_profile`
- [ ] 7 specs com `validation` e `aliases` Track 01
- [ ] Context packs usam `knowledge[]` IDs — não copiam parágrafos
- [ ] `knowledge/index.yaml` lista todos os IDs

## Rollback

Reverter commits Fase 2. `AGENTS.md` restaurado do git. `knowledge/` removível sem impacto em `albums/`.

## Riscos

| Risco | Mitigação |
|-------|-----------|
| Perda de nuance teológica na extração | Review humano theologian-reviewer |
| IAs sem repo não resolvem `@fce/` IDs | `fce export-session` inclui KB inlined (Fase 4) |
| AGENTS muito reduzido | Manter índice com resumo 1 linha por política |

## Validação

```bash
fce validate-knowledge-index     # todos IDs resolvíveis
fce validate-specs --track 01    # Track 01 contra todas specs aplicáveis
```

Checklist manual: Hero Review checklist idêntico entre KB e `AGENTS` anterior.

---

# FASE 3 — Validators + Launchers Thin + Track Manifest

## Objetivo

Automatizar gates; reduzir launchers; manifest machine-readable por faixa.

## Arquivos envolvidos

| Criar | Modificar |
|-------|-----------|
| `validators/fce_check.py` | `launcher/*.md` (13 → thin) |
| `validators/rules/*.py` | `CHANGELOG.md` |
| `validators/schemas/` | |
| `scripts/fce` (CLI entry) | |
| `albums/.../track-01/fce-status.yaml` | |
| `albums/.../track-01/assets/manifest.yaml` | |
| `architecture/adr/0002-thin-launchers.md` | |
| `tests/contract/test_registry.py` | |
| `tests/golden/track-01-resolve.json` | |

## Dependências

- Fase 1 (registry)
- Fase 2 (specs, KB)

## Critérios de aceite

- [ ] `fce check track 01` executa sem erro em Track 01 piloto
- [ ] Gates blocked retornam `remediation` com launcher_id
- [ ] 13 launchers ≤50 linhas média
- [ ] Launchers referenciam `task_id` — não listam 10+ arquivos inline
- [ ] `fce-status.yaml` Track 01 reflete gates reais
- [ ] Contract tests em CI
- [ ] **Letras e prompts finais inalterados**

## Rollback

```bash
git checkout HEAD~N -- launcher/
# Restaurar launchers fatos
rm validators/ tests/contract/
```

## Riscos

| Risco | Mitigação |
|-------|-----------|
| ChatGPT-only users perdem listas inline | `fce export-session` |
| False negatives em gates | WARN vs BLOCK; human override flag |
| Thin launcher muito thin | Manter perguntas essenciais |

## Validação

```bash
fce check track 01 --verbose
fce check task create_carousel --track 01  # deve PASS após Hero
pytest tests/contract/
```

Golden: snapshot `fce resolve` estável entre releases PATCH.

---

# FASE 4 — Router Ativo + Execution Packs + Pipelines

## Objetivo

`FCE.md` consome registry; execution packs para tarefas complexas; pipeline campanha declarativo.

## Arquivos envolvidos

| Criar | Modificar |
|-------|-----------|
| `fce/execution-packs/*.yaml` | `FCE.md` — adicionar seção resolução + link `fce resolve` |
| `fce/registry/pipelines.yaml` | |
| `fce/router/resolution.md` | |
| `pipelines/track-launch.yaml` | |
| `pipelines/campaign-full.yaml` | |
| `launcher/CREATE_CAMPAIGN.md` | |
| `fce/export-session` (subcomando) | |

## Dependências

- Fase 3 (`fce check` estável)

## Critérios de aceite

- [ ] `FCE.md` instrui: consultar `fce resolve` antes de produzir
- [ ] Menu 9 aponta `CREATE_CAMPAIGN.md` + pipeline `campaign_full`
- [ ] Execution packs para: campanha, reel, video_veo, suno_song, hero
- [ ] `fce export-session --task X --track 01` gera bundle para ChatGPT
- [ ] Pipeline `track_launch` documentado e validável
- [ ] Router blocked path testado (carrossel sem Hero → BLOCKED)

## Rollback

Reverter `FCE.md` e remover `execution-packs/`. Registry e validators permanecem úteis.

## Riscos

| Risco | Mitigação |
|-------|-----------|
| FCE.md complexo demais | Manter menu simples; detalhes em `fce/router/` |
| Execution pack desatualizado vs tools | Versionar packs; link `knowledge/platforms/` |

## Validação

```bash
fce resolve --task create_campaign --track 01
fce export-session --task create_reel --track 01 --agent chatgpt -o /tmp/bundle.md
fce check pipeline track_launch --track 01
```

Teste humano: colar bundle no ChatGPT — produção sem acesso ao repo.

---

# FASE 5 — Produção Álbum 4 + Automação Veo + Retrofit

## Objetivo

Fechar ciclo criativo em 3+ faixas; scripts Veo; retrofit 02–12 com narrative scaffold.

## Arquivos envolvidos

| Criar | Modificar |
|-------|-----------|
| `scripts/video/generate_scene.py` | `scripts/retrofit_track.py` |
| `scripts/retrofit_album_04_v2.py` | `migrate_album_04.py` (deprecate) |
| `albums/.../tracks/track-02..03/fce-status.yaml` | |
| Narrative scaffold tracks 02–12 | |
| `campaigns/campaign-track-01/` | |
| Binários em `assets/` (local, gitignored) | |
| `docs/PROJECT_STATUS_REPORT.md` (auto ou manual) | |

## Dependências

- Fase 4 (pipelines)
- Áudio Suno Track 01 (humano)
- Aprovação Veo API (humano)

## Critérios de aceite

- [ ] Track 01: áudio + ≥1 reel 9:16 + campanha 7 dias documentada
- [ ] Tracks 02–03: CDS + identity + narrative scaffold via retrofit
- [ ] `fce check track 02` passa gates aplicáveis ao stub
- [ ] Veo script gera clip sem secrets no repo
- [ ] ROADMAP Fase 1 critério: 3 faixas ciclo completo
- [ ] Track 03 VibeCore Alert resolvido ou documentado

## Rollback

Scripts opcionais — desligar sem afetar docs. Retrofit por faixa com backup git.

## Riscos

| Risco | Mitigação |
|-------|-----------|
| Retrofit sobrescreve lyrics | Opt-in flag; nunca touch `lyrics_final` |
| API costs Veo | Manual path permanece |
| Scope creep álbum inteiro | 3 faixas gate explícito |

## Validação

```bash
fce check track 01 --all
fce check pipeline track_launch --track 01
```

Review humano: qualidade ministerial — fora do escopo automatizado.

---

# FASE 6 — Core Reorganização + History + Examples

## Objetivo

Reorganizar governança em `core/`; arquivar legado; formalizar golden examples.

## Arquivos envolvidos

| Criar | Mover (com redirect) |
|-------|---------------------|
| `core/VISION.md` | `VISION.md` → redirect |
| `core/CHARTER.md` | Consolida PRINCIPLES + VISION princípios |
| `core/AGENTS.md` | Índice final |
| `core/WORKFLOW.md` | |
| `history/README.md` | |
| `history/legacy/dossie-monolitico.md` | cópia redirect |
| `history/legacy/vibeshell-manuals/` | |
| `examples/track-complete/README.md` | → Track 01 |
| `examples/minimal-track/` | fixture |
| ADR-0004-core-restructure | |

## Dependências

- Fases 1–4 estáveis
- Links externos ao dossiê raiz inventariados

## Critérios de aceite

- [ ] Todos links internos repo atualizados ou redirects
- [ ] Raiz ≤15 arquivos markdown (excl. MASTER, README, FCE)
- [ ] `history/` mapeia 100% legado raiz
- [ ] Zero broken links (`tests/link_check.py`)
- [ ] CHANGELOG documenta moves

## Rollback

Git revert — symlinks ou redirects restauram paths antigos.

## Riscos

| Risco | Mitigação |
|-------|-----------|
| Links externos quebrados | `history/` stubs com mesmo path? Manter stubs raiz 1 release |
| Confusão colaboradores | README migration notice |

## Validação

```bash
pytest tests/link_check.py
fce validate-registry
```

---

# FASE 7 — Plugins + SDK + FCE 4–5 (longo prazo)

## Objetivo

Extensibilidade sem alterar core; SDK; segundo álbum; portal MVP.

## Arquivos envolvidos

| Criar |
|-------|
| `plugins/_template/` |
| `fce/registry/plugins.yaml` |
| `plugins/fce.podcast-stub/` (exemplo) |
| `sdk/typescript/` ou `sdk/python/` |
| `fce/platform.yaml` |
| `albums/album-05-*/` (quando aprovado) |
| `docs/portal-mvp.md` |

## Dependências

- Fases 1–6
- ADR marketplace plugins
- Decisão licenciamento FCE 5

## Critérios de aceite

- [ ] Plugin template registra módulo sem editar `tasks.yaml` core
- [ ] `fce registry load` valida plugin manifest
- [ ] SDK resolve task programaticamente
- [ ] Segundo álbum criado só via templates + registry
- [ ] Documentação FCE 5 em ROADMAP atualizada

## Rollback

Plugins desregistráveis — `plugins.yaml` entry remove.

## Riscos

| Risco | Mitigação |
|-------|-----------|
| Plugin quebra gates | Sandbox validation |
| SDK drift | Gerar from schema |

## Validação

```bash
fce plugin validate plugins/fce.podcast-stub
fce check --plugin-load podcast-stub
sdk smoke test
```

---

# Matriz de dependências entre fases

```
F0 ──► F1 ──► F2 ──► F3 ──► F4 ──► F5
                  │           │
                  └───────────┴──► F6 ──► F7
```

| Fase | Bloqueia |
|------|----------|
| F1 | F2, F3, F4 (registry) |
| F2 | F3 (specs), F4 (export KB) |
| F3 | F4 (router confiável) |
| F4 | F5 (campanha orquestrada) |
| F5 | F6 (produção validada) |
| F6 | F7 (core estável) |

**Paralelizável:** F5 produção humana (Suno, Veo, Canva) paralela a F3 se registry F1 pronto.

---

# Governança de migração

## ADRs obrigatórios

| ADR | Fase |
|-----|------|
| 0001-registry | F1 |
| 0002-thin-launchers | F3 |
| 0003-core-vs-root | F1 ou F6 |
| 0004-core-restructure | F6 |
| 0005-execution-packs | F4 |
| 0006-plugins | F7 |

## Critério de release de plataforma

```
FCE Platform X.Y.Z released quando:
- Registry schema valid
- fce check passa no golden path
- CHANGELOG completo
- MASTER_BLUEPRINT compat field atualizado
- Nenhum gate BLOCKED no track piloto para tarefas P0
```

## Comunicação

Cada fase concluída → entrada `CHANGELOG.md` + atualização `fce/platform.yaml` + opcional `docs/PROJECT_STATUS_REPORT.md`.

---

# O que NÃO migrar (preservação permanente)

| Item | Motivo |
|------|--------|
| Letras `lyrics_final` | Direitos autorais |
| `suno/prompt.txt` aprovados | Produção musical |
| `veo3-prompts.md` compostos | Pipeline validado |
| Binários aprovados | Assets finais |
| `legal/dossie-direitos-autorais.md` | Legal — cópia em history apenas |

---

# Resumo executivo

| Fase | Entrega chave | FCE equiv |
|------|---------------|-----------|
| 0 | Blueprint + este plano | — |
| 1 | Registry + Context Packs | FCE 2 início |
| 2 | KB + Profiles + Specs | FCE 2 core |
| 3 | Validators + Thin launchers | FCE 2 completo |
| 4 | Router + Execution + Pipelines | FCE 3 início |
| 5 | Álbum 4 produção + retrofit | FCE 3 |
| 6 | Core + History + Examples | FCE 3–4 |
| 7 | Plugins + SDK + escala | FCE 4–5 |

---

**Próxima ação recomendada:** Aprovar MASTER_BLUEPRINT v1.0.0 → iniciar **Fase 1** (Registry físico).

---

*Franklin Creative Engine — MASTER MIGRATION PLAN v1.0.0 · 2026-07-03*
