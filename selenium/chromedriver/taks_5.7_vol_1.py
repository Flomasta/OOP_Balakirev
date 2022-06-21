from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://parsinger.ru/blank/modal/2/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    buttons = browser.find_elements(By.TAG_NAME, 'input')

    for button in buttons:
        button.click()
        browser.switch_to.alert.accept()
        time.sleep(0.1)
        code = browser.find_element(By.ID, 'result').text
        if code:
            print(code)
            break
