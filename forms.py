from fastapi import FastAPI, Request, Form, HTTPException,Header,Depends
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated,Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String,Time,Date, ForeignKey,Table,MetaData
from sqlalchemy.sql import select

event_name="holi"


#########Connecting With Database SQLite Db
DATABASE_URL = "sqlite:///./event.db"
engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(autoflush=False,autocommit = False,bind=engine)
Base = declarative_base()


event_name="holi"

metadata = MetaData()
class Events(Base):
    __tablename__=f"{event_name}"
    event_id=Column(Integer,primary_key=True)
    events_name=Column(String)


class FormData(Base):
    __tablename__ = f"{event_name}formdetails"
    form_id = Column(Integer,primary_key=True, index=True)
    name = Column(Integer)
    email=Column(String)
    phoneno=Column(Integer)
    Dropdown=Column(String)
    event_id=Column(Integer,ForeignKey("holi.event_id"))




class FormSchema(BaseModel):
    form_id : int
    name : Optional[str] = None
    email: Optional[str] = None
    phoneno: Optional[int] = None
    Dropdown: Optional[str] = None



Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/submit_form")
def getforms(request:Request):
    return templates.TemplateResponse("forms.html",{"request": request})


@app.post("/submit_form")
def postforms(name:str=Form(...),email:str=Form(...),phoneno:str=Form(...),Dropdown:str=Form(...),db: Sessionlocal = Depends(get_db)):
    id=1
    formuser=FormSchema(form_id=id,name=name,email=email,phoneno=phoneno,Dropdown=Dropdown)
    user=FormData(name=formuser.name,email=formuser.email,phoneno=formuser.phoneno,Dropdown=formuser.Dropdown)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/fetch")
def fetch_table(table_name:str=Form(...), db: Sessionlocal = Depends(get_db)):
    try:
        # Reflect the table
        table = Table(table_name, metadata, autoload_with=engine)

        # Execute a SELECT * FROM table_name
        query = select(table)
        result = db.execute(query).fetchall()

        rows = [row._asdict() for row in result]

        return rows

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching table: {str(e)}")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)





