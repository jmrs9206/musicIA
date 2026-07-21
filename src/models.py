from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any

@dataclass
class AudioAnalysis:
    file_name: str
    bpm: Optional[int] = None
    key: Optional[str] = None
    energy_level: str = "medium"  # low, medium, high, explosive
    time_signature: str = "4/4"
    key_instruments: List[str] = field(default_factory=list)
    structure: List[str] = field(default_factory=list)  # e.g. ["Intro", "Verse", "Chorus", ...]
    technical_notes: str = ""

@dataclass
class StyleAnalysis:
    primary_genre: str = ""
    subgenres: List[str] = field(default_factory=list)
    influences: List[str] = field(default_factory=list)
    atmosphere: str = ""
    production_characteristics: List[str] = field(default_factory=list)
    vocal_style: str = ""

@dataclass
class LyricAnalysis:
    theme: str = ""
    emotional_tone: str = ""
    narrative_structure: str = ""
    metaphor_types: List[str] = field(default_factory=list)
    rhythm_and_rhyme: str = ""
    key_phrases: List[str] = field(default_factory=list)

@dataclass
class MusicDNAProfile:
    artist_name: str = "Artista"
    primary_genres: List[str] = field(default_factory=list)
    signature_instruments: List[str] = field(default_factory=list)
    vocal_identity: str = ""
    preferred_bpm_range: Dict[str, int] = field(default_factory=lambda: {"min": 80, "max": 130})
    signature_atmospheres: List[str] = field(default_factory=list)
    lyric_themes: List[str] = field(default_factory=list)
    influences: List[str] = field(default_factory=list)
    suno_style_keywords: List[str] = field(default_factory=list)

@dataclass
class SunoPrompt:
    title: str
    style_prompt: str  # Must be <= 120 chars
    lyrics: str        # Structured lyrics with metatags like [Verse], [Chorus]
    concept_explanation: str = ""
    tags: List[str] = field(default_factory=list)

@dataclass
class EvaluationReport:
    track_title: str
    alignment_score: float  # 0.0 to 10.0
    strengths: List[str] = field(default_factory=list)
    divergences: List[str] = field(default_factory=list)
    recommendations_for_suno: List[str] = field(default_factory=list)
    verdict: str = "NEEDS_REFINEMENT"  # APPROVED, REJECTED, NEEDS_REFINEMENT
