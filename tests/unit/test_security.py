import pytest
from jose import jwt
from sous_marin.core.security import create_access_token
from sous_marin.core.config import settings


def test_create_access_token_assert_jwt_encoded():
    token = create_access_token("Andrei")
    decoded = jwt.decode(token, settings.secret_key)
    assert decoded["sub"] == "Andrei"


@pytest.mark.skip(reason="Test not implemented")
def test_get_current_player():
    pass
