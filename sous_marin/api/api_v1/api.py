from fastapi import APIRouter
from sous_marin.api.api_v1 import players

api_router = APIRouter()
api_router.include_router(players.router, prefix="/players", tags=["players"])
