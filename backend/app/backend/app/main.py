from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os


from .agents import run_agent


app = FastAPI(title="AI Business Agent")


class ChatRequest(BaseModel):
user_id: str
prompt: str


@app.get("/ping")
async def ping():
return {"ok": True}


@app.post("/api/chat")
async def chat(req: ChatRequest):
# Simple pass-through to the agent wrapper
try:
reply = run_agent(req.prompt, user_id=req.user_id)
return {"reply": reply}
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))
