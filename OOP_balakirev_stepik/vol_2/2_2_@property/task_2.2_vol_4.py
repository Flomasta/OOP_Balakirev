class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_info(cls, data):
        if cls.MIN_COORD < data < cls.MIN_COORD:
            return True

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_coord):
        if self.__check_info(x_coord):
            self.__x = x_coord

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_coord):
        if self.__check_info(y_coord):
            self.__x = y_coord

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/q_8BdpVWbyE
#
# Подвиг 7. Объявите класс RadiusVector2D, объекты которого должны создаваться командами:
#
# v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
# v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
# v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
# В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:
#
# __x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).
#
# В классе RadiusVector2D необходимо объявить два объекта-свойства:
#
# x - для изменения и считывания локального атрибута __x;
# y - для изменения и считывания локального атрибута __y.
#
# При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
#
# - значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
#
# Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0). Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.
#
# Также в классе RadiusVector2D необходимо объявить статический метод:
#
# norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D (квадратическая норма вектора: x*x + y*y).
#
# P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
