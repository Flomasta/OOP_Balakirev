import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent

default_url = 'https://www.dns-shop.ru/catalog/17a8ad6e16404e77/vneshnie-zhestkie-diski/'
domain = 'https://www.dns-shop.ru/'
encoding = 'utf-8-sig'
ua = UserAgent()
HEADERS = {'user-agent': ua.random}

table_headers = (
    'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
    'Материал браслета',
    'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром')


def create_table_headers(header=table_headers):
    with open('res.csv', 'w', encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)


def cooking_soup(url=default_url, encoding=encoding):
    url = url
    response = requests.get(url=url, headers=HEADERS)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_content():
    soup = cooking_soup()
    urls = [domain + i['href'] for i in soup.find_all('a', class_='catalog-product__name')]
    return urls


print(get_content())
