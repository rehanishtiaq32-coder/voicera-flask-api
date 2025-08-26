# Simple placeholder TTS engine.
# Replace with your real model (e.g., F5-TTS) later.

import os, wave, struct, math, time

class TtsEngine:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def synthesize(self, text: str, voice_ref_path: str | None = None, voice_id: str | None = None) -> str:
        # If we have a voice reference, simply return it as a "demo" result.
        if voice_ref_path and os.path.exists(voice_ref_path):
            # In real system: run cloning here and write to out_path.
            return voice_ref_path

        # Otherwise, generate a simple sine tone WAV proportional to text length.
        duration_sec = max(1.0, min(10.0, len(text) / 20.0)) if text else 2.0
        sample_rate = 16000
        freq = 440.0
        num_samples = int(duration_sec * sample_rate)
        out_path = os.path.join(self.output_dir, f"voicera_{int(time.time()*1000)}.wav")

        with wave.open(out_path, 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            for i in range(num_samples):
                value = int(32767.0 * 0.2 * math.sin(2.0 * math.pi * freq * (i / sample_rate)))
                wf.writeframesraw(struct.pack('<h', value))

        return out_path
