import pytest
import os
from main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def test_client():
    return TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def delete_db_after_tests():
    yield
    try:
        os.remove("tests/test_db.db")
    except Exception as e:
        print("Error occurred while deleting database file: ", str(e))
