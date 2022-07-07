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
