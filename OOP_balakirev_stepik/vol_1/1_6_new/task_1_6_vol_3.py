TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
        setattr(instance, 'name', args[0])
        return instance

    def __init__(self, name):
        self.name = name


dg = Dialog(1234)
print(type(dg))
print(dg.name)
print(dg.__dict__)
print(DialogWindows.__dict__)


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/sX_uP7GVqkc
#
# Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:
#
# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
# Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:
#
# dlg = Dialog(<название>)
# Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
#
# Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 и объекты класса DialogLinux, если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS может меняться в последующих строчках программы. Имейте это в виду, при объявлении класса Dialog.
#
# P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.
