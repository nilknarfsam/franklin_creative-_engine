# Cinematography Library — Narrative Engine (FCE)

Documentação de **linguagem cinematográfica clássica** — cinema de ficção, documentário e publicidade de autor. **Não é manual Veo.** É o vocabulário que o diretor (e o agente) usa antes de qualquer tradução técnica para IA.

---

## Planos (shot sizes)

| Plano | Abrev. | Enquadra | Uso dramático |
|-------|--------|----------|---------------|
| Plano geral extremo | EWS | Paisagem domina | Escala de Deus/natureza; solidão épica |
| Plano geral | WS | Corpo inteiro + ambiente | Contexto, jornada, isolamento no mundo |
| Plano médio | MS | Cintura para cima | Diálogo, ação cotidiana, rap narrativo |
| Plano médio fechado | MCU | Peito/cabeça | Emoção com contexto mínimo |
| Close-up | CU | Rosto | Intimidade, decisão, lágrima |
| Detalhe | ECU | Olho, mão, objeto | Símbolo, revelação |

**Regra FCE:** Ato emocional ↑ = plano tende a **fechar**. Clímax épico = **abrir** para respirar.

---

## Lentes (feel, não marca)

| Focal feel | Efeito psicológico | Quando usar |
|------------|-------------------|-------------|
| **Grande angular (14–24mm)** | Distorção leve, espaço, isolamento no vazio | Deserto, opressão urbana, EWS |
| **Normal (35–50mm)** | Olho humano, neutralidade ética | Documental, confiança |
| **Retrato (65–85mm)** | Flattering, separação fundo | Emoção, intimidade |
| **Tele (100mm+)** | Compressão, vigilância, distância | Comparação, voyeur, multidão |

**Profundidade de campo:**  
- **Rasa** — bokeh, isolamento emocional.  
- **Profunda** — personagem no mundo, consequências visíveis.

---

## Movimentos de câmera

| Movimento | Significado | Cuidado |
|-----------|-------------|---------|
| **Pan** | Revelar espaço, seguir ação horizontal | Não pan sem motivo |
| **Tilt** | Poder (tilt up), vulnerabilidade (tilt down) | |
| **Dolly in** | Intimidade crescente, revelação | |
| **Dolly out** | Abandono, revelar contexto trágico | |
| **Tracking** | Jornada, urgência | |
| **Crane up** | Triunfo, transcendência | |
| **Crane down** | Humildade, julgamento | |
| **Handheld** | Verdade crua, documental | Não exagerar shake |
| **Steadicam** | Fluidez onírica, destino | |
| **Static** | Peso, observação, Deus-eye sem mover | |

Ver também `library/veo3/camera-moves.md` para vocabulário em inglês em prompts.

---

## Composição

### Regra dos terços

Sujeito em interseção de linhas; horizonte no terço superior ou inferior — nunca centro morto salvo intenção.

### Espaço negativo

Área vazia **carrega emoção**: solidão (muito vazio), opressão (vazio atrás), esperança (vazio preenchido por luz depois).

### Leading lines

Estradas, corredores, raios de luz guiam o olho ao sujeito ou símbolo.

### Profundidade (foreground / mid / background)

Três planos criam **cinema** vs foto plana. Ex.: grade em FG, personagem mid, cidade BG.

### Enquadramento natural

Portas, janelas, galhos — moldura orgânica foca atenção.

---

## Luz

| Estilo | Características | Emoção |
|--------|-----------------|--------|
| **High key** | Poucas sombras | Alegria, festa |
| **Low key** | Sombras dominantes | Medo, arrependimento |
| **Chiaroscuro** | Contraste forte lateral | Drama moral |
| **Golden hour** | Warm, long shadows | Esperança, legado |
| **Blue hour** | Frio, contemplativo | Lamento, transição |
| **Practical lights** | Lâmpadas diegéticas | Realismo brasileiro |
| **Backlight** | Contorno, separação | Santo, épico |
| **Soft diffused** | Wrap, sem harsh | Paz |

**Motivação:** toda luz deve ter **fonte plausível** no mundo da cena (janela, sol, poste).

---

## Cor

| Abordagem | Uso |
|-----------|-----|
| **Desaturação** | Exaustão, passado, dor |
| **Monocromático azul** | Noite, solidão |
| **Warm lift** | Paz, resolução |
| **Split tone** | Shadow teal / highlight amber — épico moderno |
| **Paleta restrita** | 3 cores max por ato — coesão de álbum |

Documentar hex em Scene Builder para continuidade entre faixas do mesmo álbum.

---

## Blocking

Posicionamento de ator no espaço:

| Padrão | Significado |
|--------|-------------|
| Personagem **pequeno** no frame | Mundo/opressão maior |
| Personagem **centro** dominante | Agência, decisão |
| Personagem **de costas** | Jornada, mistério, oração |
| Distância entre dois | Relacional (traição = distância) |

---

## Ritmo (montagem — Filmora)

| Conceito | Aplicação |
|----------|-----------|
| **Tempo** | Duração absoluta dos planos |
| **Ritmo** | Padrão de aceleração/desaceleração |
| Verse musical | Cortes regulares no beat |
| Bridge | Long takes |
| Chorus | Cortes rápidos + wides |

Ritmo visual **antecipa** música no storyboard; sync na montagem.

---

## Quando usar cada técnica — guia rápido

| Narrativa precisa de… | Técnica |
|----------------------|---------|
| Empatia imediata | MCU, 50mm, soft light |
| Opressão sistêmica | Wide, 24mm, handheld, cold |
| Revelação divina | Crane up, backlight, golden |
| Intimidade de oração | CU static, low key soft |
| Metáfora de símbolo | ECU símbolo → cut rosto |
| Transição temporal | Match cut luz ou objeto |

---

## Vertical 9:16 — composição específica

| Regra | Motivo |
|-------|--------|
| Sujeito no **terço superior ou inferior** | Evitar corte de cabeça em UI mobile |
| Leading lines **verticais** | Arquitetura urbana BR |
| ECU funciona bem | Rosto preenche frame |
| EWS ainda precisa **ancora** no terço | Chão visível para escala |

---

## Template — Cinematography Block

```yaml
shot_size: MCU
lens_feel: 50mm
camera_move: slow_push_in
composition: "subject lower third, negative space above for sky promise"
lighting: golden_hour_side_key
color_palette: ["#C9A227", "#2D1B4E", "#1a1a2e"]
depth_of_field: shallow
blocking: "subject frame left, looking frame right toward light"
```

---

## Referências

- [03_scene_builder.md](./03_scene_builder.md)
- [04_emotion_engine.md](./04_emotion_engine.md)
- [07_prompt_composer.md](./07_prompt_composer.md)
- [library/veo3/camera-moves.md](../veo3/camera-moves.md)
