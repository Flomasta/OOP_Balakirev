# Привет! Продолжаю извращаться над заданием как могу:).
# Интересно было попробовать написать что то унифицированное,
# чтобы работало не только на одном сайте, ну или на одном, но при некоторых отличных условиях
# не уверен, что получилось хорошо, так как при подробном рассмотрении повылезает куча косяков, но я пытался))

import json
import requests
from bs4 import BeautifulSoup, Tag

domain = 'http://stepik-parsing.ru/html/'
default_url = 'http://stepik-parsing.ru/html/index4_page_1.html'
encoding = 'utf-8'
attr_to_replace = {'p_header': 'name', 'in_stock': 'count'}


def cooking_soup(url=default_url):
    response = requests.get(url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_pages():
    soup = cooking_soup()
    pages = [page['href'] for page in soup.find('div', class_='pagen').find_all('a')]
    return pages


def get_category(url=default_url):
    soup = cooking_soup()
    category = soup.find('div', class_='nav_menu').find_all('a')
    for i in category:
        if i['href'] == url.split('/')[-1]:
            return i.find('div')['id']


def get_item_cards():
    pages = get_pages()
    items_cards = []
    for page in pages:
        url = f'{domain}{page}'
        soup = cooking_soup(url)
        items_cards.append([items['href'] for items in soup.find_all('a', class_='name_item')])
    return items_cards


def check_attr(attr):
    var = list(attr.attrs.items())[0][1]
    return var[0] if attr.has_attr('class') else var


def get_inner_items(attr):
    inner_attr = check_attr(attr)
    # функцией check_attr проверяю имеем перед собой class или id, class возвращает
    # список, а не строку, список не может быть ключом словаря,поэтому беру первое попавшееся
    # значение атрибута.

    enclosure = {
        inner_attr: {list(j.attrs.values())[0]: j.text.split(':', 1)[1] if ':' in j.text else j.text
                     for j in
                     attr.find_all()}}
    # создаём словарь "значение_атрибута":"описание", конструкция list здесь используется т.к values возвращает
    # объект-представление, к нему по индексу не достучаться:)
    return enclosure


def get_items_attr():
    items = get_item_cards()
    result = []
    for page in items:
        for item in page:
            url = f'{domain}{item}'
            soup = cooking_soup(url)
            description = soup.find('div', class_='description')
            category = get_category()
            diction = {'category': category}
            for line in description:
                if isinstance(line, Tag):
                    # пришлось прописать небольшой костылик с br, так как в некоторых названиях встречается пара
                    # таких вложенных тегов
                    print(line)
                    if line.find_all() and not line.find('br'):

                        inner_attr = check_attr(line)
                        # функцией check_attr проверяю имеем перед собой class или id, class возвращает
                        # список, а не строку, список не может быть ключом словаря,поэтому беру первое попавшееся
                        # значение атрибута.

                        enclosure = {
                            inner_attr: {list(j.attrs.values())[0]: j.text.split(':', 1)[1] if ':' in j.text else j.text
                                         for j in
                                         line.find_all()}}
                        # создаём словарь "значение_атрибута":"описание", конструкция list здесь используется т.к values возвращает
                        # объект-представление, к нему по индексу не достучаться:)

                        diction.update(enclosure)
                    else:
                        single_attr = check_attr(line)
                        if single_attr in attr_to_replace:
                            single_attr = attr_to_replace[single_attr]
                        diction.update({single_attr: line.text.split(':', 1)[1] if ':' in line.text else line.text})

            diction['sale'].pop('sale_button', None)
            diction.update({'link': url})
            # Не нашёл лучше способа избавиться от кнопки "Купить"

            result.append(diction)
    return result


def create_json_file(result):
    with open('result.json', 'w', encoding=encoding) as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def get_info():
    results = get_items_attr()
    create_json_file(results)
    print('Данные успешно добавлены')


get_info()
