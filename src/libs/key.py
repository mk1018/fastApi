import libs.env as env

def openai_api_key() -> str:
    if env.run_test():
        return env.run_test_openai_api_key()
    return env.system_openai_api_key()

def azure_openai_api_key() -> str:
    if env.run_test():
        return env.run_test_azure_openai_api_key()
    return env.system_azure_openai_api_key()

def claude_api_key() -> str:
    if env.run_test():
        return env.run_test_claude_api_key()
    return env.system_claude_api_key()

def bird_api_key() -> str:
    if env.run_test():
        return env.run_test_bird_api_key()
    return env.system_bird_api_key()