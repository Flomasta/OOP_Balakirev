from time import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters = {(k, v.__name__): None for k, v in enumerate((Mechanical, Aragon, Calcium), 1)}

    def add_filter(self, slot_num, filter):
        key = (slot_num, type(filter).__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter

    def remove_filter(self, slot_num):
        for i in self.filters:
            if slot_num in i:
                self.filters[i] = None

    def get_filters(self):
        return tuple(self.filters.values())

    def water_on(self):
        # при заполненных слотах вернёт пустой список, что равносильно True
        return all([i for i in self.filters.values() if i is None or 0 > time() - i.date > self.MAX_DATE_FILTER])


class Mechanical:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


class Aragon:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date


class Calcium:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time()))
my_water.add_filter(2, Aragon(time()))
w = my_water.water_on()  # False
print(w)
my_water.add_filter(3, Calcium(time()))
w = my_water.water_on()  # True
print(w)
print(my_water.get_filters())
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time()))  # добавление в "чужой" слот также невозможно
print(my_water.get_filters())

# п
