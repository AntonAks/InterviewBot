from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, DateTime
from sqlalchemy_utils import UUIDType
from database.db import Base


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[UUID] = mapped_column(UUIDType(), primary_key=True, index=True, default=uuid4)
    text: Mapped[str] = mapped_column(String(1024), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)

