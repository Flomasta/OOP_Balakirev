from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    res = []
    input_element = browser.find_elements(By.TAG_NAME, 'p')
    for i in input_element:
        res.append(int(i.text))
    print(sum(res))
