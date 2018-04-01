# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC94e44335f7486bdfba3be0cff727eb23"
auth_token = "204dc04075eaa9831526661843dbdbea"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+17604988288",
    from_="+14427776565",
    body="Hello from the other side")
