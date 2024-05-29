from businesslayer.person import Person
from model.model import Person as DAPerson
from datetime import date


FIRSTNAME = "First"
LASTNAME = "Last"
ID_NUM = 1
ID_STR = "string"
BIRTHDATE = date.today()


def test_as_dict():
    p1 = Person(firstname=FIRSTNAME, lastname=LASTNAME, birthdate=BIRTHDATE)
    d = p1.as_dict()
    assert len(d) == 4 and d["firstname"] == FIRSTNAME and d["lastname"] == LASTNAME and d["birthdate"] == BIRTHDATE and d["person_id"] is None

    p2 = Person(firstname=FIRSTNAME, lastname=LASTNAME, birthdate=BIRTHDATE, person_id=ID_STR)
    d = p2.as_dict()
    assert len(d) == 4 and d["firstname"] == FIRSTNAME and d["lastname"] == LASTNAME and d["birthdate"] == BIRTHDATE and d["person_id"] == ID_STR

    p2 = Person(firstname=FIRSTNAME, lastname=LASTNAME, birthdate=BIRTHDATE, person_id=ID_NUM)
    d = p2.as_dict()
    assert len(d) == 4 and d["firstname"] == FIRSTNAME and d["lastname"] == LASTNAME and d["birthdate"] == BIRTHDATE and d["person_id"] == ID_NUM

    p2 = Person(person=DAPerson(firstname=FIRSTNAME, lastname=LASTNAME, birthdate=BIRTHDATE, person_id=ID_STR))
    d = p2.as_dict()
    assert len(d) == 4 and d["firstname"] == FIRSTNAME and d["lastname"] == LASTNAME and d["birthdate"] == BIRTHDATE and d["person_id"] == ID_STR

    p2 = Person(person=DAPerson(firstname=FIRSTNAME, lastname=LASTNAME, birthdate=BIRTHDATE, person_id=ID_NUM))
    d = p2.as_dict()
    assert len(d) == 4 and d["firstname"] == FIRSTNAME and d["lastname"] == LASTNAME and d["birthdate"] == BIRTHDATE and d["person_id"] == ID_NUM
