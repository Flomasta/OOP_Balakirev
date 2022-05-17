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
soup = cooking_soup()
print(type(soup))
name = soup.find('a',class_="name_item")
print(type(name))
