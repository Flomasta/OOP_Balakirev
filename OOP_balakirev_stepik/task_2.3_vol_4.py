class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    def get_things(self):
        return self.__things

    things = property(get_things)

    def add_thing(self, thing):
        current_weight = self.get_total_weight()
        if current_weight + thing.weight < self.max_weight:
            self.things.append(thing)

    def remove_thing(self, indx):
        if len(self.things) > indx:
            del self.things[indx]

    def get_total_weight(self):
        return sum([i.weight for i in self.things])


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
print(bag.things)
bag.remove_thing(1)
w = bag.get_total_weight()
print(bag.things)
print(w)
# for t in bag.things:
#     print(f"{t.name}: {t.weight}")
