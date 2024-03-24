from uuid import UUID
from fastapi import APIRouter, Depends, BackgroundTasks
from schemas.answer import AnswerSchema, CreateAnswerSchema
from controllers.answer import AnswerCreateController
from sqlalchemy.orm import Session
from database.db import get_db
from services.check_answer.engine import CheckEngine
from schemas.result import ResultAfterCheck
from celery_worker import dummy_task

router = APIRouter(tags=["Answer"])


@router.get("/answer/{answer_id}", status_code=200)
async def get_answer(answer_id: UUID) -> AnswerSchema:
    return AnswerSchema(id=answer_id, text="Answer text example")

# add it to the POST request for answers creation
@router.post("/answer", status_code=201)
async def create_answer(answer: CreateAnswerSchema,
                        db_session: Session = Depends(get_db)) -> ResultAfterCheck:
    dummy_task.delay() # Setup celery background tasks for the project
    controller = AnswerCreateController(db_session)
    new_answer = controller.create_answer(answer)
    check_engine = CheckEngine(db_session=db_session)
    result = check_engine.check_answer(new_answer)
    return result
