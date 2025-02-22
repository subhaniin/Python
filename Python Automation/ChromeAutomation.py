from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the OrangeHRM website
driver.get("https://www.orangehrm.com/")

# Keep the browser open for a while (optional)
input("Press Enter to close...")

# Close the browser
driver.quit()
