# Migração FCE 2.0 — Plano Incremental

**Versão:** 2.0.0-sprint1  
**Metodologia:** 10 mudanças por sprint · additive only · zero breaking changes

---

## Visão geral

A migração de FCE 1.x para FCE 2.0 ocorre em **sprints de 10 ações** cada. Cada sprint é autocontida, reversível e preserva compatibilidade com paths, letras, assets e workflows existentes.

```
FCE 1.x (atual)                    FCE 2.0 (alvo)
─────────────────                  ─────────────────
FCE.md = menu          ────────►   FCE.md = router declarativo
AGENTS = policy única  ────────►   Knowledge SSOT + AGENTS índice
Launchers fatos        ────────►   Launchers thin + refs
Deps implícitas        ────────►   specs/ + fce-modules.yaml
Sem validador          ────────►   fce check
```

---

## Regras de migração (todas as sprints)

1. **Não remover** arquivos sem sprint dedicada de consolidação
2. **Não mover** documentos históricos (dossiê raiz, manuais VibeShell)
3. **Não alterar** letras, prompts musicais finais, assets ou imagens
4. **Não quebrar** paths em `albums/`, `library/`, `launcher/`, `templates/`
5. **Documentar** toda mudança em `CHANGELOG.md`
6. **Atualizar** `PROJECT_STRUCTURE.md` quando novos paths forem criados
7. **Validar** contra Track 01 como golden path após cada sprint

---

## Sprint 1 — Fundação Arquitetural ✅

**Objetivo:** Criar camada `architecture/` documentando FCE 2.0 sem implementar router, profiles, knowledge ou specs físicos.

| # | Ação | Status |
|---|------|--------|
| 1 | Criar pasta `architecture/` | ✅ |
| 2 | Criar `architecture/ARCHITECTURE.md` | ✅ |
| 3 | Criar `architecture/DEPENDENCIES.md` | ✅ |
| 4 | Criar `architecture/MODULES.md` | ✅ |
| 5 | Criar `architecture/PROFILES.md` | ✅ |
| 6 | Criar `architecture/KNOWLEDGE.md` | ✅ |
| 7 | Criar `architecture/SPECS.md` | ✅ |
| 8 | Criar `architecture/MIGRATION.md` | ✅ |
| 9 | Atualizar `PROJECT_STRUCTURE.md` | ✅ |
| 10 | Atualizar `CHANGELOG.md` | ✅ |

**Não alterado:** `FCE.md`, `AGENTS.md`, `WORKFLOW.md`, letras, assets, profiles reais, knowledge real, specs reais.

---

## Sprint 2 — Registry Declarativo (planejada)

**Objetivo:** Primeiros arquivos machine-readable sem alterar FCE.md.

| # | Ação proposta |
|---|---------------|
| 1 | Criar `fce/README.md` — índice da camada declarativa |
| 2 | Criar `fce/tasks.yaml` — 13 tarefas + context packs mínimos |
| 3 | Criar `fce/modules.yaml` — grafo de dependências entre módulos |
| 4 | Criar `profiles/franklin/music.md` (primeiro profile real) |
| 5 | Criar `profiles/franklin/visual.md` |
| 6 | Criar `knowledge/software/security.md` — extrair de AGENTS |
| 7 | Criar `knowledge/design/hero-review.md` — extrair checklist 8 critérios |
| 8 | Criar `specs/README.md` — índice de specs |
| 9 | Atualizar `PROJECT_STRUCTURE.md` — paths `fce/`, `profiles/`, `knowledge/`, `specs/` |
| 10 | Atualizar `CHANGELOG.md` — Sprint 2 |

---

## Sprint 3 — Manifest Track 01 (planejada)

**Objetivo:** Estado machine-readable da faixa piloto.

