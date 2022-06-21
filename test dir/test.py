import random


class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:

    def __init__(self, n, m):
        self.pole = [[Cell(0, False) for i in range(n + 2)] for j in range(n + 2)]
        self.m = m
        self.n = n
        self.init()

    def init(self):
        self.counter = 0

        for i in range(self.m):
            while True:
                x, y = random.randint(1, self.n), random.randint(1, self.n)
                if not self.pole[x][y].mine:
                    self.pole[x][y].mine = True
                    break

        for i in range(1, self.n):
            for j in range(1, self.n):
                self.pole[i][j].around_mines = sum(
                    [self.pole[i - 1][j - 1].mine + self.pole[i - 1][j].mine +
                     self.pole[i - 1][j + 1].mine + self.pole[i][j - 1].mine +
                     self.pole[i][j + 1].mine + self.pole[i + 1][j - 1].mine +
                     self.pole[i + 1][j].mine + self.pole[i + 1][j + 1].mine])

    def show(self):
        for row in self.pole:
            for item in row:
                if item.mine and item.fl_open:
                    print('*', end='')
                elif item.fl_open:
                    print(1, end='')
                else:
                    print(0, end='')
            print()


n = 5
m = 4

pole_game = GamePole(n, m)

# pole_game.show()

# for i in range(1, n):
#     for j in range(1, n):
#         if pole_game.new_pole[i][j].mine:
#             a = pole_game.new_pole[i][j].mine
#             print(pole_game.new_pole[i][j].mine)
# print('*' * 50)


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if pole_game.pole[i][j].mine:
            print(i, j)
            b = pole_game.pole[i][j].mine

pole_game.init()

print('-*-' * 50)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if pole_game.pole[i][j].mine:
            print(i, j)
            b = pole_game.pole[i][j].mine
