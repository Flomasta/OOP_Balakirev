# пробую усовершенстовать код уже решенной задачи
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

start = datetime.now()
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_1/')
    browser.maximize_window()
    while True:
        flag = False
        for i in range(9):
            tag_input = browser.find_element(By.TAG_NAME, 'input')
            tag_input.send_keys(Keys.END)
            time.sleep(0.3)
        tags_span = browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')

        for tag_span in tags_span[::-1]:
            tag_span_class = tag_span.get_attribute('class')
            if 'last-of-list' in tag_span_class:
                flag = True
                break

        if flag:
            result = [int(i.text) for i in tags_span if i.text]
            break

print(sum(result))
print(datetime.now() - start)
