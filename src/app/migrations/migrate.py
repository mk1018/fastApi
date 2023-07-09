from sqlalchemy import create_engine

from models.task import Base

from config.db import DB_URL
engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)