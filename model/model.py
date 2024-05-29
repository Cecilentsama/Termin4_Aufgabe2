from pydantic import BaseModel
from typing import Optional
from datetime import date


class Person(BaseModel):
    person_id: Optional[int | str] = None
    firstname: str
    lastname: str
    birthdate: date
