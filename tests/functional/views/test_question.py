from uuid import uuid4
from database.db import get_db


class TestQuestion:

    base_path = "/api/question"

    def test_post_question(self, test_client):
        _text = "Example Text"

        response = test_client.post(
            f"{self.base_path}",
            json={
                "text": _text
            }
        )
        json_response = response.json()
        print(">>>>>>>>>>>>>>>", json_response)
        assert response.status_code == 201
        assert json_response["text"] == _text

    def test_get_question(self, test_client):
        _text = "Example Text"
        response = test_client.post(
            f"{self.base_path}",
            json={
                "text": _text
            }
        )
        json_response = response.json()
        print(">>>>>>>>> json_response POST >>>>>>>>>", json_response)
        new_question_id = json_response.get("id")
        print(">>>>>>>>> new_question_id >>>>>>>>>", new_question_id)
        response = test_client.get(f"{self.base_path}/{new_question_id}")
        json_response = response.json()
        print(">>>>>>>>> json_response >>>>>>>>>", json_response)
        assert response.status_code == 200
        assert json_response["id"] == str(new_question_id)

