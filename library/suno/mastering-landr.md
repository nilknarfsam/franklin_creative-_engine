# Mastering LANDR — Pós-Produção (VibeShell Fase 6)

Perfis de masterização LANDR aplicados após exportar o áudio gerado no Suno.

---

## Tabela de perfis

| Gênero / Estilo macro | Perfil LANDR | Intensidade sugerida |
|-----------------------|--------------|----------------------|
| Metal Sinfônico / Pop de Arena / Épico | **Aberto (Open)** | Alta ou Média |
| Worship / Acústico / Lofi | **Quente (Warm)** | Média |
| Trap Pesado / Industrial / Nu Metal | **Equilibrado (Balanced)** | Alta |

---

## Como escolher

1. Identificar o **gênero macro** do arranjo (não subgênero exato)
2. Aplicar o **perfil** correspondente
3. Ajustar **intensidade** conforme a dinâmica:
   - Faixas com grande contraste íntimo↔arena → intensidade Média (preserva dinâmica)
   - Faixas consistentemente densas → intensidade Alta

---

## Aplicação por vibe do Álbum 4 (referência)

| Faixa exemplo | Vibe | Perfil sugerido |
|---------------|------|-----------------|
| O Legado (Trap Acústico & Pop Teatral) | Worship/arena híbrido | Warm ou Open · Média |
| O Peso do Clamor (Dark Trap) | Trap pesado | Balanced · Alta |
| O Refúgio Inabalável (Arena Rock) | Pop de arena | Open · Alta ou Média |

> Referência — não substitui julgamento auditivo. Documentar escolha em `suno/iterations/notes.md`.

---

## Fluxo de pós-produção

```
Suno export (WAV/MP3)
        ↓
   LANDR (perfil + intensidade)
        ↓
   Master → assets/audio/track-XX-{slug}-master.wav
        ↓
   (Filmora usa master para vídeo)
```

---

**Ver também:** [vibeshell-method.md](./vibeshell-method.md) · [WORKFLOW.md § WF2 Fase C](../../WORKFLOW.md#workflow-2--faixa-letra--áudio)
