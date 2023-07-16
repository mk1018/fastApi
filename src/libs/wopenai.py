import openai
from enum import Enum
from pydantic import BaseModel

HYPER_PARAMETERS = {
    "temperature": 0.7,
    # "max_tokens": 60,
    # "top_k": 40,
    "top_p": 0.9,
    "length_penalty": 1.0,
    # "frequency_penalty": 0.5,
    "presence_penalty": 1.0
}

class Model(Enum):
    GPT_35_TURBO = 'gpt-3.5-turbo'
    GPT_35_TURBO_16k = 'gpt-3.5-turbo-16k'
    GPT_4 = 'gpt-4'

class Role(Enum):
    SYSTEM = "system"
    USER = "user"

class OpenAIMessage(BaseModel):
    role: Role
    content: str

    def __init__(self, role: Role, content: str) -> None:
        self.role = role
        self.content = content

    def message(self) -> dict[str, str]:
        return {"role": self.role.value, "content": self.content}
    
class OpenAIMessages(BaseModel):
    _messages: list[OpenAIMessage]
    _api_key: str

    def __init__(self, api_key: str):
        self._api_key = api_key

    def api_key(self):
        return self._api_key

    def add_message(self, message: OpenAIMessage):
        self._messages.append(message)

    def to_dict(self) -> list[dict[str, str]]:
        return [msg.message() for msg in self._messages]
    
class OpenAIResponse(BaseModel):
    _response: any

    def __init__(self, response) -> None:
        self._response = response 

    def response(self) -> any:
        return self._response

async def asend(model: Model, messages: OpenAIMessages, stream: bool=True) -> OpenAIResponse:
    response = await openai.ChatCompletion.acreate(
        api_key=messages.api_key(),
        model=model.value,
        messages=messages.to_dict(),
        stream=stream,
        top_p=HYPER_PARAMETERS['top_p'],
        temperature=HYPER_PARAMETERS['temperature'],
        presence_penalty=HYPER_PARAMETERS['presence_penalty'],
    )
    return OpenAIResponse(response)