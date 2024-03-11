from uuid import UUID
from fastapi import APIRouter, Depends
from schemas.answer import AnswerSchema, CreateAnswerSchema
from controllers.answer import AnswerCreateController
from sqlalchemy.orm import Session
from database.db import get_db


router = APIRouter(tags=["Answer"])


@router.get("/answer/{answer_id}", status_code=200)
async def get_answer(answer_id: UUID) -> AnswerSchema:
    return AnswerSchema(id=answer_id, text="Answer text example")


@router.post("/answer", status_code=201)
async def create_answer(answer: CreateAnswerSchema,
                        db_session: Session = Depends(get_db)):
    controller = AnswerCreateController(db_session)
    new_answer = controller.create_answer(answer)
    return {"answer": f"Your answer accepted for question with ID: {new_answer.question_id} was created"}
