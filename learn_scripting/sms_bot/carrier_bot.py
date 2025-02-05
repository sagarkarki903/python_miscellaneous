import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Recipient's phone number and carrier gateway
recipient_number = int(input("Enter Recipient's number")) # Replace with the recipient's number
carrier_gateway = "@txt.att.net"  # Replace with the correct carrier's domain

# From Email
email = "iamironman9731@gmail.com"
password = os.getenv('GOOGL_APP')

# SMS setup
to_address = f"{recipient_number}{carrier_gateway}"  # Uses variable
subject = input("Enter Subject: ")
body = input("Enter SMS body: ")

message = f"From: {email}\nTo: {to_address}\nSubject: {subject}\n\n{body}"


# Send email via SMTP
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to_address, message)

print("SMS sent successfully!")
