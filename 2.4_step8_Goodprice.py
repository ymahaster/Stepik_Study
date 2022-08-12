from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
import time
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # wait_good_price
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element(By.ID, 'book').click()

    # scroll
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, 'input_value'))

    # calc_and_return
    x = int((browser.find_element(By.ID, 'input_value')).text)
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()

    # print alert result
    # print(browser.switch_to.alert.text)

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
