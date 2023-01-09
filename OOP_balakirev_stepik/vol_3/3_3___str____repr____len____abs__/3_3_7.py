import time


class DeltaClock:
    def __init__(self, clock_1, clock_2):
        self.clock_1 = clock_1
        self.clock_2 = clock_2

    def __str__(self):
        diff = len(self)
        return time.strftime('%H: %M: %S', time.gmtime(diff))

    def __len__(self):
        diff = self.clock_1.get_time() - self.clock_2.get_time()
        return 0 if diff < 0 else diff


class Clock:
    def __init__(self, *args):
        self.hour = args[0]
        self.minutes = args[1]
        self.seconds = args[2]

    def get_time(self):
        return self.hour * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)
len_dt = len(dt)  # 5400
print(len_dt)



# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/V7SV1pOWyEY
#
# Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:
#
# dt = DeltaClock(clock1, clock2)
# где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться командой:
#
# clock = Clock(hours, minutes, seconds)
# где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).
#
# В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):
#
# get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).
#
# После создания объекта dt класса DeltaClock, с ним должны выполняться команды:
#
# str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
# print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# Если разность получается отрицательной, то разницу времен считать нулевой.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt) # 01: 30: 00
# len_dt = len(dt) # 5400
# Обратите внимание, добавляется незначащий ноль, если число меньше 10.
#
# P.S. На экран ничего выводить не нужно, только объявить классы.
