# Project Context: MusicIA

## Context identity

- Project ID: `musicIA`
- Context version: `0.1`
- Repository root: `/home/jmrs/Documentos/PROYECTOS/JMRS/MusicIA`
- Branch/worktree: `main`
- Commit verified: `7cc382c1e3edfb537de7227cc98b6387e74e0851`
- Last verified: `2026-07-21 09:48 CEST`
- Curated by: `@context`

## One-paragraph summary

MusicIA es un proyecto para desarrollo de una aplicación / plataforma de inteligencia artificial aplicada a la música. Ha sido inicializado con el marco del Orquestador de Agentes IA (`orquestadorIA`), estableciendo control de políticas, skills, plantillas y ciclo de vida por iteraciones.

## Verified facts

| ID | Fact | Source | Verified | Confidence |
|---|---|---|---|---|
| F-001 | Repositorio local inicializado en Git | `git status` / `git log` | 2026-07-21 | HIGH |
| F-002 | Remoto vinculado a `https://github.com/jmrs9206/musicIA.git` | `git remote -v` | 2026-07-21 | HIGH |
| F-003 | Marco de orquestador copiado desde `orquestadorIA` | Inspección de directorio | 2026-07-21 | HIGH |

## Current state (`CURRENT`)

### Repository map

```text
/home/jmrs/Documentos/PROYECTOS/JMRS/MusicIA
├── .agents/          # Marco de políticas, skills, roles y workflows
├── .ai/              # Paquete de control del proyecto (Charter, Context, Requisitos)
├── docs/             # Documentación de arquitectura y ciclo de vida
├── templates/        # Plantillas de artefactos de gobernanza
├── GEMINI.md         # Contexto raíz para agente AI
├── MANIFEST.md       # Manifiesto de componentes del orquestador
└── README.md         # Documento inicial del proyecto
```

### Implemented capabilities

- Estructura de gobernanza multirrol inicializada (`.agents/`).
- Paquete `.ai/` activo.
- Repositorio sincronizado con GitHub.

## Unknowns and conflicts

| ID | Type | Description | Impact | Resolution owner |
|---|---|---|---|---|
| U-001 | UNKNOWN | Módulos funcionales de IA/Audio a implementar en el proyecto | Define la arquitectura técnica | `@product` / USER |

## Current iteration

- Iteration ID: `IT-001`
- Goal: Inicialización del marco de orquestación y establecimiento del workflow inicial.
- Approved tasks:
  - T-001: Copiar marco de orquestador.
  - T-002: Crear paquete `.ai/` (Charter, Constitución, Contexto, Workflow).
