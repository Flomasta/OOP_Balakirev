class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_one):
        if isinstance(next_one, StackObj) or next_one == None:
            self.__next = next_one

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data_):
        self.__data = data_


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if not self.top:
            self.top = obj
            self.prev = self.top
        else:
            self.prev.next = obj
            self.prev = obj

    def pop(self):
        current = self.top
        while current.next.next:
            current = current.next
        current.next = None

    def get_data(self):
        current = self.top
        all_data = []
        while current:
            all_data.append(current.data)
            current = current.next
        return all_data


st = Stack()
a = StackObj("obj1")
b = StackObj("obj2")
c = StackObj("obj3")
st.push(a)
st.push(b)
st.push(c)
# st.pop()
print(st.get_data())


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/mg4b8nhVDKY
#
# Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ
#
# Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов), когда один объект ссылается на следующий и так по цепочке до последнего:
#
#
#
# Для этого объявите в программе два класса:
#
# StackObj - для описания объектов односвязного списка;
# Stack - для управления односвязным списком.
#
# Объекты класса StackObj предполагается создавать командой:
#
# obj = StackObj(данные)
# Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:
#
# __data - ссылка на строку с данными, указанными при создании объекта;
# __next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).
#
# Также в классе StackObj должны быть объявлены объекты-свойства:
#
# next - для записи и считывания информации из локального приватного свойства __next;
# data - для записи и считывания информации из локального приватного свойства __data.
#
# При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None. Если проверка не проходит, то __next остается без изменений.
#
# Класс Stack предполагается использовать следующим образом:
#
# st = Stack() # создание объекта односвязного списка
# В объектах класса Stack должен быть локальный публичный атрибут:
#
# top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).
#
# А в самом классе Stack следующие методы:
#
# push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
# get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления, или пустой список, если объектов нет).
#
# Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):
#
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
