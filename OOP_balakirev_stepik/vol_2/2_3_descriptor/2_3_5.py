class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for k, v in enumerate(self.items):
            if v.uid == indx:
                del self.items[k]
                break


class Telecast:

    def __init__(self, id, name, duration):
        self.__uid = id
        self.__name = name
        self.__duration = duration

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, value):
        self.__uid = value


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/45q8BT03c_U
#
# Подвиг 10 (на повторение). Необходимо написать программу для представления и управления расписанием телевизионного вещания. Для этого нужно объявить класс TVProgram, объекты которого создаются командой:
#
# pr = TVProgram(название канала)
# где название канала - это строка с названием телеканала.
#
# В каждом объекте класса TVProgram должен формироваться локальный атрибут:
#
# items - список из телепередач (изначально список пуст).
#
# В самом классе TVProgram должны быть реализованы следующие методы:
#
# add_telecast(self, tl) - добавление новой телепередачи в список items;
# remove_telecast(self, indx) - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).
#
# Каждая телепередача должна описываться классом Telecast, объекты которого создаются командой:
#
# tl = Telecast(порядковый номер, название, длительность)
# где порядковый номер - номер телепередачи в сетке вещания (от 1 и далее); название - наименование телепередачи; длительность - время телепередачи (в секундах - целое число).
#
# Соответственно, в каждом объекте класса Telecast должны формироваться локальные приватные атрибуты:
#
# __id - порядковый номер (целое число);
# __name - наименование телепередачи (строка);
# __duration - длительность телепередачи в секундах (целое число).
#
# Для работы с этими приватными атрибутами в классе Telecast должны быть объявлены соответствующие объекты-свойства (property):
#
# uid - для записи и считывания из локального атрибута __id;
# name - для записи и считывания из локального атрибута __name;
# duration - для записи и считывания из локального атрибута __duration.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# pr = TVProgram("Первый канал")
# pr.add_telecast(Telecast(1, "Доброе утро", 10000))
# pr.add_telecast(Telecast(2, "Новости", 2000))
# pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
# for t in pr.items:
#     print(f"{t.name}: {t.duration}")
# P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
