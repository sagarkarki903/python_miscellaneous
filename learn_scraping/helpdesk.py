import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://webservices.ulm.edu/computersos"
login_url = f"{base_url}/user?destination=office-hours-message"
dashboard_url = f"{base_url}/tickets?field_ticket_id_value=&field_customer_name_value=&field_customer_building_tid=All&field_department_tid=All&field_assigned_to_uid=All&uid_touch=&field_status_tid%5B%5D=45&field_status_tid%5B%5D=46&field_status_tid%5B%5D=89&field_status_tid%5B%5D=87&field_status_tid%5B%5D=49&field_status_tid%5B%5D=48&field_status_tid%5B%5D=82&field_status_tid%5B%5D=47&keys=karkisa&items_per_page=35"  # Replace with the actual post-login page

# Start a session
session = requests.Session()

# Headers (simulate a browser to avoid bot detection)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Login payload
payload = {
    "name": "...",  # Replace with your actual username
    "pass": "...!",  # Replace with your actual password
    "op": "Log in",           # The submit button's name
    "form_id": "user_login"   # This ensures Drupal recognizes the form
}

# Step 1: Send Login Request
login_response = session.post(login_url, data=payload, headers=headers)

# Step 2: Check if Login Was Successful
if "Logout" in login_response.text or "Dashboard" in login_response.text:
    print("Login successful!")

    # Step 3: Scrape the Protected Page
    dashboard_response = session.get(dashboard_url, headers=headers)
    soup = BeautifulSoup(dashboard_response.text, "html.parser")

    # Extract any relevant data (modify based on your needs)
    print(soup.prettify())  # Print page content

else:
    print("Login failed! Check your credentials or site settings.")
