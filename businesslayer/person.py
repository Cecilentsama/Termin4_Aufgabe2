from model.model import Person as DAPerson
from common.functions import age_from_date


class Person:
    PERSON_ATTRIBUTE_NAME_FIRSTNAME = "firstname"
    PERSON_ATTRIBUTE_NAME_LASTNAME = "lastname"
    PERSON_ATTRIBUTE_NAME_BIRTHDATE = "birthdate"
    PERSON_ATTRIBUTE_NAME_ID = "person_id"

    def __init__(self, firstname=None, lastname=None, birthdate=None, person_id=None, person=None):
        if person is None:
            self._person = DAPerson(firstname=firstname, lastname=lastname, birthdate=birthdate, person_id=person_id)
        else:
            self._person = person

    @property
    def firstname(self):
        return self._person.firstname

    @firstname.setter
    def firstname(self, firstname):
        self._person.firstname = firstname

    @property
    def lastname(self):
        return self._person.lastname

    @lastname.setter
    def lastname(self, lastname):
        self._person.lastname = lastname

    @property
    def birthdate(self):
        return self._person.birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        self._person.birthdate = birthdate

    @property
    def person_id(self):
        return self._person.person_id

    @person_id.setter
    def person_id(self, person_id):
        self._person.person_id = person_id

    def age(self):
        return age_from_date(self.birthdate)

    def __str__(self):
        return f'Person: {self.firstname} {self.lastname} {self.birthdate}'

    def as_dict(self):
        return {
            Person.PERSON_ATTRIBUTE_NAME_ID: self.person_id,
            Person.PERSON_ATTRIBUTE_NAME_FIRSTNAME: self.firstname,
            Person.PERSON_ATTRIBUTE_NAME_LASTNAME: self.lastname,
            Person.PERSON_ATTRIBUTE_NAME_BIRTHDATE: self.birthdate
        }
