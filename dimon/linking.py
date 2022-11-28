import requests
from selenium.webdriver.common.by import By
from name import linking
from name import clicking


class Links:
    def __init__(self, browser):
        self.browser = browser

    def checklink(self):
        burger_bar_links = self.browser.find_elemts(By.XPATH, "//a")
        clicklist = list()
        linkslist = list()
        for inlink in burger_bar_links:
            try:
                a = requests.head(inlink.get_attribute('href'))
                if a.status_code == 200:
                    clearlink = inlink.get_attribute('href')
                    print("Link is Valid:", clearlink)
                    if clearlink not in linklist:
                        linklist.append(clearlink)
                    else:
                        continue
                else:
                    print("Link is Invalid/Broken:", clearlink, inlink.get_attribute('outerHTML'))
            except:
                print('SomethingElseGetsWrong:', inlink.get_attribute('href'), inlink.get_attribute('outerHTML'))
        return clicklist
