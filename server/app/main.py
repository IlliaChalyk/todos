from fastapi import FastAPI

from app.task.route import router as task_router

ROOT_PATH = '/api/v1'

app = FastAPI()

app.include_router(task_router, prefix=ROOT_PATH)
