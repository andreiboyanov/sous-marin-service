def test_login(sous_marin):
    response = sous_marin.post(
        "/api/v1/login/access-token",
        data="grant_type=password&username=andrei&password=andrei",
    )
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
