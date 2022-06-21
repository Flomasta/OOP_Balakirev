from selenium import webdriver
from pprint import pprint

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    print(sum([int(cookie['value']) for cookie in cookies]))
