from fastapi import FastAPI

from app.models.task import Task
from app.routes import tasks

ROOT_PATH = '/api/v1'

app = FastAPI()

app.include_router(tasks.router, prefix=ROOT_PATH)
