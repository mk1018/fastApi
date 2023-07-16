from pydantic import BaseModel, Field

class ChatInput(BaseModel):
    prompt: str