# Notas de montagem — Filmora Pro

**Faixa:** O Legado (Salmo 37)  
**Projeto:** Curta cinematográfico 9:16 — primeiro ciclo FCE  
**Status:** roteiro pronto — aguardando clips Veo + áudio Suno  
**Duração alvo:** 45–60 s

---

## Entregáveis

| Asset | Formato | Prioridade | Status |
|-------|---------|------------|--------|
| **Reel principal** | 9:16 · 1080×1920 | Alta | Pendente |
| Teaser 15 s | 9:16 | Média | Derivado (cenas 1+6) |
| SRT legendas | PT-BR | Alta | Pendente |
| Clip YouTube | 16:9 | Baixa | Reframe opcional |

**Export final:** `assets/video/track-01-o-legado-reel-9x16.mp4`

---

## Timeline master (45–60 s)

| Início | Fim | Cena | Transição | Áudio (faixa Suno) |
|--------|-----|------|-----------|-------------------|
| 0:00 | 0:07 | scene-01 | Fade in 0,5 s | Intro — guitarra íntima |
| 0:07 | 0:15 | scene-02 | Cut | Verse 1 início |
| 0:15 | 0:23 | scene-03 | Cut | Verse 1 — trap suave |
| 0:23 | 0:31 | scene-04 | Dissolve 12f | Bridge / voz baixa |
| 0:31 | 0:39 | scene-05 | Dissolve + grade | Pre-chorus build |
| 0:39 | 0:55 | scene-06 | **Cut no drop** | Chorus hook |
| 0:55 | 1:00 | — | Fade out 0,5 s | Chorus tail / reverb |

**Trecho musical sugerido:** 0:00 – 1:00 do master Suno (ajustar após áudio disponível).

---

## Import de mídia

```
assets/audio/
└── track-01-o-legado-master.wav    ← áudio Suno (PENDENTE)

assets/video/veo3/
├── scene-01-pressao.mp4
├── scene-02-comparacao.mp4
├── scene-03-fidelidade.mp4
├── scene-04-pausa.mp4
├── scene-05-transfiguracao.mp4
└── scene-06-esperanca.mp4
```

---

## Legendas e texto (SOMENTE Filmora — nunca Veo)

### Legenda principal — Cena 06

| Campo | Valor |
|-------|-------|
| Texto | Entrega o teu caminho ao Senhor; confia nele, e ele agirá. |
| Referência | Salmo 37:5 (NVI) |
| Início | 0:42 |
| Fim | 0:52 |
| Estilo | Sans serif clean, branco, sombra suave 40%, centralizado inferior |
| Animação | Fade in 0,3 s · Fade out 0,5 s |

### Legenda secundária (opcional) — Cena 04

| Campo | Valor |
|-------|-------|
| Texto | Descansa no Senhor e espera nele. |
| Referência | Sl 37:7 |
| Início | 0:26 |
| Fim | 0:30 |
| Opacidade | 85% — discreta |

### Título final (opcional)

| Campo | Valor |
|-------|-------|
| Texto | O LEGADO · Salmo 37 |
| Início | 0:52 |
| Fim | 0:58 |
| Fonte | Serif majestosa (paleta Álbum 4) |

---

## Color grading

| Acto | Cenas | LUT / ajuste |
|------|-------|--------------|
| I — Tensão | 01–02 | Desaturação −15%, shadows azulados, contrast +5 |
| II — Fidelidade | 03 | Neutro, leve lift nos mids |
| III — Pausa | 04 | Flat, baixo contraste, íntimo |
| IV — Paz | 05–06 | LUT warm golden, highlights âmbar, vibrance +10 nos céus |

**Match cut 04→05:** Usar dissolve longo; reforçar warm grade na 05 para continuidade emocional.

---

## Áudio

| Faixa | Nível | Notas |
|-------|-------|-------|
| Música Suno | −3 dB peak | Duck −6 dB opcional sob legendas se necessário |
| SFX ambiente | −18 a −24 dB | Opcional: trânsito cena 01, vento cena 05–06 |
| Voz / ministração | Nativo do master | Não adicionar VO extra |

**Sync crítico:** Cena 06 **cut exato** no primeiro kick/snare do chorus.

---

## Ritmo de corte

| Seção | Estilo | BPM feel |
|-------|--------|----------|
| 01–03 | Cuts secos no beat | Trap cadenciado |
| 04–05 | Dissolves lentos | Ballad / bridge |
| 06 | Cut energético + hold 2 s final | Arena pop-rock |

Evitar cortes rápidos demais nas cenas 04–05 — preservar respiração emocional.

---

## Texto cinético (opcional)

Se usar trechos da letra (não versículo):

- *"Entrega o teu caminho"* — sync com chorus, kinetic minimal
- Fonte consistente com carrossel Canva (se existir fora do repo)
- **Não** sobrepor versículo bíblico e letra no mesmo frame

---

## Export settings

| Parâmetro | Valor |
|-----------|-------|
| Resolução | 1080 × 1920 |
| Frame rate | 30 fps (ou 24 fps se clips Veo forem 24) |
| Codec | H.264, High Profile |
| Bitrate | 12–16 Mbps |
| Áudio | AAC 320 kbps |

**Plataformas:** Instagram Reels, TikTok, YouTube Shorts — mesmo master.

---

## Checklist pós-montagem

- [ ] 6 cenas Veo importadas e na ordem correta
- [ ] Áudio Suno syncado (drop cena 06)
- [ ] Sl 37:5 legível em mobile
- [ ] Nenhum texto acidental nos clips Veo
- [ ] Color grade coerente 01→06
- [ ] Duração final 45–60 s
- [ ] Export em `assets/video/`
- [ ] SRT exportado para acessibilidade
- [ ] Preview em tela de celular real

---

## Pendências

| ID | Item |
|----|------|
| P01 | Áudio master Suno não presente em `assets/audio/` |
| P02 | Clips Veo ainda não gerados |
| P03 | Carrossel/post de letra existem fora do repo — alinhar tipografia se possível |
| P04 | Campanha de lançamento (`campaign-track-01`) não criada |

---

## Próximos exports derivados

1. **Teaser 15 s** — cena 01 (3 s) + cena 06 (12 s) + Sl 37:5
2. **Stories 3×** — uma cena por story com sticker “Ouça O Legado”
3. **Thumbnail frame** — frame 0:45 cena 06 para YouTube

---

## Referências

- [veo3-video-plan.md](../veo3-video-plan.md)
- [storyboard.md](../storyboard.md)
- [veo3-prompts.md](../veo3-prompts.md)
- [WORKFLOW.md § Workflow 9](../../../../../WORKFLOW.md)
