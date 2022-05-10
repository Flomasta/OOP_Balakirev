import json
import requests
from bs4 import BeautifulSoup

domain = 'http://stepik-parsing.ru/html/'
default_url = 'http://stepik-parsing.ru/html/index1_page_1.html'
encoding = 'utf-8'


def cooking_soup(url=default_url):
    response = requests.get(url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_menu_urls():
    soup = cooking_soup()
    menu_urls = [menu_url['href'] for menu_url in soup.find('div', class_='nav_menu').find_all('a')]
    return menu_urls


def get_category_pages(category_url):
    soup = cooking_soup(category_url)
    pages_urls = [page_url['href'] for page_url in soup.find('div', class_='pagen').find_all('a')]
    return pages_urls


def get_all_items():
    all_items = []
    menu_urls = get_menu_urls()
    for menu_url in menu_urls:
        url = f'{domain}{menu_url}'
        pages = get_category_pages(url)
        for page in pages:
            url = f'{domain}{page}'
            soup = cooking_soup(url)
            name = [name.text for name in soup.find_all('a', class_='name_item')]
            description = [item_description.text.split('\n') for item_description in
                           soup.find_all('div', class_='description')]
            price = [price.text for price in soup.find_all('p', class_='price')]
            for name, description, price in zip(name, description, price):
                all_items.append({'name': name} | dict([i.split(':') for i in description if i]) | {'price': price})

    return all_items


def create_json_file(result):
    with open('result.json', 'w', encoding=encoding) as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def get_info():
    result = get_all_items()
    create_json_file(result)
    print('Файл успешно создан!')

get_info()
