from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Path to chromedriver
chromedriver_path = "./chromedriver.exe"

# Initialize WebDriver
service = Service(chromedriver_path)
chrome_browser = webdriver.Chrome(service=service)

# Open the target website
chrome_browser.get("https://www.chatgpt.com")  # Replace with actual URL

# Wait for the editable div (instead of hidden textarea)
wait = WebDriverWait(chrome_browser, 10)
text_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']")))

# Scroll into view
chrome_browser.execute_script("arguments[0].scrollIntoView();", text_input)

# Type message
text_input.send_keys("Hello, this is Sagar!")

# Wait until the send button is enabled (not disabled)
send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='send-button' and not(@disabled)]")))


# Click the send button
send_button.click()

# Keep browser open for debugging
input("Press Enter to close the browser...")

# Close browser
chrome_browser.quit()
