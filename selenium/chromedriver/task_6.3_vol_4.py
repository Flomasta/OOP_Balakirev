from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    input_element = browser.find_elements(By.TAG_NAME, 'p')
    gen = (input_element[i] for i in range(1,len(input_element)+1,3))
    res = [int(i.text) for i in gen]
    print(sum(res))
