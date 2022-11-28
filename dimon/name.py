import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from linking import Links
from clicking import Clicks


class Test:

    def testing(self):
        link = 'http://ouds.alm.su'
        browser = webdriver.Chrome()
        browser.get(link)
        print("it's going")
        # print(self.browser.page_source)
        browser.maximize_window()
        burger_bar_links = browser.find_elements(By.XPATH, "//a")

        a = Links(browser)
        clicklist = a.checklink()

        b = Clicks(browser)
        b.clicking(clicklist)


if __name__ == "__main__":
    start = Test()
    start.testing()
