# Voicera Flask API (Play.ht-style)

Pure Python Flask API that exposes TTS endpoints similar to Play.ht style usage.
This starter returns a demo WAV (sine tone) or echoes a provided voice reference file.
Replace `tts/engine.py` with your real model (e.g., F5‑TTS).

## Endpoints
- `GET /health` → `{status: ok}`
- `GET /voices` (auth) → list of voices
- `POST /synthesize` (auth) → form-data: text, voice_id, voice (file). Returns audio/wav.

## Auth
- Header `x-api-key: YOUR_KEY` (set `API_KEY` env).

## CORS
- Set `ALLOWED_ORIGINS` env (default `*`).

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export API_KEY=change-me-please
python main.py
```

## Deploy (Render.com quick)
1. Push this folder to a Git repo.
2. Create a new **Web Service** on Render → Runtime: Python → Start Command: `gunicorn wsgi:app -w 2 -k gthread -b 0.0.0.0:$PORT`
3. Add Env Vars:
   - `API_KEY` = your-strong-key
   - `ALLOWED_ORIGINS` = https://stylentrade.com,https://www.stylentrade.com
4. Deploy → Note the URL (e.g., `https://voicera-api.onrender.com`).

## Example cURL
```bash
curl -X POST "https://YOUR-API/synthesize"  -H "x-api-key: YOUR_KEY"  -F "text=Hello from Voicera"  -F "voice_id=neutral_female"  -F "voice=@/path/to/ref.wav"  --output out.wav
```
