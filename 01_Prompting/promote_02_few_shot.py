from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #reading the .env file and loading the environment variables

client = OpenAI(
    api_key="AIzaSyDoOJYcfyWXa1VYMrpvbN1F34TmgdENlJ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """You should only and only answer the coding related questions. Do not answer to any other question and reply sorry I am not able to answer that.
 Rule:
 -Strictly follw the json the format
 {{
 "code": "string " or null",
 "iscodinquestion": "boolean"}}

 Question: What is the capital of India?
 Answer: {{"code": null, "iscodinquestion": false}}

 Question: How to reverse a string in python?
 Answer: {{"code": "string[::-1]", "iscodinquestion": true}}
 """


response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Who is the rock"}
    ]
)

print(response.choices[0].message.content)