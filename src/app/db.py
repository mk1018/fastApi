from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config.db import async_db_url

class DbAsyncSession(AsyncSession):
    pass

async_engine = create_async_engine(async_db_url(), echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=DbAsyncSession
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session