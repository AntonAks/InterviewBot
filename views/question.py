from uuid import UUID
from fastapi import APIRouter
from schemas.question import Question, CreateQuestion

router = APIRouter(tags=["Question"])


@router.get("/question/{question_id}", status_code=200)
async def read_question(question_id: UUID) -> Question:
    return Question(id=question_id, text="Question text example")


@router.post("/question", status_code=201)
async def create_question(q: CreateQuestion):
    return {"question": q}
