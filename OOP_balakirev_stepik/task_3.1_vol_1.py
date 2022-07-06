class Book:
    def __init__(self, title, author, pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == 'title' and isinstance(value, str):
            self.__dict__[key] = value
        elif key == 'author' and isinstance(value, str):
            self.__dict__[key] = value
        elif key == 'pages' and isinstance(value, int):
            self.__dict__[key] = value
        elif key == 'year' and isinstance(value, int):
            self.__dict__[key] = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
print(book.title)
print(book.author)
print(book.pages)
print(book.year)
