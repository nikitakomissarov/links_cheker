from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

print("dfsdpdfsdfs \n dfsds")
link = "http://ouds.alm.su/"
browser = webdriver.Chrome()
browser.get(link)
html = browser.page_source
time.sleep(1)
print(html)

header_burger = browser.find_element(By.CLASS_NAME, 'header__burger').click()

time.sleep(5)
browser.maximize_window()

expression = " Объекты "

objects = browser.find_element(By.CSS_SELECTOR, "a[href='/objects/']").click()
ActionChains(browser).move_to_element(objects).key_down(Keys.COMMAND).click(objects).key_up(Keys.COMMAND).perform()
company = browser.find_element(By.CSS_SELECTOR, "a[href='/company/']").click()
services = browser.find_element(By.CSS_SELECTOR, "a[href='/services/']").click()
news = browser.find_element(By.CSS_SELECTOR, "a[href='/news/']").click()
browser.quit()
