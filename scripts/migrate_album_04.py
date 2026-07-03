"""Fase 1 — Migração modular do Álbum 4."""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALBUM = ROOT / "albums" / "album-04-o-trono-intocavel"
DOSSIER_SRC = ROOT / "DOSSIÊ DE DIREITOS AUTORAIS_ ÁLBUM 4 - O TRONO INTOCÁVEL.md"

TRACKS = [
    {
        "num": 1, "slug": "o-legado", "title": "O Legado", "scripture": "Salmo 37", "ref": "Sl 37",
        "duration": "4:30-5:00", "vibe": "Trap Acústico & Pop Teatral", "ministration": True,
        "ministration_notes": "Oração falada no meio — clima confessional perfeito para quem descansa no Senhor",
        "suno": "Acoustic guitar pluck, smooth trap beat, poetic rap flow, theatrical pop-rock chorus, melodic hooks, massive dynamic shifts, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-37",
    },
    {
        "num": 2, "slug": "o-peso-do-clamor", "title": "O Peso do Clamor", "scripture": "Salmo 38", "ref": "Sl 38",
        "duration": "4:10-4:45", "vibe": "Dark Trap & Emo-Rap Teatral", "ministration": False,
        "ministration_notes": "Música extremamente densa — parede de som contínua, sem quebra de ministração",
        "suno": "Dark moody piano, heavy sub-bass, fast emotional rap flow, dramatic string accents, operatic backing vocals, intense dynamic shifts, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-38",
    },
    {
        "num": 3, "slug": "o-sopro-do-tempo", "title": "O Sopro do Tempo", "scripture": "Salmo 39", "ref": "Sl 39",
        "duration": "4:00-4:35", "vibe": "Rap Poético & Ambient Acústico", "ministration": True,
        "ministration_notes": "Momento sussurrado e reflexivo sobre fragilidade humana",
        "suno": "Ambient lofi trap, warm acoustic guitar, spoken-word poetry style, vulnerable melodic hook, soft vocal layers, emotional and atmospheric, Brazilian Portuguese vocals",
        "alerts": ["track-03-eclesiastes-vento"], "study_slug": "salmo-39",
    },
    {
        "num": 4, "slug": "o-lago-horrivel-e-a-rocha", "title": "O Lago Horrível e a Rocha", "scripture": "Salmo 40", "ref": "Sl 40",
        "duration": "4:15-4:50", "vibe": "Crossover Rap-Rock & Pop de Arena", "ministration": False,
        "ministration_notes": "Energia contínua — refrão de arena sem quebra longa",
        "suno": "Theatrical piano intro, abrupt switch to heavy trap-rock beat, fast urgent flow, massive pop-rock chorus, brass sections, massive dynamic shifts, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-40",
    },
    {
        "num": 5, "slug": "o-calice-da-traicao", "title": "O Cálice da Traição", "scripture": "Salmo 41", "ref": "Sl 41",
        "duration": "4:00-4:25", "vibe": "Trap-Rock Narrativo & Melancólico", "ministration": False,
        "ministration_notes": "Flow compassado e narrativa contínua",
        "suno": "Melancholic electric guitar riffs, punchy trap beat, aggressive fast rap flow, high-pitched pop hook, dramatic tension, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-41",
    },
    {
        "num": 6, "slug": "a-sede-da-minha-alma", "title": "A Sede da Minha Alma", "scripture": "Salmo 42", "ref": "Sl 42",
        "duration": "4:40-5:10", "vibe": "Power Ballad Teatral & Trap Orquestral", "ministration": True,
        "ministration_notes": 'Ministração teatral na pergunta "por que estás abatida"',
        "suno": "Cinematic strings, slow powerful trap ballad, deeply emotional vocals, epic stadium rock chorus, huge dynamic shifts, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-42",
    },
    {
        "num": 7, "slug": "luz-e-verdade", "title": "Luz e Verdade", "scripture": "Salmo 43", "ref": "Sl 43",
        "duration": "4:00-4:30", "vibe": "Cinematic Trap & Theatrical Anthem", "ministration": False,
        "ministration_notes": "Direta e enérgica — hit pop rock contínuo",
        "suno": "Cinematic trap beat, dramatic strings, fast rhythmic rap flow, stadium rock chorus, theatrical transitions, acoustic harp accents, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-43",
    },
    {
        "num": 8, "slug": "o-clamor-da-historia", "title": "O Clamor da História", "scripture": "Salmo 44", "ref": "Sl 44",
        "duration": "4:20-4:50", "vibe": "Cinematic Trap-Rock / Marcha Épica & Flow Urgente", "ministration": False,
        "ministration_notes": "Clamor contínuo com vocais agressivos",
        "suno": "Epic marching trap beat, staccato orchestral strings, urgent aggressive rap flow, anthemic stadium chants, high theatrical energy, massive dynamic shifts, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-44",
    },
    {
        "num": 9, "slug": "o-cantico-do-casamento-real", "title": "O Cântico do Casamento Real", "scripture": "Salmo 45", "ref": "Sl 45",
        "duration": "4:30-5:00", "vibe": "Pop-Rock Teatral & Upbeat Brass (Festa de Casamento)", "ministration": True,
        "ministration_notes": "Ode poética à santidade",
        "suno": "Upbeat energetic pop-rock, jaunty theatrical brass, danceable trap-pop rhythm, catchy addictive hooks, playful backing harmonies, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-45",
    },
    {
        "num": 10, "slug": "o-refugio-inabalavel", "title": "O Refúgio Inabalável", "scripture": "Salmo 46", "ref": "Sl 46",
        "duration": "4:45-5:15", "vibe": "Epic Arena Rock Anthem & Hip-Hop Crossover (O Grande Hino)", "ministration": True,
        "ministration_notes": 'Momento "aquietai-vos" — voz falada imponente no bridge',
        "suno": "Heavy sub-bass drops, rhythmic distorted guitar accents, confident rapid rap flow, massive arena rock anthem chorus, heavy dynamic shifts, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-46",
    },
    {
        "num": 11, "slug": "o-aplauso-das-nacoes", "title": "O Aplauso das Nações", "scripture": "Salmo 47", "ref": "Sl 47",
        "duration": "4:00-4:35", "vibe": "Trap-Pop Festivo & Coro Teatral", "ministration": False,
        "ministration_notes": "Foco na festa e batida contagiante",
        "suno": "Organic handclaps, rhythmic trap-pop beat, call-and-response vocals, joyful theatrical energy, soaring vocal harmonies, upbeat brass, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-47",
    },
    {
        "num": 12, "slug": "a-cidade-do-grande-rei", "title": "A Cidade do Grande Rei", "scripture": "Salmo 48", "ref": "Sl 48",
        "duration": "5:00-5:30", "vibe": "Symphonic Trap-Rock / Grand Finale Teatral", "ministration": True,
        "ministration_notes": "Declaração da eternidade de Sião — fechamento monumental",
        "suno": "Grand synth textures, cinematic trap rhythm, epic melodic rock climax, soaring vocals, satisfying resolutions, massive choir, Brazilian Portuguese vocals",
        "alerts": [], "study_slug": "salmo-48",
    },
]


