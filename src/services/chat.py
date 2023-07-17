from app.db import DbAsyncSession
from libs.key import openai_api_key
import libs.wopenai as wopenai

async def chat(prompt: str, db: DbAsyncSession) -> wopenai.OpenAIResponse:
    messages = wopenai.OpenAIMessages(
        openai_api_key(), 
        wopenai.Model.GPT_35_TURBO
    )

    messages.add_message(
        wopenai.OpenAIMessage(
            role=wopenai.Role.SYSTEM,
            content="test"
        )
    )

    messages.add_message(
        wopenai.OpenAIMessage(
            role=wopenai.Role.USER,
            content=prompt
        )
    )

    return await messages.asend()