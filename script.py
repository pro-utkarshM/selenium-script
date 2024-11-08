import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Import By class

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless (without GUI)
chrome_options.add_argument("--no-sandbox")  # To avoid sandboxing issues
chrome_options.add_argument("--disable-dev-shm-usage")  # To avoid issues with shared memory

# Automatically download the correct version of ChromeDriver using webdriver_manager
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the desired webpage
driver.get('https://github.com/royswastik/intelligent-team-building-recommendation-system')  # Replace with your desired URL

# Wait for the page to load
time.sleep(2)  # Adjust the time based on page load time

# Extract page title as an example
page_title = driver.title
print(f"Page Title: {page_title}")

# Extract the first heading (h1) from the page using the updated find_element method
heading = driver.find_element(By.TAG_NAME, 'h1').text
print(f"First Heading: {heading}")

# Close the driver
driver.quit()
