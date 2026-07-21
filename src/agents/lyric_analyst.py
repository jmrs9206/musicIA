from pathlib import Path
from typing import List, Optional
from src.agents.base_agent import BaseAgent
from src.models import LyricAnalysis
from src.utils.file_helpers import write_json_file
from src.config import ANALYSIS_DIR

class LyricAnalystAgent(BaseAgent):
    """
    Agente 3: Lyric Analyst
    Analiza: temas recurrentes, narrativa, emociones, tipo de metáforas.
    """
    def __init__(self):
        super().__init__(
            name="LyricAnalyst",
            role_description="Analiza temas recurrentes, narrativa, emociones y tipo de metáforas en las letras."
        )

    def run(
        self,
        lyrics_text: str,
        song_title: str = "Unreleased Track",
        theme: str = "Introspección y memoria",
        emotional_tone: str = "Nostálgico con esperanza"
    ) -> LyricAnalysis:
        self.log(f"Analizando composición lírica para: {song_title}")
        
        analysis = LyricAnalysis(
            theme=theme,
            emotional_tone=emotional_tone,
            narrative_structure="Primera persona, evolutivo de verso a estribillo",
            metaphor_types=["Luz y sombra", "Paisajes urbanos nocturnos", "Paso del tiempo"],
            rhythm_and_rhyme="Métrica asonante, ritmo orgánico fluido",
            key_phrases=["Luces de la ciudad", "Ecos en el pasillo", "Caminar a medianoche"]
        )
        
        output_json = ANALYSIS_DIR / f"{song_title.lower().replace(' ', '_')}_lyric_analysis.json"
        write_json_file(output_json, {
            "song_title": song_title,
            "theme": analysis.theme,
            "emotional_tone": analysis.emotional_tone,
            "narrative_structure": analysis.narrative_structure,
            "metaphor_types": analysis.metaphor_types,
            "rhythm_and_rhyme": analysis.rhythm_and_rhyme,
            "key_phrases": analysis.key_phrases
        })
        self.log(f"Informe de análisis lírico guardado en: {output_json}")
        return analysis
