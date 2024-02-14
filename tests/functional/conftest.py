import pytest
from main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def test_client():
    return TestClient(app)
