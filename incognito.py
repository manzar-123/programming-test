import webbrowser
import time
import os

def myFunction():
  # open chrome with required URL
  url = 'https://www.google.com/search?q=python+is+amazing'
  chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe  %s'
  
  webbrowser.get(chrome_path).open_new(url)

# delay of 5 seconds
# time.sleep(5)

# print("manzar")
"""
import keyboard

# here goes your code... 

keyboard.press_and_release('ctrl+w') # closes the last tab


"""
# close the window of chrome
# os.system("taskkill /im chrome.exe /f")

