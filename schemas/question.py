from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class QuestionLevel(Enum):
    JUNIOR = 'Junior'
    MIDDLE = 'Middle'
    SENIOR = 'Senior'


class Question(BaseModel):
    id: int | None = None
    text: str
    level: QuestionLevel


class CreateQuestion(BaseModel):
    text: str
    level: QuestionLevel


class GetQuestion(Question):
    created_at: datetime
