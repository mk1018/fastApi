from fastapi import APIRouter, Depends
import app.schemas.task as task_schema

import app.cruds.task as task_crud
from app.db import get_db, DbAsyncSession

router = APIRouter()

@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks(db: DbAsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(
    task_body: task_schema.TaskCreate, db: DbAsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}", response_model=int)
async def delete_task(task_id: int, db: DbAsyncSession = Depends(get_db)):
    # task = task_crud.
    return task_id