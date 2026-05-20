# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None


# In-memory storage for this assignment.
# Students can replace this with a database in future projects.
tasks = [
    {"id": 1, "title": "Learn FastAPI basics", "completed": False},
    {"id": 2, "title": "Build a REST endpoint", "completed": False},
]


@app.get("/tasks")
def list_tasks():
    # Task 1: Return all tasks
    return tasks


@app.post("/tasks", status_code=201)
def create_task(new_task: TaskCreate):
    # Task 1: Add the new task to the list with a unique ID
    # Return the created task
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Task 2: Return a single task by ID
    # Raise HTTPException(status_code=404, detail="Task not found") if missing
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, changes: TaskUpdate):
    # Task 2: Update title/completed for an existing task
    # Raise HTTPException(status_code=404, detail="Task not found") if missing
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
