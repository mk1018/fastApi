from typing import Optional
from pydantic import BaseModel, Field

class ChatBase(BaseModel):
    message: Optional[str] = Field(None, example="テストチャット")

class ChatCreate(ChatBase):
    pass

class ChatCreateResponse(ChatCreate):
    id: int

    class Config:
        orm_mode = True
        
class Chat(ChatBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True