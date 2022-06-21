from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://parsinger.ru/scroll/4/index.html'
res = 0
with webdriver.Chrome() as browser:
    browser.get(url)
    for btn in browser.find_elements(By.CLASS_NAME, 'btn'):
        if btn.size['height'] > 0 and btn.size['width'] > 0:
            browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
            btn.click()
            num = browser.find_element(By.ID, 'result')
            res += int(num.text)
            time.sleep(0.5)
print(res)
