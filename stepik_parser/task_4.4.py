from  bs4 import  BeautifulSoup
import requests


url = 'http://stepik-parsing.ru/html/hdd/4/4_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
old_price = soup.find('span', {'id': 'old_price'}).text
actual_price = soup.find('span', {'id': 'price'}).text

old_price = int(old_price.replace('руб',''))
actual_price = int(actual_price.replace('руб',''))

percent = (old_price - actual_price)*100 / old_price
print(percent)
