from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.question import CreateQuestionSchema, GetQuestionSchema
from controllers.question import QuestionCreateController, QuestionGetController, QuestionGetRandomController
from database.db import get_db

router = APIRouter(tags=["Question"])


@router.get("/question/{question_id}", status_code=200, response_model=GetQuestionSchema)
async def get_question(question_id: int, db_session: Session = Depends(get_db)):
    controller = QuestionGetController(db_session)
    return controller.get_question(question_id)


@router.get("/random-random", status_code=200)
async def get_random_question(db_session: Session = Depends(get_db)):
    controller = QuestionGetRandomController(db_session)
    return controller.get_question()


@router.post("/question", status_code=201, response_model=GetQuestionSchema)
async def create_question(question: CreateQuestionSchema, db_session: Session = Depends(get_db)):
    controller = QuestionCreateController(db_session)
    return controller.add_question(question)
