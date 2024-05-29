import sqlite3
from model.model import Person


class DataAccessSqlite:
    def __init__(self, database_name: str):
        self.db_connection = sqlite3.connect(database_name, check_same_thread=False)
        self.db_connection.execute("CREATE TABLE IF NOT EXISTS person(person_id INTEGER PRIMARY KEY, firstname TEXT NOT NULL, lastname NOT NULL, birthdate TEXT NOT NULL)")

    def save_person(self, person: Person):
        res = self.db_connection.execute(
            f'INSERT INTO person (firstname, lastname, birthdate) VALUES("{person.firstname}", "{person.lastname}", "{person.birthdate}")')
        self.db_connection.commit()
        person.person_id = res.lastrowid
        return person

    def delete_person(self, person_id: int):
        self.db_connection.execute(f'DELETE FROM person WHERE person_id={person_id}')
        self.db_connection.commit()

    def update_person(self, person: Person):
        self.db_connection.execute(
            f'UPDATE person SET firstname="{person.firstname}", lastname="{person.lastname}", birthdate="{person.birthdate}" WHERE person_id={person.person_id}')
        self.db_connection.commit()
        return person

    def load_person_list(self):
        ret = list()
        qry_result = self.db_connection.execute("SELECT * from person")
        for person_record in qry_result:
            ret.append(DataAccessSqlite.construct_person(person_record))
        return ret

    def load_person(self, person_id: int):
        qry_result = self.db_connection.execute(f"SELECT * from person WHERE person_id={person_id}")
        person_record = qry_result.fetchone()
        return DataAccessSqlite.construct_person(person_record)

    @staticmethod
    def construct_person(person_record):
        if person_record:
            return Person(person_id=person_record[0], firstname=person_record[1], lastname=person_record[2], birthdate=person_record[3])
