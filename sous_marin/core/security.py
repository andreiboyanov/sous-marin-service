from datetime import datetime, timedelta
from typing import Any, Union

from fastapi import Depends
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from sous_marin.core.config import settings
from sous_marin.models.player import PlayerBase

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: str or Any, expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.access_token_ttl_minutes
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.api_v1_path}/login/access-token"
)


def get_current_player(token: str = Depends(oauth2)):
    current_player = PlayerBase(
        email="andrei.boyanov@gmail.com",
        first_name="Andrei",
        last_name="Boyanov",
        id="1095130",
        token=token
    )
    return current_player
