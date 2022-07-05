class FloatValue:

    @classmethod
    def check_value(cls, num):
        if isinstance(num, float):
            return True

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if self.check_value(value):
            instance.__dict__[self.name] = value
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.num = (i for i in range(1, self.n * self.m + 1))
        self.cells = [[Cell(float(next(self.num))) for i in range(n)] for j in range(m)]


table = TableSheet(3, 5)

for i in table.cells:
    for j in i:
        print(j.value)
