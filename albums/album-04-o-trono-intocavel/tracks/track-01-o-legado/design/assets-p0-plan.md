---
plan_id: p0-plan-track-01
track_id: track-01
brief_id: brief-track-01
spec_id: design-spec-track-01
identity_id: identity-track-01-o-legado
version: "1.0"
status: ready_for_canva
created: 2026-07-02
updated: 2026-07-02
gate: G4-prep
---

# Assets P0 — Plano de Produção · O Legado

**Objetivo:** Pacote visual P0 pronto para execução no Canva — sem geração de imagem nesta etapa.  
**CDS:** G1 + G2 aprovados · Identity `legado-*` obrigatória  
**Big Idea:** *Do peso do dia à luz que rompe.*

---

## Documentos de produção

| Arquivo | Conteúdo |
|---------|----------|
| [carousel-production.md](./carousel-production.md) | 6 slides devocionais — spec slide a slide |
| [story-production.md](./story-production.md) | Story teaser D-3 |
| [thumbnail-production.md](./thumbnail-production.md) | Thumbnail YouTube |

**Referências canônicas:** [creative-brief.md](./creative-brief.md) · [design-specification.md](./design-specification.md) · [canva-brief.md](./canva-brief.md) · [../identity/track_identity.md](../identity/track_identity.md)

---

## Inventário P0

| # | Asset | Formato | Dimensão | Prioridade | Doc | Status |
|---|-------|---------|----------|------------|-----|--------|
| 1 | Post principal (feed) | 4:5 | **1080 × 1440** | P0 | § Post principal abaixo | [ ] Canva |
| 2 | Carrossel devocional | 4:5 × 6 | **1080 × 1440** | P0 | [carousel-production.md](./carousel-production.md) | [ ] Canva |
| 3 | Story teaser | 9:16 | **1080 × 1920** | P0 | [story-production.md](./story-production.md) | [ ] Canva |
| 4 | Thumbnail YouTube | 16:9 | **1280 × 720** | P0 | [thumbnail-production.md](./thumbnail-production.md) | [ ] Canva |

> **Nota de formato:** Dimensões 4:5 (1080×1440) escolhidas para feed IG — maior área útil que 1:1. Thumbnail em 1280×720 (padrão YT). Capa Spotify 1:1 e Canvas 9:16 ficam fora deste pacote P0 de campanha social.

---

## Arco visual global

Todos os assets seguem o mesmo arco narrativo da faixa e do Narrative Engine:

```
Ato I (pressão)  →  Ato II (fidelidade)  →  Ato III (luz)
legado-night/urban     legado-earth/seed       legado-gold/purple
símbolos: path, storm  símbolos: seed, root    símbolos: light, dawn
```

| Asset | Ato dominante | Gradiente assinatura |
|-------|---------------|----------------------|
| Post principal | III | `esperanca` |
| Carrossel slides 1–2 | I | `pressao` |
| Carrossel slide 3 | II | neutro + `legado-seed` |
| Carrossel slide 4 | II→III | `transfiguracao` |
| Carrossel slide 5 | III | tipografia + `light` |
| Carrossel slide 6 | III | `esperanca` |
| Story | I→III (3 frames) | `pressao` → `esperanca` |
| Thumbnail | III | `esperanca` |

---

## Tokens obrigatórios (`legado-*`)

| Token | Hex | Uso neste pacote |
|-------|-----|------------------|
| `legado-gold` | `#C9A227` | Clímax, CTAs, destaques tipográficos |
| `legado-purple` | `#553C9A` | Céus ato III, acentos álbum |
| `legado-night` | `#2D3748` | Fundos ato I, overlays |
| `legado-urban` | `#4A5568` | Cards, superfícies ato I |
| `legado-white` | `#F7FAFC` | Texto sobre escuro |
| `legado-earth` | `#718096` | Corpo, refs bíblicas |
| `legado-seed` | `#48BB78` | Slide fidelidade |
| `legado-cold` | `#1A365D` | Glow digital, acentos frios |
| `legado-amber` | `#F6E05E` | Highlights sol da manhã |

**Gradientes Canva:** `pressao` · `transfiguracao` · `esperanca` — valores em [design-specification.md](./design-specification.md).

---

## Grid e margens (4:5 — 1080×1440)

| Parâmetro | Valor |
|-----------|-------|
| Colunas | 12 |
| Gutter | 20px |
| Margem lateral | 64px |
| Margem superior/inferior | 64px (texto crítico: +32px safe = 96px do topo/base) |
| Whitespace título ↔ corpo | 32px |
| Whitespace antes versículo | 48px |
| Máx. palavras body por slide | 40 |

---

## Tipografia (escala 4:5)

| Nível | Família | Peso | Tamanho | Line-height |
|-------|---------|------|---------|-------------|
| Display | Serif majestosa | Bold | 80px | 1.1 |
| H1 | Sans geométrica | Bold | 44px | 1.2 |
| Body | Sans humanista | Regular | 20px | 1.55 |
| Scripture | Serif / sans | Medium Italic | 24px | 1.5 |
| Caption | Sans small caps | Regular | 14px | 1.4 |

**Regra:** máx. 2 familias por layout · versículo anchor Sl 37:5 uma vez por peça (exceto carrossel onde slide 4 e 5 têm funções distintas).

---

## 1. Post principal — 1080×1440

