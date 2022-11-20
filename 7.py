from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1"); num1 = int(num1.text)
    num2 = browser.find_element(By.ID, "num2"); num2 = int(num2.text)
    x = num1 + num2

    browser.find_element(By.TAG_NAME, "select").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()