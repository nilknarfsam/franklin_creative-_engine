# Launcher — Criar post para Instagram

**Menu FCE.md:** Opção 1  
**Formato típico:** 4:5 (1080×1440) ou 1:1 (1080×1080) — confirmar com design spec

---

## Objetivo

Orientar a IA a produzir **briefing de post**, **prompt premium para imagem** (sem gerar binário), **legenda** e **checklist de revisão** — alinhados à identidade da faixa e ao CDS.

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md) — regras gerais
3. [docs/PRODUCTION_PHILOSOPHY.md](../docs/PRODUCTION_PHILOSOPHY.md) — Hero first se post usar foto hero
4. Contexto da faixa (paths abaixo)
5. [WORKFLOW.md § WF4](../WORKFLOW.md#workflow-4--design-canva) — Design Canva

---

## Perguntas que a IA deve fazer ao usuário

1. **Qual álbum e faixa?** (ex.: Álbum 4, Track 01 — O Legado)
2. **Objetivo do post?** (lançamento · devocional · teaser · CTA ouvir)
3. **Formato?** (4:5 feed · 1:1 — verificar `design/design-specification.md`)
4. **Hero Asset já aprovado?** Se sim, derivar do Hero; se não, orientar [CREATE_HERO_ASSET.md](./CREATE_HERO_ASSET.md) primeiro
5. **Versículo ou hook preferido?** (default: anchor da faixa em `track.yaml` / brief)
6. **Plataforma secundária?** (só IG ou adaptar legenda)

---

## Arquivos que a IA deve consultar

| Arquivo | Path relativo à faixa |
|---------|------------------------|
| Metadados | `track.yaml` |
| Letra | `lyrics.md` |
| Conceito | `concept.md` |
| Identidade visual | `identity/track_identity.md` |
| Creative brief | `design/creative-brief.md` (se existir) |
| Design spec | `design/design-specification.md` (se existir) |
| Hero | `assets/hero/README.md` (se existir) |
| Plano P0 | `design/assets-p0-plan.md` (se existir) |
| Copy existente | `copy/posts.md`, `copy/captions.md` |

**Álbum:** `albums/{album}/album.yaml`, `concept.md`

---

## Saídas esperadas

Entregar ao usuário (markdown, pronto para Canva/humano executar):

1. **Briefing do post** — objetivo, formato, hierarquia visual, paleta (`legado-*` ou tokens da faixa)
2. **Prompt premium para imagem** — inglês ou PT descritivo; **sem texto legível na imagem**; direção fotográfica alinhada à identity
3. **Texto do post** — Display/H1/Body conforme spec; versículo com referência NVI
4. **Legenda IG** — hook + 2–3 frases + CTA autêntico + **até 5 hashtags**
5. **Checklist de revisão** — identity, Do Not Use, contraste, Hero alignment

**Não gerar PNG/JPG** — apenas documentação e prompts.

---

## Checklist de qualidade

- [ ] Faixa e álbum confirmados nos arquivos reais
- [ ] Tokens de cor da track identity aplicados
- [ ] Versículo citado com referência (NVI)
- [ ] Prompt de imagem sem texto legível · sem clichê gospel
- [ ] Legenda ≤ 5 hashtags · tom VibeCore · não preachy
- [ ] Hero derivado se `assets/hero/approved/` existir
- [ ] Nenhum item Do Not Use da identity violado
- [ ] Formato e margens conforme design spec

---

## O que a IA não deve fazer

- ❌ Inventar faixa ou letra não documentada
- ❌ Alterar `lyrics.md` ou letras definitivas
- ❌ Gerar ou exportar imagens binárias
- ❌ Pular CDS/identity quando existirem
- ❌ Usar stock gospel genérico ou prosperidade visual
- ❌ Colocar tipografia dentro do prompt de fotografia (texto vai no Canva)
- ❌ Criar nova engine ou módulo
- ❌ Commit ou push sem solicitação explícita

---

**Workflow completo:** [WORKFLOW.md § WF4](../WORKFLOW.md#workflow-4--design-canva)
