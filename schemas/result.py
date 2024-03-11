from uuid import UUID
from pydantic import BaseModel


class ResultSchema(BaseModel):
    id: UUID
    details: dict