def clean_cites(text: str) -> str:
    text = re.sub(r"\\\[cite: [^\]]+\\\]", "", text)
    return text.replace("\\!", "!").replace("\\-", "-")


def parse_dossier(text: str) -> list[dict]:
    text = text.replace("\r\n", "\n")
    parts = re.split(r"### \*\*\d+\\. TÍTULO DA FAIXA:", text)[1:13]
    results = []
    for block in parts:
        concept_m = re.search(
            r"\* \*\*RESUMO DA FAIXA / CONCEITO DE CRIAÇÃO:\*\* (.+?)(?=\n\* \*\*FICHA)",
            block,
            re.DOTALL,
        )
        concept = clean_cites(concept_m.group(1).strip()) if concept_m else ""
        lyrics_m = re.search(r"\* \*\*LETRA DEFINITIVA:\*\* (.+?)(?=\n\n|\Z)", block, re.DOTALL)
        lyrics_raw = lyrics_m.group(1).strip() if lyrics_m else ""
        lyrics_raw = re.sub(
            r"^\*\(Atenção: ver VibeCore Alerts no final do relatório\)\.\* ",
            "",
            lyrics_raw,
        )
        results.append({"concept": concept, "lyrics_raw": lyrics_raw})
    return results


def format_lyrics_md(title, scripture, lyrics_raw, status="final", alert_note=False):
    lines = [
        f"# {title} — Letra Definitiva",
        "",
        "**Idioma:** Português Brasileiro  ",
        f"**Referência:** {scripture}  ",
        f"**Status:** {status}",
        "",
    ]
    if alert_note:
        lines.extend([
            "> **VibeCore Alert:** Ver [`../../legal/vibecore-alerts.md`](../../legal/vibecore-alerts.md)",
            "",
        ])
    lines.extend(["---", ""])
    formatted = lyrics_raw
    formatted = re.sub(r"(\[Language: Brazilian Portuguese\])", r"\n\1\n", formatted)
    formatted = re.sub(
        r"(\[(?:Intro|Verse|Pre-Chorus|Chorus|Bridge|Outro)[^\]]*\])",
        r"\n\n\1\n",
        formatted,
    )
    formatted = re.sub(r"(\[End\])", r"\n\1", formatted)
    lines.append(formatted.strip())
    lines.append("")
    return "\n".join(lines)


