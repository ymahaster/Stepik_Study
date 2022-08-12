from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "https://hh.ru/account/login?backurl=%2F"
    browser = webdriver.Chrome()
    browser.get(link)

    more = browser.find_element(By.CSS_SELECTOR, '[data-qa="expand-login-by-password"]')
    more.click()
    email = browser.find_element(By.CSS_SELECTOR, '[inputmode="email"]')
    email.send_keys('ymahaster@gmail.com')
    password = browser.find_element(By.CSS_SELECTOR, '[data-qa="login-input-password"]')
    password.send_keys('Canon555')
    enter = browser.find_element(By.CSS_SELECTOR, '[data-qa="account-login-submit"]')
    enter.click()
    time.sleep(5)

    vacancy = browser.find_element(By.CSS_SELECTOR, '#a11y-search-input')
   # vacancy.click()  senior, team lead, headhunter
    vacancy.send_keys('Qa')
    search = browser.find_element(By.CSS_SELECTOR, '.bloko-button_stretched')
    search.click()

    filter = browser.find_element(By.CSS_SELECTOR, '[data-qa="novafilters-excluded-text-input"]')
    filter.send_keys('senior, team lead, headhunter, game \n')


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()