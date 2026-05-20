# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a basic REST API using the FastAPI framework. You will create endpoints, validate request data, and return structured JSON responses for a simple task manager service.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI app and build foundational endpoints that let users view all tasks and add new ones.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Add a GET endpoint at `/tasks` that returns all tasks as JSON
- Add a POST endpoint at `/tasks` that accepts task data and stores it in memory
- Return appropriate HTTP status codes for successful requests


### 🛠️ Add Task Lookup and Updates

#### Description
Expand your API to support retrieving a single task and updating task status by ID.

#### Requirements
Completed program should:

- Add a GET endpoint at `/tasks/{task_id}` to return one task
- Return a 404 response when a task ID does not exist
- Add a PUT endpoint at `/tasks/{task_id}` to update a task (for example, title or completed status)
- Return the updated task in JSON format
