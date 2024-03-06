from uuid import UUID
from schemas.question import CreateQuestion, GetQuestion
from datetime import datetime, timezone
from models.question import Question
from sqlalchemy.orm import Session


class QuestionCreateController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_question(self, question: CreateQuestion) -> Question:
        new_question = Question(text=question.text, created_at=datetime.now(timezone.utc))
        self.db_session.add(new_question)
        self.db_session.commit()
        return new_question


class QuestionGetController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_question(self, question_id: UUID) -> GetQuestion:
        question = self.db_session.query(Question).where(Question.id == question_id).scalar()
        return GetQuestion(**question.__dict__)
