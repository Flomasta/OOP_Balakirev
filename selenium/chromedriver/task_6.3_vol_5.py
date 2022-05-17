import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/4/4.html')

    for i in range(1,521):
        input_element = browser.find_element(By.XPATH,f'//input[{i}]')
        input_element.click()
    browser.find_element(By.XPATH,f'//input[@class = "btn"]').click()
    time.sleep(10)
