import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters = {(k, v.__name__): None for k, v in enumerate((Mechanical, Aragon, Calcium), 1)}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter

    def remove_filter(self, slot_num):

        for i in self.filters.keys():
            if slot_num in i:
                self.filters[i] = None
                break

    def get_filters(self):
        return tuple(self.filters.values())

    def water_on(self):
        end = time.time()
        for i in self.filters.values():
            if i is None:
                return False
            start = i.date
            if end - start > self.MAX_DATE_FILTER:
                return False

        return True


class Filter:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


m = Mechanical(time.time())
a = Aragon(time.time())
c = Calcium(time.time())
g = GeyserClassic()

g.add_filter(3, c)
g.add_filter(1, m)
g.add_filter(2, a)
#
# print(g.filters)
# g.remove_filter(3)
# print(g.filters)
# print(g.get_filters())

print(g.water_on())
