from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["AI"])

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_agent(request: ChatRequest):
    return {"reply": f"Processing your request about: {request.message}"}

@router.get("/status")
async def ai_status():
    return {"status": "AI Agent is online"}
