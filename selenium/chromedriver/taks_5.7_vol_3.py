import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/blank/modal/4/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    pins = browser.find_elements(By.CLASS_NAME, 'pin')
    button_to_check = browser.find_element(By.ID, 'check')
    result = browser.find_element(By.ID, 'result')
    for pin in pins:
        pt = pin.text
        button_to_check.click()
        time.sleep(.3)
        alert = browser.switch_to.alert
        alert.send_keys(pt)
        alert.accept()
        time.sleep(.3)
        if result.text.isdigit():
            print(result.text)
            break
