# Design Specification — CDS (FCE)

A Design Specification transforma o **Creative Brief** em um **sistema visual documentado** — regras que qualquer designer ou agente de IA pode executar com consistência, sem reinterpretar estratégia a cada asset.

**Escopo:** permanente, multi-álbum.  
**Não gera:** imagens, layouts finais, arquivos Canva.

**Input obrigatório:** `creative-brief.md` aprovado.  
**Output:** `tracks/track-XX/design/design-specification.md`

---

## Fluxo

```
Creative Brief (01) → Design Specification (02) → Creative Review (03) → Canva / assets
                              ↓
                    Narrative Engine (paleta, luz, mood)
```

---

## Elementos do sistema visual

Cada elemento abaixo deve ser documentado na spec da faixa. Este documento ensina **o que**, **por que**, **quando** e **boas práticas** para cada um.

---

### Canvas

**O que é:** A superfície de trabalho — dimensões, proporção e zona segura de cada formato de entrega.

**Por que existe:** Assets cortados em mobile ou com texto sob UI de plataforma destroem campanha profissional.

**Quando usar:** Definir uma vez por campanha; derivar todos os formatos a partir da matriz.

**Boas práticas:**

| Formato | Dimensão | Uso FCE |
|---------|----------|---------|
| 9:16 | 1080 × 1920 | Reels, Stories, TikTok, Shorts |
| 1:1 | 1080 × 1080 | Feed, capa Spotify |
| 4:5 | 1080 × 1350 | Feed IG (opcional) |
| 16:9 | 1920 × 1080 | YouTube, clip |

- Declarar **safe zone** — margem superior/inferior livre de texto crítico (UI de plataforma)
- 9:16: evitar texto nos 15% superior e inferior
- Export em 2× para retina quando plataforma permitir

---

### Grid

**O que é:** Sistema de colunas e linhas invisíveis que organizam conteúdo — ritmo estrutural do layout.

**Por que existe:** Sem grid, carrosséis e capas parecem amadores mesmo com boa tipografia.

**Quando usar:** Todo layout com mais de um elemento (texto + imagem + logo).

**Boas práticas:**

| Formato | Grid sugerido |
|---------|---------------|
| 1:1 carrossel | 12 colunas, gutter 16–24px |
| 9:16 story | 6 colunas, margens laterais 48px |
| 16:9 thumbnail | 12 colunas, foco no terço esquerdo (rosto/título) |

- Alinhar texto a colunas — nunca "quase" alinhado
- Grid pode ser assimétrico se intencional (documentar no creative review)
- VibeCore épico: grid mais aberto; íntimo: grid mais fechado

---

### Margins

**O que é:** Espaço entre conteúdo e borda do canvas — respiração estrutural.

**Por que existe:** Margens apertadas comunicam ansiedade; generosas comunicam confiança e premium.

**Quando usar:** Sempre — mínimo definido por formato.

**Boas práticas:**

| Formato | Margem mínima |
|---------|---------------|
| 1:1 | 64–80px |
| 9:16 | 48–64px laterais; 120px top/bottom safe |
| 16:9 | 80px |

- Margens **maiores** em slides devocionais (leitura longa)
- Margens **menores** apenas em slides de impacto visual puro
- Consistência entre slides de um mesmo carrossel

---

### Whitespace

**O que é:** Espaço vazio intencional **dentro** do grid — entre blocos de conteúdo.

**Por que existe:** Hierarquia e foco; whitespace não é "espaço desperdiçado".

**Quando usar:** Entre título e corpo; entre versículo e aplicação; ao redor de elemento hero.

**Boas práticas:**
- Um foco por slide — se precisa de muito texto, dividir slide
- Whitespace generoso em tom contemplativo (ballad, lamento)
- Menos whitespace em tom festivo — mas nunca zerar
- Testar em tela de celular real — não só no desktop

---

### Typography

**O que é:** Sistema de fontes, pesos, tamanhos e espaçamento tipográfico.

**Por que existe:** Tipografia é 80% da identidade em social; fonte errada quebra VibeCore instantaneamente.

**Quando usar:** Definir escala completa antes do primeiro slide.

**Boas práticas:**

| Nível | Função | Escala relativa |
|-------|--------|-----------------|
| Display | Título de capa, hook visual | 1× (maior) |
| H1 | Título de slide | 0.65× display |
| H2 | Subtítulo, seção | 0.5× display |
| Body | Texto devocional | 16–20px equivalente |
| Caption | Referência bíblica, crédito | 12–14px |
| CTA | Chamada | Bold, legível em mobile |

- Máximo **2 famílias** por campanha (display + body)
- Display: serif majestosa ou sans geométrica conforme vibe
- Body: sans altamente legível em PT-BR
- Line-height body: 1.4–1.6
- Tracking: abrir levemente em caps display
- **Nunca** texto abaixo de 12px em mobile

---

### Hierarchy

**O que é:** Ordem em que o olho percorre o layout — o que vem primeiro, segundo, terceiro.

