# Roadmap — Franklin Creative Engine

Roadmap evolutivo do FCE. Datas são orientativas; prioridade segue valor ministerial + completude do Álbum 4.

**Legenda:** ✅ Concluído · 🔄 Em progresso · 📋 Planejado · 💡 Backlog

---

## Fase 0 — Fundação documental

**Objetivo:** Estabelecer a infraestrutura de conhecimento para humanos e agentes de IA.

| Entrega | Status | Notas |
|---------|--------|-------|
| README.md | ✅ | Ponto de entrada |
| VISION.md | ✅ | Missão e VibeCore |
| ROADMAP.md | ✅ | Este arquivo |
| PROJECT_STRUCTURE.md | ✅ | Pastas e convenções |
| AGENTS.md | ✅ | Regras para IAs |
| WORKFLOW.md | ✅ | Pipelines de produção |
| CHANGELOG.md | ✅ | v0.1.0 inicial |
| `.gitignore` para assets binários | ✅ |

**Critério de conclusão:** Agente externo consegue orientar-se só com docs da raiz.

---

## Fase 1 — Estrutura modular e Álbum 4

**Objetivo:** Organizar o dossiê existente e preparar templates replicáveis.

**Horizonte:** 4–8 semanas

### 1.1 Estrutura de pastas

| Tarefa | Status |
|--------|--------|
| Criar `albums/album-04-o-trono-intocavel/` | ✅ |
| Migrar dossiê para `legal/dossie-direitos-autorais.md` | ✅ |
| Extrair 12 faixas em `tracks/track-XX-slug/` | ✅ |
| Criar `album.yaml` com metadados do álbum | ✅ |

### 1.2 Templates

| Template | Caminho previsto | Status |
|----------|------------------|--------|
| Faixa (letra + ficha) | `templates/track-template.md` | ✅ |
| Campanha de lançamento | `templates/campaign-template.md` | ✅ |
| Estudo bíblico | `templates/bible-study-template.md` | ✅ |
| Suno prompt sheet | `templates/suno-prompt-template.md` | ✅ |
| Brief Veo 3 | `templates/veo3-brief-template.md` | ✅ |
| Kit Canva | `templates/canva-kit-brief.md` | ✅ |

### 1.3 Álbum 4 — entregas por faixa

Para cada uma das 12 faixas (Salmos 37–48):

| Entregável | Ferramenta | Status global |
|------------|------------|---------------|
| Letra definitiva + ficha técnica | ChatGPT / Cursor | ✅ (migrado do dossiê) |
| Áudio master | Suno + pós | 📋 |
| Lyric video / clip | Veo 3 + Filmora | 📋 |
| Carrossel devocional (5–10 slides) | Canva | 📋 |
| Legendas IG/TikTok/YT | ChatGPT + Filmora | 📋 |
| Estudo bíblico | ChatGPT | 📋 |
| Calendário de posts | WORKFLOW campanha | 📋 |

**Pendência conhecida:** Faixa 3 (*O Sopro do Tempo*) — micro-refatoração teológica na estrofe de Eclesiastes (ver dossiê, VibeCore Alert).

**Critério de conclusão:** Álbum 4 com pelo menos 3 faixas em ciclo completo (áudio + campanha + estudo).

---

## Fase 2 — Biblioteca criativa

**Objetivo:** Centralizar prompts, estilos e assets reutilizáveis.

**Horizonte:** 2–3 meses após Fase 1

| Módulo | Conteúdo | Status |
|--------|----------|--------|
| `library/suno/` | Prompts por vibe (Dark Trap, Arena, Festivo…) | 📋 |
| `library/veo3/` | Cenas, movimentos de câmera, paletas | 📋 |
| `library/canva/` | Tipografia, cores, layouts por álbum | 📋 |
| `library/copy/` | CTAs, hooks, hashtags cristãs BR | 📋 |
| `library/theology/` | Notas exegéticas por livro bíblico | 📋 |

### Identidade visual — Álbum 4

| Elemento | Direção |
|----------|---------|
| Paleta | Ouro, roxo profundo, preto teatral, branco puro |
| Motivos | Trono, montanhas, correntes d'água, luz rompendo |
| Tipografia | Serif majestosa + sans bold para títulos de faixa |

---

## Fase 3 — Automação e agentes

**Objetivo:** Reduzir trabalho repetitivo via Cursor, scripts e regras.

**Horizonte:** 3–6 meses

| Automação | Descrição | Status |
|-----------|-----------|--------|
| Regra Cursor `.cursor/rules/fce.mdc` | Contexto permanente do projeto | 📋 |
| Skill FCE customizada | Prompts padronizados para faixa/campanha | 📋 |
| Validador de letra | Checagem de tags Suno obrigatórias | 💡 |
| Gerador de `track.yaml` | Metadados a partir da ficha | 💡 |
| Export de campanha | Markdown → checklist Notion/Sheets | 💡 |

**Critério de conclusão:** Nova faixa criada seguindo template com < 30 min de setup manual.

---

## Fase 4 — Novos álbuns e produtos derivados

**Objetivo:** Replicar pipeline para novos projetos temáticos.

**Horizonte:** 6–12 meses

### Álbuns candidatos (priorização futura)

| Slug | Tema | Escopo bíblico |
|------|------|----------------|
| `album-05-` | TBD | Salmos 49–60 |
| `album-gospel-narrativas` | Evangelhos | Parábolas em rap teatral |
| `album-apocalipse` | Apocalipse | Visões cinematográficas |

### Produtos derivados

| Produto | Formato | Status |
|---------|---------|--------|
| Devocional 40 dias | PDF + carrosséis | 💡 |
| Podcast "Por trás da faixa" | Roteiro + áudio | 💡 |
| Material para células | Estudo + discussion guide | 💡 |
| Partituras / cifras simplificadas | Para igrejas locais | 💡 |

---

## Fase 5 — Distribuição e métricas

**Objetivo:** Publicação multi-plataforma com feedback loop.

**Horizonte:** 12+ meses

| Área | Entregas |
|------|----------|
| Distribuição musical | Spotify, Apple Music, YouTube Music |
| Vídeo | YouTube, Reels, TikTok, Shorts |
| Social | Calendário unificado, A/B de hooks |
| Analytics | Planilha ou dashboard de KPIs por faixa |
| Comunidade | Lista de e-mail, WhatsApp devocional |

---

## Marcos (milestones)

```
M0  Fundação documental          ✅
M1  Álbum 4 estruturado no repo    ✅
M2  3 faixas com campanha completa
M3  Álbum 4 lançado (12/12 faixas)
M4  Biblioteca VibeCore v1
M5  Automações Cursor ativas
M6  Segundo álbum em produção
```

---

## Riscos e mitigações

| Risco | Mitigação |
|-------|-----------|
| Deriva teológica em letras IA | VibeCore Alerts + revisão humana |
| Inconsistência visual entre faixas | Kits Canva versionados por álbum |
| Perda de contexto entre sessões IA | AGENTS.md + YAML por faixa |
| Direitos autorais Suno | Dossiê legal + letras originais documentadas |
| Sobrecarga de escopo | Uma faixa completa antes de escalar |

---

## Como atualizar este roadmap

1. Mover tarefas entre status quando concluídas
2. Registrar mudanças significativas em CHANGELOG.md
3. Não remover marcos concluídos — marcar ✅ com data
4. Novas fases exigem entrada em CHANGELOG com justificativa

**Última revisão:** 2026-07-02 — criação da fundação v0.1.0
