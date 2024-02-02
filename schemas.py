from pydantic import BaseModel
from datetime import datetime


class UserTemplate(BaseModel):
    user_id : int
    username : str
    age : int
    create_at: datetime



