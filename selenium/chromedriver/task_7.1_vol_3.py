from selenium import webdriver

result = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    # for cookie in cookies:
    #     name = int(cookie['name'].split('_')[-1]) % 2 == 0
    #     if name % 2 == 0:
    #         result += int(cookie['value'])
    # print(result)

print(sum(int(cookie['value']) for cookie in cookies if int(cookie['name'].split('_')[-1]) % 2 == 0))
