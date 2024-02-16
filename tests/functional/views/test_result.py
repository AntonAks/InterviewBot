from uuid import uuid4


class TestResult:

    base_path = "/api/result"

    def test_get_answers(self, test_client):
        _id = uuid4()
        response = test_client.get(f"{self.base_path}")
        assert response.status_code == 200
