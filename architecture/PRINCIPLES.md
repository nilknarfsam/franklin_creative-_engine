# Princípios Fundamentais — FCE 2.0

**Versão:** 2.0.0-sprint1.5  
**Status:** Canônico para arquitetura — complementa `VISION.md` e `AGENTS.md` sem substituí-los  
**Autoridade operacional diária:** continua em `AGENTS.md` e `WORKFLOW.md`

---

## Propósito

Este documento consolida os **princípios inegociáveis** que governam decisões arquiteturais, de produto e de operação no Franklin Creative Engine. Toda sprint de migração, novo módulo ou mudança de processo deve ser avaliada contra estes princípios.

Princípios aqui são **estáveis** — mudam raramente e com revisão explícita. Implementações concretas (paths, YAMLs, launchers) evoluem em sprints.

---

## Hierarquia normativa

```
PRINCIPLES (este documento)     ← por quê existimos e como decidimos
        │
        ▼
VISION + AGENTS + WORKFLOW      ← identidade e operação (Core)
        │
        ▼
architecture/*                  ← como estruturamos o crescimento
        │
        ▼
Registry + Context Packs        ← como executamos com leitura mínima [futuro]
        │
        ▼
Output (albums/)                ← instâncias de produção
```

---

## P1 — Escritura como fonte

**Declaração:** Todo conceito, letra e decisão teológica ancora-se no texto bíblico da faixa — não em paráfrases de outros livros ou inspiração genérica.

**Implicações arquiteturais:**
- Knowledge `theology/` será domínio prioritário na KB
- Projetos bíblicos ativam Verificação Teológica Estrita (VibeShell)
- Dúvidas viram **VibeCore Alerts** documentados — nunca resolvidas em silêncio no chat

---

## P2 — Repositório como fonte única de verdade

**Declaração:** O repositório é a memória oficial do FCE. O chat não substitui arquivos versionados.

**Implicações arquiteturais:**
- Registry aponta para paths reais — não inventa faixas ou letras
- Context Packs listam arquivos consultáveis — não resumos de sessão anterior
- Mudanças significativas registradas em `CHANGELOG.md`
- Status de faixa futuramente em `fce-status.yaml` por track

---

## P3 — Additive, not destructive

**Declaração:** Evolução arquitetural adiciona camadas sem remover legado até sprint explícita de consolidação.

**Implicações arquiteturais:**
- Dossiê e manuais históricos permanecem na raiz durante migração
- `AGENTS.md` coexiste com Knowledge até extração completa
- Novos paths (`fce/`, `knowledge/`, `profiles/`) são aditivos
- Rollback de sprint = revert git, sem dependência de remoção prévia

---

## P4 — Leitura mínima de contexto

**Declaração:** Cada tarefa carrega apenas o contexto necessário para executá-la com qualidade — nem mais, nem menos.

**Implicações arquiteturais:**
- Context Packs definem listas fechadas de arquivos por tarefa
- Launchers não devem exigir leitura de `WORKFLOW.md` inteiro
- Profiles filtram domínio — música não carrega Narrative Engine completo
- Anti-padrão: ler 12 faixas quando a tarefa é Track 01

---

## P5 — Módulos independentes com contratos claros

**Declaração:** Cada engine em `library/` possui domínio, entradas, saídas e fronteiras explícitas.

**Implicações arquiteturais:**
- Módulos não alteram instâncias de faixa (`albums/`) como método
- Dependências entre módulos são acíclicas (ver `DEPENDENCIES.md`)
- Specs futuras formalizam contratos; Modules documentam método
- Suno ∥ CDS — áudio e visual em paralelo até campanha unir

---

## P6 — Router-first (evolução)

**Declaração:** `FCE.md` evoluirá para roteador central que resolve tarefa, dependências e contexto antes da produção.

**Implicações arquiteturais:**
- Sprint 1–1.5: FCE.md permanece menu — princípio é direção, não estado atual
- Registry declarativo alimentará o router (`fce/tasks.yaml` — Sprint 2)
- Gate evaluation antes de iniciar tarefas bloqueadas
- Humano ou IA escolhe tarefa; router monta pacote — não assume tarefa

---

## P7 — Separação método / política / instância

**Declaração:** Três camadas de conteúdo não se misturam.

| Camada | Onde | Exemplo |
|--------|------|---------|
| **Método** | `library/` | VibeShell 6 fases |
| **Política** | `knowledge/` [futuro] | Regra da Alma |
| **Instância** | `albums/` | `lyrics.md` Track 01 |

**Implicações:** Launchers delegam método a Modules e política a Knowledge — não duplicam.

