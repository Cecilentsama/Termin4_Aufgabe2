from datalayer.dataaccess_rest import DataAccessRest
from businesslayer.person import Person as BLPerson
from datetime import date
import uvicorn
import pytest
from multiprocessing import Process
from webservice.service import webservice as app


def start_server():
    uvicorn.run(app=app, host="127.0.0.1", port=8000)


@pytest.fixture(scope="session", autouse=True)
def setup():
    proc = Process(target=start_server, args=())
    proc.start()
    yield
    proc.terminate()


def test_save_person():
    da = DataAccessRest("http://127.0.0.1:8000")
    p = da.save_person(BLPerson(firstname="Test", lastname="Test", birthdate=date(2000, 1, 1)))
    assert p.person_id is not None


def test_update_person():
    da = DataAccessRest("http://127.0.0.1:8000")

    p = da.save_person(BLPerson(firstname="Test1", lastname="Test1", birthdate=date(2000, 1, 1)))
    assert p.person_id is not None
    p.lastname = "CHANGE"
    p.birthdate = date.today()
    da.update_person(p)
    pu = da.get_person(p.person_id)
    assert p.lastname == pu.lastname and p.birthdate == pu.birthdate


def test_get_person():
    da = DataAccessRest("http://127.0.0.1:8000")

    p = da.save_person(BLPerson(firstname="Test1", lastname="Test1", birthdate=date(2000, 1, 1)))
    assert p.person_id is not None
    pg = da.get_person(p.person_id)
    assert p.person_id == pg.person_id


def test_delete_person():
    da = DataAccessRest("http://127.0.0.1:8000")

    p = da.save_person(BLPerson(firstname="Test1", lastname="Test1", birthdate=date(2000, 1, 1)))
    assert p.person_id is not None
    pg = da.get_person(p.person_id)
    assert p.person_id == pg.person_id
    da.delete_person(p)
    pd = da.get_person(p.person_id)
    assert pd is None


def test_load_person_list():
    da = DataAccessRest("http://127.0.0.1:8000")

    p = da.save_person(BLPerson(firstname="Test1", lastname="Test1", birthdate=date(2000, 1, 1)))
    assert p.person_id is not None
    plist = da.load_person_list()
    assert len(plist) > 0
