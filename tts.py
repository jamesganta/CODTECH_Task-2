from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(text, lang='en', voice='en-us'):
  """
  Converts text to speech using Google Text-to-Speech.

  Args:
    text: The text to be converted to speech.
    lang: The language code for the output speech.
    voice: The voice code for the output speech.

  Returns:
    None
  """

  try:
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang)

    # Save the audio to a temporary file
    filename = "output.mp3"
    tts.save(filename)

    # Play the audio using playsound
    playsound(filename)

    # Remove the temporary file
    os.remove(filename)

  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  while True:
    text = input("Enter text: ")
    lang = input("Enter language code (e.g., en, es, fr): ")
    voice = input("Enter voice code (e.g., en-us, en-uk, es-es): ")

    text_to_speech(text, lang, voice)

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
      break