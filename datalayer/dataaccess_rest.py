import requests
from http import HTTPStatus
from model.model import Person as DAPerson
from businesslayer.person import Person as BLPerson


class DataAccessRest:
    def __init__(self, protocol_host_port: str):
        self.protocol_host_port = protocol_host_port

    def save_person(self, person: BLPerson):
        response = requests.post(f'{self.protocol_host_port}/person/', data=person._person.model_dump_json())
        if response.status_code == HTTPStatus.CREATED:
            person._person = DAPerson.model_validate_json(response.content)
            return person
        else:
            print("ERROR")

    def delete_person(self, person: BLPerson):
        pass

    def update_person(self, person: BLPerson):
        pass

    def load_person_list(self):
        response = requests.get(f'{self.protocol_host_port}/persons')
        ret = list()
        if response.status_code == HTTPStatus.OK:
            for data in response.json():
                person = BLPerson(person=DAPerson.model_validate(data))
                ret.append(person)
        else:
            print("ERROR")
        return ret

    def get_person(self, person_id: int):
        pass
