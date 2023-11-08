from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: Optional[UUID] = Field(default_factory=lambda: uuid4())
    name: str
    description: str
    is_done: bool
    password: str = Field(exclude=True)
