import libs.env as env
import libs.wopenai as openai

async def chat(prompt: str) -> openai.OpenAIResponse:
    messages = openai.OpenAIMessages(env.get_system_openai_api_key())

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