from sqlalchemy import select
from sqlalchemy.engine import Result

import app.models.task as task_model
import app.schemas.task as task_schema
from app.db import DbAsyncSession

async def send_llm(db: DbAsyncSession, task_create: task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task
