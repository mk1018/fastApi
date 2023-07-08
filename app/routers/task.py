from typing import List
from fastapi import APIRouter
from schemas.task import Task, TaskCreate, TaskCreateResponse

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
async def list_tasks():
    return [Task(id=1, title="1つ目のTODOタスク")]


@router.post("/tasks", response_model=TaskCreateResponse)
async def create_task(task_body: TaskCreate):
    return TaskCreateResponse(id=1, **task_body.dict())


@router.put("/tasks/{task_id}", response_model=TaskCreateResponse)
async def update_task(task_id: int, task_body: TaskCreate):
    return TaskCreateResponse(id=task_id, **task_body.dict())


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return