from uuid import UUID
from pydantic import BaseModel


class ResultSchema(BaseModel):
    id: UUID
    details: dict


class ResultAfterCheck(BaseModel):
    question: str
    answer: str
    estimation: str
    how_to_improve: str
