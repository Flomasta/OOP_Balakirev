import requests

url = 'http://httpbin.org/gh/'

response = requests.get(url)
print(response.status_code)
