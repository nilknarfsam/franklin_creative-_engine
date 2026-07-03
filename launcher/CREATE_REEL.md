# Launcher — Criar Reel

**Menu FCE.md:** Opção 5  
**Formato:** 9:16 (1080×1920) · 45–60s típico

---

## Objetivo

Orientar a IA a planejar **reel de lançamento** — hook, ordem de cenas, sync com áudio, legendas Filmora — usando Narrative Engine e clips Veo quando existirem.

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md)
3. [WORKFLOW.md § Narrative Pipeline](../WORKFLOW.md#narrative-pipeline--direção-cinematográfica-obrigatório)
4. [WORKFLOW.md § WF9](../WORKFLOW.md#workflow-9--geração-de-vídeo-com-veo-api)
5. `video/narrative/` — hook, character, scenes, director-commentary
6. `video/storyboard.md`, `video/filmora/edit-notes.md`
7. `design/creative-brief.md` — hook de campanha

---

## Perguntas que a IA deve fazer ao usuário

1. **Qual álbum e faixa?**
2. **Áudio master disponível?** (Suno export)
3. **Clips Veo gerados?** (`assets/video/veo3/`) — se não, orientar [CREATE_VIDEO_VEO.md](./CREATE_VIDEO_VEO.md)
4. **Tipo de reel?** (lançamento · lyric kinetic · teaser 15s)
5. **Duração alvo?** (45–60s · 15s teaser)
6. **Legendas?** (burn-in Filmora · SRT separado)

---

## Arquivos que a IA deve consultar

| Arquivo | Função |
|---------|--------|
| `video/narrative/hook.md` | Primeiros 3 segundos |
| `video/narrative/scenes.md` | Ordem e emoção das cenas |
| `video/veo3-prompts.md` | Prompts exportados |
| `video/storyboard.md` | Timing |
| `video/filmora/edit-notes.md` | Montagem |
| `lyrics.md` | Sync chorus/bridge |
| `technical-sheet.md` | Dinâmica musical |
| `copy/captions.md` | Legenda do reel |

---

## Saídas esperadas

1. **Plano do reel** — duração, hook, ordem de cenas, beats de corte
2. **Mapa áudio × vídeo** — intro íntima → explosão refrão
3. **Lista de clips necessários** — cena NN, take, path
4. **Instruções Filmora** — import, sync, color grade, export 9:16
5. **Legenda IG/TikTok** — ver [CREATE_CAPTION.md](./CREATE_CAPTION.md)
6. **Checklist** — retenção 15s, 9:16, legendas PT-BR, no text no footage

---

## Checklist de qualidade

- [ ] Narrative Pipeline completo antes de planejar
- [ ] Hook nos primeiros 3s
- [ ] Cortes no beat (chorus explosion)
- [ ] 9:16 export primário
- [ ] Legendas em camada — não no Veo
- [ ] Director commentary respeitado
- [ ] CTA e hashtags na legenda

---

## O que a IA não deve fazer

- ❌ Escrever prompts Veo manualmente (usar Prompt Composer)
- ❌ Pular Narrative Engine
- ❌ Planejar 16:9 como primário social
- ❌ Texto legível nos clips Veo
- ❌ Gerar MP4 ou commitar vídeos
- ❌ Alterar letras

---

**Vídeo:** [CREATE_VIDEO_VEO.md](./CREATE_VIDEO_VEO.md) · **Legenda:** [CREATE_CAPTION.md](./CREATE_CAPTION.md)
