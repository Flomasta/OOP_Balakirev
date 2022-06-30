class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj
        else:
            self.head = self.tail = obj

    def remove_obj(self):
        if self.tail != None and self.tail.get_prev():
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

        else:
            self.head = None
            self.tail = None

    def get_data(self):
        res = []
        start = self.head
        while start:
            res.append(start.get_data())
            start = start.get_next()
        return res


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList('data_1'))
lst.add_obj(ObjList('data_2'))
lst.add_obj(ObjList('data_3'))
print(lst.get_data())
