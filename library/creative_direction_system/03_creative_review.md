# Creative Review — CDS (FCE)

O Creative Review é o **sistema de aprovação** do Franklin Creative Engine. Transforma brief e design spec em **gates de qualidade** — nenhuma execução (Canva, Veo, publicação) avança sem revisão documentada.

**Escopo:** permanente, multi-álbum.  
**Não gera:** assets, feedback automático, imagens.

**Inputs obrigatórios:**
- `creative-brief.md` (status `approved` ou em revisão final)
- `design-specification.md` (completo)
- Assets em revisão (quando aplicável — fase de execução)

**Output:** `tracks/track-XX/design/creative-review.md`

---

## Filosofia de revisão

1. **Revisar intenção antes de pixels** — brief e spec falhos geram retrabalho infinito
2. **Checklists não substituem julgamento** — mas impedem esquecimento sistemático
3. **Aprovação é explícita** — "parece bom" no chat não conta; status no documento conta
4. **VibeCore Alerts bloqueiam** — pendência teológica = não publicar
5. **Revisão por fase** — estratégia → design → assets → publicação

---

## Fases de revisão

```
Fase A — Estratégia     → Checklists: qualidade, bíblico, emocional, marketing (brief)
Fase B — Design System  → Checklists: visual, branding (spec)
Fase C — Assets         → Todos os checklists em assets concretos
Fase D — Pré-publicação → Gate final operacional
```

---

## Papéis de aprovação

| Papel | Responsabilidade |
|-------|------------------|
| **Direção criativa** | Big idea, coerência VibeCore, excelência artística |
| **Teologia / VibeCore** | Fidelidade bíblica, alerts, tom ministerial |
| **Design** | Sistema visual, legibilidade, consistência |
| **Produção** | Entregáveis completos, formatos, cronograma |
| **Marketing** | CTAs, funil, plataforma, mensagem ao público |

Em projetos solo: um humano pode acumular papéis — mas **cada checklist deve ser respondido**.

---

## Checklist de qualidade (geral)

Aplica-se a **todo** projeto CDS antes de aprovar Fase A.

### Estrutura documental

- [ ] `creative-brief.md` existe e está completo (14 seções)
- [ ] `design-specification.md` existe e está completo (14 elementos)
- [ ] `creative-review.md` (este documento) preenchido
- [ ] Links cruzados para `track.yaml`, `concept.md`, `lyrics.md`
- [ ] Versão e status documentados no frontmatter
- [ ] CHANGELOG atualizado se mudança estrutural

### Coerência interna

- [ ] Big idea aparece refletida na design spec (visual style)
- [ ] Mensagem-chave do brief alinha com hierarquia tipográfica
- [ ] Entregáveis P0 do brief têm spec visual correspondente
- [ ] Cronograma estratégico compatível com assets planejados
- [ ] Nenhuma contradição entre tom do brief e direção fotográfica

### Excelência FCE

- [ ] VibeCore identificável em ≤ 3 segundos de qualquer asset P0
- [ ] Refrão da faixa reconhecível na campanha
- [ ] Campanha não parece template genérico de motivação
- [ ] Documentação legível por agente sem contexto de chat

---

## Checklist visual

Aplica-se na **Fase B** (design spec) e **Fase C** (assets).

### Sistema visual

- [ ] Paleta com tokens nomeados — não cores soltas sem função
- [ ] Tipografia: máximo 2 famílias; escala definida
- [ ] Grid e margens documentados por formato P0
- [ ] Hierarquia clara em layout tipo (capa, slide, story)
- [ ] Whitespace intencional — não crowding
- [ ] Safe zones respeitadas em 9:16

### Execução (assets)

- [ ] Legibilidade em mobile 375px width
- [ ] Contraste texto/fundo suficiente (WCAG AA mínimo onde aplicável)
- [ ] Imagens alinhadas à direção fotográfica da spec
- [ ] Textura e depth não competem com conteúdo
- [ ] Ícones consistentes (estilo único)
- [ ] Nenhum texto cortado por UI de plataforma
- [ ] Adaptação entre formatos segue regras de responsividade

### Vídeo (quando aplicável)

- [ ] Narrative Pipeline completo antes de revisar clips
- [ ] Color grade alinhado à paleta da design spec
- [ ] 9:16 priorizado para entregável social P0
- [ ] Legendas no Filmora — não texto acidental no Veo
- [ ] Continuidade visual entre cenas

