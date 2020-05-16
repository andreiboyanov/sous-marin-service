import pytest
from jose import jwt
from sous_marin.api.api_v1.login import login
from sous_marin.core.config import settings


@pytest.mark.asyncio
async def test_login_assert_username_matches():
    class RequestForm:
        username = "Andrei"
        password = "password"
    response = await login(RequestForm())
    token = response["access_token"]
    decoded_token = jwt.decode(token, settings.secret_key)
    assert decoded_token["sub"] == "Andrei"
