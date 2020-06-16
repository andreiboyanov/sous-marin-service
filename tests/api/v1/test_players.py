def test_players(sous_marin):
    response = sous_marin.get("/api/v1/players")
    assert response.status_code == 200
    assert response.json() == "{}"


def test_me(sous_marin):
    response = sous_marin.get("/api/v1/players/me")
    assert response.status_code == 200
    assert response.json()["username"] == "andrei"
