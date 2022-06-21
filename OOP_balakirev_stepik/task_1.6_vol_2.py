class SingletonFive:
    __counter = 0
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__counter < 5:
            cls.__counter += 1
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
print(objs[0])
print(objs[1])
print(objs[2])
print(objs[3])
print(objs[4])
print(objs[5])
