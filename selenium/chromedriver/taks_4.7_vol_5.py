from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/table/5/index.html')
    print(
        sum(
            [float(item.find_element(By.CLASS_NAME, 'orange').text) *
             float(item.find_element(By.CSS_SELECTOR, 'td:last-child').text)
             for item in browser.find_elements(By.TAG_NAME, 'tr')[1::]]))
