from random import choice
from schemas.question import CreateQuestion, GetQuestion
from datetime import datetime, timezone
from models.question import Question
from sqlalchemy.orm import Session


class QuestionController:
    def __init__(self, db_session: Session):
        self.db_session = db_session


class QuestionCreateController(QuestionController):
    def add_question(self, question: CreateQuestion) -> Question:
        print("CreateQuestion >>>>>>>>>>>>>>>>>>>>", CreateQuestion)
        new_question = Question(
            text=question.text,
            level=question.level.value,
            created_at=datetime.now(timezone.utc)
        )
        self.db_session.add(new_question)
        self.db_session.commit()
        return new_question


class QuestionGetController(QuestionController):
    def get_question(self, question_id: int) -> GetQuestion:
        question = self.db_session.query(Question).where(Question.id == question_id).scalar()
        return GetQuestion(**question.__dict__)


class QuestionGetRandomController(QuestionController):
    def get_question(self):
        questions_count = self.db_session.query(Question).count()
        _id = choice(range(questions_count))+1
        question = self.db_session.query(Question).where(Question.id == _id).scalar()
        return GetQuestion(**question.__dict__)

