from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI(title="AIRA - AI Agent Assistant")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = agent.run(req.message)
    return {"response": response}

@app.get("/")
def root():
    return {"status": "AIRA AI Agent is running"}
