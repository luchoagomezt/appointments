from twilio.rest import Client


class TwilioMessenger:

    def send_sms_message(self, to: str, message: str) -> bool:
        return False
