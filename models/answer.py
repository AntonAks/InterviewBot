from uuid import uuid4
from datetime import datetime
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, DateTime, UUID
from database.db import Base


class Answer(Base):
    __tablename__ = 'answers'

    id: Mapped[Integer] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    text: Mapped[str] = mapped_column(String(1024), nullable=False)
    question_id: Mapped[Integer] = mapped_column(Integer, nullable=False)
    result_id: Mapped[UUID] = mapped_column(UUID, nullable=False, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime)
