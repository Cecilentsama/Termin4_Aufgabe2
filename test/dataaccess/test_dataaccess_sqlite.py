from businesslayer.person import Person
from datalayer.dataaccess_sqlite import DataAccessSqlite
from datetime import date


def test_save_person():
    da = DataAccessSqlite("test_sqlite.db")
    da.save_person(Person(firstname="Test", lastname="it", birthdate=date(2000, 12, 31)))
    pl = da.load_person_list()
    assert len(pl) > 0


def test_delete_person():
    da = DataAccessSqlite("test_sqlite.db")
    len_list = len(da.load_person_list())
    p = da.save_person(Person(firstname="Test", lastname="it", birthdate=date(2000, 12, 31)))
    pl = da.load_person_list()
    assert len(pl) == len_list + 1
    da.delete_person(p)
    pl = da.load_person_list()
    assert len(pl) == len_list


def test_update_person():
    da = DataAccessSqlite("test_sqlite.db")
    p = da.save_person(Person(firstname="Test", lastname="it", birthdate=date(2000, 12, 31)))
    p.lastname = "Changed"
    da.update_person(p)
    pu = da.load_person(p.person_id)
    assert pu.lastname == p.lastname


def test_load_person_list():
    da = DataAccessSqlite("test_sqlite.db")
    pl = da.load_person_list()
    len_pl = len(pl)
    da.save_person(Person(firstname="Test", lastname="it", birthdate=date(2000, 12, 31)))
    pl = da.load_person_list()
    assert len(pl) > len_pl
