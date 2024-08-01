from fastapi import FastAPI

from model import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "HEEEello World"}


todos = []


# Get all todos
@app.get("/todos/")
async def get_todos():
    return {"all todos": todos}


# Get single todo
@app.get("/todos/{id}")
async def get_todos(id: int):
    for todo in todos:
        if todo.id == id:
            return {"todo": todo, "message": f"Fetched {id}"}
    return {"message": f"Todo with id {id} not found"}


# Create todos
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": f"{todo.item} has been created"}


"""
When a request is made to the endpoint, FastAPI:

Reads the request body.
Parses the JSON data.
Validates the data against the Pydantic model.
Converts the validated data into an instance of the Pydantic model.
"""


# In FastAPI, the todo_object is obtained from the request body.
# Update todos
@app.put("/todos/{id}")
async def update_todo(id: int, todo_object: Todo):
    for todo in todos:
        if todo.id == id:
            todo.id = id
            todo.item = todo_object.item
            return {"message": f"Todo with id {id} has been updated"}
    return {"message": f"Todo with id {id} not found"}


# Delete todos
@app.delete("/todos/{id}")
async def delete_todos(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"message": f"Todo with id {id} has been deleted"}
    return {"messages": "Todo not found"}
