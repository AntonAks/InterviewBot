from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class Question(BaseModel):
    id: UUID
    text: str


class CreateQuestion(BaseModel):
    text: str


class GetQuestion(Question):
    created_at: datetime
