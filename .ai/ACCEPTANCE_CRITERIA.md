# Acceptance Criteria: MusicIA

## Metadata

- Project ID: `musicIA`
- Version: `0.1`

## Acceptance Criteria List

### AC-001: Estructura de Orquestación

- **Given**: El repositorio `MusicIA`.
- **When**: Se efectúa la inicialización del proyecto.
- **Then**: Deben copiarse correctamente las carpetas `.agents/`, `templates/`, `docs/` y los archivos `GEMINI.md` y `MANIFEST.md`.

### AC-002: Paquete de Control `.ai/`

- **Given**: El framework del orquestador instalado.
- **When**: Se ejecuta el skill `inicializar_proyecto`.
- **Then**: Deben crearse los documentos `.ai/PROJECT_CHARTER.md`, `.ai/PROJECT_CONSTITUTION.md`, `.ai/PROJECT_CONTEXT.md`, `.ai/REQUIREMENTS.md` y `.ai/WORKFLOW.md`.

### AC-003: Definición del Workflow

- **Given**: El marco del orquestador activo.
- **When**: Se inicia el workflow del proyecto.
- **Then**: Debe documentarse el roadmap por fases e iteraciones en `.ai/WORKFLOW.md` y `.ai/HANDOFF.md`.
