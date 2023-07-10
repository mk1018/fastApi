from sqlalchemy import select
from sqlalchemy.engine import Result

import app.models.task as task_model
import app.schemas.task as task_schema
from app.db import DbAsyncSession

async def create_task(
    db: DbAsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: DbAsyncSession, task: task_model.Task) -> None:
    db.delete(task)
    db.commit()

async def get_task(db: DbAsyncSession, task_id: int) -> task_model.Task | None:
    result: Result = db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )

    return result.scalars().first()

async def update_task(db: DbAsyncSession, task_create: task_schema.TaskCreate, task: task_model.Task):
    task.title = task_create.title
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

async def get_tasks_with_done(db: DbAsyncSession) -> list[task_schema.Task]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done)
        )
    )

    return result.all()