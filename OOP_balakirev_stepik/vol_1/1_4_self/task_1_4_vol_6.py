lst = ['tree – дерево', 'car – машина', 'car – автомобиль', 'leaf – лист', 'river – река', 'go – идти', 'go – ехать',
       'go – ходить', 'milk – молоко']
lst = [v.split(' – ') for v in lst]


class Translator:
    def __init__(self):
        self.d = {}

    def add(self, eng, rus):
        self.eng = eng
        self.rus = rus
        if self.d.get(self.eng):
            self.d[self.eng].append(self.rus)
        else:
            self.d.update({self.eng: [self.rus]})

    def remove(self, eng):
        if self.d.get(self.eng):
            del self.d[eng]

    def translate(self, eng):
        return self.d.get(eng)


tr = Translator()
[tr.add(i[0], i[1]) for i in lst]

tr.remove('car')
print(*tr.translate('go'))
