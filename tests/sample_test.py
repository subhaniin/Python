from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

# Check if the page loaded correctly
if "Example Domain" in driver.title:
    print("PASSED")
else:
    print("FAILED")

driver.quit()