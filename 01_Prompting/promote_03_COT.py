from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #reading the .env file and loading the environment variables

client = OpenAI(
    api_key="AIzaSyDoOJYcfyWXa1VYMrpvbN1F34TmgdENlJ8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You're an expert AI assistant in resolving user queries using chain of thought.
You work on START, PLAN and  OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strintly follow the given JSON output format.
- Only run one step at a time in the PLAN and wait for the output before running the next step.

Output JSON format:
{"step":"START" | "PLAN" | "OUTPUT", "content":"string"}

Exmaple:
START: hey , can you solve 2+3*/10
PLAN: {step: "PLAN", content: "First I will solve the multiplication part 3*10 and then I will add 2 to it"}
PLAN: {step: "PLAN", content: "The output of multiplication is 30. Now I will add 2 to it"}
PLAN: {step: "PLAN", content: "The output of addition is 32. This is the final output"}
PLAN: {step: "PLAN", content: "The final answer is 32"}
OUTPUT: {step: "OUTPUT", content: "The final answer is 32"}
 """


response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Who is the rock"}
    ]
)

print(response.choices[0].message.content)