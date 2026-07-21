# Project Constitution: MusicIA

## Metadata

- Project ID: `musicIA`
- Status: `APPROVED`
- Version: `1.0`
- Approved by: `jmrs9206`
- Effective from: `2026-07-21`

## Purpose of this constitution

Define project-specific permissions and restrictions for MusicIA. Global policies in `.agents/policies/` apply at all times.

## Allowed repositories and roots

| Root | Purpose | Read | Write | Notes |
|---|---|---:|---:|---|
| `/home/jmrs/Documentos/PROYECTOS/JMRS/MusicIA` | Workspace principal de MusicIA | yes | yes | Único workspace autorizado |

## Prohibited paths

- `/home/jmrs/Documentos/PROYECTOS/JMRS/orquestadorIA` (solo lectura como referencia previa, no modificar)
- Archivos fuera del workspace `/home/jmrs/Documentos/PROYECTOS/JMRS/MusicIA`

## Allowed roles

- `@director`
- `@product`
- `@context`
- `@architect`
- `@planner`
- `@frontend`
- `@backend`
- `@qa`
- `@reviewer`
- `@memory`

## Technology constraints

- Required: Git, Node.js / Web Stack o Python según arquitectura aprobada.
- Prohibited: Invención de pruebas, commitear secretos o credenciales.
- Package manager: npm / pip (según módulo).

## Actions requiring human approval

- Instalación de dependencias de producción no planeadas.
- Push a ramas protegidas o remotos adicionales.
- Modificación de la constitución.
- Eliminación destructiva de archivos.

## Git policy

- Default branch: `main`
- Commit policy: Commits claros con mensajes descriptivos.
- Push policy: Requiere aprobación previa o instrucción explícita del usuario.
