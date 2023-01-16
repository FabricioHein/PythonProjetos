from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel


# interface do modelo recebido via post
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

fake_items_db = [
    {"nome": "Joao"}, {"nome": "Carlos"}, {"nome": "Eduardo"}]

app = FastAPI()

# rota get 
@app.get("/")
async def init():
    return {"message": ["Hello World"]}

# enviando item
@app.post("/items/")
async def create_item(item: Item):
    return item

# query dados
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}