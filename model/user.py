from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    date_created: Optional[datetime]