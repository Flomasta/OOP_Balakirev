from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_num():
    browser.refresh()
    code = browser.find_element(By.ID, 'result')
    if not code.text.isnumeric():
        return get_num()
    return code


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    print(get_num().text)
