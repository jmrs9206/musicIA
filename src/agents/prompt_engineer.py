from pathlib import Path
from typing import Optional, List
from src.agents.base_agent import BaseAgent
from src.models import MusicDNAProfile, SunoPrompt
from src.utils.suno_formatter import optimize_style_prompt, format_suno_lyrics
from src.utils.file_helpers import write_json_file
from src.config import PROMPTS_HISTORICO_DIR, SUNO_MAX_STYLE_LENGTH

class PromptEngineerAgent(BaseAgent):
    """
    Agente 5: Prompt Engineer Agent
    Convierte tu idea en un prompt optimizado y profesional para Suno AI.
    """
    def __init__(self):
        super().__init__(
            name="PromptEngineer",
            role_description="Convierte ideas y el Music DNA Profile en prompts optimizados para Suno AI (<120 chars style, metatags)."
        )

    def run(
        self,
        user_idea: str,
        dna_profile: MusicDNAProfile,
        override_bpm: Optional[int] = None,
        custom_genre: Optional[str] = None
    ) -> SunoPrompt:
        self.log(f"Generando prompt optimizado para Suno a partir de la idea: '{user_idea}'")
        
        # Build style tags
        genre = custom_genre or (dna_profile.primary_genres[0] if dna_profile.primary_genres else "Indie Rock")
        bpm = override_bpm or 100
        
        tags = [
            genre,
            f"{bpm} bpm",
            dna_profile.signature_instruments[0] if dna_profile.signature_instruments else "acoustic guitar",
            dna_profile.signature_instruments[1] if len(dna_profile.signature_instruments) > 1 else "analog synth",
            dna_profile.signature_atmospheres[0] if dna_profile.signature_atmospheres else "melancholic",
            "intimate raw vocals"
        ]
        
        # Format style prompt ensuring <= 120 chars
        style_prompt = optimize_style_prompt(tags)
        
        # Sample lyrics structure with Suno metatags
        verses = [
            f"Camino por las calles cuando cae la noche,\nla ciudad susurra historias que olvidé.\n{user_idea} en cada esquina,\nbuscando las respuestas que nunca encontré.",
            f"Las luces parpadean en el horizonte,\nel viento trae el eco de tu voz.\nGuardamos el secreto bajo la lluvia,\nmientras el tiempo pasa entre los dos."
        ]
        chorus = f"Y es aquí, en esta calma,\ndonde resuena nuestra canción.\n{user_idea},\nel palpitar de este corazón."
        bridge = "Y aunque la tormenta vuelva a empezar,\nsabemos exactamente hacia dónde caminar."
        
        lyrics = format_suno_lyrics(
            verses=verses,
            chorus=chorus,
            intro="Guitarra acústica suave con sintetizador analógico de fondo",
            bridge=bridge,
            outro="Desvanecimiento suave con solo de guitarra y ecos vocales"
        )
        
        title = f"Canción - {user_idea[:25].title()}"
        
        suno_prompt = SunoPrompt(
            title=title,
            style_prompt=style_prompt,
            lyrics=lyrics,
            concept_explanation=f"Prompt optimizado para Suno basado en la identidad de {dna_profile.artist_name} e idea '{user_idea}'.",
            tags=tags
        )
        
        # Save prompt to history
        file_name = title.lower().replace(" ", "_").replace("-", "").strip("_") + ".json"
        history_file = PROMPTS_HISTORICO_DIR / file_name
        write_json_file(history_file, {
            "title": suno_prompt.title,
            "style_prompt": suno_prompt.style_prompt,
            "style_prompt_length": len(suno_prompt.style_prompt),
            "style_length_valid": len(suno_prompt.style_prompt) <= SUNO_MAX_STYLE_LENGTH,
            "lyrics": suno_prompt.lyrics,
            "concept_explanation": suno_prompt.concept_explanation,
            "tags": suno_prompt.tags
        })
        
        self.log(f"Prompt generado exitosamente! Longitud Style: {len(style_prompt)} caracteres.")
        self.log(f"Guardado en histórico: {history_file}")
        return suno_prompt
