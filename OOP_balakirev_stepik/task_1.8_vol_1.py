class Data:
    def __init__(self, data, IP):
        self.data = data
        self.ip = IP


class Server:
    ip = 1

    def __init__(self):
        self.ip = Server.ip
        self.routers = set()
        self.buffer = []
        Server.ip += 1

    def send_data(self, data):
        [router.buffer.append(data) for router in self.routers]

    def get_ip(self):
        return self.ip

    def get_data(self):
        return [self.buffer.pop(0) for i in range(len(self.buffer))]


class Router:

    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers.update({server.ip: server})
        server.routers.add(self)

    def unlink(self, server):
        del self.servers[server.ip]

    def send_data(self):
        for i in range(len(self.buffer)):
            data = self.buffer.pop()
            self.servers[data.ip].buffer.append(data)


# создали роутер
router_1 = Router()

# создали серверы
output_server_1 = Server()
output_server_2 = Server()
input_server_1 = Server()
input_server_2 = Server()

# привязали серверы к роутеру
router_1.link(output_server_1)
router_1.link(output_server_2)
router_1.link(input_server_1)
router_1.link(input_server_2)

# отправили данные на роутер
output_server_1.send_data(Data('First data to send server_1', input_server_1.ip))
output_server_1.send_data(Data('Second data to send server_1', input_server_1.ip))
output_server_1.send_data(Data('Second data to send', input_server_2.ip))
print('Роутер перед отправкой', router_1.buffer)

# отправляем все пакеты данных с роутера на принимающие серверы
router_1.send_data()

print('Роутер после отправки', router_1.buffer)
print(input_server_1.buffer)
print(input_server_2.buffer)

print(input_server_1.get_data())
