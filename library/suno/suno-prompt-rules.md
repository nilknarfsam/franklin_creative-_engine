# Suno Prompt Rules — Sintaxe de Controle (VibeShell Fase 2)

Sintaxe rígida que controla fluxo da música e separação de canais de voz no Suno.

---

## 1. Colchetes `[ ]` — A voz do diretor

**NÃO É CANTADO.** Comandos estruturais e de produção.

| Uso | Exemplos |
|-----|----------|
| Estrutura | `[Intro]` · `[Verse 1]` · `[Pre-Chorus]` · `[Chorus]` · `[Bridge]` · `[Outro]` · `[End]` |
| Comando de banda | `[Heavy breakdown]` · `[Sudden silence]` · `[Bassline Focus]` · `[Long Instrumental Interlude]` |
| Estilo vocal | `[Clean Soft Vocal]` · `[Aggressive Male Vocal]` · `[Soaring Chorus]` · `[Powerful Theatrical Vocal]` |
| Idioma (trava) | `[Language: Brazilian Portuguese]` — sempre a **1ª linha** |

**Formato FCE combinado:** `[Section - production notes, Vocal type]`
Ex.: `[Chorus - Theatrical pop-rock explosion, huge melodic hook, Powerful Theatrical Vocal]`

---

## 2. Parênteses `( )` — A voz da multidão

**É CANTADO** por vozes secundárias.

| Uso | Exemplo |
|-----|---------|
| Backing vocals | `(Vem da mão do Criador!)` |
| Call-and-response | `Entrega! (Entrega!) Confia! (Confia!)` |
| Ecos / coros de estádio | `(Oh, oh, oh!)` |

---

## 3. Pontuação de fluxo

| Símbolo | Efeito |
|---------|--------|
| `...` (reticências) | Pausa dramática / sustentação de nota / respiração |
| `!` (exclamação) | Intensidade, volume, crueza emocional |

Ex.: `Não esquenta a cabeça... Deixa o tempo mostrar...`

---

## 4. Prompt de estilo (Suno "Style of Music")

**Estrutura recomendada (inglês técnico):**

```
[Subgêneros técnicos], [instrumentação característica], [dinâmica],
[timbre vocal + emoção], [andamento],
Brazilian Portuguese vocals
```

**Exemplo (Track 01 — O Legado):**
```
Acoustic guitar pluck, smooth trap beat, poetic rap flow,
theatrical pop-rock chorus, melodic hooks, massive dynamic shifts,
Brazilian Portuguese vocals
```

**Regras:**
- Sempre terminar com `Brazilian Portuguese vocals` (trava de sotaque)
- **Nunca** citar nomes de bandas reais — ver [bypass-and-safety.md](./bypass-and-safety.md)
- Descrever "alma sonora" em inglês, não marcas

---

## 5. Checklist de sintaxe

- [ ] 1ª linha da letra: `[Language: Brazilian Portuguese]`
- [ ] Estrutura completa em colchetes (Intro → End)
- [ ] Backing vocals / call-and-response em parênteses
- [ ] Pausas com `...` e intensidade com `!`
- [ ] Prompt de estilo termina em `Brazilian Portuguese vocals`
- [ ] Nenhum nome de banda real no prompt
- [ ] `[End]` presente no encerramento

---

**Ver também:** [vibeshell-method.md](./vibeshell-method.md) · [lyrics-structure.md](./lyrics-structure.md)
