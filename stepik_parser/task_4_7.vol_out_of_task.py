import json
import requests
from bs4 import BeautifulSoup

domain = 'http://stepik-parsing.ru/html/'
default_url = 'http://stepik-parsing.ru/html/index4_page_1.html'
encoding = 'utf-8'


def cooking_soup(url=default_url):
    response = requests.get(url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_pages():
    soup = cooking_soup()
    pages = [page['href'] for page in soup.find('div', class_='pagen').find_all('a')]
    return pages


def get_item_cards():
    pages = get_pages()
    items_cards = []
    for page in pages:
        url = f'{domain}{page}'
        soup = cooking_soup(url)
        items_cards.append([items['href'] for items in soup.find_all('a', class_='name_item')])
    return items_cards


def get_item_info():
    items_lst = get_item_cards()
    result = []
    for items in items_lst:
        for item in items:
            url = f'{domain}{item}'
            soup = cooking_soup(url)
            description = [i for i in soup.find('div', class_='description').text.split('\n') if i]
            result.append(
                {'Наименование': description[0]} | dict([line.split(':', 1) for line in description if ':' in line]) | {
                    'Цена': description[-3],
                    'Старая цена':
                        description[-2]})

    return result


def create_json_file(result):
    with open('result.json', 'w', encoding=encoding) as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def get_info():
    results = get_item_info()
    create_json_file(results)
    print('Данные успешно добавлены')


get_info()
