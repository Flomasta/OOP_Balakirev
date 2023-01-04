class WindowDlg:
    MIN_NUM = 0
    MAX_NUM = 10_000

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @classmethod
    def check_info(cls, data):
        return type(data) is int and cls.MIN_NUM < data < cls.MAX_NUM

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    def set_width(self, width):
        if self.check_info(width):
            self.__width = width
            self.show()

    def set_height(self, height):
        if self.check_info(height):
            self.__height = height
            self.show()


one = WindowDlg('Диалог 1', 100, 50)

one.show()

one.set_height(150)
