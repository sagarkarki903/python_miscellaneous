import requests
from bs4 import BeautifulSoup
import re

# Base URL
base_url = "https://webservices.ulm.edu/computersos"
search_user = input("Username: ")
password = input("Password: ")
desired_user = input("Whose ticket count do you want to check? ")



login_url = f"{base_url}/user?destination=office-hours-message"

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

# Step 2: Check if Login Was Successful
if "Log out?" in login_response.text:
    print(" Login successful!\n")

    count = 0
    page = 0
    last_page_data = None  # Store previous page content to detect repetition

    while True:
        # Construct URL dynamically for each page
        dashboard_url = f"{base_url}/tickets?field_ticket_id_value=&field_customer_name_value=&field_customer_building_tid=All&field_department_tid=All&field_assigned_to_uid=All&uid_touch={desired_user}&field_status_tid%5B0%5D=47&keys=&items_per_page=35&page={page}"

        print(f"Scraping Page {page + 1}...")  # Indicate progress

        # Step 3: Scrape the Protected Page
        dashboard_response = session.get(dashboard_url, headers=headers)
        soup = BeautifulSoup(dashboard_response.text, "html.parser")

        # Find all table rows
        all_table = soup.find("tbody").find_all("tr")

        # Stop if the page contains the same data as the last one (infinite loop prevention)
        current_page_data = [row.text.strip() for row in all_table]
        if current_page_data == last_page_data:
            print(" Reached duplicate page. Stopping pagination.\n")
            break
        last_page_data = current_page_data  # Update last_page_data for next iteration

        #  Stop if there is no valid ticket data
        if not all_table:
            print(" No more pages to scrape. Stopping.\n")
            break

        for row in all_table:
            td_elements = row.find_all('td')

            if len(td_elements) > 7:  #  Ensure at least 8 <td> elements exist
                user_result = td_elements[7].text.strip()
                clean_text = re.sub(r"\s*\[.*?\]\s*", "", user_result).strip()

                if clean_text == desired_user:
                    count += 1

        page += 1  # Move to the next page

    print(f"🔢 Total Count for {desired_user}: {count}")

else:
    print("Login failed! Check your credentials or site settings.")