**Por que existe:** Sem hierarquia, versículo e CTA competem; nada é lido.

**Quando usar:** Cada slide e cada capa — desenhar hierarquia antes de escolher foto.

**Boas práticas:**

| Nível | Típico em FCE |
|-------|---------------|
| 1º | Hook visual ou versículo anchor |
| 2º | Título da faixa / conceito |
| 3º | Corpo devocional |
| 4º | CTA / referência / handle |

- Tamanho + peso + contraste + posição = hierarquia
- Um único elemento dominante por slide
- Carrossel: hierarquia pode evoluir slide a slide (arco narrativo)

---

### Photography

**O que é:** Direção de estilo fotográfico — tipo de imagem, tratamento, sujeito, autenticidade.

**Por que existe:** FCE usa fotografia cinematográfica contemporânea — não stock genérico de igreja.

**Quando usar:** Sempre que asset incluir foto ou frame de vídeo.

**Boas práticas:**

| Vibe | Direção fotográfica |
|------|---------------------|
| Dark / lamento | Contraste alto, sombras, close emocional |
| Épico / arena | Wide, golden hour, escala |
| Festivo | Movimento, cores quentes, energia |
| Íntimo | Soft, shallow depth, luz natural |

- Pessoas reais, diversidade brasileira autêntica
- Evitar stock "sorriso de dentes brancos no campo"
- Fotografia pode ser **frame de Veo** — spec deve alinhar mood
- P&B apenas se documentado na spec

---

### Lighting

**O que é:** Direção de luz para fotografia, ilustração e coerência com vídeo.

**Por que existe:** Luz comunica emoção antes do texto; desalinhamento com Narrative Engine quebra campanha.

**Quando usar:** Definir paleta de luz macro; derivar por asset.

**Boas práticas:**

| Emoção campanha | Luz |
|-----------------|-----|
| Esperança | Golden hour, backlight suave |
| Lamento | Low key, azul-cinza |
| Paz | Diffused, wrap |
| Vitória | High contrast, lens flare controlado |
| Adoração | Volumetric, god rays sem kitsch |

- Documentar temperatura de cor (K) quando relevante
- Narrative Engine e design spec **compartilham** direção de luz macro
- Evitar flash direto de evento — exceto se estética documental intencional

---

### Composition

**O que é:** Como elementos se organizam no frame — regra dos terços, simetria, leading lines, enquadramento.

**Por que existe:** Composição guia emoção; centro morto sem intenção é amador.

**Quando usar:** Todo asset com imagem dominante.

**Boas práticas:**
- **9:16:** sujeito em terço superior ou inferior; linhas verticais urbanas
- **1:1:** centro ou terços conforme hierarquia
- Leading lines para versículo ou rosto
- Espaço negativo para texto overlay
- Símbolos bíblicos como metáfora — não literal centralizado

---

### Depth

**O que é:** Sensação de camadas — foreground, midground, background; sombra e elevação em layout.

**Por que existe:** Profundidade separa design premium de template plano.

**Quando usar:** Capas, slides hero, thumbnails.

**Boas práticas:**
- Foto: shallow depth of field para foco emocional
- Layout: sombra suave em cards (blur 8–24px, opacity 10–25%)
- Não empilhar mais de 3 camadas visuais
- Depth em vídeo: alinhar com `06_cinematography_library.md`

---

### Icons

**O que é:** Sistema de ícones — estilo, peso de traço, uso permitido.

**Por que existe:** Ícones inconsistentes destroem brand em carrosséis devocionais.

**Quando usar:** CTAs, bullets, separadores — não decoração excessiva.

**Boas práticas:**
- Um estilo: outline **ou** filled — nunca misturar
- Stroke 1.5–2px consistente
- Tamanho mínimo 24px em mobile
- Evitar ícones religiosos clichê (cruz ornamentada, pomba cartoon)
- Preferir ícones funcionais (play, share, seta) sobre símbolos teológicos

---

### Texture

**O que é:** Superfície tátil visual — grão, noise, papel, gradientes, materiais.

**Por que existe:** VibeCore teatral se beneficia de textura sutil; digital plano demais parece template.

**Quando usar:** Backgrounds, overlays, separação de seções.

**Boas práticas:**

| Vibe | Textura |
|------|---------|
| Acústico / íntimo | Grão leve, papel, noise 3–5% |
| Arena / épico | Gradient mesh, light leak sutil |
| Dark trap | Noise alto, vignette |
| Festivo | Mínima — cores saturadas bastam |

- Textura nunca compete com legibilidade
- Opacity baixa (5–15%) em overlays
- Documentar se textura é fixa ou por slide

---

### Visual Style

**O que é:** A síntese — como todos os elementos acima se combinam na identidade desta campanha.

**Por que existe:** É o "como reconhecer" sem ver o logo.

**Quando usar:** Resumo executivo no topo da design spec.

**Boas práticas:**
- 3–5 adjetivos + 3 proibições
- Paleta de cores nomeada (ver abaixo)
- Relação com brand do álbum (`library/canva/album-XX-brand.md` se existir)
- Coerência com `vibe` em `track.yaml`

