import libs.env as env

DB_CONNECT_INFO = f"{env.mysql_user()}:{env.mysql_password()}@{env.mysql_host()}:{env.mysql_port()}/{env.mysql_database()}?charset=utf8"

def sync_db_usl() -> str:
    return f"mysql+pymysql://{DB_CONNECT_INFO}"

def async_db_url() -> str:
    return f"mysql+aiomysql://{DB_CONNECT_INFO}"