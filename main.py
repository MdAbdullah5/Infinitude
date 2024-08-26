from fastapi import FastAPI, Request, Form, HTTPException,Header,Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated,Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String


#########Connecting With Database SQLite Db
DATABASE_URL = "sqlite:///./event.db"
engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(autoflush=False,autocommit = False,bind=engine)
Base = declarative_base()



######Model for database
class EventUser(Base):
    __tablename__ = "event"
    e_id = Column(Integer,primary_key=True, index=True)
    e_name = Column(String)
    e_email = Column(String)
    e_password = Column(String)


class UserSchema(BaseModel):
    e_id : int
    e_name : Optional[str] = None
    e_password: Optional[str] = None
    e_email : Optional[str] = None


Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()

app = FastAPI()
l=[]
templates = Jinja2Templates(directory="templates")

@app.get("/submit_login")
def loginp(request:Request):
    return templates.TemplateResponse("login.html",{"request": request})


@app.post("/submit_login")
def login(email:str=Form(...),password:str=Form(...),db: Sessionlocal = Depends(get_db)):
    users = db.query(EventUser).filter(EventUser.e_email == email).first()
    if users:
        if users.e_password==password:
            return "Login Successful"
    return "Not"





@app.get("/submit_signup")
def add(request:Request):
    return templates.TemplateResponse("spage.html",{"request": request})


@app.post("/submit_signup")
def signup(name:str=Form(...),email: str = Form(...), password: str = Form(...),db: Sessionlocal = Depends(get_db)):
    id=1
    request=UserSchema(e_id=id,e_name=name,e_email=email,e_password=password)
    l.append(name)
    l.append(email)
    l.append(password)
    user=EventUser(e_name=request.e_name,e_email=request.e_email,e_password=request.e_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/fetch/signupenrolls")
def readsignups(id:int,db:Sessionlocal=Depends(get_db)):
    db_user = db.query(EventUser).filter(EventUser.e_id == id).first()
    if db_user:
        return db_user
    return f"users {id} doesn't exist"


@app.get(("/signupdetails"))
def read():
    return l



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

