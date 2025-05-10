from elevenlabs import save
from elevenlabs.client import ElevenLabs
from playsound import playsound

client = ElevenLabs(
  api_key="sk_d9959509b80a843fcf8baf8fcf1c691da818dadec9274c47", # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
  text="This is the beginning of the Copycat Project, where I repeat whatever you say.",
  voice="Daniel",
)

save(audio, "output.mp3")
playsound("output.mp3")