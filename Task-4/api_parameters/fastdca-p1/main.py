from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

# ✅ Root route
@app.get("/")
def root():
    return {"message": "Welcome to the DACA API!"}

# Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., ge=1)):
    return {"item_id": item_id}

@app.get("/items/")
async def read_items(
    q: str | None = Query(None, min_length=3, max_length=50),
    skip: int = 0,
    limit: int = 10
):
    return {"q": q, "skip": skip, "limit": limit}

@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(..., ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = None
):
    result = {"item_id": item_id}
    if q:
        result["q"] = q
    if item:
        result["item"] = item.dict()
    return result
