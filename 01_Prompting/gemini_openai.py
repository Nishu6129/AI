from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #reading the .env file and loading the environment variables

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role":"system","content":"You are a rude person only give rude reply."},
        {"role":"user","content":"Hey There"}
    ]
)

print(response.choices[0].message.content)
