# Suno Music System (VibeShell) — Franklin Creative Engine

**Sistema oficial de produção musical do FCE.** Consolida o método **VibeShell** (manuais V1 → V3.0) em um padrão único, limpo e reutilizável para gerar música com Suno.

| Regra | Detalhe |
|-------|---------|
| Gera áudio? | **Não** — orienta o humano/IA a compor prompt + letra para colar no Suno |
| Escopo | Bíblico/cristão (Verificação Teológica Estrita) **e** livre/secular |
| Idioma da letra | Português Brasileiro |
| Idioma do prompt Suno | Inglês técnico + `Brazilian Portuguese vocals` |
| Base canônica | **VibeShell V3.0** (mais completo — adiciona Escopo Temático) |

---

## Propósito

O VibeShell responde à pergunta que vem **depois** do conceito e **antes** do áudio:

> *Como transformar um tema (Salmo, narrativa ou tema livre) em um prompt Suno preciso + letra definitiva que soe teatral, humana e sem bloqueios de plataforma?*

Complementa o pipeline existente — não substitui `lyrics.md`, `technical-sheet.md` ou o CDS.

---

## Arquivos do módulo

| Arquivo | Função |
|---------|--------|
| [vibeshell-method.md](./vibeshell-method.md) | Método completo — 6 fases (V3.0 consolidado) |
| [suno-prompt-rules.md](./suno-prompt-rules.md) | Sintaxe de controle: colchetes, parênteses, pontuação, prompt de estilo |
| [lyrics-structure.md](./lyrics-structure.md) | Estrutura de letra, dinâmica, humanização, Super Edição |
| [bypass-and-safety.md](./bypass-and-safety.md) | Travas de sotaque, copyright lírico e "Regra da Alma" |
| [mastering-landr.md](./mastering-landr.md) | Perfis de masterização LANDR por gênero |

**Launcher operacional:** [launcher/CREATE_SUNO_SONG.md](../../launcher/CREATE_SUNO_SONG.md)

---

## As 6 fases VibeShell (resumo)

1. **Escopo e planejamento** — bíblico vs livre; roadmap (título, tema, vibe, tempo, ministração)
2. **Núcleo do prompt** — sintaxe de controle (`[ ]`, `( )`, `...`, `!`)
3. **Humanização, tempo e dinâmica** — Super Edição, alongamento, quebra de fadiga, ministração
4. **Segurança e bypass** — anti-sotaque, bypass lírico, Regra da Alma
5. **Padrão de saída** — 🎛️ Ficha Técnica + 📝 Letra Definitiva
6. **Pós-produção** — perfis LANDR

---

## Posição na arquitetura FCE

```
Conceito (letra + tema)
        ↓
   VibeShell (este módulo)  ← prompt Suno + letra definitiva
        ↓
   Suno (humano gera áudio)
        ↓
   Master (LANDR) → assets/audio/
```

**Relação com outros módulos:**

| Módulo | Relação |
|--------|---------|
| WORKFLOW § WF2 | VibeShell alimenta Fase B (letra) e Fase C (Suno prompt) |
| CDS | Fornece tom/mensagem-chave — VibeShell executa a letra |
| `templates/suno-prompt-template.md` | Template de output por faixa |
| `library/suno/vibes/` | Vibes curadas (futuro — placeholder no PROJECT_STRUCTURE) |

---

## Fonte histórica

Consolidado dos manuais na raiz (tratados como **fonte histórica**, não canônica):

- `MANUAL ... VIBESHELL (V3.0).md` — **base principal**
- `MANUAL ... VIBESHELL (V2.0).md` / `Manual ... V2.0.md` — roadmap detalhado + super prompt
- `MANUAL ... VIBESHELL.md` (V1) — super prompt copy & paste

Diferença-chave V3.0: introduz a **Fase 1 — Escopo Temático** com a trava de Verificação Teológica Estrita para projetos bíblicos.

---

**Versão:** 1.0.0 — VibeShell consolidado · 2026-07-03