def stub(template: str, track: dict) -> str:
    return (
        template.replace("{{TITLE}}", track["title"])
        .replace("{{SCRIPTURE}}", track["scripture"])
        .replace("{{VIBE}}", track["vibe"])
    )


STUB_VIDEO = """# Brief Veo 3 — {{TITLE}}

**Faixa:** {{TITLE}} ({{SCRIPTURE}})  
**Status:** pendente  
**Álbum:** [O Trono Intocável](../../concept.md)

## Direção visual

[PREENCHER — ver WORKFLOW.md § Workflow 3]

## Cenas sugeridas

| # | Duração | Descrição | Prompt Veo 3 |
|---|---------|-----------|--------------|
| 1 | 5-8s | [PREENCHER] | [PREENCHER] |

## Referências

- Vibe: {{VIBE}}
- Paleta álbum: ouro, roxo profundo, preto teatral
"""

STUB_STORY = """# Storyboard — {{TITLE}}

**Status:** pendente

| Cena | Timestamp | Visual | Áudio / Letra |
|------|-----------|--------|---------------|
| 1 | 0:00 | [PREENCHER] | Intro |
"""

STUB_FILMORA = """# Notas de montagem — Filmora Pro

**Faixa:** {{TITLE}}  
**Status:** pendente

## Entregáveis previstos

- [ ] Clip 16:9
- [ ] Reel 9:16
- [ ] Lyric video
- [ ] SRT legendas

## Notas

[PREENCHER após geração Veo 3 e áudio Suno]
"""

STUB_CANVA = """# Brief Canva — {{TITLE}}

**Status:** pendente

## Assets previstos

- [ ] Capa de faixa (1080×1080)
- [ ] Carrossel devocional (5-10 slides)
- [ ] Story teaser (1080×1920)
- [ ] Thumbnail YouTube (1280×720)

## Elementos visuais

- Versículo anchor: {{SCRIPTURE}}
- Vibe: {{VIBE}}
"""

STUB_CAPTIONS = """# Legendas — {{TITLE}}

**Status:** pendente — gerar via WORKFLOW.md § Workflow 5

## Instagram

[PREENCHER]

## TikTok

[PREENCHER]

## YouTube

[PREENCHER]
"""

STUB_POSTS = """# Posts — {{TITLE}}

**Status:** pendente

## Hooks sugeridos

[PREENCHER a partir do refrão]

## CTAs

[PREENCHER]
"""

SUNO_NOTES = """# Notas de iteração Suno

**Faixa:** {{TITLE}}  
**Status:** pendente — nenhuma geração registrada ainda

| # | Data | Notas | Avaliação |
|---|------|-------|-----------|
| — | — | — | — |
"""


