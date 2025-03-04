from __future__ import annotations
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]
    is_superuser: Mapped[bool] = mapped_column(default=False)
    post: Mapped[List["Post"]] = relationship(back_populates="user")

