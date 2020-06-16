import pytest
from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


@pytest.fixture
def sous_marin():
    return client
