from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = (browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")).click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    (browser.find_element(By.ID, 'answer')).send_keys(y) #written answer
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    print(browser.switch_to.alert.text)
    print(new_window)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
