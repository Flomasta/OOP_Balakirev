import csv
import requests
from bs4 import BeautifulSoup

url = 'http://stepik-parsing.ru/html/index1_page_1.html#1_1'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
domain = 'http://stepik-parsing.ru/html/'
pagination = [num.text for num in soup.find('div', class_='pagen').find_all()][-1]

with open('res.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
        'Материал браслета',
        'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'])

for page in range(1, int(pagination) + 1):
    url = f'http://stepik-parsing.ru/html/index1_page_{page}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    item = [link['href'] for link in soup.find_all('a', class_='name_item')]
    for item_card in item:
        url = f'{domain}{item_card}'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text.split(':')[1].strip()
        descriptions = [item.text.split('\n') for item in soup.find('ul', id='description').find_all()]
        in_stock = soup.find('span', {'id': 'in_stock'}).text.split(':')[1]
        price = soup.find('span', {'id': 'price'}).text
        old_price = soup.find('span', {'id': 'old_price'}).text
        item_url = url
        result = [name, article]

        for i in descriptions:
            for j in i:
                result.append(j.split(':')[1])
        result += [in_stock, price, old_price, item_url]

        with open('res.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(result)

print('Файл res.csv создан')
