from uuid import UUID
from pydantic import BaseModel


class Answer(BaseModel):
    id: UUID
    text: str


class CreateAnswer(BaseModel):
    text: str
