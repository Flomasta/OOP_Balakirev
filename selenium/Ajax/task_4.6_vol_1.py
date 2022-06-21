import requests
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
categories = ['main', 'regional', 'sport', 'lady', 'auto', 'cinema', 'hitech', 'games', 'deti', 'health', 'dom', 'pets']

for category in categories:
    url = f"https://mail.ru/?news={category}&json=1"
    response = requests.get(url=url, headers=headers).json()
    print(*[i['title'] for i in response['data']['news']['general']],sep = '\n')
    print('*' * 50)
    time.sleep(3)
