from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/2/index.html')
    tags_input = browser.find_elements(By.TAG_NAME, 'input')
    counter = 1
    res = []
    for input in tags_input:
        input.click()
        num = browser.find_element(By.ID, f'result{counter}').text
        res.append(int(num)) if num else None
        input.send_keys(Keys.DOWN)
        counter += 1
print(sum(res))
