from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics")

element = driver.find_element_by_id("yearDD")

all_options = element.find_elements(by=By.TAG_NAME, value="option")

time.sleep(10)

for option in all_options:
    option.click()
    time.sleep(5)

input('Press enter to close the window...')