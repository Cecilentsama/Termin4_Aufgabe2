import pandas as pd
from businesslayer.person import Person
from common.common import person_list_as_dataframe, dataframe_as_person_list
from pathlib import Path
from uuid import uuid4


class DataAccessPandas:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.person_list = list()

    def save(self):
        person_list_as_dataframe(self.person_list).to_csv(self.filepath)

    def save_person(self, person: Person):
        person.person_id = DataAccessPandas.generate_id()
        self.person_list.append(person)
        self.save()
        return person

    def update_person(self, person: Person):
        p = next((p for p in self.person_list if p.person_id == person.person_id))
        self.person_list.remove(p)
        self.person_list.append(person)
        self.save()

    def delete_person(self, person: Person):
        p = next((p for p in self.person_list if p.person_id == person.person_id))
        self.person_list.remove(p)
        self.save()

    def load_person_list(self):
        file = Path(self.filepath)
        if file.exists():
            self.person_list = dataframe_as_person_list(pd.read_csv(self.filepath))
        return self.person_list

    @staticmethod
    def generate_id():
        return str(uuid4())
