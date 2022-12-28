class PositiveNumber:
    # __get__ возвращает значение переменной, служит в качестве геттера
    # self - объект переменной, в нашем случае amount
    # instance - объект, в котором находится дескриптор. В нашем случае order.
    # owner - класс объекта order --> Order()

    def __get__(self, instance, owner):
        return getattr(instance, self.var_name)

    # сеттер, instance - order, value - значение
    def __set__(self, instance, value):
        setattr(instance, self.var_name, value)

    # необходима для указания имени свойства. Мы вызываем от одного объекта order (instance)  дескрипоторы
    # cost и  amount. И каждый раз определяя его, например order.amount = 10, значение будет меняться также и у
    # свойства cost. Т.е order.cost == order.amount. Чтобы избежать подобного поведения используем __set_name__
    # owner - класс Order
    # name - имя свойства

    # вызывается автоматически при создании экземпляра класса
    # self - ссылка на объект класса PositiveNumber(), amount или cost
    # owner - ссылка на класс Order
    # name = имя переменной, котому присваивается экземпляр класса amount или cost
    # self.name - локальное свойство экземпляра класса дескриптора
    def __set_name__(self, owner, name):
        self.var_name = '_' + name


class Order:
    product = 'Milk'
    _amount = PositiveNumber()
    _cost = PositiveNumber()


order = Order()
