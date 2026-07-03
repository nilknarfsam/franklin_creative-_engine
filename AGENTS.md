# Agentes de IA — Franklin Creative Engine

Instruções operacionais para **ChatGPT, Cursor, Codex, Claude** e demais agentes que trabalham neste repositório.

Leia este arquivo **por completo** antes de gerar, editar ou reorganizar conteúdo.

---

## Identidade do projeto

| Campo | Valor |
|-------|-------|
| Nome | Franklin Creative Engine |
| Sigla | FCE |
| Domínio | Produção criativa cristã com IA |
| Idioma de conteúdo | Português Brasileiro (PT-BR) |
| Idioma Suno prompts | Inglês + `Brazilian Portuguese vocals` |
| Estilo musical | VibeCore — ver [VISION.md](./VISION.md) |

---

## Ordem de leitura obrigatória

1. **AGENTS.md** (este arquivo)
2. **PROJECT_STRUCTURE.md** — paths e schemas
3. **WORKFLOW.md** — pipeline da tarefa solicitada
4. **album.yaml** / **track.yaml** do contexto específico
5. **legal/dossie-direitos-autorais.md** se trabalhar com letras existentes

---

## Regras absolutas

### ✅ Sempre faça

- Consulte arquivos existentes antes de inventar conteúdo
- Use slugs e paths definidos em PROJECT_STRUCTURE.md
- Mantenha tags Suno no formato `[Section - notes, Vocal type]`
- Documente pendências teológicas como **VibeCore Alerts**
- Escreva markdown limpo, sem HTML desnecessário
- Registre mudanças significativas em CHANGELOG.md quando solicitado
- Preserve fidelidade bíblica — adaptação poética, não distorção
- Indique `status` em YAML ao criar ou atualizar metadados

### ❌ Nunca faça

- Inventar faixas, álbuns ou letras não documentadas
- Alterar letras marcadas como **definitivas** sem flag `needs_review`
- Remover ou ignorar VibeCore Alerts existentes
- Criar conteúdo genérico de motivação sem ancoragem bíblica
- Misturar idiomas na letra (exceto tags Suno em inglês)
- Commitar secrets, API keys ou `.env`
- Expor ou repetir API keys fornecidas pelo usuário no chat
- Hardcodar credenciais em scripts de vídeo (`scripts/video/`)
- Gerar prompts Veo com texto legível no vídeo (salvo pedido explícito)
- Planejar vídeo social em 16:9 quando o entregável primário é Reel/TikTok/Shorts
- Entregar prompt de cena sem os 6 elementos (personagem, ambiente, emoção, câmera, iluminação, objetivo dramático)
- Reorganizar pastas sem atualizar PROJECT_STRUCTURE.md
- Substituir teologia bíblica por paráfrases de outros livros (ex.: Eclesiastes no Salmo 39)

---

## Contexto do álbum ativo

**Álbum 4 — O Trono Intocável**

| # | Título | Salmo | Vibe resumida |
|---|--------|-------|---------------|
| 01 | O Legado | 37 | Trap Acústico & Pop Teatral |
| 02 | O Peso do Clamor | 38 | Dark Trap & Emo-Rap Teatral |
| 03 | O Sopro do Tempo | 39 | Rap Poético & Ambient Acústico |
| 04 | O Lago Horrível e a Rocha | 40 | Crossover Rap-Rock & Pop de Arena |
| 05 | O Cálice da Traição | 41 | Trap-Rock Narrativo |
| 06 | A Sede da Minha Alma | 42 | Power Ballad Teatral & Trap Orquestral |
| 07 | Luz e Verdade | 43 | Cinematic Trap & Theatrical Anthem |
| 08 | O Clamor da História | 44 | Cinematic Trap-Rock / Marcha Épica |
| 09 | O Cântico do Casamento Real | 45 | Pop-Rock Festivo & Brass |
| 10 | O Refúgio Inabalável | 46 | Epic Arena Rock & Hip-Hop Crossover |
| 11 | O Aplauso das Nações | 47 | Trap-Pop Festivo |
| 12 | A Cidade do Grande Rei | 48 | Symphonic Trap-Rock / Grand Finale |

