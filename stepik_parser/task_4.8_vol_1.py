from bs4 import BeautifulSoup
import json
import requests

url = 'http://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url).json()
dict = {'watch': 0, 'mobile': 0, 'mouse': 0, 'hdd': 0, 'headphones': 0}

for item in response:
    category = item['categories']
    if category in dict:
        dict[category] += int(item['count'])
print(dict)
