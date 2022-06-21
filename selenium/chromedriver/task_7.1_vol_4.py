from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/methods/5/index.html'
d = {}
with webdriver.Chrome() as browser:
    browser.get(url)
    links = browser.find_elements(By.TAG_NAME, 'a')
    for link in links:
        with webdriver.Chrome() as browser:
            browser.get(link.get_attribute("href"))
            id_result = browser.find_element(By.ID, 'result').text
            exp_cookie = browser.get_cookie('expiry')['expiry']
            d.update({exp_cookie:id_result})
print(d[max(d)])
