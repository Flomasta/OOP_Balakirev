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
