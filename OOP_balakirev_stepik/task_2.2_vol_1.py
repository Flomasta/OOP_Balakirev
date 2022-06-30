class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, car_model):
        if isinstance(car_model, str) and 2 <= len(car_model) <= 100:
            self.__model = car_model


car = Car()

car.model = 'Toyota'
