import requests

# response = requests.get(url= 'https://jsonplaceholder.typicode.com/todos/')
# print(response.text)

response = requests.get(url='http://httpbin.org/')
print(response)
help(response)

# response = requests.get(url='http://httpbin.org/image/jpeg')
# with open('image.jpeg', 'wb') as file:
#     file.write(response.content)
