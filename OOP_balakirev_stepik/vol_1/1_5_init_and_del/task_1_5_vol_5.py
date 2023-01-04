class Graph():
    err = 'Отображение данных закрыто'

    def __init__(self, data, is_show=True):
        self.data = data
        self.is_show = is_show

    def check_data(self, data, is_show):
        return data if is_show else Graph.err

    def set_data(self, data):
        self.data = data

    def show_table(self):
        self.lst_to_str = ' '.join([str(i) for i in self.data])
        return self.check_data(self.lst_to_str, self.is_show)

    def show_graph(self):
        return self.check_data(f'Графическое отображение данных: {self.show_table()}', self.is_show)

    def show_bar(self):
        return self.check_data(f'Столбчатая диаграмма: {self.show_table()}', self.is_show)

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))

gr = Graph(data_graph)

print(gr.show_graph())
print(gr.show_table())
print(gr.show_bar())
gr.set_show(False)
print(gr.show_table())
# 8 11 10 -32 0 7 18


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/a3Har3Z_89Q
#
# Подвиг 6. Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:
#
# gr_1 = Graph(data)
# где data - список из числовых данных (данные для графика). При создании каждого экземпляра класса должны формироваться следующие локальные свойства:
#
# data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать копию переданного списка);
# is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);
#
# В этом классе объявите следующие методы:
#
# set_data(self, data) - для передачи нового списка данных в текущий график;
# show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
# show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
# show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
# set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.
#
# Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить сообщение:
#
# "Отображение данных закрыто"
#
# Прочитайте из входного потока числовые данные с помощью команды:
#
# data_graph = list(map(int, input().split()))
# Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show() со значением fl_show = False и вызовите метод show_table(). На экране должны отобразиться две соответствующие строки.
