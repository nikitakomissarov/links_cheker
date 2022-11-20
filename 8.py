from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    robotrule = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotrule)
    robotrule.click()

    num1 = browser.find_element(By.ID, "input_value"); num1 = int(num1.text)
    x = num1
    print(x)
    y = calc(x)
    print(y)

    browser.find_element(By.ID, "answer").send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
finally:
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)
    browser.quit()
