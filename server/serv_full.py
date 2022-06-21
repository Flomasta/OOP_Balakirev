import socket

# данный сокет может быть потенциально и клиенским и серверным

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# создаём серверыный сокет, т.к сокет с адресом  и портом является сервером. Лучше указать 4-x значное число порта
server.bind(('127.0.0.3', 2222))
# указываем количество входящих запросов, которые будут приняты операционной системой и поставлены в режим ожидания,
# остальные запросы будут сброшены
server.listen(10)
print('starting...')
# принимаем отправленные запросы, ожидаем клиента  и получаем его адрес

client_socket, address = server.accept()
# получаем данные пользователя

data = client_socket.recv(1024).decode('utf-8')
# отправляем  браузеру заголовки и данные
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n'
content = 'Well done,bro!'.encode('utf-8')
client_socket.send(HDRS.encode('utf-8') + content)
print(data)
print('it\'s all done')
client_socket.close()
