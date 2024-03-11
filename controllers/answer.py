from random import choice
from schemas.answer import CreateAnswerSchema
from datetime import datetime, timezone
from models.answer import Answer
from sqlalchemy.orm import Session
from exceptions.base import NotFoundError


class AnswerController:
    def __init__(self, db_session: Session):
        self.db_session = db_session


class AnswerCreateController(AnswerController):
    def create_answer(self, answer: CreateAnswerSchema) -> Answer:
        new_answer = Answer(
            text=answer.text,
            question_id=answer.question_id,
            created_at=datetime.now(timezone.utc)
        )
        self.db_session.add(new_answer)
        self.db_session.commit()
        return new_answer
