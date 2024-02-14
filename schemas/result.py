from uuid import UUID
from pydantic import BaseModel


class Result(BaseModel):
    id: UUID
    details: dict
