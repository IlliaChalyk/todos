from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.task import crud
from app.task.dto import TaskCreate, Task


router = APIRouter(prefix='/tasks')

db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/', response_model=list[Task])
async def get_all_tasks(db: db_dependency, offset: int = 0, limit: int = 100):
    return await crud.get_all_tasks(db, offset, limit)


@router.post('/', response_model=Task)
async def create_task(db: db_dependency, task: TaskCreate):
    return await crud.create_task(db, task)


@router.get('/{task_id}', response_model=Task)
async def get_task(db: db_dependency, task_id: UUID):
    return await crud.get_task_by_id(db, task_id)


@router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(db: db_dependency, task_id: UUID):
    pass
