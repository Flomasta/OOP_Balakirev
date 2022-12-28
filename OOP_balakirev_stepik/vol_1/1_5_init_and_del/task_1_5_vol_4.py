class TriangleChecker:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def is_triangle(self):
        self.coordinates = [self.a, self.b, self.c]
        if any(not isinstance(i, int) or i <= 0 for i in self.coordinates):
            return 1
        elif max(self.coordinates) >= sum(self.coordinates) - max(self.coordinates):
            return 2
        else:
            return 3


a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
