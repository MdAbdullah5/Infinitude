from typing import Optional
from models import Base, User
from pydantic import BaseModel
from schema import UserSchema
from database import engine,Sessionlocal
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends,HTTPException

Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()


app=FastAPI()
@app.post("/adduser")
def add_user(request:UserSchema, db: Session = Depends(get_db)):
    user = User(name=request.name, email = request.email,nickname=request.nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/user/{user_name}")
def get_users(user_name,db: Session= Depends(get_db)):
    users = db.query(User).filter(User.name == user_name).first()  #Explanation Needed
    return users
######put and delete
@app.put("/Users/Update/{id}")
def update_user(user_id: int, user:UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.nickname=user.nickname
        db.commit()
        db.refresh(db_user)
        return db_user
    return f"userid:{user_id} not found"

@app.delete("/delete/{id}")
def delete(user_id: int, db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return f"users {user_id} doesn't exist"
@app.put("/update_attributes/{id}")
def update_attributes(user_id: int,user:UserSchema, db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if user.name:
            db_user.name = user.name
        if user.email:
            db_user.email=user.email
        if user.nickname:
            db_user.nickname=user.nickname
        db.commit()
        db.refresh(db_user)
        return db_user
    return f"users {user_id} doesn't exist"