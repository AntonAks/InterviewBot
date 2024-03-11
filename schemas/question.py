from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class QuestionLevel(Enum):
    JUNIOR = 'Junior'
    MIDDLE = 'Middle'
    SENIOR = 'Senior'


class QuestionSchema(BaseModel):
    id: int | None = None
    text: str
    level: QuestionLevel


class CreateQuestionSchema(BaseModel):
    text: str
    level: QuestionLevel


class GetQuestionSchema(QuestionSchema):
    created_at: datetime
