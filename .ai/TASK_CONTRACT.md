# Task Contract: TASK-001 (Iteración IT-001)

## Metadata

- Task ID: `TASK-001`
- Iteration ID: `IT-001`
- Title: `Implementación del Motor Core de Agentes de MusicIA y CLI de Suno`
- Assigned Role: `@architect` / `@backend`
- Status: `DONE`
- Approved by: `jmrs9206`

- Date: `2026-07-21`

---

## Objective

Implementar los módulos en Python (`src/agents/`) para la red de 6 agentes (Music Director, Audio Analyst, Style Analyst, Lyric Analyst, Prompt Engineer, Critic Agent), así como la integración con la base de conocimiento (`knowledge/`), el almacenamiento de canciones y análisis (`songs/`, `analysis/`) y un ejecutable CLI (`main.py`) para generar prompts optimizados para Suno AI.

---

## Inputs

- `knowledge/mi_identidad_musical.md`
- `knowledge/mis_preferencias.json`
- `knowledge/mis_influencias.json`
- `prompts/templates_suno.json`

---

## Scope & Authorized Paths

- `src/` (crear módulos y agentes)
- `main.py` (CLI ejecutable)
- `requirements.txt` (si fuera necesario dependencias estándar)

---

## Acceptance Criteria

- [x] Implementación de `src/models.py` con los modelos de datos de identidad, análisis y prompt de Suno.
- [x] Implementación de la suite de 6 agentes en `src/agents/`.
- [x] Generación de prompts Suno válidos respetando la regla del Style Prompt (<120 caracteres) y metatags de canción (`[Intro]`, `[Verse]`, `[Chorus]`, etc.).
- [x] CLI `main.py` funcional con comandos `generate-prompt`, `analyze-song`, `build-dna` y `evaluate-track`.
