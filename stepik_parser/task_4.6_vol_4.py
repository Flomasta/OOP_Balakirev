#Привет! Заранее благодарю за ревью кода и отдельно за советы и замечания =)

import csv
import requests
from bs4 import BeautifulSoup

domain = 'http://stepik-parsing.ru/html/'
default_url = 'http://stepik-parsing.ru/html/index1_page_1.html'
headers = (
    'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
    'Материал браслета',
    'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром')

# если указать просто utf-8, то excel не кодирует нормально, показывая иероглифы
encoding = 'utf-8-sig'


def create_table_headers(header=headers):
    with open('res.csv', 'w', encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)


def cooking_soup(url=default_url, encoding=encoding):
    url = url
    response = requests.get(url=url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_menu_items():
    soup = cooking_soup()
    menu = [item['href'] for item in soup.find('div', class_='nav_menu').find_all('a')]
    return menu


def get_pages_amount(url=default_url):
    soup = cooking_soup(url)
    pages = [num.text for num in soup.find('div', class_='pagen').find_all()][-1]
    pages_indexes = [idx['href'] for idx in soup.find('div', class_='pagen').find_all('a')]
    return pages, pages_indexes


# данную функцию можно было бы сделать проще, попытался сделать её универсальной,
# не зависящей от количества элементов меню и страниц (пагинации)
def get_items_url():
    menu = get_menu_items()
    items_url_list = []
    for item_menu in menu:
        url = f'{domain}{item_menu}'
        pages = get_pages_amount(url)[0]
        for page in range(1, int(pages) + 1):
            page_index = get_pages_amount(url)[1][int(page) - 1]
            url = f'{domain}' + page_index
            soup = cooking_soup(url)
            item_urls = [domain + item['href'] for item in soup.find_all('a', class_='name_item')]
            items_url_list.append(item_urls)
    return items_url_list


def get_items_description():
    urls = get_items_url()
    result = []
    for category in urls:
        for item_card_url in category:
            soup = cooking_soup(item_card_url)
            descriptions = [info.text.split('\n') for info in soup.find_all('div', class_='description')][0]
            # пытаюсь подогнать столбцы, т.к не полное соответствие, возможно на данном этапе этого не требуется
            for k, v in enumerate(descriptions):
                if any([x in v for x in ['Диагональ экрана', 'Вес', 'Энергопотребление']]):
                    del descriptions[k]
                if 'Особенность' in v:
                    descriptions[k] = 'Не указан'
            descriptions = [prop.strip().split(":", 1) for prop in descriptions if prop][:-1]
            data = list(map(lambda prop: prop[1].strip() if len(prop) == 2 else prop[0].strip(), descriptions)) + [
                item_card_url]
            result.append(data)
    return result


def add_to_csv_file(data, encoding=encoding):
    for line in data:
        with open('res.csv', 'a', encoding=encoding, newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(line)


def get_info():
    create_table_headers()
    data = get_items_description()
    add_to_csv_file(data)
    print('Успешно добавлено!')


get_info()
