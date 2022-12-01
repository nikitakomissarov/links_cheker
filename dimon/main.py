from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from asks import Links
from clicking import Clicks

url = 'http://ouds.alm.su'

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(url)
    start = Links(driver)
    start.requesting()
