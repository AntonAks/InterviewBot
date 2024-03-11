from uuid import uuid4
from schemas.question import QuestionLevel


class TestAnswers:

    def test_get_answers(self, test_client):
        _id = uuid4()
        response = test_client.get(f"/api/answer/{_id}")
        json_response = response.json()
        assert response.status_code == 200
        assert json_response["id"] == str(_id)

    def test_post_answers__success(self, test_client):
        _text = "Example Text"

        # Create a question
        test_client.post(
            f"/api/question",
            json={
                "text": "Test Question",
                "level": QuestionLevel.MIDDLE.value
            }
        )

        response = test_client.post(
            f"/api/answer",
            json={
                "text": _text,
                "question_id": 1
            }
        )
        json_response = response.json()

        assert response.status_code == 201
        assert json_response['answer'] == 'Your answer accepted for question with ID: 1 was created'

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
