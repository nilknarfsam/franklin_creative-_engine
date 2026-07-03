---
asset_id: story-track-01-p0
track_id: track-01
format: "9:16"
dimensions: "1080x1920"
frames: 3
version: "1.0"
status: ready_for_canva
created: 2026-07-02
---

# Story Teaser — Produção Canva · O Legado

**Formato:** **1080 × 1920** (9:16) · **3 frames** sequenciais  
**Função:** Pré-lançamento D-3 — teaser emocional + CTA ouça  
**Plano:** [assets-p0-plan.md](./assets-p0-plan.md)

---

## Estratégia

Story de impacto imediato — **pouco texto**, arco comprimido em 3 telas (~5s cada, 15s total com tap ou vídeo estático). Alternativa: publicar frame 3 isolado como story único no D-1.

| Frame | Ato | Função | Paleta |
|-------|-----|--------|--------|
| 1 | I | Hook — peso do dia | `pressao` |
| 2 | II→III | Virada — entrega | `transfiguracao` |
| 3 | III | CTA — luz que rompe | `esperanca` |

---

## Safe zones (obrigatório)

| Zona | Medida |
|------|--------|
| Topo | 120px livres — sem texto crítico (UI IG) |
| Base | 120px livres — sem CTA (barra resposta) |
| Laterais | 48px margem mínima |
| Texto máx. | 2 linhas por frame |
| Grid | 6 colunas · gutter 16px |

---

## Frame 01 — Hook

### Texto exato

| Linha | Conteúdo |
|-------|----------|
| 1 | Não esquenta a cabeça. |
| 2 | Deixa o tempo mostrar. |

### Hierarquia visual

1. Imagem full-bleed — crepúsculo urbano, homem saindo do trabalho (cena 01 narrative)
2. Linha 1 — H1 bold, terço inferior
3. Linha 2 — Body, abaixo, `legado-earth`
4. Sem logo · sem versículo neste frame

### Paleta

| Elemento | Token |
|----------|-------|
| Fundo foto | Desaturado −15%, azul-cinza |
| Overlay | `legado-night` 50% bottom third |
| Linha 1 | `legado-white` 40px sans bold |
| Linha 2 | `legado-earth` 18px |

### Imagem sugerida

Homem ~30 anos, camisa azul-marinho, saindo de portaria/comercial modesto ao entardecer. Ombros pesados, luz fluorescente fria. Calçada como `path`. Grão 4%. **Referência:** Narrative cena 01 · Moodboard Painel 1.

**Busca Canva:** "worker leaving building dusk urban brazil moody"

### Composição

- Sujeito terço inferior-esquerdo
- Céu/edifícios terço superior — espaço negativo
- Texto alinhado centro-inferior, acima da safe zone base (120px)
- Leading line vertical da arquitetura

### Observações Canva

- Sticker "Próximo" ou seta outline `legado-gold` 1.5px — opcional, canto direito
- Não usar fonte meme · não usar countdown fake
- Export: `track-01-story-f01-hook.png`

---

## Frame 02 — Virada

### Texto exato

| Linha | Conteúdo |
|-------|----------|
| 1 | Entrega o teu caminho. |
| 2 | Confia. |

### Hierarquia visual

1. Fundo — transição visual: metade superior foto fria, metade inferior warm (split gradient)
2. Linha 1 — Display serif 56px, centrado terço médio
3. Linha 2 — "Confia." isolado em `legado-gold`, maior peso
4. Transição `transfiguracao` como camada sobre foto

### Paleta

| Elemento | Token |
|----------|-------|
| Gradiente overlay | `transfiguracao` `#718096` → `#C9A227` diagonal |
| Linha 1 | `legado-white` |
| Linha 2 | `legado-gold` Display 64px |
| Foto base | Terraço, olhos fechados, livro fechado — opacity 30% |

### Imagem sugerida