---

## Checklist de branding

Aplica-se em **Fase B** e **Fase C**.

### Identidade de álbum

- [ ] Coerência com brand do álbum (`library/canva/album-XX-brand.md` se existir)
- [ ] Paleta da faixa derivada ou complementar ao álbum — não aleatória
- [ ] Tipografia compatível com sistema do álbum
- [ ] Faixa distinguível dentro do álbum — não clone de outra track

### Consistência cross-touchpoint

- [ ] Capa, carrossel, reel e thumbnail "parecem mesma campanha"
- [ ] Tom visual alinha com tom sonoro (vibe em `track.yaml`)
- [ ] Big idea reconhecível em pelo menos 3 touchpoints P0
- [ ] Nome da faixa e álbum grafados consistentemente

### Anti-brand (proibições)

- [ ] Sem estética de igreja genérica anos 2000
- [ ] Sem stock photo clichê cristão
- [ ] Sem logos de terceiros não autorizados
- [ ] Sem paleta que contradiz emoção da faixa (festivo em lamento, etc.)

---

## Checklist bíblico

Aplica-se em **todas as fases** — bloqueante se falhar.

### Fidelidade textual

- [ ] Versículos citados com referência correta (livro cap:v)
- [ ] Versão bíblica declarada (NVI, ARA, etc.)
- [ ] Citações conferidas contra texto — não de memória
- [ ] Letra da faixa não contradiz passagem base sem VibeCore Alert documentado
- [ ] Metáforas visuais ancoradas em Escritura — não decorativas

### Teologia e tom

- [ ] Mensagem aponta para Cristo/Escritura — não autoajuda secular
- [ ] Lamento não resolvido prematuramente em faixa de lamento
- [ ] Esperança presente em arcos que exigem esperança cristã
- [ ] CTAs autênticos — sem manipulação de culpa ou medo
- [ ] Ministração (se houver) alinhada ao conceito da faixa

### VibeCore Alerts

- [ ] `vibecore_alerts` em `track.yaml` verificado
- [ ] Nenhum alert aberto no momento da aprovação final
- [ ] Pendências teológicas escaladas para humano — não resolvidas silenciosamente

---

## Checklist emocional

Aplica-se na **Fase A** (brief) e **Fase C** (assets).

### Arco emocional

- [ ] Emoção dominante da campanha identificável e nomeada
- [ ] Arco emocional completo (setup → tensão → resolução) em vídeo/carrossel longo
- [ ] Tom do brief refletido nos assets — não apenas no áudio
- [ ] Hook dos primeiros 3s (vídeo) ou primeiro slide (carrossel) retém atenção

### Empatia e autenticidade

- [ ] Público se vê representado — sem caricatura
- [ ] Dor tratada com dignidade — não exploração
- [ ] Celebração sem superficialidade
- [ ] Emoção serve a mensagem — não emoção por emoção

### Coerência som ↔ visual

- [ ] Assets visuais compatíveis com dinâmica da faixa (intro íntima vs chorus explosivo)
- [ ] Momentos de ministração têm respiração visual
- [ ] Vibe dark não iluminada como festa — e vice-versa

---

## Checklist de marketing

Aplica-se na **Fase A** e **Fase D**.

### Estratégia

- [ ] Persona definida com barreira e contexto reais
- [ ] Big idea diferenciada e memorável
- [ ] Entregáveis P0 cobrem funil: awareness → engajamento → conversão espiritual
- [ ] Plataformas escolhidas com função clara — não "postar em tudo"
- [ ] Cronograma estratégico documentado

### Copy e CTA

- [ ] Hook alinhado ao refrão ou mensagem-chave
- [ ] CTAs cristãos autênticos (ouvir, compartilhar, refletir — não clickbait)
- [ ] Hashtags planejadas (se aplicável) — não spam
- [ ] Legendas por plataforma previstas em entregáveis

### Funil e calendário

- [ ] Pré-lançamento gera expectativa sem entregar tudo
- [ ] Dia D tem asset hero (reel ou clip)
- [ ] Pós-lançamento sustenta (devocional, estudo, CTA)
- [ ] Critérios de sucesso do brief revisitados na Fase D

### Compliance

