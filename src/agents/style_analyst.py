from pathlib import Path
from typing import List, Optional
from src.agents.base_agent import BaseAgent
from src.models import StyleAnalysis
from src.utils.file_helpers import write_json_file
from src.config import ANALYSIS_DIR

class StyleAnalystAgent(BaseAgent):
    """
    Agente 2: Style Analyst
    Encuentra patrones: géneros, influencias, atmósferas y producción.
    """
    def __init__(self):
        super().__init__(
            name="StyleAnalyst",
            role_description="Identifica géneros, influencias, atmósferas y características de producción."
        )

    def run(
        self,
        track_name: str,
        primary_genre: str = "Alternative Indie Rock",
        subgenres: Optional[List[str]] = None,
        influences: Optional[List[str]] = None,
        atmosphere: str = "Melancholic, Warm, Nostalgic",
        vocal_style: str = "Raw, intimate, emotive vocals"
    ) -> StyleAnalysis:
        self.log(f"Analizando patrones de estilo para: {track_name}")
        
        analysis = StyleAnalysis(
            primary_genre=primary_genre,
            subgenres=subgenres or ["Indie Pop", "Synth Folk"],
            influences=influences or ["Radiohead", "Phoebe Bridgers", "The xx"],
            atmosphere=atmosphere,
            production_characteristics=["Tape warmth", "Subtle reverb", "Dynamic contrast", "Analog compression"],
            vocal_style=vocal_style
        )
        
        output_json = ANALYSIS_DIR / f"{track_name.lower().replace(' ', '_')}_style_analysis.json"
        write_json_file(output_json, {
            "track_name": track_name,
            "primary_genre": analysis.primary_genre,
            "subgenres": analysis.subgenres,
            "influences": analysis.influences,
            "atmosphere": analysis.atmosphere,
            "production_characteristics": analysis.production_characteristics,
            "vocal_style": analysis.vocal_style
        })
        self.log(f"Informe de análisis de estilo guardado en: {output_json}")
        return analysis