Homem no terraço, olhos fechados, livro fechado no colo — símbolo `word`. Céu nublado. Foto em baixa opacity sob gradiente quente. Sensação: bridge / pausa antes do clímax.

**Busca Canva:** "man terrace peaceful eyes closed" — mesma ref. carrossel slide 04

### Composição

- Tipografia centrada verticalmente (entre safe zones)
- Split diagonal 45° frio→quente reforça arco narrativo
- Máximo 5 palavras totais — respeitado
- "Confia." com tracking aberto +2%

### Observações Canva

- **Momento teatral** — eco refrão sem overcrowding
- Pode animar no Canva: fade frio→ouro (se exportar vídeo story)
- Export: `track-01-story-f02-virada.png`

---

## Frame 03 — CTA

### Texto exato

| Linha | Conteúdo |
|-------|----------|
| Display | O LEGADO |
| CTA | OUÇA AGORA ↓ |
| Micro | Salmo 37 · Faixa 01 |

### Hierarquia visual

1. Foto hero — amanhecer, calçada, homem caminhando (cena 06)
2. **Display** "O LEGADO" — terço superior-médio
3. **CTA** — terço inferior, acima safe zone
4. **Micro** — abaixo do CTA, caption size
5. Sticker link "Ouvir no Spotify" — nativo IG quando publicar

### Paleta

| Elemento | Token |
|----------|-------|
| Fundo foto | Golden hour — `legado-purple` + `legado-gold` céu |
| Overlay bottom | `legado-night` 40% gradient |
| Display | `legado-white` 72px serif |
| CTA | `legado-gold` fill · texto `legado-night` bold |
| Micro | `legado-amber` 14px |

### Imagem sugerida

Calçada arborizada ao amanhecer. Homem caminha em direção à luz. Skyline brasileiro. God rays. Símbolo `dawn`. **Mesma foto** post principal / carrossel slide 06.

### Composição

- Homem no terço inferior, caminhando para cima (movimento ascensional)
- Display no terço médio-superior — nunca sobre rosto
- CTA button: min. 44px altura · 200px largura · cantos 24px
- Link sticker posicionado sobre CTA na publicação IG

### Observações Canva

- Preparar versão **com** e **sem** texto "OUÇA AGORA" ( sticker nativo substitui)
- Data sugerida: D-3 pré-lançamento · repost D-1
- Export: `track-01-story-f03-cta.png`

---

## Variante — Story único (D-1)

Para publicação rápida, usar **apenas Frame 03** com copy:

```
O Legado — faixa 01
Disponível amanhã.
```

Substituir CTA por "AMANHÃ" em `legado-gold`.

---

## Sequência de publicação

| Dia | Frame(s) | Nota |
|-----|----------|------|
| D-3 | 1 → 2 → 3 | Sequência completa |
| D-2 | Behind — foto plantio (slide 03 crop) | Sem texto ou "Plantio silencioso." |
| D-1 | Frame 3 variante "AMANHÃ" | Urgência suave |
| D0 | Repost reel + link | Story complementar ao lançamento |

---

## Audio (quando disponível)

- Overlay 15–30s do intro acústico ("Não esquenta a cabeça...") ou snippet refrão
- **Pendente:** master Suno — usar story estático até áudio pronto

---

## Export

| File | Uso |
|------|-----|
| `track-01-story-f01-hook.png` | Frame 1 |
| `track-01-story-f02-virada.png` | Frame 2 |
| `track-01-story-f03-cta.png` | Frame 3 |
| `track-01-story-animated.mp4` | Opcional — Canva animate 15s |

**Destino:** `design/exports/`

---

## Checklist story

- [ ] Safe zones 120px topo/base respeitadas
- [ ] Máx. 2 linhas texto por frame
- [ ] Tokens `legado-*` aplicados
- [ ] Sem texto legível em tela de celular
- [ ] Sem clichê gospel / stock smile
- [ ] CTA autêntico — não clickbait
