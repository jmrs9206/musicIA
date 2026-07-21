#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from src.agents import (
    MusicDirectorAgent,
    AudioAnalystAgent,
    StyleAnalystAgent,
    LyricAnalystAgent,
    PromptEngineerAgent,
    CriticAgent
)
from src.config import SONGS_PROPIAS_DIR, SONGS_REFERENCIAS_DIR

def print_banner():
    banner = """
  ███╗   ███╗██   ██║███████╗██║██████╗   █████╗ 
  ████╗ ████║██║   ██║██╔════╝██║██╔════╝  ██╔══██╗
  ██╔████╔██║██║   ██║███████╗██║██║       ███████║
  ██║╚██╔╝██║██║   ██║╚════██║██║██║       ██╔══██║
  ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗ ██║  ██║
  ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝
  -- Orquestador de Producción Musical e Inteligencia de Prompts Suno AI --
    """
    print(banner)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="MusicIA - Sistema de Productores y Prompting para Suno AI")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")
    
    # Comando 1: generate-prompt
    prompt_parser = subparsers.add_parser("generate-prompt", help="Generar un prompt optimizado para Suno AI")
    prompt_parser.add_argument("--idea", type=str, required=True, help="Idea o concepto de la canción")
    prompt_parser.add_argument("--bpm", type=int, help="BPM específico (opcional)")
    prompt_parser.add_argument("--genre", type=str, help="Género específico (opcional)")
    
    # Comando 2: analyze-song
    analyze_parser = subparsers.add_parser("analyze-song", help="Ejecutar análisis de audio, estilo y lírica en una canción")
    analyze_parser.add_argument("--file", type=str, required=True, help="Ruta o nombre del archivo MP3/WAV")
    analyze_parser.add_argument("--title", type=str, default="Demo Track", help="Título de la canción")
    
    # Comando 3: build-dna
    dna_parser = subparsers.add_parser("build-dna", help="Consolidar el perfil Music DNA Profile desde la Base de Conocimiento")
    
    # Comando 4: evaluate-track
    eval_parser = subparsers.add_parser("evaluate-track", help="Evaluar una canción generada por Suno contra tu identidad")
    eval_parser.add_argument("--title", type=str, required=True, help="Título de la canción generada")
    eval_parser.add_argument("--feedback", type=str, default="", help="Notas u observaciones de escucha")

    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
        
    director = MusicDirectorAgent()
    
    if args.command == "build-dna":
        print("\n--- Ejecutando Music Director Agent ---")
        dna = director.run()
        print("\n[ÉXITO] Perfil Music DNA Profile consolidado exitosamente:")
        print(f" - Artista: {dna.artist_name}")
        print(f" - Géneros: {', '.join(dna.primary_genres)}")
        print(f" - Instrumentos clave: {', '.join(dna.signature_instruments)}")
        print(f" - Palabras clave Suno: {', '.join(dna.suno_style_keywords)}")

    elif args.command == "generate-prompt":
        print("\n--- Ejecutando Flujo de Generación de Prompt Suno ---")
        dna = director.run()
        prompt_agent = PromptEngineerAgent()
        suno_prompt = prompt_agent.run(
            user_idea=args.idea,
            dna_profile=dna,
            override_bpm=args.bpm,
            custom_genre=args.genre
        )
        
        print("\n" + "="*60)
        print(f"🎵 PROMPT GENERADO PARA SUNO AI: '{suno_prompt.title}'")
        print("="*60)
        print(f"\n📌 STYLE PROMPT (Longitud: {len(suno_prompt.style_prompt)} / 120 caracteres):\n")
        print(f"   {suno_prompt.style_prompt}")
        print("\n" + "-"*60)
        print("📝 LYRICS & METATAGS:\n")
        print(suno_prompt.lyrics)
        print("="*60)

    elif args.command == "analyze-song":
        print("\n--- Ejecutando Red de Agentes Analistas ---")
        audio_path = Path(args.file)
        
        audio_agent = AudioAnalystAgent()
        style_agent = StyleAnalystAgent()
        lyric_agent = LyricAnalystAgent()
        
        audio_res = audio_agent.run(audio_file_path=audio_path)
        style_res = style_agent.run(track_name=args.title)
        lyric_res = lyric_agent.run(lyrics_text="", song_title=args.title)
        
        print("\n[ÉXITO] Análisis completados por la red de agentes:")
        print(f" - BPM detectado: {audio_res.bpm}")
        print(f" - Tonalidad: {audio_res.key}")
        print(f" - Género: {style_res.primary_genre}")
        print(f" - Atmósfera: {style_res.atmosphere}")
        print(f" - Tema lírico: {lyric_res.theme}")

    elif args.command == "evaluate-track":
        print("\n--- Ejecutando Critic Agent ---")
        dna = director.run()
        critic = CriticAgent()
        report = critic.run(
            track_title=args.title,
            dna_profile=dna,
            feedback_notes=args.feedback
        )
        print("\n" + "="*60)
        print(f"📊 INFORME DE EVALUACIÓN CRITIC AGENT: '{report.track_title}'")
        print("="*60)
        print(f" - Score de Alineación: {report.alignment_score} / 10.0")
        print(f" - Veredicto: {report.verdict}")
        print("\n[PUNTOS FUERTES]:")
        for s in report.strengths:
            print(f"  ✓ {s}")
        print("\n[DIVERGENCIAS DETECTADAS]:")
        for d in report.divergences:
            print(f"  ⚠ {d}")
        print("\n[RECOMENDACIONES PARA EL PRÓXIMO PROMPT SUNO]:")
        for r in report.recommendations_for_suno:
            print(f"  💡 {r}")
        print("="*60)

if __name__ == "__main__":
    main()
