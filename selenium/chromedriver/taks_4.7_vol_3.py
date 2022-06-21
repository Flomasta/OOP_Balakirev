from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/table/3/index.html')
    print(sum([float(item.text) for item in browser.find_elements(By.TAG_NAME, 'b')]))
