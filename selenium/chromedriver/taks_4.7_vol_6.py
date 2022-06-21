from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/table/5/index.html')
    headers = [i.text for i in browser.find_elements(By.TAG_NAME, 'th')]
    rows = len(browser.find_elements(By.TAG_NAME, 'tr'))
    cols = len(browser.find_element(By.TAG_NAME, 'tr').find_elements(By.TAG_NAME, 'th'))
    amnt = []

    for col in range(1, cols + 1):
        line = sum([float(browser.find_element(By.XPATH, f'//tr[{row}]/td[{col}]').text) for row in range(2, rows + 1)])
        amnt.append(round(line, 3))
    print(dict(zip(headers, amnt)))
