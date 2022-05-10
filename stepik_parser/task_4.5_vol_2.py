from  bs4 import  BeautifulSoup
import requests

articles = []
for i in range(1,33):
    url = f'http://stepik-parsing.ru/html/mouse/3/3_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    article = int(soup.find('p',class_ = 'article').text.split()[1])
    articles.append(article)
print(sum(articles))
