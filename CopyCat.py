import pyaudio
import wave
import time
import keyboard
import speech_recognition as sr
import os
from dotenv import load_dotenv

from elevenlabs import save
from elevenlabs.client import ElevenLabs
from playsound import playsound

load_dotenv()

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
    api_key=os.getenv("ELEVENLABS_API_KEY")
  )
  
  audio = client.generate(
    text=text+".",
    voice="Brian",
  )

  
  save(audio, "output.mp3")
  playsound("output.mp3")




recordAudio()
textToSpeech()



"""
def conversation_loop():
    print("Starting conversation loop. Press SPACE to stop...")
    
    # Give user time to release spacebar if pressed before starting
    time.sleep(1)
    
    while True:
        # Full conversation cycle
        recordAudio()
        textToSpeech()
        
        # Check for spacebar press
        if keyboard.is_pressed('space'):
            print("\nSpacebar pressed - ending conversation")
            break
            
        # Small delay to prevent CPU overload
        time.sleep(0.1)

def main():
    try:
        conversation_loop()
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Cleaning up...")

if __name__ == "__main__":
    main()
"""

