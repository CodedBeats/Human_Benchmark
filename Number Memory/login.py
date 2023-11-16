import os
import time
import pyautogui
from dotenv import load_dotenv

# load sensitive values
load_dotenv()
PASSWORD = os.getenv('PASSWORD')

# automatic login (god I'm lazy)
def login():
    time.sleep(5)
    # login btn
    pyautogui.click(x=1390, y=180)

    # username text box
    pyautogui.click(x=900, y=460)
    # username
    pyautogui.typewrite("SynthetIQ")
    # password text box
    pyautogui.click(x=830, y=530)
    # password
    pyautogui.typewrite(PASSWORD)
    time.sleep(0.1)

    # login btn
    pyautogui.click(x=940, y=600)

    time.sleep(2)
