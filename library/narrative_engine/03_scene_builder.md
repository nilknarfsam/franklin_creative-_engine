# Scene Builder — Narrative Engine (FCE)

O Scene Builder é a **unidade atômica da narrativa cinematográfica** no FCE. Uma cena não é um clip Veo — é um **beat dramático** com intenção teológica, emocional e visual documentada.

**Regra:** nenhuma cena existe sem os campos obrigatórios abaixo. O Prompt Final **não** é escrito à mão — é produzido por `07_prompt_composer.md`.

---

## Anatomia de uma cena FCE

```
Cena = Objetivo dramático + Emoção + Escritura + Símbolo + Mundo + Fotografia + Som + Transição + Mensagem
```

---

## Campos obrigatórios

| # | Campo | Responsável | Descrição |
|---|-------|-------------|-----------|
| 1 | **Objetivo dramático** | Diretor | Por que esta cena existe no arco |
| 2 | **Emoção** | Emotion Engine | Estado dominante — ver `04_emotion_engine.md` |
| 3 | **Versículo relacionado** | Teologia | Ref bíblica (livro cap:v), não só letra da faixa |
| 4 | **Símbolo** | Symbol Library | Metáfora visual — `05_symbol_library.md` |
| 5 | **Personagem** | Character Engine | Quem age; `character_id` |
| 6 | **Ambiente** | Diretor | Lugar, cultura, época, profundidade |
| 7 | **Clima** | Diretor | Chuva, seco, névoa, vento |
| 8 | **Hora do dia** | Diretor | Dawn, blue hour, noon, dusk, night |
| 9 | **Movimento de câmera** | Cinematography | Dolly, crane, handheld… |
| 10 | **Plano** | Cinematography | EWS, WS, MS, CU, ECU |
| 11 | **Lente** | Cinematography | Wide 24mm, normal 50mm, tele 85mm+ (feel) |
| 12 | **Paleta de cores** | Cinematography | Hex ou descritores (warm/cold) |
| 13 | **Iluminação** | Cinematography | Key, fill, backlight, motivo |
| 14 | **Som ambiente** | Diretor | Diegético: trânsito, vento, silêncio |
| 15 | **Transição** | Editor | Para cena seguinte: cut, dissolve, match |
| 16 | **Mensagem** | Diretor | O que o espectador deve **entender** |
| 17 | **Prompt Final** | Prompt Composer | **Gerado** — nunca manual |

---

## Estrutura em atos (qualquer duração)

| Ato | Função | % típico reel 60s |
|-----|--------|-------------------|
| **I — Setup** | Mundo, tensão, hook | 25% |
| **II — Confronto** | Escolha, luta, queda | 35% |
| **III — Resolução** | Revelação, paz, envio | 40% |

Número de cenas: flexível. Reels curtos: 4–6 cenas. Clip longo: 8–12.

---

## Template reutilizável — Scene Document

Salvar em: `tracks/track-XX/video/narrative/scenes/scene-{NN}.md`

```yaml
---
scene_id: scene-{NN}
track_id: track-{NN}
character_id: char-{slug}
emotion_id: hope          # ver 04_emotion_engine.md
symbol_id: seed           # ver 05_symbol_library.md
duration_target_seconds: 7
aspect_ratio: "9:16"
---

# Cena {NN} — {Título curto}

## Objetivo dramático

[PREENCHER — uma frase: o que muda após esta cena]

## Emoção

| Campo | Valor |
|-------|-------|
| Primária | |
| Secundária | |
| Arco | entrada → saída |

## Escritura

| Campo | Valor |
|-------|-------|
| Referência | |
| Texto (NVI/ARA) | |
| Conexão com letra da faixa | |

## Símbolo

| Campo | Valor |
|-------|-------|
| Símbolo | |
| Significado nesta cena | |
| Como aparece visualmente | |

## Personagem

| Campo | Valor |
|-------|-------|
| character_id | |
| Ação | |
| Gesto-chave | |

## Mundo

| Campo | Valor |
|-------|-------|
| Ambiente | |
| Clima | |
| Hora do dia | |

## Fotografia

| Campo | Valor |
|-------|-------|
| Movimento de câmera | |
| Plano | |
| Lente (feel) | |
| Composição | ex.: rule of thirds, negative space left |
| Paleta | |
| Iluminação | |

## Som

| Campo | Valor |
|-------|-------|
| Ambiente diegético | |
| Sync musical (seção da faixa) | |
| Silêncio intencional? | sim/não |

## Edição

| Campo | Valor |
|-------|-------|
| Transição para próxima | |
| Notas Filmora | legendas, texto — **não Veo** |

## Mensagem

[PREENCHER — uma frase para o espectador]

## Prompt Final

> **Gerado por `07_prompt_composer.md`. Não editar manualmente sem atualizar campos acima.**

```
[COMPOR — output do Prompt Composer]
```

## Director commentary

Ver `08_director_commentary.md` — seção desta cena.
```

---

## Relação cena × música

| Seção musical | Tipo de cena típica | Energia |
|---------------|---------------------|---------|
| Intro | Setup, hook, silêncio | Baixa |
| Verse | Narrativa, conflito | Média |
| Pre-chorus | Tensão, contraste | Crescendo |
| Chorus | Clímax visual, símbolo épico | Alta |
| Bridge | Pausa, revelação | Vale |
| Outro | Resolução, envio | Alta → paz |

Música **informa** ritmo de corte no Filmora; Veo gera **momentos** isolados.

---

## Validação de cena

- [ ] Objetivo dramático único e claro
- [ ] Versículo citado corretamente
- [ ] Símbolo ligado à Escritura (não decorativo)
- [ ] Personagem com ficha em `02_character_engine.md`
- [ ] Fotografia preenchida (plano + lente + luz)
- [ ] Prompt Final via Composer
- [ ] Director commentary esboçado

---

## Anti-padrões

| Evitar | Por quê |
|--------|---------|
| Cena que só "ilustra" versículo literalmente | Cinema é metáfora |
| Duas emoções dominantes iguais em sequência | Monotonia |
| Símbolo sem setup | Confusão |
| Prompt escrito sem campos | Deriva Veo, perda de direção |

---

## Referências

- [01_hook_engine.md](./01_hook_engine.md)
- [04_emotion_engine.md](./04_emotion_engine.md)
- [05_symbol_library.md](./05_symbol_library.md)
- [06_cinematography_library.md](./06_cinematography_library.md)
- [07_prompt_composer.md](./07_prompt_composer.md)
