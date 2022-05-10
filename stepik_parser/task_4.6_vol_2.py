import csv
import requests
from bs4 import BeautifulSoup

with open('res.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', 'Тип', 'Материал корпуса', 'Технология экрана', 'Цена'])

url = 'http://stepik-parsing.ru/html/index4_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
domain = 'http://stepik-parsing.ru/html/'
menu = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]

for item in menu:
    url = f'{domain}{item}'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    pages = [page.text for page in soup.find('div', class_='pagen').find_all('a')][-1]
    columns = [col.split(':') for col in soup.find('div', class_='description').text.split('\n') if col]
    table_headers = []
    for column in columns:
        table_headers.append(column[0])

    print(table_headers)
    if item.split('_')[0] != 'index1':
        with open('res.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Наименование'] + table_headers + ['Цена'])

    for i in range(1, int(pages) + 1):
        url = f'{domain}{item.replace("page_1", "page_" + str(i))}'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = soup.find_all('a', class_='name_item')
        descriptions = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        price = [prc.text for prc in soup.find_all('p', class_='price')]

        for name, descriptions, price in zip(name, descriptions, price):
            result = []
            flatten = name.text, [x.split(':')[1].strip() for x in descriptions if x], price

            for j in flatten:
                if isinstance(j, list):
                    for k in j:
                        result.append(k)
                else:
                    result.append(j)
            with open('res.csv', 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(result)

print('Файл res.csv создан')