**Pendência ativa:** Track 03 — estrofe com referência a Eclesiastes; trocar por imagem do Salmo 39 ("sombra e ilusão").

---

## Papéis por ferramenta

### ChatGPT

**Melhor para:**
- Brainstorm de conceito e arco narrativo
- Exegese e estudo bíblico
- Rascunho de letras (depois formatar para Suno)
- Copy de posts, legendas, roteiros de ministração
- Briefs para Veo 3 e Canva em linguagem natural

**Prompt de sistema sugerido:**

```
Você opera no Franklin Creative Engine (FCE).
Leia AGENTS.md e VISION.md. Produza em PT-BR.
Estilo: Pop Teatral / Trap Crossover. Tags Suno em inglês.
Não invente faixas fora do Álbum 4 sem autorização.
```

### Cursor / Codex

**Melhor para:**
- Criar e manter estrutura de pastas e templates
- Split/merge de dossiês em arquivos modulares
- Refatoração de letras com diff rastreável
- Automações, scripts, regras `.cursor/rules`
- Validação de schemas YAML

**Ao editar letras:** preserve tags `[Section]` e indicações vocais.

### Suno (via humano ou prompt exportado)

**Input esperado:** `lyrics.md` + `suno/prompt.txt`

**Regras:**
- Letra com tags de seção na linha ou bloco
- Prompt descreve instrumentação, dinâmica, vocal style
- Sempre incluir `Brazilian Portuguese vocals`
- Documentar iterações em `suno/iterations/notes.md`

### Veo 3 / Veo API

**Input esperado:** `video/veo3-brief.md`, `video/veo3-video-plan.md`, `video/scenes/scene-NN.md`

**Diretrizes FCE:**
- Estética cinematográfica teatral
- Simbolismo bíblico contemporâneo (não kitsch religioso)
- Coerência com vibe da faixa (dark vs festivo vs arena)
- Cenas de 5–8s pensadas para edição Filmora
- **Priorizar 9:16** para Reels, TikTok e Shorts
- Cada cena deve declarar: **personagem, ambiente, emoção, câmera, iluminação, objetivo dramático**
- Prompts em **inglês**; incluir `no text, no watermark` salvo solicitação explícita do humano

**Library:** `library/veo3/` — regras, câmera, continuidade, archetypes  
**Doc API:** `docs/API_VIDEO_AUTOMATION.md`  
**Workflow:** WORKFLOW.md § Workflow 9

### Segurança de vídeo (Veo API)

| Regra | Ação |
|-------|------|
| **Nunca expor API keys** | Não ecoar, logar ou commitar chaves |
| **Nunca salvar secrets no repo** | Sem `.env`, JSON de SA ou tokens versionados |
| **Usar `.env` local** | Copiar de `scripts/video/.env.example` |
| **Sem texto no vídeo Veo** | Default `no text` — legendas no Filmora |
| **9:16 first** | Social vertical antes de 16:9 |
| **6 elementos por cena** | Ver `library/veo3/prompt-rules.md` |
| **Scripts de API** | Não implementar chamadas reais sem autorização explícita |

Se o usuário colar uma API key no chat: **não** repetir, **não** commitar — orientar uso em `.env` local.

### Filmora Pro

**Input esperado:** `video/filmora/edit-notes.md` + assets Veo 3 + áudio

**Entregáveis:** lyric video, reel 9:16, clip 16:9, export com legendas queimadas opcionais

### Canva

**Input esperado:** `design/canva-brief.md`

**Entregáveis:** capa de faixa, carrossel devocional, story, thumbnail YouTube

---

## Tarefas comuns — instruções

### Criar nova faixa

1. Copiar `templates/track-template.md` → `albums/.../tracks/track-XX-{slug}/`
2. Preencher `track.yaml`, `concept.md`, `lyrics.md`, `technical-sheet.md`
3. Gerar `suno/prompt.txt` a partir da ficha técnica
4. Linkar campanha e estudo bíblico (criar stubs se necessário)
5. Atualizar `album.yaml` se track_count mudar

