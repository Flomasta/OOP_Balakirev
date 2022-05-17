from datetime import datetime

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
start_time = datetime.now()
url = 'http://parsinger.ru/infiniti_scroll_1/'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(0.5)
    count = 0
    checking = []
    result = []
    while True:
        input_list = [x for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')]

        for inp in input_list:
            if inp not in checking:
                inp.send_keys(Keys.DOWN)
                count += 1
                checking.append(inp)

        span_list = [result.append(int(x.text)) for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span') if int(x.text) not in result]
        break_loop = [x for x in browser.find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
        if break_loop:
            break
    print(f'Результат: {sum(result)}')
print(datetime.now() - start_time)
