import time
from selenium import webdriver
from selenium.webdriver.common.by import By

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

url = 'https://parsinger.ru/window_size/2/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    for x in window_size_x:
        for y in window_size_y:
            browser.set_window_size(x + 13, y + 131)
            code = browser.find_element(By.ID, 'result').text
            if code:
                print(code)
                break
            time.sleep(.3)
