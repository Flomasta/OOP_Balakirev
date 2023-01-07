class InputDigits:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        data = self.fn()
        return [int(i) for i in data.split()]


@InputDigits
def input_dg():
    return input()


res = input_dg()
print(res)

# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/EEzEodYvoXc
#
# Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе строки из целых чисел, записанных через пробел, например:
#
# "12 -5 10 83"
#
# на выходе возвращался список из целых чисел:
#
# [12, -5, 10, 83]
#
# Назовите декорированную функцию input_dg и вызовите ее командой:
#
# res = input_dg()
# P.S. На экран ничего выводить не нужно.
