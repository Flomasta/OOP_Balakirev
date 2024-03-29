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


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/gmjwMakXk0c
#
# Большой подвиг 10. Объявите два класса:
#
# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером N x N клеток.
#
# С помощью класса Cell предполагается создавать отдельные клетки командой:
#
# c1 = Cell(around_mines, mine)
# Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
#
# around_mines - число мин вокруг клетки (начальное значение 0);
# mine - наличие мины в текущей клетке (True/False);
# fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).
#
#
#
# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
#
# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.
#
# В классе GamePole должны быть также реализованы следующие методы:
#
# init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #).
#
# При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.
#
#     В классе GamePole могут быть и другие вспомогательные методы.
#
#     Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.
#
# P.S. На экран в программе ничего выводить не нужно.
