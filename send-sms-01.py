from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC9ed7870ee65d37406592045ff1bc46a9'
auth_token = '8f596745a7082b5bf02f761e27363188'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello from Python!',
    from_='+250788862399',
    to='+250789449645'
)

print(message.sid)
