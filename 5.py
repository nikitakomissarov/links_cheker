from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    y = calc(x)

    x_element = browser.find_element(By.ID, "answer")
    x_element.send_keys(y)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    button.click()

    button1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    button1.click()

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()