from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open ParaBank
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()

    # Wait until login elements are visible
    wait = WebDriverWait(driver, 10)

    # Find and enter credentials
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = driver.find_element(By.NAME, "password")
    
    username_input.send_keys("admin")
    password_input.send_keys("admin123")
    
    # Click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, "input.button")
    login_button.click()

    # Wait until login is successful
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Open New Account")))

    # Click "Open New Account"
    open_account_button = driver.find_element(By.LINK_TEXT, "Open New Account")
    open_account_button.click()

    # Wait for dropdown to load
    account_dropdown = wait.until(EC.presence_of_element_located((By.ID, "type")))
    
    # Select "Checking" from the dropdown
    Select(account_dropdown).select_by_visible_text("CHECKING")

    # Click "Open New Account" button
    open_account_submit = driver.find_element(By.CSS_SELECTOR, "input.button")
    open_account_submit.click()

    # Wait for confirmation page
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Account Opened!')]")))
    print("New Checking account opened successfully!")

    # Keep the browser open
    input("Press ENTER to close the browser...")

except Exception as e:
    print(f"Error: {e}")