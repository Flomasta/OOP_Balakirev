import time

from selenium import webdriver
from selenium.webdriver.common.by import By

w = h = 555
url = 'https://parsinger.ru/window_size/1/'
with webdriver.Chrome() as browser:
    browser.set_window_size(w + 13, h + 131)
    browser.get(url)
    print(browser.find_element(By.ID, 'result').text)
