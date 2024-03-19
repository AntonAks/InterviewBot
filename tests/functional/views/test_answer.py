from uuid import uuid4
from schemas.question import QuestionLevel
from tests.mock_stuff.answers import mock_oai_client_answer_check, ANSWER_TEXT, QUESTION_TEXT, HOW_TO_IMPROVE


class TestAnswers:

    def test_get_answers(self, test_client):
        _id = uuid4()
        response = test_client.get(f"/api/answer/{_id}")
        json_response = response.json()
        assert response.status_code == 200
        assert json_response["id"] == str(_id)

    @mock_oai_client_answer_check
    def test_post_answers__success(self, test_client):
        _text = "Example Text"

        # Create a question
        test_client.post(
            f"/api/question",
            json={
                "text": QUESTION_TEXT,
                "level": QuestionLevel.MIDDLE.value
            }
        )

        response = test_client.post(
            f"/api/answer",
            json={
                "text": ANSWER_TEXT,
                "question_id": 1
            }
        )
        json_response = response.json()

        assert response.status_code == 201
        assert json_response['question'] == QUESTION_TEXT
        assert json_response['answer'] == ANSWER_TEXT
        assert json_response['estimation'] == "3/10"
        assert json_response['how_to_improve'] == HOW_TO_IMPROVE

    def test_post_answers__question_error(self, test_client):
        _text = "Example Text"

        response = test_client.post(
            f"/api/answer",
            json={
                "text": _text,
                "question_id": 10
            }
        )
        json_response = response.json()
        assert response.status_code == 404
        assert json_response["message"] == "Question not found. ID: 10"
