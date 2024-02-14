from uuid import uuid4


class TestQuestion:

    base_path = "/api/question"

    def test_get_answers(self, test_client):
        _id = uuid4()
        response = test_client.get(f"{self.base_path}/{_id}")
        json_response = response.json()
        assert response.status_code == 200
        assert json_response["id"] == str(_id)

    def test_post_answers(self, test_client):
        _text = "Example Text"

        response = test_client.post(
            f"{self.base_path}",
            json={
                "text": _text
            }
        )
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["question"]["text"] == _text
