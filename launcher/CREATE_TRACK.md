# Launcher — Criar nova faixa

**Menu FCE.md:** Opção 10

---

## Objetivo

Orientar a IA a **iniciar uma nova faixa** no FCE — estrutura de pastas, metadados, conceito e letra rascunho — sem pular workflows futuros (CDS, Narrative, Suno).

---

## Ordem de leitura obrigatória

1. [FCE.md](../FCE.md)
2. [AGENTS.md](../AGENTS.md)
3. [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) — módulo faixa
4. [WORKFLOW.md § WF2](../WORKFLOW.md#workflow-2--faixa-letra--áudio)
5. [templates/track-template.md](../templates/track-template.md)
6. `albums/{album}/album.yaml` — track_count, scripture_range
7. `albums/{album}/concept.md` — arco do álbum

---

## Perguntas que a IA deve fazer ao usuário

1. **Qual álbum?** (slug · número)
2. **Número e título da faixa?**
3. **Salmo ou passagem base?**
4. **Vibe Geral?** (VibeCore — ver VISION.md)
5. **Ministração?** (sim/não + momento)
6. **Status inicial?** (`concept` · `lyrics_draft`)
7. **Autorização humana?** — confirmar que faixa não existe ainda no dossiê

---

## Arquivos que a IA deve consultar

| Arquivo | Função |
|---------|--------|
| `album.yaml` | Próximo track number |
| `legal/dossie-direitos-autorais.md` | Não duplicar faixa |
| `concept.md` (álbum) | Posição no arco |
| Faixas vizinhas | Coerência vibe |
| `templates/track-template.md` | Estrutura |
| `library/theology/` | Notas exegéticas se existir |

---

## Saídas esperadas

1. **Plano da faixa** — conceito 1 parágrafo, vibe, Salmo, ministração
2. **Lista de arquivos a criar** — paths conforme PROJECT_STRUCTURE
3. **`track.yaml`** — schema preenchido, `status: concept` ou `lyrics_draft`
4. **`concept.md`** — resumo criação
5. **Stub `lyrics.md`** — se rascunho autorizado (tags Suno vazias OK)
6. **Checklist próximos passos** — letra → ficha → Suno → CDS → identity → narrative
7. **Entrada CHANGELOG** — se alteração estrutural (quando usuário solicitar)

**Criar pasta:** `albums/album-XX-{slug}/tracks/track-NN-{slug}/`

---

## Checklist de qualidade

- [ ] Slug conforme PROJECT_STRUCTURE (`track-NN-kebab`)
- [ ] Salmo/passagem declarada em YAML
- [ ] Vibe Geral documentada
- [ ] Links para álbum e campanha stub
- [ ] Não conflita com dossiê legal existente
- [ ] VibeCore Alert se dúvida teológica
- [ ] Não marcar `lyrics_final` sem aprovação humana

---

## O que a IA não deve fazer

- ❌ Inventar faixa já no dossiê
- ❌ Marcar letra como definitiva sem revisão
- ❌ Criar álbum inteiro quando pedido foi uma faixa
- ❌ Pular templates e inventar estrutura de pastas
- ❌ Gerar áudio Suno automaticamente
- ❌ Alterar letras definitivas de outras faixas
- ❌ Criar nova engine Track

---

**Próximos launchers:** CDS via [WORKFLOW.md § CDS](../WORKFLOW.md#creative-direction-pipeline--estratégia-de-campanha-obrigatório) · Vídeo via [CREATE_VIDEO_VEO.md](./CREATE_VIDEO_VEO.md)
