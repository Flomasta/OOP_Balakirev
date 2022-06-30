import random


class BaseClass:

    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Line(BaseClass):
    pass


class Rect(BaseClass):
    pass


class Ellipse(BaseClass):
    pass


objects = [Line, Rect, Ellipse]

elements = [random.choice(objects)(*[random.randint(1, 100) for j in range(4)]) for i in range(217)]
elements = [Line(0, 0, 0, 0) if isinstance(i, Line) else i for i in elements]

print(type(elements[0]) == Rect)
