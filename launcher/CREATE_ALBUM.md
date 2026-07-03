# Launcher — Criar novo álbum

**Menu FCE.md:** Opção 11

---

## Objetivo

Orientar a IA a **iniciar um novo álbum** no FCE — conceito macro, tracklist, estrutura modular — antes de produzir faixas individuais.

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md)
3. [VISION.md](../VISION.md) — missão e VibeCore
4. [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) — módulo álbum
5. [WORKFLOW.md § WF1](../WORKFLOW.md#workflow-1--álbum-completo)
6. [ROADMAP.md](../ROADMAP.md) — fase atual do projeto

---

## Perguntas que a IA deve fazer ao usuário

1. **Número e título do álbum?**
2. **Escritura ou tema base?** (ex.: Salmos 37–48)
3. **Quantas faixas?** (tracklist inicial)
4. **Arco narrativo/emocional?** (atos, clímax)
5. **Identidade visual álbum?** (ouro/roxo, etc.)
6. **Relação com álbuns existentes?** (ex.: Álbum 4 já documentado)
7. **Autorização** — confirmar que álbum não existe no repo

---

## Arquivos que a IA deve consultar

| Arquivo | Função |
|---------|--------|
| `albums/` | Álbuns existentes — não duplicar |
| `albums/album-04-o-trono-intocavel/` | Referência de estrutura completa |
| `templates/` | Templates disponíveis |
| `library/canva/` | Brand por álbum |
| `CHANGELOG.md` | Registrar mudança estrutural |

---

## Saídas esperadas

1. **Tese do álbum** — 1–2 parágrafos
2. **Tracklist preliminar** — NN, título, Salmo, vibe resumida
3. **Schema `album.yaml`** — id, slug, track_count, status `concept`
4. **`concept.md`** — arco, teologia, referências visuais/sonoras
5. **Estrutura de pastas** — `tracks/`, `campaigns/`, `bible-studies/`, `legal/`
6. **Plano de faixas** — ordem de produção WF2 por track
7. **Stub legal** — `legal/dossie-direitos-autorais.md` vazio ou cabeçalho
8. **Próximo passo** — [CREATE_TRACK.md](./CREATE_TRACK.md) para faixa 01

---

## Checklist de qualidade

- [ ] Slug `album-NN-{kebab}` correto
- [ ] Arco teológico claro — Escritura como fonte
- [ ] VibeCore declarado por faixa na tracklist
- [ ] Não conflita com Álbum 4 sem autorização explícita
- [ ] Links cruzados album ↔ tracks planejados
- [ ] CHANGELOG quando usuário solicitar commit

---

## O que a IA não deve fazer

- ❌ Criar álbum 5+ sem autorização quando escopo é Álbum 4
- ❌ Inventar 12 faixas completas com letras de uma vez
- ❌ Duplicar *O Trono Intocável* silenciosamente
- ❌ Nova engine Album
- ❌ Apagar álbum existente
- ❌ Gerar assets ou áudio

---

**Faixa seguinte:** [CREATE_TRACK.md](./CREATE_TRACK.md) · **Campanha:** [WORKFLOW.md § WF7](../WORKFLOW.md#workflow-7--campanha-de-lançamento)
