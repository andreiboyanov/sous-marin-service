import pytest
from jose import jwt
from datetime import timedelta, datetime
from sous_marin.core import security
from sous_marin.core.config import settings


def test_create_access_token_assert_jwt_encoded():
    token = security.create_access_token("Andrei")
    decoded = jwt.decode(token, settings.secret_key)
    assert decoded["sub"] == "Andrei"


def test_create_access_token_with_expire_delta_assert_expires_sooner_then_delta():
    token = security.create_access_token("Andrei", timedelta(minutes=100))
    decoded = jwt.decode(token, settings.secret_key)
    assert datetime.fromtimestamp(decoded["exp"]) < datetime.now() + timedelta(
        minutes=100
    )


@pytest.mark.skip(reason="Test not implemented")
def test_get_current_player():
    pass


def test_get_password_hash():
    password_hash = security.get_password_hash("password")
    assert len(password_hash) > 0


def test_verify_password_hash():
    password_hash = security.get_password_hash("password")
    assert security.verify_password("password", password_hash)
