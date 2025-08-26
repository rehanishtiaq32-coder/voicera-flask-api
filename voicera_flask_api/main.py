from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from auth import require_api_key
from tts.engine import TtsEngine
from storage.local import save_upload
import os, uuid
from config import ALLOWED_ORIGINS, UPLOAD_DIR

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ALLOWED_ORIGINS}})

engine = TtsEngine()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/voices")
@require_api_key
def voices():
    # Static demo voices. Extend as needed.
    return {"voices": [
        {"id": "neutral_female", "name": "Neutral Female"},
        {"id": "neutral_male", "name": "Neutral Male"}
    ]}

@app.post("/synthesize")
@require_api_key
def synthesize():
    text = request.form.get("text") or ""
    voice_id = request.form.get("voice_id")
    ref = request.files.get("voice")
    ref_path = None
    if ref:
        filename = f"{uuid.uuid4().hex}_{ref.filename}"
        temp_path = os.path.join(UPLOAD_DIR, filename)
        ref.save(temp_path)
        ref_path = temp_path

    out_path = engine.synthesize(text=text, voice_ref_path=ref_path, voice_id=voice_id)
    return send_file(out_path, mimetype="audio/wav", as_attachment=True, download_name="voicera.wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
