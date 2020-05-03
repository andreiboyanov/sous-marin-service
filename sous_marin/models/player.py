from typing import Optional
from pydantic import BaseModel, EmailStr


class PlayerBase(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    first_name: str
    last_name: str
