# Привет! Вкратце: очень сильно переусложнил:)
# Сдедал немного не по заданию, но результат можно получить как по заданию, так и немного пошире.
# Продолжаю писать что то унифицированное,
# чтобы работало не только на одном сайте, ну или на одном, но при некоторых отличных условиях
# не уверен, что получилось хорошо, так как при подробном рассмотрении повылезает куча косяков, но я пытался))
# В итоге, я сам себе додумал, написать рабочий код, на случай если будет несколько вложенных списков,
# чтобы при этом и условия задания выполнялись. Такой вариант виден в ul description и div sale.
# Ниже в коде я прокомментирую это.

import json
import requests
from bs4 import BeautifulSoup, Tag

domain = 'http://stepik-parsing.ru/html/'
default_url = 'http://stepik-parsing.ru/html/index4_page_1.html'
encoding = 'utf-8'
attr_to_replace = {'p_header': 'name', 'in_stock': 'count'}
attr_to_remove_list = ['sale_button']
attr_to_remove_dict = {'sale': 'sale_button'}


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
    ''' Проверяет  имеем перед собой class или id. Сlass возвращает
        список, а не строку, список не может быть ключом словаря.Если указан class функция возвращет первое попавшееся
        значение атрибута.'''
    var = list(attr.attrs.items())[0][1]
    return var[0] if attr.has_attr('class') else var


def get_inner_items(attr):
    ''' данная функция возвращает словарь из дочерних элементов, если они есть.'''
    inner_attr = check_attr(attr)
    if inner_attr in attr_to_replace:
        inner_attr = attr_to_replace[inner_attr]
    # enclosure = {
    #     inner_attr: {list(j.attrs.values())[0]: j.text.split(':', 1)[1] if ':' in j.text else j.text
    #                  for j in
    #                  attr.find_all()}}
    enclosure = {inner_attr: {}}
    for i in attr.find_all():
        txt = i.text.split(':', 1)[1] if ':' in i.text else i.text
        i_inner = list(i.attrs.values())[0]
        if i_inner in attr_to_replace:
            i_inner = attr_to_replace[i_inner]
        enclosure[inner_attr].update({i_inner: txt})

    # создаём словарь "значение_атрибута":"описание", конструкция list здесь используется т.к values возвращает
    # объект-представление, к нему по индексу не достучаться:)
    return enclosure


def get_items_attr(deep=1, counter=0):
    '''значение deep указывает на количество необходимых нам вложенных атрибутов в файле json, если deep = 0, то получим плоский
        список, если 1, то вернёт первый попавшийся список с дочерними элементами в виде ключ - родительский элемент и значение в виде словаря, состоящего из дочерних
        элементов, остальные значения по коду будут без вложений(т.е это условие задания), если указать 2, то вернёт json, в котором будет 2 списка с вложениями.
        Если будет интересно, попробуйте, запустить мой код и поменять в нём значение deep'''

    items = get_item_cards()
    result = []
    for page in items:
        for item in page:
            url = f'{domain}{item}'
            soup = cooking_soup(url)
            description = soup.find('div', class_='description')
            category = get_category()
            dictionary = {'category': category}
            for line in description:
                if isinstance(line, Tag):
                    # пришлось прописать небольшой костылик с br, так как в некоторых названиях встречается пара
                    # таких вложенных тегов
                    if line.find_all() and not line.find('br'):
                        if counter < deep:
                            counter += 1
                            enclosure = get_inner_items(line)
                            print(enclosure)
                            dictionary.update(enclosure)
                            # в зависимости от необходимости вывода, удаляю ненужные элементы, в данном случае кнопку
                            # Купить. Для плоского списка использую список значений, для вложенного - словарь. Сделал так
                            # чтобы редактировать всё это дело в одном месте и не бегать по коду в случае необходимости

                        elif counter >= deep:
                            for i in line.find_all():
                                dictionary.update({i['id']: i.text})


                    else:
                        single_attr = check_attr(line)
                        if single_attr in attr_to_replace:
                            single_attr = attr_to_replace[single_attr]
                        dictionary.update({single_attr: line.text.split(':', 1)[1] if ':' in line.text else line.text})

                    for k, v in attr_to_remove_dict.items():
                        if dictionary.get(k):
                            dictionary[k].pop(v, None)
                    for item_to_remove in attr_to_remove_list:
                        if dictionary.get(item_to_remove):
                            dictionary.pop(item_to_remove, None)

            dictionary.update({'link': url})

            result.append(dictionary)
    return result


def create_json_file(result):
    with open('result.json', 'w', encoding=encoding) as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def get_info():
    results = get_items_attr()
    create_json_file(results)
    print('Данные успешно добавлены')


get_info()
