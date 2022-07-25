class Circle:

    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value

    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        self.__radius = value

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    radius = property(get_radius, set_radius)

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            if key == '_Circle__radius' and value > 0 or key != '_Circle__radius':
                return super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False


c = Circle(1, 2, 3)

circle = Circle(10.5, 7, 22)
circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
print(circle.radius)
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует
print(res)

'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/vOh4gzHnMWg

Подвиг 8. Объявите класс Circle (окружность), объекты которого должны создаваться командой:

circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности
В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:

__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):

x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.

При изменении значений приватных атрибутов через объекты-свойства нужно дополнительно проверять, что присваиваемые значения - числа (целые или вещественные). Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля). Сделать это нужно через магические методы. При некорректных переданных значениях, прежние значения меняться не должны (исключений никаких генерировать при этом не нужно).

Если присваиваемое значение не числовое, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.

Пример использования класса (эти строчки в программе писать не нужно):

circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
P.S. На экран ничего выводить не нужно. 
'''
