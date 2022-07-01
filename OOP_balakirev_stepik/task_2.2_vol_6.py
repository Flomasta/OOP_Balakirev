class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0),) + args)

    def get_path(self):
        return self.coords[1:]

    def get_length(self):
        res = 0
        for i in range(1, len(self.coords)):
            x0 = self.coords[i].x
            y0 = self.coords[i].y
            x = self.coords[i - 1].x
            y = self.coords[i - 1].y
            res += ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5

        return res

    def add_line(self, line):
        self.coords.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
print(p.get_length())
