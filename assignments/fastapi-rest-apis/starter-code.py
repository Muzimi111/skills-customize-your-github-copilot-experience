# Import FastAPI and other necessary modules
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Create FastAPI app instance
app = FastAPI()

# Define Pydantic model for Item
class Item(BaseModel):
    id: int
    title: str
    description: str = None

# In-memory storage for items
items = []

# Task 1: Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

# Task 2: CRUD endpoints
@app.get("/items", response_model=List[Item])
def get_items():
    # Return all items
    pass

@app.post("/items", response_model=Item)
def create_item(item: Item):
    # Add new item to the list
    # Return the created item
    pass

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    # Find and return the item with the given id
    # If not found, return appropriate error
    pass

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    # Update the item with the given id
    # Return the updated item
    pass

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Delete the item with the given id
    # Return confirmation message
    pass