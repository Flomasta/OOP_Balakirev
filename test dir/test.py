import requests
from bs4 import BeautifulSoup
import json

name, description, price = [], [], []
for i in range(1, 5):
    url = f'https://stepik-parsing.ru/html/index1_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    name_i = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    name.extend(name_i)
    description_i = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    description.extend(description_i)
    price_i = [x.text for x in soup.find_all('p', class_='price')]
    price.extend(price_i)

watch_json = []
for list_item, price_item, name in zip(description, price, name):
    watch_json.append({
        'Наименование': name,
        'Бренд': [x.split(':')[1] for x in list_item][0],
        'Тип': [x.split(':')[1] for x in list_item][1],
        'Материал корпуса': [x.split(':')[1] for x in list_item][2],
        'Технология экрана': [x.split(':')[1] for x in list_item][3],
        'Цена': price_item

    })

with open('watch.json', 'w', encoding='utf-8') as file:
    json.dump(watch_json, file, indent=4, ensure_ascii=False)
