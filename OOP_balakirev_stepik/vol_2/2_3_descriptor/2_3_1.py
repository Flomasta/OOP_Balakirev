class FloatValue:

    @classmethod
    def check_value(cls, num):
        if isinstance(num, float):
            return True

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if self.check_value(value):
            instance.__dict__[self.name] = value
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.num = (i for i in range(1, self.n * self.m + 1))
        self.cells = [[Cell(float(next(self.num))) for i in range(n)] for j in range(m)]

table = TableSheet(3, 5)


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/xHINhSQJh5c
#
# Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать исключение командой:
#
# raise TypeError("Присваивать можно только вещественный тип данных.")
# Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться командой:
#
# cell = Cell(начальное значение ячейки)
# Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:
#
# table = TableSheet(N, M)
# Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект value (начальное значение должно быть 0.0).
#
# В каждом объекте класса TableSheet должен формироваться локальный атрибут:
#
# cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).
#
# Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).
#
# P.S. На экран в программе выводить ничего не нужно.
