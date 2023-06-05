# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACcbf07f2c0b208633293cd1694331ed22"
auth_token = '1ebd44c245b18a05c3b57fb5bfcffb55'
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+16205089020",
  to="+573209196254"
)
print(message.status)
print(message.sid)
