class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if isinstance(new_width, int) and -1 < new_width < 10_001:
            self.__width = new_width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if isinstance(new_height, int) and -1 < new_height < 10_001:
            self.__height = new_height
            self.show()

    def show(self):
        print(f'{self.__title}: {self.get_width}, {self.get_height}')


d = WindowDlg('Диалог 1', 200, 100)

d.height = 210
