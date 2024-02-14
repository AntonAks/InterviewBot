from uuid import uuid4
from fastapi import APIRouter
from schemas.result import Result

router = APIRouter(tags=["Result"])


@router.get("/result", status_code=200)
async def read_question() -> Result:
    return Result(id=uuid4(), details={"message": "Result example"})
