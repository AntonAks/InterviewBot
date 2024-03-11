from uuid import uuid4
from fastapi import APIRouter
from schemas.result import ResultSchema

router = APIRouter(tags=["Result"])


@router.get("/result", status_code=200)
async def read_question() -> ResultSchema:
    return ResultSchema(id=uuid4(), details={"message": "Result example"})
