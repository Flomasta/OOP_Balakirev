from selenium import webdriver
from selenium.webdriver.common.by import By

res = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/table/1/index.html')
    all_nums = browser.find_elements(By.TAG_NAME,'td')
    print(sum({float(i.text) for i in all_nums}))
