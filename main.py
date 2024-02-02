from typing import List

from database import db_dependency, get_db
from fastapi import Depends, FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from models import User, users_dict
from schemas import UserTemplate
from sqlalchemy.orm import Session

app = FastAPI(
    title="Users API",
    description="""This is a simple Users RESTful API built with Python and FastAPI framework. It uses SQLAlchemy ORM for interacting with the PostgreSQL database & Alembic for data migration."""
)



@app.get("/get-users", response_model=List[UserTemplate])
def get_all_users(db: db_dependency):
    users = db.query(User).all()
    return  [users_dict(u) for u in users]

@app.get("/get-users/{user_id}", response_model=List[UserTemplate])
def get_by_user_id(user_id: int =  Path(..., description="Write the user ID you want."), db: Session =Depends(get_db)):
    user = db.query(User).filter(User.user_id ==user_id).first()
    if not user :
        raise HTTPException(status_code=404, detail=f"User with id  {user_id} not found.")
    return [users_dict(user)]

@app.get("/get-by-username", response_model = List[UserTemplate])
def get_by_username(username: str = Query(...,description="Write the name you want."), db: Session = Depends(get_db) ):
    user = db.query(User).filter(User.username== username).first()
    if not user :
        raise  HTTPException(status_code=404,detail="The user does not exist.")
    return [users_dict(user)]


@app.post("/create-user", response_model=List[UserTemplate])
def create_user(user_info:  UserTemplate, user_id: int, db: Session = Depends(get_db)):
    # check if the user already exists
    if db.query(User).filter(User.user_id == user_id).first():
        raise HTTPException(status_code=409, detail="User already exists")
    else:
        db.add(User(**user_info.dict()))
        db.commit()
    return [users_dict(user_info)]



@app.put("/update-user", response_model = List[UserTemplate])
def  update_user(user_id : int, user_info: UserTemplate, db: Session =  Depends(get_db)):
    user_exists =  db.query(User).filter(User.user_id == user_id).first()
    if user_exists:
        for fields, values in user_info.dict().items():
            setattr(user_exists, fields, values)
        db.commit()
        return [users_dict(user_exists)]
    else:
        raise HTTPException(status_code=404, detail = "User ID does not exist.")



@app.delete("/delete-user", response_model = List[UserTemplate])
def  delete_user(user_id: int, db: Session =Depends(get_db)):
    user_del = db.query(User).filter(User.user_id == user_id).first()
    if user_del:
        db.delete(user_del)
        db.commit()
        return JSONResponse({"Data": "User Successfully deleted."})
    else:
        raise HTTPException(status_code=404, detail="User Not Found")

