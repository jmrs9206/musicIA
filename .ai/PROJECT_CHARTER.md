# Project Charter: MusicIA

## Metadata

- Project ID: `musicIA`
- Project name: `MusicIA - Productor IA & Prompting Suno`
- Owner: `jmrs9206`
- Repository: `/home/jmrs/Documentos/PROYECTOS/JMRS/MusicIA` (https://github.com/jmrs9206/musicIA.git)
- Status: `APPROVED`
- Version: `1.0`
- Last verified: `2026-07-21`
- Approved by: `jmrs9206`

## Problem

Crear un sistema de Inteligencia Artificial que aprenda la identidad musical del usuario (analizando sus propias canciones y sus influencias de otros autores) y actúe como un productor musical inteligente capaz de redactar prompts optimizados para Suno AI y evaluar las canciones generadas.

## Intended users

| User/persona | Need | Source | Status |
|---|---|---|---|
| Músico / Creador | Aprender su ADN musical e influencias para crear canciones en Suno con su estilo | USER | CONFIRMED |
| Productor Musical IA | Automatizar el proceso de análisis de audio, estilo, letras y creación de prompts Suno | USER | CONFIRMED |

## Desired outcome

Un ecosistema multipropósito de 6 agentes (Music Director, Audio Analyst, Style Analyst, Lyric Analyst, Prompt Engineer y Critic Agent) respaldado por una base de conocimiento persistente (`knowledge/`, `songs/`, `prompts/`, `analysis/`).

## In scope

- Red de 6 agentes especializados (`@music_director`, `@audio_analyst`, `@style_analyst`, `@lyric_analyst`, `@prompt_engineer`, `@critic_agent`).
- Base de conocimiento (`knowledge/mi_identidad_musical.md`, `mis_preferencias.json`, `mis_influencias.json`).
- Repositorio de audios (`songs/propias/`, `songs/referencias/`).
- Generación de prompts profesionales estructurados para Suno AI (`prompts/`).
- Módulo de análisis y reporte del Critic Agent.

## Out of scope / non-goals

- Despliegue en servidores en la nube sin aprobación previa.
- Compra automatizada de créditos de servicios de terceros.

## Success criteria

| ID | Criterion | Measurement | Target | Evidence owner |
|---|---|---|---|---|
| SC-001 | Red de Agentes definida | Documentada en `.agents/agents.md` y `.ai/ARCHITECTURE.md` | 100% | `@architect` |
| SC-002 | Base de conocimiento operativa | Estructura en `knowledge/` con archivos base | 100% | `@context` |
| SC-003 | Generador de Prompts Suno | Generación de style prompts (<120 caracteres) y metatags de estructura | 100% | `@prompt_engineer` |
