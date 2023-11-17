from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Image(BaseModel):
    id: Optional[UUID] = Field(default_factory=lambda: uuid4())
    url: str


class TaskBase(BaseModel):
    name: str
    description: str
    is_done: bool = False
    images: Optional[list[Image]] = []


class Task(TaskBase):
    id: UUID = Field(default_factory=lambda: uuid4())


class TaskCreate(TaskBase):
    pass
