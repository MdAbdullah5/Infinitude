from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory data storage
items = {
  1:{
  "name": "Abdullah",
  "description": "hi",
  "batch": "1"
},
  2:{
  "name": "Abdullah",
  "description": "hi",
  "batch": "1"
},

}


# Pydantic model for request body
class Item(BaseModel):
    name: str
    description: str
    batch:str


# PUT method to update an item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    items[item_id] = item
    return item


# POST method to create an item
@app.post("/items/{item_id}", response_model=Item)
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")

    items[item_id] = item
    return item


# GET method to read an item
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    return items[item_id]


# DELETE method to remove an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    del items[item_id]
    return {"detail": "Item deleted"}
#Get all the items
@app.get("/items")
def readAll():
    return items
@app.get("/items/items")
def readAll():
    items_list = [value for key, value in items.items()]
    return items_list

