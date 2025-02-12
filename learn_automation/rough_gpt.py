from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup  # ✅ Use BeautifulSoup for better text extraction

# ✅ Attach Selenium to running Chrome session
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "127.0.0.1:9222"

service = Service("./chromedriver.exe")
chrome_browser = webdriver.Chrome(service=service, options=chrome_options)

# ✅ Open ChatGPT
chrome_browser.get("https://chat.openai.com/")

# ✅ Wait for the input text area
wait = WebDriverWait(chrome_browser, 30)
text_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']")))

# ✅ Type a message
message = "write me 3 lines of a song"
text_input.send_keys(message)
text_input.send_keys(Keys.ENTER)

# ✅ Wait for ChatGPT's response
print("Waiting for ChatGPT's response...")
response_div = wait.until(EC.presence_of_element_located((
    By.XPATH, "//div[@data-message-author-role='assistant']//div[contains(@class, 'markdown')]"
)))
print("Response element found!")

# ✅ Extract full response, including handling <br> and <strong>
paragraphs = response_div.find_elements(By.TAG_NAME, "p")
full_response = ""

for p in paragraphs:
    raw_html = p.get_attribute("innerHTML")  # Get raw HTML
    soup = BeautifulSoup(raw_html, "html.parser")  # Parse with BeautifulSoup
    text = soup.get_text(separator="\n").strip()  # Extract text with <br> converted to \n
    full_response += text + "\n"

# ✅ Print the cleaned response
print("ChatGPT Response:", full_response.strip())

# ✅ Keep browser open for debugging
input("Press Enter to close the browser...")

# ✅ Close browser
chrome_browser.quit()