- [ ] Sem promessas de cura/prosperidade se faixa não trata disso
- [ ] Sem comparação depreciativa com outras denominações
- [ ] Créditos e direitos autorais previstos

---

## Matriz de gates

| Gate | Pré-requisito | Checklists obrigatórios | Aprovador mínimo |
|------|---------------|-------------------------|------------------|
| **G1 — Brief** | Track documentada | Qualidade, Bíblico, Emocional, Marketing | Direção + Teologia |
| **G2 — Design Spec** | G1 aprovado | Qualidade, Visual, Branding | Direção + Design |
| **G3 — Narrative** | G1 aprovado | Bíblico, Emocional, Visual (vídeo) | Direção criativa |
| **G4 — Assets** | G2 + G3 (se vídeo) | Todos | Todos os papéis relevantes |
| **G5 — Publicação** | G4 aprovado | Marketing, Bíblico (final) | Produção + Teologia |

---

## Template reutilizável — Creative Review

Salvar em: `tracks/track-XX/design/creative-review.md`

```yaml
---
review_id: review-{track_id}
brief_id: brief-{track_id}
spec_id: design-spec-{track_id}
track_id: track-{NN}
version: "1.0"
phase: A              # A | B | C | D
status: in_progress   # in_progress | approved | blocked
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

```markdown
# Creative Review — {Título da faixa}

**Fase atual:** [A / B / C / D]  
**Gate alvo:** [G1 / G2 / G3 / G4 / G5]

---

## Resumo da revisão

[PREENCHER — 2–3 frases: o que foi revisado, resultado geral]

## Bloqueios

| ID | Descrição | Severidade | Responsável | Status |
|----|-----------|------------|-------------|--------|
| | | blocker / major / minor | | |

---

## Checklist de qualidade

- [ ] [itens conforme seção acima]

**Notas:** [PREENCHER]

---

## Checklist visual

- [ ] [itens]

**Notas:** [PREENCHER]

---

## Checklist de branding

- [ ] [itens]

**Notas:** [PREENCHER]

---

## Checklist bíblico

- [ ] [itens]

**Notas:** [PREENCHER]

---

## Checklist emocional

- [ ] [itens]

**Notas:** [PREENCHER]

---

## Checklist de marketing

- [ ] [itens]

**Notas:** [PREENCHER]

---

## Decisões e exceções

| Decisão | Justificativa | Aprovado por |
|---------|---------------|--------------|
| | | |

---

## Aprovações

| Papel | Gate | Status | Data | Assinatura |
|-------|------|--------|------|------------|
| Direção criativa | | pending / approved / rejected | | |
| Teologia / VibeCore | | | | |
| Design | | | | |
| Produção | | | | |
| Marketing | | | | |

---

## Histórico de revisões

| Data | Fase | Revisor | Resultado | Notas |
|------|------|---------|-----------|-------|
| | | | | |
```

---

## Resultados possíveis

| Status | Significado | Próximo passo |
|--------|-------------|---------------|
| **approved** | Gate liberado | Avançar para próxima fase |
| **approved_with_notes** | Liberado com ressalvas menores | Corrigir na execução; documentar |
| **revision_required** | Retrabalho necessário | Voltar ao brief ou spec |
| **blocked** | Bloqueio teológico ou estratégico grave | Escalar humano; VibeCore Alert |

---

## Integração com status da faixa

| Gate aprovado | Sugestão `track.yaml` status |
|---------------|------------------------------|
| G1 | `creative_brief_approved` (custom) ou manter `lyrics_final` |
| G2 | `design_spec_approved` |
| G4 | `video` ou `campaign_ready` |
| G5 | `published` (após publicação real) |

*Nota: valores custom podem ser adicionados ao schema conforme evolução.*

---

## Anti-padrões de revisão

| Evitar | Por quê |
|--------|---------|
| Aprovar brief vazio "para avançar" | Retrabalho em cascata |
| Pular checklist bíblico em faixa devocional | Risco ministerial |
| Revisar pixels sem spec | Critério subjetivo inconsistente |
| Aprovação verbal sem documento | Agentes perdem memória |

---

## Referências

- [01_creative_brief.md](./01_creative_brief.md)
- [02_design_specification.md](./02_design_specification.md)
- [README.md](./README.md)
- [legal/vibecore-alerts.md](../../albums/) — por álbum
