lst_in = '1 Сергей 35 120000'


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        for i in data:
            DataBase.lst_data.append({k: v for k, v in zip(DataBase.FIELDS, i.split(' '))})

    def select(self, a, b):
        return DataBase.lst_data[a:b + 1]


db = DataBase()
print(db.insert(lst_in))
