from twilio.rest import Client
from dotenv import load_dotenv
import os

#loading .env variables
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp = os.getenv('TWILIO_WHATSAPP_NUMBER')
to_whatsapp = os.getenv('RECIPIENT_NUMBER')

# Initializing Twilio client
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_= from_whatsapp,
  body="Hey Sagar! This is Tony. You're doing a great job!",
  to=to_whatsapp
)

print(message.sid)