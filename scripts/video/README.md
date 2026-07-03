# Scripts de Vídeo — FCE

Scripts para geração de vídeo com **Google Veo** (Gemini API ou Vertex AI).

**Status:** preparação — **nenhum script de API implementado ainda.**

---

## Propósito

Este diretório abrigará automação futura para:

- Gerar cenas individuais a partir de `veo3-scene-template.md`
- Processar planos completos (`veo3-video-plan-template.md`)
- Registrar logs de geração (sem secrets)
- Exportar MP4 para `albums/.../tracks/.../assets/video/veo3/`

---

## Setup (quando scripts existirem)

```bash
cd scripts/video
cp .env.example .env
# Editar .env LOCALMENTE — nunca commitar
```

### Dependências previstas (futuro)

```
google-genai          # Gemini API
google-cloud-aiplatform  # Vertex AI (opcional)
python-dotenv
```

Instalação futura via `requirements-video.txt` (a criar).

---

## Estrutura prevista

```
scripts/video/
├── README.md              ← este arquivo
├── .env.example           ← template de variáveis
├── requirements-video.txt ← (futuro)
├── generate_scene.py      ← (futuro) uma cena
├── generate_video_plan.py ← (futuro) plano completo
└── lib/
    ├── prompts.py         ← (futuro) validação 6 elementos
    └── config.py          ← (futuro) leitura segura de env
```

---

## Uso manual (hoje)

1. Ler `docs/API_VIDEO_AUTOMATION.md`
2. Preencher templates em `templates/veo3-*.md`
3. Copiar prompts para [Google AI Studio](https://aistudio.google.com/)
4. Salvar MP4 em `tracks/.../assets/video/veo3/`

---

## Segurança

| Regra | Detalhe |
|-------|---------|
| `.env` | Gitignored — copiar de `.env.example` |
| API keys | Nunca no código, markdown ou YAML |
| Service accounts | Fora do repositório |
| Logs | Sem keys, sem PII |
| Agentes IA | Não commitar `.env` mesmo se usuário colar key no chat |

Ver `AGENTS.md` § Segurança de vídeo.

---

## Links

- [API_VIDEO_AUTOMATION.md](../../docs/API_VIDEO_AUTOMATION.md)
- [library/veo3/](../../library/veo3/)
- [WORKFLOW.md § Workflow 9](../../WORKFLOW.md)
