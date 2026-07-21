from typing import List
from src.config import SUNO_MAX_STYLE_LENGTH, SUNO_MAX_LYRICS_LENGTH

def optimize_style_prompt(tags: List[str]) -> str:
    """
    Formats a list of music keywords into a Suno Style Prompt <= 120 chars.
    Deduplicates keywords and truncates intelligently if needed.
    """
    clean_tags = []
    seen = set()
    for tag in tags:
        tag_clean = tag.strip().lower()
        if tag_clean and tag_clean not in seen:
            seen.add(tag_clean)
            clean_tags.append(tag.strip())
            
    prompt = ", ".join(clean_tags)
    
    if len(prompt) > SUNO_MAX_STYLE_LENGTH:
        # Truncate at keyword boundaries
        words = prompt.split(", ")
        fitted = []
        current_len = 0
        for w in words:
            additional_len = len(w) + (2 if fitted else 0)
            if current_len + additional_len <= SUNO_MAX_STYLE_LENGTH:
                fitted.append(w)
                current_len += additional_len
            else:
                break
        prompt = ", ".join(fitted)
        
    return prompt

def format_suno_lyrics(
    verses: List[str],
    chorus: str,
    intro: str = "",
    bridge: str = "",
    outro: str = ""
) -> str:
    """
    Formats song sections into Suno-compliant lyrics with metatags.
    """
    sections = []
    
    if intro:
        sections.append(f"[Intro]\n{intro.strip()}")
    else:
        sections.append("[Intro]\n(Instrumental Fade-In)")
        
    for idx, verse in enumerate(verses, 1):
        sections.append(f"[Verse {idx}]\n{verse.strip()}")
        if chorus and idx == 1:
            sections.append(f"[Chorus]\n{chorus.strip()}")
            
    if bridge:
        sections.append(f"[Bridge]\n{bridge.strip()}")
        
    if chorus:
        sections.append(f"[Chorus]\n{chorus.strip()}")
        
    if outro:
        sections.append(f"[Outro]\n{outro.strip()}")
    else:
        sections.append("[Outro]\n[Fade Out]")
        
    full_lyrics = "\n\n".join(sections)
    
    if len(full_lyrics) > SUNO_MAX_LYRICS_LENGTH:
        full_lyrics = full_lyrics[:SUNO_MAX_LYRICS_LENGTH]
        
    return full_lyrics
