from fastapi import FastAPI
from pydantic import BaseModel
import openai

openai.api_key = "YOUR_API_KEY_HERE"

app = FastAPI()

class ChatInput(BaseModel):
    message: str

SYSTEM_PROMPT = """
You are an expert analog IC design engineer.
You reason using device physics, gm/Id methodology, and small-signal models.

Always respond in this format:

ARCHITECTURE:
DIAGNOSIS:
ACTIONS:
RISKS:
"""

@app.post("/chat")
def chat(inp: ChatInput):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": inp.message}
        ]
    )
    return {"reply": response.choices[0].message.content}
