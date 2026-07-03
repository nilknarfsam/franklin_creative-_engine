# Launcher — Criar Story

**Menu FCE.md:** Opção 4  
**Formato:** 9:16 (1080×1920)

---

## Objetivo

Orientar a IA a produzir **spec de story** (1–3 frames), prompts de imagem, copy mínimo e safe zones — derivando do Hero quando possível.

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md)
3. [docs/PRODUCTION_PHILOSOPHY.md](../docs/PRODUCTION_PHILOSOPHY.md)
4. `identity/track_identity.md`
5. `design/design-specification.md` — safe zones 9:16
6. `assets/hero/README.md` — preferir derivar do Hero

**Referência:** `track-01-o-legado/design/story-production.md`

---

## Perguntas que a IA deve fazer ao usuário

1. **Qual álbum e faixa?**
2. **Quantos frames?** (1 único · sequência 3 — teaser D-3)
3. **Objetivo?** (teaser · CTA ouvir · countdown lançamento)
4. **Hero aprovado?** Derivar frame CTA do Hero
5. **Áudio disponível?** (snippet Suno — se não, story estático)
6. **Data de publicação?** (D-3, D-1, D0)

---

## Arquivos que a IA deve consultar

| Arquivo | Path |
|---------|------|
| `track.yaml` | Metadados |
| `lyrics.md` | Hook intro/refrão |
| `identity/track_identity.md` | Tom, safe zones, tokens |
| `design/design-specification.md` | Canvas 9:16 |
| `design/story-production.md` | Se existir |
| `assets/hero/` | Crop vertical do Hero |
| `campaigns/campaign-track-XX/calendar.md` | Se existir — timing |

---

## Saídas esperadas

1. **Spec por frame** — texto exato (máx. 2 linhas), hierarquia, paleta
2. **Prompt de imagem por frame** — sem texto legível · sem UI de celular legível
3. **Safe zones** — 120px topo/base · 48px laterais
4. **Sequência de publicação** — D-3 a D0 se campanha
5. **CTA** — sticker/link sugerido na publicação IG
6. **Checklist** — identity, Do Not Use, contraste

---

## Checklist de qualidade

- [ ] Máx. 2 linhas de texto por frame
- [ ] Safe zones respeitadas
- [ ] Arco frio→ouro se sequência 3 frames
- [ ] Derivado do Hero no frame CTA
- [ ] CTA autêntico — não clickbait
- [ ] 9:16 first

---

## O que a IA não deve fazer

- ❌ Crowding de texto no story
- ❌ Tela de celular com UI legível
- ❌ Gerar vídeo/PNG
- ❌ Alterar letras
- ❌ Story antes de Hero (frame clímax)

---

**Workflow:** [WORKFLOW.md § WF4](../WORKFLOW.md#workflow-4--design-canva)
