import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

start = datetime.now()
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_1/')
    browser.maximize_window()
    while True:
        flag = False
        res = 0
        tag_input = browser.find_element(By.TAG_NAME, 'input')
        tags_span = browser.find_elements(By.TAG_NAME, 'span')
        tag_input.send_keys(Keys.END)
        time.sleep(0.1)

        for tag_span in tags_span:
            if tag_span.text:
                res += int(tag_span.text)
            tag_span_class = tag_span.get_attribute('class')
            if 'last-of-list' in tag_span_class:
                flag = True
        if flag: break
print(res)
print(datetime.now() - start)
