from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_players():
    response = client.get("/api/v1/players")
    assert response.status_code == 200
    assert response.json() == "{}"


def test_me():
    response = client.get("/api/v1/players/me")
    assert response.status_code == 200
    assert response.json()["username"] == "andrei"
