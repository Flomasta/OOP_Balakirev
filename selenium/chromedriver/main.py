import time
from selenium import webdriver
from selenium.webdriver.common.by import By

d = {"first_name": "John", "last_name": "Smith", "patronymic": "Smithovich", "age": '18', "city": 'New-York',
     "email": 'john@smith.com'}
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/1/1.html')
    for k, v in d.items():
        inputElement = browser.find_element(By.NAME, k)
        inputElement.send_keys(v)
    inputElement = browser.find_element(By.ID, "btn").click()
    time.sleep(10)
