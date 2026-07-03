# Automação de Vídeo — API Veo (Gemini / Vertex AI)

Documentação do módulo de geração de vídeo do **Franklin Creative Engine (FCE)**.

**Status:** preparação — sem implementação de API ativa.  
**Objetivo:** habilitar workflow manual/semiautomático hoje e automação futura com segurança.

---

## Visão geral

O FCE produz vídeos para campanhas de música cristã (Reels, TikTok, Shorts, clips 16:9). A geração visual usa **Google Veo** via:

| Caminho | Uso recomendado | Credencial |
|---------|-----------------|------------|
| **Gemini API** | Prototipagem, artista solo, baixo volume | `GEMINI_API_KEY` em `.env` local |
| **Vertex AI** | Produção em escala, equipe, billing GCP | Service account + `GOOGLE_CLOUD_PROJECT` |

Ambos compartilham a mesma **lógica de prompts** documentada em `library/veo3/`. A diferença está na autenticação, quotas e onde os assets são armazenados.

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  track.yaml     │────►│ veo3-video-plan  │────►│ veo3-scene × N  │
│  storyboard.md  │     │ (template)       │     │ (template)      │
└─────────────────┘     └────────┬─────────┘     └────────┬────────┘
                                 │                        │
                                 ▼                        ▼
                        library/veo3/              Prompts em inglês
                        (regras curadas)           no text by default
                                 │                        │
                                 ▼                        ▼
                        ┌────────────────────────────────────────┐
                        │  FUTURO: scripts/video/generate_*.py   │
                        │  HOJE:   geração manual no AI Studio   │
                        └────────────────┬───────────────────────┘
                                         ▼
                        tracks/.../assets/video/veo3/*.mp4
                                         │
                                         ▼
                        Filmora Pro → reel 9:16 / clip 16:9
```

---

## Estado atual vs. futuro

| Capacidade | Hoje | Futuro |
|------------|------|--------|
| Planejamento de cenas | ✅ Templates + library | ✅ |
| Prompts Veo curados | ✅ `library/veo3/` | ✅ |
| Geração via script | ❌ | `scripts/video/generate_scene.py` |
| Batch por faixa | ❌ | `scripts/video/generate_video_plan.py` |
| Upload automático GCS | ❌ | Vertex AI pipeline |
| CI/CD | ❌ | Opcional, secrets no vault |

**Regra:** Nenhum script neste repositório deve conter API keys ou chamar a API até revisão explícita de segurança e entrada no ROADMAP Fase 3+.

---

## Gemini API vs. Vertex AI

### Gemini API (Google AI Studio)

**Quando usar:**
- Testes de prompt por cena
- 1–5 vídeos por sessão
- Desenvolvedor individual

**Configuração (futura):**
```bash
# scripts/video/.env (NUNCA commitar)
GEMINI_API_KEY=sua_chave_aqui
VEO_MODEL=veo-3.0-generate-preview   # confirmar ID atual na documentação Google
```

**Referência:** [Google AI — Veo](https://ai.google.dev/gemini-api/docs/video)

### Vertex AI (Google Cloud)

**Quando usar:**
- Volume alto (12 faixas × múltiplas cenas)
- Controle de billing por projeto
- Storage em Cloud Storage para assets

**Configuração (futura):**
```bash
GOOGLE_CLOUD_PROJECT=fce-production
GOOGLE_CLOUD_REGION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json  # fora do repo
VEO_MODEL=veo-3.0-generate-preview
GCS_OUTPUT_BUCKET=fce-veo-assets
```

**Referência:** [Vertex AI — Generate videos](https://cloud.google.com/vertex-ai/generative-ai/docs/video/overview)

---

## Segurança

### Regras inegociáveis

1. **Nunca** commitar `.env`, API keys, JSON de service account ou tokens
2. **Nunca** hardcodar secrets em scripts, markdown ou YAML versionado
3. Usar `scripts/video/.env.example` como referência — copiar para `.env` local
4. `.gitignore` já cobre `.env` e `.env.*` (exceto `.env.example`)
5. Agentes de IA **não** devem pedir, logar ou ecoar chaves do usuário
6. Assets gerados (`.mp4`) ficam em `assets/video/` — gitignored

### Checklist antes de implementar scripts

- [ ] `.env.example` documentado
- [ ] Leitura de env via `os.environ` / python-dotenv (futuro)
- [ ] Falha clara se variável ausente (sem fallback com key fake)
- [ ] Logs sem prompt completo se contiver PII (futuro)
- [ ] Rate limiting e retry documentados
- [ ] Revisão de custos Vertex/Gemini por cena

---

## Workflow manual (hoje)

### 1. Planejar

1. Abrir `tracks/track-XX/video/storyboard.md`
2. Copiar `templates/veo3-video-plan-template.md` → `video/veo3-video-plan.md`
3. Definir cenas com os 6 elementos obrigatórios (ver `library/veo3/prompt-rules.md`)

### 2. Escrever prompts

1. Por cena: copiar `templates/veo3-scene-template.md` → `video/scenes/scene-NN.md` (opcional)
2. Aplicar regras de `library/veo3/`
3. Validar: **no text**, **9:16** para social, vibe alinhada à faixa

### 3. Gerar (manual)

1. Colar prompt no Google AI Studio / Vertex console
2. Aspect ratio: **9:16** (720×1280 ou 1080×1920) para Reels/TikTok/Shorts
3. Duração alvo: **5–8 segundos** por cena
4. Baixar MP4 → `tracks/.../assets/video/veo3/scene-NN.mp4`

### 4. Registrar

1. Anotar take escolhido em `video/veo3-brief.md` ou plano
2. Atualizar `video/filmora/edit-notes.md` com ordem de cenas

### 5. Montar

Seguir WORKFLOW.md § Workflow 3 (Filmora Pro).

---

## Workflow semiautomático (futuro)

Quando `scripts/video/` estiver implementado:

```bash
cd scripts/video
cp .env.example .env
# editar .env localmente

# Gerar uma cena (futuro)
# python generate_scene.py --track ../../albums/.../track-01-o-legado --scene 01

# Gerar plano completo (futuro)
# python generate_video_plan.py --track ../../albums/.../track-01-o-legado
```

Saída esperada:
```
tracks/track-XX/assets/video/veo3/
├── scene-01.mp4
├── scene-02.mp4
├── generation-log.json    # metadados, sem secrets
└── prompts/               # prompts usados (versionados opcionalmente)
```

---

## Formato e prioridades de entrega

| Formato | Aspect ratio | Resolução alvo | Uso FCE |
|---------|--------------|----------------|---------|
| **Reel / Short / TikTok** | **9:16** | 1080×1920 | **Prioridade 1** |
| Lyric clip social | 9:16 | 1080×1920 | Lançamento faixa |
| YouTube clip | 16:9 | 1920×1080 | Secundário |
| Thumbnail source | 16:9 | 1280×720 | Frame grab Filmora |

**Default FCE:** planejar e gerar primeiro em **9:16**. Derivar 16:9 no Filmora (crop/reframe) se necessário.

---

## Estrutura de arquivos

```
docs/
└── API_VIDEO_AUTOMATION.md     ← este arquivo

library/veo3/
├── prompt-rules.md
├── camera-moves.md
├── character-continuity.md
└── scene-archetypes.md

templates/
├── veo3-scene-template.md
└── veo3-video-plan-template.md

scripts/video/
├── README.md
├── .env.example
└── (generate_*.py — futuro)

albums/.../tracks/track-XX/
└── video/
    ├── veo3-brief.md
    ├── veo3-video-plan.md      ← plano completo (opcional)
    ├── storyboard.md
    ├── scenes/                 ← cenas individuais (opcional)
    └── filmora/edit-notes.md
```

---

## Integração com VibeCore (Álbum 4)

| Vibe da faixa | Direção Veo | Archetype |
|---------------|-------------|-----------|
| Dark Trap (02) | Chuva, piano, sombras | `lament`, `confession` |
| Arena Rock (10) | Montanhas, luz rompendo | `refuge`, `epic-wide` |
| Festivo (09, 11) | Palmas, ouro, movimento | `celebration`, `coronation` |
| Power Ballad (06) | Água, cervo, névoa | `thirst`, `longing` |
| Grand Finale (12) | Sião, trono, synth glow | `holy-city`, `throne` |

Ver detalhes em `library/veo3/scene-archetypes.md`.

---

## Custos e quotas (orientativo)

> Valores mudam — consultar pricing oficial antes de batch.

- Estimar **N cenas × iterações** por faixa (ex.: 8 cenas × 3 takes = 24 gerações)
- Gemini API: billing por uso / tier free limitado
- Vertex AI: billing GCP + storage GCS
- Registrar custo estimado no plano de vídeo antes de batch

---

## Links internos

- [WORKFLOW.md § Workflow 9](../WORKFLOW.md) — pipeline Veo API
- [WORKFLOW.md § Workflow 3](../WORKFLOW.md) — montagem Filmora
- [AGENTS.md § Vídeo e segurança](../AGENTS.md)
- [scripts/video/README.md](../scripts/video/README.md)

---

## Histórico

| Data | Evento |
|------|--------|
| 2026-07-02 | Módulo inicial — docs, library, templates, scripts stub |
