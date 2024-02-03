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
PLAY_BTN = (880, 670)
START_BTN = (950, 630)
SEEN_BTN = (880, 550)
NEW_BTN = (1000, 550)


# setup
def setup():
    # Get the page source after interactions
    url = "https://humanbenchmark.com/tests/verbal-memory"
    driver.get(url)

    # login
    login()
    # click play
    pyautogui.click(PLAY_BTN)
    
    # click start
    time.sleep(3)
    pyautogui.click(START_BTN)

    return driver


# open website and get text
def process_word(driver, seen_words):
    # Wait for the "word" div to appear
    wait = WebDriverWait(driver, 1)
    word_div = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'word')))

    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find and scrape the word
    word_div = soup.find('div', class_='word')
    if word_div:
        value = word_div.text.strip()  # Get the text content within the div
        
        # check if word has been seen
        if check_for_word(value, seen_words):
            # click seen
            pyautogui.click(SEEN_BTN)
            print("seen")
        else:
            # click new
            pyautogui.click(NEW_BTN)
            print("new")
            # store word in seen arr
            seen_words.append(value)

    else:
        print("No 'word' div found")
        return 0



# check if word exists in seen words arr
def check_for_word(word, seen_words):
    if word in seen_words:
        return True
    else:
        return False



# main func
def automate():
    # init arr of seen words
    seen_words = []

    # setup
    driver = setup()

    # loop x times
    for i in range(100):
        # find and process word
        process_word(driver, seen_words)

    print(len(seen_words))



automate()
    

# Keep the browser window open for further interaction
input("Press Enter to close the browser window...")
driver.quit()