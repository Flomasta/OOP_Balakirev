from datetime import datetime

from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

start_time = datetime.now()
url = 'http://parsinger.ru/infiniti_scroll_2/'
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.maximize_window()
    container = browser.find_element(By.ID, 'scroll-container')
    while True:
        ActionChains(browser).click().scroll(570, 400, 570, 1000).perform()
        tag = container.find_elements(By.TAG_NAME, 'p')[-1]
        tag_class = tag.get_attribute('class')
        if tag_class == 'last-of-list':
            res = [int(i.text) for i in container.find_elements(By.TAG_NAME, 'p') if i.text]
            break
        time.sleep(0.3)
print(sum(res))
print(datetime.now() - start_time)
