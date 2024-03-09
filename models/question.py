from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, DateTime
from sqlalchemy_utils import UUIDType
from database.db import Base
from sqlalchemy.sql.schema import Sequence


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[Integer] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    text: Mapped[str] = mapped_column(String(1024), nullable=False)
    level: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime)
