from uuid import UUID
from fastapi import APIRouter
from schemas.answer import Answer, CreateAnswer


router = APIRouter(tags=["Answer"])


@router.get("/answer/{answer_id}", status_code=200)
async def get_answer(answer_id: UUID) -> Answer:
    return Answer(id=answer_id, text="Answer text example")


@router.post("/answer", status_code=201)
async def create_answer(a: CreateAnswer):
    return {"answer": a}
