from fastapi.testclient import TestClient
from webservice.service import webservice as app
from http import HTTPStatus


client = TestClient(app)


def test_get_person():
    response = client.post("/person/",
                           json={"firstname": "Test", "lastname": "It", "birthdate": "2000-01-01"})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() is not None
    assert response.json()["person_id"] > 0

    response = client.get(f"/person/?person_id={response.json()["person_id"]}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() is not None


def test_get_persons():
    response = client.post("/person/",
                           json={"firstname": "Test", "lastname": "It", "birthdate": "2000-01-01"})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() is not None
    assert response.json()["person_id"] > 0
    response = client.post("/person/",
                           json={"firstname": "Test", "lastname": "It", "birthdate": "2000-01-01"})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() is not None
    assert response.json()["person_id"] > 0

    response = client.get("/persons/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() is not None
    assert len(response.json()) > 1


def test_save_person():
    response = client.post("/person/",
                          json={"firstname": "Test", "lastname": "It", "birthdate": "2000-01-01"})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() is not None
    assert response.json()["person_id"] > 0


def test_update_person():
    response = client.post("/person/",
                           json={"firstname": "Test", "lastname": "It", "birthdate": "2000-01-01"})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() is not None
    assert response.json()["person_id"] > 0

    response = client.put("/person/",
                          json={"firstname": "Test1", "lastname": "It1", "birthdate": "1999-01-01", "person_id": f"{response.json()["person_id"]}"})
    assert response.status_code == HTTPStatus.ACCEPTED


def test_delete_person():
    response = client.post("/person/",
                           json={"firstname": "Test", "lastname": "It", "birthdate": "2000-01-01"})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() is not None
    assert response.json()["person_id"] > 0

    response = client.delete(f"/person/?person_id={response.json()["person_id"]}")
    assert response.status_code == HTTPStatus.OK
