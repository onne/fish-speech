# Fish Speech TTS Engine (OpenAudio)

This directory contains the Python backend for the Fish Speech v1.5 TTS engine (also known as OpenAudio).

## Architecture
- **Shared Infrastructure:** Uses `python_shared/tts_server` for FastAPI/CORS/Routing.
- `server.py`: Implementation of `BaseTTSServer`.
- `tools/api_server.py`: Main API server implementation (legacy/upstream).
- `checkpoints/openaudio-s1-mini/`: Model weights.

## Maintenance Notes
- **Process Management:** The server is managed by the Next.js `ProcessManager`. It is started via `uv run server.py`.
- **Port:** `8883`
- **Dependencies:** Managed via `pyproject.toml`. Use `uv` for all package operations.
- **Device:** Automatically detects MPS (Apple Silicon) or falls back to CPU.

## API Endpoint
(Inherited from `BaseTTSServer` but may map to internal `v1/tts`)

```
POST http://localhost:8883/v1/audio/speech
Content-Type: application/json

{
  "input": "Hello world",
  "voice": "default",
  "speed": 1.0
}
```

## Features
- Zero-shot and few-shot voice cloning via reference audio
- Multilingual support (English, Chinese, Japanese, and more)
- High-quality natural speech synthesis

## Troubleshooting
- If the server fails to start, check if port 8883 is occupied.
- Ensure `uv` is installed and the venv is created.
- Model files must be downloaded from Hugging Face (requires authentication).
- First startup takes 2-5 minutes for model loading and warm-up.
