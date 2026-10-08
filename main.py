from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple Items API")

class Item(BaseModel):
    name: str
    price: float

# In-memory store (resets on restart; use a database for real apps)
items: dict[int, Item] = {}

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Heroku!"}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]