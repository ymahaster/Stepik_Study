from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = (browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")).click()
    browser.switch_to.alert.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    (browser.find_element(By.ID, 'answer')).send_keys(y) #written answer
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    print(browser.switch_to.alert.text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()