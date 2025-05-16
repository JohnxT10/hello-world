from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

# Set up logging to a file
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s %(message)s")

app = FastAPI()

# In-memory storage for items
items = {}

class Item(BaseModel):
    name: str
    value: int

# Create
@app.post("/items/")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    logging.info(f"Created item {item_id}: {item}")
    return {"message": "Item created", "item": item}

# Read
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    logging.info(f"Read item {item_id}")
    return items[item_id]

# Update
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    logging.info(f"Updated item {item_id}: {item}")
    return {"message": "Item updated", "item": item}

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    logging.info(f"Deleted item {item_id}")
    return {"message": "Item deleted"}

# Add numbers via GET
@app.get("/add/")
def add_numbers(a: int, b: int):
    result = a + b
    logging.info(f"Added numbers: {a} + {b} = {result}")
    return {"result": result}