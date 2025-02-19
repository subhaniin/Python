import pyautogui
import webbrowser


webbrowser.open("https://www.youtube.com")
pyautogui.sleep(5)

print(pyautogui.position())  # Move your mouse to the search bar and run this