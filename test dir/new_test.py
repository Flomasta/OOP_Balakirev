class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def add_obj(self, obj):
        if self.head:
            temp = obj
            temp.set_prev(self.tail)
            self.tail.set_next(temp)
            self.tail = temp
        else:
            self.head = obj
            self.tail = obj

    def remove_obj(self):
        if self.tail.get_prev():
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail = None
            self.head = None

    def get_data(self):
        result = []
        obj = self.head
        while obj:
            result.append(obj.get_data())
            obj = obj.get_next()
        return result

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.add_obj(ObjList("данные 4"))
lst.add_obj(ObjList("данные 5"))

res = lst.get_data()
