from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BuildRequest(BaseModel):
    prompt: str
    project_type: str = "python-script"

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "AI App Builder backend is running."
    }

@app.post("/build")
def build_project(req: BuildRequest):
    return {
        "status": "received",
        "prompt": req.prompt,
        "project_type": req.project_type,
        "message": "Backend is wired up. Code generation logic comes next."
    }
@app.get("/test")
def test():
    return {"message": "Backend is alive!"}