### Refinar letra existente

1. Ler versão em `legal/dossie-direitos-autorais.md` ou `lyrics.md`
2. Aplicar mudanças mantendo tags Suno
3. Se alteração teológica: adicionar nota em `vibecore-alerts.md`
4. Setar `status: needs_review` até aprovação humana

### Gerar campanha de lançamento

1. Ler `track.yaml` + `concept.md`
2. Seguir WORKFLOW.md § Campanha
3. Output em `campaigns/campaign-track-XX/`
4. Incluir calendário mínimo 7 dias (teaser → launch → devocional)

### Gerar estudo bíblico

1. Ancorar no texto bíblico da faixa (não só na letra)
2. Estrutura: contexto → versículos-chave → aplicação → oração
3. Derivar `carousel-outline.md` para Canva (5–10 slides)

---

## Formato de resposta para agentes

Ao entregar trabalho no FCE, use esta estrutura:

```markdown
## Resumo
[1-2 frases do que foi feito]

## Arquivos afetados
- path/to/file.md — descrição

## Decisões
- [Decisão criativa ou teológica relevante]

## Pendências / VibeCore Alerts
- [Se houver]

## Próximo passo sugerido
- [Ação concreta]
```

---

## Metadados e frontmatter

Preferir `track.yaml` / `album.yaml` para dados machine-readable.

Se usar frontmatter markdown:

```yaml
---
fce_module: track
album_id: album-04
track_id: track-01
status: lyrics_final
updated: 2026-07-02
---
```

---

## Qualidade — checklist antes de entregar

### Letra
- [ ] Tags Suno em todas as seções
- [ ] Call-and-response marcados com parênteses
- [ ] Refrão identificável e repetível
- [ ] Fidelidade ao Salmo/passagem base
- [ ] `[End]` presente

### Ficha técnica
- [ ] Vibe Geral declarada
- [ ] Tempo estimado
- [ ] Ministração: Sim/Não + notas
- [ ] Suno prompt completo

### Campanha
- [ ] Hooks alinhados ao refrão
- [ ] CTAs cristãos autênticos (sem manipulação)
- [ ] Formato por plataforma

### Estudo bíblico
- [ ] Referências bíblicas citadas
- [ ] Aplicação prática
- [ ] Tom acolhedor, não preachy

---

## Tratamento de incerteza

| Situação | Ação |
|----------|------|
| Faixa não documentada | Perguntar ou criar stub com `status: concept` |
| Conflito letra vs Salmo | Flag VibeCore Alert, não resolver silenciosamente |
| Ferramenta indisponível | Documentar brief; humano executa depois |
| Escopo ambíguo | Default: uma faixa, não álbum inteiro |

---

## Glossário FCE

| Termo | Significado |
|-------|-------------|
| **VibeCore** | Identidade artística trap + teatral + arena |
| **Super Edição** | Faixa expandida com dinâmica cinematográfica |
| **Letra definitiva** | Versão aprovada para Suno e direitos autorais |
| **VibeCore Alert** | Pendência teológica ou de fidelidade bíblica |
| **Ficha técnica** | Metadados de produção (vibe, tempo, prompt) |
| **Campanha** | Conjunto de assets + calendário para uma faixa |
| **Ministração** | Momento falado/oração dentro da faixa |

---

## Versionamento com humanos

Agentes **não** fazem commit unless explicitly requested.

Quando humano pedir commit:
- Mensagem em PT ou EN clara
- Referenciar módulo: `docs:`, `track-01:`, `campaign:`, etc.
- Nunca commitar assets binários grandes

---

## Expansão deste documento

Novas regras para módulos (podcast, merch, etc.) devem ser adicionadas como seções aqui e referenciadas em PROJECT_STRUCTURE.md.

**Versão AGENTS.md:** 0.2.1 — módulo Veo API 2026-07-02
