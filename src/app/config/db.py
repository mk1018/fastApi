import os

MYSQL_DATABASE=os.getenv('MYSQL_DATABASE')
MYSQL_USER=os.getenv('MYSQL_USER')
MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')

DB_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@mysql:3306/{MYSQL_DATABASE}?charset=utf8"
ASYNC_DB_URL = f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@mysql:3306/{MYSQL_DATABASE}?charset=utf8"