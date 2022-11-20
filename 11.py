from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()

    humber = browser.find_element(By.ID, "input_value"); humber = int(humber.text)
    print(humber)

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
