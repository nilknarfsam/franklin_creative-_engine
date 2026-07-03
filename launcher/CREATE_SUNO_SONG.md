# Launcher — Criar música para Suno

**Menu FCE.md:** Opção 13  
**Método:** VibeShell consolidado — [library/suno/](../library/suno/)

---

## Objetivo

Conduzir o usuário do tema à **Ficha Técnica + Letra Definitiva** prontas para colar no Suno — em qualquer chat (ChatGPT, Cursor, Codex, Claude, Gemini). **Não gera áudio.**

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md)
3. [library/suno/vibeshell-method.md](../library/suno/vibeshell-method.md) — método completo
4. [library/suno/suno-prompt-rules.md](../library/suno/suno-prompt-rules.md) — sintaxe
5. [library/suno/lyrics-structure.md](../library/suno/lyrics-structure.md) — dinâmica
6. [library/suno/bypass-and-safety.md](../library/suno/bypass-and-safety.md) — travas
7. [library/suno/mastering-landr.md](../library/suno/mastering-landr.md) — perfil LANDR
8. [WORKFLOW.md § WF2](../WORKFLOW.md#workflow-2--faixa-letra--áudio) — se for faixa de álbum FCE
9. [templates/suno-prompt-template.md](../templates/suno-prompt-template.md)

---

## Fluxo conversacional (passo a passo)

### Passo 1 — Natureza da música

Perguntar: **A música é bíblica/cristã ou livre/secular?**

- **Bíblica/cristã** → ativar **Verificação Teológica Estrita**
  - Letra biblicamente correta, fiel à mensagem original
  - Dúvida teológica → registrar **VibeCore Alert**, não resolver silenciosamente
- **Livre/secular** → trava teológica desativada; liberdade poética total no tema (mantendo regras estruturais)

### Passo 2 — Coletar parâmetros

Perguntar (uma pergunta ou bloco):

1. **Título**
2. **Tema / foco central**
3. **Passagem bíblica** (se houver)
4. **Vibe desejada** (gêneros + atmosfera — VibeCore se FCE)
5. **Duração aproximada** (ex.: 3:30–4:00)
6. **Terá ministração (Spoken Word)?** (Sim/Não + momento)

### Passo 3 — Gerar 🎛️ Ficha Técnica

```
🎛️ FICHA TÉCNICA
- Vibe Geral: [estilo macro]
- Estimativa de Tempo: [ex: 3:45 - 4:10]
- Sugestão de Ministração: [Sim/Não - motivo]
- Estilo Suno Prompt: [tags em inglês + Brazilian Portuguese vocals]
```

### Passo 4 — Gerar prompt Suno (inglês)

- Subgêneros técnicos + instrumentação + dinâmica + timbre vocal + andamento
- **Terminar sempre** com `Brazilian Portuguese vocals`
- **Nunca** citar bandas reais — descrever a **alma sonora** ([bypass-and-safety.md](../library/suno/bypass-and-safety.md))

### Passo 5 — Gerar 📝 Letra Definitiva

Formato obrigatório:

- 1ª linha: `[Language: Brazilian Portuguese]`
- Tags de seção em colchetes `[Intro]`, `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Outro]`, `[End]`
- Backing vocals / call-and-response em parênteses `(...)`
- Pausas com reticências `...`
- Intensidade com exclamações `!`
- Dinâmica intro íntima → refrão explosão (ver [lyrics-structure.md](../library/suno/lyrics-structure.md))

### Passo 6 — Aplicar bypass lírico (se necessário)

Se houver texto bíblico/domínio público muito conhecido → trocar palavras-chave literais por sinônimos equivalentes, preservando métrica e teologia. Em projeto bíblico, se o sentido mudar → VibeCore Alert.

### Passo 7 — Sugerir perfil LANDR

Conforme gênero macro ([mastering-landr.md](../library/suno/mastering-landr.md)):

- Metal Sinfônico / Pop de Arena → Aberto (Open)
- Worship / Acústico / Lofi → Quente (Warm)
- Trap Pesado / Nu Metal → Equilibrado (Balanced)

### Passo 8 — Checklist de revisão

Antes de o usuário colar no Suno (seção abaixo).

---

## Perguntas que a IA deve fazer ao usuário

1. Bíblica/cristã ou livre/secular?
2. Título?
3. Tema / foco central?
4. Passagem bíblica (se houver)?
5. Vibe desejada?
6. Duração aproximada?
7. Terá ministração?
8. É faixa de um álbum FCE existente ou música avulsa? (define onde salvar)

---

## Arquivos que a IA deve consultar

| Arquivo | Quando |
|---------|--------|
| `library/suno/*.md` | Sempre — método |
| `templates/suno-prompt-template.md` | Estrutura de output |
| `album.yaml` / `track.yaml` | Se faixa de álbum FCE |
| `lyrics.md` existente | Se refinar faixa (não alterar definitiva sem autorização) |
| `legal/vibecore-alerts.md` | Registrar dúvida teológica |
| `library/theology/` | Exegese (se existir) |

---

## Saídas esperadas

1. **🎛️ Ficha Técnica** — 4 campos
2. **Prompt Suno em inglês** — com `Brazilian Portuguese vocals`
3. **📝 Letra Definitiva** — tags, parênteses, `...`, `!`, `[End]`
4. **Bypass lírico aplicado** (se aplicável) + notas
5. **Perfil LANDR sugerido**
6. **Checklist de revisão**
7. **Path de salvamento sugerido** (se faixa FCE): `tracks/track-XX-{slug}/lyrics.md` + `suno/prompt.txt`

---

## Checklist de revisão (antes de colar no Suno)

- [ ] Natureza definida (bíblica → Verificação Teológica Estrita)
- [ ] 1ª linha: `[Language: Brazilian Portuguese]`
- [ ] Estrutura completa em colchetes até `[End]`
- [ ] Call-and-response em parênteses
- [ ] Pausas `...` e intensidade `!`
- [ ] Prompt de estilo termina em `Brazilian Portuguese vocals`
- [ ] Nenhum nome de banda real (alma sonora descrita)
- [ ] Bypass lírico em textos famosos (métrica + teologia preservadas)
- [ ] Refrão identificável e repetível
- [ ] Duração alvo coerente com tags de alongamento
- [ ] Fidelidade bíblica (se aplicável) — VibeCore Alert se dúvida
- [ ] Perfil LANDR sugerido

---

## O que a IA não deve fazer

- ❌ Gerar áudio ou fingir que gerou
- ❌ Citar nomes de bandas/artistas reais no prompt
- ❌ Distorcer teologia em projeto bíblico (usar VibeCore Alert)
- ❌ Alterar letras definitivas de faixas existentes sem autorização
- ❌ Mexer no Álbum 4 sem pedido explícito
- ❌ Misturar idiomas na letra (tags em inglês são exceção)
- ❌ Omitir a trava de sotaque
- ❌ Criar nova engine musical — usar VibeShell consolidado

---

**Método completo:** [library/suno/README.md](../library/suno/README.md) · **Workflow:** [WORKFLOW.md § WF2](../WORKFLOW.md#workflow-2--faixa-letra--áudio)
