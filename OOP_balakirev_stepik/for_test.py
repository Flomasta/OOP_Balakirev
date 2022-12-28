class Translator:

    def add(self, eng, rus):
        self.__dict__.setdefault(eng, []).append(rus)

    def remove(self, eng):
        if self.__dict__.get(eng):
            delattr(self, eng)

    def translate(self, eng):
        return self.__dict__.get(eng)


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
