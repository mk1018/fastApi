from libs.env import system_openai_api_key
import libs.wopenai as openai

async def chat(prompt: str) -> openai.OpenAIResponse:
    messages = openai.OpenAIMessages(system_openai_api_key())

    messages.add_message(
        openai.OpenAIMessage(
            role=openai.Role.SYSTEM,
            content="test"
        )
    )

    messages.add_message(
        openai.OpenAIMessage(
            role=openai.Role.USER,
            content=prompt
        )
    )

    return await openai.asend(messages)