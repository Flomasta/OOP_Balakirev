
class Cart:
    def __init__(self, goods=[]):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, idx):
        if 0 <= idx < len(self.goods):
            del self.goods[idx]

    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Item):
    pass


class TV(Item):
    pass


class Notebook(Item):
    pass


class Cup(Item):
    pass

gd = [TV('samsung', '100'), TV('toshiba', '200'), Table('ikea', '1000'), Notebook('sony', '900'),
      Notebook('acer', '450'), Cup('gus_chrustalny', '999')]
cart = Cart(gd)

print(cart.get_list())
cart.remove(1)
print(cart.get_list())


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HbtVara1GPI
#
# Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:
#
# cart = Cart()
# Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.
#
# В классе Cart объявить методы:
#
# add(self, gd) - добавление в корзину товара, представленного объектом gd;
# remove(self, indx) - удаление из корзины товара по индексу indx;
# get_list(self) - получение из корзины товаров в виде списка из строк:
#
# ['<наименовние_1>: <цена_1>',
#  '<наименовние_2>: <цена_2>',
#  ...
#  '<наименовние_N>: <цена_N>']
#
# Объявите в программе следующие классы для описания товаров:
#
# Table - столы;
# TV - телевизоры;
# Notebook - ноутбуки;
# Cup - кружки.
#
# Объекты этих классов должны создаваться командой:
#
# gd = ИмяКласса(name, price)
# Каждый объект классов товаров должен содержать локальные свойства:
#
# name - наименование;
# price - цена.
#
# Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
#
# P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
