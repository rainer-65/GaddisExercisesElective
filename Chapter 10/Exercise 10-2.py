# Create a class Car

def car_test():
    # Create a Car object
    car = Car("2023", "Tesla")

    # Accelerate the car five times
    for _ in range(5):
        car.accelerate()
        print("Current speed after acceleration:", car.get_speed())

    # Brake the car five times
    for _ in range(5):
        car.brake()
        print("Current speed after braking:", car.get_speed())


class Car:
    # Create data attributes for class Car
    # __init__ method that accept the car’s year model and make as arguments.
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # accelerate method should add 5 to the speed data
    # attribute each time it is called.
    def accelerate(self):
        self.__speed += 5

    # brake method should subtract 5 from the
    # speed data attribute each time it is called.
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5

    # get_speed method should return the current speed.
    def get_speed(self):
        return self.__speed


if __name__ == '__main__':
    car_test()
