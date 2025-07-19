# 🧠🎙️ AI Voice Assistant with Whisper, Cohere, and TTS

This is a simple voice assistant built using Python that:
1. Records your voice input
2. Transcribes it to text using Whisper
3. Sends the text to Cohere's language model for a response (supports Arabic!)
4. Converts the response back to speech and plays it directly

---

## 📦 Requirements

- Python 3.10+
- Anaconda (optional but recommended)
- VS Code (optional for editing)

---

💻 How It Works
The assistant records 5 seconds of your voice.

It transcribes the audio using faster-whisper (runs offline on CPU).

The text is sent to Cohere’s chat() endpoint using the command-r7b-arabic-02-2025 model.

The assistant replies and plays the audio using gTTS and playsound.

Supports both Arabic and English seamlessly.

