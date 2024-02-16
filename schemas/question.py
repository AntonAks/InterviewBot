from uuid import UUID
from pydantic import BaseModel


class Question(BaseModel):
    id: UUID
    text: str


class CreateQuestion(BaseModel):
    text: str
