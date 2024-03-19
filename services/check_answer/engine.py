from services.language_models.open_ai import OpenAIService
from schemas.answer import CreateAnswerSchema
from controllers.question import QuestionGetController
from sqlalchemy.orm import Session
from schemas.result import ResultAfterCheck


class CheckEngine:

    def __init__(self, db_session: Session):
        self.oai_client = OpenAIService()
        self.db_session = db_session

    def check_answer(self, answer: CreateAnswerSchema):

        question_controller = QuestionGetController(db_session=self.db_session)
        question = question_controller.get_question(answer.question_id)

        prompt = f"""
        I have a question: "{question.text}".
        Is this answer correct: "{answer.text}" ?
        How can you evaluate the answer from 0 to 10 in the next format:
        Estimation: (integer) 
        How to Improve: (text)
        """
        completion = self.oai_client.completions_create(prompt)
        completion_dict = completion.model_dump()
        content = completion_dict['choices'][0]['message']['content']

        estimation = ""
        how_to_improve = ""

        lines = content.split('\n')
        for line in lines:
            if line.startswith("Estimation:"):
                estimation = line.split(":")[1].strip() + "/10"
            elif line.startswith("How to Improve:"):
                how_to_improve = line.split(":", 1)[1].strip()

        return ResultAfterCheck(question=question.text,
                                answer=answer.text,
                                estimation=estimation,
                                how_to_improve=how_to_improve)
