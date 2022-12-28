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
