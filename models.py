from database import Base
from sqlalchemy import INTEGER, Column, DateTime, String, func


class User(Base):
    __tablename__ = "users"

    user_id = Column(INTEGER, primary_key=True)
    username = Column(String)
    age = Column(INTEGER)
    create_at = Column(DateTime,  default=func.now())

def  users_dict(user: User):
    return {
        "user_id": user.user_id,
        "username": user.username,
        "age": user.age,
        "create_at": user.create_at,
    }