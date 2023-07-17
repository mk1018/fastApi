import os
""" test """
def run_test() -> bool:
    return True if os.getenv("RUN_TEST") == "True" else False

""" api key """
def system_openai_api_key() -> str:
    return os.getenv("SYSTEM_OPENAI_API_KEY")

def system_azure_openai_api_key() -> str:
    return os.getenv("SYSTEM_AZURE_OPENAI_API_KEY")

def system_claude_api_key() -> str:
    return os.getenv("SYSTEM_CLAUDE_API_KEY")

def system_bird_api_key() -> str:
    return os.getenv("SYSTEM_BIRD_API_KEY")

""" test api key """
def run_test_openai_api_key() -> str:
    return os.getenv("RUN_TEST_OPENAI_API_KEY")

def run_test_azure_openai_api_key() -> str:
    return os.getenv("RUN_TEST_AZURE_OPENAI_API_KEY")

def run_test_claude_api_key() -> str:
    return os.getenv("RUN_TEST_CLAUDE_API_KEY")

def run_test_bird_api_key() -> str:
    return os.getenv("RUN_TEST_BIRD_API_KEY")

""" database """
def mysql_database() -> str:
    return os.getenv("MYSQL_DATABASE")

def mysql_user() -> str:
    return os.getenv("MYSQL_USER")

def mysql_password() -> str:
    return os.getenv("MYSQL_PASSWORD")

def mysql_root_password() -> str:
    return ""

def mysql_port() -> str:
    return os.getenv("MYSQL_PORT")

def mysql_host() -> str:
    return os.getenv("MYSQL_HOST")

""" test database """
def mysql_test_database() -> str:
    return os.getenv("MYSQL_TEST_DATABASE")

""" email """
def email_host() -> str:
    return os.getenv("EMAIL_HOST")

def email_port() -> str:
    return os.getenv("EMAIL_PORT")

def email_use_tls() -> str:
    return os.getenv("EMAIL_USE_TLS")

def email_host_user() -> str:
    return os.getenv("EMAIL_HOST_USER")

def email_host_password() -> str:
    return os.getenv("EMAIL_HOST_PASSWORD")