# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a simple REST API using the FastAPI framework in Python. The API will manage a collection of items (e.g., books or tasks) and support basic CRUD operations: Create, Read, Update, and Delete.

## 📝 Tasks

### 🛠️	Set Up FastAPI Project

#### Description
Install FastAPI and create a basic FastAPI application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a FastAPI app instance
- Define a GET endpoint at "/" that returns {"message": "Welcome to the API"}
- Run the server and verify it works


### 🛠️	Implement CRUD Endpoints

#### Description
Add endpoints to manage a list of items. Use an in-memory list to store the items.

#### Requirements
Completed program should:

- Define a Pydantic model for the item (e.g., with id, title, description)
- Implement GET /items to retrieve all items
- Implement POST /items to create a new item
- Implement GET /items/{id} to retrieve a specific item
- Implement PUT /items/{id} to update an item
- Implement DELETE /items/{id} to delete an item
- Handle cases where item is not found