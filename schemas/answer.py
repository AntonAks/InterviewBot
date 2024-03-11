from uuid import UUID
from pydantic import BaseModel


class AnswerSchema(BaseModel):
    id: UUID | None = None
    text: str


class CreateAnswerSchema(BaseModel):
    text: str
    question_id: int
