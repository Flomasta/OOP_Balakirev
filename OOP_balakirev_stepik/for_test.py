class NewList:
    def __init__(self, lst=None):
        if lst is None:
            self.lst = []
        elif isinstance(lst, list):
            self.lst = lst
        else:
            raise TypeError('Выражение должно быть списком!')

    def get_list(self):
        return self.lst

    def __sub__(self, other):
        lst = self.lst.copy()
        data = other
        if isinstance(data, list):
            data = NewList(other)
        if isinstance(data, NewList):
            for i in data.lst:
                if i in lst:
                    if type(i) == type(lst[lst.index(i)]):
                        lst.remove(i)
                    else:
                        for k, v in enumerate(lst):
                            if type(i) == type(v) and i == v:
                                del lst[k]
                                break
            return NewList(lst)

        else:
            return TypeError('Неверный тип данных!')

    def __isub__(self, other):
        if isinstance(other, NewList):
            self.lst = self.__sub__(other).lst
            return self

    def __rsub__(self, other):
        return NewList(other) - self.get_list()


# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2
#
# lst2 = NewList([0, 1, 2, 3, True])
# res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
#
# print(res_1)
# print(lst1.lst)
# print(res_2)
# print(res_4)
# print(lst1.get_list())
#
# lst = NewList()
# lst1 = NewList([0, 1, -3.4, "abc", True])
# lst2 = NewList([1, 0, True])
# res1 = lst1 - lst2  # [-3.4, "abc"]
# print(res1.get_list())
lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

print(lst1.get_list())  # [0, 1, -3.4, "abc", True]
print(lst.get_list())  # []
print('*' * 100)

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

print(res1.get_list())  # [-3.4, "abc"]
print(res2.get_list())  # [1, -3.4, "abc"]
print(res3.get_list())  # [2, 3, 4.5]
print(lst1.get_list())  # [-3.4, "abc"]

print('*' * 100)

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
print(res.get_list())  # [0, 5.0, 1, True, -7.87]
print('*' * 100)

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]

print(res_4.get_list())  # [1, 2]
