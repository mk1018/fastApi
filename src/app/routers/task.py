from typing import List
from fastapi import APIRouter, Depends
from app.schemas.task import Task, TaskCreate, TaskCreateResponse

import app.cruds.task as task_crud
from app.db import get_db, DbAsyncSession

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
async def list_tasks(db: DbAsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)

@router.post("/tasks", response_model=TaskCreateResponse)
async def create_task(
    task_body: TaskCreate, db: DbAsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}", response_model=TaskCreateResponse)
async def update_task(task_id: int, task_body: TaskCreate):
    return TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}", response_model=int)
async def delete_task(task_id: int):
    return task_id