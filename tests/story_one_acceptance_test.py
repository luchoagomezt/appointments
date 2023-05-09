from lib.entities import is_there_a_patient_with_this_name
from lib.entities import retrieve_patient_by_name
from lib.entities import is_there_a_provider_with_this_name
from lib.entities import retrieve_provider_by_name
from lib.entities import Appointment
from lib.entities import DataStorage
from lib.entities import send_appointment_alert
from lib.json_data_storage import JsonDataStorage
from lib.twilio_messenger import TwilioMessenger


def validate_patient_is_registered(full_name: dict, data_storage=DataStorage) -> None:
    if not is_there_a_patient_with_this_name(first_name=full_name["first_name"], last_name=full_name["last_name"],
                                             data_storage=data_storage):
        assert False, f"patient {full_name['first_name']} {full_name['last_name']} is not registered"


def validate_provider_is_registered(full_name: dict, data_storage=DataStorage) -> None:
    if not is_there_a_provider_with_this_name(first_name=full_name["first_name"], last_name=full_name["last_name"],
                                              data_storage=data_storage):
        assert False, f"provider {full_name['first_name']} {full_name['last_name']} is not registered"


def test_story_one():
    storage = JsonDataStorage("lib/test_data.json")

    patient_s_name = {"first_name": "mon", "last_name": "patient"}
    provider_s_name = {"first_name": "john", "last_name": "smith"}
    validate_patient_is_registered(patient_s_name, storage)
    validate_provider_is_registered(provider_s_name, storage)

    appointment_date = "13:30:00 05-11-2023"

    a_patient = retrieve_patient_by_name(first_name=patient_s_name["first_name"], last_name=patient_s_name["last_name"],
                                         data_storage=storage)
    a_provider = retrieve_provider_by_name(first_name=provider_s_name["first_name"],
                                           last_name=provider_s_name["last_name"],
                                           data_storage=storage)

    an_appointment = Appointment(date=appointment_date, patient=a_patient, provider=a_provider)
    assert send_appointment_alert(appointment=an_appointment, client=TwilioMessenger()), \
        f"Failed to send SMS to provider and patient"
