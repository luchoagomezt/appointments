# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACcbf07f2c0b208633293cd1694331ed22"
auth_token = "a33034b421e763f8296d46b4c2fc1804"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+16205089020",
  to="+573209196254"
)
print(message.status)
print(message.sid)
