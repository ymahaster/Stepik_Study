from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    with open("test.txt", "w") as file:
        content = file.write("Piska")

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("Ivan@gmail.com")

    file = browser.find_element(By.ID, 'file')
    current_dir =os.path.abspath(os.path.dirname(__file__))
    file_path =os.path.join(current_dir, "test.txt")
    file.send_keys(file_path)

    sumbit = (browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')).click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()