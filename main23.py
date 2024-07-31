from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class Employee(BaseModel):
    name:str
    role:str
employee={
    1:{
        "name":"Ganesh",
        "role":"tester"
    }
}
@app.get("/test/{id}")
def test(id:int):
    if id not in employee:
        return "details not found"
    return employee[id]

@app.get("/query/{id}")
def getname(id:int,name:str):
    for id in employee:
        if employee[id][name] == name:
            return employee[id]
        return {"name":"not found"}
    return "details not found"

@app.post("/post/{id}")
def create(id:int,emp:Employee):
    if id in employee:
        return {"Employee id already exists"}
    employee[id]=emp
    return emp
@app.put("/put/{id}")
def update(id:int,emp:Employee):
    if id not in employee:
        return "doesnt exists"
    employee[id] = emp
    return emp
# @app.put("/putname")
# def update_name(id:int,name:Employee.name):
#     if id not in employee:
#         return "id doesn't exist"
#     employee[id]["name"]=name
#     return employee[id]