from random import choice
from schemas.question import CreateQuestionSchema, GetQuestionSchema
from datetime import datetime, timezone
from models.question import Question
from sqlalchemy.orm import Session
from exceptions.base import NotFoundError


class QuestionController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def is_exists(self, question_id: int) -> bool:
        is_exists = self.db_session.query(Question).filter(Question.id == question_id).scalar() is not None
        return is_exists


class QuestionCreateController(QuestionController):
    def add_question(self, question: CreateQuestionSchema) -> Question:
        new_question = Question(
            text=question.text,
            level=question.level.value,
            created_at=datetime.now(timezone.utc)
        )
        self.db_session.add(new_question)
        self.db_session.commit()
        return new_question


class QuestionGetController(QuestionController):
    def get_question(self, question_id: int) -> GetQuestionSchema:
        question = self.db_session.query(Question).where(Question.id == question_id).scalar()
        if question is None:
            raise NotFoundError(details=f"Question not found. ID: {question_id}")
        return GetQuestionSchema(**question.__dict__)


class QuestionGetRandomController(QuestionController):
    def get_question(self):
        questions_count = self.db_session.query(Question).count()
        _id = choice(range(questions_count))+1
        question = self.db_session.query(Question).where(Question.id == _id).scalar()
        return GetQuestionSchema(**question.__dict__)

