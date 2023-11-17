from uuid import UUID
from sqlalchemy.orm import Session

from app.task import dto, model


async def get_all_tasks(db: Session, offset: int = 0, limit: int = 100):
    return (db.query(model.Task)
            .offset(offset)
            .limit(limit)
            .all())


async def get_task_by_id(db: Session, task_id: UUID):
    return (db.query(model.Task)
            .filter(model.Task.id == task_id)
            .first())


async def create_task(db: Session, task: dto.TaskCreate):
    task_model = model.Task(**task.model_dump())

    db.add(task_model)
    db.commit()
    db.refresh(task_model)

    return task_model
