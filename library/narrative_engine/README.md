# Narrative Engine — Franklin Creative Engine

**Framework cinematográfico permanente.** Ensina qualquer agente de IA a pensar como **Diretor de Cinema** antes de qualquer prompt Veo.

| Regra | Detalhe |
|-------|---------|
| Gera vídeo? | **Não** |
| Obrigatório antes de Veo? | **Sim** |
| Escopo | Todos os álbuns, todas as faixas |
| Output | Cenas documentadas + Prompt Composer + Director Commentary |

---

## Ordem de leitura

| # | Módulo | Função |
|---|--------|--------|
| 01 | [hook_engine.md](./01_hook_engine.md) | Primeiros 3 segundos |
| 02 | [character_engine.md](./02_character_engine.md) | Construção de pessoas |
| 03 | [scene_builder.md](./03_scene_builder.md) | Unidade de cena |
| 04 | [emotion_engine.md](./04_emotion_engine.md) | Emoção → fotografia |
| 05 | [symbol_library.md](./05_symbol_library.md) | Metáforas bíblicas |
| 06 | [cinematography_library.md](./06_cinematography_library.md) | Linguagem de cinema |
| 07 | [prompt_composer.md](./07_prompt_composer.md) | Montagem do prompt |
| 08 | [director_commentary.md](./08_director_commentary.md) | Documentação do porquê |

---

## Pipeline resumido

```
Hook → Character → Scene(s) → Emotion → Symbol → Cinematography → Prompt Composer → veo3/prompt-rules → Veo
                                      ↘ Director Commentary (paralelo, obrigatório)
```

---

## Paths no repositório (por faixa)

```
tracks/track-XX/video/narrative/
├── hook.md
├── character-{slug}.md
├── scenes/scene-{NN}.md
├── director-commentary.md
└── narrative-manifest.yaml    # opcional futuro
```

---

## Links externos

- [WORKFLOW.md § Narrative Pipeline](../../WORKFLOW.md)
- [AGENTS.md](../../AGENTS.md)
- [library/veo3/](../veo3/) — camada de execução Veo
- [docs/API_VIDEO_AUTOMATION.md](../../docs/API_VIDEO_AUTOMATION.md)

**Versão:** 1.0.0 — Sprint 4
