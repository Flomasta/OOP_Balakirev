from  bs4 import  BeautifulSoup
import requests


url = 'http://stepik-parsing.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')

pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

urls = [f'http://stepik-parsing.ru/html/index3_page_{i}.html' for i in range(1,int(pagen)+1)]

items = []
for i in urls:
    current_url = i
    response = requests.get(url=current_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    items_from_page = soup.find_all('a', class_ = 'name_item' )
    items.append( [i.text for i in items_from_page])

print(items)
