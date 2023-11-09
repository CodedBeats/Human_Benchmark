import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# load sensitive values
load_dotenv()
PASSWORD = os.getenv('PASSWORD')

# automatic login (god I'm lazy)
def login(driver):
    # Open the website
    url = "https://humanbenchmark.com/"
    driver.get(url)
    time.sleep(5)

    # make clicks slower while logging in
    pyautogui.PAUSE = 2

    # login btn
    pyautogui.click(x=1390, y=180)
    # username text box
    pyautogui.click(x=900, y=460)
    # username
    pyautogui.PAUSE = 0.1
    pyautogui.typewrite("SynthetIQ")
    pyautogui.PAUSE = 2
    # password text box
    pyautogui.click(x=830, y=530)
    # password
    pyautogui.PAUSE = 0.1
    pyautogui.typewrite(PASSWORD)
    pyautogui.PAUSE = 2
    # login btn
    pyautogui.click(x=940, y=600)

    time.sleep(3)
