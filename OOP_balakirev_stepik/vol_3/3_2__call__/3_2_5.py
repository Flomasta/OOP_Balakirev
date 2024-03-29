class RenderList:
    def __init__(self, type_list):
        self.type_list = self.__check_type_list(type_list)
        self.nl = '\n'

    @classmethod
    def __check_type_list(cls, data):
        return data if data in ('ul', 'ol') else 'ul'

    def __call__(self, *args, **kwargs):
        return f'<{self.type_list}>\n{self.nl.join(["<li>" + i + "</li>" for i in args[0]])}\n</{self.type_list}>'


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)

print(html)



# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wp4CyhdXcbY
#
# Подвиг 6. Предположим, вам необходимо создать программу по преобразованию списка строк, например:
#
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# в следующий фрагмент HTML-разметки (многострочной строки, кавычки выводить не нужно):
#
# '''<ul>
# <li>Пункт меню 1</li>
# <li>Пункт меню 2</li>
# <li>Пункт меню 3</li>
# </ul>'''
#
# Для этого необходимо объявить класс RenderList, объекты которого создаются командой:
#
# render = RenderList(type_list)
# где type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и "ol" - для списка с тегом <ol>). Если значение параметра type_list другое (не "ul" и не "ol"), то формируется список с тегом <ul>.
#
# Затем, предполагается использовать объект render следующим образом:
#
# html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
# Пример использования класса (эти строчки в программе писать не нужно):
#
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# render = RenderList("ol")
# html = render(lst)
# P.S. На экран ничего выводить не нужно.
