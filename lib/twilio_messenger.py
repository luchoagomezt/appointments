from twilio.rest import Client


def send_sms_message(message: str, to: str = "+573209196254") -> bool:
    account_sid = 'ACcbf07f2c0b208633293cd1694331ed22'
    auth_token = '1ebd44c245b18a05c3b57fb5bfcffb55'
    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        body=message,
        from_="+16205089020",
        to=to
    )
    return msg.sid is not None
