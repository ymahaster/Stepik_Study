from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '[valuex]')
    x = x_element.get_attribute('valuex')
    print(x)
    y = calc(x)
    input_result = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_result.send_keys(y)
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()