---

## P8 — Gates explícitos antes de produção

**Declaração:** Entregáveis downstream exigem aprovação documentada dos upstream.

| Gate | Bloqueia |
|------|----------|
| G1 — Creative Brief | Design specification |
| G2 — Design Spec | Hero, Narrative |
| G2.5 — Hero Approved | Carrossel, story, thumbnail |
| Narrative complete | Prompts Veo, geração |
| Prompt Composer | Prompts manuais Veo |

**Implicações:** Registry e `fce check` (futuro) validam gates antes de Context Pack completo.

---

## P9 — Hero primeiro, derivação depois

**Declaração:** Identidade visual de campanha nasce no Hero Asset aprovado — demais peças derivam, não competem.

**Implicações:**
- Tipografia nunca na fotografia (Veo/stock) — sempre Canva depois
- Espaço negativo mínimo 35–40% no Hero
- Launchers de carrossel/story referenciam gate G2.5

---

## P10 — Narrative antes de Veo

**Declaração:** Nenhum prompt Veo é escrito manualmente. Narrative Pipeline + Prompt Composer são obrigatórios.

**Implicações:**
- `CREATE_VIDEO_VEO.md` valida narrative antes de export
- `library/veo3/` valida — não substitui — Narrative Engine
- 6 elementos por cena; 9:16 first; `no text` default

---

## P11 — Compatibilidade com FCE 1.x

**Declaração:** Migração preserva paths, letras definitivas, prompts finais e assets existentes.

**Implicações:**
- Aliases em specs para Track 01 (`scenes.md` monolítico, `character.md`)
- `launcher/` e `library/` permanecem válidos durante toda migração
- Produção criativa atual não depende de Registry até Sprint 4+

---

## P12 — Idioma e tom

**Declaração:** Conteúdo em PT-BR; prompts Suno/Veo em inglês; tags Suno em inglês; tom VibeCore teatral e teologicamente fiel.

**Implicações:**
- Knowledge `music/` e `platforms/suno.md` documentam convenção de idioma
- Profiles herdam restrição de idioma por domínio

---

## P13 — Segurança e secrets

**Declaração:** API keys, `.env` e credenciais nunca versionadas, ecoadas no chat ou hardcodadas em scripts.

**Implicações:**
- Knowledge `software/security.md` será SSOT (Sprint 2)
- Scripts Veo usam `.env.example` apenas

---

## P14 — Qualidade sobre velocidade genérica

**Declaração:** O FCE produz obras completas (Salmo → faixa → campanha) — não conteúdo genérico de motivação.

**Implicações:**
- Cada faixa declara Vibe Geral e identidade
- Campanha orquestra múltiplos entregáveis — não post isolado sem contexto
- Track piloto (01) é golden path para validar arquitetura

---

## Matriz princípio → documento

| Princípio | Documento primário | Documento arquitetural |
|-----------|-------------------|------------------------|
| P1 Escritura | `VISION.md` | `KNOWLEDGE.md` (theology) |
| P2 Repo SSOT | `AGENTS.md` | `REGISTRY.md` |
| P3 Additive | `MIGRATION.md` | este documento |
| P4 Leitura mínima | — | `CONTEXT_PACKS.md` |
| P5 Módulos | `library/*/README` | `MODULES.md` |
| P6 Router | `FCE.md` | `REGISTRY.md` |
| P7 Separação | `AGENTS.md` | `MODULES.md` |
| P8 Gates | `AGENTS.md`, `WORKFLOW.md` | `SPECS.md` |
| P9 Hero | `PRODUCTION_PHILOSOPHY.md` | `KNOWLEDGE.md` (design) |
| P10 Narrative | `WORKFLOW.md` | `DEPENDENCIES.md` |
| P11 Compatibilidade | `MIGRATION.md` | `MIGRATION.md` |
| P12 Idioma | `AGENTS.md` | `PROFILES.md` |
| P13 Segurança | `AGENTS.md` | `KNOWLEDGE.md` (software) |
| P14 Qualidade | `VISION.md` | `ARCHITECTURE.md` |

---

## Uso em decisões

Antes de aprovar mudança estrutural, responder:

1. Viola algum princípio P1–P14?
2. Exige remoção de legado sem sprint de consolidação?
3. Aumenta leitura de contexto sem justificativa?
4. Cria dependência circular entre módulos?
5. Quebra path ou conteúdo definitivo existente?

Se qualquer resposta for **sim** → redesign ou nova sprint dedicada.

---

**Versão:** Sprint 1.5 — Consolidação Arquitetural · 2026-07-03