def main():
    for d in ["tracks", "campaigns", "bible-studies", "assets", "legal"]:
        (ALBUM / d).mkdir(parents=True, exist_ok=True)
    (ROOT / "templates").mkdir(exist_ok=True)

    shutil.copy2(DOSSIER_SRC, ALBUM / "legal" / "dossie-direitos-autorais.md")

    parsed = parse_dossier(DOSSIER_SRC.read_text(encoding="utf-8"))
    assert len(parsed) == 12, f"Expected 12 tracks, got {len(parsed)}"

    for i, tr in enumerate(TRACKS):
        n = tr["num"]
        nn = f"{n:02d}"
        folder = ALBUM / "tracks" / f"track-{nn}-{tr['slug']}"
        for sub in [
            "suno/iterations",
            "video/filmora",
            "design",
            "copy",
            "assets/audio",
            "assets/video",
            "assets/images",
        ]:
            (folder / sub).mkdir(parents=True, exist_ok=True)

        p = parsed[i]
        status = "needs_review" if tr["alerts"] else "lyrics_final"
        lyrics_status = "needs_review" if tr["alerts"] else "final"

        if tr["alerts"]:
            alerts_block = "vibecore_alerts:\n" + "\n".join(f"  - {a}" for a in tr["alerts"])
        else:
            alerts_block = "vibecore_alerts: []"

        yaml_content = f"""id: track-{nn}
album_id: album-04
number: {n}
title: "{tr['title']}"
slug: {tr['slug']}
scripture: "{tr['scripture']}"
scripture_ref: "{tr['ref']}"
duration_estimate: "{tr['duration']}"
vibe: "{tr['vibe']}"
ministration: {str(tr['ministration']).lower()}
ministration_notes: "{tr['ministration_notes']}"
suno_prompt: "{tr['suno']}"
status: {status}
{alerts_block}
updated: 2026-07-02
"""
        (folder / "track.yaml").write_text(yaml_content, encoding="utf-8")

        concept_md = f"""# {tr['title']} — Conceito de Criação

**Álbum:** [O Trono Intocável](../../concept.md)  
**Referência bíblica:** {tr['scripture']} ({tr['ref']})  
**Faixa:** {n} de 12

## Resumo

{p['concept']}

## Links

- [Letra definitiva](./lyrics.md)
- [Ficha técnica](./technical-sheet.md)
- [Suno prompt](./suno/prompt.txt)
- Campanha: `../../campaigns/campaign-track-{nn}/` (pendente)
- Estudo bíblico: `../../bible-studies/study-track-{nn}-{tr['study_slug']}/` (pendente)
"""
        (folder / "concept.md").write_text(concept_md, encoding="utf-8")

        (folder / "lyrics.md").write_text(
            format_lyrics_md(
                tr["title"],
                tr["scripture"],
                p["lyrics_raw"],
                lyrics_status,
                alert_note=bool(tr["alerts"]),
            ),
            encoding="utf-8",
        )

        min_str = "Sim" if tr["ministration"] else "Não"
        tech = f"""# Ficha Técnica — {tr['title']}

**Referência:** {tr['scripture']}  
**Status da letra:** {lyrics_status}

## Vibe Geral

{tr['vibe']}

## Estimativa de Tempo

{tr['duration']}

## Ministração

**{min_str}** — {tr['ministration_notes']}

## Suno Prompt

```
{tr['suno']}
```

## Arquivos relacionados

- [Letra definitiva](./lyrics.md)
- [Prompt Suno](./suno/prompt.txt)
"""
        (folder / "technical-sheet.md").write_text(tech, encoding="utf-8")
        (folder / "suno" / "prompt.txt").write_text(tr["suno"] + "\n", encoding="utf-8")

        for name, tpl in [
            ("video/veo3-brief.md", STUB_VIDEO),
            ("video/storyboard.md", STUB_STORY),
            ("video/filmora/edit-notes.md", STUB_FILMORA),
            ("design/canva-brief.md", STUB_CANVA),
            ("copy/captions.md", STUB_CAPTIONS),
            ("copy/posts.md", STUB_POSTS),
            ("suno/iterations/notes.md", SUNO_NOTES),
        ]:
            (folder / name).write_text(stub(tpl, tr), encoding="utf-8")

        for ad in ["assets/audio", "assets/video", "assets/images"]:
            (folder / ad / ".gitkeep").write_text("", encoding="utf-8")

        print(f"OK track-{nn}-{tr['slug']}")

    (ALBUM / "assets" / ".gitkeep").write_text("", encoding="utf-8")
    print("Migration complete.")


if __name__ == "__main__":
    main()
