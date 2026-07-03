# Continuidade de Personagem — Veo 3 (FCE)

Guia para manter **coerência visual** entre cenas da mesma faixa ou campanha. Veo não garante continuidade automática — o FCE documenta e repete descritores.

---

## Princípio

> Mesma faixa = mesmo protagonista visual (salvo decisão criativa explícita).

Definir o personagem **uma vez** no `veo3-video-plan.md` e **repetir** a descrição canônica em cada prompt de cena, alterando apenas emoção, ação e enquadramento.

---

## Ficha de personagem (Character Sheet)

Preencher no plano de vídeo antes de gerar cenas:

```yaml
character_id: protagonist-track-01
name: "Protagonista — O Legado"
description: >
  Brazilian man, late 20s, brown skin, short dark hair,
  simple black t-shirt, no jewelry, authentic not model-like
wardrobe: casual dark clothing, no logos
distinctive: subtle scar on eyebrow (optional anchor)
avoid: suit and tie, stereotypical pastor look, crown, halo
```

### Campos obrigatórios

| Campo | Propósito |
|-------|-----------|
| `character_id` | Referência cruzada entre cenas |
| `description` | Bloco copiável para cada prompt |
| `wardrobe` | Consistência de roupa por ato |
| `avoid` | Prevenir deriva visual |

---

## Estratégias de continuidade

### 1. Descriptor block (recomendado)

Copiar o mesmo parágrafo de personagem no início de **cada** prompt:

```
The same young Brazilian man (late 20s, brown skin, short dark hair,
black t-shirt, authentic appearance) ...
```

### 2. Referência por cena anterior (sem imagem)

```
Same character as previous scene, now with expression of hope instead of anxiety
```

> Nota: Veo pode ignorar — descriptor block é mais confiável.

### 3. Reference image (futuro)

Quando a API suportar image-to-video ou reference frames:
- Salvar frame aprovado em `assets/video/veo3/ref-character.png`
- Documentar em plano — **não versionar PNG grande no git**

### 4. Silhueta / back-only

Para cenas difíceis de consistência:
```
Silhouette of a man from behind, no facial details visible
```
Útil em bridges e shots simbólicos.

---

## Múltiplos personagens

| Tipo de faixa | Personagens |
|---------------|-------------|
| Lamento pessoal (38, 42) | 1 protagonista |
| Traição (41) | Protagonista + figura distante (traidor = silhueta, nunca rosto claro) |
| Casamento Real (45) | Rei (silhueta majestosa) + noiva (figura em luz) — **simbolismo**, não literalismo |
| Nações (47) | Multidão genérica, diversidade, sem rosto dominante |

---

## Continuidade de ambiente

Além do personagem, fixar:

```yaml
environment_anchor:
  act_1: "urban apartment, rainy window, dawn"
  act_2: "open field, storm clearing, golden light"
  act_3: "elevated viewpoint over city at sunset"
```

Transições entre atos = mudança de ambiente permitida na **seção musical** correspondente (verse → chorus).

---

## Continuidade por álbum (Álbum 4)

Opcional — identidade visual unificada:

| Elemento | Constante no álbum |
|----------|-------------------|
| Protagonista | Pode variar por faixa OU manter "viajante" recorrente |
| Paleta | Ouro, roxo, preto teatral |
| Motivo recorrente | Trono como luz distante no horizonte (easter egg) |

Documentar decisão em `albums/album-04-o-trono-intocavel/concept.md` se adotar protagonista único.

---

## Checklist por cena

- [ ] Descriptor block idêntico ao plano
- [ ] Wardrobe consistente com cenas anteriores
- [ ] Mesma faixa etária e etnia
- [ ] Emoção evolui — aparência física não muda sem motivo
- [ ] `character_id` referenciado no `veo3-scene-template.md`

---

## Quando quebrar continuidade

- Flashback teológico (raro)
- Metáfora puramente simbólica (ex.: cervo no Sl 42 — usar animal, não humano)
- Multidão / povos (Sl 47)

Registrar quebra no plano: `continuity: broken — symbolic scene`.

---

## Referências

- `prompt-rules.md`
- `templates/veo3-video-plan-template.md`
- `docs/API_VIDEO_AUTOMATION.md`
