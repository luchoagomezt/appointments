from lib.entities import HealthCareProvider
from lib.entities import Patient
from lib.entities import is_there_a_patient_with_this_name
from lib.entities import is_there_a_provider_with_this_name


class DataStorageTest:
    def retrieve_provider(self, first_name: str, last_name: str) -> HealthCareProvider:
        provider = None
        if first_name == "robin" and last_name == "hood":
            provider = HealthCareProvider(first_name="robin", last_name="hood", cell="1231231234")
        return provider

    def retrieve_patient(self, first_name: str, last_name: str) -> Patient:
        patient = None
        if first_name == "mon" and last_name == "patient":
            patient = HealthCareProvider(first_name="robin", last_name="hood", cell="1231231234")
        return patient


def test_patient_not_found():
    response = is_there_a_patient_with_this_name(first_name="your", last_name="patient", data_storage=DataStorageTest())
    assert not response


def test_patient_found():
    response = is_there_a_patient_with_this_name(first_name="mon", last_name="patient", data_storage=DataStorageTest())
    assert response


def test_provider_not_found():
    response = is_there_a_provider_with_this_name(first_name="jack", last_name="batman", data_storage=DataStorageTest())
    assert not response


def test_provider_found():
    response = is_there_a_provider_with_this_name(first_name="robin", last_name="hood", data_storage=DataStorageTest())
    assert response

