from pydantic import BaseModel, Field

class ChatInput(BaseModel):
    prompt: str
    
    def get_prompt(self):
        return self.prompt