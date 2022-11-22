import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://ouds.alm.su/"








class Pages():

    def __init__(self):
        self.link = link

    def just_start(self, link):
        self.link = link
        print("it's going")
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)
        return browser


    def link_testingfirst(self, browser):
        browser.maximize_window()
        try:
            burger_bar_links = browser.find_elements(By.CLASS_NAME, "header__nav_link")


            for inlink in burger_bar_links:
                if (requests.head(inlink.get_attribute('href')).status_code == 200):
                    print("Link is Valid")
                    print(inlink.get_attribute('href'))
                    browser.implicitly_wait(5)

                else:
                    print("Link is Invalid/Broken")

        finally:
            browser.quit()




if __name__ == "__main__":
    start = Pages()
    start.link_testingfirst(start.just_start(link))


