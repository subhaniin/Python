from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Check if the page loaded correctly
if "Google" in driver.title:
    print("PASSED")
else:
    print("FAILED")

driver.quit()