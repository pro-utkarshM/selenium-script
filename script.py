import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless (without GUI)
chrome_options.add_argument("--no-sandbox")  # To avoid sandboxing issues
chrome_options.add_argument("--disable-dev-shm-usage")  # To avoid issues with shared memory

# Automatically download the correct version of ChromeDriver using webdriver_manager
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the research paper URL (e.g., an arXiv or publisher page)
driver.get('https://arxiv.org/abs/2301.09856')  # Example paper URL (replace with actual)

# Wait for the page to load
time.sleep(3)  # Adjust the time based on page load time

# Extract title, authors, and abstract (you need to inspect the specific webpage)
title = driver.find_element(By.TAG_NAME, 'h1').text  # Title for arXiv
authors = driver.find_element(By.CSS_SELECTOR, '.authors').text  # Authors for arXiv
abstract = driver.find_element(By.CSS_SELECTOR, 'blockquote.abstract').text  # Abstract for arXiv

# Print extracted content
print(f"Title: {title}")
print(f"Authors: {authors}")
print(f"Abstract: {abstract}")

# Close the driver
driver.quit()
