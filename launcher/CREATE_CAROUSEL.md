# Launcher — Criar carrossel

**Menu FCE.md:** Opção 2  
**Formato típico:** 4:5 (1080×1440) × 5–8 slides

---

## Objetivo

Orientar a IA a produzir **outline slide a slide**, specs de produção Canva e copy de legenda — **somente após Hero Asset aprovado** (Sprint 5.2).

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md) — **nunca carrossel sem Hero aprovado**
3. [docs/PRODUCTION_PHILOSOPHY.md](../docs/PRODUCTION_PHILOSOPHY.md)
4. [WORKFLOW.md § Hero Asset](../WORKFLOW.md#hero-asset-workflow)
5. Contexto da faixa + CDS
6. Referência piloto: `track-01-o-legado/design/carousel-production.md` (se Track 01)

---

## Perguntas que a IA deve fazer ao usuário

1. **Qual álbum e faixa?**
2. **Quantos slides?** (default: 6 — hook → problema → insight → versículo → mapa → CTA)
3. **Hero Asset aprovado?** Se **não** → redirecionar para [CREATE_HERO_ASSET.md](./CREATE_HERO_ASSET.md)
4. **Foco devocional?** (Salmo base · aplicação prática · lançamento faixa)
5. **Versículos a incluir?** (ancorar no Salmo da faixa)
6. **Export para qual plataforma?** (IG feed principal)

---

## Arquivos que a IA deve consultar

| Arquivo | Path |
|---------|------|
| `track.yaml` | Metadados, scripture anchor |
| `lyrics.md` | Hooks e refrão |
| `identity/track_identity.md` | Tokens, símbolos, Do Not Use |
| `design/creative-brief.md` | Big idea, mensagem-chave |
| `design/design-specification.md` | Grid, tipografia, outline carrossel |
| `design/canva-brief.md` | Spec operacional |
| `assets/hero/README.md` | Hero aprovado — fonte de recortes |
| `bible-studies/study-track-XX/` | Se existir — conteúdo devocional |
| `design/carousel-production.md` | Se existir — spec slide a slide |

---

## Saídas esperadas

1. **Arco narrativo** — paleta evolui frio→ouro (ou equivalente da faixa)
2. **Spec por slide** — texto exato, hierarquia, paleta, imagem sugerida, composição, notas Canva
3. **Ordem de produção Canva** — Hero → slide mapa → demais slides
4. **Legenda do carrossel** — hook + CTA save/compartilhar + até 5 hashtags
5. **Checklist G4** — identity, Sl reference, max 40 palavras/slide body

**Não gerar imagens** — documentação executável no Canva.

---

## Checklist de qualidade

- [ ] Hero Approved confirmado (`assets/hero/approved/`)
- [ ] 6–8 slides com arco claro
- [ ] Máx. 40 palavras body por slide
- [ ] Versículos com referência NVI
- [ ] Um símbolo dominante por slide
- [ ] Tokens identity em todos os slides
- [ ] Slide final com CTA autêntico (não clickbait)
- [ ] Recortes do Hero no slide CTA/mapa — não fotos novas genéricas

---

## O que a IA não deve fazer

- ❌ Iniciar carrossel **sem Hero aprovado**
- ❌ Produzir todos os slides com fotos diferentes e inconsistentes
- ❌ Alterar letras definitivas
- ❌ Inventar versículos ou paráfrases de outros livros no lugar do Salmo base
- ❌ Gerar PNGs ou abrir Canva automaticamente
- ❌ Usar ícones religiosos kitsch (cruz dominante, halos, pomba)
- ❌ Criar nova engine de carrossel

---

**Referência:** [WORKFLOW.md § WF4](../WORKFLOW.md#workflow-4--design-canva) · [CREATE_HERO_ASSET.md](./CREATE_HERO_ASSET.md)
