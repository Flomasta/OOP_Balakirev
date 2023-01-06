class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + '__' + name

    def __set__(self, instance, value):
        if instance.check_info(value) and isinstance(value, (int, float)):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return property() if instance is None else instance.__dict__[self.name]


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    # @property
    # def a(self):
    #     return self.__a
    #
    # @a.setter
    # def a(self, a):
    #     if self.check_info(a):
    #         self.__a = a
    #
    # @property
    # def b(self):
    #
    #     return self.__b
    #
    # @b.setter
    # def b(self, b):
    #     if self.check_info(b):
    #         self.__b = b
    #
    # @property
    # def c(self):
    #     return self.__c
    #
    # @c.setter
    # def c(self, c):
    #     if self.check_info(c)
    #         self.__c = c

    @classmethod
    def check_info(cls, data):
        return cls.MIN_DIMENSION <= data <= cls.MAX_DIMENSION

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        else:
            super().__setattr__(key, value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError

print(a, b, c)


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/2iS8qnEK9to
#
# Подвиг 9. Объявите в программе класс Dimensions (габариты) с атрибутами:
#
# MIN_DIMENSION = 10
# MAX_DIMENSION = 1000
#
# Каждый объект класса Dimensions должен создаваться командой:
#
# d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
# и содержать локальные атрибуты:
#
# __a, __b, __c - габаритные размеры (целые или вещественные числа).
#
# Для работы с этими локальными атрибутами в классе Dimensions следует прописать следующие объекты-свойства:
#
# a, b, c - для изменения и считывания соответствующих локальных атрибутов __a, __b, __c.
#
# При изменении значений __a, __b, __c следует проверять, что присваиваемое значение число в диапазоне [MIN_DIMENSION; MAX_DIMENSION]. Если это не так, то новое значение не присваивается (игнорируется).
#
# С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions. При попытке это сделать генерировать исключение:
#
# raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
# Пример использования класса  (эти строчки в программе писать не нужно):
#
# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError
# P.S. В программе нужно объявить только класс Dimensions. На экран ничего выводить не нужно.
