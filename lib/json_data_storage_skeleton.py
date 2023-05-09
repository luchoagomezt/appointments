from lib.entities import HealthCareProvider
from lib.entities import Patient


class JsonDataStorage:

    def retrieve_provider(self, first_name: str, last_name: str) -> HealthCareProvider:
        return None

    def retrieve_patient(self, first_name: str, last_name: str) -> Patient:
        return None
