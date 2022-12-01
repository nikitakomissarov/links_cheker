
import requests
from selenium.webdriver.common.by import By

from selenium import webdriver

# class Links:
#
#     def __init__(self, url):
#         self.url = url
#
#     def requesting(self):
#         html = urllib.request.urlopen(self.url).read()
#         soup = BeautifulSoup(html, 'html.parser')
#         linksbufer = soup.findAll('a')
#         for link in linksbufer:
#             print(link.get('href'))

class Links:

    def __init__(self, browser):
        self.browser = browser

    def requesting(self):
        burger_bar_links = self.browser.find_elements(By.XPATH, "//a")
        linklist = list(burger_bar_links)
        for link in burger_bar_links:
            try:
                a = requests.head(link.get_attribute('href'))
                if a.status_code == 200:
                    clearlink = link.get_attribute('href')
                    print("Link is Valid:", clearlink)
                    if clearlink not in linklist:
                        linklist.append(clearlink)
                    else:
                        continue
                else:
                    print("Link is Invalid/Broken:", clearlink, link.get_attribute('outerHTML'))
            except:
                print('SomethingElseGetsWrong:', link.get_attribute('href'), link.get_attribute('outerHTML'))

        return linklist