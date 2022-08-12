from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int((browser.find_element(By.ID, 'input_value')).text)
    y = calc(x)
    scroll = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", scroll)
    scroll.send_keys(y)
    check_button = (browser.find_element(By.ID, 'robotCheckbox')).click()
    radio_button = browser.find_element(By.ID, 'robotsRule').click()
    sumbit = (browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')).click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
