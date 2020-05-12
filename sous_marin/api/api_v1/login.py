from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sous_marin.core.security import create_access_token

router = APIRouter()


@router.post("/access-token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if password == "":
        raise HTTPException(status_code=400, detail="Incorrect username ot password")
    return {
        "access_token": create_access_token(username),
        "token_type": "bearer",
    }
