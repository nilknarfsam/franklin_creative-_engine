# Launcher — Criar prompt para Veo

**Menu FCE.md:** Opção 7  
**Pré-requisito:** Narrative Pipeline completo + CDS G1

---

## Objetivo

Orientar a IA a **validar, ordenar e documentar prompts Veo** — nunca reescrever manualmente — com ordem de geração, regras `no text`, 9:16 first e instruções de salvamento.

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md) — Prompt Composer obrigatório
3. [WORKFLOW.md § Narrative Pipeline](../WORKFLOW.md#narrative-pipeline--direção-cinematográfica-obrigatório)
4. [WORKFLOW.md § WF9](../WORKFLOW.md#workflow-9--geração-de-vídeo-com-veo-api)
5. [library/narrative_engine/07_prompt_composer.md](../library/narrative_engine/07_prompt_composer.md)
6. [library/veo3/prompt-rules.md](../library/veo3/prompt-rules.md)
7. `video/narrative/` — **todos** os arquivos
8. `video/narrative/prompt-composition.md`
9. `video/veo3-prompts.md`

---

## Perguntas que a IA deve fazer ao usuário

1. **Qual álbum e faixa?**
2. **Narrative Pipeline completo?** Se não → executar WF Narrative antes
3. **Quantas cenas?** (ver `scenes.md` / `narrative-manifest.yaml`)
4. **Geração manual ou script futuro?** (hoje: manual AI Studio / Vertex)
5. **Aspect ratio?** (default: **9:16** — confirmar 16:9 só se clip YT separado)
6. **Quais cenas prioritárias?** (P0 reel: hook + clímax)

---

## Arquivos que a IA deve consultar

| Arquivo | Função |
|---------|--------|
| `video/narrative/hook.md` | Hook 3s |
| `video/narrative/character.md` | Continuidade personagem |
| `video/narrative/scenes.md` | 17 campos por cena |
| `video/narrative/prompt-composition.md` | Prompts compostos + linhagem |
| `video/narrative/director-commentary.md` | Porquê de cada cena |
| `video/veo3-prompts.md` | Export consolidado |
| `video/veo3-video-plan.md` | Plano operacional |
| `library/veo3/character-continuity.md` | Consistência visual |
| `identity/track_identity.md` | Paleta e Do Not Use |

---

## Saídas esperadas

1. **Checklist Narrative** — hook, character, cenas, commentary OK
2. **Ordem de geração das cenas** — sequência recomendada (ato I → III)
3. **Prompts em inglês** — copiados de `prompt-composition.md` / Prompt Composer — **não reescritos**
4. **Parâmetros por take** — 9:16 · 5–8s · `no text, no watermark`
5. **Instruções de salvamento:**

   ```
   tracks/track-XX-{slug}/assets/video/veo3/scene-NN-{slug}.mp4
   ```

   Registrar take escolhido em `veo3-video-plan.md` ou `scenes.md`

6. **Log de geração** — cena, data, take, notas (sem API keys)
7. **Alertas** — cenas pendentes, continuidade, VibeCore

---

## Checklist de qualidade

- [ ] Prompts via Prompt Composer — não manual
- [ ] Cada cena: personagem, ambiente, emoção, câmera, iluminação, objetivo dramático
- [ ] `no text` em todos os prompts
- [ ] 9:16 default para social
- [ ] Director commentary existe
- [ ] Character continuity validada
- [ ] Nenhum secret/API key no output
- [ ] Do Not Use da identity respeitado nos prompts

---

## O que a IA não deve fazer

- ❌ **Criar texto legível dentro do vídeo** nos prompts
- ❌ Reescrever prompts sem Prompt Composer
- ❌ Pular Narrative Engine
- ❌ Hardcodar API keys ou pedir commit de `.env`
- ❌ Gerar MP4 (humano/API executa)
- ❌ Prompts em português para Veo (inglês)
- ❌ Criar nova Video Engine
- ❌ Alterar letras

---

**Segurança:** [docs/API_VIDEO_AUTOMATION.md](../docs/API_VIDEO_AUTOMATION.md) · [scripts/video/.env.example](../scripts/video/.env.example)
