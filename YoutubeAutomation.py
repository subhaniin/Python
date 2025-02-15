from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com")
time.sleep(3)  # Wait for the page to load

# Find the search bar and enter the search term
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Selenium Python tutorials")
search_box.send_keys(Keys.RETURN)  # Press Enter

# Wait for results to load
time.sleep(5)

# Keep the browser open
print("Browser will remain open. Close it manually when done.")
input("Press Enter to exit and close the browser...")

# Close the browser after user input
driver.quit()