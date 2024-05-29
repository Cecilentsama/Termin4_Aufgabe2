from datalayer.dataaccess_pandas import DataAccessPandas
from businesslayer.person import Person
from datetime import date


def test_save():
    da_pandas = DataAccessPandas("test_pandas.csv")
    person = Person(firstname="Max", lastname="Test", birthdate=date(2000, 1, 31))

    size_person_list_before = len(da_pandas.load_person_list())
    da_pandas.save_person(person)
    person_list_after = da_pandas.load_person_list()

    assert size_person_list_before < len(person_list_after)


def test_load_person_list():
    da_pandas = DataAccessPandas("test_pandas.csv")
    person_list = da_pandas.load_person_list()
    assert person_list is not None

    size_person_list_before = len(person_list)
    person = Person(firstname="Max", lastname="Test", birthdate=date(2000, 1, 31))
    da_pandas.save_person(person)
    person_list_after = da_pandas.load_person_list()
    assert size_person_list_before + 1 == len(person_list_after)


def test_update():
    da_pandas = DataAccessPandas("test_pandas.csv")
    person_list = da_pandas.load_person_list()
    assert person_list is not None

    person = da_pandas.save_person(Person(firstname="Update", lastname="Test", birthdate=date(2000, 1, 31)))
    person.firstname = "Update1"
    person.lastname = "Test1"
    person.birthdate = date(1999, 1, 1)
    da_pandas.update_person(person)
    person_list = da_pandas.load_person_list()
    updt_person = next((p for p in person_list if p.person_id == person.person_id))
    assert updt_person.firstname == "Update1"
    assert updt_person.lastname == "Test1"
    assert updt_person.birthdate == date(1999, 1, 1)


def test_delete():
    da_pandas = DataAccessPandas("test_pandas.csv")
    person_list = da_pandas.load_person_list()
    assert person_list is not None
    size_person_list_before = len(person_list)
    person = da_pandas.save_person(Person(firstname="Update", lastname="Test", birthdate=date(2000, 1, 31)))
    assert size_person_list_before < len(da_pandas.load_person_list())
    da_pandas.delete_person(person)
    assert size_person_list_before == len(da_pandas.load_person_list())
