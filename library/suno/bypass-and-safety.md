# Bypass & Safety — Sistemas de Segurança (VibeShell Fase 4)

Travas obrigatórias para evitar bloqueios de sotaque, plágio e copyright no Suno.

---

## 1. Trava de sotaque (anti-europeu)

O Suno tende a cantar PT em sotaque europeu sem instrução explícita.

| Onde | O quê |
|------|-------|
| 1ª linha da letra | `[Language: Brazilian Portuguese]` |
| Final do prompt de estilo | `Brazilian Portuguese vocals` |

**Sempre ambos.** Sem isso, o vocal sai com sotaque errado.

---

## 2. Trava de copyright lírico (bypass de sinônimos)

Textos de domínio público muito conhecidos (ex.: Bíblia, hinos clássicos) podem acionar **falso positivo de plágio**.

**Solução:** trocar palavras-chave literais por **sinônimos equivalentes**, preservando:

- **Métrica** de rima
- **Teologia** / mensagem original

| Original famoso | Bypass equivalente |
|-----------------|--------------------|
| "Refúgio e Fortaleza" | "Abrigo e Torre inabalável" |
| (termo literal muito citado) | (sinônimo com mesma métrica) |

**Regra FCE:** o bypass **nunca** distorce a teologia. Em projeto bíblico, se o sinônimo alterar o sentido → registrar **VibeCore Alert** em vez de aplicar silenciosamente.

---

## 3. Trava de copyright instrumental (A Regra da Alma)

**Nunca** citar nomes de bandas ou artistas reais no prompt de estilo.

**Solução:** descrever a **alma sonora** em inglês técnico — textura, época, instrumentos.

| Em vez de (proibido) | Descrever a alma (correto) |
|----------------------|----------------------------|
| Coldplay | `Atmospheric Arena Rock, British pop-rock, cinematic strings` |
| Imagine Dragons | `Anthemic stadium pop-rock, big drums, electronic pulse` |
| (qualquer banda) | subgênero + instrumentação + atmosfera |

---

## Checklist de segurança

- [ ] `[Language: Brazilian Portuguese]` na 1ª linha
- [ ] `Brazilian Portuguese vocals` no fim do prompt de estilo
- [ ] Nenhum nome de banda/artista real
- [ ] Bypass lírico aplicado a textos famosos, se necessário
- [ ] Teologia preservada (projeto bíblico) — VibeCore Alert se dúvida
- [ ] Alma sonora descrita, não copiada

---

**Ver também:** [suno-prompt-rules.md](./suno-prompt-rules.md) · [vibeshell-method.md](./vibeshell-method.md)
