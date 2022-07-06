class Shop:
    def __init__(self, name):
        self.goods = []
        self.name = name

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:
    __id = 1
    d = {'name': str,
         'weight': int,
         'price': int,
         'id': int
         }

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product.__id
        Product.__id += 1

    def __setattr__(self, key, value):
        if type(value) == self.d[key] and str(value).find('-'):

            self.__dict__[key] = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))

for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}, {p.id}")
