import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Avoid sandboxing issues
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues

# Specify the correct ChromeDriver binary path manually
chromedriver_path = "/home/gilfoyle/.wdm/drivers/chromedriver/linux64/131.0.6778.69/chromedriver-linux64/chromedriver"
service = Service(chromedriver_path)

# Debug: Print the path to ensure correctness
print(f"Using ChromeDriver binary at: {chromedriver_path}")

# Initialize WebDriver with the specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the URL to scrape
url = "https://arxiv.org/abs/2301.09856"
print(f"Fetching data from: {url}")

try:
    # Open the webpage
    driver.get(url)

    # Extract elements using WebDriverWait for robustness
    wait = WebDriverWait(driver, 10)
    title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
    authors = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".authors"))).text
    abstract_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "blockquote.abstract")))
    abstract = abstract_element.text.replace("Abstract: ", "").strip()

    # Print the extracted information
    print("\nExtracted Information:")
    print(f"Title: {title}")
    print(f"Authors: {authors}")
    print(f"Abstract: {abstract}")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver
    driver.quit()
    print("WebDriver closed.")
