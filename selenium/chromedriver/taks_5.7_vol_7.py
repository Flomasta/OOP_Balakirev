from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/blank/3/index.html'
res = 0
with webdriver.Chrome() as browser:
    browser.get(url)
    links = browser.find_elements(By.CLASS_NAME, 'buttons')
    [link.click() for link in links]
    pages = browser.window_handles
    for page in pages[1::]:
        browser.switch_to.window(page)
        res += int(browser.execute_script("return document.title;"))
print(res)
