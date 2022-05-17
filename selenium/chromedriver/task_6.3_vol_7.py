import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    options = browser.find_elements(By.TAG_NAME, 'option')
    res = sum([int(i.text) for i in options])
    inpt_res = browser.find_element(By.ID, 'input_result').send_keys(res)
    browser.find_element(By.ID, 'sendbutton').click()
    time.sleep(10)
