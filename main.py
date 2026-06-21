# 
#  FILE: main.py
#  PURPOSE: FastAPI backend for Groq-powered AI App Builder and command console
#  AUTO-GENERATED: No
#  PROTECTED: Yes
#  LAST UPDATED: 06/21/2026 12:55 PM EDT
#  VERSION: 1.0.0
#

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import os
import httpx

app = FastAPI()

# Load Groq variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = os.getenv("GROQ_API_URL")

SYSTEM_PROMPT = """
You are a highly accurate, code‑oriented AI assistant. 
Your priorities are correctness, clarity, and clean structure.

Rules:
1. Always respond with clean, well‑formatted code when the user asks for anything technical.
2. Keep explanations short, structured, and never ramble.
3. Never produce run‑on sentences.
4. Never invent APIs or functions. If unsure, ask.
5. Prefer step‑by‑step logic.
6. Use headings, bullet points, and code blocks.
7. When generating code, include only what is necessary.
8. Never output broken or partial code.
9. If the user asks for something unclear, request clarification.
10. Always behave like a senior software engineer.

Always format your responses using this structure:

## Summary
A 1–2 sentence explanation of what you are doing.

## Code
The complete code solution in a single code block.

## Notes
Any important details or limitations.

Default to code‑first responses.
Use a confident, direct, helpful tone.
Avoid filler language.
Avoid generic phrases.
Be concise and practical.
"""

class BuildRequest(BaseModel):
    prompt: str
    project_type: str = "python-script"

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "AI App Builder backend is running."
    }

@app.get("/chat")
def chat_page():
    return FileResponse("chat.html")

@app.post("/project/generate")
async def generate_code(data: dict):
    prompt = data.get("prompt", "")
    project_type = data.get("project_type", "unknown")

    if not GROQ_API_KEY or not GROQ_API_URL:
        return {
            "status": "error",
            "message": "Missing GROQ_API_KEY or GROQ_API_URL"
        }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(GROQ_API_URL, json=payload, headers=headers)
        out = resp.json()

    if "error" in out:
        return {"status": "groq_error", "details": out}

    if "choices" not in out:
        return {"status": "unexpected_groq_response", "details": out}

    return {
        "status": "ok",
        "prompt": prompt,
        "project_type": project_type,
        "generated_code": out["choices"][0]["message"]["content"]
    }

# END OF main.py (147 lines)