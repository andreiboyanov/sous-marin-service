from fastapi import APIRouter
from sous_marin.api.api_v1 import players, login

api_router = APIRouter()
api_router.include_router(players.router, prefix="/players", tags=["players"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
