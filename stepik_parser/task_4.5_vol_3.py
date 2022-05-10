from bs4 import BeautifulSoup
import requests

prices = []
links= []
amount = []
url = 'http://stepik-parsing.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

domain = 'http://stepik-parsing.ru/html'
categories = [domain + link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]
print(categories)

for i in range(1,len(categories)+1):
    url_cat = f'http://stepik-parsing.ru/html/index{i}_page_1.html'
    response = requests.get(url=url_cat)
    response.encoding = 'utf-8'
    soup_cat = BeautifulSoup(response.text, 'lxml')
    pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

    for j in range(1,int(pagen)+1):
         pagen_url = f'http://stepik-parsing.ru/html/index{i}_page_{j}.html'
         response = requests.get(url=pagen_url)
         response.encoding = 'utf-8'
         soup_pagen = BeautifulSoup(response.text, 'lxml')
         cat_links = soup_pagen.find_all('a', class_ = 'name_item')
         for item in cat_links:
             links.append(domain+'/'+item['href'])

for link in links:
    item_url = link
    response = requests.get(url=item_url)
    response.encoding = 'utf-8'
    soup_url = BeautifulSoup(response.text, 'lxml')
    in_stock = int(soup_url.find('span', {'id': 'in_stock'}).text.split()[-1])
    price = int(soup_url.find('span', {'id': 'price'}).text.split()[0])
    summ = in_stock*price
    amount.append(summ)
print(sum(amount))
