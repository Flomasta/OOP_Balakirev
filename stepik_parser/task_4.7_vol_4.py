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


def get_menu_info():
    soup = cooking_soup()
    menu_urls = [menu_url['href'] for menu_url in soup.find('div', class_='nav_menu').find_all('a')]
    categories = [category['id'] for category in soup.find('div', class_='nav_menu').find_all('div')]
    return zip(menu_urls, categories)


def get_category_pages(category_url):
    soup = cooking_soup(category_url)
    pages_urls = [page_url['href'] for page_url in soup.find('div', class_='pagen').find_all('a')]
    return pages_urls


def get_items_url(page):
    soup = cooking_soup(page)
    item_urls_per_page = [link['href'] for link in soup.find_all('a', class_='name_item')]
    return item_urls_per_page


def get_item(url, **kwargs):
    soup = cooking_soup(url)
    name = {'name': soup.find('p', id='p_header').text}
    article = {'article': soup.find('p', class_='article').text.split(':', 1)[1]}
    description = {'description': {line['id']: line.text.split(':', 1)[1] for line in
                                   soup.find('ul', id='description').find_all('li')}}
    in_stock = {'count': soup.find('span', {'id': 'in_stock'}).text.split(':')[1]}
    sale = {item['id']: item.text for item in soup.find(class_='sale').find_all('span')}
    link = {'link': url}
    item_description = kwargs | name | article | description | in_stock | sale | link
    return item_description


def get_all_items():
    result = []
    categories_info = get_menu_info()
    for category in categories_info:
        category_url = f'{domain}{category[0]}'
        category_title = category[1]
        pages = get_category_pages(category_url)
        for page in pages:
            url = f'{domain}{page}'
            items_urls = get_items_url(url)
            for item_url in items_urls:
                url = f'{domain}{item_url}'
                item_description = get_item(url, categories=category_title)
                result.append(item_description)
    return result

def create_json_file(result):
    with open('res.json', 'w', encoding=encoding) as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

def get_info():
    result = get_all_items()
    create_json_file(result)
    print('Файл успешно создан!')

get_info()
