import os

def system_openai_api_key() -> str:
    return os.getenv("SYSTEM_OPENAI_API_KEY")

def system_azure_openai_api_key() -> str:
    return os.getenv("SYSTEM_AZURE_OPENAI_API_KEY")

def system_claude_api_key() -> str:
    return os.getenv("SYSTEM_CLAUDE_API_KEY")

def system_bird_api_key() -> str:
    return os.getenv("SYSTEM_BIRD_API_KEY")