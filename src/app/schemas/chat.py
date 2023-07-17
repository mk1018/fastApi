from pydantic import BaseModel

class ChatInput(BaseModel):
    prompt: str
    
    def get_prompt(self):
        return self.prompt