import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import cohere
from faster_whisper import WhisperModel
from gtts import gTTS
import os

# Step 1 - Record Audio
def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎙️ Recording for", duration, "seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, fs, audio)
    print("✅ Recording saved as", filename)

# Step 2 - Transcribe Audio
def transcribe_audio(filename="input.wav"):
    print("🔍 Transcribing audio...")
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, info = model.transcribe(filename)
    text = "".join([segment.text for segment in segments])
    print("📝 You said:", text)
    return text.strip()

# Step 3 - Generate AI Response from Cohere
def get_ai_response(prompt, api_key):
    print("🧠 Generating response...")
    co = cohere.Client(api_key)
    response = co.chat(
        message=prompt,
        model="command-r7b-arabic-02-2025"
    )
    reply = response.text.strip()
    print("🤖 AI says:", reply)
    return reply


# Step 4 - Speak Response
def speak(text):
    print("🔊 Speaking...")
    tts = gTTS(text, lang='ar')  # Use lang='ar' for Arabic
    tts.save("response.mp3")
    os.system("start response.mp3")  # or "afplay" for Mac, "xdg-open" for Linux

# Main Execution
if __name__ == "__main__":
    COHERE_API_KEY = "" 

    record_audio()
    user_text = transcribe_audio()
    ai_reply = get_ai_response(user_text, COHERE_API_KEY)
    speak(ai_reply)
