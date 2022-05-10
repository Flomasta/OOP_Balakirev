# ипортируем модули, csv - для формирования таблицы, requests - для отправки и получения запросов с web-сайта, bs4 для того, чтобы использовать парсер

import csv
import requests
from bs4 import BeautifulSoup

# создаём новый файл и таблицу

with open('res.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена'])

# формируем запрос к файлу и 'готовим суп'
# 1) url - страница, которая будет парситься
# 2) ответ, который получим от сайта при запросе url
# 3) Распарсенные данные парсером lxml в виде строки(.text)
# 4) При помощи soup.find находим нужный нам блок, вернёт контейнер с вложениями <div><a>...</a><a>...</a><a>...</a></div>
# 5) Внутри нужного нам блока, находим все атрибуты 'a', на выходе получаем список тегов
# 6) Чтобы обрезать теги применяем .text

url = 'http://stepik-parsing.ru/html/index4_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

# Циклом проходим по каждой странице, для этого создаём переменную url

for i in range(1, int(pagen) + 1):
    url = f'http://stepik-parsing.ru/html/index4_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # получаем название, цену и список характеристик товара. Характеристики разбиваем по переносу строки,
    # тем самым создавая список

    name = [item.text.strip() for item in soup.find_all('a', class_='name_item')]
    price = [i.text for i in soup.find_all('p', class_='price')]
    description = [i.text.split('\n') for i in soup.find_all('div', class_='description')]

    # в данном цикле собираем карточку товара
    for name, description, price in zip(name, description, price):
        result = []
        flatten = name, [x.split(':')[1].strip() for x in description if x], price
        for x in flatten:
            #распаковываем характеристики из списка и создаеём новый список без вложенных значений
            if isinstance(x, list):
                for i in x:
                    result.append(i)
            else:
                result.append(x)
        with open('res.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(result)

print('Файл res.csv создан')