**Paleta (documentar na spec):**

| Token | Uso | Hex |
|-------|-----|-----|
| primary | Títulos, destaques | #______ |
| secondary | Subtítulos, acentos | #______ |
| background | Fundo dominante | #______ |
| surface | Cards, overlays | #______ |
| text-primary | Corpo | #______ |
| text-muted | Legendas, refs | #______ |
| accent | CTA, links | #______ |

---

### Responsividade

**O que é:** Como o sistema visual adapta entre formatos e tamanhos de tela — não só redimensionar, **reorganizar**.

**Por que existe:** Legenda legível em story pode ser ilegível em thumbnail.

**Quando usar:** Definir regras de adaptação entre 9:16, 1:1 e 16:9.

**Boas práticas:**

| Regra | Aplicação |
|-------|-----------|
| Escala tipográfica | Reduzir body proporcionalmente em 9:16 se texto longo |
| Crop inteligente | Foco central em rosto para adaptar 16:9 → 9:16 |
| Prioridade de conteúdo | Em telas pequenas: versículo > decoração |
| Touch targets | CTAs com área mínima 44×44px equivalente |
| Teste | Preview em 375px width mínimo |

- Um master layout por família (carrossel, capa) — derivar formatos
- Documentar o que **cai** em adaptação (texto secundário, textura)

---

## Integração cross-módulo

| Módulo | O que recebe da Design Spec |
|--------|----------------------------|
| Narrative Engine | Paleta, lighting, photography mood |
| Prompt Composer | Color palette, lighting descriptors EN |
| Canva brief | Tokens, grid, tipografia, formatos |
| Filmora | Color grade LUT direction |
| Copy | Hierarquia informa estrutura de legenda |

---

## Template reutilizável — Design Specification

Salvar em: `tracks/track-XX/design/design-specification.md`

```yaml
---
spec_id: design-spec-{track_id}
brief_id: brief-{track_id}
track_id: track-{NN}
version: "1.0"
status: draft          # draft | in_review | approved
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

```markdown
# Design Specification — {Título da faixa}

**Brief:** [creative-brief.md](./creative-brief.md)  
**Visual style (resumo):** [PREENCHER — 3 adjetivos]

---

## Canvas

| Formato | Dimensão | Safe zone | Uso |
|---------|----------|-----------|-----|
| 9:16 | 1080×1920 | | |
| 1:1 | 1080×1080 | | |
| 16:9 | 1920×1080 | | |

## Grid

| Formato | Colunas | Gutter | Margem |
|---------|---------|--------|--------|
| | | | |

## Margins & Whitespace

| Contexto | Margem | Whitespace entre blocos |
|----------|--------|-------------------------|
| Carrossel | | |
| Capa | | |
| Story | | |

## Typography

| Nível | Família | Peso | Tamanho | Line-height |
|-------|---------|------|---------|-------------|
| Display | | | | |
| H1 | | | | |
| Body | | | | |
| Caption | | | | |

## Hierarchy

1. [PREENCHER — elemento primário]
2. [PREENCHER]
3. [PREENCHER]

## Photography

**Direção:** [PREENCHER]  
**Sujeito:** [PREENCHER]  
**Evitar:** [PREENCHER]

## Lighting

**Macro:** [PREENCHER]  
**Temperatura:** [PREENCHER]  
**Alinhamento vídeo:** [sim/não — ref narrative]

## Composition

[PREENCHER — regras de enquadramento por formato]

## Depth

[PREENCHER — foto + layout]

## Icons

**Estilo:** [outline/filled]  
**Stroke:** [PREENCHER]  
**Uso permitido:** [PREENCHER]

## Texture

[PREENCHER — tipo, opacity, onde aplicar]

## Visual Style

**Adjetivos:** [PREENCHER]  
**Proibições:** [PREENCHER]

### Paleta

| Token | Hex | Uso |
|-------|-----|-----|
| primary | | |
| secondary | | |
| background | | |
| text-primary | | |
| accent | | |

## Responsividade

| De → Para | Regras de adaptação |
|-----------|---------------------|
| 16:9 → 9:16 | |
| 1:1 → story | |

---

## Aprovações

| Papel | Status | Data |
|-------|--------|------|
| Direção criativa | | |
| Design | | |
```

---

## Checklist Design Specification

- [ ] Brief aprovado como input
- [ ] Todos os 14 elementos documentados
- [ ] Paleta com tokens nomeados e hex
- [ ] Tipografia com escala completa
- [ ] Canvas com safe zones
- [ ] Lighting alinhado a vídeo (se aplicável)
- [ ] Responsividade entre formatos P0
- [ ] Status `approved` antes de Canva/Veo

---

## Referências

- [01_creative_brief.md](./01_creative_brief.md)
- [03_creative_review.md](./03_creative_review.md)
- [library/narrative_engine/06_cinematography_library.md](../narrative_engine/06_cinematography_library.md)
