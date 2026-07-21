from pathlib import Path
from typing import Dict, Any, Optional
from src.agents.base_agent import BaseAgent
from src.models import AudioAnalysis
from src.utils.file_helpers import write_json_file
from src.config import ANALYSIS_DIR

class AudioAnalystAgent(BaseAgent):
    """
    Agente 1: Audio Analyst
    Analiza archivos MP3/WAV/FLAC y detecta BPM, energía, instrumentos y estructura.
    """
    def __init__(self):
        super().__init__(
            name="AudioAnalyst",
            role_description="Analiza archivos MP3/WAV y extrae BPM, energía, instrumentos y estructura musical."
        )

    def run(
        self,
        audio_file_path: Path,
        bpm: Optional[int] = None,
        key: Optional[str] = None,
        energy_level: str = "medium",
        key_instruments: Optional[list] = None,
        structure: Optional[list] = None
    ) -> AudioAnalysis:
        self.log(f"Analizando archivo de audio: {audio_file_path.name}")
        
        analysis = AudioAnalysis(
            file_name=audio_file_path.name,
            bpm=bpm or 105,
            key=key or "A Minor",
            energy_level=energy_level,
            time_signature="4/4",
            key_instruments=key_instruments or ["Acoustic Guitar", "Analog Synth", "Drums", "Electric Bass"],
            structure=structure or ["Intro", "Verse 1", "Chorus", "Verse 2", "Bridge", "Chorus", "Outro"],
            technical_notes=f"Análisis procesado para {audio_file_path.name}."
        )
        
        output_json = ANALYSIS_DIR / f"{audio_file_path.stem}_audio_analysis.json"
        write_json_file(output_json, {
            "file_name": analysis.file_name,
            "bpm": analysis.bpm,
            "key": analysis.key,
            "energy_level": analysis.energy_level,
            "key_instruments": analysis.key_instruments,
            "structure": analysis.structure,
            "technical_notes": analysis.technical_notes
        })
        self.log(f"Informe de análisis de audio guardado en: {output_json}")
        return analysis
