from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

result = []
with webdriver.Chrome() as browser:
    # browser.get('http://parsinger.ru/scroll/3/')
    browser.get('http://parsinger.ru/scroll/training_task_3/')
    tags_input = browser.find_elements(By.TAG_NAME, 'input')
    for tag in tags_input:
        tag.click()
        tag_id = tag.get_attribute('id')
        num = browser.find_element(By.ID, f'result{tag_id}')
        result.append(int(tag_id)) if num.text else None
        tag.send_keys(Keys.DOWN)

print(sum(result))


# второй вариант через next
from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# result = []
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/training_task_3/')
#     tags_input = browser.find_elements(By.TAG_NAME, 'input')
#     num = (i for i in browser.find_elements(By.TAG_NAME, 'span'))
#
#     for tag in tags_input:
#         tag.click()
#         tag_id = tag.get_attribute('id')
#         txt = next(num).text
#         if txt:
#             result.append(int(tag_id))
#         tag.send_keys(Keys.DOWN)
#
# print(sum(result))
