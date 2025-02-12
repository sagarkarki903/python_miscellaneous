from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Path to chromedriver
chromedriver_path = "./chromedriver.exe"

# Initialize WebDriver
service = Service(chromedriver_path)
chrome_browser = webdriver.Chrome(service=service)

# Open the target website
chrome_browser.get("https://webapps.ulm.edu/myulm/login")

# Wait for the page to load completely (optional but recommended)
chrome_browser.implicitly_wait(5)  # Waits up to 5 seconds if elements are not found

# Wait for the page to load
chrome_browser.implicitly_wait(5)

# Locate the "Need Help?" link using XPath
help_link = chrome_browser.find_element(By.XPATH, "//span[@class='hlp-text-b']/a")

# Click the link (optional)
help_link.click()

cwid_input = chrome_browser.find_element(By.ID, "edit-cwid")

cwid_input.send_keys("30135337")

# Locate the button using ID and click it
submit_button = chrome_browser.find_element(By.ID, "edit-actions")
submit_button.click()

# Keep browser open until user presses Enter
input("Press Enter to close the browser...")

chrome_browser.quit()  # Close the browser after user input
