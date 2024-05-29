import sqlite3
from businesslayer.person import Person
from datetime import date


class DataAccessSqlite:
    def __init__(self, database_name: str):
        self.db_connection = sqlite3.connect(database_name, check_same_thread=False)
        self.db_connection.execute(
            "CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY, firstname TEXT NOT NULL, lastname NOT NULL, birthdate TEXT NOT NULL)")

    def save_person(self, person: Person):
        res = self.db_connection.execute(
            f'INSERT INTO person (firstname, lastname, birthdate) VALUES("{person.firstname}", "{person.lastname}", "{person.birthdate}")')
        self.db_connection.commit()
        person.person_id = res.lastrowid
        return person

    def delete_person(self, person: Person):
        self.db_connection.execute(f'DELETE FROM person WHERE id={person.person_id}')
        self.db_connection.commit()

    def update_person(self, person: Person):
        self.db_connection.execute(
            f'UPDATE person SET firstname="{person.firstname}", lastname="{person.lastname}", birthdate="{person.birthdate}" WHERE id={person.person_id}')
        self.db_connection.commit()

    def load_person_list(self):
        ret = list()
        res = self.db_connection.execute("SELECT * from person")
        for pos in res:
            ret.append(Person(person_id=pos[0], firstname=pos[1], lastname=pos[2], birthdate=date.fromisoformat(pos[3])))
        return ret

    def load_person(self, person_id: str):
        qry_result = self.db_connection.execute(f'SELECT * from person WHERE id={person_id}')
        person_record = qry_result.fetchone()
        if person_record:
            return Person(person_id=person_record[0], firstname=person_record[1], lastname=person_record[2], birthdate=date.fromisoformat(person_record[3]))
