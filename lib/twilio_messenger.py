from twilio.rest import Client


class TwilioMessenger:
    def __init__(self):
        self.account_sid = "ACcbf07f2c0b208633293cd1694331ed22"
        self.auth_token = "a33034b421e763f8296d46b4c2fc1804"
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms_message(self, to: str, message: str) -> bool:
        msg = self.client.messages.create(
            body=message,
            from_="+16205089020",
            to="+573209196254"
        )
        return msg.sid is not None
