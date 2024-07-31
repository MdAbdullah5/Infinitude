########
#####################
from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Employee(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None

# class Employee1(BaseModel):
#     name: Optional[str] = None
#     role: Optional[str] = None



employee = {
    1: {
        "name": "Ganesh",
        "role": "Tester"
    }
}


# @app.get("/basic")
# def test():
#     return {"Test":"Manual input"}

@app.get("/test/{employe_id}")
def test(employe_id: int = Path(description="ID is required", gt=0, le=3)):
    if employe_id in employee:
        return employee[employe_id]
    return {"Data": "Not found"}


@app.get("/query/{employe_id}")
def get_by_query(employe_id: int, name: str):
    for employe_id in employee:
        if employee[employe_id]["name"] == name:
            return employee[employe_id]
        return {"name": "Not Found"}
    return {"Data": "Not found"}


@app.post("/post/{employe_id}")
def create(employe_id: int, employe: Employee):
    if employe_id in employee:
        return {"Employee": "ID already exsists"}
    employee[employe_id] = employe
    return employee[employe_id]

@app.put("/update/{employe_id}")
def update(employe_id: int, employe: Employee):
    if employe_id not in employee:
        return {"Employe": "NOt exsists"}
    employee[employe_id] = employe

@app.put("/update_attributes/{employe_id}")
def updatename(employe_id: int, employe: Employee):
    if employe_id not in employee:
        return {"Emplooye": "Not exsists"}
    if employe.name != None:
        employee[employe_id]["name"]= employe.name
    if employe.role !=None:
        employee[employe_id]["role"]=employe.role

