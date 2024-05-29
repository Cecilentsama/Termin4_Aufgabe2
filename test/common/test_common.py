from common.common import dataframe_as_person_list, person_list_as_dataframe
from datetime import date
from businesslayer.person import Person
from model.model import Person as DAPerson
import pandas as pd


def test_person_list_as_dataframe():
    try:
        person_list_as_dataframe(None)
    except TypeError:
        assert True
    r2 = person_list_as_dataframe([])
    assert len(r2) == 0
    list_p = [Person(firstname="Test", lastname="1", birthdate=date.today()),
              Person(firstname="Test", lastname="2", birthdate=date.today(), person_id=8599),
              Person(firstname="Test", lastname="3", birthdate=date.today(), person_id='abcd-efgh-1234-5678'),
              Person(person=DAPerson(firstname="Test", lastname="4", birthdate=date.today())),
              Person(person=DAPerson(firstname="Test", lastname="4", birthdate=date.today(), person_id=9599)),
              Person(person=DAPerson(firstname="Test", lastname="4", birthdate=date.today(), person_id='5678-efgh-1234-abcd'))
              ]
    r3 = person_list_as_dataframe(list_p)
    assert len(r3) == 6


def test_dataframe_as_person_list():
    try:
        dataframe_as_person_list(None)
    except TypeError:
        assert True
    r2 = dataframe_as_person_list(pd.DataFrame())
    assert len(r2) == 0
    df = pd.DataFrame([{"firstname": "Test", "lastname": "1", "birthdate": "2000-01-01", "person_id": 12222},
                       {"firstname": "Test", "lastname": "1", "birthdate": "2000-01-01", "person_id": "abcd-efgh-1234-5678"}])
    r3 = dataframe_as_person_list(df)
    assert len(r3) == 2
