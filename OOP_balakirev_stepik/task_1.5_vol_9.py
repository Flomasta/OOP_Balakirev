import random
import copy


class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:

    def __init__(self, n, m):
        self.pole = [[Cell() for i in range(n + 2)] for j in range(n + 2)]
        self.m = m
        self.n = n
        self.init()

    def init(self):
        self.counter = 0
        self.new_pole = copy.deepcopy(self.pole)
        while self.counter < self.m:
            x, y = random.randint(1, self.n), random.randint(1, self.n)
            cell_for_mine = self.new_pole[x][y]
            if not cell_for_mine.mine:
                cell_for_mine.mine = True
                self.counter += 1
        for i in range(1, self.n):
            for j in range(1, self.n):
                self.new_pole[i][j].around_mines = sum(
                    [self.new_pole[i - 1][j - 1].mine + self.new_pole[i - 1][j].mine +
                     self.new_pole[i - 1][j + 1].mine + self.new_pole[i][j - 1].mine +
                     self.new_pole[i][j + 1].mine + self.new_pole[i + 1][j - 1].mine +
                     self.new_pole[i + 1][j].mine + self.new_pole[i + 1][j + 1].mine])

    def show(self):
        for row in self.new_pole:
            for item in row:
                if item.mine and item.fl_open:
                    print('*', end='')
                elif item.fl_open:
                    print(1, end='')
                else:
                    print('#', end='')
            print()


n = 5
m = 4

pole_game = GamePole(n, m)

pole_game.show()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if pole_game.new_pole[i][j].mine:
            print(i, j)
            print(pole_game.new_pole[i][j].mine)

print('*' * 50)

pole_game.init()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if pole_game.new_pole[i][j].mine:
            print(i, j)
            print(pole_game.new_pole[i][j].mine)
