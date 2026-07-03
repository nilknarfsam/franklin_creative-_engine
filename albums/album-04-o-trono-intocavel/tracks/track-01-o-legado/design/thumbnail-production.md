---
asset_id: thumbnail-track-01-p0
track_id: track-01
format: "16:9"
dimensions: "1280x720"
version: "1.0"
status: ready_for_canva
created: 2026-07-02
---

# Thumbnail YouTube — Produção Canva · O Legado

**Formato:** **1280 × 720** (16:9)  
**Função:** Clip / lyric video YouTube — legível em mobile (equivalente 48px+)  
**Plano:** [assets-p0-plan.md](./assets-p0-plan.md)

---

## Objetivo

Thumbnail reconhecível em ≤ 2s: **O LEGADO** + rosto ou horizonte dourado + arco `esperanca`. Deve competir no feed YT mobile sem parecer gospel stock ou clickbait.

---

## Texto exato

| Nível | Conteúdo |
|-------|----------|
| Display | O LEGADO |
| Subtitle | Salmo 37 |
| Micro (opcional) | O Trono Intocável · Faixa 01 |

**Não incluir:** versículo completo (ilegível em mobile) · "ASSISTA AGORA" · setas exageradas

---

## Hierarquia visual

1. **Imagem hero** — rosto sereno OU horizonte dourado (terço esquerdo)
2. **Display** "O LEGADO" — terço direito ou sobreposto com contraste
3. **Subtitle** "Salmo 37" — abaixo do Display, Scripture/caption
4. **Micro** álbum — canto inferior direito, 14px
5. Gradiente `esperanca` — suporte,           sky treatment

Ordem de leitura: olho → título → referência bíblica.

---

## Paleta

| Elemento | Token / valor |
|----------|---------------|
| Céu / gradiente hero | `esperanca` — `#553C9A` → `#C9A227` → `#F6E05E` |
| Display | `legado-white` `#F7FAFC` — drop shadow sutil `legado-night` 40% |
| Subtitle | `legado-gold` `#C9A227` ou `legado-amber` |
| Micro | `legado-earth` `#718096` |
| Overlay lateral (se texto sobre foto) | `legado-night` 55% — apenas faixa direita 45% width |
| Contorno Display (opcional) | 2px `legado-night` — legibilidade sobre céu claro |

---

## Imagem sugerida

**Opção A (preferida) — Rosto + horizonte**

Homem brasileiro ~30 anos, 3/4 profile olhando para horizonte dourado. Expressão: paz serena, não sorriso. Camisa azul-marinho. Golden hour no rosto (luz quente lateral). Background: skyline desfocado + céu purple-gold. Shallow DOF. Símbolo `dawn`.

**Opção B — Horizonte épico**

Wide shot calçada arborizada ao amanhecer — homem pequeno caminhando para luz. Escala cinematográfica. Mais texto visível. Símbolo `path` + `dawn`.

**Referência canônica:** Narrative cena 06 · Moodboard Painel 6.

**Busca Canva:** "golden hour portrait man hope cinematic" · "sunrise city skyline purple orange"

**Evitar:** boca aberta shock face · setas vermelhas · filtro HDR · cruz · Bíblia aberta

---

## Composição

| Parâmetro | Valor |
|-----------|-------|
| Canvas | 1280 × 720 |
| Margem | 80px mínima |
| Grid | 12 colunas · gutter 24px |
| Sujeito | Terço esquerdo (cols 1–5) |
| Tipografia | Terço direito (cols 7–12) ou overlay centralizado inferior |
| Espaço negativo | 35% mínimo — céu ou overlay limpo |
| Profundidade | 3 camadas max: bg skyline · mid sujeito · fg texto |

### Layout recomendado

```
┌─────────────────────────────────────────────┐
│  [céu purple-gold]     │   O LEGADO         │
│                        │   Salmo 37         │
│   [rosto 3/4]          │                    │
│   golden hour          │   O Trono Intocável│
│   [skyline blur]       │   Faixa 01         │
└─────────────────────────────────────────────┘
     terço esquerdo              terço direito
```

### Alternativa mobile-first

Display "O LEGADO" grande bottom-left sobre overlay escuro; rosto ocupa 60% frame; subtitle acima do título.

---

## Tipografia (escala 16:9 / 1280×720)

| Nível | Família | Tamanho | Peso |
|-------|---------|---------|------|
| Display | Serif majestosa | **72px** | Bold |
| Subtitle | Sans ou Scripture | **28px** | Medium Italic |
| Micro | Sans small caps | **14px** | Regular |

- Tracking Display: +3%
- Line-height Display: 1.05
- **Teste:** reduzir preview Canva a 25% — título ainda legível

---

## Tratamento de imagem

| Ajuste | Valor |
|--------|-------|
| Saturação céu | +10% (ato III) |
| Sombras | Lift leve — não esmagar rosto |
| Grão | 2% max — thumbnail deve ser nítida |
| Vignette | 8% cantos — foco central |
| LUT feel | `legado-gold` lift em highlights |

---

## Observações Canva

### Setup
- Template: YouTube Thumbnail → redimensionar/confirmar **1280 × 720**
- Duplicar layout do post principal 4:5 e adaptar crop — manter mesma foto hero

### Contraste
- Display sobre céu claro: adicionar overlay `legado-night` 30% atrás do texto OU stroke 2px
- WCAG AA obrigatório — testar contraste branco sobre gold

### Export
- PNG · máx. qualidade
- Filename: `track-01-thumbnail-youtube-o-legado.png`
- Destino: `design/exports/`
- Tamanho arquivo: ideal < 2MB (YT aceita até 2MB estático)

### Variantes A/B (opcional)
| Variante | Diferença | Teste |
|----------|-----------|-------|
| A | Rosto close | CTR emoção |
| B | Wide horizonte | CTR escala épica |

Manter tipografia idêntica entre variantes.

---

## Coerência cross-asset

| Asset | Elemento compartilhado |
|-------|----------------------|
| Post principal 4:5 | Mesma foto hero · Display · Sl 37:5 |
| Carrossel slide 06 | Mesma foto · CTA visual |
| Story frame 03 | Mesmo amanhecer · título |
| Capa Spotify (futuro) | Crop central 1:1 desta foto |

---

## Título vídeo sugerido (YT — fora do thumbnail)

```
O Legado | Salmo 37 — Trap Acústico & Pop Teatral | O Trono Intocável
```

Thumbnail não repete título longo — apenas "O LEGADO" + "Salmo 37".

---

## Checklist thumbnail

- [ ] 1280 × 720 px
- [ ] "O LEGADO" legível em preview 25%
- [ ] Tokens `legado-*` — gradiente `esperanca` presente
- [ ] Terço esquerdo: rosto ou horizonte
- [ ] Sem versículo completo · sem clickbait
- [ ] Sem Do Not Use (halos, cruz dominante, stock gospel)
- [ ] Margem 80px respeitada
- [ ] Export PNG em `design/exports/`

---

## Pendências

| Item | Nota |
|------|------|
| Foto final | Usar still Veo cena 06 quando clip existir — substituir stock Canva |
| A/B test | Após 7 dias publicação, comparar CTR variantes A/B se ambas produzidas |