| # | Ação proposta |
|---|---------------|
| 1 | Criar `albums/.../track-01-o-legado/fce-status.yaml` |
| 2 | Criar `specs/track.spec.yaml` |
| 3 | Criar `specs/narrative.spec.yaml` |
| 4 | Criar `specs/cds.spec.yaml` |
| 5 | Criar `profiles/franklin/theology.md` |
| 6 | Criar `profiles/franklin/social.md` |
| 7 | Criar `knowledge/theology/fidelity-rules.md` |
| 8 | Criar `knowledge/music/vibecore-principles.md` |
| 9 | Atualizar `architecture/MIGRATION.md` — marcar Sprint 3 |
| 10 | Atualizar `CHANGELOG.md` |

---

## Sprint 4 — Launcher Thin Piloto (planejada)

**Objetivo:** Refatorar 2 launchers para padrão thin + refs KB.

| # | Ação proposta |
|---|---------------|
| 1 | Refatorar `CREATE_HERO_ASSET.md` — remover duplicação, linkar KB |
| 2 | Refatorar `CREATE_VIDEO_VEO.md` — idem |
| 3 | Criar `specs/hero-asset.spec.yaml` |
| 4 | Criar `specs/veo-prompt.spec.yaml` |
| 5 | Criar `launcher/CREATE_CAMPAIGN.md` — fecha menu 9 |
| 6 | Adicionar entrada menu 9 em `FCE.md` apontando para novo launcher |
| 7 | Criar `profiles/franklin/writing.md` |
| 8 | Criar `knowledge/marketing/campaign-structure.md` |
| 9 | Atualizar `PROJECT_STRUCTURE.md` |
| 10 | Atualizar `CHANGELOG.md` |

---

## Sprint 5 — Validação e Profiles restantes (planejada)

| # | Ação proposta |
|---|---------------|
| 1 | Criar `scripts/fce_check.py` (read-only) |
| 2 | Criar `profiles/franklin/artist.md` |
| 3 | Criar `profiles/franklin/coding.md` |
| 4 | Criar `knowledge/software/repo-rules.md` |
| 5 | Criar `specs/suno.spec.yaml` |
| 6 | Criar `specs/campaign.spec.yaml` |
| 7 | Thin: `CREATE_SUNO_SONG.md` |
| 8 | Thin: `CREATE_CAROUSEL.md` |
| 9 | Sync `docs/PROJECT_STATUS_REPORT.md` |
| 10 | Atualizar `CHANGELOG.md` |

---

## Sprint 6+ — Escala e consolidação (backlog)

- Retrofit script v2 para tracks 02–12
- `library/canva/`, `library/copy/` implementados
- Thin launchers restantes
- `FCE.md` evolui para router com link `fce/tasks.yaml`
- `AGENTS.md` vira índice → Knowledge
- `archive/legacy/` com redirects (sem remoção)
- `fce export-context` CLI

---

## Critérios de conclusão FCE 2.0

| Critério | Meta |
|----------|------|
| Task registry | 13+ tarefas com context packs |
| Knowledge SSOT | Políticas críticas sem duplicação em launchers |
| Profiles | 7 profiles franklin operacionais |
| Specs | 7+ specs com validação |
| Golden path | Track 01 passa `fce check` |
| Retrofit | ≥3 faixas com manifest |
| Router | FCE.md resolve deps antes de launcher |

---

## Rollback

Cada sprint é reversível via git revert. Como sprints são aditivas, rollback = remover pasta/arquivos criados na sprint — **nunca** dependeu de remoção de legado.

---

## Referências

- [ARCHITECTURE.md](./ARCHITECTURE.md) — visão de componentes
- [DEPENDENCIES.md](./DEPENDENCIES.md) — grafo ideal
- [MODULES.md](./MODULES.md) — fronteiras
- `PROJECT_STRUCTURE.md` — paths canônicos
- `ROADMAP.md` — fases de produto (paralelo à migração técnica)

---

**Versão:** Sprint 1 concluída · 2026-07-03
