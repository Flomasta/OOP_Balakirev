from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/2/2.html')
    inputElement = browser.find_element(By.LINK_TEXT, '16243162441624')
    inputElement.click()
    inputElement = browser.find_element(By.ID,'result').text
    print(inputElement)
