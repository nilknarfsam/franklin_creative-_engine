# Production Philosophy — Franklin Creative Engine

**Sprint 5.2** — aprendizados validados na produção real da Track 01 — *O Legado*.

Este documento registra **como** o FCE produz campanhas visuais. Não cria engines, módulos ou automações — apenas formaliza decisões já testadas em produção.

---

## Princípio central

> **O FCE produz primeiro o Hero Asset. Após aprovação, toda a campanha deriva dele.**

---

## O que é o Hero Asset

O **Hero Asset** é a **primeira peça visual produzida** de uma campanha — tipicamente a fotografia ou frame cinematográfico que encapsula a identidade da faixa no clímax visual (ato III na Track 01).

Características obrigatórias:

- Representa a **Track Identity** — tokens, símbolos, arco emocional
- Possui **espaço negativo** intencional para tipografia aplicada depois
- **Sem texto** na geração da imagem/fotografia — tipografia é camada posterior (Canva)
- Serve como **fonte canônica** para crop, adaptação e reutilização

Na Track 01, o Hero aprovado é a cena **ato III — amanhecer urbano**: calçada arborizada, homem caminhando em direção à luz, céu purple-gold (`dawn`). Alinhado à Narrative cena 06 e ao Painel 6 do moodboard.

---

## Por que produzir primeiro o Hero

### 1. A campanha precisa de uma âncora visual

Antes de carrossel, story, thumbnail ou capa, o time precisa **ver** se a identidade funciona em uma peça real — não apenas na design specification. O Hero materializa a spec em decisão concreta.

### 2. A spec não substitui julgamento humano

`design-specification.md` define sistema; o Hero valida **expressão, luz, composição e impacto** no mundo real. Track 01 confirmou: tokens `legado-*` só ganham confiança quando aplicados num frame hero aprovado.

### 3. Erros baratos cedo, caros tarde

Reprovar um Hero antes de produzir seis slides de carrossel evita retrabalho em cascata — paleta errada, rosto inconsistente, falta de respiro tipográfico.

---

## Por que derivar (e não produzir tudo junto)

### O anti-padrão

Produzir simultaneamente post, carrossel (6 slides), story (3 frames) e thumbnail **sem Hero aprovado** gera:

- Paletas divergentes entre peças
- Fotos stock diferentes para o mesmo personagem
- Tipografia competindo com imagens pensadas sem respiro
- Retrabalho total quando uma peça base falha na revisão

### O padrão FCE

```
Design Specification (G2)
        ↓
   Hero Asset          ← primeira peça, isolada
        ↓
   Hero Review         ← checklist AGENTS.md
        ↓
   Hero Approved       ← assets/hero/approved/
        ↓
   Asset Derivation    ← carrossel, story, thumb, post
        ↓
   Exports             ← assets/exports/
```

**Nunca criar todas as peças ao mesmo tempo.** Primeiro aprovar o Hero. Depois derivar.

---

## Asset Derivation — o que deriva do Hero

| Peça derivada | Como usa o Hero |
|---------------|-----------------|
| Post principal feed | Hero full-bleed + overlay tipográfico |
| Carrossel slide 06 (CTA) | Mesma foto + botão |
| Story frame 03 | Crop 9:16 central |
| Thumbnail YouTube | Crop 16:9 — rosto/horizonte terço esquerdo |
| Carrossel slide 05 (mapa) | Recorte estação LUZ do Hero |
| Spotify Canvas (P1) | Movimento extraído do Hero (ato III) |

Track 01 documentou esta derivação em `design/assets-p0-plan.md` — ordem Canva: slide 05 (mapa) primeiro para definir trilha; Hero antes de slides 01–06 em execução real.

---

## Benefícios comprovados (Track 01)

| Benefício | Evidência na produção |
|-----------|----------------------|
| **Consistência** | Mesmo amanhecer urbano em post, CTA, story e thumb |
| **Escalabilidade** | Próximas faixas replicam workflow Hero → Derivation |
| **Reutilização** | Um frame alimenta 4+ formatos com crop, não nova geração |
| **Redução de retrabalho** | Hero Review antes de 6 slides evita refazer carrossel inteiro |
| **Maior qualidade visual** | Espaço negativo e tipografia pós-produção = editorial premium |

---

## Regras operacionais

1. **Hero sem texto** — `no text` em Veo; sem tipografia em stock AI; Canva aplica Display/Scripture depois
2. **Hero Review obrigatório** — checklist em [AGENTS.md](../AGENTS.md) antes de derivar
3. **Carrossel bloqueado sem Hero** — nunca iniciar slides devocionais antes de Hero Approved
4. **Binários em `assets/hero/approved/`** — gitignored; path referenciado em markdown
5. **Exports finais em `assets/exports/`** — PNG/PDF prontos para publicação

---

## Relação com outros módulos FCE

| Módulo | Relação |
|--------|---------|
| **CDS** | Hero executa a design spec — não a substitui |
| **Track Identity** | Hero deve passar checklist de consistência identity |
| **Narrative Engine** | Hero fotográfico alinha com cena de clímax (Track 01: cena 06) |
| **Canva** | Tipografia e layout aplicados **após** Hero Approved |

---

## Referências

- [WORKFLOW.md](../WORKFLOW.md) — § Hero Asset Workflow
- [AGENTS.md](../AGENTS.md) — § Hero Asset + Hero Review Checklist
- [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) — `assets/hero/`, `approved/`, `exports/`
- Track 01 piloto: [assets/hero/](../albums/album-04-o-trono-intocavel/tracks/track-01-o-legado/assets/hero/)

---

**Versão:** 1.0.0 — Sprint 5.2 · 2026-07-02
