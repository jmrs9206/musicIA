from pathlib import Path
from typing import Optional, List
from src.agents.base_agent import BaseAgent
from src.models import MusicDNAProfile, AudioAnalysis, StyleAnalysis, LyricAnalysis
from src.utils.file_helpers import read_json_file, read_markdown_file, write_json_file, write_markdown_file
from src.config import IDENTITY_FILE, PREFERENCES_FILE, INFLUENCES_FILE, KNOWLEDGE_DIR

class MusicDirectorAgent(BaseAgent):
    """
    Agente 4: Music Director Agent
    Une todo y crea/mantiene tu identidad musical (Music DNA Profile).
    """
    def __init__(self):
        super().__init__(
            name="MusicDirector",
            role_description="Orquesta la red de agentes y construye/sintetiza el perfil de identidad Music DNA."
        )

    def load_knowledge_base(self) -> dict:
        identity_md = read_markdown_file(IDENTITY_FILE)
        preferences_json = read_json_file(PREFERENCES_FILE)
        influences_json = read_json_file(INFLUENCES_FILE)
        return {
            "identity_markdown": identity_md,
            "preferences": preferences_json,
            "influences": influences_json
        }

    def run(
        self,
        audio_analyses: Optional[List[AudioAnalysis]] = None,
        style_analyses: Optional[List[StyleAnalysis]] = None,
        lyric_analyses: Optional[List[LyricAnalysis]] = None
    ) -> MusicDNAProfile:
        self.log("Consolidando perfil de Identidad Musical (Music DNA Profile)...")
        kb = self.load_knowledge_base()
        
        # Default fallback preferences
        pref = kb.get("preferences", {})
        inf = kb.get("influences", {})
        
        bpm_min = pref.get("preferencias_generales", {}).get("bpm_rango", {}).get("min", 85)
        bpm_max = pref.get("preferencias_generales", {}).get("bpm_rango", {}).get("max", 130)
        
        primary_genres = ["Indie Rock", "Alternative Folk", "Synth Pop"]
        if style_analyses:
            primary_genres = list(set([s.primary_genre for s in style_analyses if s.primary_genre]))
            
        instruments = ["Acoustic Guitar", "Analog Synth", "Warm Bass", "Organic Drums"]
        if audio_analyses:
            combined_inst = []
            for a in audio_analyses:
                combined_inst.extend(a.key_instruments)
            if combined_inst:
                instruments = list(set(combined_inst))
                
        dna = MusicDNAProfile(
            artist_name="Creador MusicIA",
            primary_genres=primary_genres,
            signature_instruments=instruments,
            vocal_identity="Raw emotive vocals, intimate lead, layered backing harmonies",
            preferred_bpm_range={"min": bpm_min, "max": bpm_max},
            signature_atmospheres=["Melancholic", "Warm analog", "Atmospheric", "Nostalgic"],
            lyric_themes=["Introspección", "Narrativas nocturnas", "Búsqueda personal"],
            influences=["Radiohead", "Phoebe Bridgers", "Bon Iver", "The xx"],
            suno_style_keywords=[
                "indie rock", "warm acoustic guitar", "analog synth",
                "melancholic vibe", "intimate raw vocals", "tape saturation"
            ]
        )
        
        # Save consolidated JSON profile
        profile_json = KNOWLEDGE_DIR / "music_dna_profile.json"
        write_json_file(profile_json, {
            "artist_name": dna.artist_name,
            "primary_genres": dna.primary_genres,
            "signature_instruments": dna.signature_instruments,
            "vocal_identity": dna.vocal_identity,
            "preferred_bpm_range": dna.preferred_bpm_range,
            "signature_atmospheres": dna.signature_atmospheres,
            "lyric_themes": dna.lyric_themes,
            "influences": dna.influences,
            "suno_style_keywords": dna.suno_style_keywords
        })
        self.log(f"Perfil Music DNA guardado en: {profile_json}")
        return dna
