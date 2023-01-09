class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class ObjList:
    data = Descriptor()
    prev = Descriptor()
    next = Descriptor()

    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class LinkedList:
    head = Descriptor()
    tail = Descriptor()

    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head == self.tail == None:
            self.head = self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def remove_obj(self, indx):
        if indx < len(self):
            obj = self.head
            counter = 0
            while counter != indx:
                counter += 1
                obj = obj.next
            if obj == self.head and obj == self.tail:
                self.head = self.tail = None

            elif obj == self.tail:
                obj.prev.next = None
                self.tail = obj.prev

            elif obj == self.head:
                obj.next.prev = None
                obj.next = self.head.next
                self.head = obj.next

            else:
                obj.prev.next = obj.next
                obj.next.prev = obj.prev

    def __len__(self):
        obj = self.head
        counter = 0
        while obj is not None:
            counter += 1
            obj = obj.next
        return counter

    def __call__(self, indx, *args, **kwargs):
        if 0 <= indx < len(self):
            current = obj = self.head
            counter = 0
            while counter <= indx:
                counter += 1
                current = obj
                obj = obj.next
            return current.data


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
print(len(linked_lst))  # 3
print(linked_lst(0))
print(linked_lst(1))
print(linked_lst(2))
linked_lst.remove_obj(1)

print(len(linked_lst))  # 2
print(linked_lst(0))  # Sergey
print(linked_lst(1))  # Python
print(linked_lst(2))  # None
linked_lst.add_obj(ObjList("Python ООП"))
print(len(linked_lst))  # 3
print(linked_lst(2))  # Python ООП

print(len(linked_lst))

# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
#
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1)  # s = Balakirev
#
# print(n)
# print(s)

#
# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6-xKuQp9b7Y
#
# Теория по двусвязным спискам (при необходимости): https://youtu.be/0sTH9EwXT1I
#
# Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:
#
#
#
# Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:
#
# obj = ObjList(data)
# где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:
#
# __data - ссылка на строку с данными;
# __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
# __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).
#
# В свою очередь, объекты класса LinkedList должны создаваться командой:
#
# linked_lst = LinkedList()
# и содержать локальные атрибуты:
#
# head - ссылка на первый объект связного списка (если список пуст, то head = None);
# tail - ссылка на последний объект связного списка (если список пуст, то tail = None).
#
# А сам класс содержать следующие методы:
#
# add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
# remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.
#
# Также с объектами класса LinkedList должны поддерживаться следующие операции:
#
# len(linked_lst) - возвращает число объектов в связном списке;
# linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# P.S. На экран в программе ничего выводить не нужно.
