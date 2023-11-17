from typing import Optional
from uuid import UUID
from sqlalchemy import ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(128), index=True)
    description: Mapped[Optional[str]]
    is_done: Mapped[bool] = mapped_column(default=False)

    images: Mapped[list['Image']] = relationship(back_populates='task')


class Image(Base):
    __tablename__ = 'image'

    id: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()"))
    url: Mapped[str]
    task_id: Mapped[UUID] = mapped_column(ForeignKey('task.id'))

    task: Mapped['Task'] = relationship(back_populates='images')
