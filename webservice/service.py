from fastapi import FastAPI, HTTPException, status
from typing import List
from webservice.dataaccess_sqlite import DataAccessSqlite
from model.model import Person


data_access = DataAccessSqlite(database_name="service.db") #ca gere l acces aux donnes
webservice = FastAPI()


@webservice.get("/") # definie la route HTTp get pour un decorateur
def get_root():
    return {"message": "Hello from Python WebService"}


@webservice.get("/person/", response_model=Person | None)
def get_person(person_id: int):
    try:
        return data_access.load_person(person_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@webservice.get("/persons", response_model=List[Person])
def get_persons():
    try:
        return data_access.load_person_list()
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@webservice.post("/person/", response_model=Person, status_code=status.HTTP_201_CREATED)
def insert_person(person: Person):
    try:
        if not person.person_id:
            return data_access.save_person(person)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@webservice.put("/person/", response_model=Person, status_code=status.HTTP_202_ACCEPTED)
def update_person(person: Person):
    try:
        if person.person_id:
            return data_access.update_person(person)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@webservice.delete("/person/")
def delete_person(person_id: int):
    try:
        data_access.delete_person(person_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
