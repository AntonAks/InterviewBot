from schemas.question import QuestionLevel


class TestQuestion:

    base_path = "/api/question"

    def test_post_question(self, test_client):
        _text = "Example Text"

        response = test_client.post(
            f"{self.base_path}",
            json={
                "text": _text,
                "level": QuestionLevel.MIDDLE.value
            }
        )
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["text"] == _text

    def test_get_question(self, test_client):
        _text = "Example Text"
        response = test_client.post(
            f"{self.base_path}",
            json={
                "text": _text,
                "level": QuestionLevel.MIDDLE.value
            }
        )
        json_response = response.json()
        new_question_id = json_response.get("id")
        response = test_client.get(f"{self.base_path}/{new_question_id}")

        assert response.status_code == 200
        assert json_response["id"] == new_question_id

