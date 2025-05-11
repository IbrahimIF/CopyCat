import pyaudio
import wave
import time

import speech_recognition as sr

from elevenlabs import save
from elevenlabs.client import ElevenLabs
from playsound import playsound


def recordAudio():
  FORMAT = pyaudio.paInt16
  CHANNELS = 1
  RATE = 44100
  CHUNK = 1024
  OUTPUT_FILENAME = "recordFile.wav"

  audio = pyaudio.PyAudio()
  stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
  )

  print("recording start")
  frames = []
  seconds = 6

  for i in range(0, int(RATE / CHUNK * seconds)):    
    data = stream.read(CHUNK)
    frames.append(data)

  print("recording stopped")
  
  stream.stop_stream()
  stream.close()
  audio.terminate()
  
  wf = wave.open(OUTPUT_FILENAME, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(audio.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(b''.join(frames))
  wf.close()



def micToText():
  """Process the recorded audio"""
  print("Processing audio...")
  try:
      with sr.AudioFile('recordFile.wav') as source:
            r = sr.Recognizer()
            r.energy_threshold = 5000
            r.pause_threshold = 2.0
                
            print("Listening...")
            audio = r.listen(source)
                
            print("Processing audio...")
            
            said = r.recognize_google(audio)
            print("Full transcript:", said)
            return said.lower()
  except Exception as e:
      print(e)
      print("Google didn't understand.")
      return "none"


def processText():
  text = micToText()
  if text == "none":
        return "silence."
  elif "copy" in text:
        return "Ok I won't then."
  else:
        return text

def textToSpeech():
  print("test")
  text = processText()
  client = ElevenLabs(
    api_key="sk_d9959509b80a843fcf8baf8fcf1c691da818dadec9274c47", # Defaults to ELEVEN_API_KEY
  )
  
  audio = client.generate(
    text=text+".",
    voice="Brian",
  )

  
  save(audio, "output.mp3")
  playsound("output.mp3")




recordAudio()
textToSpeech()