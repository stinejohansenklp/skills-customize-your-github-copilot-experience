# Starter Code: Test a FastAPI Task API with Pytest

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API for Testing")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Write API tests", "completed": False},
    {"id": 2, "title": "Check status codes", "completed": False},
]


@app.get("/tasks")
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=201)
def create_task(new_task: TaskCreate):
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    created = {"id": new_id, "title": new_task.title, "completed": new_task.completed}
    tasks.append(created)
    return created


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
