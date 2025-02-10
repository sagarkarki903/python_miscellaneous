import requests
from bs4 import BeautifulSoup
# import re


# Base URL
base_url = "https://webservices.ulm.edu/computersos"
search_user = input("Username: ")
password = input("Password: ")

login_url = f"{base_url}/user?destination=office-hours-message"
# dashboard_url = "f{base_url}/office-hours-message"
# Start a session
session = requests.Session()

# Headers (simulate a browser to avoid bot detection)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Login payload
payload = {
    "name": search_user,
    "pass": password,
    "op": "Log in",
    "form_id": "user_login"
}

# Step 1: Send Login Request
login_response = session.post(login_url, data=payload, headers=headers)


soup = BeautifulSoup(login_response.text, "html.parser")


if "Log out?" in login_response.text:
    print(True)

# dashboard_response = session.get(dashboard_url, headers=headers)
# soup = BeautifulSoup(dashboard_response.text, "html.parser")


