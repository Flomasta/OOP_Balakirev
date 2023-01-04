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

print('Проверяем все ли серверы добавлены, должно быть (4)', len(router_1.servers), router_1.servers)

# отправили данные на роутер
output_server_1.send_data(Data('First data to send server_1', input_server_1.ip))
output_server_1.send_data(Data('Second data to send server_1', input_server_1.ip))
output_server_1.send_data(Data('Second data to send', input_server_2.ip))
print('Роутер перед отправкой', router_1.buffer)

# отправляем все пакеты данных с роутера на принимающие серверы
router_1.send_data()

print('Роутер после отправки', router_1.buffer)
print('буффер первого сервера', input_server_1.buffer)
print('буффер второго сервера', input_server_2.buffer)

print('получаем данные get_data первого сервера', input_server_1.get_data())
print('получаем данные get_data второго сервера', input_server_2.get_data())

print('буффер первого сервера', input_server_1.buffer)
print('буффер второго сервера', input_server_2.buffer)


# Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/26pwwOu_-d0
#
# Время первого испытания. Представьте, что вы получили задание от заказчика. Вас просят реализовать простую имитацию локальной сети, состоящую из набора серверов, соединенных между собой через роутер.
#
#
#
# Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у каждого есть свой уникальный IP-адрес. Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов. Алгоритм следующий. Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3. Для этого, он сначала отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).
#
# Для реализации этой схемы программе предлагается объявить три класса:
#
# Server - для описания работы серверов в сети;
# Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
# Data - для описания пакета информации.
#
# Серверы будут создаваться командой:
#
# sv = Server()
# При этом, уникальный IP-адрес каждого сервера должен формироваться автоматически при создании нового экземпляра класса Server.
#
# Далее, роутер должен создаваться аналогичной командой:
#
# router = Router()
# А, пакеты данных, командой:
#
# data = Data(строка с данными, IP-адрес назначения)
# Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:
#
# link(server) - для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый сервер соединен только с одним роутером);
# unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
# send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после отправки буфер должен очищаться).
#
# И одно обязательное локальное свойство (могут быть и другие свойства):
#
# buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
#
# Класс Server должен содержать свой набор методов:
#
# send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
# get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;
# get_ip() - возвращает свой IP-адрес.
#
# Соответственно в объектах класса Server должны быть локальные свойства:
#
# buffer - список принятых пакетов (объекты класса Data, изначально пустой);
# ip - IP-адрес текущего сервера.
#
# Наконец, объекты класса Data должны содержать два следующих локальных свойства:
#
# data - передаваемые данные (строка);
# ip - IP-адрес назначения.
#
# Пример использования этих классов (эти строчки в программе писать не нужно):
#
# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()
# Ваша задача реализовать классы Router, Server и Data в соответствии с приведенным техническим заданием (ТЗ). Что-либо выводить на экран не нужно.
