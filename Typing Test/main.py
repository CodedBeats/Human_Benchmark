import os
import time
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# load sensitive values
load_dotenv()
PASSWORD = os.getenv('PASSWORD')

# setup text arr
textArr = []


# Set the path to the ChromeDriver executable
service = Service(executable_path='C:/Users/Luca/CodedBeats/Code/AI/Human_Benchmark_Test/chromedriver-win64/chromedriver.exe')

# Create a Chrome driver instance
options = Options()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver = webdriver.Chrome(service=service, options=options)


# automatic login (god I'm lazy)
def login():
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

# open website and get text
def get_text():
    # Open the website and continue with your scraping code
    url = "https://humanbenchmark.com/"
    driver.get(url)
    time.sleep(5)

    # login
    login()

    # Get the page source after interactions
    url = "https://humanbenchmark.com/tests/typing"
    driver.get(url)
    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find and scrape span elements using BeautifulSoup
    span_elements = soup.find_all('span')

    # Extract text from span elements and print it
    for span in span_elements:
        print(span.text, sep=' ', end='', flush=True)
        textArr.append(span.text)


# type out text
def type_text():
    # type fastttttt
    pyautogui.PAUSE = 0.01

    for char in textArr:
        pyautogui.typewrite(char)



# run functions
get_text()
type_text()
    

# Keep the browser window open for further interaction
input("Press Enter to close the browser window...")
driver.quit()