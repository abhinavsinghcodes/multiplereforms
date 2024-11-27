import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

def get_gender(name):
    if name.lower() in ["john", "mike", "james", "alex"]:
        return "male"
    else:
        return "female"

def random_delay(min_delay=1.5, max_delay=3.5):
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)

def random_user_agent():
    ua = UserAgent()
    return ua.random  # Get a random user-agent string

def process_names(name1, name2):
    chrome_options = Options()
    
    # Set up random User-Agent
    chrome_options.add_argument(f"user-agent={random_user_agent()}")
    
    # Add additional arguments to avoid detection
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("window-size=1200x600")

    # Start the WebDriver with random User-Agent
    service = Service("H:/Main-projects/MultipleReForms/chromedriver-win64/chromedriver.exe")  # Adjust path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get("https://www.getlinks.info/love/c/lceyrwz")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "yourname")))

    random_delay()  # Random delay before interacting with the page

    yourname_input = driver.find_element(By.ID, "yourname")
    yourname_input.send_keys(name1)

    gender1 = get_gender(name1)
    dropdown1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown']//div[@class='select']")))
    dropdown1.click()
    random_delay()

    if gender1 == "male":
        male_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "male")))
        male_option.click()
    else:
        female_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "female")))
        driver.execute_script("arguments[0].scrollIntoView(true);", female_option)
        WebDriverWait(driver, 10).until(EC.visibility_of(female_option))
        female_option.click()

    crushname_input = driver.find_element(By.ID, "crushname")
    crushname_input.send_keys(name2)
    random_delay()

    gender2 = get_gender(name2)
    dropdown2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown']//div[@class='select']")))
    dropdown2.click()
    random_delay()

    if gender2 == "male":
        male_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "male")))
        male_option.click()
    else:
        female_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "female")))
        driver.execute_script("arguments[0].scrollIntoView(true);", female_option)
        WebDriverWait(driver, 10).until(EC.visibility_of(female_option))
        female_option.click()

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    random_delay()

    driver.quit()

# Read names from the text files
with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    names1 = [line.strip() for line in file1.readlines()]
    names2 = [line.strip() for line in file2.readlines()]  # Ensure this file is aligned with file1

# Process each pair of names
for name1, name2 in zip(names1, names2):
    process_names(name1, name2)
