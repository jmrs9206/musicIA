import os
from pathlib import Path

# Absolute Root Directory of the Project
BASE_DIR = Path(__file__).resolve().parent.parent

# Core Paths
KNOWLEDGE_DIR = BASE_DIR / "knowledge"
SONGS_DIR = BASE_DIR / "songs"
SONGS_PROPIAS_DIR = SONGS_DIR / "propias"
SONGS_REFERENCIAS_DIR = SONGS_DIR / "referencias"
ANALYSIS_DIR = BASE_DIR / "analysis"
PROMPTS_DIR = BASE_DIR / "prompts"
PROMPTS_HISTORICO_DIR = PROMPTS_DIR / "historico"

# Core Knowledge Files
IDENTITY_FILE = KNOWLEDGE_DIR / "mi_identidad_musical.md"
PREFERENCES_FILE = KNOWLEDGE_DIR / "mis_preferencias.json"
INFLUENCES_FILE = KNOWLEDGE_DIR / "mis_influencias.json"
SUNO_TEMPLATES_FILE = PROMPTS_DIR / "templates_suno.json"

# Suno AI Constraints
SUNO_MAX_STYLE_LENGTH = 120
SUNO_MAX_LYRICS_LENGTH = 3000

# Ensure essential directories exist
for folder in [KNOWLEDGE_DIR, SONGS_PROPIAS_DIR, SONGS_REFERENCIAS_DIR, ANALYSIS_DIR, PROMPTS_HISTORICO_DIR]:
    folder.mkdir(parents=True, exist_ok=True)
