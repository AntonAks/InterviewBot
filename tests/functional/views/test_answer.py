from uuid import uuid4


class TestAnswers:

    def test_get_answers(self, test_client):
        _id = uuid4()
        response = test_client.get(f"/api/answer/{_id}")
        json_response = response.json()
        assert response.status_code == 200
        assert json_response["id"] == str(_id)

    def test_post_answers(self, test_client):
        _text = "Example Text"

        response = test_client.post(
            f"/api/answer",
            json={
                "text": _text
            }
        )
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["answer"]["text"] == _text
