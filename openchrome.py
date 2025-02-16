import webbrowser
import time
import pyautogui

# Open Google Homepage
webbrowser.open("https://www.google.com")

# Wait for Google to load
time.sleep(3)

# Type "Wikipedia" in the search bar and press Enter
pyautogui.write("Wikipedia", interval=0.1)
pyautogui.press("enter")