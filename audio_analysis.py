import numpy as np
import librosa

def analyze_audio(audio_file):
    """ Convert audio to confidence score based on energy """
    try:
        y, sr = librosa.load(audio_file, sr=None)
        rms = np.mean(librosa.feature.rms(y=y))
        confidence = round(min(1.0, max(0.0, rms * 10)), 2)
        return confidence
    except Exception:
        return 0.6  # fallback
