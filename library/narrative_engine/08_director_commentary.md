# Director Commentary — Narrative Engine (FCE)

Todo vídeo do Franklin Creative Engine **deve** possuir um Comentário do Diretor — documentação permanente que explica **por que** cada decisão existe. Não é marketing. É **memória institucional** para humanos, agentes futuros e auditoria teológica-artística.

**Path padrão:** `tracks/track-XX/video/narrative/director-commentary.md`

---

## Propósito

| Para quem | Valor |
|-----------|-------|
| **Agente de IA** | Retomar contexto sem re-alucinar |
| **Editor (Filmora)** | Entender intenção além do storyboard |
| **Ministério** | Validar fidelidade bíblica |
| **Futuros álbuns** | Replicar padrão de excelência |

---

## Estrutura do documento

### 1. Visão do diretor (vídeo inteiro)

Responder em prosa:

- Qual é a **tese** deste vídeo em uma frase?
- Qual **emoção** o espectador deve levar ao sair?
- Qual **versículo** ancora tudo (mesmo que legenda só no final)?
- Por que **9:16** e este runtime?
- Como este vídeo serve a **faixa** sem ser literal demais?

### 2. Hook — por que estes 3 segundos?

| Pergunta | Resposta |
|----------|----------|
| Qual tipo de hook? | cold_open / question / conflict / silence / contrast / impact_image |
| Por que este e não outro? | |
| O que o espectador sente em 1 s? | |
| O que promete sem entregar ainda? | |

Ver `01_hook_engine.md`.

### 3. Personagem — por que esta pessoa?

| Pergunta | Resposta |
|----------|----------|
| Quem é? | Nome + essência |
| Por que o público se identifica? | |
| Qual medo e qual sonho movem o arco? | |
| Como a câmera o trata no início vs fim? | |

Ver `02_character_engine.md`.

### 4. Comentário por cena

**Para cada cena**, responder todas:

| # | Pergunta |
|---|----------|
| 1 | **Por que esta cena existe?** (objetivo dramático) |
| 2 | **Qual versículo ela representa?** (ref + uma linha de conexão) |
| 3 | **Qual emoção ela transmite?** (primária + arco entrada→saída) |
| 4 | **Qual símbolo está sendo utilizado?** (e por quê) |
| 5 | **Por que a câmera foi escolhida?** (plano + movimento) |
| 6 | **Por que esta iluminação?** (motivação + emoção) |
| 7 | **O que o espectador deve entender sem legenda?** | |
| 8 | **O que só o Filmora adiciona?** (texto, versículo, música) | |

---

## Template — Director Commentary

```markdown
# Director Commentary — {Título do vídeo}

**Track:** {track_id} — {Título da faixa}
**Referência:** {Livro cap:v}
**Runtime:** {45–60s}
**Formato:** 9:16
**Data:** YYYY-MM-DD
**Direção:** [nome ou FCE Creative]

---

## Visão

[PREENCHER — 2–4 parágrafos]

---

## Hook (0:00–0:03)

| Campo | Conteúdo |
|-------|----------|
| Tipo | |
| Justificativa | |
| Promessa visual | |

---

## Personagem

| Campo | Conteúdo |
|-------|----------|
| character_id | |
| Por que ele/ela | |
| Arco | |

---

## Cena 01 — {Título}

| Pergunta | Resposta |
|----------|----------|
| Por que existe? | |
| Versículo | |
| Emoção | |
| Símbolo | |
| Câmera | |
| Iluminação | |
| Sem legenda | |
| Filmora | |

---

## Cena 02 — {Título}

[REPETIR]

---

## Notas de montagem

[PREENCHER — decisões que só fazem sentido no edit]

---

## Pendências e iterações

| Data | Nota |
|------|------|
| | |

---

## Aprovações

| Papel | Status | Data |
|-------|--------|------|
| Direção criativa | | |
| Teologia / VibeCore | | |
| Produção | | |
```

---

## Critérios de qualidade

Um commentary **bom**:

- Explica **escolhas rejeitadas** ("quase usei cold open, mas silêncio servia melhor ao Sl 37:7")
- Cita **Escritura** com referência verificável
- Não repete o prompt Veo — explica **intenção**
- É legível por quem **não** viu o storyboard

Um commentary **ruim**:

- "Cena bonita para engajar"
- Lista só equipamento
- Ignora versículo

---

## Relação com outros arquivos

| Arquivo | Relação |
|---------|---------|
| `veo3-video-plan.md` | Plano operacional |
| `storyboard.md` | Timing visual |
| `veo3-prompts.md` | Output técnico Veo |
| `director-commentary.md` | **Porquê** de tudo |
| `filmora/edit-notes.md` | **Como** montar |

**Ordem de escrita recomendada:**

1. Narrative pipeline (character + scenes)
2. Director commentary (rascunho por cena)
3. Prompt Composer
4. Revisar commentary após prompts
5. Filmora edit notes

---

## Teologia e VibeCore

Se uma cena usa metáfora não-literal:

- Documentar **intenção teológica**
- Flag em `legal/vibecore-alerts.md` se houver risco de deriva

O commentary é onde o diretor **justifica** metáfora vs literalismo.

---

## Referências

- [01_hook_engine.md](./01_hook_engine.md) … [07_prompt_composer.md](./07_prompt_composer.md)
- [WORKFLOW.md § Narrative Pipeline](../../WORKFLOW.md)
