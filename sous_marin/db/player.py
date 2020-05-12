from motor import motor_asyncio as motor
from sous_marin.core.config import settings
from sous_marin.models.player import Player


client = motor.AsyncIOMotorClient(settings.db_url)


def authenticate(email, password):
    return Player({})