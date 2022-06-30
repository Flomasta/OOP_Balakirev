class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        if isinstance(obj, ListObject):
            self.next_obj = obj


data = ['1. Первые шаги в ООП',
        '1.1 Как правильно проходить этот курс',
        '1.2 Концепция ООП простыми словами',
        '1.3 Классы и объекты. Атрибуты классов и объектов',
        '1.4 Методы классов. Параметр self',
        '1.5 Инициализатор init и финализатор del',
        '1.6 Магический метод new. Пример паттерна Singleton',
        '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
head_obj = ListObject(data[0])
obj = head_obj
for i in range(1, len(data)):
    new_obj = ListObject(data[i])
    obj.link(new_obj)
    obj = new_obj

nxt = head_obj
print(nxt.data)
while nxt.next_obj != None:
    nxt = nxt.next_obj
    print(nxt.data)
