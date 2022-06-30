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
