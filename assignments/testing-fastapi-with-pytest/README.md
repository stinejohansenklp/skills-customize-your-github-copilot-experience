# 📘 Assignment: Test a FastAPI Task API with Pytest

## 🎯 Objective

Learn how to test a REST API built with FastAPI using pytest. You will write automated tests to verify endpoint behavior, status codes, and error handling.

## 📝 Tasks

### 🛠️ Write Tests for Core Endpoints

#### Description
Use pytest and FastAPI's TestClient to test the main Task API endpoints for listing tasks and creating new tasks.

#### Requirements
Completed program should:

- Create a test file that uses `pytest` and `TestClient`
- Add a test for `GET /tasks` that checks a successful response and JSON list output
- Add a test for `POST /tasks` that sends valid JSON and verifies the created task fields
- Assert expected HTTP status codes for each endpoint


### 🛠️ Test Edge Cases and Error Handling

#### Description
Expand your tests to cover invalid input and missing resources so the API is verified under realistic scenarios.

#### Requirements
Completed program should:

- Add a test for `GET /tasks/{task_id}` when the task exists
- Add a test for `GET /tasks/{task_id}` when the task does not exist and confirm a 404 response
- Add at least one test for invalid request data to `POST /tasks` and confirm validation failure
- Keep tests isolated and readable with clear test function names