**Função:** Post de lançamento ou devocional standalone no feed IG.  
**Ato:** III · **Símbolo:** `dawn` + `light`

### Texto exato

| Nível | Conteúdo |
|-------|----------|
| Display | O LEGADO |
| Scripture | Entrega o teu caminho ao Senhor; confia nele, e ele agirá. |
| Caption | Salmo 37:5 · NVI |
| Micro | O Trono Intocável · Faixa 01 |

### Hierarquia visual

1. Imagem hero — horizonte dourado, calçada arborizada (ato III)
2. Display "O LEGADO" — terço inferior, sobre overlay escuro 40%
3. Versículo Sl 37:5 — Scripture abaixo do título
4. Caption referência + micro álbum — base, `legado-earth`

### Paleta

- Fundo/imagem: golden hour, céu `legado-purple` → `legado-gold`
- Overlay inferior: gradiente `#2D3748` 0% → 65% opacity (bottom third)
- Texto: `legado-white` · destaque versículo: `legado-gold` na palavra *Entrega* (opcional)

### Imagem sugerida

Homem brasileiro ~30 anos (ref. Rafael), camisa azul-marinho desbotada, caminhando em calçada arborizada ao amanhecer. Skyline brasileiro desfocado. God rays suaves. Expressão: paz serena, passos firmes. **Sem** celular, **sem** sorriso stock.

### Composição

- Formato 4:5 vertical
- Sujeito no terço inferior-esquerdo; horizonte dourado no terço superior
- Leading line da calçada guia ao horizonte
- 40% frame como espaço negativo (céu + overlay)
- Texto confinado ao terço inferior — nunca sobre rosto

### Observações Canva

- Template: Instagram Post → custom 1080×1440
- Foto full-bleed; overlay gradiente em camada separada
- Grão fotográfico 3% apenas se foto for muito limpa
- Export PNG · qualidade máxima
- Alt text sugerido: *O Legado — Salmo 37 — homem caminha ao amanhecer urbano*

---

## 2. Carrossel devocional — 6 × 1080×1440

**Função:** Devocional Sl 37 — profundidade, saves, compartilhamento.  
**Doc completo:** [carousel-production.md](./carousel-production.md)

| Slide | Função | Ato | Símbolo |
|-------|--------|-----|---------|
| 01 | Título e impacto | I | `path` |
| 02 | Problema | I | `storm` |
| 03 | Raiz / fidelidade | II | `seed` · `root` |
| 04 | Entrega | II→III | `word` |
| 05 | Mapa visual | III | arco path→seed→light |
| 06 | CTA | III | `dawn` |

**Paleta evolui:** `pressao` (1–2) → neutro + seed (3) → `transfiguracao` (4) → `esperanca` (5–6)

---

## 3. Story teaser — 1080×1920

**Função:** Pré-lançamento D-3 — impacto imediato, CTA ouça.  
**Doc completo:** [story-production.md](./story-production.md)

- 3 frames sequenciais (ou 1 frame único simplificado)
- Texto máx. 2 linhas por frame
- Safe zone: 120px topo/base · 48px laterais

---

## 4. Thumbnail YouTube — 1280×720

**Função:** Clip / lyric video — legível em mobile 48px equivalente.  
**Doc completo:** [thumbnail-production.md](./thumbnail-production.md)

- Título "O LEGADO" Display 64–72px
- Rosto ou horizonte terço esquerdo
- Gradiente `esperanca` no hero

---

## Ordem de execução Canva

| Ordem | Asset | Motivo |
|-------|-------|--------|
| 1 | Carrossel slide 05 (mapa visual) | Define paleta de transição — reutilizar elementos |
| 2 | Carrossel slides 01–04, 06 | Mesmo arquivo multi-page |
| 3 | Post principal | Reutiliza foto/tratamento slide 06 |
| 4 | Thumbnail | Crop/adaptação do hero ato III |
| 5 | Story | Derivado slides 01 + 06 ou frames narrative |

---

## Checklist pré-export (G4)

### Identidade
- [ ] Tokens `legado-*` em todos os layouts
- [ ] Arco frio→ouro visível no carrossel completo
- [ ] Nenhum item Do Not Use ([identity § Do Not Use](../identity/track_identity.md#do-not-use))
- [ ] Sl 37:5 citado com referência NVI

### Tipografia
- [ ] Máx. 2 famílias por slide
- [ ] Body ≥ 16px equivalente mobile
- [ ] Contraste WCAG AA

### Formato
- [ ] Post 1080×1440
- [ ] Carrossel 6 slides 1080×1440
- [ ] Story 1080×1920
- [ ] Thumbnail 1280×720

### Copy
- [ ] Pouco texto — editorial premium
- [ ] Sem clichê gospel · sem prosperidade visual
- [ ] Hook alinhado à letra ("Não esquenta a cabeça...")

---

## Pendências externas (fora deste pacote)

| Item | Status | Impacto |
|------|--------|---------|
| Áudio master Suno | Pendente | Story/reel precisam de áudio no D0 |
| Clips Veo (6 cenas) | Pendente | Story pode usar stills até clips prontos |
| Capa Spotify 1:1 | Fora do escopo P0 social | Distribuição |
| Spotify Canvas loop | P1 | Pós-lançamento |
| Legendas IG/TikTok/YT | P0 copy separado | Publicação D0 |

---

**Próximo gate:** G4 — revisão visual após export Canva · [creative-review.md](./creative-review.md)
