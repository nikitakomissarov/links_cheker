import asks
from selenium.webdriver.common.by import By
from selenium import webdriver

class Links:

    def linking(self, browser):
        burger_bar_links = browser.find_elements(By.XPATH, "//a")
        clicklist = list(burger_bar_links)
        linklist = list()
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
