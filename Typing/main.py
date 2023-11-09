# libraries
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# functions
from login import login


# setup text arr
textArr = []


# Set the path to the ChromeDriver executable
service = Service(executable_path='C:/Users/Luca/CodedBeats/Code/AI/Human_Benchmark_Test/chromedriver-win64/chromedriver.exe')

# Create a Chrome driver instance
options = Options()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver = webdriver.Chrome(service=service, options=options)


# open website and get text
def get_text():
    # login
    login(driver)

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