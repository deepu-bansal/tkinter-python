# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC117dbe7e6ccb73c318283d6d51673d1a"
auth_token = "3a469c0263114a4567f1472bcff4193c"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+13203356803",
  to="+918890752305"
)
# print(message.sid)