from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    texts = '$100'


    timer = WebDriverWait(browser, 12).until(
         EC.text_to_be_present_in_element((By.ID, "price"), texts)
     )
    print(timer)

    message = browser.find_element(By.ID, "book").click()


    num1 = browser.find_element(By.ID, "input_value")
    num1 = int(num1.text)
    x = num1
    print(x)
    y = calc(x)
    print(y)

    browser.find_element(By.ID, "answer").send_keys(y)


    button2 = browser.find_element(By.ID, "solve").click()
    assert 'Stepik1' in browser.switch_to.alert.text






finally:
    browser.quit()

