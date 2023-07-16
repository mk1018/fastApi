import openai, json
from enum import Enum
from typing import Any, AsyncGenerator

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

class OpenAIMessage():
    role: Role
    content: str

    def __init__(self, role: Role, content: str) -> None:
        self.role = role
        self.content = content

    def message(self) -> dict[str, str]:
        return {"role": self.role.value, "content": self.content}
    
class OpenAIMessages():
    _messages: list[OpenAIMessage]
    _model: Model
    _api_key: str

    def __init__(self, api_key: str, model: Model):
        self._messages = []
        self._model = model
        self._api_key = api_key

    def api_key(self) -> str:
        return self._api_key
    
    def model(self) -> str:
        return self._model.value

    def add_message(self, message: OpenAIMessage) -> None:
        self._messages.append(message)

    def to_dict(self) -> list[dict[str, str]]:
        return [msg.message() for msg in self._messages]

class OpenAIResponse():
    _response: list[Any]

    def __init__(self, response) -> None:
        self._response = response 
    
    async def generate_response_stream(self) -> AsyncGenerator[str, None]:
        async for chunk in self._response:
            yield json.dumps(chunk)
    
async def asend(messages: OpenAIMessages, stream: bool=True) -> OpenAIResponse:
    response = await openai.ChatCompletion.acreate(
        api_key=messages.api_key(),
        model=messages.model(),
        messages=messages.to_dict(),
        stream=stream,
        top_p=HYPER_PARAMETERS['top_p'],
        temperature=HYPER_PARAMETERS['temperature'],
        presence_penalty=HYPER_PARAMETERS['presence_penalty'],
    )
    return OpenAIResponse(response)