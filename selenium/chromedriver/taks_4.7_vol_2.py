from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/table/2/index.html')
    print(
        sum([float(row.find_element(By.TAG_NAME, 'td').text) for row in browser.find_elements(By.TAG_NAME, 'tr')[1::]]))
