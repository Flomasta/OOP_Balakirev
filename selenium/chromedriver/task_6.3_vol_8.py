import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/6/6.html')
    res = eval([i.text for i in browser.find_elements(By.ID, 'text_box')][0].replace(')', '', 1))
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    input_options = [select.select_by_visible_text(i.text) if res == int(i.text) else None for i in
                     browser.find_elements(By.TAG_NAME, 'option')]
    browser.find_element(By.ID,'sendbutton').click()

    time.sleep(10)
