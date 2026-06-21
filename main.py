from fastapi import FastAPI
from pydantic import BaseModel
import os
import httpx

app = FastAPI()

# Load Groq variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = os.getenv("GROQ_API_URL")

class BuildRequest(BaseModel):
    prompt: str
    project_type: str = "python-script"

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "AI App Builder backend is running."
    }

@app.get("/test")
def test():
    return {"message": "Backend is alive!"}

@app.post("/echo")
def echo(data: dict):
    return {"you_sent": data}

@app.post("/project/create")
def create_project(data: dict):
    return {
        "status": "created",
        "project_id": "proj_12345",
        "name": data.get("name", "Untitled Project"),
        "project_type": data.get("project_type", "unknown")
    }

@app.get("/project/status/{project_id}")
def project_status(project_id: str):
    return {
        "project_id": project_id,
        "status": "ready",
        "message": "Project is initialized and ready."
    }

@app.get("/projects")
def list_projects():
    return {
        "projects": [
            {"id": "proj_12345", "name": "My First App"},
            {"id": "proj_67890", "name": "Weather App"},
        ]
    }

@app.delete("/project/{project_id}")
def delete_project(project_id: str):
    return {
        "status": "deleted",
        "project_id": project_id
    }

# REAL AI endpoint
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
            {"role": "system", "content": f"You generate {project_type} app code."},
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
        return {
            "status": "groq_error",
            "details": out
        }

    if "choices" not in out:
        return {
            "status": "unexpected_groq_response",
            "details": out
        }

    return {
        "status": "ok",
        "prompt": prompt,
        "project_type": project_type,
        "generated_code": out["choices"][0]["message"]["content"]
    }
