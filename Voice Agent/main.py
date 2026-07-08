
from http import client
import asyncio
from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI
from openai import AsyncOpenAI
from openai.helper import LocalAudioPlayer

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

async_client = AsyncOpenAI()

async def tts(speech :str):
    response = await async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        intstructions="You are a helpful assistant that can convert text to speech.",
        input=speech,
        response_format="pcm"
    )as response:
    await LocalAudioPlayer.play_streaming(response)

def main():

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak now!")
        
        SYSTEM_PROMPT = f"""
            You're an expert voice agent that can transcribe audio and provide relevant information based on the transcribed text. Please provide a detailed response or action based on this input.
            """

        messages = []
        
        while True:
            # Capture the audio
            audio_data = recognizer.listen(source)
            print("Recognizing...")

            try:
                #STT
                # Transcribe audio using Google Speech Recognition
                text = recognizer.recognize_google(audio_data)
                print(f"You said: {text}")
                messages.append({"role": "user", "content": text})
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages
                )
                

                print("AI response:", response.choices[0].message.content)
                asyncio.run(tts(response.choices[0].message.content))  # Call the TTS function to convert the response to speech

                #TTS text to speech
                
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from the service; {e}")
