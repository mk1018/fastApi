from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config.db import ASYNC_DB_URL

class DbAsyncSession(AsyncSession):
    pass

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=DbAsyncSession
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session