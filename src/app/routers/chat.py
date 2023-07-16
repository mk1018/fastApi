from fastapi import APIRouter, Depends, HTTPException
import app.schemas.task as task_schema

import app.cruds.task as task_crud
from app.db import get_db, DbAsyncSession

router = APIRouter()

@router.get("/chats", response_model=list[task_schema.Task])
async def chat(db: DbAsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)