import json
from lib.entities import HealthCareProvider
from lib.entities import Patient


def init_storage(path: str) -> object:
    with open(path, 'r') as myfile:
        data = myfile.read()
    return json.loads(data)


class JsonDataStorage:
    def __init__(self, path: str):
        self.storage = init_storage(path)

    def retrieve_provider(self, first_name: str, last_name: str) -> HealthCareProvider:
        providers = [p for p in self.storage["providers"] if p["first_name"] == first_name and p["last_name"] == last_name]
        return HealthCareProvider(**providers[0]) if len(providers) > 0 else None

    def retrieve_patient(self, first_name: str, last_name: str) -> Patient:
        patients = [p for p in self.storage["patients"] if p["first_name"] == first_name and p["last_name"] == last_name]
        return Patient(**patients[0]) if len(patients) > 0 else None
