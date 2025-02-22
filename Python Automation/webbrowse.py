import webbrowser
import time
import pyautogui

# Open YouTube
webbrowser.open("https://www.youtube.com")

# Wait for YouTube to load
time.sleep(7)

# Click on the search bar (You may need to adjust coordinates)
pyautogui.click(x=888, y=150)  # Adjust based on your screen resolution

# Type "Selenium Python"
pyautogui.write("Selenium Python", interval=0.1)

# Press Enter to search
pyautogui.press("enter")

# Click on 3rd video
time.sleep(5)
pyautogui.click(x=888, y=850)  # Adjust based on your screen resolution