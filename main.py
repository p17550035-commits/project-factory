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
    @app.post("/project/generate")
def generate_code(data: dict):
    return {
        "status": "processing",
        "prompt": data.get("prompt"),
        "message": "Code generation started."
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
