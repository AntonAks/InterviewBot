from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.question import Question, CreateQuestion, GetQuestion
from controllers.question import QuestionCreateController, QuestionGetController
from database.db import get_db

router = APIRouter(tags=["Question"])


@router.get("/question/{question_id}", status_code=200, response_model=GetQuestion)
async def get_question(question_id: UUID, db_session: Session = Depends(get_db)):
    controller = QuestionGetController(db_session)
    return controller.get_question(question_id)


@router.get("/question/random", status_code=200, response_model=Question)
async def get_random_question(question_id: UUID, db_session: Session = Depends(get_db)):
    return Question(id=question_id, text="Random question text example")


@router.post("/question", status_code=201, response_model=GetQuestion)
async def create_question(question: CreateQuestion,  db_session: Session = Depends(get_db)):
    controller = QuestionCreateController(db_session)
    return controller.add_question(question)
