from datetime import datetime

from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

start_time = datetime.now()
url = 'http://parsinger.ru/infiniti_scroll_3/'

with webdriver.Chrome() as browser:
    browser.get(url)

    browser.set_window_size(1700, 1000)
    action = ActionChains(browser)
    tag_id = browser.find_element(By.ID, 'scroll-container_5')

    while True:

        action.scroll(450, 275, 615, 275).perform()
        action.scroll(615, 275, 700, 275).perform()
        action.scroll(800, 275, 900, 275).perform()
        action.scroll(1000, 275, 1100, 275).perform()
        action.scroll(1200, 275, 1300, 275).perform()
        break_point = [i.get_attribute('class') for i in tag_id.find_elements(By.TAG_NAME, 'span')[-1:-4:-1] if
                       i.get_attribute('class') == 'last-of-list']
        if break_point:
            res = [int(i.text) for i in browser.find_element(By.CLASS_NAME, 'main').find_elements(By.TAG_NAME, 'span')]
            break

print(sum(res))
print(datetime.now() - start_time)
