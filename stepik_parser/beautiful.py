from  bs4 import  BeautifulSoup
import requests
import lxml

# with open('index.html',encoding='utf-8') as file:
#     soup = BeautifulSoup(file,'lxml')
#     print(soup)
url = 'http://stepik-parsing.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
div = soup.find_all('p',class_ ='price' )
lst = []
for txt in div:
  lst.append(int(txt.text.replace('руб','')))
print(sum(lst))
