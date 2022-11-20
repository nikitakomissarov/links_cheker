from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])


    humber = browser.find_element(By.ID, "input_value"); humber = int(humber.text)
    o = 0
    for i in (browser.window_handles):
        o += 1
        print(o)

    x = calc(humber)
    print(x)

    answer = browser.find_element(By.ID, "answer").send_keys(x)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()
finally:
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)
    browser.quit()
