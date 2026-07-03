# Franklin Creative Engine (FCE)

**Sistema operacional criativo com IA para produção de campanhas completas de músicas cristãs.**

> **Porta de entrada:** leia **[FCE.md](./FCE.md)** — interface conversacional oficial. Funciona em ChatGPT, Cursor, Codex, Claude ou Gemini.

O FCE orquestra álbuns, faixas, conteúdo visual, vídeos, legendas, roteiros, estudos bíblicos e campanhas de divulgação — do conceito teológico ao asset publicado — usando um pipeline modular integrado a ChatGPT, Cursor/Codex, Suno, Veo 3, Filmora Pro e Canva.

---

## O que é o FCE

O Franklin Creative Engine não é apenas um repositório de letras. É uma **infraestrutura de produção criativa** desenhada para:

- Transformar textos bíblicos (Salmos, narrativas, epístolas) em **músicas teatrais** com identidade sonora consistente
- Gerar **campanhas completas** por faixa, por álbum ou por temporada litúrgica
- Manter **continuidade artística** entre Suno, vídeo, design e copy
- Permitir que **agentes de IA** (Cursor, Codex, ChatGPT) retomem contexto e produzam sem perder qualidade

**Projeto ativo de referência:** Álbum 4 — *O Trono Intocável* (Salmos 37–48), com 12 faixas em Trap Acústico, Pop Teatral, Cinematic Trap-Rock e estética de arena.

---

## Documentação principal

| Arquivo | Propósito |
|---------|-----------|
| **[FCE.md](./FCE.md)** | **Porta de entrada conversacional** — menu de tarefas + launchers |
| [launcher/](./launcher/) | Playbooks por tarefa (post, carrossel, Hero, Veo, etc.) |
| [VISION.md](./VISION.md) | Missão, princípios teológicos-artísticos e visão de longo prazo |
| [ROADMAP.md](./ROADMAP.md) | Fases, entregas e cronograma evolutivo |
| [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) | Estrutura de pastas, módulos e convenções de nomenclatura |
| [AGENTS.md](./AGENTS.md) | Instruções para agentes de IA operarem no projeto |
| [WORKFLOW.md](./WORKFLOW.md) | Pipelines de produção ponta a ponta |
| [docs/PRODUCTION_PHILOSOPHY.md](./docs/PRODUCTION_PHILOSOPHY.md) | Filosofia Hero Asset → Asset Derivation |
| [library/creative_direction_system/](./library/creative_direction_system/) | Direção criativa estratégica (CDS) |
| [library/narrative_engine/](./library/narrative_engine/) | Direção cinematográfica (vídeo) |
| [CHANGELOG.md](./CHANGELOG.md) | Histórico de versões e mudanças documentais |

---

## Stack criativa

| Ferramenta | Papel no FCE |
|------------|--------------|
| **ChatGPT** | Ideação, estudo bíblico, copy, roteiros, prompts para outras ferramentas |
| **Cursor / Codex** | Engenharia do repositório, automação, templates, revisão de dossiês |
| **Suno** | Geração e iteração de faixas musicais a partir de letras anotadas |
| **Veo 3** | Clipes, B-roll cinematográfico, cenas teatrais e motion para reels |
| **Filmora Pro** | Montagem final, legendas, color grading, export multi-plataforma |
| **Canva** | Carrosséis, capas, stories, thumbnails e kits visuais de campanha |

---

## Tipos de entrega suportados

- **Álbuns** — conceito macro, arco narrativo, tracklist, dossiê de direitos
- **Faixas** — letra definitiva, ficha técnica, Suno prompt, metadados
- **Carrosséis** — séries educativas e devocionais (Instagram, LinkedIn)
- **Vídeos** — lyric video, clip teatral, reel de lançamento, B-roll Veo 3
- **Posts e legendas** — copy por plataforma (IG, TikTok, YouTube, WhatsApp)
- **Roteiros** — ministração, spoken word, narração de clip, podcast curto
- **Campanhas** — calendário editorial, funil de lançamento, CTAs
- **Estudos bíblicos** — material de aprofundamento ligado a cada faixa

