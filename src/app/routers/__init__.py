from fastapi import FastAPI

from app.routers import task, done, chat

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)
app.include_router(chat.router)