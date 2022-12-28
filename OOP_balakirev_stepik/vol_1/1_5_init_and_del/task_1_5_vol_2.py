class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) for i in range(1, 1001) if i % 2 != 0]
points[1].color = 'yellow'

print(points[0].x)