---

## Início rápido para humanos

1. Abra **[FCE.md](./FCE.md)** e escolha o que produzir hoje
2. Leia [VISION.md](./VISION.md) para entender o *porquê* do projeto
3. Consulte [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) antes de criar arquivos
4. Siga [WORKFLOW.md](./WORKFLOW.md) para o tipo de entrega desejada
5. Registre mudanças em [CHANGELOG.md](./CHANGELOG.md)

---

## Início rápido para agentes de IA

```
Contexto: Franklin Creative Engine (FCE) — SO criativo para música cristã.
Leia FCE.md PRIMEIRO — porta de entrada conversacional.
Depois AGENTS.md e o launcher/ da tarefa escolhida.
Respeite PROJECT_STRUCTURE.md para paths e naming.
Não invente faixas ou álbuns não documentados.
Idioma padrão de conteúdo: Português Brasileiro.
Estilo musical padrão: Pop Teatral / Trap Crossover / Arena Rock (ver VISION.md).
```

**Ordem de leitura recomendada:** `FCE.md` → launcher da tarefa → `AGENTS.md` → `PROJECT_STRUCTURE.md` → `WORKFLOW.md` → contexto álbum/faixa em `albums/`.

---

## Production Philosophy

> **O FCE produz primeiro o Hero Asset. Após aprovação, toda a campanha deriva dele.**

O Hero Asset é a primeira peça visual produzida de uma campanha — a fotografia ou frame que encapsula a identidade da faixa. Tipografia é aplicada **depois**, em Canva. Carrossel, story, thumbnail e post **derivam** do Hero aprovado — nunca são produzidos todos ao mesmo tempo.

Documentação completa: [docs/PRODUCTION_PHILOSOPHY.md](./docs/PRODUCTION_PHILOSOPHY.md) · Workflow: [WORKFLOW.md § Hero Asset](./WORKFLOW.md#hero-asset-workflow)

---

## Estado atual do repositório

| Item | Status |
|------|--------|
| Fundação documental | ✅ Concluída (v0.1.0) |
| Álbum 4 — O Trono Intocável | ✅ Estrutura modular (v0.2.0) — 12 faixas documentadas |
| Estrutura modular `albums/` | ✅ `albums/album-04-o-trono-intocavel/` |
| Templates de faixa e campanha | ✅ Em `templates/` |
| Automações Cursor | 🔜 Fase 3 do ROADMAP |
| Narrative Engine | ✅ Sprint 4 — `library/narrative_engine/` |
| Creative Direction System | ✅ Sprint 5 — `library/creative_direction_system/` |
| Hero Asset Workflow | ✅ Sprint 5.2 — [PRODUCTION_PHILOSOPHY.md](./docs/PRODUCTION_PHILOSOPHY.md) |
| FCE Launcher | ✅ Interface conversacional — [FCE.md](./FCE.md) + [launcher/](./launcher/) |

---

## Princípios inegociáveis

1. **Fidelidade bíblica** — adaptação poética, não distorção teológica
2. **Excelência artística** — produção teatral, dinâmica e memorável
3. **Modularidade** — cada faixa é uma unidade; cada álbum é um ecossistema
4. **Rastreabilidade** — versões, pendências e decisões documentadas
5. **Pronto para IA** — markdown limpo, metadados explícitos, links cruzados

---

## Licença e direitos

Conteúdo musical, letras e assets visuais são propriedade intelectual do projeto Franklin Creative Engine. Dossiês de direitos autorais devem ser mantidos por álbum em `albums/{slug}/legal/`.

---

## Contato e manutenção

Este repositório é a **fonte única de verdade** do FCE. Qualquer agente ou colaborador deve priorizar documentação versionada sobre conversas isoladas em chat.

Para expandir o sistema, adicione módulos em `PROJECT_STRUCTURE.md` e registre a mudança em `CHANGELOG.md`.
