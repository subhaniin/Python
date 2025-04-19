from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.get("https://www.codingninjas.com/")

# Maximize window (optional)
driver.maximize_window()

# Wait for the Login button and click it
try:
    wait = WebDriverWait(driver, 10)
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Login']")))
    login_btn.click()
    print("Login button clicked. You can now log in manually.")
except:
    print("Login button not found.")

# Keep browser open for manual login
input("Press Enter after logging in manually to continue...")

# (Optional) You can now continue automation after login here

# Close the driver if done
# driver.quit()