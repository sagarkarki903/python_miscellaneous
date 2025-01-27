import  smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

#Loading environment variables from the .env
load_dotenv()
app_pass = os.getenv("PASSWORD")

email = EmailMessage()
email['from'] = "Tony Stark<iamironman@gmail.com>"
email["to"] = input("To: ")
email["subject"] = input("Subject: ")
email.set_content(input("Message: "))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp_conf:
    smtp_conf.ehlo()
    smtp_conf.starttls()
    smtp_conf.login("iamironman9731@gmail.com", app_pass)
    smtp_conf.send_message(email)
    print("Email Sent Success...........")
