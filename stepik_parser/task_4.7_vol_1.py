import json
import requests
from bs4 import BeautifulSoup

domain = 'http://stepik-parsing.ru/html/'
default_url = 'http://stepik-parsing.ru/html/index1_page_1.html'
encoding = 'utf-8-sig'


def cooking_soup(url=default_url):
    response = requests.get(url=url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_pages():
    soup = cooking_soup()
    pages = [i['href'] for i in soup.find('div', class_='pagen').find_all('a')]
    return pages


def get_description():
    pages = get_pages()
    result = []
    for i in pages:
        url = f'{domain}{i}'
        soup = cooking_soup(url)
        names = [name.text for name in soup.find_all('a', class_='name_item')]
        description = [[i.text.split('\n') for i in prop.find_all('li')] for prop in
                       soup.find_all('div', class_='description')]

        price = [price.text for price in soup.find_all('p', class_='price')]
        # я тут слегка перемудрил:)
        
        for names, description, price in zip(names, description, price):
            res = {**{'name': names}, **dict([i.split(':') for prop in description for i in prop]), **{'price': price}}
            result.append(
                {**{'name': names}, **dict([i.split(':') for prop in description for i in prop]), **{'price': price}})
    return result


def create_json_file(result):
    with open('res.json', 'w', encoding=encoding) as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def get_info():
    result = get_description()
    create_json_file(result)
    print('Успешно создано')


get_info()
