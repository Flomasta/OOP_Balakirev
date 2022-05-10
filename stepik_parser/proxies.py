from random import choice
import requests

url = 'http://httpbin.org/ip'

with open('proxy.txt') as file:
    proxy_file = file.read().split('\n')
    for _ in range(1000):
        try:
            ip = choice(proxy_file).strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'http://{ip}'
            }
            response = requests.get(url=url, proxies=proxy,timeout = 1)
            print(response.json(), 'Success connection')
        except Exception as _ex:
            continue
