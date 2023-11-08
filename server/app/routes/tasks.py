from http import HTTPStatus
from uuid import UUID
from fastapi import APIRouter, HTTPException

from app.models.task import Task


router = APIRouter(prefix='/tasks')

# TODO: replace with an actual db
tasks = [
    Task(name="Task 1", description="Task 1 Description",
         is_done=False, password='123456'),
    Task(name="Task 2", description="Task 2 Description",
         is_done=False, password='123456'),
    Task(name="Task 3", description="Task 3 Description",
         is_done=False, password='123456'),
    Task(name="Task 4", description="Task 4 Description",
         is_done=False, password='123456'),
    Task(name="Task 5", description="Task 5 Description",
         is_done=False, password='123456')
]


@router.get('/')
def get_all_tasks() -> list[Task]:
    return tasks


@router.get('/{id}')
def get_task(id: UUID) -> Task:
    if not any(task.id == id for task in tasks):
        raise HTTPException(HTTPStatus.NOT_FOUND, f'Task with {id=} not found')
    return next(task for task in tasks if task.id == id)


@router.post('/')
def create_task(task: Task) -> Task:
    tasks.append(task)
    return task
