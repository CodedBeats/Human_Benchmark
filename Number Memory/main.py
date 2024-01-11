# libraries
import time
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# functions
from login import login


# Set the path to the ChromeDriver executable
service = Service(executable_path='C:/Users/Luca/CodedBeats/Code/AI/Human_Benchmark_Test/chromedriver-win64/chromedriver.exe')

# Create a Chrome driver instance
options = Options()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver = webdriver.Chrome(service=service, options=options)

# constants
PLAY_BTN = (880, 720)
START_BTN = (950, 620)
SUBMIT_BTN = (950, 560)
NEXT_BTN = (950, 630)


# setup
def setup():
    # Get the page source after interactions
    url = "https://humanbenchmark.com/tests/number-memory"
    driver.get(url)

    # login
    login()
    # click play
    time.sleep(3)
    pyautogui.click(PLAY_BTN)
    
    # click start
    time.sleep(3)
    pyautogui.click(START_BTN)

    return driver


# open website and get text
def get_num(driver):
    # Wait for the "big-number" div to appear
    wait = WebDriverWait(driver, 1)
    big_number_div = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'big-number')))

    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find and scrape the number
    big_number_div = soup.find('div', class_='big-number')
    if big_number_div:
        value = big_number_div.text.strip()  # Get the text content within the div
        num = value
        print(num)
        return num
    else:
        print("No 'big-number' div found")
        return 0



# type out num
def type_text(inputNum, waitTime):
    # type fastttttt
    pyautogui.PAUSE = 0.01

    # wait for input to come up
    time.sleep(3 + waitTime)
    
    # type num
    pyautogui.typewrite(str(inputNum))



# main func
def automate():
    # setup
    driver = setup()

    # loop x times
    for i in range(50):
        # scrape number
        num = get_num(driver)
        print(f'Number {i} = {num}')
        
        # type number
        type_text(num, i)

        # submit
        pyautogui.click(SUBMIT_BTN)

        # next
        time.sleep(2)
        pyautogui.click(NEXT_BTN)



automate()
    

# Keep the browser window open for further interaction
input("Press Enter to close the browser window...")
driver.quit()
