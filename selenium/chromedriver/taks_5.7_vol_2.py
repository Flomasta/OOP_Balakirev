from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
url = 'https://parsinger.ru/blank/modal/3/index.html'

with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    buttons = browser.find_element(By.CLASS_NAME, 'main').find_elements(By.TAG_NAME, 'input')
    window_to_check = browser.find_element(By.ID, 'input')
    button_to_click = browser.find_element(By.ID, 'check')
    result = browser.find_element(By.ID, 'result')
    for button in buttons:
        button.click()
        alert = browser.switch_to.alert
        pin_code = alert.text
        alert.accept()
        window_to_check.send_keys(pin_code)
        button_to_click.click()
        if result.text.isdigit():
            print(result.text)
            break
