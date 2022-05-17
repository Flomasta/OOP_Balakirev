import requests

response = requests.get('http://parsinger.ru/img_download/index.html', stream=True)

for i in range(1,161):
    response = requests.get(f'http://parsinger.ru/img_download/img/ready/{i}.png')
    with open(f'img/img{i}.jpeg', 'wb') as file:
        file.write(response.content)
