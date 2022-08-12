from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
try:
    with open('words.txt', 'r') as file:
        words = file.readlines()
        words = [s.strip("\n") for s in words]
    def random_word(words):
        return random.choice(words)

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys(random_word(words))

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
# Print code for exercise in line status
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
