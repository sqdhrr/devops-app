import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.is_json


def test_tasks_api(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.is_json