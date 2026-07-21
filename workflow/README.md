# Music Producer AI - Context

## Objetivo
Crear una IA que NO genere música, sino que actúe como productor musical personal y genere prompts optimizados para Suno.

## Conclusiones
- No entrenar un modelo.
- Analizar 20 canciones propias.
- Analizar canciones de influencia.
- Construir un Music DNA Profile.
- Usar Suno para generar el audio final.

## Agentes
- Music Director
- Audio Analyst
- Style Analyst
- Lyric Analyst
- Prompt Engineer
- Critic

## Flujo
Canciones + Influencias -> Análisis -> Perfil Musical -> Prompt -> Suno.

## Stack propuesto
- Next.js
- Java Spring Boot o FastAPI
- PostgreSQL/MySQL
- ChromaDB/Qdrant (opcional)
- Librosa
- Whisper
- Gemini Pro
- Docker

## Estructura
music-ai/
  knowledge/
  songs/propias
  songs/influencias
  analysis/
  prompts/

## Próximos pasos
1. Diseñar formato del Music DNA.
2. Crear pipeline de análisis.
3. Crear agentes.
4. Integrar Suno.
