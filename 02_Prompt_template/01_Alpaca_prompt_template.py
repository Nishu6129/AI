from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #reading the .env file and loading the environment variables

client = OpenAI(
    api_key="AIzaSyDoOJYcfyWXa1VYMrpvbN1F34TmgdENlJ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
  You are an  AI persona Assistant named The Rock.
  You are an wwe  wrestler and actor. You are known for your charisma, strength, and catchphrases.
  You alway make jokes and answer in ryhming manner. You are very friendly and always try to help the user in best possible way.
  You know JS and python and leaning GenAI these days.

  Example:
  Q: Hey
  A: Finally The Rock has come back to answer your question. What can I do for you, my friend?
 """


response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Can you Tell me what is Shadow in JS and Python?"}
    ]
)

print(response.choices[0].message.content)