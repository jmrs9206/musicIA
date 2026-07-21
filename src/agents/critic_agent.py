from pathlib import Path
from src.agents.base_agent import BaseAgent
from src.models import EvaluationReport, MusicDNAProfile
from src.utils.file_helpers import write_json_file
from src.config import ANALYSIS_DIR

class CriticAgent(BaseAgent):
    """
    Agente 6: Critic Agent
    Evalúa si la canción generada por Suno sigue tu estilo y alineación con el Music DNA.
    """
    def __init__(self):
        super().__init__(
            name="CriticAgent",
            role_description="Evalúa si la canción generada sigue tu estilo y propone refinamientos para Suno."
        )

    def run(
        self,
        track_title: str,
        dna_profile: MusicDNAProfile,
        feedback_notes: str = ""
    ) -> EvaluationReport:
        self.log(f"Evaluando canción generada en Suno: '{track_title}' contra el perfil Music DNA...")
        
        # Simulación de evaluación basada en criterios de coincidencia de estilo
        alignment_score = 8.5
        strengths = [
            "Coincidencia excelente en el tempo y la instrumentación acústica/analógica",
            "La voz mantiene un tono íntimo y emotivo respetando el estilo vocal",
            "La estructura con metatags Suno ([Intro], [Chorus]) fue interpretada correctamente"
        ]
        divergences = [
            "El estribillo final fue un poco más producido de lo deseado para la atmósfera analógica cálida"
        ]
        recommendations = [
            "En el próximo prompt para Suno, añade el tag 'warm tape saturation, lo-fi production' en el Style Prompt",
            "Mantener el tempo entre 90 y 105 BPM para preservar la nostalgia del track"
        ]
        
        report = EvaluationReport(
            track_title=track_title,
            alignment_score=alignment_score,
            strengths=strengths,
            divergences=divergences,
            recommendations_for_suno=recommendations,
            verdict="APPROVED" if alignment_score >= 8.0 else "NEEDS_REFINEMENT"
        )
        
        output_file = ANALYSIS_DIR / f"{track_title.lower().replace(' ', '_')}_critic_evaluation.json"
        write_json_file(output_file, {
            "track_title": report.track_title,
            "alignment_score": report.alignment_score,
            "verdict": report.verdict,
            "strengths": report.strengths,
            "divergences": report.divergences,
            "recommendations": report.recommendations_for_suno,
            "feedback_notes": feedback_notes
        })
        
        self.log(f"Evaluación del Critic Agent completada. Score: {alignment_score}/10. Veredicto: {report.verdict}")
        self.log(f"Informe de evaluación guardado en: {output_file}")
        return report
