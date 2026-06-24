from fastapi import FastAPI, Body
from ollama import Client, Ollama

app = FastAPI()

client = Client(
    base_url="http://localhost:11434",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact-us")
def read_contact():
    return {"Contact": "abc@gmail.com"}


@app.post("/chat")
def chat_with_model(message: str = Body(..., embed=True)):
    response = client.chat.completions.create(
        model="llama-2-7b-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return {"response": response.choices[0].message.content}
