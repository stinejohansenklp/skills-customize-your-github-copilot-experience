# Starter Tests: complete these test cases with pytest

from fastapi.testclient import TestClient

from starter_code import app

client = TestClient(app)


def test_list_tasks_returns_ok_and_list():
    # TODO: Assert GET /tasks returns status 200 and a list
    pass


def test_create_task_returns_created_task():
    # TODO: Send POST /tasks with valid JSON and assert status 201
    # TODO: Assert returned JSON contains title and completed fields
    pass


def test_get_task_not_found_returns_404():
    # TODO: Request a non-existing task id and assert status 404
    pass


def test_create_task_invalid_payload_returns_422():
    # TODO: Send invalid payload to POST /tasks and assert status 422
    pass
