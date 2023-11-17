from .task import model
from fastapi import FastAPI

from app.database import Base, engine
from app.task.route import router as task_router

API_VERSION = '/api/v1'

# TODO: remove this, only for development purposes
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_router, prefix=API_VERSION)
