from math import sqrt


class Descriptor:

    @classmethod
    def __check_info(cls, data):
        return isinstance(data, (int, float))

    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __set__(self, instance, value):

        if self.name in ('_Complex__real', '_Complex__img') and self.__check_info(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Неверный тип данных.")

    def __get__(self, instance, owner):
        # код для того, чтобы принял степик
        if instance is None:
            return property()
        return instance.__dict__[self.name]
        # код для стандартного решения
        # return instance.__dict__[self.name]


class Complex:
    real = Descriptor()
    img = Descriptor()

    def __init__(self, real=None, img=None):
        self.real = real
        self.img = img

    @property
    def test(self):
        return self.__test

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4

c_abs = abs(cmp)
print(c_abs)

# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/t8KuHjY71-o
#
# Подвиг 6. Объявите класс с именем Complex для представления и работы с комплексными числами. Объекты этого класса должны создаваться командой:
#
# cm = Complex(real, img)
# где real - действительная часть комплексного числа (целое или вещественное значение); img - мнимая часть комплексного числа (целое или вещественное значение).
#
# Объявите в этом классе следующие объекты-свойства (property):
#
# real - для записи и считывания действительного значения;
# img - для записи и считывания мнимого значения.
#
# При записи новых значений необходимо проверять тип передаваемых данных. Если тип не соответствует целому или вещественному числу, то генерировать исключение командой:
#
# raise ValueError("Неверный тип данных.")
# Также с объектами класса Complex должна поддерживаться функция:
#
# res = abs(cm)
# возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img) - корень квадратный от суммы квадратов действительной и мнимой частей комплексного числа).
#
# Создайте объект cmp класса Complex для комплексного числа с real = 7 и img = 8. Затем, через объекты-свойства real и img измените эти значения на real = 3 и img = 4. Вычислите модуль полученного комплексного числа (сохраните результат в переменной c_abs).
#
# P.S. На экран ничего выводить не нужно.
