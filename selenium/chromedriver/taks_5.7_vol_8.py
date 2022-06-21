import time
from math import sqrt
from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html', ]
res = 0
with webdriver.Chrome() as browser:
    for site in sites:
        browser.get(site)
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        res += sqrt(int(browser.find_element(By.ID, 'result').text))

print('%.9f' % res)
