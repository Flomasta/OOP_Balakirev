import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 2222))
server.listen(10)
while True:
    client_socket, address = server.accept()
    while True:
        data = client_socket.recv(1024)
        if not data or data == 'close': break
        client_socket.send(data)

    client_socket.close()
