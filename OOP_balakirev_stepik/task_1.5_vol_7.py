
class Cart:
    def __init__(self, goods=[]):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, idx):
        if 0 <= idx < len(self.goods):
            del self.goods[idx]

    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Item):
    pass


class TV(Item):
    pass


class Notebook(Item):
    pass


class Cup(Item):
    pass

gd = [TV('samsung', '100'), TV('toshiba', '200'), Table('ikea', '1000'), Notebook('sony', '900'),
      Notebook('acer', '450'), Cup('gus_chrustalny', '999')]
cart = Cart(gd)

print(cart.get_list())
cart.remove(1)
print(cart.get_list())
