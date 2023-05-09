from dataclasses import dataclass
from typing import Protocol


@dataclass()
class Patient:
    """
    Represents a Patient, the datastorage contains information for the patient
    """
    first_name: str
    last_name: str
    cell: str


@dataclass()
class HealthCareProvider:
    """
    Represents a Health Care Provider, there is correspondence in the data storage
    """
    first_name: str
    last_name: str
    cell: str


@dataclass()
class Appointment:
    """
    Represents an appointment between a Patient and a Providers, there is not yet correspondence in the data storage
    """
    date: str
    patient: Patient
    provider: HealthCareProvider


class Messenger(Protocol):
    """
    A protocol, or interface, for the messengers. Defines the contract only, it does not have an implementation
    """
    def send_sms_message(self, to: str, message: str) -> bool:
        ...


class DataStorage(Protocol):
    """
    Interface for the data storage, contract only
    """
    def retrieve_provider(self, first_name: str, last_name: str) -> HealthCareProvider:
        ...

    def retrieve_patient(self, first_name: str, last_name: str) -> Patient:
        ...


def send_appointment_alert(appointment: Appointment, client: Messenger) -> bool:
    """
    Sends an appointment alert via the messenger to both the provider and patient
    :param appointment: The appointment.
    :param client: A client or messenger, sends the alert to both the provider and patient
    :return:
    """
    msg = f"Hello {appointment.patient.first_name} {appointment.patient.last_name} Confirming your {appointment.date} appointment"
    return client.send_sms_message(to="+573209196254", message=msg)


def is_there_a_patient_with_this_name(first_name: str, last_name: str, data_storage: DataStorage) -> bool:
    """
    checks if there is a patient by fist and last name in the storage

    :param first_name:
    :param last_name:
    :param data_storage: the dependency, injected to the method here
    :return: True if there is a patient with this name in the data storage
    """
    a_patient = data_storage.retrieve_patient(first_name, last_name)
    return a_patient is not None


def is_there_a_provider_with_this_name(first_name: str, last_name: str, data_storage: DataStorage) -> bool:
    """
    checks if there is a provider by fist and last name in the storage

    :param first_name:
    :param last_name:
    :param data_storage:
    :return: True if there is a provider with this name in the data storage
    """
    a_health_care_provider = data_storage.retrieve_provider(first_name, last_name)
    return a_health_care_provider is not None


def retrieve_provider_by_name(first_name: str, last_name: str, data_storage: DataStorage) -> HealthCareProvider:
    """
    Retrieves a Provider by name from the data storage
    :param first_name:
    :param last_name:
    :param data_storage:
    :return: A Provider, None if there is not a provider in the data storage
    """
    a_health_care_provider = data_storage.retrieve_provider(first_name, last_name)
    return a_health_care_provider


def retrieve_patient_by_name(first_name: str, last_name: str, data_storage: DataStorage) -> Patient:
    """
    Retrieves a Patient by name from the data storage
    :param first_name:
    :param last_name:
    :param data_storage:
    :return: A Patient, None if there is not a patient in the data storage
    """
    a_patient = data_storage.retrieve_patient(first_name, last_name)
    return a_patient
