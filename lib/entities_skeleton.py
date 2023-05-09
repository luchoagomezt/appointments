from dataclasses import dataclass
from typing import Protocol


@dataclass()
class Patient:
    first_name: str
    middle_name: str
    last_name: str
    cell: str


@dataclass()
class HealthCareProvider:
    first_name: str
    middle_name: str
    last_name: str
    cell: str


@dataclass()
class Appointment:
    date: str
    patient: Patient
    provider: HealthCareProvider


class Messenger(Protocol):
    def send_sms_message(self, to: str, message: str) -> bool:
        ...


class DataStorage(Protocol):
    def retrieve_provider(self, first_name: str, last_name: str) -> HealthCareProvider:
        ...

    def retrieve_patient(self, first_name: str, last_name: str) -> Patient:
        ...


def send_appointment_alert(appointment: Appointment, client: Messenger) -> bool:
    """

    :param appointment:
    :param client:
    :return:
    """
    return False


def is_there_a_patient_with_this_name(first_name: str, last_name: str, data_storage: DataStorage) -> bool:
    """
    :param first_name:
    :param last_name:
    :param data_storage:
    :return:
    """
    return False


def is_there_a_provider_with_this_name(first_name: str, last_name: str, data_storage: DataStorage) -> bool:
    """

    :param first_name:
    :param last_name:
    :param data_storage:
    :return:
    """
    return False


def retrieve_provider_by_name(first_name: str, last_name: str, data_storage: DataStorage) -> HealthCareProvider:
    """

    :param first_name:
    :param last_name:
    :param data_storage:
    :return:
    """
    return None


def retrieve_patient_by_name(first_name: str, last_name: str, data_storage: DataStorage) -> Patient:
    """

    :param first_name:
    :param last_name:
    :param data_storage:
    :return:
    """
    return None
