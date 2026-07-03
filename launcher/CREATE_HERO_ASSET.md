# Launcher — Criar Hero Asset

**Menu FCE.md:** Opção 3  
**Gate:** Pós CDS G2 (Design Specification aprovada)

---

## Objetivo

Orientar a IA a definir, revisar e documentar o **Hero Asset** — primeira peça visual da campanha. Todo post, carrossel, story e thumbnail **deriva** dele após aprovação.

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [docs/PRODUCTION_PHILOSOPHY.md](../docs/PRODUCTION_PHILOSOPHY.md)
3. [AGENTS.md § Hero Asset](../AGENTS.md) — Hero Review Checklist (8 critérios)
4. [WORKFLOW.md § Hero Asset Workflow](../WORKFLOW.md#hero-asset-workflow)
5. `identity/track_identity.md`
6. `design/design-specification.md`
7. `video/narrative/scenes.md` — cena de clímax (se existir)

**Piloto aprovado:** `track-01-o-legado/assets/hero/README.md`

---

## Perguntas que a IA deve fazer ao usuário

1. **Qual álbum e faixa?**
2. **CDS G2 aprovado?** Se não → orientar Creative Direction Pipeline primeiro
3. **Qual ato/símbolo para o Hero?** (default: ato III clímax — ex.: `dawn`, `light`)
4. **Fonte da imagem?** (Veo cena · foto Canva · stock curada · ainda não produzida)
5. **Hero já existe em rascunho?** Revisar ou criar spec do zero
6. **Formato master?** (mín. 1080×1440 4:5 recomendado)

---

## Arquivos que a IA deve consultar

| Arquivo | Função |
|---------|--------|
| `identity/track_identity.md` | Tokens, símbolos, moodboard, Do Not Use |
| `design/design-specification.md` | Paleta, fotografia, composição |
| `design/creative-brief.md` | Big idea, arco emocional |
| `video/narrative/scenes.md` | Referência fotográfica canônica |
| `video/narrative/character.md` | Personagem visual (ex.: Rafael) |
| `assets/hero/README.md` | Status e critérios — criar se não existir |
| `assets/hero/approved/` | Destino do binário aprovado |

---

## Saídas esperadas

1. **Spec do Hero Asset** — cena, símbolo, paleta, composição, espaço negativo (%)
2. **Prompt premium para imagem** — **sem texto na imagem** · inglês para Veo ou descritivo fotográfico
3. **Hero Review Checklist** — 8 critérios (AGENTS.md) com pass/fail
4. **Documentação** — atualizar ou criar `assets/hero/README.md` com status
5. **Plano de derivação** — lista de peças que usarão este Hero (post, carrossel s06, story, thumb)
6. **Instruções de salvamento** — filename sugerido em `assets/hero/approved/`

**Status APPROVED** só após usuário confirmar revisão visual do binário (IA não aprova sozinha sem validação humana).

---

## Checklist de qualidade (Hero Review)

- [ ] Expressão — emoção da faixa, não stock smile
- [ ] Narrativa — clímax do arco visual
- [ ] Iluminação — alinhada à design spec por ato
- [ ] Composição — terços, leading lines, um foco
- [ ] Espaço negativo — 35–40% para tipografia posterior
- [ ] Consistência Track Identity — tokens, Do Not Use
- [ ] Realismo — documental BR, sem kitsch
- [ ] Impacto — reconhecível em ≤ 3s

---

## O que a IA não deve fazer

- ❌ Incluir tipografia no prompt de fotografia/Veo
- ❌ Aprovar Hero sem confirmação humana do binário
- ❌ Derivar carrossel/story antes de Hero Approved
- ❌ Criar Hero sem design spec G2
- ❌ Gerar binário e commitar no git
- ❌ Ignorar Narrative Engine quando cenas existirem
- ❌ Criar nova engine Hero

---

**Filosofia:** [docs/PRODUCTION_PHILOSOPHY.md](../docs/PRODUCTION_PHILOSOPHY.md)
