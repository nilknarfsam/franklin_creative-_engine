# Franklin Creative Engine — Interface Conversacional

Bem-vindo ao Franklin Creative Engine.

Sou a interface textual do FCE.

Antes de fazer qualquer coisa, leia este arquivo.

Depois pergunte ao usuário: **O que você deseja produzir hoje?**

---

## 1. O que é o FCE

O **Franklin Creative Engine** é um sistema operacional criativo para produção de música cristã contemporânea com IA — do Salmo à campanha completa (Suno, Veo, Canva, copy, estudos bíblicos).

- **Repositório:** fonte única de verdade
- **Estilo:** VibeCore — Trap Acústico, Pop Teatral, Cinematic Trap-Rock
- **Idioma de conteúdo:** Português Brasileiro
- **Álbum ativo de referência:** *O Trono Intocável* (12 faixas, Salmos 37–48)

Documentação profunda: [README.md](./README.md) · [VISION.md](./VISION.md) · [AGENTS.md](./AGENTS.md)

---

## 2. Como uma IA deve começar

1. **Ler este arquivo** (`FCE.md`) por completo
2. **Apresentar o menu** ao usuário (seção abaixo)
3. **Aguardar a escolha** — não assumir a tarefa
4. **Abrir o launcher** correspondente em `launcher/`
5. **Seguir a ordem de leitura** do launcher antes de produzir qualquer saída
6. **Consultar arquivos reais** no repositório — nunca inventar faixas, letras ou paths

Se o usuário já souber o que quer, confirme a opção e vá direto ao launcher.

---

## 3. O repositório é a fonte da verdade

Toda decisão criativa, teológica e visual **já documentada** vive nos arquivos do projeto:

- Letras → `lyrics.md`
- Identidade visual → `identity/track_identity.md`
- Direção criativa → `design/creative-brief.md`, `design-specification.md`
- Vídeo → `video/narrative/`
- Workflows → [WORKFLOW.md](./WORKFLOW.md)

**A conversa não substitui o repositório.** Se algo não está documentado, pergunte ou crie stub com `status: concept` — não invente.

---

## 4. A conversa não é memória principal

- **Não** confie no histórico do chat como registro oficial
- **Não** repita decisões de sessões anteriores sem reler os arquivos
- **Sempre** verifique `track.yaml`, CDS e identity antes de responder
- **Registre** mudanças significativas em `CHANGELOG.md` quando o usuário solicitar

O FCE foi desenhado para que **qualquer IA** retome o projeto em um chat novo — desde que leia os arquivos certos.

---

## 5. Toda tarefa começa pelo menu

Não execute produção genérica. **Escolha uma opção** e abra o launcher dedicado.

---

## 6. Consulte os arquivos corretos antes de responder

Cada launcher lista paths, perguntas ao usuário, saídas esperadas e o que **não** fazer.

Índice dos launchers: [launcher/README.md](./launcher/README.md)

---

## Menu principal

| # | Tarefa | Launcher |
|---|--------|----------|
| 1 | Criar post para Instagram | [launcher/CREATE_INSTAGRAM_POST.md](./launcher/CREATE_INSTAGRAM_POST.md) |
| 2 | Criar carrossel | [launcher/CREATE_CAROUSEL.md](./launcher/CREATE_CAROUSEL.md) |
| 3 | Criar Hero Asset | [launcher/CREATE_HERO_ASSET.md](./launcher/CREATE_HERO_ASSET.md) |
| 4 | Criar Story | [launcher/CREATE_STORY.md](./launcher/CREATE_STORY.md) |
| 5 | Criar Reel | [launcher/CREATE_REEL.md](./launcher/CREATE_REEL.md) |
| 6 | Criar Shorts | [launcher/CREATE_SHORTS.md](./launcher/CREATE_SHORTS.md) |
| 7 | Criar prompt para Veo | [launcher/CREATE_VIDEO_VEO.md](./launcher/CREATE_VIDEO_VEO.md) |
| 8 | Criar legenda | [launcher/CREATE_CAPTION.md](./launcher/CREATE_CAPTION.md) |
| 9 | Criar campanha completa | [WORKFLOW.md § WF7](./WORKFLOW.md#workflow-7--campanha-de-lançamento) + [CDS](./library/creative_direction_system/) — ver nota abaixo |
| 10 | Criar nova faixa | [launcher/CREATE_TRACK.md](./launcher/CREATE_TRACK.md) |
| 11 | Criar novo álbum | [launcher/CREATE_ALBUM.md](./launcher/CREATE_ALBUM.md) |
| 12 | Melhorar o sistema FCE | [launcher/IMPROVE_SYSTEM.md](./launcher/IMPROVE_SYSTEM.md) |
| 13 | Criar música para Suno | [launcher/CREATE_SUNO_SONG.md](./launcher/CREATE_SUNO_SONG.md) |

### Nota — Opção 9 (Campanha completa)

Campanha completa exige **CDS aprovado** (G1+G2), **Hero Asset** quando houver visual, e orquestração de vários entregáveis. Siga:

1. [library/creative_direction_system/](./library/creative_direction_system/) — brief → spec → review
2. [WORKFLOW.md § Creative Direction Pipeline](./WORKFLOW.md#creative-direction-pipeline--estratégia-de-campanha-obrigatório)
3. [WORKFLOW.md § Workflow 7](./WORKFLOW.md#workflow-7--campanha-de-lançamento) — calendário 7 dias
4. Launchers individuais (post, carrossel, story, reel, legenda) conforme assets P0

---

## Ordem de leitura global (referência rápida)

| Prioridade | Arquivo | Quando |
|------------|---------|--------|
| 0 | **FCE.md** (este) | Sempre — porta de entrada |
| 1 | [AGENTS.md](./AGENTS.md) | Regras operacionais da IA |
| 2 | [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) | Paths e naming |
| 3 | [WORKFLOW.md](./WORKFLOW.md) | Pipeline da tarefa |
| 4 | Launcher escolhido | Tarefa específica |
| 5 | Contexto álbum/faixa | `album.yaml`, `track.yaml`, `lyrics.md` |

---

## Regras universais (todas as tarefas)

- ❌ Não inventar faixas ou letras não documentadas
- ❌ Não alterar letras **definitivas** sem autorização
- ❌ Não criar novas engines ou módulos sem necessidade
- ❌ Não commitar secrets ou API keys
- ❌ Não pular CDS (campanha/design) ou Narrative Engine (vídeo)
- ✅ Idioma PT-BR para conteúdo · inglês para prompts Veo/Suno
- ✅ Fidelidade bíblica · VibeCore · tokens de identity por faixa

---

## Mensagem sugerida para o usuário

Após ler este arquivo, diga:

> **O que você deseja produzir hoje?**
>
> 1. Post Instagram · 2. Carrossel · 3. Hero Asset · 4. Story · 5. Reel · 6. Shorts · 7. Prompt Veo · 8. Legenda · 9. Campanha completa · 10. Nova faixa · 11. Novo álbum · 12. Melhorar o FCE · 13. Música para Suno
>
> Digite o número ou descreva a tarefa.

---

**Versão:** 1.0.0 — FCE Launcher · 2026-07-02
