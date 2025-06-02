<div align="center">
 
# CopyCat

</div>


![Project Status](https://img.shields.io/badge/status-in_progress-Green)

![Static Badge](https://img.shields.io/badge/made_with-python-blue)

#### **Description**:
A simple Python project that listens to your microphone, processes the speech, and responds using Text-to-Speech (TTS).
CopyCat records audio from your microphone, converts it to text, processes the text (with special responses to phrases like "copy"), and generates a spoken reply using ElevenLabs' TTS API.

----
## Getting started:


### Prerequisites
1. **Python 3.10+**
2. **FFmpeg** (Required for audio processing)
```
   - Install via:
     - macOS: `brew install ffmpeg`
     - Linux: `sudo apt install ffmpeg`
     - Windows: Download from [FFmpeg's official site](https://ffmpeg.org/)
```

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/CopyCat.git
cd CopyCat
```

2. Install dependencies:
```bash

pip install -r requirements.txt
```
3. Add your ElevenLabs API key to a .env file:
```
ELEVENLABS_API_KEY=your_api_key_here
```
-----
## Features:

This project includes several exciting features for you to explore:

- **Microphone recording**: Real-time microphone recording (6-second clips).
- **Speech-to-text conversion**: Speech-to-text conversion via Google's Speech Recognition.
- **Smart text processing**: Copies what you say and provides special responses based on your input (e.g., replies "Ok I won't then" if you say "copy").
- **TTS Responses**: Natural-sounding TTS responses using ElevenLabs.
- **Automatic responses**: Plays responses aloud automatically.


----
## Technologies and Tools Utilised:

![My Skills](https://go-skill-icons.vercel.app/api/icons?i=python,vscode&perline=2)

-----
## Acknowledgment:
- [ElevenLabs](https://elevenlabs.io/)
- [Google Speech Recognition](https://cloud.google.com/speech-to-text)
- [FFmpeg](https://ffmpeg.org/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
- [Speech Recognition](https://pypi.org/project/SpeechRecognition/)
- [playsound](https://github.com/TaylorSMarks/playsound)

- [My other project (Discord-Mute-Yourself)](https://github.com/IbrahimIF/Discord-Mute-Yourself)
