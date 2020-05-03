from fastapi import APIRouter, Depends
from sous_marin.core.security import get_current_player
from sous_marin.models.player import Player

router = APIRouter()


@router.get("/")
async def get_players(current_player: Player = Depends(get_current_player)):
    return []


@router.get("/me")
async def get_myself(current_player: Player = Depends(get_current_player)):
    return current_player
