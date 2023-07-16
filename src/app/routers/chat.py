from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.db import get_db, DbAsyncSession
from libs.wopenai import OpenAIResponse
from app.schemas.chat import ChatInput
import services.chat as schat

router = APIRouter()

@router.post("/chats")
async def chat(chat_input: ChatInput, db: DbAsyncSession = Depends(get_db)):
    response_stream: OpenAIResponse = await schat.chat(chat_input.get_prompt())
    # TODO: dbへ保存
    return StreamingResponse(response_stream.generate_response_stream())